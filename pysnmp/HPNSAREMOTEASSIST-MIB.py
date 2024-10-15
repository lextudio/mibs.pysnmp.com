# SNMP MIB module (HPNSAREMOTEASSIST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPNSAREMOTEASSIST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:23 2024
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

_Hp_ObjectIdentity = ObjectIdentity
hp = _Hp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11)
)
_Nm_ObjectIdentity = ObjectIdentity
nm = _Nm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2)
)
_Hpnsa_ObjectIdentity = ObjectIdentity
hpnsa = _Hpnsa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23)
)
_HpnsaRemoteAssist_ObjectIdentity = ObjectIdentity
hpnsaRemoteAssist = _HpnsaRemoteAssist_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8)
)
_HpnsaRAMibRev_ObjectIdentity = ObjectIdentity
hpnsaRAMibRev = _HpnsaRAMibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 1)
)


class _HpnsaRAMibRevMajor_Type(Integer32):
    """Custom type hpnsaRAMibRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnsaRAMibRevMajor_Type.__name__ = "Integer32"
_HpnsaRAMibRevMajor_Object = MibScalar
hpnsaRAMibRevMajor = _HpnsaRAMibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 1, 1),
    _HpnsaRAMibRevMajor_Type()
)
hpnsaRAMibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaRAMibRevMajor.setStatus("mandatory")


class _HpnsaRAMibRevMinor_Type(Integer32):
    """Custom type hpnsaRAMibRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnsaRAMibRevMinor_Type.__name__ = "Integer32"
_HpnsaRAMibRevMinor_Object = MibScalar
hpnsaRAMibRevMinor = _HpnsaRAMibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 1, 2),
    _HpnsaRAMibRevMinor_Type()
)
hpnsaRAMibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaRAMibRevMinor.setStatus("mandatory")
_HpnsaRAAgent_ObjectIdentity = ObjectIdentity
hpnsaRAAgent = _HpnsaRAAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 2)
)
_HpnsaRAAgentTable_Object = MibTable
hpnsaRAAgentTable = _HpnsaRAAgentTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 2, 1)
)
if mibBuilder.loadTexts:
    hpnsaRAAgentTable.setStatus("mandatory")
_HpnsaRAAgentEntry_Object = MibTableRow
hpnsaRAAgentEntry = _HpnsaRAAgentEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 2, 1, 1)
)
hpnsaRAAgentEntry.setIndexNames(
    (0, "HPNSAREMOTEASSIST-MIB", "hpnsaRAAgentIndex"),
)
if mibBuilder.loadTexts:
    hpnsaRAAgentEntry.setStatus("mandatory")


class _HpnsaRAAgentIndex_Type(Integer32):
    """Custom type hpnsaRAAgentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnsaRAAgentIndex_Type.__name__ = "Integer32"
_HpnsaRAAgentIndex_Object = MibTableColumn
hpnsaRAAgentIndex = _HpnsaRAAgentIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 2, 1, 1, 1),
    _HpnsaRAAgentIndex_Type()
)
hpnsaRAAgentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaRAAgentIndex.setStatus("mandatory")


class _HpnsaRAAgentName_Type(DisplayString):
    """Custom type hpnsaRAAgentName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaRAAgentName_Type.__name__ = "DisplayString"
_HpnsaRAAgentName_Object = MibTableColumn
hpnsaRAAgentName = _HpnsaRAAgentName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 2, 1, 1, 2),
    _HpnsaRAAgentName_Type()
)
hpnsaRAAgentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaRAAgentName.setStatus("mandatory")


class _HpnsaRAAgentVersion_Type(DisplayString):
    """Custom type hpnsaRAAgentVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_HpnsaRAAgentVersion_Type.__name__ = "DisplayString"
_HpnsaRAAgentVersion_Object = MibTableColumn
hpnsaRAAgentVersion = _HpnsaRAAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 2, 1, 1, 3),
    _HpnsaRAAgentVersion_Type()
)
hpnsaRAAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaRAAgentVersion.setStatus("mandatory")


class _HpnsaRAAgentDate_Type(OctetString):
    """Custom type hpnsaRAAgentDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_HpnsaRAAgentDate_Type.__name__ = "OctetString"
_HpnsaRAAgentDate_Object = MibTableColumn
hpnsaRAAgentDate = _HpnsaRAAgentDate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 2, 1, 1, 4),
    _HpnsaRAAgentDate_Type()
)
hpnsaRAAgentDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaRAAgentDate.setStatus("mandatory")
_HpnsaRAInfo_ObjectIdentity = ObjectIdentity
hpnsaRAInfo = _HpnsaRAInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 3)
)


class _HpnsaRAInfoBoardType_Type(DisplayString):
    """Custom type hpnsaRAInfoBoardType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_HpnsaRAInfoBoardType_Type.__name__ = "DisplayString"
_HpnsaRAInfoBoardType_Object = MibScalar
hpnsaRAInfoBoardType = _HpnsaRAInfoBoardType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 3, 1),
    _HpnsaRAInfoBoardType_Type()
)
hpnsaRAInfoBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaRAInfoBoardType.setStatus("mandatory")


class _HpnsaRAInfoBoardName_Type(DisplayString):
    """Custom type hpnsaRAInfoBoardName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HpnsaRAInfoBoardName_Type.__name__ = "DisplayString"
_HpnsaRAInfoBoardName_Object = MibScalar
hpnsaRAInfoBoardName = _HpnsaRAInfoBoardName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 3, 2),
    _HpnsaRAInfoBoardName_Type()
)
hpnsaRAInfoBoardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaRAInfoBoardName.setStatus("mandatory")
_HpnsaRAInfoBoardID_Type = Integer32
_HpnsaRAInfoBoardID_Object = MibScalar
hpnsaRAInfoBoardID = _HpnsaRAInfoBoardID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 3, 3),
    _HpnsaRAInfoBoardID_Type()
)
hpnsaRAInfoBoardID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaRAInfoBoardID.setStatus("mandatory")


class _HpnsaRAInfoBoardVersion_Type(DisplayString):
    """Custom type hpnsaRAInfoBoardVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_HpnsaRAInfoBoardVersion_Type.__name__ = "DisplayString"
_HpnsaRAInfoBoardVersion_Object = MibScalar
hpnsaRAInfoBoardVersion = _HpnsaRAInfoBoardVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 3, 4),
    _HpnsaRAInfoBoardVersion_Type()
)
hpnsaRAInfoBoardVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaRAInfoBoardVersion.setStatus("mandatory")
_HpnsaRATemp_ObjectIdentity = ObjectIdentity
hpnsaRATemp = _HpnsaRATemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 4)
)
_HpnsaRATempMeasured_Type = Integer32
_HpnsaRATempMeasured_Object = MibScalar
hpnsaRATempMeasured = _HpnsaRATempMeasured_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 4, 1),
    _HpnsaRATempMeasured_Type()
)
hpnsaRATempMeasured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaRATempMeasured.setStatus("mandatory")
_HpnsaRATempWarnLimit_Type = Integer32
_HpnsaRATempWarnLimit_Object = MibScalar
hpnsaRATempWarnLimit = _HpnsaRATempWarnLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 4, 2),
    _HpnsaRATempWarnLimit_Type()
)
hpnsaRATempWarnLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaRATempWarnLimit.setStatus("mandatory")
_HpnsaRATempGracefulSDLimit_Type = Integer32
_HpnsaRATempGracefulSDLimit_Object = MibScalar
hpnsaRATempGracefulSDLimit = _HpnsaRATempGracefulSDLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 4, 3),
    _HpnsaRATempGracefulSDLimit_Type()
)
hpnsaRATempGracefulSDLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaRATempGracefulSDLimit.setStatus("mandatory")
_HpnsaRATempCriticalSDLimit_Type = Integer32
_HpnsaRATempCriticalSDLimit_Object = MibScalar
hpnsaRATempCriticalSDLimit = _HpnsaRATempCriticalSDLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 4, 4),
    _HpnsaRATempCriticalSDLimit_Type()
)
hpnsaRATempCriticalSDLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaRATempCriticalSDLimit.setStatus("mandatory")
_HpnsaRAVolt_ObjectIdentity = ObjectIdentity
hpnsaRAVolt = _HpnsaRAVolt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 5)
)
_HpnsaRAVoltTable_Object = MibTable
hpnsaRAVoltTable = _HpnsaRAVoltTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 5, 1)
)
if mibBuilder.loadTexts:
    hpnsaRAVoltTable.setStatus("mandatory")
_HpnsaRAVoltEntry_Object = MibTableRow
hpnsaRAVoltEntry = _HpnsaRAVoltEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 5, 1, 1)
)
hpnsaRAVoltEntry.setIndexNames(
    (0, "HPNSAREMOTEASSIST-MIB", "hpnsaRAVoltTypeIndex"),
)
if mibBuilder.loadTexts:
    hpnsaRAVoltEntry.setStatus("mandatory")


class _HpnsaRAVoltTypeIndex_Type(Integer32):
    """Custom type hpnsaRAVoltTypeIndex based on Integer32"""
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
        *(("negative12v", 1),
          ("positive12v", 2),
          ("positive3v", 4),
          ("positive5v", 3))
    )


_HpnsaRAVoltTypeIndex_Type.__name__ = "Integer32"
_HpnsaRAVoltTypeIndex_Object = MibTableColumn
hpnsaRAVoltTypeIndex = _HpnsaRAVoltTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 5, 1, 1, 1),
    _HpnsaRAVoltTypeIndex_Type()
)
hpnsaRAVoltTypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaRAVoltTypeIndex.setStatus("mandatory")
_HpnsaRAVoltMeasured_Type = DisplayString
_HpnsaRAVoltMeasured_Object = MibTableColumn
hpnsaRAVoltMeasured = _HpnsaRAVoltMeasured_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 5, 1, 1, 2),
    _HpnsaRAVoltMeasured_Type()
)
hpnsaRAVoltMeasured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaRAVoltMeasured.setStatus("mandatory")
_HpnsaRAVoltLoLimit_Type = DisplayString
_HpnsaRAVoltLoLimit_Object = MibTableColumn
hpnsaRAVoltLoLimit = _HpnsaRAVoltLoLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 5, 1, 1, 3),
    _HpnsaRAVoltLoLimit_Type()
)
hpnsaRAVoltLoLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaRAVoltLoLimit.setStatus("mandatory")
_HpnsaRAVoltHiLimit_Type = DisplayString
_HpnsaRAVoltHiLimit_Object = MibTableColumn
hpnsaRAVoltHiLimit = _HpnsaRAVoltHiLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 5, 1, 1, 4),
    _HpnsaRAVoltHiLimit_Type()
)
hpnsaRAVoltHiLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaRAVoltHiLimit.setStatus("mandatory")
_HpnsaRABusUsage_ObjectIdentity = ObjectIdentity
hpnsaRABusUsage = _HpnsaRABusUsage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 6)
)
_HpnsaRABusUsage5SecAve_Type = Integer32
_HpnsaRABusUsage5SecAve_Object = MibScalar
hpnsaRABusUsage5SecAve = _HpnsaRABusUsage5SecAve_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 6, 1),
    _HpnsaRABusUsage5SecAve_Type()
)
hpnsaRABusUsage5SecAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaRABusUsage5SecAve.setStatus("mandatory")
_HpnsaRABusUsage15SecAve_Type = Integer32
_HpnsaRABusUsage15SecAve_Object = MibScalar
hpnsaRABusUsage15SecAve = _HpnsaRABusUsage15SecAve_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 6, 2),
    _HpnsaRABusUsage15SecAve_Type()
)
hpnsaRABusUsage15SecAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaRABusUsage15SecAve.setStatus("mandatory")
_HpnsaRABusUsage1MinAve_Type = Integer32
_HpnsaRABusUsage1MinAve_Object = MibScalar
hpnsaRABusUsage1MinAve = _HpnsaRABusUsage1MinAve_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 6, 3),
    _HpnsaRABusUsage1MinAve_Type()
)
hpnsaRABusUsage1MinAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaRABusUsage1MinAve.setStatus("mandatory")
_HpnsaRABusUsage5MinAve_Type = Integer32
_HpnsaRABusUsage5MinAve_Object = MibScalar
hpnsaRABusUsage5MinAve = _HpnsaRABusUsage5MinAve_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 6, 4),
    _HpnsaRABusUsage5MinAve_Type()
)
hpnsaRABusUsage5MinAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaRABusUsage5MinAve.setStatus("mandatory")
_HpnsaRABusUsageLimit_Type = Integer32
_HpnsaRABusUsageLimit_Object = MibScalar
hpnsaRABusUsageLimit = _HpnsaRABusUsageLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 6, 5),
    _HpnsaRABusUsageLimit_Type()
)
hpnsaRABusUsageLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaRABusUsageLimit.setStatus("mandatory")
_HpnsaRALog_ObjectIdentity = ObjectIdentity
hpnsaRALog = _HpnsaRALog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 7)
)
_HpnsaRALogTable_Object = MibTable
hpnsaRALogTable = _HpnsaRALogTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 7, 1)
)
if mibBuilder.loadTexts:
    hpnsaRALogTable.setStatus("mandatory")
_HpnsaRALogEntry_Object = MibTableRow
hpnsaRALogEntry = _HpnsaRALogEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 7, 1, 1)
)
hpnsaRALogEntry.setIndexNames(
    (0, "HPNSAREMOTEASSIST-MIB", "hpnsaRALogIndex"),
)
if mibBuilder.loadTexts:
    hpnsaRALogEntry.setStatus("mandatory")
_HpnsaRALogIndex_Type = Integer32
_HpnsaRALogIndex_Object = MibTableColumn
hpnsaRALogIndex = _HpnsaRALogIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 7, 1, 1, 1),
    _HpnsaRALogIndex_Type()
)
hpnsaRALogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaRALogIndex.setStatus("mandatory")
_HpnsaRALogEventCode_Type = Integer32
_HpnsaRALogEventCode_Object = MibTableColumn
hpnsaRALogEventCode = _HpnsaRALogEventCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 7, 1, 1, 2),
    _HpnsaRALogEventCode_Type()
)
hpnsaRALogEventCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaRALogEventCode.setStatus("mandatory")


class _HpnsaRALogDescription_Type(DisplayString):
    """Custom type hpnsaRALogDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaRALogDescription_Type.__name__ = "DisplayString"
_HpnsaRALogDescription_Object = MibTableColumn
hpnsaRALogDescription = _HpnsaRALogDescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 7, 1, 1, 3),
    _HpnsaRALogDescription_Type()
)
hpnsaRALogDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaRALogDescription.setStatus("mandatory")


class _HpnsaRALogViewed_Type(Integer32):
    """Custom type hpnsaRALogViewed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("new", 0),
          ("viewed", 1))
    )


_HpnsaRALogViewed_Type.__name__ = "Integer32"
_HpnsaRALogViewed_Object = MibTableColumn
hpnsaRALogViewed = _HpnsaRALogViewed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 7, 1, 1, 4),
    _HpnsaRALogViewed_Type()
)
hpnsaRALogViewed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaRALogViewed.setStatus("mandatory")


class _HpnsaRALogDateTime_Type(OctetString):
    """Custom type hpnsaRALogDateTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_HpnsaRALogDateTime_Type.__name__ = "OctetString"
_HpnsaRALogDateTime_Object = MibTableColumn
hpnsaRALogDateTime = _HpnsaRALogDateTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 7, 1, 1, 5),
    _HpnsaRALogDateTime_Type()
)
hpnsaRALogDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaRALogDateTime.setStatus("mandatory")
_HpnsaRALogData_Type = Integer32
_HpnsaRALogData_Object = MibTableColumn
hpnsaRALogData = _HpnsaRALogData_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 7, 1, 1, 6),
    _HpnsaRALogData_Type()
)
hpnsaRALogData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaRALogData.setStatus("mandatory")
_HpnsaRAEventConfig_ObjectIdentity = ObjectIdentity
hpnsaRAEventConfig = _HpnsaRAEventConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 8)
)


class _HpnsaRAEventConfigGlobal_Type(Integer32):
    """Custom type hpnsaRAEventConfigGlobal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_HpnsaRAEventConfigGlobal_Type.__name__ = "Integer32"
_HpnsaRAEventConfigGlobal_Object = MibScalar
hpnsaRAEventConfigGlobal = _HpnsaRAEventConfigGlobal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 8, 1),
    _HpnsaRAEventConfigGlobal_Type()
)
hpnsaRAEventConfigGlobal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaRAEventConfigGlobal.setStatus("mandatory")


class _HpnsaRAEventConfigVolt_Type(Integer32):
    """Custom type hpnsaRAEventConfigVolt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_HpnsaRAEventConfigVolt_Type.__name__ = "Integer32"
_HpnsaRAEventConfigVolt_Object = MibScalar
hpnsaRAEventConfigVolt = _HpnsaRAEventConfigVolt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 8, 2),
    _HpnsaRAEventConfigVolt_Type()
)
hpnsaRAEventConfigVolt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaRAEventConfigVolt.setStatus("mandatory")


class _HpnsaRAEventConfigTemp_Type(Integer32):
    """Custom type hpnsaRAEventConfigTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_HpnsaRAEventConfigTemp_Type.__name__ = "Integer32"
_HpnsaRAEventConfigTemp_Object = MibScalar
hpnsaRAEventConfigTemp = _HpnsaRAEventConfigTemp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 8, 3),
    _HpnsaRAEventConfigTemp_Type()
)
hpnsaRAEventConfigTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaRAEventConfigTemp.setStatus("mandatory")


class _HpnsaRAEventConfigAsr_Type(Integer32):
    """Custom type hpnsaRAEventConfigAsr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_HpnsaRAEventConfigAsr_Type.__name__ = "Integer32"
_HpnsaRAEventConfigAsr_Object = MibScalar
hpnsaRAEventConfigAsr = _HpnsaRAEventConfigAsr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 8, 4),
    _HpnsaRAEventConfigAsr_Type()
)
hpnsaRAEventConfigAsr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaRAEventConfigAsr.setStatus("mandatory")


class _HpnsaRAEventConfigRemBoot_Type(Integer32):
    """Custom type hpnsaRAEventConfigRemBoot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_HpnsaRAEventConfigRemBoot_Type.__name__ = "Integer32"
_HpnsaRAEventConfigRemBoot_Object = MibScalar
hpnsaRAEventConfigRemBoot = _HpnsaRAEventConfigRemBoot_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 8, 5),
    _HpnsaRAEventConfigRemBoot_Type()
)
hpnsaRAEventConfigRemBoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaRAEventConfigRemBoot.setStatus("mandatory")


class _HpnsaRAEventConfigBusUsage_Type(Integer32):
    """Custom type hpnsaRAEventConfigBusUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_HpnsaRAEventConfigBusUsage_Type.__name__ = "Integer32"
_HpnsaRAEventConfigBusUsage_Object = MibScalar
hpnsaRAEventConfigBusUsage = _HpnsaRAEventConfigBusUsage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 8, 6),
    _HpnsaRAEventConfigBusUsage_Type()
)
hpnsaRAEventConfigBusUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaRAEventConfigBusUsage.setStatus("mandatory")


class _HpnsaRAEventConfigRemAsst_Type(Integer32):
    """Custom type hpnsaRAEventConfigRemAsst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_HpnsaRAEventConfigRemAsst_Type.__name__ = "Integer32"
_HpnsaRAEventConfigRemAsst_Object = MibScalar
hpnsaRAEventConfigRemAsst = _HpnsaRAEventConfigRemAsst_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 8, 7),
    _HpnsaRAEventConfigRemAsst_Type()
)
hpnsaRAEventConfigRemAsst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaRAEventConfigRemAsst.setStatus("mandatory")


class _HpnsaRAEventConfigTrapTest_Type(Integer32):
    """Custom type hpnsaRAEventConfigTrapTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_HpnsaRAEventConfigTrapTest_Type.__name__ = "Integer32"
_HpnsaRAEventConfigTrapTest_Object = MibScalar
hpnsaRAEventConfigTrapTest = _HpnsaRAEventConfigTrapTest_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 8, 8),
    _HpnsaRAEventConfigTrapTest_Type()
)
hpnsaRAEventConfigTrapTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaRAEventConfigTrapTest.setStatus("mandatory")


class _HpnsaRAEventConfigHostSys_Type(Integer32):
    """Custom type hpnsaRAEventConfigHostSys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_HpnsaRAEventConfigHostSys_Type.__name__ = "Integer32"
_HpnsaRAEventConfigHostSys_Object = MibScalar
hpnsaRAEventConfigHostSys = _HpnsaRAEventConfigHostSys_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 8, 9),
    _HpnsaRAEventConfigHostSys_Type()
)
hpnsaRAEventConfigHostSys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaRAEventConfigHostSys.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPNSAREMOTEASSIST-MIB",
    **{"hp": hp,
       "nm": nm,
       "hpnsa": hpnsa,
       "hpnsaRemoteAssist": hpnsaRemoteAssist,
       "hpnsaRAMibRev": hpnsaRAMibRev,
       "hpnsaRAMibRevMajor": hpnsaRAMibRevMajor,
       "hpnsaRAMibRevMinor": hpnsaRAMibRevMinor,
       "hpnsaRAAgent": hpnsaRAAgent,
       "hpnsaRAAgentTable": hpnsaRAAgentTable,
       "hpnsaRAAgentEntry": hpnsaRAAgentEntry,
       "hpnsaRAAgentIndex": hpnsaRAAgentIndex,
       "hpnsaRAAgentName": hpnsaRAAgentName,
       "hpnsaRAAgentVersion": hpnsaRAAgentVersion,
       "hpnsaRAAgentDate": hpnsaRAAgentDate,
       "hpnsaRAInfo": hpnsaRAInfo,
       "hpnsaRAInfoBoardType": hpnsaRAInfoBoardType,
       "hpnsaRAInfoBoardName": hpnsaRAInfoBoardName,
       "hpnsaRAInfoBoardID": hpnsaRAInfoBoardID,
       "hpnsaRAInfoBoardVersion": hpnsaRAInfoBoardVersion,
       "hpnsaRATemp": hpnsaRATemp,
       "hpnsaRATempMeasured": hpnsaRATempMeasured,
       "hpnsaRATempWarnLimit": hpnsaRATempWarnLimit,
       "hpnsaRATempGracefulSDLimit": hpnsaRATempGracefulSDLimit,
       "hpnsaRATempCriticalSDLimit": hpnsaRATempCriticalSDLimit,
       "hpnsaRAVolt": hpnsaRAVolt,
       "hpnsaRAVoltTable": hpnsaRAVoltTable,
       "hpnsaRAVoltEntry": hpnsaRAVoltEntry,
       "hpnsaRAVoltTypeIndex": hpnsaRAVoltTypeIndex,
       "hpnsaRAVoltMeasured": hpnsaRAVoltMeasured,
       "hpnsaRAVoltLoLimit": hpnsaRAVoltLoLimit,
       "hpnsaRAVoltHiLimit": hpnsaRAVoltHiLimit,
       "hpnsaRABusUsage": hpnsaRABusUsage,
       "hpnsaRABusUsage5SecAve": hpnsaRABusUsage5SecAve,
       "hpnsaRABusUsage15SecAve": hpnsaRABusUsage15SecAve,
       "hpnsaRABusUsage1MinAve": hpnsaRABusUsage1MinAve,
       "hpnsaRABusUsage5MinAve": hpnsaRABusUsage5MinAve,
       "hpnsaRABusUsageLimit": hpnsaRABusUsageLimit,
       "hpnsaRALog": hpnsaRALog,
       "hpnsaRALogTable": hpnsaRALogTable,
       "hpnsaRALogEntry": hpnsaRALogEntry,
       "hpnsaRALogIndex": hpnsaRALogIndex,
       "hpnsaRALogEventCode": hpnsaRALogEventCode,
       "hpnsaRALogDescription": hpnsaRALogDescription,
       "hpnsaRALogViewed": hpnsaRALogViewed,
       "hpnsaRALogDateTime": hpnsaRALogDateTime,
       "hpnsaRALogData": hpnsaRALogData,
       "hpnsaRAEventConfig": hpnsaRAEventConfig,
       "hpnsaRAEventConfigGlobal": hpnsaRAEventConfigGlobal,
       "hpnsaRAEventConfigVolt": hpnsaRAEventConfigVolt,
       "hpnsaRAEventConfigTemp": hpnsaRAEventConfigTemp,
       "hpnsaRAEventConfigAsr": hpnsaRAEventConfigAsr,
       "hpnsaRAEventConfigRemBoot": hpnsaRAEventConfigRemBoot,
       "hpnsaRAEventConfigBusUsage": hpnsaRAEventConfigBusUsage,
       "hpnsaRAEventConfigRemAsst": hpnsaRAEventConfigRemAsst,
       "hpnsaRAEventConfigTrapTest": hpnsaRAEventConfigTrapTest,
       "hpnsaRAEventConfigHostSys": hpnsaRAEventConfigHostSys}
)
