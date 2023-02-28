import React, { useState, useEffect } from "react";

import { api } from "../apis/api";


const Stocks = () => {
    const [stockData, setStockData] = useState(null);

    useEffect(() => {

        const fetchStocks = async () => {
            try {
                const response = await api.get("/symbols");
                setStockData(response?.data?.symbols);

            } catch(error) {
                console.error(error);
            }
        };

        fetchStocks();
    }, []);

    return stockData?.length ? (
        stockData.map((stock, idx) => {
            return (
                <div className="stock-item" key={idx}>
                    <h1 className="text-center">{stock.name}</h1>
                    <table>
                        <tbody>
                            <tr>
                                <th scope="col">Symbol</th>
                                <td >{stock.symbol}</td>
                                <th scope="col">Position</th>
                                <td className={stock.position === "Gain" ? "td-green" : "td-red"}>{stock.position}</td>
                            </tr>
                            <tr>
                            <th scope="col">Price</th>
                                <td className={stock.position === "Gain" ? "td-green" : "td-red"}>{stock.price}</td>
                                <th scope="col">Last Scraped</th>
                                <td >{stock.date_scraped}</td>
                            </tr>
                            <tr>
                                <th scope="col">Exchange</th>
                                <td >{stock.exchange}</td>
                                <th scope="col">Market Cap (in trillions USD)</th>
                                <td >{stock.market_cap}</td>
                            </tr>
                            <tr>
                                <th scope="col">Dividend Yield</th>
                                <td >{stock.dividend_yield}</td>
                                <th scope="col">Average Volume (in millions)</th>
                                <td >{stock.avg_volume}</td>
                            </tr>
                            <tr>
                                <th scope="col">Today's Close</th>
                                <td >{stock.close_price}</td>
                                <th scope="col">Previous Close</th>
                                <td >{stock.prev_close}</td>
                            </tr>
                            <tr>
                                <th scope="col">Change</th>
                                <td className={stock.position === "Gain" ? "td-green" : "td-red"}>{stock.close_diff}</td>
                                <th scope="col">Change (in %)</th>
                                <td className={stock.position === "Gain" ? "td-green" : "td-red"}>{stock.close_diff_percent}</td>
                            </tr>
                            <tr>
                                <th scope="col">Day Low</th>
                                <td >{stock.day_low}</td>
                                <th scope="col">Year Low</th>
                                <td >{stock.year_low}</td>
                            </tr>
                            <tr>
                                <th scope="col">Day High</th>
                                <td >{stock.day_high}</td>
                                <th scope="col">Year High</th>
                                <td >{stock.year_high}</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            );
        })
    ) : (
        <div> Fetching data... </div>
    );
};

export default Stocks;
