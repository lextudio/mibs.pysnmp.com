# SNMP MIB module (MICOM-ISDN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MICOM-ISDN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:43 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(callActiveIndex,
 callActiveSetupTime,
 dialCtlPeerCfgId) = mibBuilder.importSymbols(
    "DIAL-CONTROL-MIB",
    "callActiveIndex",
    "callActiveSetupTime",
    "dialCtlPeerCfgId")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(micom_oscar,) = mibBuilder.importSymbols(
    "MICOM-OSCAR-MIB",
    "micom-oscar")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Micom_isdn_ObjectIdentity = ObjectIdentity
micom_isdn = _Micom_isdn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24)
)
_Configuration_ObjectIdentity = ObjectIdentity
configuration = _Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1)
)
_NvmIsdnBasicRateTable_Object = MibTable
nvmIsdnBasicRateTable = _NvmIsdnBasicRateTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 1)
)
if mibBuilder.loadTexts:
    nvmIsdnBasicRateTable.setStatus("mandatory")
_NvmIsdnBasicRateEntry_Object = MibTableRow
nvmIsdnBasicRateEntry = _NvmIsdnBasicRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 1, 1)
)
nvmIsdnBasicRateEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    nvmIsdnBasicRateEntry.setStatus("mandatory")


class _NvmIsdnBasicRateLineTopology_Type(Integer32):
    """Custom type nvmIsdnBasicRateLineTopology based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pointToMultipoint", 2),
          ("pointToPoint", 1))
    )


_NvmIsdnBasicRateLineTopology_Type.__name__ = "Integer32"
_NvmIsdnBasicRateLineTopology_Object = MibTableColumn
nvmIsdnBasicRateLineTopology = _NvmIsdnBasicRateLineTopology_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 1, 1, 1),
    _NvmIsdnBasicRateLineTopology_Type()
)
nvmIsdnBasicRateLineTopology.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIsdnBasicRateLineTopology.setStatus("mandatory")


class _NvmIsdnBasicRateSignalMode_Type(Integer32):
    """Custom type nvmIsdnBasicRateSignalMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dialup", 1),
          ("leased", 2))
    )


_NvmIsdnBasicRateSignalMode_Type.__name__ = "Integer32"
_NvmIsdnBasicRateSignalMode_Object = MibTableColumn
nvmIsdnBasicRateSignalMode = _NvmIsdnBasicRateSignalMode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 1, 1, 2),
    _NvmIsdnBasicRateSignalMode_Type()
)
nvmIsdnBasicRateSignalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIsdnBasicRateSignalMode.setStatus("mandatory")
_NvmIsdnSignalingTable_Object = MibTable
nvmIsdnSignalingTable = _NvmIsdnSignalingTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 2)
)
if mibBuilder.loadTexts:
    nvmIsdnSignalingTable.setStatus("mandatory")
_NvmIsdnSignalingEntry_Object = MibTableRow
nvmIsdnSignalingEntry = _NvmIsdnSignalingEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 2, 1)
)
nvmIsdnSignalingEntry.setIndexNames(
    (0, "MICOM-ISDN-MIB", "nvmIsdnSignalingIndex"),
)
if mibBuilder.loadTexts:
    nvmIsdnSignalingEntry.setStatus("mandatory")


class _NvmIsdnSignalingIndex_Type(Integer32):
    """Custom type nvmIsdnSignalingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NvmIsdnSignalingIndex_Type.__name__ = "Integer32"
_NvmIsdnSignalingIndex_Object = MibTableColumn
nvmIsdnSignalingIndex = _NvmIsdnSignalingIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 2, 1, 1),
    _NvmIsdnSignalingIndex_Type()
)
nvmIsdnSignalingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmIsdnSignalingIndex.setStatus("mandatory")


class _NvmIsdnSignalingProtocol_Type(Integer32):
    """Custom type nvmIsdnSignalingProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              6,
              7,
              9,
              12,
              13,
              17,
              19,
              23)
        )
    )
    namedValues = NamedValues(
        *(("dms100", 7),
          ("dss1", 2),
          ("ess5", 6),
          ("etsi", 3),
          ("ins64", 17),
          ("itr6", 19),
          ("ni1", 9),
          ("qsig", 23),
          ("vn2", 12),
          ("vn3", 13))
    )


_NvmIsdnSignalingProtocol_Type.__name__ = "Integer32"
_NvmIsdnSignalingProtocol_Object = MibTableColumn
nvmIsdnSignalingProtocol = _NvmIsdnSignalingProtocol_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 2, 1, 2),
    _NvmIsdnSignalingProtocol_Type()
)
nvmIsdnSignalingProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIsdnSignalingProtocol.setStatus("mandatory")


class _NvmIsdnSignalingCallingAddress_Type(DisplayString):
    """Custom type nvmIsdnSignalingCallingAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 131),
    )


_NvmIsdnSignalingCallingAddress_Type.__name__ = "DisplayString"
_NvmIsdnSignalingCallingAddress_Object = MibTableColumn
nvmIsdnSignalingCallingAddress = _NvmIsdnSignalingCallingAddress_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 2, 1, 3),
    _NvmIsdnSignalingCallingAddress_Type()
)
nvmIsdnSignalingCallingAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIsdnSignalingCallingAddress.setStatus("mandatory")


class _NvmIsdnSignalingSubAddress_Type(DisplayString):
    """Custom type nvmIsdnSignalingSubAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 131),
    )


_NvmIsdnSignalingSubAddress_Type.__name__ = "DisplayString"
_NvmIsdnSignalingSubAddress_Object = MibTableColumn
nvmIsdnSignalingSubAddress = _NvmIsdnSignalingSubAddress_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 2, 1, 4),
    _NvmIsdnSignalingSubAddress_Type()
)
nvmIsdnSignalingSubAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIsdnSignalingSubAddress.setStatus("mandatory")


class _NvmIsdnSignalingInfoTrapEnable_Type(Integer32):
    """Custom type nvmIsdnSignalingInfoTrapEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_NvmIsdnSignalingInfoTrapEnable_Type.__name__ = "Integer32"
_NvmIsdnSignalingInfoTrapEnable_Object = MibTableColumn
nvmIsdnSignalingInfoTrapEnable = _NvmIsdnSignalingInfoTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 2, 1, 5),
    _NvmIsdnSignalingInfoTrapEnable_Type()
)
nvmIsdnSignalingInfoTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIsdnSignalingInfoTrapEnable.setStatus("mandatory")
_McmIsdnLapdTable_Object = MibTable
mcmIsdnLapdTable = _McmIsdnLapdTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 3)
)
if mibBuilder.loadTexts:
    mcmIsdnLapdTable.setStatus("mandatory")
_McmIsdnLapdEntry_Object = MibTableRow
mcmIsdnLapdEntry = _McmIsdnLapdEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 3, 1)
)
mcmIsdnLapdEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    mcmIsdnLapdEntry.setStatus("mandatory")


class _McmIsdnLapdTxwinsiz_Type(Integer32):
    """Custom type mcmIsdnLapdTxwinsiz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_McmIsdnLapdTxwinsiz_Type.__name__ = "Integer32"
_McmIsdnLapdTxwinsiz_Object = MibTableColumn
mcmIsdnLapdTxwinsiz = _McmIsdnLapdTxwinsiz_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 3, 1, 1),
    _McmIsdnLapdTxwinsiz_Type()
)
mcmIsdnLapdTxwinsiz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIsdnLapdTxwinsiz.setStatus("mandatory")


class _McmIsdnLapdRxwinsiz_Type(Integer32):
    """Custom type mcmIsdnLapdRxwinsiz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_McmIsdnLapdRxwinsiz_Type.__name__ = "Integer32"
_McmIsdnLapdRxwinsiz_Object = MibTableColumn
mcmIsdnLapdRxwinsiz = _McmIsdnLapdRxwinsiz_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 3, 1, 2),
    _McmIsdnLapdRxwinsiz_Type()
)
mcmIsdnLapdRxwinsiz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIsdnLapdRxwinsiz.setStatus("mandatory")


class _McmIsdnLapdTxfrmsiz_Type(Integer32):
    """Custom type mcmIsdnLapdTxfrmsiz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_McmIsdnLapdTxfrmsiz_Type.__name__ = "Integer32"
_McmIsdnLapdTxfrmsiz_Object = MibTableColumn
mcmIsdnLapdTxfrmsiz = _McmIsdnLapdTxfrmsiz_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 3, 1, 3),
    _McmIsdnLapdTxfrmsiz_Type()
)
mcmIsdnLapdTxfrmsiz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIsdnLapdTxfrmsiz.setStatus("mandatory")


class _McmIsdnLapdRxfrmsiz_Type(Integer32):
    """Custom type mcmIsdnLapdRxfrmsiz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_McmIsdnLapdRxfrmsiz_Type.__name__ = "Integer32"
_McmIsdnLapdRxfrmsiz_Object = MibTableColumn
mcmIsdnLapdRxfrmsiz = _McmIsdnLapdRxfrmsiz_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 3, 1, 4),
    _McmIsdnLapdRxfrmsiz_Type()
)
mcmIsdnLapdRxfrmsiz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIsdnLapdRxfrmsiz.setStatus("mandatory")


class _McmIsdnLapdTimert200_Type(Integer32):
    """Custom type mcmIsdnLapdTimert200 based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600000),
    )


_McmIsdnLapdTimert200_Type.__name__ = "Integer32"
_McmIsdnLapdTimert200_Object = MibTableColumn
mcmIsdnLapdTimert200 = _McmIsdnLapdTimert200_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 3, 1, 5),
    _McmIsdnLapdTimert200_Type()
)
mcmIsdnLapdTimert200.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIsdnLapdTimert200.setStatus("mandatory")


class _McmIsdnLapdTimert201_Type(Integer32):
    """Custom type mcmIsdnLapdTimert201 based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600000),
    )


_McmIsdnLapdTimert201_Type.__name__ = "Integer32"
_McmIsdnLapdTimert201_Object = MibTableColumn
mcmIsdnLapdTimert201 = _McmIsdnLapdTimert201_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 3, 1, 6),
    _McmIsdnLapdTimert201_Type()
)
mcmIsdnLapdTimert201.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIsdnLapdTimert201.setStatus("mandatory")


class _McmIsdnLapdTimert202_Type(Integer32):
    """Custom type mcmIsdnLapdTimert202 based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600000),
    )


_McmIsdnLapdTimert202_Type.__name__ = "Integer32"
_McmIsdnLapdTimert202_Object = MibTableColumn
mcmIsdnLapdTimert202 = _McmIsdnLapdTimert202_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 3, 1, 7),
    _McmIsdnLapdTimert202_Type()
)
mcmIsdnLapdTimert202.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIsdnLapdTimert202.setStatus("mandatory")


class _McmIsdnLapdTimert203_Type(Integer32):
    """Custom type mcmIsdnLapdTimert203 based on Integer32"""
    defaultValue = 10000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600000),
    )


_McmIsdnLapdTimert203_Type.__name__ = "Integer32"
_McmIsdnLapdTimert203_Object = MibTableColumn
mcmIsdnLapdTimert203 = _McmIsdnLapdTimert203_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 3, 1, 8),
    _McmIsdnLapdTimert203_Type()
)
mcmIsdnLapdTimert203.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIsdnLapdTimert203.setStatus("mandatory")


class _McmIsdnLapdTimertm20_Type(Integer32):
    """Custom type mcmIsdnLapdTimertm20 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600000),
    )


_McmIsdnLapdTimertm20_Type.__name__ = "Integer32"
_McmIsdnLapdTimertm20_Object = MibTableColumn
mcmIsdnLapdTimertm20 = _McmIsdnLapdTimertm20_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 3, 1, 9),
    _McmIsdnLapdTimertm20_Type()
)
mcmIsdnLapdTimertm20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIsdnLapdTimertm20.setStatus("mandatory")


class _McmIsdnLapdn200_Type(Integer32):
    """Custom type mcmIsdnLapdn200 based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_McmIsdnLapdn200_Type.__name__ = "Integer32"
_McmIsdnLapdn200_Object = MibTableColumn
mcmIsdnLapdn200 = _McmIsdnLapdn200_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 3, 1, 10),
    _McmIsdnLapdn200_Type()
)
mcmIsdnLapdn200.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIsdnLapdn200.setStatus("mandatory")


class _McmIsdnLapdn202_Type(Integer32):
    """Custom type mcmIsdnLapdn202 based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_McmIsdnLapdn202_Type.__name__ = "Integer32"
_McmIsdnLapdn202_Object = MibTableColumn
mcmIsdnLapdn202 = _McmIsdnLapdn202_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 3, 1, 11),
    _McmIsdnLapdn202_Type()
)
mcmIsdnLapdn202.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIsdnLapdn202.setStatus("mandatory")


class _McmIsdnLapdnm20_Type(Integer32):
    """Custom type mcmIsdnLapdnm20 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_McmIsdnLapdnm20_Type.__name__ = "Integer32"
_McmIsdnLapdnm20_Object = MibTableColumn
mcmIsdnLapdnm20 = _McmIsdnLapdnm20_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 3, 1, 12),
    _McmIsdnLapdnm20_Type()
)
mcmIsdnLapdnm20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIsdnLapdnm20.setStatus("mandatory")
_NvmIsdnLapdTable_Object = MibTable
nvmIsdnLapdTable = _NvmIsdnLapdTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 4)
)
if mibBuilder.loadTexts:
    nvmIsdnLapdTable.setStatus("mandatory")
_NvmIsdnLapdEntry_Object = MibTableRow
nvmIsdnLapdEntry = _NvmIsdnLapdEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 4, 1)
)
nvmIsdnLapdEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    nvmIsdnLapdEntry.setStatus("mandatory")


class _NvmIsdnLapdTxwinsiz_Type(Integer32):
    """Custom type nvmIsdnLapdTxwinsiz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_NvmIsdnLapdTxwinsiz_Type.__name__ = "Integer32"
_NvmIsdnLapdTxwinsiz_Object = MibTableColumn
nvmIsdnLapdTxwinsiz = _NvmIsdnLapdTxwinsiz_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 4, 1, 1),
    _NvmIsdnLapdTxwinsiz_Type()
)
nvmIsdnLapdTxwinsiz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIsdnLapdTxwinsiz.setStatus("mandatory")


class _NvmIsdnLapdRxwinsiz_Type(Integer32):
    """Custom type nvmIsdnLapdRxwinsiz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_NvmIsdnLapdRxwinsiz_Type.__name__ = "Integer32"
_NvmIsdnLapdRxwinsiz_Object = MibTableColumn
nvmIsdnLapdRxwinsiz = _NvmIsdnLapdRxwinsiz_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 4, 1, 2),
    _NvmIsdnLapdRxwinsiz_Type()
)
nvmIsdnLapdRxwinsiz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIsdnLapdRxwinsiz.setStatus("mandatory")


class _NvmIsdnLapdTxfrmsiz_Type(Integer32):
    """Custom type nvmIsdnLapdTxfrmsiz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_NvmIsdnLapdTxfrmsiz_Type.__name__ = "Integer32"
_NvmIsdnLapdTxfrmsiz_Object = MibTableColumn
nvmIsdnLapdTxfrmsiz = _NvmIsdnLapdTxfrmsiz_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 4, 1, 3),
    _NvmIsdnLapdTxfrmsiz_Type()
)
nvmIsdnLapdTxfrmsiz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIsdnLapdTxfrmsiz.setStatus("mandatory")


class _NvmIsdnLapdRxfrmsiz_Type(Integer32):
    """Custom type nvmIsdnLapdRxfrmsiz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_NvmIsdnLapdRxfrmsiz_Type.__name__ = "Integer32"
_NvmIsdnLapdRxfrmsiz_Object = MibTableColumn
nvmIsdnLapdRxfrmsiz = _NvmIsdnLapdRxfrmsiz_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 4, 1, 4),
    _NvmIsdnLapdRxfrmsiz_Type()
)
nvmIsdnLapdRxfrmsiz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIsdnLapdRxfrmsiz.setStatus("mandatory")


class _NvmIsdnLapdTimert200_Type(Integer32):
    """Custom type nvmIsdnLapdTimert200 based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600000),
    )


_NvmIsdnLapdTimert200_Type.__name__ = "Integer32"
_NvmIsdnLapdTimert200_Object = MibTableColumn
nvmIsdnLapdTimert200 = _NvmIsdnLapdTimert200_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 4, 1, 5),
    _NvmIsdnLapdTimert200_Type()
)
nvmIsdnLapdTimert200.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIsdnLapdTimert200.setStatus("mandatory")


class _NvmIsdnLapdTimert201_Type(Integer32):
    """Custom type nvmIsdnLapdTimert201 based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600000),
    )


_NvmIsdnLapdTimert201_Type.__name__ = "Integer32"
_NvmIsdnLapdTimert201_Object = MibTableColumn
nvmIsdnLapdTimert201 = _NvmIsdnLapdTimert201_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 4, 1, 6),
    _NvmIsdnLapdTimert201_Type()
)
nvmIsdnLapdTimert201.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIsdnLapdTimert201.setStatus("mandatory")


class _NvmIsdnLapdTimert202_Type(Integer32):
    """Custom type nvmIsdnLapdTimert202 based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600000),
    )


_NvmIsdnLapdTimert202_Type.__name__ = "Integer32"
_NvmIsdnLapdTimert202_Object = MibTableColumn
nvmIsdnLapdTimert202 = _NvmIsdnLapdTimert202_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 4, 1, 7),
    _NvmIsdnLapdTimert202_Type()
)
nvmIsdnLapdTimert202.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIsdnLapdTimert202.setStatus("mandatory")


class _NvmIsdnLapdTimert203_Type(Integer32):
    """Custom type nvmIsdnLapdTimert203 based on Integer32"""
    defaultValue = 10000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600000),
    )


_NvmIsdnLapdTimert203_Type.__name__ = "Integer32"
_NvmIsdnLapdTimert203_Object = MibTableColumn
nvmIsdnLapdTimert203 = _NvmIsdnLapdTimert203_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 4, 1, 8),
    _NvmIsdnLapdTimert203_Type()
)
nvmIsdnLapdTimert203.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIsdnLapdTimert203.setStatus("mandatory")


class _NvmIsdnLapdTimertm20_Type(Integer32):
    """Custom type nvmIsdnLapdTimertm20 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600000),
    )


_NvmIsdnLapdTimertm20_Type.__name__ = "Integer32"
_NvmIsdnLapdTimertm20_Object = MibTableColumn
nvmIsdnLapdTimertm20 = _NvmIsdnLapdTimertm20_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 4, 1, 9),
    _NvmIsdnLapdTimertm20_Type()
)
nvmIsdnLapdTimertm20.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIsdnLapdTimertm20.setStatus("mandatory")


class _NvmIsdnLapdn200_Type(Integer32):
    """Custom type nvmIsdnLapdn200 based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_NvmIsdnLapdn200_Type.__name__ = "Integer32"
_NvmIsdnLapdn200_Object = MibTableColumn
nvmIsdnLapdn200 = _NvmIsdnLapdn200_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 4, 1, 10),
    _NvmIsdnLapdn200_Type()
)
nvmIsdnLapdn200.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIsdnLapdn200.setStatus("mandatory")


class _NvmIsdnLapdn202_Type(Integer32):
    """Custom type nvmIsdnLapdn202 based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_NvmIsdnLapdn202_Type.__name__ = "Integer32"
_NvmIsdnLapdn202_Object = MibTableColumn
nvmIsdnLapdn202 = _NvmIsdnLapdn202_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 4, 1, 11),
    _NvmIsdnLapdn202_Type()
)
nvmIsdnLapdn202.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIsdnLapdn202.setStatus("mandatory")


class _NvmIsdnLapdnm20_Type(Integer32):
    """Custom type nvmIsdnLapdnm20 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_NvmIsdnLapdnm20_Type.__name__ = "Integer32"
_NvmIsdnLapdnm20_Object = MibTableColumn
nvmIsdnLapdnm20 = _NvmIsdnLapdnm20_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 4, 1, 12),
    _NvmIsdnLapdnm20_Type()
)
nvmIsdnLapdnm20.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIsdnLapdnm20.setStatus("mandatory")
_NvmIsdnEndpointTable_Object = MibTable
nvmIsdnEndpointTable = _NvmIsdnEndpointTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 5)
)
if mibBuilder.loadTexts:
    nvmIsdnEndpointTable.setStatus("mandatory")
_NvmIsdnEndpointEntry_Object = MibTableRow
nvmIsdnEndpointEntry = _NvmIsdnEndpointEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 5, 1)
)
nvmIsdnEndpointEntry.setIndexNames(
    (0, "MICOM-ISDN-MIB", "nvmIsdnEndpointIndex"),
)
if mibBuilder.loadTexts:
    nvmIsdnEndpointEntry.setStatus("mandatory")


class _NvmIsdnEndpointIndex_Type(Integer32):
    """Custom type nvmIsdnEndpointIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NvmIsdnEndpointIndex_Type.__name__ = "Integer32"
_NvmIsdnEndpointIndex_Object = MibTableColumn
nvmIsdnEndpointIndex = _NvmIsdnEndpointIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 5, 1, 1),
    _NvmIsdnEndpointIndex_Type()
)
nvmIsdnEndpointIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmIsdnEndpointIndex.setStatus("mandatory")


class _NvmIsdnEndpointTeiType_Type(Integer32):
    """Custom type nvmIsdnEndpointTeiType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )


_NvmIsdnEndpointTeiType_Type.__name__ = "Integer32"
_NvmIsdnEndpointTeiType_Object = MibTableColumn
nvmIsdnEndpointTeiType = _NvmIsdnEndpointTeiType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 5, 1, 2),
    _NvmIsdnEndpointTeiType_Type()
)
nvmIsdnEndpointTeiType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIsdnEndpointTeiType.setStatus("mandatory")


class _NvmIsdnEndpointTeiValue_Type(Integer32):
    """Custom type nvmIsdnEndpointTeiValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_NvmIsdnEndpointTeiValue_Type.__name__ = "Integer32"
_NvmIsdnEndpointTeiValue_Object = MibTableColumn
nvmIsdnEndpointTeiValue = _NvmIsdnEndpointTeiValue_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 5, 1, 3),
    _NvmIsdnEndpointTeiValue_Type()
)
nvmIsdnEndpointTeiValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIsdnEndpointTeiValue.setStatus("mandatory")


class _NvmIsdnEndpointSpid_Type(DisplayString):
    """Custom type nvmIsdnEndpointSpid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 131),
    )


_NvmIsdnEndpointSpid_Type.__name__ = "DisplayString"
_NvmIsdnEndpointSpid_Object = MibTableColumn
nvmIsdnEndpointSpid = _NvmIsdnEndpointSpid_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 5, 1, 4),
    _NvmIsdnEndpointSpid_Type()
)
nvmIsdnEndpointSpid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIsdnEndpointSpid.setStatus("mandatory")
_NvmIsdnDirectoryTable_Object = MibTable
nvmIsdnDirectoryTable = _NvmIsdnDirectoryTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 6)
)
if mibBuilder.loadTexts:
    nvmIsdnDirectoryTable.setStatus("mandatory")
_NvmIsdnDirectoryEntry_Object = MibTableRow
nvmIsdnDirectoryEntry = _NvmIsdnDirectoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 6, 1)
)
nvmIsdnDirectoryEntry.setIndexNames(
    (0, "MICOM-ISDN-MIB", "nvmIsdnDirectoryIndex"),
)
if mibBuilder.loadTexts:
    nvmIsdnDirectoryEntry.setStatus("mandatory")


class _NvmIsdnDirectoryIndex_Type(Integer32):
    """Custom type nvmIsdnDirectoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NvmIsdnDirectoryIndex_Type.__name__ = "Integer32"
_NvmIsdnDirectoryIndex_Object = MibTableColumn
nvmIsdnDirectoryIndex = _NvmIsdnDirectoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 6, 1, 1),
    _NvmIsdnDirectoryIndex_Type()
)
nvmIsdnDirectoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmIsdnDirectoryIndex.setStatus("mandatory")


class _NvmIsdnDirectoryNumber_Type(DisplayString):
    """Custom type nvmIsdnDirectoryNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 131),
    )


_NvmIsdnDirectoryNumber_Type.__name__ = "DisplayString"
_NvmIsdnDirectoryNumber_Object = MibTableColumn
nvmIsdnDirectoryNumber = _NvmIsdnDirectoryNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 6, 1, 2),
    _NvmIsdnDirectoryNumber_Type()
)
nvmIsdnDirectoryNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIsdnDirectoryNumber.setStatus("mandatory")


class _NvmIsdnDirectorySigIndex_Type(Integer32):
    """Custom type nvmIsdnDirectorySigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NvmIsdnDirectorySigIndex_Type.__name__ = "Integer32"
_NvmIsdnDirectorySigIndex_Object = MibTableColumn
nvmIsdnDirectorySigIndex = _NvmIsdnDirectorySigIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 6, 1, 3),
    _NvmIsdnDirectorySigIndex_Type()
)
nvmIsdnDirectorySigIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIsdnDirectorySigIndex.setStatus("mandatory")


class _NvmIsdnDirectoryStatus_Type(Integer32):
    """Custom type nvmIsdnDirectoryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("add", 1),
          ("delete", 2))
    )


_NvmIsdnDirectoryStatus_Type.__name__ = "Integer32"
_NvmIsdnDirectoryStatus_Object = MibTableColumn
nvmIsdnDirectoryStatus = _NvmIsdnDirectoryStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 6, 1, 4),
    _NvmIsdnDirectoryStatus_Type()
)
nvmIsdnDirectoryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmIsdnDirectoryStatus.setStatus("mandatory")
_NvmDialCtlConfiguration_ObjectIdentity = ObjectIdentity
nvmDialCtlConfiguration = _NvmDialCtlConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 7)
)


class _NvmDialCtlAcceptMode_Type(Integer32):
    """Custom type nvmDialCtlAcceptMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("acceptAll", 2),
          ("acceptKnown", 3),
          ("acceptNone", 1))
    )


_NvmDialCtlAcceptMode_Type.__name__ = "Integer32"
_NvmDialCtlAcceptMode_Object = MibScalar
nvmDialCtlAcceptMode = _NvmDialCtlAcceptMode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 7, 1),
    _NvmDialCtlAcceptMode_Type()
)
nvmDialCtlAcceptMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmDialCtlAcceptMode.setStatus("mandatory")


class _NvmDialCtlTrapEnable_Type(Integer32):
    """Custom type nvmDialCtlTrapEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_NvmDialCtlTrapEnable_Type.__name__ = "Integer32"
_NvmDialCtlTrapEnable_Object = MibScalar
nvmDialCtlTrapEnable = _NvmDialCtlTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 7, 2),
    _NvmDialCtlTrapEnable_Type()
)
nvmDialCtlTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmDialCtlTrapEnable.setStatus("mandatory")
_McmDialCtlPeerCfgTable_Object = MibTable
mcmDialCtlPeerCfgTable = _McmDialCtlPeerCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 8)
)
if mibBuilder.loadTexts:
    mcmDialCtlPeerCfgTable.setStatus("mandatory")
_McmDialCtlPeerCfgEntry_Object = MibTableRow
mcmDialCtlPeerCfgEntry = _McmDialCtlPeerCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 8, 1)
)
mcmDialCtlPeerCfgEntry.setIndexNames(
    (0, "MICOM-ISDN-MIB", "mcmDialCtlPeerCfgId"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    mcmDialCtlPeerCfgEntry.setStatus("mandatory")


class _McmDialCtlPeerCfgId_Type(Integer32):
    """Custom type mcmDialCtlPeerCfgId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_McmDialCtlPeerCfgId_Type.__name__ = "Integer32"
_McmDialCtlPeerCfgId_Object = MibTableColumn
mcmDialCtlPeerCfgId = _McmDialCtlPeerCfgId_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 8, 1, 1),
    _McmDialCtlPeerCfgId_Type()
)
mcmDialCtlPeerCfgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmDialCtlPeerCfgId.setStatus("mandatory")


class _McmDialCtlPeerCfgBchannel_Type(Integer32):
    """Custom type mcmDialCtlPeerCfgBchannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_McmDialCtlPeerCfgBchannel_Type.__name__ = "Integer32"
_McmDialCtlPeerCfgBchannel_Object = MibTableColumn
mcmDialCtlPeerCfgBchannel = _McmDialCtlPeerCfgBchannel_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 8, 1, 2),
    _McmDialCtlPeerCfgBchannel_Type()
)
mcmDialCtlPeerCfgBchannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmDialCtlPeerCfgBchannel.setStatus("mandatory")
_NvmDialCtlPeerCfgTable_Object = MibTable
nvmDialCtlPeerCfgTable = _NvmDialCtlPeerCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 9)
)
if mibBuilder.loadTexts:
    nvmDialCtlPeerCfgTable.setStatus("mandatory")
_NvmDialCtlPeerCfgEntry_Object = MibTableRow
nvmDialCtlPeerCfgEntry = _NvmDialCtlPeerCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 9, 1)
)
nvmDialCtlPeerCfgEntry.setIndexNames(
    (0, "MICOM-ISDN-MIB", "nvmDialCtlPeerCfgId"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    nvmDialCtlPeerCfgEntry.setStatus("mandatory")


class _NvmDialCtlPeerCfgId_Type(Integer32):
    """Custom type nvmDialCtlPeerCfgId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NvmDialCtlPeerCfgId_Type.__name__ = "Integer32"
_NvmDialCtlPeerCfgId_Object = MibTableColumn
nvmDialCtlPeerCfgId = _NvmDialCtlPeerCfgId_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 9, 1, 1),
    _NvmDialCtlPeerCfgId_Type()
)
nvmDialCtlPeerCfgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmDialCtlPeerCfgId.setStatus("mandatory")


class _NvmDialCtlPeerCfgBchannel_Type(Integer32):
    """Custom type nvmDialCtlPeerCfgBchannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_NvmDialCtlPeerCfgBchannel_Type.__name__ = "Integer32"
_NvmDialCtlPeerCfgBchannel_Object = MibTableColumn
nvmDialCtlPeerCfgBchannel = _NvmDialCtlPeerCfgBchannel_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 9, 1, 2),
    _NvmDialCtlPeerCfgBchannel_Type()
)
nvmDialCtlPeerCfgBchannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmDialCtlPeerCfgBchannel.setStatus("mandatory")


class _NvmDialCtlPeerCfgLowerIf_Type(Integer32):
    """Custom type nvmDialCtlPeerCfgLowerIf based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NvmDialCtlPeerCfgLowerIf_Type.__name__ = "Integer32"
_NvmDialCtlPeerCfgLowerIf_Object = MibTableColumn
nvmDialCtlPeerCfgLowerIf = _NvmDialCtlPeerCfgLowerIf_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 9, 1, 3),
    _NvmDialCtlPeerCfgLowerIf_Type()
)
nvmDialCtlPeerCfgLowerIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmDialCtlPeerCfgLowerIf.setStatus("mandatory")


class _NvmDialCtlPeerCfgOriginateAddress_Type(DisplayString):
    """Custom type nvmDialCtlPeerCfgOriginateAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 131),
    )


_NvmDialCtlPeerCfgOriginateAddress_Type.__name__ = "DisplayString"
_NvmDialCtlPeerCfgOriginateAddress_Object = MibTableColumn
nvmDialCtlPeerCfgOriginateAddress = _NvmDialCtlPeerCfgOriginateAddress_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 9, 1, 4),
    _NvmDialCtlPeerCfgOriginateAddress_Type()
)
nvmDialCtlPeerCfgOriginateAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmDialCtlPeerCfgOriginateAddress.setStatus("mandatory")


class _NvmDialCtlPeerCfgSubAddress_Type(DisplayString):
    """Custom type nvmDialCtlPeerCfgSubAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 131),
    )


_NvmDialCtlPeerCfgSubAddress_Type.__name__ = "DisplayString"
_NvmDialCtlPeerCfgSubAddress_Object = MibTableColumn
nvmDialCtlPeerCfgSubAddress = _NvmDialCtlPeerCfgSubAddress_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 9, 1, 5),
    _NvmDialCtlPeerCfgSubAddress_Type()
)
nvmDialCtlPeerCfgSubAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmDialCtlPeerCfgSubAddress.setStatus("mandatory")


class _NvmDialCtlPeerCfgClosedUserGroup_Type(DisplayString):
    """Custom type nvmDialCtlPeerCfgClosedUserGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 131),
    )


_NvmDialCtlPeerCfgClosedUserGroup_Type.__name__ = "DisplayString"
_NvmDialCtlPeerCfgClosedUserGroup_Object = MibTableColumn
nvmDialCtlPeerCfgClosedUserGroup = _NvmDialCtlPeerCfgClosedUserGroup_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 9, 1, 6),
    _NvmDialCtlPeerCfgClosedUserGroup_Type()
)
nvmDialCtlPeerCfgClosedUserGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmDialCtlPeerCfgClosedUserGroup.setStatus("mandatory")


class _NvmDialCtlPeerCfgSpeed_Type(Integer32):
    """Custom type nvmDialCtlPeerCfgSpeed based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NvmDialCtlPeerCfgSpeed_Type.__name__ = "Integer32"
_NvmDialCtlPeerCfgSpeed_Object = MibTableColumn
nvmDialCtlPeerCfgSpeed = _NvmDialCtlPeerCfgSpeed_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 9, 1, 7),
    _NvmDialCtlPeerCfgSpeed_Type()
)
nvmDialCtlPeerCfgSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmDialCtlPeerCfgSpeed.setStatus("mandatory")


class _NvmDialCtlPeerCfgInfoType_Type(Integer32):
    """Custom type nvmDialCtlPeerCfgInfoType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("audio31", 6),
          ("audio7", 7),
          ("fax", 10),
          ("other", 1),
          ("packetSwitched", 9),
          ("restrictedDigital", 5),
          ("speech", 2),
          ("unrestrictedDigital", 3),
          ("unrestrictedDigital56", 4),
          ("video", 8))
    )


_NvmDialCtlPeerCfgInfoType_Type.__name__ = "Integer32"
_NvmDialCtlPeerCfgInfoType_Object = MibTableColumn
nvmDialCtlPeerCfgInfoType = _NvmDialCtlPeerCfgInfoType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 9, 1, 8),
    _NvmDialCtlPeerCfgInfoType_Type()
)
nvmDialCtlPeerCfgInfoType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmDialCtlPeerCfgInfoType.setStatus("mandatory")


class _NvmDialCtlPeerCfgPermission_Type(Integer32):
    """Custom type nvmDialCtlPeerCfgPermission based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("answer", 2),
          ("both", 3),
          ("none", 5),
          ("originate", 1))
    )


_NvmDialCtlPeerCfgPermission_Type.__name__ = "Integer32"
_NvmDialCtlPeerCfgPermission_Object = MibTableColumn
nvmDialCtlPeerCfgPermission = _NvmDialCtlPeerCfgPermission_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 9, 1, 9),
    _NvmDialCtlPeerCfgPermission_Type()
)
nvmDialCtlPeerCfgPermission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmDialCtlPeerCfgPermission.setStatus("mandatory")


class _NvmDialCtlPeerCfgCallRetries_Type(Integer32):
    """Custom type nvmDialCtlPeerCfgCallRetries based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NvmDialCtlPeerCfgCallRetries_Type.__name__ = "Integer32"
_NvmDialCtlPeerCfgCallRetries_Object = MibTableColumn
nvmDialCtlPeerCfgCallRetries = _NvmDialCtlPeerCfgCallRetries_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 9, 1, 10),
    _NvmDialCtlPeerCfgCallRetries_Type()
)
nvmDialCtlPeerCfgCallRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmDialCtlPeerCfgCallRetries.setStatus("mandatory")


class _NvmDialCtlPeerCfgRetryDelay_Type(Integer32):
    """Custom type nvmDialCtlPeerCfgRetryDelay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NvmDialCtlPeerCfgRetryDelay_Type.__name__ = "Integer32"
_NvmDialCtlPeerCfgRetryDelay_Object = MibTableColumn
nvmDialCtlPeerCfgRetryDelay = _NvmDialCtlPeerCfgRetryDelay_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 9, 1, 11),
    _NvmDialCtlPeerCfgRetryDelay_Type()
)
nvmDialCtlPeerCfgRetryDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmDialCtlPeerCfgRetryDelay.setStatus("mandatory")


class _NvmDialCtlPeerCfgFailureDelay_Type(Integer32):
    """Custom type nvmDialCtlPeerCfgFailureDelay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NvmDialCtlPeerCfgFailureDelay_Type.__name__ = "Integer32"
_NvmDialCtlPeerCfgFailureDelay_Object = MibTableColumn
nvmDialCtlPeerCfgFailureDelay = _NvmDialCtlPeerCfgFailureDelay_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 9, 1, 12),
    _NvmDialCtlPeerCfgFailureDelay_Type()
)
nvmDialCtlPeerCfgFailureDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmDialCtlPeerCfgFailureDelay.setStatus("mandatory")


class _NvmDialCtlPeerCfgTrapEnable_Type(Integer32):
    """Custom type nvmDialCtlPeerCfgTrapEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_NvmDialCtlPeerCfgTrapEnable_Type.__name__ = "Integer32"
_NvmDialCtlPeerCfgTrapEnable_Object = MibTableColumn
nvmDialCtlPeerCfgTrapEnable = _NvmDialCtlPeerCfgTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 9, 1, 13),
    _NvmDialCtlPeerCfgTrapEnable_Type()
)
nvmDialCtlPeerCfgTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmDialCtlPeerCfgTrapEnable.setStatus("mandatory")


class _NvmDialCtlPeerCfgStatus_Type(Integer32):
    """Custom type nvmDialCtlPeerCfgStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("add", 1),
          ("delete", 2))
    )


_NvmDialCtlPeerCfgStatus_Type.__name__ = "Integer32"
_NvmDialCtlPeerCfgStatus_Object = MibTableColumn
nvmDialCtlPeerCfgStatus = _NvmDialCtlPeerCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 9, 1, 14),
    _NvmDialCtlPeerCfgStatus_Type()
)
nvmDialCtlPeerCfgStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmDialCtlPeerCfgStatus.setStatus("mandatory")


class _NvmCallHistoryTableMaxLength_Type(Integer32):
    """Custom type nvmCallHistoryTableMaxLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_NvmCallHistoryTableMaxLength_Type.__name__ = "Integer32"
_NvmCallHistoryTableMaxLength_Object = MibScalar
nvmCallHistoryTableMaxLength = _NvmCallHistoryTableMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 1, 10),
    _NvmCallHistoryTableMaxLength_Type()
)
nvmCallHistoryTableMaxLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmCallHistoryTableMaxLength.setStatus("mandatory")
_Control_ObjectIdentity = ObjectIdentity
control = _Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 2)
)
_McmIsdnSigStatsCntrTable_Object = MibTable
mcmIsdnSigStatsCntrTable = _McmIsdnSigStatsCntrTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 2, 1)
)
if mibBuilder.loadTexts:
    mcmIsdnSigStatsCntrTable.setStatus("obsolete")
_McmIsdnSigStatsCntrEntry_Object = MibTableRow
mcmIsdnSigStatsCntrEntry = _McmIsdnSigStatsCntrEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 2, 1, 1)
)
mcmIsdnSigStatsCntrEntry.setIndexNames(
    (0, "MICOM-ISDN-MIB", "mcmIsdnSigStatsCntrIndex"),
)
if mibBuilder.loadTexts:
    mcmIsdnSigStatsCntrEntry.setStatus("obsolete")


class _McmIsdnSigStatsCntrIndex_Type(Integer32):
    """Custom type mcmIsdnSigStatsCntrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_McmIsdnSigStatsCntrIndex_Type.__name__ = "Integer32"
_McmIsdnSigStatsCntrIndex_Object = MibTableColumn
mcmIsdnSigStatsCntrIndex = _McmIsdnSigStatsCntrIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 2, 1, 1, 1),
    _McmIsdnSigStatsCntrIndex_Type()
)
mcmIsdnSigStatsCntrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIsdnSigStatsCntrIndex.setStatus("obsolete")


class _McmIsdnSigStatsCntrAction_Type(Integer32):
    """Custom type mcmIsdnSigStatsCntrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_McmIsdnSigStatsCntrAction_Type.__name__ = "Integer32"
_McmIsdnSigStatsCntrAction_Object = MibTableColumn
mcmIsdnSigStatsCntrAction = _McmIsdnSigStatsCntrAction_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 2, 1, 1, 2),
    _McmIsdnSigStatsCntrAction_Type()
)
mcmIsdnSigStatsCntrAction.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mcmIsdnSigStatsCntrAction.setStatus("obsolete")
_McmIsdnLapdCntrTable_Object = MibTable
mcmIsdnLapdCntrTable = _McmIsdnLapdCntrTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 2, 2)
)
if mibBuilder.loadTexts:
    mcmIsdnLapdCntrTable.setStatus("obsolete")
_McmIsdnLapdCntrEntry_Object = MibTableRow
mcmIsdnLapdCntrEntry = _McmIsdnLapdCntrEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 2, 2, 1)
)
mcmIsdnLapdCntrEntry.setIndexNames(
    (0, "MICOM-ISDN-MIB", "mcmIsdnLapdCntrIndex"),
)
if mibBuilder.loadTexts:
    mcmIsdnLapdCntrEntry.setStatus("obsolete")


class _McmIsdnLapdCntrIndex_Type(Integer32):
    """Custom type mcmIsdnLapdCntrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McmIsdnLapdCntrIndex_Type.__name__ = "Integer32"
_McmIsdnLapdCntrIndex_Object = MibTableColumn
mcmIsdnLapdCntrIndex = _McmIsdnLapdCntrIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 2, 2, 1, 1),
    _McmIsdnLapdCntrIndex_Type()
)
mcmIsdnLapdCntrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIsdnLapdCntrIndex.setStatus("obsolete")


class _McmIsdnLapdCntrAction_Type(Integer32):
    """Custom type mcmIsdnLapdCntrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_McmIsdnLapdCntrAction_Type.__name__ = "Integer32"
_McmIsdnLapdCntrAction_Object = MibTableColumn
mcmIsdnLapdCntrAction = _McmIsdnLapdCntrAction_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 2, 2, 1, 2),
    _McmIsdnLapdCntrAction_Type()
)
mcmIsdnLapdCntrAction.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mcmIsdnLapdCntrAction.setStatus("obsolete")
_McmDialCtlPeerStatsGaugeTable_Object = MibTable
mcmDialCtlPeerStatsGaugeTable = _McmDialCtlPeerStatsGaugeTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 2, 3)
)
if mibBuilder.loadTexts:
    mcmDialCtlPeerStatsGaugeTable.setStatus("obsolete")
_McmDialCtlPeerStatsGaugeEntry_Object = MibTableRow
mcmDialCtlPeerStatsGaugeEntry = _McmDialCtlPeerStatsGaugeEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 2, 3, 1)
)
mcmDialCtlPeerStatsGaugeEntry.setIndexNames(
    (0, "DIAL-CONTROL-MIB", "dialCtlPeerCfgId"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    mcmDialCtlPeerStatsGaugeEntry.setStatus("obsolete")


class _McmDialCtlPeerStatsGaugeAction_Type(Integer32):
    """Custom type mcmDialCtlPeerStatsGaugeAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_McmDialCtlPeerStatsGaugeAction_Type.__name__ = "Integer32"
_McmDialCtlPeerStatsGaugeAction_Object = MibTableColumn
mcmDialCtlPeerStatsGaugeAction = _McmDialCtlPeerStatsGaugeAction_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 2, 3, 1, 1),
    _McmDialCtlPeerStatsGaugeAction_Type()
)
mcmDialCtlPeerStatsGaugeAction.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mcmDialCtlPeerStatsGaugeAction.setStatus("obsolete")
_McmCallActiveGaugeTable_Object = MibTable
mcmCallActiveGaugeTable = _McmCallActiveGaugeTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 2, 4)
)
if mibBuilder.loadTexts:
    mcmCallActiveGaugeTable.setStatus("obsolete")
_McmCallActiveGaugeEntry_Object = MibTableRow
mcmCallActiveGaugeEntry = _McmCallActiveGaugeEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 2, 4, 1)
)
mcmCallActiveGaugeEntry.setIndexNames(
    (0, "DIAL-CONTROL-MIB", "callActiveSetupTime"),
    (0, "DIAL-CONTROL-MIB", "callActiveIndex"),
)
if mibBuilder.loadTexts:
    mcmCallActiveGaugeEntry.setStatus("obsolete")


class _McmCallActiveGaugeAction_Type(Integer32):
    """Custom type mcmCallActiveGaugeAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_McmCallActiveGaugeAction_Type.__name__ = "Integer32"
_McmCallActiveGaugeAction_Object = MibTableColumn
mcmCallActiveGaugeAction = _McmCallActiveGaugeAction_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 2, 4, 1, 1),
    _McmCallActiveGaugeAction_Type()
)
mcmCallActiveGaugeAction.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mcmCallActiveGaugeAction.setStatus("obsolete")


class _McmCallHistoryTableResetCmd_Type(Integer32):
    """Custom type mcmCallHistoryTableResetCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_McmCallHistoryTableResetCmd_Type.__name__ = "Integer32"
_McmCallHistoryTableResetCmd_Object = MibScalar
mcmCallHistoryTableResetCmd = _McmCallHistoryTableResetCmd_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 24, 2, 5),
    _McmCallHistoryTableResetCmd_Type()
)
mcmCallHistoryTableResetCmd.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mcmCallHistoryTableResetCmd.setStatus("obsolete")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MICOM-ISDN-MIB",
    **{"micom-isdn": micom_isdn,
       "configuration": configuration,
       "nvmIsdnBasicRateTable": nvmIsdnBasicRateTable,
       "nvmIsdnBasicRateEntry": nvmIsdnBasicRateEntry,
       "nvmIsdnBasicRateLineTopology": nvmIsdnBasicRateLineTopology,
       "nvmIsdnBasicRateSignalMode": nvmIsdnBasicRateSignalMode,
       "nvmIsdnSignalingTable": nvmIsdnSignalingTable,
       "nvmIsdnSignalingEntry": nvmIsdnSignalingEntry,
       "nvmIsdnSignalingIndex": nvmIsdnSignalingIndex,
       "nvmIsdnSignalingProtocol": nvmIsdnSignalingProtocol,
       "nvmIsdnSignalingCallingAddress": nvmIsdnSignalingCallingAddress,
       "nvmIsdnSignalingSubAddress": nvmIsdnSignalingSubAddress,
       "nvmIsdnSignalingInfoTrapEnable": nvmIsdnSignalingInfoTrapEnable,
       "mcmIsdnLapdTable": mcmIsdnLapdTable,
       "mcmIsdnLapdEntry": mcmIsdnLapdEntry,
       "mcmIsdnLapdTxwinsiz": mcmIsdnLapdTxwinsiz,
       "mcmIsdnLapdRxwinsiz": mcmIsdnLapdRxwinsiz,
       "mcmIsdnLapdTxfrmsiz": mcmIsdnLapdTxfrmsiz,
       "mcmIsdnLapdRxfrmsiz": mcmIsdnLapdRxfrmsiz,
       "mcmIsdnLapdTimert200": mcmIsdnLapdTimert200,
       "mcmIsdnLapdTimert201": mcmIsdnLapdTimert201,
       "mcmIsdnLapdTimert202": mcmIsdnLapdTimert202,
       "mcmIsdnLapdTimert203": mcmIsdnLapdTimert203,
       "mcmIsdnLapdTimertm20": mcmIsdnLapdTimertm20,
       "mcmIsdnLapdn200": mcmIsdnLapdn200,
       "mcmIsdnLapdn202": mcmIsdnLapdn202,
       "mcmIsdnLapdnm20": mcmIsdnLapdnm20,
       "nvmIsdnLapdTable": nvmIsdnLapdTable,
       "nvmIsdnLapdEntry": nvmIsdnLapdEntry,
       "nvmIsdnLapdTxwinsiz": nvmIsdnLapdTxwinsiz,
       "nvmIsdnLapdRxwinsiz": nvmIsdnLapdRxwinsiz,
       "nvmIsdnLapdTxfrmsiz": nvmIsdnLapdTxfrmsiz,
       "nvmIsdnLapdRxfrmsiz": nvmIsdnLapdRxfrmsiz,
       "nvmIsdnLapdTimert200": nvmIsdnLapdTimert200,
       "nvmIsdnLapdTimert201": nvmIsdnLapdTimert201,
       "nvmIsdnLapdTimert202": nvmIsdnLapdTimert202,
       "nvmIsdnLapdTimert203": nvmIsdnLapdTimert203,
       "nvmIsdnLapdTimertm20": nvmIsdnLapdTimertm20,
       "nvmIsdnLapdn200": nvmIsdnLapdn200,
       "nvmIsdnLapdn202": nvmIsdnLapdn202,
       "nvmIsdnLapdnm20": nvmIsdnLapdnm20,
       "nvmIsdnEndpointTable": nvmIsdnEndpointTable,
       "nvmIsdnEndpointEntry": nvmIsdnEndpointEntry,
       "nvmIsdnEndpointIndex": nvmIsdnEndpointIndex,
       "nvmIsdnEndpointTeiType": nvmIsdnEndpointTeiType,
       "nvmIsdnEndpointTeiValue": nvmIsdnEndpointTeiValue,
       "nvmIsdnEndpointSpid": nvmIsdnEndpointSpid,
       "nvmIsdnDirectoryTable": nvmIsdnDirectoryTable,
       "nvmIsdnDirectoryEntry": nvmIsdnDirectoryEntry,
       "nvmIsdnDirectoryIndex": nvmIsdnDirectoryIndex,
       "nvmIsdnDirectoryNumber": nvmIsdnDirectoryNumber,
       "nvmIsdnDirectorySigIndex": nvmIsdnDirectorySigIndex,
       "nvmIsdnDirectoryStatus": nvmIsdnDirectoryStatus,
       "nvmDialCtlConfiguration": nvmDialCtlConfiguration,
       "nvmDialCtlAcceptMode": nvmDialCtlAcceptMode,
       "nvmDialCtlTrapEnable": nvmDialCtlTrapEnable,
       "mcmDialCtlPeerCfgTable": mcmDialCtlPeerCfgTable,
       "mcmDialCtlPeerCfgEntry": mcmDialCtlPeerCfgEntry,
       "mcmDialCtlPeerCfgId": mcmDialCtlPeerCfgId,
       "mcmDialCtlPeerCfgBchannel": mcmDialCtlPeerCfgBchannel,
       "nvmDialCtlPeerCfgTable": nvmDialCtlPeerCfgTable,
       "nvmDialCtlPeerCfgEntry": nvmDialCtlPeerCfgEntry,
       "nvmDialCtlPeerCfgId": nvmDialCtlPeerCfgId,
       "nvmDialCtlPeerCfgBchannel": nvmDialCtlPeerCfgBchannel,
       "nvmDialCtlPeerCfgLowerIf": nvmDialCtlPeerCfgLowerIf,
       "nvmDialCtlPeerCfgOriginateAddress": nvmDialCtlPeerCfgOriginateAddress,
       "nvmDialCtlPeerCfgSubAddress": nvmDialCtlPeerCfgSubAddress,
       "nvmDialCtlPeerCfgClosedUserGroup": nvmDialCtlPeerCfgClosedUserGroup,
       "nvmDialCtlPeerCfgSpeed": nvmDialCtlPeerCfgSpeed,
       "nvmDialCtlPeerCfgInfoType": nvmDialCtlPeerCfgInfoType,
       "nvmDialCtlPeerCfgPermission": nvmDialCtlPeerCfgPermission,
       "nvmDialCtlPeerCfgCallRetries": nvmDialCtlPeerCfgCallRetries,
       "nvmDialCtlPeerCfgRetryDelay": nvmDialCtlPeerCfgRetryDelay,
       "nvmDialCtlPeerCfgFailureDelay": nvmDialCtlPeerCfgFailureDelay,
       "nvmDialCtlPeerCfgTrapEnable": nvmDialCtlPeerCfgTrapEnable,
       "nvmDialCtlPeerCfgStatus": nvmDialCtlPeerCfgStatus,
       "nvmCallHistoryTableMaxLength": nvmCallHistoryTableMaxLength,
       "control": control,
       "mcmIsdnSigStatsCntrTable": mcmIsdnSigStatsCntrTable,
       "mcmIsdnSigStatsCntrEntry": mcmIsdnSigStatsCntrEntry,
       "mcmIsdnSigStatsCntrIndex": mcmIsdnSigStatsCntrIndex,
       "mcmIsdnSigStatsCntrAction": mcmIsdnSigStatsCntrAction,
       "mcmIsdnLapdCntrTable": mcmIsdnLapdCntrTable,
       "mcmIsdnLapdCntrEntry": mcmIsdnLapdCntrEntry,
       "mcmIsdnLapdCntrIndex": mcmIsdnLapdCntrIndex,
       "mcmIsdnLapdCntrAction": mcmIsdnLapdCntrAction,
       "mcmDialCtlPeerStatsGaugeTable": mcmDialCtlPeerStatsGaugeTable,
       "mcmDialCtlPeerStatsGaugeEntry": mcmDialCtlPeerStatsGaugeEntry,
       "mcmDialCtlPeerStatsGaugeAction": mcmDialCtlPeerStatsGaugeAction,
       "mcmCallActiveGaugeTable": mcmCallActiveGaugeTable,
       "mcmCallActiveGaugeEntry": mcmCallActiveGaugeEntry,
       "mcmCallActiveGaugeAction": mcmCallActiveGaugeAction,
       "mcmCallHistoryTableResetCmd": mcmCallHistoryTableResetCmd}
)
