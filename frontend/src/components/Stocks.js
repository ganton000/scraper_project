import React, { useState, useEffect } from "react";

import { api } from "../apis/api";


const Stocks = () => {
    const [stockData, setStockData] = useState([]);

    useEffect(() => {

        const fetchStocks = async () => {
            try {
                const response = await api.get("/symbols");
                console.log(response);
                setStockData(response.data);

            } catch(error) {
                console.error(error);
            }
        };

        fetchStocks();
    }, []);

    return stockData.length ? (
        stockData.map((stock, idx) => {
            return (
                <div className="stock-item" key={idx}>
                    {stock.name}, {stock.price}, {stock.day_low},{" "}
                    {stock.day_high}
                </div>
            );
        })
    ) : (
        <div> Fetching data... </div>
    );
};

export default Stocks;
