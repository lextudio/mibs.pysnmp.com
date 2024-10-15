# SNMP MIB module (XIO-HUB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XIO-HUB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:18:40 2024
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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
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

_Xiotech_ObjectIdentity = ObjectIdentity
xiotech = _Xiotech_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2366)
)
_XioHub_ObjectIdentity = ObjectIdentity
xioHub = _XioHub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2366, 1)
)
_XioHubIdentification_ObjectIdentity = ObjectIdentity
xioHubIdentification = _XioHubIdentification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2366, 1, 1)
)


class _XioHubHuName_Type(DisplayString):
    """Custom type xioHubHuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_XioHubHuName_Type.__name__ = "DisplayString"
_XioHubHuName_Object = MibScalar
xioHubHuName = _XioHubHuName_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 1, 1),
    _XioHubHuName_Type()
)
xioHubHuName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xioHubHuName.setStatus("mandatory")
_XioHubHuSerialNum_Type = Integer32
_XioHubHuSerialNum_Object = MibScalar
xioHubHuSerialNum = _XioHubHuSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 1, 2),
    _XioHubHuSerialNum_Type()
)
xioHubHuSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubHuSerialNum.setStatus("mandatory")
_XioHubHuCompat_Type = Integer32
_XioHubHuCompat_Object = MibScalar
xioHubHuCompat = _XioHubHuCompat_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 1, 3),
    _XioHubHuCompat_Type()
)
xioHubHuCompat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubHuCompat.setStatus("mandatory")


class _XioHubHuTCPIPAddr_Type(DisplayString):
    """Custom type xioHubHuTCPIPAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_XioHubHuTCPIPAddr_Type.__name__ = "DisplayString"
_XioHubHuTCPIPAddr_Object = MibScalar
xioHubHuTCPIPAddr = _XioHubHuTCPIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 1, 4),
    _XioHubHuTCPIPAddr_Type()
)
xioHubHuTCPIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xioHubHuTCPIPAddr.setStatus("mandatory")
_XioHubHuHeartbeat_Type = Integer32
_XioHubHuHeartbeat_Object = MibScalar
xioHubHuHeartbeat = _XioHubHuHeartbeat_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 1, 5),
    _XioHubHuHeartbeat_Type()
)
xioHubHuHeartbeat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubHuHeartbeat.setStatus("mandatory")
_XioHubEnvironment_ObjectIdentity = ObjectIdentity
xioHubEnvironment = _XioHubEnvironment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2366, 1, 2)
)
_XioHubEvUpsAc_Type = Integer32
_XioHubEvUpsAc_Object = MibScalar
xioHubEvUpsAc = _XioHubEvUpsAc_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 2, 1),
    _XioHubEvUpsAc_Type()
)
xioHubEvUpsAc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubEvUpsAc.setStatus("mandatory")
_XioHubEvUpsBattLow_Type = Integer32
_XioHubEvUpsBattLow_Object = MibScalar
xioHubEvUpsBattLow = _XioHubEvUpsBattLow_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 2, 2),
    _XioHubEvUpsBattLow_Type()
)
xioHubEvUpsBattLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubEvUpsBattLow.setStatus("mandatory")
_XioHubEvMainPower_Type = Integer32
_XioHubEvMainPower_Object = MibScalar
xioHubEvMainPower = _XioHubEvMainPower_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 2, 3),
    _XioHubEvMainPower_Type()
)
xioHubEvMainPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubEvMainPower.setStatus("mandatory")
_XioHubEvNumSupplies_Type = Integer32
_XioHubEvNumSupplies_Object = MibScalar
xioHubEvNumSupplies = _XioHubEvNumSupplies_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 2, 4),
    _XioHubEvNumSupplies_Type()
)
xioHubEvNumSupplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubEvNumSupplies.setStatus("mandatory")
_XioHubEvNumFrontFans_Type = Integer32
_XioHubEvNumFrontFans_Object = MibScalar
xioHubEvNumFrontFans = _XioHubEvNumFrontFans_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 2, 5),
    _XioHubEvNumFrontFans_Type()
)
xioHubEvNumFrontFans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubEvNumFrontFans.setStatus("mandatory")
_XioHubEvNumRearFans_Type = Integer32
_XioHubEvNumRearFans_Object = MibScalar
xioHubEvNumRearFans = _XioHubEvNumRearFans_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 2, 6),
    _XioHubEvNumRearFans_Type()
)
xioHubEvNumRearFans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubEvNumRearFans.setStatus("mandatory")
_XioHubEvMainDcPowerTable_Object = MibTable
xioHubEvMainDcPowerTable = _XioHubEvMainDcPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 2, 7)
)
if mibBuilder.loadTexts:
    xioHubEvMainDcPowerTable.setStatus("mandatory")
_XioHubEvMainDcPowerEntry_Object = MibTableRow
xioHubEvMainDcPowerEntry = _XioHubEvMainDcPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 2, 7, 1)
)
xioHubEvMainDcPowerEntry.setIndexNames(
    (0, "XIO-HUB-MIB", "xioHubEvDcId"),
)
if mibBuilder.loadTexts:
    xioHubEvMainDcPowerEntry.setStatus("mandatory")


class _XioHubEvDcId_Type(Integer32):
    """Custom type xioHubEvDcId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_XioHubEvDcId_Type.__name__ = "Integer32"
_XioHubEvDcId_Object = MibTableColumn
xioHubEvDcId = _XioHubEvDcId_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 2, 7, 1, 1),
    _XioHubEvDcId_Type()
)
xioHubEvDcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubEvDcId.setStatus("mandatory")


class _XioHubEvDcExists_Type(Integer32):
    """Custom type xioHubEvDcExists based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_XioHubEvDcExists_Type.__name__ = "Integer32"
_XioHubEvDcExists_Object = MibTableColumn
xioHubEvDcExists = _XioHubEvDcExists_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 2, 7, 1, 2),
    _XioHubEvDcExists_Type()
)
xioHubEvDcExists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubEvDcExists.setStatus("mandatory")


class _XioHubEvDcGood_Type(Integer32):
    """Custom type xioHubEvDcGood based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_XioHubEvDcGood_Type.__name__ = "Integer32"
_XioHubEvDcGood_Object = MibTableColumn
xioHubEvDcGood = _XioHubEvDcGood_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 2, 7, 1, 3),
    _XioHubEvDcGood_Type()
)
xioHubEvDcGood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubEvDcGood.setStatus("mandatory")
_XioHubEvFrontFansTable_Object = MibTable
xioHubEvFrontFansTable = _XioHubEvFrontFansTable_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 2, 8)
)
if mibBuilder.loadTexts:
    xioHubEvFrontFansTable.setStatus("mandatory")
_XioHubEvFrontFansEntry_Object = MibTableRow
xioHubEvFrontFansEntry = _XioHubEvFrontFansEntry_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 2, 8, 1)
)
xioHubEvFrontFansEntry.setIndexNames(
    (0, "XIO-HUB-MIB", "xioHubEvFrontFansId"),
)
if mibBuilder.loadTexts:
    xioHubEvFrontFansEntry.setStatus("mandatory")


class _XioHubEvFrontFansId_Type(Integer32):
    """Custom type xioHubEvFrontFansId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_XioHubEvFrontFansId_Type.__name__ = "Integer32"
_XioHubEvFrontFansId_Object = MibTableColumn
xioHubEvFrontFansId = _XioHubEvFrontFansId_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 2, 8, 1, 1),
    _XioHubEvFrontFansId_Type()
)
xioHubEvFrontFansId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubEvFrontFansId.setStatus("mandatory")


class _XioHubEvFrontFansGood_Type(Integer32):
    """Custom type xioHubEvFrontFansGood based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_XioHubEvFrontFansGood_Type.__name__ = "Integer32"
_XioHubEvFrontFansGood_Object = MibTableColumn
xioHubEvFrontFansGood = _XioHubEvFrontFansGood_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 2, 8, 1, 2),
    _XioHubEvFrontFansGood_Type()
)
xioHubEvFrontFansGood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubEvFrontFansGood.setStatus("mandatory")
_XioHubEvRearFansTable_Object = MibTable
xioHubEvRearFansTable = _XioHubEvRearFansTable_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 2, 9)
)
if mibBuilder.loadTexts:
    xioHubEvRearFansTable.setStatus("mandatory")
_XioHubEvRearFansEntry_Object = MibTableRow
xioHubEvRearFansEntry = _XioHubEvRearFansEntry_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 2, 9, 1)
)
xioHubEvRearFansEntry.setIndexNames(
    (0, "XIO-HUB-MIB", "xioHubEvRearFansId"),
)
if mibBuilder.loadTexts:
    xioHubEvRearFansEntry.setStatus("mandatory")


class _XioHubEvRearFansId_Type(Integer32):
    """Custom type xioHubEvRearFansId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_XioHubEvRearFansId_Type.__name__ = "Integer32"
_XioHubEvRearFansId_Object = MibTableColumn
xioHubEvRearFansId = _XioHubEvRearFansId_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 2, 9, 1, 1),
    _XioHubEvRearFansId_Type()
)
xioHubEvRearFansId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubEvRearFansId.setStatus("mandatory")


class _XioHubEvRearFansGood_Type(Integer32):
    """Custom type xioHubEvRearFansGood based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_XioHubEvRearFansGood_Type.__name__ = "Integer32"
_XioHubEvRearFansGood_Object = MibTableColumn
xioHubEvRearFansGood = _XioHubEvRearFansGood_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 2, 9, 1, 2),
    _XioHubEvRearFansGood_Type()
)
xioHubEvRearFansGood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubEvRearFansGood.setStatus("mandatory")
_XioHubEvExtUpsAc_Type = Integer32
_XioHubEvExtUpsAc_Object = MibScalar
xioHubEvExtUpsAc = _XioHubEvExtUpsAc_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 2, 10),
    _XioHubEvExtUpsAc_Type()
)
xioHubEvExtUpsAc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubEvExtUpsAc.setStatus("mandatory")
_XioHubEvExtUpsBatt_Type = Integer32
_XioHubEvExtUpsBatt_Object = MibScalar
xioHubEvExtUpsBatt = _XioHubEvExtUpsBatt_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 2, 11),
    _XioHubEvExtUpsBatt_Type()
)
xioHubEvExtUpsBatt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubEvExtUpsBatt.setStatus("mandatory")
_XioHubEvExtDcMain_Type = Integer32
_XioHubEvExtDcMain_Object = MibScalar
xioHubEvExtDcMain = _XioHubEvExtDcMain_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 2, 12),
    _XioHubEvExtDcMain_Type()
)
xioHubEvExtDcMain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubEvExtDcMain.setStatus("mandatory")
_XioHubEvExtNumSupplies_Type = Integer32
_XioHubEvExtNumSupplies_Object = MibScalar
xioHubEvExtNumSupplies = _XioHubEvExtNumSupplies_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 2, 13),
    _XioHubEvExtNumSupplies_Type()
)
xioHubEvExtNumSupplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubEvExtNumSupplies.setStatus("mandatory")
_XioHubEvExtNumRearFans_Type = Integer32
_XioHubEvExtNumRearFans_Object = MibScalar
xioHubEvExtNumRearFans = _XioHubEvExtNumRearFans_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 2, 14),
    _XioHubEvExtNumRearFans_Type()
)
xioHubEvExtNumRearFans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubEvExtNumRearFans.setStatus("mandatory")
_XioHubEvExtMainDcPowerTable_Object = MibTable
xioHubEvExtMainDcPowerTable = _XioHubEvExtMainDcPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 2, 15)
)
if mibBuilder.loadTexts:
    xioHubEvExtMainDcPowerTable.setStatus("mandatory")
_XioHubEvExtMainDcPowerEntry_Object = MibTableRow
xioHubEvExtMainDcPowerEntry = _XioHubEvExtMainDcPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 2, 15, 1)
)
xioHubEvExtMainDcPowerEntry.setIndexNames(
    (0, "XIO-HUB-MIB", "xioHubEvExtDcId"),
)
if mibBuilder.loadTexts:
    xioHubEvExtMainDcPowerEntry.setStatus("mandatory")


class _XioHubEvExtDcId_Type(Integer32):
    """Custom type xioHubEvExtDcId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_XioHubEvExtDcId_Type.__name__ = "Integer32"
_XioHubEvExtDcId_Object = MibTableColumn
xioHubEvExtDcId = _XioHubEvExtDcId_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 2, 15, 1, 1),
    _XioHubEvExtDcId_Type()
)
xioHubEvExtDcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubEvExtDcId.setStatus("mandatory")


class _XioHubEvExtDcExists_Type(Integer32):
    """Custom type xioHubEvExtDcExists based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_XioHubEvExtDcExists_Type.__name__ = "Integer32"
_XioHubEvExtDcExists_Object = MibTableColumn
xioHubEvExtDcExists = _XioHubEvExtDcExists_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 2, 15, 1, 2),
    _XioHubEvExtDcExists_Type()
)
xioHubEvExtDcExists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubEvExtDcExists.setStatus("mandatory")


class _XioHubEvExtDcGood_Type(Integer32):
    """Custom type xioHubEvExtDcGood based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_XioHubEvExtDcGood_Type.__name__ = "Integer32"
_XioHubEvExtDcGood_Object = MibTableColumn
xioHubEvExtDcGood = _XioHubEvExtDcGood_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 2, 15, 1, 3),
    _XioHubEvExtDcGood_Type()
)
xioHubEvExtDcGood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubEvExtDcGood.setStatus("mandatory")
_XioHubEvExtRearFansTable_Object = MibTable
xioHubEvExtRearFansTable = _XioHubEvExtRearFansTable_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 2, 16)
)
if mibBuilder.loadTexts:
    xioHubEvExtRearFansTable.setStatus("mandatory")
_XioHubEvExtRearFansEntry_Object = MibTableRow
xioHubEvExtRearFansEntry = _XioHubEvExtRearFansEntry_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 2, 16, 1)
)
xioHubEvExtRearFansEntry.setIndexNames(
    (0, "XIO-HUB-MIB", "xioHubEvExtRearFansId"),
)
if mibBuilder.loadTexts:
    xioHubEvExtRearFansEntry.setStatus("mandatory")


class _XioHubEvExtRearFansId_Type(Integer32):
    """Custom type xioHubEvExtRearFansId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_XioHubEvExtRearFansId_Type.__name__ = "Integer32"
_XioHubEvExtRearFansId_Object = MibTableColumn
xioHubEvExtRearFansId = _XioHubEvExtRearFansId_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 2, 16, 1, 1),
    _XioHubEvExtRearFansId_Type()
)
xioHubEvExtRearFansId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubEvExtRearFansId.setStatus("mandatory")


class _XioHubEvExtRearFansGood_Type(Integer32):
    """Custom type xioHubEvExtRearFansGood based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_XioHubEvExtRearFansGood_Type.__name__ = "Integer32"
_XioHubEvExtRearFansGood_Object = MibTableColumn
xioHubEvExtRearFansGood = _XioHubEvExtRearFansGood_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 2, 16, 1, 2),
    _XioHubEvExtRearFansGood_Type()
)
xioHubEvExtRearFansGood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubEvExtRearFansGood.setStatus("mandatory")
_XioHubEvHabTempsTable_Object = MibTable
xioHubEvHabTempsTable = _XioHubEvHabTempsTable_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 2, 17)
)
if mibBuilder.loadTexts:
    xioHubEvHabTempsTable.setStatus("mandatory")
_XioHubEvHabTempsEntry_Object = MibTableRow
xioHubEvHabTempsEntry = _XioHubEvHabTempsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 2, 17, 1)
)
xioHubEvHabTempsEntry.setIndexNames(
    (0, "XIO-HUB-MIB", "xioHubEvHabId"),
)
if mibBuilder.loadTexts:
    xioHubEvHabTempsEntry.setStatus("mandatory")
_XioHubEvHabId_Type = Integer32
_XioHubEvHabId_Object = MibTableColumn
xioHubEvHabId = _XioHubEvHabId_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 2, 17, 1, 1),
    _XioHubEvHabId_Type()
)
xioHubEvHabId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubEvHabId.setStatus("mandatory")
_XioHubEvHabInstalled_Type = Integer32
_XioHubEvHabInstalled_Object = MibTableColumn
xioHubEvHabInstalled = _XioHubEvHabInstalled_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 2, 17, 1, 2),
    _XioHubEvHabInstalled_Type()
)
xioHubEvHabInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubEvHabInstalled.setStatus("mandatory")
_XioHubEvHubHabTemp_Type = Integer32
_XioHubEvHubHabTemp_Object = MibTableColumn
xioHubEvHubHabTemp = _XioHubEvHubHabTemp_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 2, 17, 1, 3),
    _XioHubEvHubHabTemp_Type()
)
xioHubEvHubHabTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubEvHubHabTemp.setStatus("mandatory")
_XioHubEvServerHabTemp_Type = Integer32
_XioHubEvServerHabTemp_Object = MibTableColumn
xioHubEvServerHabTemp = _XioHubEvServerHabTemp_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 2, 17, 1, 4),
    _XioHubEvServerHabTemp_Type()
)
xioHubEvServerHabTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubEvServerHabTemp.setStatus("mandatory")
_XioHubEvProcessorTemp_Type = Integer32
_XioHubEvProcessorTemp_Object = MibScalar
xioHubEvProcessorTemp = _XioHubEvProcessorTemp_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 2, 18),
    _XioHubEvProcessorTemp_Type()
)
xioHubEvProcessorTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubEvProcessorTemp.setStatus("mandatory")
_XioHubEvCacheTemp_Type = Integer32
_XioHubEvCacheTemp_Object = MibScalar
xioHubEvCacheTemp = _XioHubEvCacheTemp_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 2, 19),
    _XioHubEvCacheTemp_Type()
)
xioHubEvCacheTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubEvCacheTemp.setStatus("mandatory")
_XioHubEvIsaTemp_Type = Integer32
_XioHubEvIsaTemp_Object = MibScalar
xioHubEvIsaTemp = _XioHubEvIsaTemp_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 2, 20),
    _XioHubEvIsaTemp_Type()
)
xioHubEvIsaTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubEvIsaTemp.setStatus("mandatory")
_XioHubEvRearTemp_Type = Integer32
_XioHubEvRearTemp_Object = MibScalar
xioHubEvRearTemp = _XioHubEvRearTemp_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 2, 21),
    _XioHubEvRearTemp_Type()
)
xioHubEvRearTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubEvRearTemp.setStatus("mandatory")
_XioHubEvExtCabinetTemp_Type = Integer32
_XioHubEvExtCabinetTemp_Object = MibScalar
xioHubEvExtCabinetTemp = _XioHubEvExtCabinetTemp_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 2, 22),
    _XioHubEvExtCabinetTemp_Type()
)
xioHubEvExtCabinetTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubEvExtCabinetTemp.setStatus("mandatory")
_XioHubEvKBsPerSec_Type = Integer32
_XioHubEvKBsPerSec_Object = MibScalar
xioHubEvKBsPerSec = _XioHubEvKBsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 2, 23),
    _XioHubEvKBsPerSec_Type()
)
xioHubEvKBsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubEvKBsPerSec.setStatus("mandatory")
_XioHubEvIOsPerSec_Type = Integer32
_XioHubEvIOsPerSec_Object = MibScalar
xioHubEvIOsPerSec = _XioHubEvIOsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 2, 24),
    _XioHubEvIOsPerSec_Type()
)
xioHubEvIOsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubEvIOsPerSec.setStatus("mandatory")
_XioHubStatusData_ObjectIdentity = ObjectIdentity
xioHubStatusData = _XioHubStatusData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2366, 1, 3)
)


class _XioHubSdEmbedPcState_Type(Integer32):
    """Custom type xioHubSdEmbedPcState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              15,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("failed", 6),
          ("goneoffline", 65535),
          ("notconnected", 9),
          ("offline", 0),
          ("operational", 5),
          ("post0", 2),
          ("post1", 3),
          ("runningdiagnostics", 4),
          ("standby", 1),
          ("synchronizing", 8),
          ("unknown", 15),
          ("waitingforfibreconnect", 7))
    )


_XioHubSdEmbedPcState_Type.__name__ = "Integer32"
_XioHubSdEmbedPcState_Object = MibScalar
xioHubSdEmbedPcState = _XioHubSdEmbedPcState_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 3, 1),
    _XioHubSdEmbedPcState_Type()
)
xioHubSdEmbedPcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubSdEmbedPcState.setStatus("mandatory")


class _XioHubSdControllerState_Type(Integer32):
    """Custom type xioHubSdControllerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              15,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("failed", 6),
          ("goneoffline", 65535),
          ("notconnected", 9),
          ("offline", 0),
          ("operational", 5),
          ("post0", 2),
          ("post1", 3),
          ("runningdiagnostics", 4),
          ("standby", 1),
          ("synchronizing", 8),
          ("unknown", 15),
          ("waitingforfibreconnect", 7))
    )


_XioHubSdControllerState_Type.__name__ = "Integer32"
_XioHubSdControllerState_Object = MibScalar
xioHubSdControllerState = _XioHubSdControllerState_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 3, 2),
    _XioHubSdControllerState_Type()
)
xioHubSdControllerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubSdControllerState.setStatus("mandatory")
_XioHubSdCacheState_Type = Integer32
_XioHubSdCacheState_Object = MibScalar
xioHubSdCacheState = _XioHubSdCacheState_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 3, 3),
    _XioHubSdCacheState_Type()
)
xioHubSdCacheState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubSdCacheState.setStatus("mandatory")
_XioHubSdHabStatusTable_Object = MibTable
xioHubSdHabStatusTable = _XioHubSdHabStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 3, 4)
)
if mibBuilder.loadTexts:
    xioHubSdHabStatusTable.setStatus("mandatory")
_XioHubSdHabStatusEntry_Object = MibTableRow
xioHubSdHabStatusEntry = _XioHubSdHabStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 3, 4, 1)
)
xioHubSdHabStatusEntry.setIndexNames(
    (0, "XIO-HUB-MIB", "xioHubSdHabId"),
)
if mibBuilder.loadTexts:
    xioHubSdHabStatusEntry.setStatus("mandatory")
_XioHubSdHabId_Type = Integer32
_XioHubSdHabId_Object = MibTableColumn
xioHubSdHabId = _XioHubSdHabId_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 3, 4, 1, 1),
    _XioHubSdHabId_Type()
)
xioHubSdHabId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubSdHabId.setStatus("mandatory")
_XioHubSdHabInstalled_Type = Integer32
_XioHubSdHabInstalled_Object = MibTableColumn
xioHubSdHabInstalled = _XioHubSdHabInstalled_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 3, 4, 1, 2),
    _XioHubSdHabInstalled_Type()
)
xioHubSdHabInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubSdHabInstalled.setStatus("mandatory")


class _XioHubSdHubHabState_Type(Integer32):
    """Custom type xioHubSdHubHabState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              15,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("failed", 6),
          ("goneoffline", 65535),
          ("notconnected", 9),
          ("offline", 0),
          ("operational", 5),
          ("post0", 2),
          ("post1", 3),
          ("runningdiagnostics", 4),
          ("standby", 1),
          ("synchronizing", 8),
          ("unknown", 15),
          ("waitingforfibreconnect", 7))
    )


_XioHubSdHubHabState_Type.__name__ = "Integer32"
_XioHubSdHubHabState_Object = MibTableColumn
xioHubSdHubHabState = _XioHubSdHubHabState_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 3, 4, 1, 3),
    _XioHubSdHubHabState_Type()
)
xioHubSdHubHabState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubSdHubHabState.setStatus("mandatory")


class _XioHubSdServerHabState_Type(Integer32):
    """Custom type xioHubSdServerHabState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              15,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("failed", 6),
          ("goneoffline", 65535),
          ("notconnected", 9),
          ("offline", 0),
          ("operational", 5),
          ("post0", 2),
          ("post1", 3),
          ("runningdiagnostics", 4),
          ("standby", 1),
          ("synchronizing", 8),
          ("unknown", 15),
          ("waitingforfibreconnect", 7))
    )


_XioHubSdServerHabState_Type.__name__ = "Integer32"
_XioHubSdServerHabState_Object = MibTableColumn
xioHubSdServerHabState = _XioHubSdServerHabState_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 3, 4, 1, 4),
    _XioHubSdServerHabState_Type()
)
xioHubSdServerHabState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubSdServerHabState.setStatus("mandatory")
_XioHubSdServerInfoTable_Object = MibTable
xioHubSdServerInfoTable = _XioHubSdServerInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 3, 5)
)
if mibBuilder.loadTexts:
    xioHubSdServerInfoTable.setStatus("mandatory")
_XioHubSdServerInfoEntry_Object = MibTableRow
xioHubSdServerInfoEntry = _XioHubSdServerInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 3, 5, 1)
)
xioHubSdServerInfoEntry.setIndexNames(
    (0, "XIO-HUB-MIB", "xioHubSdServerId"),
)
if mibBuilder.loadTexts:
    xioHubSdServerInfoEntry.setStatus("mandatory")
_XioHubSdServerId_Type = Integer32
_XioHubSdServerId_Object = MibTableColumn
xioHubSdServerId = _XioHubSdServerId_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 3, 5, 1, 1),
    _XioHubSdServerId_Type()
)
xioHubSdServerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubSdServerId.setStatus("mandatory")


class _XioHubSdServerStates_Type(Integer32):
    """Custom type xioHubSdServerStates based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              15,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("failed", 6),
          ("goneoffline", 65535),
          ("notconnected", 9),
          ("offline", 0),
          ("operational", 5),
          ("post0", 2),
          ("post1", 3),
          ("runningdiagnostics", 4),
          ("standby", 1),
          ("synchronizing", 8),
          ("unknown", 15),
          ("waitingforfibreconnect", 7))
    )


_XioHubSdServerStates_Type.__name__ = "Integer32"
_XioHubSdServerStates_Object = MibTableColumn
xioHubSdServerStates = _XioHubSdServerStates_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 3, 5, 1, 2),
    _XioHubSdServerStates_Type()
)
xioHubSdServerStates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubSdServerStates.setStatus("mandatory")
_XioHubPhysicalDevice_ObjectIdentity = ObjectIdentity
xioHubPhysicalDevice = _XioHubPhysicalDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2366, 1, 4)
)
_XioHubPdPhysDevTable_Object = MibTable
xioHubPdPhysDevTable = _XioHubPdPhysDevTable_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 4, 1)
)
if mibBuilder.loadTexts:
    xioHubPdPhysDevTable.setStatus("mandatory")
_XioHubPdPhysDevEntry_Object = MibTableRow
xioHubPdPhysDevEntry = _XioHubPdPhysDevEntry_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 4, 1, 1)
)
xioHubPdPhysDevEntry.setIndexNames(
    (0, "XIO-HUB-MIB", "xioHubPdIndex"),
)
if mibBuilder.loadTexts:
    xioHubPdPhysDevEntry.setStatus("mandatory")
_XioHubPdIndex_Type = Integer32
_XioHubPdIndex_Object = MibTableColumn
xioHubPdIndex = _XioHubPdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 4, 1, 1, 1),
    _XioHubPdIndex_Type()
)
xioHubPdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubPdIndex.setStatus("mandatory")
_XioHubPdChannel_Type = Integer32
_XioHubPdChannel_Object = MibTableColumn
xioHubPdChannel = _XioHubPdChannel_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 4, 1, 1, 2),
    _XioHubPdChannel_Type()
)
xioHubPdChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubPdChannel.setStatus("mandatory")
_XioHubPdScsiId_Type = Integer32
_XioHubPdScsiId_Object = MibTableColumn
xioHubPdScsiId = _XioHubPdScsiId_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 4, 1, 1, 3),
    _XioHubPdScsiId_Type()
)
xioHubPdScsiId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubPdScsiId.setStatus("mandatory")


class _XioHubPdClass_Type(Integer32):
    """Custom type xioHubPdClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("data", 2),
          ("hotspare", 3),
          ("notsafe", 4),
          ("unlabled", 1))
    )


_XioHubPdClass_Type.__name__ = "Integer32"
_XioHubPdClass_Object = MibTableColumn
xioHubPdClass = _XioHubPdClass_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 4, 1, 1, 4),
    _XioHubPdClass_Type()
)
xioHubPdClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubPdClass.setStatus("mandatory")


class _XioHubPdDevName_Type(DisplayString):
    """Custom type xioHubPdDevName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_XioHubPdDevName_Type.__name__ = "DisplayString"
_XioHubPdDevName_Object = MibTableColumn
xioHubPdDevName = _XioHubPdDevName_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 4, 1, 1, 5),
    _XioHubPdDevName_Type()
)
xioHubPdDevName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubPdDevName.setStatus("mandatory")
_XioHubPdSerialNum_Type = Integer32
_XioHubPdSerialNum_Object = MibTableColumn
xioHubPdSerialNum = _XioHubPdSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 4, 1, 1, 6),
    _XioHubPdSerialNum_Type()
)
xioHubPdSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubPdSerialNum.setStatus("mandatory")


class _XioHubPdPostStatus_Type(Integer32):
    """Custom type xioHubPdPostStatus based on Integer32"""
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
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("deviceok", 2),
          ("failinquirecmd", 3),
          ("failinquireserialno", 6),
          ("failrdcapacity", 12),
          ("failreadbuf", 9),
          ("failsenddiag", 7),
          ("failstartunit", 5),
          ("failtestunitready", 4),
          ("failverify", 11),
          ("failwritebuf", 8),
          ("failwrrdbufpat", 10),
          ("nonexistent", 1))
    )


_XioHubPdPostStatus_Type.__name__ = "Integer32"
_XioHubPdPostStatus_Object = MibTableColumn
xioHubPdPostStatus = _XioHubPdPostStatus_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 4, 1, 1, 7),
    _XioHubPdPostStatus_Type()
)
xioHubPdPostStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubPdPostStatus.setStatus("mandatory")


class _XioHubPdDevStatus_Type(Integer32):
    """Custom type xioHubPdDevStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("deviceOK", 2),
          ("inoperable", 3),
          ("nonExistent", 1))
    )


_XioHubPdDevStatus_Type.__name__ = "Integer32"
_XioHubPdDevStatus_Object = MibTableColumn
xioHubPdDevStatus = _XioHubPdDevStatus_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 4, 1, 1, 8),
    _XioHubPdDevStatus_Type()
)
xioHubPdDevStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubPdDevStatus.setStatus("mandatory")
_XioHubPdDevCapacity_Type = Integer32
_XioHubPdDevCapacity_Object = MibTableColumn
xioHubPdDevCapacity = _XioHubPdDevCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 4, 1, 1, 9),
    _XioHubPdDevCapacity_Type()
)
xioHubPdDevCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubPdDevCapacity.setStatus("mandatory")


class _XioHubPdProductId_Type(DisplayString):
    """Custom type xioHubPdProductId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_XioHubPdProductId_Type.__name__ = "DisplayString"
_XioHubPdProductId_Object = MibTableColumn
xioHubPdProductId = _XioHubPdProductId_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 4, 1, 1, 10),
    _XioHubPdProductId_Type()
)
xioHubPdProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubPdProductId.setStatus("mandatory")


class _XioHubPdVendorId_Type(DisplayString):
    """Custom type xioHubPdVendorId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_XioHubPdVendorId_Type.__name__ = "DisplayString"
_XioHubPdVendorId_Object = MibTableColumn
xioHubPdVendorId = _XioHubPdVendorId_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 4, 1, 1, 11),
    _XioHubPdVendorId_Type()
)
xioHubPdVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubPdVendorId.setStatus("mandatory")


class _XioHubPdProductRev_Type(DisplayString):
    """Custom type xioHubPdProductRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_XioHubPdProductRev_Type.__name__ = "DisplayString"
_XioHubPdProductRev_Object = MibTableColumn
xioHubPdProductRev = _XioHubPdProductRev_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 4, 1, 1, 12),
    _XioHubPdProductRev_Type()
)
xioHubPdProductRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubPdProductRev.setStatus("mandatory")


class _XioHubPdSerialNo_Type(DisplayString):
    """Custom type xioHubPdSerialNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 13),
    )


_XioHubPdSerialNo_Type.__name__ = "DisplayString"
_XioHubPdSerialNo_Object = MibTableColumn
xioHubPdSerialNo = _XioHubPdSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 4, 1, 1, 13),
    _XioHubPdSerialNo_Type()
)
xioHubPdSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubPdSerialNo.setStatus("mandatory")
_XioHubPdTotAvail_Type = Integer32
_XioHubPdTotAvail_Object = MibTableColumn
xioHubPdTotAvail = _XioHubPdTotAvail_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 4, 1, 1, 14),
    _XioHubPdTotAvail_Type()
)
xioHubPdTotAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubPdTotAvail.setStatus("mandatory")
_XioHubPdLargestAvail_Type = Integer32
_XioHubPdLargestAvail_Object = MibTableColumn
xioHubPdLargestAvail = _XioHubPdLargestAvail_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 4, 1, 1, 15),
    _XioHubPdLargestAvail_Type()
)
xioHubPdLargestAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubPdLargestAvail.setStatus("mandatory")
_XioHubPdTotRdReq_Type = Counter32
_XioHubPdTotRdReq_Object = MibTableColumn
xioHubPdTotRdReq = _XioHubPdTotRdReq_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 4, 1, 1, 16),
    _XioHubPdTotRdReq_Type()
)
xioHubPdTotRdReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubPdTotRdReq.setStatus("mandatory")
_XioHubPdTotWrReq_Type = Counter32
_XioHubPdTotWrReq_Object = MibTableColumn
xioHubPdTotWrReq = _XioHubPdTotWrReq_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 4, 1, 1, 17),
    _XioHubPdTotWrReq_Type()
)
xioHubPdTotWrReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubPdTotWrReq.setStatus("mandatory")
_XioHubPdTotCorrectErr_Type = Counter32
_XioHubPdTotCorrectErr_Object = MibTableColumn
xioHubPdTotCorrectErr = _XioHubPdTotCorrectErr_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 4, 1, 1, 18),
    _XioHubPdTotCorrectErr_Type()
)
xioHubPdTotCorrectErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubPdTotCorrectErr.setStatus("mandatory")
_XioHubPdAvgSec_Type = Integer32
_XioHubPdAvgSec_Object = MibTableColumn
xioHubPdAvgSec = _XioHubPdAvgSec_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 4, 1, 1, 19),
    _XioHubPdAvgSec_Type()
)
xioHubPdAvgSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubPdAvgSec.setStatus("mandatory")
_XioHubPdNumReq_Type = Integer32
_XioHubPdNumReq_Object = MibTableColumn
xioHubPdNumReq = _XioHubPdNumReq_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 4, 1, 1, 20),
    _XioHubPdNumReq_Type()
)
xioHubPdNumReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubPdNumReq.setStatus("mandatory")
_XioHubPdQueDepth_Type = Integer32
_XioHubPdQueDepth_Object = MibTableColumn
xioHubPdQueDepth = _XioHubPdQueDepth_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 4, 1, 1, 21),
    _XioHubPdQueDepth_Type()
)
xioHubPdQueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubPdQueDepth.setStatus("mandatory")
_XioHubPdKBytesPS_Type = Integer32
_XioHubPdKBytesPS_Object = MibTableColumn
xioHubPdKBytesPS = _XioHubPdKBytesPS_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 4, 1, 1, 22),
    _XioHubPdKBytesPS_Type()
)
xioHubPdKBytesPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubPdKBytesPS.setStatus("mandatory")
_XioHubRaidDevice_ObjectIdentity = ObjectIdentity
xioHubRaidDevice = _XioHubRaidDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2366, 1, 5)
)
_XioHubRdRaidDevTable_Object = MibTable
xioHubRdRaidDevTable = _XioHubRdRaidDevTable_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 5, 1)
)
if mibBuilder.loadTexts:
    xioHubRdRaidDevTable.setStatus("mandatory")
_XioHubRdRaidDevEntry_Object = MibTableRow
xioHubRdRaidDevEntry = _XioHubRdRaidDevEntry_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 5, 1, 1)
)
xioHubRdRaidDevEntry.setIndexNames(
    (0, "XIO-HUB-MIB", "xioHubRdRaidId"),
)
if mibBuilder.loadTexts:
    xioHubRdRaidDevEntry.setStatus("mandatory")
_XioHubRdRaidId_Type = Integer32
_XioHubRdRaidId_Object = MibTableColumn
xioHubRdRaidId = _XioHubRdRaidId_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 5, 1, 1, 1),
    _XioHubRdRaidId_Type()
)
xioHubRdRaidId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubRdRaidId.setStatus("mandatory")


class _XioHubRdClass_Type(Integer32):
    """Custom type xioHubRdClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("classNonRaid", 1),
          ("classRaid0", 2),
          ("classRaid1", 3),
          ("classRaid10", 5),
          ("classRaid5", 4))
    )


_XioHubRdClass_Type.__name__ = "Integer32"
_XioHubRdClass_Object = MibTableColumn
xioHubRdClass = _XioHubRdClass_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 5, 1, 1, 2),
    _XioHubRdClass_Type()
)
xioHubRdClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubRdClass.setStatus("mandatory")


class _XioHubRdDevStatus_Type(Integer32):
    """Custom type xioHubRdDevStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("deviceOK", 2),
          ("inoperable", 4),
          ("nonExistent", 1),
          ("uninitialized", 3))
    )


_XioHubRdDevStatus_Type.__name__ = "Integer32"
_XioHubRdDevStatus_Object = MibTableColumn
xioHubRdDevStatus = _XioHubRdDevStatus_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 5, 1, 1, 3),
    _XioHubRdDevStatus_Type()
)
xioHubRdDevStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubRdDevStatus.setStatus("mandatory")
_XioHubRdDepthMirror_Type = Integer32
_XioHubRdDepthMirror_Object = MibTableColumn
xioHubRdDepthMirror = _XioHubRdDepthMirror_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 5, 1, 1, 4),
    _XioHubRdDepthMirror_Type()
)
xioHubRdDepthMirror.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubRdDepthMirror.setStatus("mandatory")
_XioHubRdDevStripe_Type = Integer32
_XioHubRdDevStripe_Object = MibTableColumn
xioHubRdDevStripe = _XioHubRdDevStripe_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 5, 1, 1, 5),
    _XioHubRdDevStripe_Type()
)
xioHubRdDevStripe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubRdDevStripe.setStatus("mandatory")
_XioHubRdDevCapacity_Type = Integer32
_XioHubRdDevCapacity_Object = MibTableColumn
xioHubRdDevCapacity = _XioHubRdDevCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 5, 1, 1, 6),
    _XioHubRdDevCapacity_Type()
)
xioHubRdDevCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubRdDevCapacity.setStatus("mandatory")
_XioHubRdNumSectors_Type = Integer32
_XioHubRdNumSectors_Object = MibTableColumn
xioHubRdNumSectors = _XioHubRdNumSectors_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 5, 1, 1, 7),
    _XioHubRdNumSectors_Type()
)
xioHubRdNumSectors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubRdNumSectors.setStatus("mandatory")
_XioHubRdTotRdReq_Type = Counter32
_XioHubRdTotRdReq_Object = MibTableColumn
xioHubRdTotRdReq = _XioHubRdTotRdReq_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 5, 1, 1, 8),
    _XioHubRdTotRdReq_Type()
)
xioHubRdTotRdReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubRdTotRdReq.setStatus("mandatory")
_XioHubRdTotWrReq_Type = Counter32
_XioHubRdTotWrReq_Object = MibTableColumn
xioHubRdTotWrReq = _XioHubRdTotWrReq_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 5, 1, 1, 9),
    _XioHubRdTotWrReq_Type()
)
xioHubRdTotWrReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubRdTotWrReq.setStatus("mandatory")
_XioHubRdTotCorrectErr_Type = Counter32
_XioHubRdTotCorrectErr_Object = MibTableColumn
xioHubRdTotCorrectErr = _XioHubRdTotCorrectErr_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 5, 1, 1, 10),
    _XioHubRdTotCorrectErr_Type()
)
xioHubRdTotCorrectErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubRdTotCorrectErr.setStatus("mandatory")
_XioHubRdAvgSec_Type = Integer32
_XioHubRdAvgSec_Object = MibTableColumn
xioHubRdAvgSec = _XioHubRdAvgSec_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 5, 1, 1, 11),
    _XioHubRdAvgSec_Type()
)
xioHubRdAvgSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubRdAvgSec.setStatus("mandatory")
_XioHubRdNumReq_Type = Integer32
_XioHubRdNumReq_Object = MibTableColumn
xioHubRdNumReq = _XioHubRdNumReq_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 5, 1, 1, 12),
    _XioHubRdNumReq_Type()
)
xioHubRdNumReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubRdNumReq.setStatus("mandatory")
_XioHubRdQueDepth_Type = Integer32
_XioHubRdQueDepth_Object = MibTableColumn
xioHubRdQueDepth = _XioHubRdQueDepth_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 5, 1, 1, 13),
    _XioHubRdQueDepth_Type()
)
xioHubRdQueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubRdQueDepth.setStatus("mandatory")
_XioHubRdKBytesPS_Type = Integer32
_XioHubRdKBytesPS_Object = MibTableColumn
xioHubRdKBytesPS = _XioHubRdKBytesPS_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 5, 1, 1, 14),
    _XioHubRdKBytesPS_Type()
)
xioHubRdKBytesPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubRdKBytesPS.setStatus("mandatory")
_XioHubRdPhysDevTable_Object = MibTable
xioHubRdPhysDevTable = _XioHubRdPhysDevTable_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 5, 2)
)
if mibBuilder.loadTexts:
    xioHubRdPhysDevTable.setStatus("mandatory")
_XioHubRdPhysDevEntry_Object = MibTableRow
xioHubRdPhysDevEntry = _XioHubRdPhysDevEntry_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 5, 2, 1)
)
xioHubRdPhysDevEntry.setIndexNames(
    (0, "XIO-HUB-MIB", "xioHubRdRaidDevId"),
)
if mibBuilder.loadTexts:
    xioHubRdPhysDevEntry.setStatus("mandatory")
_XioHubRdRaidDevId_Type = Integer32
_XioHubRdRaidDevId_Object = MibTableColumn
xioHubRdRaidDevId = _XioHubRdRaidDevId_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 5, 2, 1, 1),
    _XioHubRdRaidDevId_Type()
)
xioHubRdRaidDevId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubRdRaidDevId.setStatus("mandatory")
_XioHubRdChannel_Type = Integer32
_XioHubRdChannel_Object = MibTableColumn
xioHubRdChannel = _XioHubRdChannel_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 5, 2, 1, 2),
    _XioHubRdChannel_Type()
)
xioHubRdChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubRdChannel.setStatus("mandatory")
_XioHubRdScsiId_Type = Integer32
_XioHubRdScsiId_Object = MibTableColumn
xioHubRdScsiId = _XioHubRdScsiId_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 5, 2, 1, 3),
    _XioHubRdScsiId_Type()
)
xioHubRdScsiId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubRdScsiId.setStatus("mandatory")
_XioHubRdDevInRaid_Type = Integer32
_XioHubRdDevInRaid_Object = MibTableColumn
xioHubRdDevInRaid = _XioHubRdDevInRaid_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 5, 2, 1, 4),
    _XioHubRdDevInRaid_Type()
)
xioHubRdDevInRaid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubRdDevInRaid.setStatus("mandatory")
_XioHubRdDevRebuild_Type = Integer32
_XioHubRdDevRebuild_Object = MibTableColumn
xioHubRdDevRebuild = _XioHubRdDevRebuild_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 5, 2, 1, 5),
    _XioHubRdDevRebuild_Type()
)
xioHubRdDevRebuild.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubRdDevRebuild.setStatus("mandatory")
_XioHubRdDevFailed_Type = Integer32
_XioHubRdDevFailed_Object = MibTableColumn
xioHubRdDevFailed = _XioHubRdDevFailed_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 5, 2, 1, 6),
    _XioHubRdDevFailed_Type()
)
xioHubRdDevFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubRdDevFailed.setStatus("mandatory")
_XioHubVirtualDevice_ObjectIdentity = ObjectIdentity
xioHubVirtualDevice = _XioHubVirtualDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2366, 1, 6)
)
_XioHubVdVirtualDevTable_Object = MibTable
xioHubVdVirtualDevTable = _XioHubVdVirtualDevTable_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 6, 1)
)
if mibBuilder.loadTexts:
    xioHubVdVirtualDevTable.setStatus("mandatory")
_XioHubVdVirtualDevEntry_Object = MibTableRow
xioHubVdVirtualDevEntry = _XioHubVdVirtualDevEntry_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 6, 1, 1)
)
xioHubVdVirtualDevEntry.setIndexNames(
    (0, "XIO-HUB-MIB", "xioHubVdVirtualId"),
)
if mibBuilder.loadTexts:
    xioHubVdVirtualDevEntry.setStatus("mandatory")
_XioHubVdVirtualId_Type = Integer32
_XioHubVdVirtualId_Object = MibTableColumn
xioHubVdVirtualId = _XioHubVdVirtualId_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 6, 1, 1, 1),
    _XioHubVdVirtualId_Type()
)
xioHubVdVirtualId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubVdVirtualId.setStatus("mandatory")
_XioHubVdHabGroup_Type = Integer32
_XioHubVdHabGroup_Object = MibTableColumn
xioHubVdHabGroup = _XioHubVdHabGroup_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 6, 1, 1, 2),
    _XioHubVdHabGroup_Type()
)
xioHubVdHabGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubVdHabGroup.setStatus("mandatory")


class _XioHubVdDevStatus_Type(Integer32):
    """Custom type xioHubVdDevStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("copyingTo", 5),
          ("deviceOK", 2),
          ("inoperable", 4),
          ("mirroring", 6),
          ("nonExistent", 1),
          ("pausedInCopy", 7),
          ("uninitialized", 3))
    )


_XioHubVdDevStatus_Type.__name__ = "Integer32"
_XioHubVdDevStatus_Object = MibTableColumn
xioHubVdDevStatus = _XioHubVdDevStatus_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 6, 1, 1, 3),
    _XioHubVdDevStatus_Type()
)
xioHubVdDevStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubVdDevStatus.setStatus("mandatory")
_XioHubVdDevCapacity_Type = Integer32
_XioHubVdDevCapacity_Object = MibTableColumn
xioHubVdDevCapacity = _XioHubVdDevCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 6, 1, 1, 4),
    _XioHubVdDevCapacity_Type()
)
xioHubVdDevCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubVdDevCapacity.setStatus("mandatory")
_XioHubVdTotRdReq_Type = Counter32
_XioHubVdTotRdReq_Object = MibTableColumn
xioHubVdTotRdReq = _XioHubVdTotRdReq_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 6, 1, 1, 5),
    _XioHubVdTotRdReq_Type()
)
xioHubVdTotRdReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubVdTotRdReq.setStatus("mandatory")
_XioHubVdTotWrReq_Type = Counter32
_XioHubVdTotWrReq_Object = MibTableColumn
xioHubVdTotWrReq = _XioHubVdTotWrReq_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 6, 1, 1, 6),
    _XioHubVdTotWrReq_Type()
)
xioHubVdTotWrReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubVdTotWrReq.setStatus("mandatory")
_XioHubVdAvgSec_Type = Integer32
_XioHubVdAvgSec_Object = MibTableColumn
xioHubVdAvgSec = _XioHubVdAvgSec_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 6, 1, 1, 7),
    _XioHubVdAvgSec_Type()
)
xioHubVdAvgSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubVdAvgSec.setStatus("mandatory")
_XioHubVdNumReq_Type = Integer32
_XioHubVdNumReq_Object = MibTableColumn
xioHubVdNumReq = _XioHubVdNumReq_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 6, 1, 1, 8),
    _XioHubVdNumReq_Type()
)
xioHubVdNumReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubVdNumReq.setStatus("mandatory")
_XioHubVdQueDepth_Type = Integer32
_XioHubVdQueDepth_Object = MibTableColumn
xioHubVdQueDepth = _XioHubVdQueDepth_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 6, 1, 1, 9),
    _XioHubVdQueDepth_Type()
)
xioHubVdQueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubVdQueDepth.setStatus("mandatory")
_XioHubVdKBytesPS_Type = Integer32
_XioHubVdKBytesPS_Object = MibTableColumn
xioHubVdKBytesPS = _XioHubVdKBytesPS_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 6, 1, 1, 10),
    _XioHubVdKBytesPS_Type()
)
xioHubVdKBytesPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubVdKBytesPS.setStatus("mandatory")
_XioHubVdAttribute_Type = Integer32
_XioHubVdAttribute_Object = MibTableColumn
xioHubVdAttribute = _XioHubVdAttribute_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 6, 1, 1, 11),
    _XioHubVdAttribute_Type()
)
xioHubVdAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubVdAttribute.setStatus("mandatory")
_XioHubVdRaidDevTable_Object = MibTable
xioHubVdRaidDevTable = _XioHubVdRaidDevTable_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 6, 2)
)
if mibBuilder.loadTexts:
    xioHubVdRaidDevTable.setStatus("mandatory")
_XioHubVdRaidDevEntry_Object = MibTableRow
xioHubVdRaidDevEntry = _XioHubVdRaidDevEntry_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 6, 2, 1)
)
xioHubVdRaidDevEntry.setIndexNames(
    (0, "XIO-HUB-MIB", "xioHubVdRaidVirtId"),
)
if mibBuilder.loadTexts:
    xioHubVdRaidDevEntry.setStatus("mandatory")
_XioHubVdRaidVirtId_Type = Integer32
_XioHubVdRaidVirtId_Object = MibTableColumn
xioHubVdRaidVirtId = _XioHubVdRaidVirtId_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 6, 2, 1, 1),
    _XioHubVdRaidVirtId_Type()
)
xioHubVdRaidVirtId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubVdRaidVirtId.setStatus("mandatory")
_XioHubVdRaidId_Type = Integer32
_XioHubVdRaidId_Object = MibTableColumn
xioHubVdRaidId = _XioHubVdRaidId_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 6, 2, 1, 2),
    _XioHubVdRaidId_Type()
)
xioHubVdRaidId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubVdRaidId.setStatus("mandatory")
_XioHubVdRaidExists_Type = Integer32
_XioHubVdRaidExists_Object = MibTableColumn
xioHubVdRaidExists = _XioHubVdRaidExists_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 6, 2, 1, 3),
    _XioHubVdRaidExists_Type()
)
xioHubVdRaidExists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubVdRaidExists.setStatus("mandatory")
_XioHubVdCacheInfoTable_Object = MibTable
xioHubVdCacheInfoTable = _XioHubVdCacheInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 6, 3)
)
if mibBuilder.loadTexts:
    xioHubVdCacheInfoTable.setStatus("mandatory")
_XioHubVdCacheInfoEntry_Object = MibTableRow
xioHubVdCacheInfoEntry = _XioHubVdCacheInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 6, 3, 1)
)
xioHubVdCacheInfoEntry.setIndexNames(
    (0, "XIO-HUB-MIB", "xioHubVdCacheVirtId"),
)
if mibBuilder.loadTexts:
    xioHubVdCacheInfoEntry.setStatus("mandatory")
_XioHubVdCacheVirtId_Type = Integer32
_XioHubVdCacheVirtId_Object = MibTableColumn
xioHubVdCacheVirtId = _XioHubVdCacheVirtId_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 6, 3, 1, 1),
    _XioHubVdCacheVirtId_Type()
)
xioHubVdCacheVirtId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubVdCacheVirtId.setStatus("mandatory")
_XioHubVdCacheEnabled_Type = Integer32
_XioHubVdCacheEnabled_Object = MibTableColumn
xioHubVdCacheEnabled = _XioHubVdCacheEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 6, 3, 1, 2),
    _XioHubVdCacheEnabled_Type()
)
xioHubVdCacheEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubVdCacheEnabled.setStatus("mandatory")
_XioHubVdReadHits_Type = Counter32
_XioHubVdReadHits_Object = MibTableColumn
xioHubVdReadHits = _XioHubVdReadHits_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 6, 3, 1, 3),
    _XioHubVdReadHits_Type()
)
xioHubVdReadHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubVdReadHits.setStatus("mandatory")
_XioHubVdReadMiss_Type = Counter32
_XioHubVdReadMiss_Object = MibTableColumn
xioHubVdReadMiss = _XioHubVdReadMiss_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 6, 3, 1, 4),
    _XioHubVdReadMiss_Type()
)
xioHubVdReadMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubVdReadMiss.setStatus("mandatory")
_XioHubVdWriteHits_Type = Counter32
_XioHubVdWriteHits_Object = MibTableColumn
xioHubVdWriteHits = _XioHubVdWriteHits_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 6, 3, 1, 5),
    _XioHubVdWriteHits_Type()
)
xioHubVdWriteHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubVdWriteHits.setStatus("mandatory")
_XioHubVdWriteMiss_Type = Counter32
_XioHubVdWriteMiss_Object = MibTableColumn
xioHubVdWriteMiss = _XioHubVdWriteMiss_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 6, 3, 1, 6),
    _XioHubVdWriteMiss_Type()
)
xioHubVdWriteMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubVdWriteMiss.setStatus("mandatory")
_XioHubCacheInfo_ObjectIdentity = ObjectIdentity
xioHubCacheInfo = _XioHubCacheInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2366, 1, 7)
)


class _XioHubCiStatus_Type(Integer32):
    """Custom type xioHubCiStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("deviceOK", 2),
          ("hwFailure", 4),
          ("noPower", 3),
          ("notInstalled", 1))
    )


_XioHubCiStatus_Type.__name__ = "Integer32"
_XioHubCiStatus_Object = MibScalar
xioHubCiStatus = _XioHubCiStatus_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 7, 1),
    _XioHubCiStatus_Type()
)
xioHubCiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubCiStatus.setStatus("mandatory")
_XioHubCiCacheSize_Type = Integer32
_XioHubCiCacheSize_Object = MibScalar
xioHubCiCacheSize = _XioHubCiCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 7, 2),
    _XioHubCiCacheSize_Type()
)
xioHubCiCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubCiCacheSize.setStatus("mandatory")
_XioHubCiMaxCacheable_Type = Integer32
_XioHubCiMaxCacheable_Object = MibScalar
xioHubCiMaxCacheable = _XioHubCiMaxCacheable_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 7, 3),
    _XioHubCiMaxCacheable_Type()
)
xioHubCiMaxCacheable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubCiMaxCacheable.setStatus("mandatory")
_XioHubCiNumWrBacks_Type = Integer32
_XioHubCiNumWrBacks_Object = MibScalar
xioHubCiNumWrBacks = _XioHubCiNumWrBacks_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 7, 4),
    _XioHubCiNumWrBacks_Type()
)
xioHubCiNumWrBacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubCiNumWrBacks.setStatus("mandatory")
_XioHubCiFreeBuffers_Type = Integer32
_XioHubCiFreeBuffers_Object = MibScalar
xioHubCiFreeBuffers = _XioHubCiFreeBuffers_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 7, 5),
    _XioHubCiFreeBuffers_Type()
)
xioHubCiFreeBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubCiFreeBuffers.setStatus("mandatory")
_XioHubCiCleanBuffers_Type = Integer32
_XioHubCiCleanBuffers_Object = MibScalar
xioHubCiCleanBuffers = _XioHubCiCleanBuffers_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 7, 6),
    _XioHubCiCleanBuffers_Type()
)
xioHubCiCleanBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubCiCleanBuffers.setStatus("mandatory")
_XioHubCiDirtyBuffers_Type = Integer32
_XioHubCiDirtyBuffers_Object = MibScalar
xioHubCiDirtyBuffers = _XioHubCiDirtyBuffers_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 7, 7),
    _XioHubCiDirtyBuffers_Type()
)
xioHubCiDirtyBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubCiDirtyBuffers.setStatus("mandatory")
_XioHubHabInfo_ObjectIdentity = ObjectIdentity
xioHubHabInfo = _XioHubHabInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2366, 1, 8)
)
_XioHubHiHabInfoTable_Object = MibTable
xioHubHiHabInfoTable = _XioHubHiHabInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 8, 1)
)
if mibBuilder.loadTexts:
    xioHubHiHabInfoTable.setStatus("mandatory")
_XioHubHiHabInfoEntry_Object = MibTableRow
xioHubHiHabInfoEntry = _XioHubHiHabInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 8, 1, 1)
)
xioHubHiHabInfoEntry.setIndexNames(
    (0, "XIO-HUB-MIB", "xioHubHiHabId"),
)
if mibBuilder.loadTexts:
    xioHubHiHabInfoEntry.setStatus("mandatory")


class _XioHubHiStatus_Type(Integer32):
    """Custom type xioHubHiStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("deviceNotInstalled", 1),
          ("deviceOK", 2),
          ("failed", 3))
    )


_XioHubHiStatus_Type.__name__ = "Integer32"
_XioHubHiStatus_Object = MibTableColumn
xioHubHiStatus = _XioHubHiStatus_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 8, 1, 1, 1),
    _XioHubHiStatus_Type()
)
xioHubHiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubHiStatus.setStatus("mandatory")
_XioHubHiHabId_Type = Integer32
_XioHubHiHabId_Object = MibTableColumn
xioHubHiHabId = _XioHubHiHabId_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 8, 1, 1, 2),
    _XioHubHiHabId_Type()
)
xioHubHiHabId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubHiHabId.setStatus("mandatory")


class _XioHubHiHabGroup_Type(Integer32):
    """Custom type xioHubHiHabGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            255
        )
    )
    namedValues = NamedValues(
        ("unassigned", 255)
    )


_XioHubHiHabGroup_Type.__name__ = "Integer32"
_XioHubHiHabGroup_Object = MibTableColumn
xioHubHiHabGroup = _XioHubHiHabGroup_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 8, 1, 1, 3),
    _XioHubHiHabGroup_Type()
)
xioHubHiHabGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubHiHabGroup.setStatus("mandatory")


class _XioHubHiServerName_Type(DisplayString):
    """Custom type xioHubHiServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_XioHubHiServerName_Type.__name__ = "DisplayString"
_XioHubHiServerName_Object = MibTableColumn
xioHubHiServerName = _XioHubHiServerName_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 8, 1, 1, 4),
    _XioHubHiServerName_Type()
)
xioHubHiServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubHiServerName.setStatus("mandatory")
_XioHubBusInfo_ObjectIdentity = ObjectIdentity
xioHubBusInfo = _XioHubBusInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2366, 1, 9)
)
_XioHubBiBusInfoTable_Object = MibTable
xioHubBiBusInfoTable = _XioHubBiBusInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 9, 1)
)
if mibBuilder.loadTexts:
    xioHubBiBusInfoTable.setStatus("mandatory")
_XioHubBiBusInfoEntry_Object = MibTableRow
xioHubBiBusInfoEntry = _XioHubBiBusInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 9, 1, 1)
)
xioHubBiBusInfoEntry.setIndexNames(
    (0, "XIO-HUB-MIB", "xioHubBiChannel"),
)
if mibBuilder.loadTexts:
    xioHubBiBusInfoEntry.setStatus("mandatory")
_XioHubBiChannel_Type = Integer32
_XioHubBiChannel_Object = MibTableColumn
xioHubBiChannel = _XioHubBiChannel_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 9, 1, 1, 1),
    _XioHubBiChannel_Type()
)
xioHubBiChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubBiChannel.setStatus("mandatory")
_XioHubBiTotRdReq_Type = Counter32
_XioHubBiTotRdReq_Object = MibTableColumn
xioHubBiTotRdReq = _XioHubBiTotRdReq_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 9, 1, 1, 2),
    _XioHubBiTotRdReq_Type()
)
xioHubBiTotRdReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubBiTotRdReq.setStatus("mandatory")
_XioHubBiTotWrReq_Type = Counter32
_XioHubBiTotWrReq_Object = MibTableColumn
xioHubBiTotWrReq = _XioHubBiTotWrReq_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 9, 1, 1, 3),
    _XioHubBiTotWrReq_Type()
)
xioHubBiTotWrReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubBiTotWrReq.setStatus("mandatory")
_XioHubBiTotCorrectErr_Type = Counter32
_XioHubBiTotCorrectErr_Object = MibTableColumn
xioHubBiTotCorrectErr = _XioHubBiTotCorrectErr_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 9, 1, 1, 4),
    _XioHubBiTotCorrectErr_Type()
)
xioHubBiTotCorrectErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubBiTotCorrectErr.setStatus("mandatory")
_XioHubBiAvgSec_Type = Integer32
_XioHubBiAvgSec_Object = MibTableColumn
xioHubBiAvgSec = _XioHubBiAvgSec_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 9, 1, 1, 5),
    _XioHubBiAvgSec_Type()
)
xioHubBiAvgSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubBiAvgSec.setStatus("mandatory")
_XioHubBiNumReq_Type = Integer32
_XioHubBiNumReq_Object = MibTableColumn
xioHubBiNumReq = _XioHubBiNumReq_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 9, 1, 1, 6),
    _XioHubBiNumReq_Type()
)
xioHubBiNumReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubBiNumReq.setStatus("mandatory")
_XioHubBiQueDepth_Type = Integer32
_XioHubBiQueDepth_Object = MibTableColumn
xioHubBiQueDepth = _XioHubBiQueDepth_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 9, 1, 1, 7),
    _XioHubBiQueDepth_Type()
)
xioHubBiQueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubBiQueDepth.setStatus("mandatory")
_XioHubBiKBytesPS_Type = Integer32
_XioHubBiKBytesPS_Object = MibTableColumn
xioHubBiKBytesPS = _XioHubBiKBytesPS_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 9, 1, 1, 8),
    _XioHubBiKBytesPS_Type()
)
xioHubBiKBytesPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubBiKBytesPS.setStatus("mandatory")
_XioHubTrapVariables_ObjectIdentity = ObjectIdentity
xioHubTrapVariables = _XioHubTrapVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2366, 1, 10)
)


class _XioHubTvEventNum_Type(DisplayString):
    """Custom type xioHubTvEventNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_XioHubTvEventNum_Type.__name__ = "DisplayString"
_XioHubTvEventNum_Object = MibScalar
xioHubTvEventNum = _XioHubTvEventNum_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 10, 1),
    _XioHubTvEventNum_Type()
)
xioHubTvEventNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubTvEventNum.setStatus("mandatory")


class _XioHubTvTimestamp_Type(DisplayString):
    """Custom type xioHubTvTimestamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_XioHubTvTimestamp_Type.__name__ = "DisplayString"
_XioHubTvTimestamp_Object = MibScalar
xioHubTvTimestamp = _XioHubTvTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 10, 2),
    _XioHubTvTimestamp_Type()
)
xioHubTvTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubTvTimestamp.setStatus("mandatory")
_XioHubTvType_Type = Integer32
_XioHubTvType_Object = MibScalar
xioHubTvType = _XioHubTvType_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 10, 3),
    _XioHubTvType_Type()
)
xioHubTvType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubTvType.setStatus("mandatory")
_XioHubTvExtType_Type = Integer32
_XioHubTvExtType_Object = MibScalar
xioHubTvExtType = _XioHubTvExtType_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 10, 4),
    _XioHubTvExtType_Type()
)
xioHubTvExtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubTvExtType.setStatus("mandatory")
_XioHubTvFlags_Type = Integer32
_XioHubTvFlags_Object = MibScalar
xioHubTvFlags = _XioHubTvFlags_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 10, 5),
    _XioHubTvFlags_Type()
)
xioHubTvFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubTvFlags.setStatus("mandatory")
_XioHubTvLedStatus_Type = Integer32
_XioHubTvLedStatus_Object = MibScalar
xioHubTvLedStatus = _XioHubTvLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 10, 6),
    _XioHubTvLedStatus_Type()
)
xioHubTvLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubTvLedStatus.setStatus("mandatory")


class _XioHubTvMessage_Type(DisplayString):
    """Custom type xioHubTvMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_XioHubTvMessage_Type.__name__ = "DisplayString"
_XioHubTvMessage_Object = MibScalar
xioHubTvMessage = _XioHubTvMessage_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 10, 7),
    _XioHubTvMessage_Type()
)
xioHubTvMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubTvMessage.setStatus("mandatory")


class _XioHubTvAddress_Type(DisplayString):
    """Custom type xioHubTvAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_XioHubTvAddress_Type.__name__ = "DisplayString"
_XioHubTvAddress_Object = MibScalar
xioHubTvAddress = _XioHubTvAddress_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 10, 8),
    _XioHubTvAddress_Type()
)
xioHubTvAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubTvAddress.setStatus("mandatory")


class _XioHubTvHubName_Type(DisplayString):
    """Custom type xioHubTvHubName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_XioHubTvHubName_Type.__name__ = "DisplayString"
_XioHubTvHubName_Object = MibScalar
xioHubTvHubName = _XioHubTvHubName_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 10, 9),
    _XioHubTvHubName_Type()
)
xioHubTvHubName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubTvHubName.setStatus("mandatory")
_XioHubTraps_ObjectIdentity = ObjectIdentity
xioHubTraps = _XioHubTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2366, 1, 20)
)
_XioHubLoadInfo_ObjectIdentity = ObjectIdentity
xioHubLoadInfo = _XioHubLoadInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2366, 1, 30)
)
_XioHubLiProcUsed_Type = Integer32
_XioHubLiProcUsed_Object = MibScalar
xioHubLiProcUsed = _XioHubLiProcUsed_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 30, 1),
    _XioHubLiProcUsed_Type()
)
xioHubLiProcUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubLiProcUsed.setStatus("mandatory")
_XioHubLiFHabTable_Object = MibTable
xioHubLiFHabTable = _XioHubLiFHabTable_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 30, 2)
)
if mibBuilder.loadTexts:
    xioHubLiFHabTable.setStatus("mandatory")
_XioHubLiFHabEntry_Object = MibTableRow
xioHubLiFHabEntry = _XioHubLiFHabEntry_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 30, 2, 1)
)
xioHubLiFHabEntry.setIndexNames(
    (0, "XIO-HUB-MIB", "xioHubLiIndex"),
)
if mibBuilder.loadTexts:
    xioHubLiFHabEntry.setStatus("mandatory")
_XioHubLiFHabUsed_Type = Integer32
_XioHubLiFHabUsed_Object = MibTableColumn
xioHubLiFHabUsed = _XioHubLiFHabUsed_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 30, 2, 1, 1),
    _XioHubLiFHabUsed_Type()
)
xioHubLiFHabUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubLiFHabUsed.setStatus("mandatory")
_XioHubLiFHabMbs_Type = Integer32
_XioHubLiFHabMbs_Object = MibTableColumn
xioHubLiFHabMbs = _XioHubLiFHabMbs_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 30, 2, 1, 2),
    _XioHubLiFHabMbs_Type()
)
xioHubLiFHabMbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubLiFHabMbs.setStatus("mandatory")
_XioHubLiFHabIOs_Type = Integer32
_XioHubLiFHabIOs_Object = MibTableColumn
xioHubLiFHabIOs = _XioHubLiFHabIOs_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 30, 2, 1, 3),
    _XioHubLiFHabIOs_Type()
)
xioHubLiFHabIOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubLiFHabIOs.setStatus("mandatory")
_XioHubLiIndex_Type = Integer32
_XioHubLiIndex_Object = MibTableColumn
xioHubLiIndex = _XioHubLiIndex_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 30, 2, 1, 4),
    _XioHubLiIndex_Type()
)
xioHubLiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubLiIndex.setStatus("mandatory")
_XioHubStorageDevList_ObjectIdentity = ObjectIdentity
xioHubStorageDevList = _XioHubStorageDevList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2366, 1, 40)
)
_XioHubStDevListNum_Type = Integer32
_XioHubStDevListNum_Object = MibScalar
xioHubStDevListNum = _XioHubStDevListNum_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 40, 1),
    _XioHubStDevListNum_Type()
)
xioHubStDevListNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubStDevListNum.setStatus("mandatory")
_XioHubStDevListSNTable_Object = MibTable
xioHubStDevListSNTable = _XioHubStDevListSNTable_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 40, 2)
)
if mibBuilder.loadTexts:
    xioHubStDevListSNTable.setStatus("mandatory")
_XioHubStDevListSNEntry_Object = MibTableRow
xioHubStDevListSNEntry = _XioHubStDevListSNEntry_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 40, 2, 1)
)
xioHubStDevListSNEntry.setIndexNames(
    (0, "XIO-HUB-MIB", "xioHubStDevSNIndex"),
)
if mibBuilder.loadTexts:
    xioHubStDevListSNEntry.setStatus("mandatory")
_XioHubStDevListSNum_Type = Integer32
_XioHubStDevListSNum_Object = MibTableColumn
xioHubStDevListSNum = _XioHubStDevListSNum_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 40, 2, 1, 1),
    _XioHubStDevListSNum_Type()
)
xioHubStDevListSNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubStDevListSNum.setStatus("mandatory")
_XioHubStDevSNIndex_Type = Integer32
_XioHubStDevSNIndex_Object = MibTableColumn
xioHubStDevSNIndex = _XioHubStDevSNIndex_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 40, 2, 1, 2),
    _XioHubStDevSNIndex_Type()
)
xioHubStDevSNIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubStDevSNIndex.setStatus("mandatory")
_XioHubStDevListNTable_Object = MibTable
xioHubStDevListNTable = _XioHubStDevListNTable_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 40, 3)
)
if mibBuilder.loadTexts:
    xioHubStDevListNTable.setStatus("mandatory")
_XioHubStDevListNEntry_Object = MibTableRow
xioHubStDevListNEntry = _XioHubStDevListNEntry_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 40, 3, 1)
)
xioHubStDevListNEntry.setIndexNames(
    (0, "XIO-HUB-MIB", "xioHubStDevNIndex"),
)
if mibBuilder.loadTexts:
    xioHubStDevListNEntry.setStatus("mandatory")


class _XioHubStDevListName_Type(DisplayString):
    """Custom type xioHubStDevListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_XioHubStDevListName_Type.__name__ = "DisplayString"
_XioHubStDevListName_Object = MibTableColumn
xioHubStDevListName = _XioHubStDevListName_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 40, 3, 1, 1),
    _XioHubStDevListName_Type()
)
xioHubStDevListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubStDevListName.setStatus("mandatory")
_XioHubStDevNIndex_Type = Integer32
_XioHubStDevNIndex_Object = MibTableColumn
xioHubStDevNIndex = _XioHubStDevNIndex_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 40, 3, 1, 2),
    _XioHubStDevNIndex_Type()
)
xioHubStDevNIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubStDevNIndex.setStatus("mandatory")
_XioHubStDevListATable_Object = MibTable
xioHubStDevListATable = _XioHubStDevListATable_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 40, 4)
)
if mibBuilder.loadTexts:
    xioHubStDevListATable.setStatus("mandatory")
_XioHubStDevListAEntry_Object = MibTableRow
xioHubStDevListAEntry = _XioHubStDevListAEntry_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 40, 4, 1)
)
xioHubStDevListAEntry.setIndexNames(
    (0, "XIO-HUB-MIB", "xioHubStDevAIndex"),
)
if mibBuilder.loadTexts:
    xioHubStDevListAEntry.setStatus("mandatory")


class _XioHubStDevListAddr_Type(DisplayString):
    """Custom type xioHubStDevListAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_XioHubStDevListAddr_Type.__name__ = "DisplayString"
_XioHubStDevListAddr_Object = MibTableColumn
xioHubStDevListAddr = _XioHubStDevListAddr_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 40, 4, 1, 1),
    _XioHubStDevListAddr_Type()
)
xioHubStDevListAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubStDevListAddr.setStatus("mandatory")
_XioHubStDevAIndex_Type = Integer32
_XioHubStDevAIndex_Object = MibTableColumn
xioHubStDevAIndex = _XioHubStDevAIndex_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 40, 4, 1, 2),
    _XioHubStDevAIndex_Type()
)
xioHubStDevAIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubStDevAIndex.setStatus("mandatory")
_XioHubVpInfo_ObjectIdentity = ObjectIdentity
xioHubVpInfo = _XioHubVpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2366, 1, 50)
)
_XioHubVpInfoTable_Object = MibTable
xioHubVpInfoTable = _XioHubVpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 50, 1)
)
if mibBuilder.loadTexts:
    xioHubVpInfoTable.setStatus("mandatory")
_XioHubVpInfoEntry_Object = MibTableRow
xioHubVpInfoEntry = _XioHubVpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 50, 1, 1)
)
xioHubVpInfoEntry.setIndexNames(
    (0, "XIO-HUB-MIB", "xioHubVpId"),
)
if mibBuilder.loadTexts:
    xioHubVpInfoEntry.setStatus("mandatory")
_XioHubVpKBS_Type = Integer32
_XioHubVpKBS_Object = MibTableColumn
xioHubVpKBS = _XioHubVpKBS_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 50, 1, 1, 1),
    _XioHubVpKBS_Type()
)
xioHubVpKBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubVpKBS.setStatus("mandatory")
_XioHubVpIOs_Type = Integer32
_XioHubVpIOs_Object = MibTableColumn
xioHubVpIOs = _XioHubVpIOs_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 50, 1, 1, 2),
    _XioHubVpIOs_Type()
)
xioHubVpIOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubVpIOs.setStatus("mandatory")
_XioHubVpId_Type = Integer32
_XioHubVpId_Object = MibTableColumn
xioHubVpId = _XioHubVpId_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 50, 1, 1, 3),
    _XioHubVpId_Type()
)
xioHubVpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubVpId.setStatus("mandatory")
_XioHubPpInfo_ObjectIdentity = ObjectIdentity
xioHubPpInfo = _XioHubPpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2366, 1, 60)
)
_XioHubPpInfoTable_Object = MibTable
xioHubPpInfoTable = _XioHubPpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 60, 1)
)
if mibBuilder.loadTexts:
    xioHubPpInfoTable.setStatus("mandatory")
_XioHubPpInfoEntry_Object = MibTableRow
xioHubPpInfoEntry = _XioHubPpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 60, 1, 1)
)
xioHubPpInfoEntry.setIndexNames(
    (0, "XIO-HUB-MIB", "xioHubPpId"),
)
if mibBuilder.loadTexts:
    xioHubPpInfoEntry.setStatus("mandatory")
_XioHubPpKBS_Type = Integer32
_XioHubPpKBS_Object = MibTableColumn
xioHubPpKBS = _XioHubPpKBS_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 60, 1, 1, 1),
    _XioHubPpKBS_Type()
)
xioHubPpKBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubPpKBS.setStatus("mandatory")
_XioHubPpIOs_Type = Integer32
_XioHubPpIOs_Object = MibTableColumn
xioHubPpIOs = _XioHubPpIOs_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 60, 1, 1, 2),
    _XioHubPpIOs_Type()
)
xioHubPpIOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubPpIOs.setStatus("mandatory")
_XioHubPpId_Type = Integer32
_XioHubPpId_Object = MibTableColumn
xioHubPpId = _XioHubPpId_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 60, 1, 1, 3),
    _XioHubPpId_Type()
)
xioHubPpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubPpId.setStatus("mandatory")
_XioHubSvInfo_ObjectIdentity = ObjectIdentity
xioHubSvInfo = _XioHubSvInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2366, 1, 70)
)
_XioHubSvInfoTable_Object = MibTable
xioHubSvInfoTable = _XioHubSvInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 70, 1)
)
if mibBuilder.loadTexts:
    xioHubSvInfoTable.setStatus("mandatory")
_XioHubSvInfoEntry_Object = MibTableRow
xioHubSvInfoEntry = _XioHubSvInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 70, 1, 1)
)
xioHubSvInfoEntry.setIndexNames(
    (0, "XIO-HUB-MIB", "xioHubSvId"),
)
if mibBuilder.loadTexts:
    xioHubSvInfoEntry.setStatus("mandatory")
_XioHubSvClusterId_Type = Integer32
_XioHubSvClusterId_Object = MibTableColumn
xioHubSvClusterId = _XioHubSvClusterId_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 70, 1, 1, 1),
    _XioHubSvClusterId_Type()
)
xioHubSvClusterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubSvClusterId.setStatus("mandatory")
_XioHubSvFCalId_Type = Integer32
_XioHubSvFCalId_Object = MibTableColumn
xioHubSvFCalId = _XioHubSvFCalId_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 70, 1, 1, 2),
    _XioHubSvFCalId_Type()
)
xioHubSvFCalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubSvFCalId.setStatus("mandatory")
_XioHubSvVDiskId_Type = Integer32
_XioHubSvVDiskId_Object = MibTableColumn
xioHubSvVDiskId = _XioHubSvVDiskId_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 70, 1, 1, 3),
    _XioHubSvVDiskId_Type()
)
xioHubSvVDiskId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubSvVDiskId.setStatus("mandatory")
_XioHubSvVDiskLUN_Type = Integer32
_XioHubSvVDiskLUN_Object = MibTableColumn
xioHubSvVDiskLUN = _XioHubSvVDiskLUN_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 70, 1, 1, 4),
    _XioHubSvVDiskLUN_Type()
)
xioHubSvVDiskLUN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubSvVDiskLUN.setStatus("mandatory")
_XioHubSvId_Type = Integer32
_XioHubSvId_Object = MibTableColumn
xioHubSvId = _XioHubSvId_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 70, 1, 1, 5),
    _XioHubSvId_Type()
)
xioHubSvId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubSvId.setStatus("mandatory")


class _XioHubSvName_Type(DisplayString):
    """Custom type xioHubSvName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_XioHubSvName_Type.__name__ = "DisplayString"
_XioHubSvName_Object = MibTableColumn
xioHubSvName = _XioHubSvName_Object(
    (1, 3, 6, 1, 4, 1, 2366, 1, 70, 1, 1, 6),
    _XioHubSvName_Type()
)
xioHubSvName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xioHubSvName.setStatus("mandatory")

# Managed Objects groups


# Notification objects

xioHubUnknownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2366, 1, 20, 0, 2)
)
xioHubUnknownEvent.setObjects(
      *(("XIO-HUB-MIB", "xioHubTvEventNum"),
        ("XIO-HUB-MIB", "xioHubTvTimestamp"),
        ("XIO-HUB-MIB", "xioHubTvType"),
        ("XIO-HUB-MIB", "xioHubTvExtType"),
        ("XIO-HUB-MIB", "xioHubTvFlags"),
        ("XIO-HUB-MIB", "xioHubTvLedStatus"),
        ("XIO-HUB-MIB", "xioHubTvMessage"),
        ("XIO-HUB-MIB", "xioHubTvAddress"),
        ("XIO-HUB-MIB", "xioHubTvHubName"))
)
if mibBuilder.loadTexts:
    xioHubUnknownEvent.setStatus(
        ""
    )

xioHubInfoEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2366, 1, 20, 0, 5)
)
xioHubInfoEvent.setObjects(
      *(("XIO-HUB-MIB", "xioHubTvEventNum"),
        ("XIO-HUB-MIB", "xioHubTvTimestamp"),
        ("XIO-HUB-MIB", "xioHubTvType"),
        ("XIO-HUB-MIB", "xioHubTvExtType"),
        ("XIO-HUB-MIB", "xioHubTvFlags"),
        ("XIO-HUB-MIB", "xioHubTvLedStatus"),
        ("XIO-HUB-MIB", "xioHubTvMessage"),
        ("XIO-HUB-MIB", "xioHubTvAddress"),
        ("XIO-HUB-MIB", "xioHubTvHubName"))
)
if mibBuilder.loadTexts:
    xioHubInfoEvent.setStatus(
        ""
    )

xioHubWarningEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2366, 1, 20, 0, 6)
)
xioHubWarningEvent.setObjects(
      *(("XIO-HUB-MIB", "xioHubTvEventNum"),
        ("XIO-HUB-MIB", "xioHubTvTimestamp"),
        ("XIO-HUB-MIB", "xioHubTvType"),
        ("XIO-HUB-MIB", "xioHubTvExtType"),
        ("XIO-HUB-MIB", "xioHubTvFlags"),
        ("XIO-HUB-MIB", "xioHubTvLedStatus"),
        ("XIO-HUB-MIB", "xioHubTvMessage"),
        ("XIO-HUB-MIB", "xioHubTvAddress"),
        ("XIO-HUB-MIB", "xioHubTvHubName"))
)
if mibBuilder.loadTexts:
    xioHubWarningEvent.setStatus(
        ""
    )

xioHubSeriousEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2366, 1, 20, 0, 7)
)
xioHubSeriousEvent.setObjects(
      *(("XIO-HUB-MIB", "xioHubTvEventNum"),
        ("XIO-HUB-MIB", "xioHubTvTimestamp"),
        ("XIO-HUB-MIB", "xioHubTvType"),
        ("XIO-HUB-MIB", "xioHubTvExtType"),
        ("XIO-HUB-MIB", "xioHubTvFlags"),
        ("XIO-HUB-MIB", "xioHubTvLedStatus"),
        ("XIO-HUB-MIB", "xioHubTvMessage"),
        ("XIO-HUB-MIB", "xioHubTvAddress"),
        ("XIO-HUB-MIB", "xioHubTvHubName"))
)
if mibBuilder.loadTexts:
    xioHubSeriousEvent.setStatus(
        ""
    )

xioHubFatalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2366, 1, 20, 0, 8)
)
xioHubFatalEvent.setObjects(
      *(("XIO-HUB-MIB", "xioHubTvEventNum"),
        ("XIO-HUB-MIB", "xioHubTvTimestamp"),
        ("XIO-HUB-MIB", "xioHubTvType"),
        ("XIO-HUB-MIB", "xioHubTvExtType"),
        ("XIO-HUB-MIB", "xioHubTvFlags"),
        ("XIO-HUB-MIB", "xioHubTvLedStatus"),
        ("XIO-HUB-MIB", "xioHubTvMessage"),
        ("XIO-HUB-MIB", "xioHubTvAddress"),
        ("XIO-HUB-MIB", "xioHubTvHubName"))
)
if mibBuilder.loadTexts:
    xioHubFatalEvent.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XIO-HUB-MIB",
    **{"xiotech": xiotech,
       "xioHub": xioHub,
       "xioHubIdentification": xioHubIdentification,
       "xioHubHuName": xioHubHuName,
       "xioHubHuSerialNum": xioHubHuSerialNum,
       "xioHubHuCompat": xioHubHuCompat,
       "xioHubHuTCPIPAddr": xioHubHuTCPIPAddr,
       "xioHubHuHeartbeat": xioHubHuHeartbeat,
       "xioHubEnvironment": xioHubEnvironment,
       "xioHubEvUpsAc": xioHubEvUpsAc,
       "xioHubEvUpsBattLow": xioHubEvUpsBattLow,
       "xioHubEvMainPower": xioHubEvMainPower,
       "xioHubEvNumSupplies": xioHubEvNumSupplies,
       "xioHubEvNumFrontFans": xioHubEvNumFrontFans,
       "xioHubEvNumRearFans": xioHubEvNumRearFans,
       "xioHubEvMainDcPowerTable": xioHubEvMainDcPowerTable,
       "xioHubEvMainDcPowerEntry": xioHubEvMainDcPowerEntry,
       "xioHubEvDcId": xioHubEvDcId,
       "xioHubEvDcExists": xioHubEvDcExists,
       "xioHubEvDcGood": xioHubEvDcGood,
       "xioHubEvFrontFansTable": xioHubEvFrontFansTable,
       "xioHubEvFrontFansEntry": xioHubEvFrontFansEntry,
       "xioHubEvFrontFansId": xioHubEvFrontFansId,
       "xioHubEvFrontFansGood": xioHubEvFrontFansGood,
       "xioHubEvRearFansTable": xioHubEvRearFansTable,
       "xioHubEvRearFansEntry": xioHubEvRearFansEntry,
       "xioHubEvRearFansId": xioHubEvRearFansId,
       "xioHubEvRearFansGood": xioHubEvRearFansGood,
       "xioHubEvExtUpsAc": xioHubEvExtUpsAc,
       "xioHubEvExtUpsBatt": xioHubEvExtUpsBatt,
       "xioHubEvExtDcMain": xioHubEvExtDcMain,
       "xioHubEvExtNumSupplies": xioHubEvExtNumSupplies,
       "xioHubEvExtNumRearFans": xioHubEvExtNumRearFans,
       "xioHubEvExtMainDcPowerTable": xioHubEvExtMainDcPowerTable,
       "xioHubEvExtMainDcPowerEntry": xioHubEvExtMainDcPowerEntry,
       "xioHubEvExtDcId": xioHubEvExtDcId,
       "xioHubEvExtDcExists": xioHubEvExtDcExists,
       "xioHubEvExtDcGood": xioHubEvExtDcGood,
       "xioHubEvExtRearFansTable": xioHubEvExtRearFansTable,
       "xioHubEvExtRearFansEntry": xioHubEvExtRearFansEntry,
       "xioHubEvExtRearFansId": xioHubEvExtRearFansId,
       "xioHubEvExtRearFansGood": xioHubEvExtRearFansGood,
       "xioHubEvHabTempsTable": xioHubEvHabTempsTable,
       "xioHubEvHabTempsEntry": xioHubEvHabTempsEntry,
       "xioHubEvHabId": xioHubEvHabId,
       "xioHubEvHabInstalled": xioHubEvHabInstalled,
       "xioHubEvHubHabTemp": xioHubEvHubHabTemp,
       "xioHubEvServerHabTemp": xioHubEvServerHabTemp,
       "xioHubEvProcessorTemp": xioHubEvProcessorTemp,
       "xioHubEvCacheTemp": xioHubEvCacheTemp,
       "xioHubEvIsaTemp": xioHubEvIsaTemp,
       "xioHubEvRearTemp": xioHubEvRearTemp,
       "xioHubEvExtCabinetTemp": xioHubEvExtCabinetTemp,
       "xioHubEvKBsPerSec": xioHubEvKBsPerSec,
       "xioHubEvIOsPerSec": xioHubEvIOsPerSec,
       "xioHubStatusData": xioHubStatusData,
       "xioHubSdEmbedPcState": xioHubSdEmbedPcState,
       "xioHubSdControllerState": xioHubSdControllerState,
       "xioHubSdCacheState": xioHubSdCacheState,
       "xioHubSdHabStatusTable": xioHubSdHabStatusTable,
       "xioHubSdHabStatusEntry": xioHubSdHabStatusEntry,
       "xioHubSdHabId": xioHubSdHabId,
       "xioHubSdHabInstalled": xioHubSdHabInstalled,
       "xioHubSdHubHabState": xioHubSdHubHabState,
       "xioHubSdServerHabState": xioHubSdServerHabState,
       "xioHubSdServerInfoTable": xioHubSdServerInfoTable,
       "xioHubSdServerInfoEntry": xioHubSdServerInfoEntry,
       "xioHubSdServerId": xioHubSdServerId,
       "xioHubSdServerStates": xioHubSdServerStates,
       "xioHubPhysicalDevice": xioHubPhysicalDevice,
       "xioHubPdPhysDevTable": xioHubPdPhysDevTable,
       "xioHubPdPhysDevEntry": xioHubPdPhysDevEntry,
       "xioHubPdIndex": xioHubPdIndex,
       "xioHubPdChannel": xioHubPdChannel,
       "xioHubPdScsiId": xioHubPdScsiId,
       "xioHubPdClass": xioHubPdClass,
       "xioHubPdDevName": xioHubPdDevName,
       "xioHubPdSerialNum": xioHubPdSerialNum,
       "xioHubPdPostStatus": xioHubPdPostStatus,
       "xioHubPdDevStatus": xioHubPdDevStatus,
       "xioHubPdDevCapacity": xioHubPdDevCapacity,
       "xioHubPdProductId": xioHubPdProductId,
       "xioHubPdVendorId": xioHubPdVendorId,
       "xioHubPdProductRev": xioHubPdProductRev,
       "xioHubPdSerialNo": xioHubPdSerialNo,
       "xioHubPdTotAvail": xioHubPdTotAvail,
       "xioHubPdLargestAvail": xioHubPdLargestAvail,
       "xioHubPdTotRdReq": xioHubPdTotRdReq,
       "xioHubPdTotWrReq": xioHubPdTotWrReq,
       "xioHubPdTotCorrectErr": xioHubPdTotCorrectErr,
       "xioHubPdAvgSec": xioHubPdAvgSec,
       "xioHubPdNumReq": xioHubPdNumReq,
       "xioHubPdQueDepth": xioHubPdQueDepth,
       "xioHubPdKBytesPS": xioHubPdKBytesPS,
       "xioHubRaidDevice": xioHubRaidDevice,
       "xioHubRdRaidDevTable": xioHubRdRaidDevTable,
       "xioHubRdRaidDevEntry": xioHubRdRaidDevEntry,
       "xioHubRdRaidId": xioHubRdRaidId,
       "xioHubRdClass": xioHubRdClass,
       "xioHubRdDevStatus": xioHubRdDevStatus,
       "xioHubRdDepthMirror": xioHubRdDepthMirror,
       "xioHubRdDevStripe": xioHubRdDevStripe,
       "xioHubRdDevCapacity": xioHubRdDevCapacity,
       "xioHubRdNumSectors": xioHubRdNumSectors,
       "xioHubRdTotRdReq": xioHubRdTotRdReq,
       "xioHubRdTotWrReq": xioHubRdTotWrReq,
       "xioHubRdTotCorrectErr": xioHubRdTotCorrectErr,
       "xioHubRdAvgSec": xioHubRdAvgSec,
       "xioHubRdNumReq": xioHubRdNumReq,
       "xioHubRdQueDepth": xioHubRdQueDepth,
       "xioHubRdKBytesPS": xioHubRdKBytesPS,
       "xioHubRdPhysDevTable": xioHubRdPhysDevTable,
       "xioHubRdPhysDevEntry": xioHubRdPhysDevEntry,
       "xioHubRdRaidDevId": xioHubRdRaidDevId,
       "xioHubRdChannel": xioHubRdChannel,
       "xioHubRdScsiId": xioHubRdScsiId,
       "xioHubRdDevInRaid": xioHubRdDevInRaid,
       "xioHubRdDevRebuild": xioHubRdDevRebuild,
       "xioHubRdDevFailed": xioHubRdDevFailed,
       "xioHubVirtualDevice": xioHubVirtualDevice,
       "xioHubVdVirtualDevTable": xioHubVdVirtualDevTable,
       "xioHubVdVirtualDevEntry": xioHubVdVirtualDevEntry,
       "xioHubVdVirtualId": xioHubVdVirtualId,
       "xioHubVdHabGroup": xioHubVdHabGroup,
       "xioHubVdDevStatus": xioHubVdDevStatus,
       "xioHubVdDevCapacity": xioHubVdDevCapacity,
       "xioHubVdTotRdReq": xioHubVdTotRdReq,
       "xioHubVdTotWrReq": xioHubVdTotWrReq,
       "xioHubVdAvgSec": xioHubVdAvgSec,
       "xioHubVdNumReq": xioHubVdNumReq,
       "xioHubVdQueDepth": xioHubVdQueDepth,
       "xioHubVdKBytesPS": xioHubVdKBytesPS,
       "xioHubVdAttribute": xioHubVdAttribute,
       "xioHubVdRaidDevTable": xioHubVdRaidDevTable,
       "xioHubVdRaidDevEntry": xioHubVdRaidDevEntry,
       "xioHubVdRaidVirtId": xioHubVdRaidVirtId,
       "xioHubVdRaidId": xioHubVdRaidId,
       "xioHubVdRaidExists": xioHubVdRaidExists,
       "xioHubVdCacheInfoTable": xioHubVdCacheInfoTable,
       "xioHubVdCacheInfoEntry": xioHubVdCacheInfoEntry,
       "xioHubVdCacheVirtId": xioHubVdCacheVirtId,
       "xioHubVdCacheEnabled": xioHubVdCacheEnabled,
       "xioHubVdReadHits": xioHubVdReadHits,
       "xioHubVdReadMiss": xioHubVdReadMiss,
       "xioHubVdWriteHits": xioHubVdWriteHits,
       "xioHubVdWriteMiss": xioHubVdWriteMiss,
       "xioHubCacheInfo": xioHubCacheInfo,
       "xioHubCiStatus": xioHubCiStatus,
       "xioHubCiCacheSize": xioHubCiCacheSize,
       "xioHubCiMaxCacheable": xioHubCiMaxCacheable,
       "xioHubCiNumWrBacks": xioHubCiNumWrBacks,
       "xioHubCiFreeBuffers": xioHubCiFreeBuffers,
       "xioHubCiCleanBuffers": xioHubCiCleanBuffers,
       "xioHubCiDirtyBuffers": xioHubCiDirtyBuffers,
       "xioHubHabInfo": xioHubHabInfo,
       "xioHubHiHabInfoTable": xioHubHiHabInfoTable,
       "xioHubHiHabInfoEntry": xioHubHiHabInfoEntry,
       "xioHubHiStatus": xioHubHiStatus,
       "xioHubHiHabId": xioHubHiHabId,
       "xioHubHiHabGroup": xioHubHiHabGroup,
       "xioHubHiServerName": xioHubHiServerName,
       "xioHubBusInfo": xioHubBusInfo,
       "xioHubBiBusInfoTable": xioHubBiBusInfoTable,
       "xioHubBiBusInfoEntry": xioHubBiBusInfoEntry,
       "xioHubBiChannel": xioHubBiChannel,
       "xioHubBiTotRdReq": xioHubBiTotRdReq,
       "xioHubBiTotWrReq": xioHubBiTotWrReq,
       "xioHubBiTotCorrectErr": xioHubBiTotCorrectErr,
       "xioHubBiAvgSec": xioHubBiAvgSec,
       "xioHubBiNumReq": xioHubBiNumReq,
       "xioHubBiQueDepth": xioHubBiQueDepth,
       "xioHubBiKBytesPS": xioHubBiKBytesPS,
       "xioHubTrapVariables": xioHubTrapVariables,
       "xioHubTvEventNum": xioHubTvEventNum,
       "xioHubTvTimestamp": xioHubTvTimestamp,
       "xioHubTvType": xioHubTvType,
       "xioHubTvExtType": xioHubTvExtType,
       "xioHubTvFlags": xioHubTvFlags,
       "xioHubTvLedStatus": xioHubTvLedStatus,
       "xioHubTvMessage": xioHubTvMessage,
       "xioHubTvAddress": xioHubTvAddress,
       "xioHubTvHubName": xioHubTvHubName,
       "xioHubTraps": xioHubTraps,
       "xioHubUnknownEvent": xioHubUnknownEvent,
       "xioHubInfoEvent": xioHubInfoEvent,
       "xioHubWarningEvent": xioHubWarningEvent,
       "xioHubSeriousEvent": xioHubSeriousEvent,
       "xioHubFatalEvent": xioHubFatalEvent,
       "xioHubLoadInfo": xioHubLoadInfo,
       "xioHubLiProcUsed": xioHubLiProcUsed,
       "xioHubLiFHabTable": xioHubLiFHabTable,
       "xioHubLiFHabEntry": xioHubLiFHabEntry,
       "xioHubLiFHabUsed": xioHubLiFHabUsed,
       "xioHubLiFHabMbs": xioHubLiFHabMbs,
       "xioHubLiFHabIOs": xioHubLiFHabIOs,
       "xioHubLiIndex": xioHubLiIndex,
       "xioHubStorageDevList": xioHubStorageDevList,
       "xioHubStDevListNum": xioHubStDevListNum,
       "xioHubStDevListSNTable": xioHubStDevListSNTable,
       "xioHubStDevListSNEntry": xioHubStDevListSNEntry,
       "xioHubStDevListSNum": xioHubStDevListSNum,
       "xioHubStDevSNIndex": xioHubStDevSNIndex,
       "xioHubStDevListNTable": xioHubStDevListNTable,
       "xioHubStDevListNEntry": xioHubStDevListNEntry,
       "xioHubStDevListName": xioHubStDevListName,
       "xioHubStDevNIndex": xioHubStDevNIndex,
       "xioHubStDevListATable": xioHubStDevListATable,
       "xioHubStDevListAEntry": xioHubStDevListAEntry,
       "xioHubStDevListAddr": xioHubStDevListAddr,
       "xioHubStDevAIndex": xioHubStDevAIndex,
       "xioHubVpInfo": xioHubVpInfo,
       "xioHubVpInfoTable": xioHubVpInfoTable,
       "xioHubVpInfoEntry": xioHubVpInfoEntry,
       "xioHubVpKBS": xioHubVpKBS,
       "xioHubVpIOs": xioHubVpIOs,
       "xioHubVpId": xioHubVpId,
       "xioHubPpInfo": xioHubPpInfo,
       "xioHubPpInfoTable": xioHubPpInfoTable,
       "xioHubPpInfoEntry": xioHubPpInfoEntry,
       "xioHubPpKBS": xioHubPpKBS,
       "xioHubPpIOs": xioHubPpIOs,
       "xioHubPpId": xioHubPpId,
       "xioHubSvInfo": xioHubSvInfo,
       "xioHubSvInfoTable": xioHubSvInfoTable,
       "xioHubSvInfoEntry": xioHubSvInfoEntry,
       "xioHubSvClusterId": xioHubSvClusterId,
       "xioHubSvFCalId": xioHubSvFCalId,
       "xioHubSvVDiskId": xioHubSvVDiskId,
       "xioHubSvVDiskLUN": xioHubSvVDiskLUN,
       "xioHubSvId": xioHubSvId,
       "xioHubSvName": xioHubSvName}
)
