# SNMP MIB module (CPQSCSI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CPQSCSI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:40 2024
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

(compaq,
 cpqHoTrapFlags) = mibBuilder.importSymbols(
    "CPQHOST-MIB",
    "compaq",
    "cpqHoTrapFlags")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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

_CpqScsi_ObjectIdentity = ObjectIdentity
cpqScsi = _CpqScsi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 5)
)
_CpqScsiMibRev_ObjectIdentity = ObjectIdentity
cpqScsiMibRev = _CpqScsiMibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 5, 1)
)


class _CpqScsiMibRevMajor_Type(Integer32):
    """Custom type cpqScsiMibRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CpqScsiMibRevMajor_Type.__name__ = "Integer32"
_CpqScsiMibRevMajor_Object = MibScalar
cpqScsiMibRevMajor = _CpqScsiMibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 1, 1),
    _CpqScsiMibRevMajor_Type()
)
cpqScsiMibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiMibRevMajor.setStatus("mandatory")


class _CpqScsiMibRevMinor_Type(Integer32):
    """Custom type cpqScsiMibRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqScsiMibRevMinor_Type.__name__ = "Integer32"
_CpqScsiMibRevMinor_Object = MibScalar
cpqScsiMibRevMinor = _CpqScsiMibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 1, 2),
    _CpqScsiMibRevMinor_Type()
)
cpqScsiMibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiMibRevMinor.setStatus("mandatory")


class _CpqScsiMibCondition_Type(Integer32):
    """Custom type cpqScsiMibCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqScsiMibCondition_Type.__name__ = "Integer32"
_CpqScsiMibCondition_Object = MibScalar
cpqScsiMibCondition = _CpqScsiMibCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 1, 3),
    _CpqScsiMibCondition_Type()
)
cpqScsiMibCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiMibCondition.setStatus("mandatory")
_CpqScsiComponent_ObjectIdentity = ObjectIdentity
cpqScsiComponent = _CpqScsiComponent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 5, 2)
)
_CpqScsiInterface_ObjectIdentity = ObjectIdentity
cpqScsiInterface = _CpqScsiInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 1)
)
_CpqScsiOsNetWare_ObjectIdentity = ObjectIdentity
cpqScsiOsNetWare = _CpqScsiOsNetWare_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 1, 1)
)


class _CpqScsiNw3xDriverName_Type(DisplayString):
    """Custom type cpqScsiNw3xDriverName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CpqScsiNw3xDriverName_Type.__name__ = "DisplayString"
_CpqScsiNw3xDriverName_Object = MibScalar
cpqScsiNw3xDriverName = _CpqScsiNw3xDriverName_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 1, 1, 1),
    _CpqScsiNw3xDriverName_Type()
)
cpqScsiNw3xDriverName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiNw3xDriverName.setStatus("deprecated")


class _CpqScsiNw3xDriverVers_Type(DisplayString):
    """Custom type cpqScsiNw3xDriverVers based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_CpqScsiNw3xDriverVers_Type.__name__ = "DisplayString"
_CpqScsiNw3xDriverVers_Object = MibScalar
cpqScsiNw3xDriverVers = _CpqScsiNw3xDriverVers_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 1, 1, 2),
    _CpqScsiNw3xDriverVers_Type()
)
cpqScsiNw3xDriverVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiNw3xDriverVers.setStatus("deprecated")


class _CpqScsiNw3xDriverPollType_Type(Integer32):
    """Custom type cpqScsiNw3xDriverPollType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("demand", 3),
          ("other", 1),
          ("polled", 2))
    )


_CpqScsiNw3xDriverPollType_Type.__name__ = "Integer32"
_CpqScsiNw3xDriverPollType_Object = MibScalar
cpqScsiNw3xDriverPollType = _CpqScsiNw3xDriverPollType_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 1, 1, 3),
    _CpqScsiNw3xDriverPollType_Type()
)
cpqScsiNw3xDriverPollType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiNw3xDriverPollType.setStatus("deprecated")


class _CpqScsiNw3xDriverPollTime_Type(Integer32):
    """Custom type cpqScsiNw3xDriverPollTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_CpqScsiNw3xDriverPollTime_Type.__name__ = "Integer32"
_CpqScsiNw3xDriverPollTime_Object = MibScalar
cpqScsiNw3xDriverPollTime = _CpqScsiNw3xDriverPollTime_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 1, 1, 4),
    _CpqScsiNw3xDriverPollTime_Type()
)
cpqScsiNw3xDriverPollTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiNw3xDriverPollTime.setStatus("deprecated")
_CpqScsiNw3xCntlrInfoTable_Object = MibTable
cpqScsiNw3xCntlrInfoTable = _CpqScsiNw3xCntlrInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cpqScsiNw3xCntlrInfoTable.setStatus("deprecated")
_CpqScsiNw3xCntlrInfoEntry_Object = MibTableRow
cpqScsiNw3xCntlrInfoEntry = _CpqScsiNw3xCntlrInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 1, 1, 5, 1)
)
cpqScsiNw3xCntlrInfoEntry.setIndexNames(
    (0, "CPQSCSI-MIB", "cpqScsiNw3xCntlrIndex"),
    (0, "CPQSCSI-MIB", "cpqScsiNw3xBusIndex"),
)
if mibBuilder.loadTexts:
    cpqScsiNw3xCntlrInfoEntry.setStatus("deprecated")


class _CpqScsiNw3xCntlrIndex_Type(Integer32):
    """Custom type cpqScsiNw3xCntlrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqScsiNw3xCntlrIndex_Type.__name__ = "Integer32"
_CpqScsiNw3xCntlrIndex_Object = MibTableColumn
cpqScsiNw3xCntlrIndex = _CpqScsiNw3xCntlrIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 1, 1, 5, 1, 1),
    _CpqScsiNw3xCntlrIndex_Type()
)
cpqScsiNw3xCntlrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiNw3xCntlrIndex.setStatus("deprecated")


class _CpqScsiNw3xBusIndex_Type(Integer32):
    """Custom type cpqScsiNw3xBusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqScsiNw3xBusIndex_Type.__name__ = "Integer32"
_CpqScsiNw3xBusIndex_Object = MibTableColumn
cpqScsiNw3xBusIndex = _CpqScsiNw3xBusIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 1, 1, 5, 1, 2),
    _CpqScsiNw3xBusIndex_Type()
)
cpqScsiNw3xBusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiNw3xBusIndex.setStatus("deprecated")


class _CpqScsiNw3xXptDesc_Type(DisplayString):
    """Custom type cpqScsiNw3xXptDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CpqScsiNw3xXptDesc_Type.__name__ = "DisplayString"
_CpqScsiNw3xXptDesc_Object = MibTableColumn
cpqScsiNw3xXptDesc = _CpqScsiNw3xXptDesc_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 1, 1, 5, 1, 3),
    _CpqScsiNw3xXptDesc_Type()
)
cpqScsiNw3xXptDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiNw3xXptDesc.setStatus("deprecated")


class _CpqScsiNw3xXptVers_Type(DisplayString):
    """Custom type cpqScsiNw3xXptVers based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_CpqScsiNw3xXptVers_Type.__name__ = "DisplayString"
_CpqScsiNw3xXptVers_Object = MibTableColumn
cpqScsiNw3xXptVers = _CpqScsiNw3xXptVers_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 1, 1, 5, 1, 4),
    _CpqScsiNw3xXptVers_Type()
)
cpqScsiNw3xXptVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiNw3xXptVers.setStatus("deprecated")


class _CpqScsiNw3xSimDesc_Type(DisplayString):
    """Custom type cpqScsiNw3xSimDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CpqScsiNw3xSimDesc_Type.__name__ = "DisplayString"
_CpqScsiNw3xSimDesc_Object = MibTableColumn
cpqScsiNw3xSimDesc = _CpqScsiNw3xSimDesc_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 1, 1, 5, 1, 5),
    _CpqScsiNw3xSimDesc_Type()
)
cpqScsiNw3xSimDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiNw3xSimDesc.setStatus("deprecated")


class _CpqScsiNw3xSimVers_Type(DisplayString):
    """Custom type cpqScsiNw3xSimVers based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_CpqScsiNw3xSimVers_Type.__name__ = "DisplayString"
_CpqScsiNw3xSimVers_Object = MibTableColumn
cpqScsiNw3xSimVers = _CpqScsiNw3xSimVers_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 1, 1, 5, 1, 6),
    _CpqScsiNw3xSimVers_Type()
)
cpqScsiNw3xSimVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiNw3xSimVers.setStatus("deprecated")


class _CpqScsiNw3xHbaDesc_Type(DisplayString):
    """Custom type cpqScsiNw3xHbaDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CpqScsiNw3xHbaDesc_Type.__name__ = "DisplayString"
_CpqScsiNw3xHbaDesc_Object = MibTableColumn
cpqScsiNw3xHbaDesc = _CpqScsiNw3xHbaDesc_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 1, 1, 5, 1, 7),
    _CpqScsiNw3xHbaDesc_Type()
)
cpqScsiNw3xHbaDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiNw3xHbaDesc.setStatus("deprecated")
_CpqScsiLogDrvStatTable_Object = MibTable
cpqScsiLogDrvStatTable = _CpqScsiLogDrvStatTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 1, 1, 6)
)
if mibBuilder.loadTexts:
    cpqScsiLogDrvStatTable.setStatus("deprecated")
_CpqScsiLogDrvStatEntry_Object = MibTableRow
cpqScsiLogDrvStatEntry = _CpqScsiLogDrvStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 1, 1, 6, 1)
)
cpqScsiLogDrvStatEntry.setIndexNames(
    (0, "CPQSCSI-MIB", "cpqScsiNw3xStatCntlrIndex"),
    (0, "CPQSCSI-MIB", "cpqScsiNw3xStatBusIndex"),
    (0, "CPQSCSI-MIB", "cpqScsiNw3xStatLogDrvIndex"),
)
if mibBuilder.loadTexts:
    cpqScsiLogDrvStatEntry.setStatus("deprecated")


class _CpqScsiNw3xStatCntlrIndex_Type(Integer32):
    """Custom type cpqScsiNw3xStatCntlrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqScsiNw3xStatCntlrIndex_Type.__name__ = "Integer32"
_CpqScsiNw3xStatCntlrIndex_Object = MibTableColumn
cpqScsiNw3xStatCntlrIndex = _CpqScsiNw3xStatCntlrIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 1, 1, 6, 1, 1),
    _CpqScsiNw3xStatCntlrIndex_Type()
)
cpqScsiNw3xStatCntlrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiNw3xStatCntlrIndex.setStatus("deprecated")


class _CpqScsiNw3xStatBusIndex_Type(Integer32):
    """Custom type cpqScsiNw3xStatBusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 225),
    )


_CpqScsiNw3xStatBusIndex_Type.__name__ = "Integer32"
_CpqScsiNw3xStatBusIndex_Object = MibTableColumn
cpqScsiNw3xStatBusIndex = _CpqScsiNw3xStatBusIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 1, 1, 6, 1, 2),
    _CpqScsiNw3xStatBusIndex_Type()
)
cpqScsiNw3xStatBusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiNw3xStatBusIndex.setStatus("deprecated")


class _CpqScsiNw3xStatLogDrvIndex_Type(Integer32):
    """Custom type cpqScsiNw3xStatLogDrvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 225),
    )


_CpqScsiNw3xStatLogDrvIndex_Type.__name__ = "Integer32"
_CpqScsiNw3xStatLogDrvIndex_Object = MibTableColumn
cpqScsiNw3xStatLogDrvIndex = _CpqScsiNw3xStatLogDrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 1, 1, 6, 1, 3),
    _CpqScsiNw3xStatLogDrvIndex_Type()
)
cpqScsiNw3xStatLogDrvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiNw3xStatLogDrvIndex.setStatus("deprecated")
_CpqScsiNw3xTotalReads_Type = Counter32
_CpqScsiNw3xTotalReads_Object = MibTableColumn
cpqScsiNw3xTotalReads = _CpqScsiNw3xTotalReads_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 1, 1, 6, 1, 4),
    _CpqScsiNw3xTotalReads_Type()
)
cpqScsiNw3xTotalReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiNw3xTotalReads.setStatus("deprecated")
_CpqScsiNw3xTotalWrites_Type = Counter32
_CpqScsiNw3xTotalWrites_Object = MibTableColumn
cpqScsiNw3xTotalWrites = _CpqScsiNw3xTotalWrites_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 1, 1, 6, 1, 5),
    _CpqScsiNw3xTotalWrites_Type()
)
cpqScsiNw3xTotalWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiNw3xTotalWrites.setStatus("deprecated")
_CpqScsiNw3xCorrReads_Type = Counter32
_CpqScsiNw3xCorrReads_Object = MibTableColumn
cpqScsiNw3xCorrReads = _CpqScsiNw3xCorrReads_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 1, 1, 6, 1, 6),
    _CpqScsiNw3xCorrReads_Type()
)
cpqScsiNw3xCorrReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiNw3xCorrReads.setStatus("deprecated")
_CpqScsiNw3xCorrWrites_Type = Counter32
_CpqScsiNw3xCorrWrites_Object = MibTableColumn
cpqScsiNw3xCorrWrites = _CpqScsiNw3xCorrWrites_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 1, 1, 6, 1, 7),
    _CpqScsiNw3xCorrWrites_Type()
)
cpqScsiNw3xCorrWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiNw3xCorrWrites.setStatus("deprecated")
_CpqScsiNw3xFatalReads_Type = Counter32
_CpqScsiNw3xFatalReads_Object = MibTableColumn
cpqScsiNw3xFatalReads = _CpqScsiNw3xFatalReads_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 1, 1, 6, 1, 8),
    _CpqScsiNw3xFatalReads_Type()
)
cpqScsiNw3xFatalReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiNw3xFatalReads.setStatus("deprecated")
_CpqScsiNw3xFatalWrites_Type = Counter32
_CpqScsiNw3xFatalWrites_Object = MibTableColumn
cpqScsiNw3xFatalWrites = _CpqScsiNw3xFatalWrites_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 1, 1, 6, 1, 9),
    _CpqScsiNw3xFatalWrites_Type()
)
cpqScsiNw3xFatalWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiNw3xFatalWrites.setStatus("deprecated")
_CpqScsiVolMapTable_Object = MibTable
cpqScsiVolMapTable = _CpqScsiVolMapTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 1, 1, 7)
)
if mibBuilder.loadTexts:
    cpqScsiVolMapTable.setStatus("deprecated")
_CpqScsiVolMapEntry_Object = MibTableRow
cpqScsiVolMapEntry = _CpqScsiVolMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 1, 1, 7, 1)
)
cpqScsiVolMapEntry.setIndexNames(
    (0, "CPQSCSI-MIB", "cpqScsiNw3xVolCntlrIndex"),
    (0, "CPQSCSI-MIB", "cpqScsiNw3xVolBusIndex"),
    (0, "CPQSCSI-MIB", "cpqScsiNw3xVolLogDrvIndex"),
)
if mibBuilder.loadTexts:
    cpqScsiVolMapEntry.setStatus("deprecated")


class _CpqScsiNw3xVolCntlrIndex_Type(Integer32):
    """Custom type cpqScsiNw3xVolCntlrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 225),
    )


_CpqScsiNw3xVolCntlrIndex_Type.__name__ = "Integer32"
_CpqScsiNw3xVolCntlrIndex_Object = MibTableColumn
cpqScsiNw3xVolCntlrIndex = _CpqScsiNw3xVolCntlrIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 1, 1, 7, 1, 1),
    _CpqScsiNw3xVolCntlrIndex_Type()
)
cpqScsiNw3xVolCntlrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiNw3xVolCntlrIndex.setStatus("deprecated")


class _CpqScsiNw3xVolBusIndex_Type(Integer32):
    """Custom type cpqScsiNw3xVolBusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 225),
    )


_CpqScsiNw3xVolBusIndex_Type.__name__ = "Integer32"
_CpqScsiNw3xVolBusIndex_Object = MibTableColumn
cpqScsiNw3xVolBusIndex = _CpqScsiNw3xVolBusIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 1, 1, 7, 1, 2),
    _CpqScsiNw3xVolBusIndex_Type()
)
cpqScsiNw3xVolBusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiNw3xVolBusIndex.setStatus("deprecated")


class _CpqScsiNw3xVolLogDrvIndex_Type(Integer32):
    """Custom type cpqScsiNw3xVolLogDrvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 225),
    )


_CpqScsiNw3xVolLogDrvIndex_Type.__name__ = "Integer32"
_CpqScsiNw3xVolLogDrvIndex_Object = MibTableColumn
cpqScsiNw3xVolLogDrvIndex = _CpqScsiNw3xVolLogDrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 1, 1, 7, 1, 3),
    _CpqScsiNw3xVolLogDrvIndex_Type()
)
cpqScsiNw3xVolLogDrvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiNw3xVolLogDrvIndex.setStatus("deprecated")


class _CpqScsiNw3xVolMap_Type(OctetString):
    """Custom type cpqScsiNw3xVolMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqScsiNw3xVolMap_Type.__name__ = "OctetString"
_CpqScsiNw3xVolMap_Object = MibTableColumn
cpqScsiNw3xVolMap = _CpqScsiNw3xVolMap_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 1, 1, 7, 1, 4),
    _CpqScsiNw3xVolMap_Type()
)
cpqScsiNw3xVolMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiNw3xVolMap.setStatus("deprecated")
_CpqScsiOsCommon_ObjectIdentity = ObjectIdentity
cpqScsiOsCommon = _CpqScsiOsCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 1, 4)
)


class _CpqScsiOsCommonPollFreq_Type(Integer32):
    """Custom type cpqScsiOsCommonPollFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqScsiOsCommonPollFreq_Type.__name__ = "Integer32"
_CpqScsiOsCommonPollFreq_Object = MibScalar
cpqScsiOsCommonPollFreq = _CpqScsiOsCommonPollFreq_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 1, 4, 1),
    _CpqScsiOsCommonPollFreq_Type()
)
cpqScsiOsCommonPollFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqScsiOsCommonPollFreq.setStatus("mandatory")
_CpqScsiOsCommonModuleTable_Object = MibTable
cpqScsiOsCommonModuleTable = _CpqScsiOsCommonModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cpqScsiOsCommonModuleTable.setStatus("deprecated")
_CpqScsiOsCommonModuleEntry_Object = MibTableRow
cpqScsiOsCommonModuleEntry = _CpqScsiOsCommonModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 1, 4, 2, 1)
)
cpqScsiOsCommonModuleEntry.setIndexNames(
    (0, "CPQSCSI-MIB", "cpqScsiOsCommonModuleIndex"),
)
if mibBuilder.loadTexts:
    cpqScsiOsCommonModuleEntry.setStatus("deprecated")


class _CpqScsiOsCommonModuleIndex_Type(Integer32):
    """Custom type cpqScsiOsCommonModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqScsiOsCommonModuleIndex_Type.__name__ = "Integer32"
_CpqScsiOsCommonModuleIndex_Object = MibTableColumn
cpqScsiOsCommonModuleIndex = _CpqScsiOsCommonModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 1, 4, 2, 1, 1),
    _CpqScsiOsCommonModuleIndex_Type()
)
cpqScsiOsCommonModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiOsCommonModuleIndex.setStatus("deprecated")


class _CpqScsiOsCommonModuleName_Type(DisplayString):
    """Custom type cpqScsiOsCommonModuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqScsiOsCommonModuleName_Type.__name__ = "DisplayString"
_CpqScsiOsCommonModuleName_Object = MibTableColumn
cpqScsiOsCommonModuleName = _CpqScsiOsCommonModuleName_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 1, 4, 2, 1, 2),
    _CpqScsiOsCommonModuleName_Type()
)
cpqScsiOsCommonModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiOsCommonModuleName.setStatus("deprecated")


class _CpqScsiOsCommonModuleVersion_Type(DisplayString):
    """Custom type cpqScsiOsCommonModuleVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_CpqScsiOsCommonModuleVersion_Type.__name__ = "DisplayString"
_CpqScsiOsCommonModuleVersion_Object = MibTableColumn
cpqScsiOsCommonModuleVersion = _CpqScsiOsCommonModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 1, 4, 2, 1, 3),
    _CpqScsiOsCommonModuleVersion_Type()
)
cpqScsiOsCommonModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiOsCommonModuleVersion.setStatus("deprecated")


class _CpqScsiOsCommonModuleDate_Type(OctetString):
    """Custom type cpqScsiOsCommonModuleDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_CpqScsiOsCommonModuleDate_Type.__name__ = "OctetString"
_CpqScsiOsCommonModuleDate_Object = MibTableColumn
cpqScsiOsCommonModuleDate = _CpqScsiOsCommonModuleDate_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 1, 4, 2, 1, 4),
    _CpqScsiOsCommonModuleDate_Type()
)
cpqScsiOsCommonModuleDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiOsCommonModuleDate.setStatus("deprecated")


class _CpqScsiOsCommonModulePurpose_Type(DisplayString):
    """Custom type cpqScsiOsCommonModulePurpose based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqScsiOsCommonModulePurpose_Type.__name__ = "DisplayString"
_CpqScsiOsCommonModulePurpose_Object = MibTableColumn
cpqScsiOsCommonModulePurpose = _CpqScsiOsCommonModulePurpose_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 1, 4, 2, 1, 5),
    _CpqScsiOsCommonModulePurpose_Type()
)
cpqScsiOsCommonModulePurpose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiOsCommonModulePurpose.setStatus("deprecated")
_CpqScsiCntlr_ObjectIdentity = ObjectIdentity
cpqScsiCntlr = _CpqScsiCntlr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 2)
)
_CpqScsiCntlrTable_Object = MibTable
cpqScsiCntlrTable = _CpqScsiCntlrTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cpqScsiCntlrTable.setStatus("mandatory")
_CpqScsiCntlrEntry_Object = MibTableRow
cpqScsiCntlrEntry = _CpqScsiCntlrEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 2, 1, 1)
)
cpqScsiCntlrEntry.setIndexNames(
    (0, "CPQSCSI-MIB", "cpqScsiCntlrIndex"),
    (0, "CPQSCSI-MIB", "cpqScsiCntlrBusIndex"),
)
if mibBuilder.loadTexts:
    cpqScsiCntlrEntry.setStatus("mandatory")
_CpqScsiCntlrIndex_Type = Integer32
_CpqScsiCntlrIndex_Object = MibTableColumn
cpqScsiCntlrIndex = _CpqScsiCntlrIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 2, 1, 1, 1),
    _CpqScsiCntlrIndex_Type()
)
cpqScsiCntlrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiCntlrIndex.setStatus("mandatory")


class _CpqScsiCntlrBusIndex_Type(Integer32):
    """Custom type cpqScsiCntlrBusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 225),
    )


_CpqScsiCntlrBusIndex_Type.__name__ = "Integer32"
_CpqScsiCntlrBusIndex_Object = MibTableColumn
cpqScsiCntlrBusIndex = _CpqScsiCntlrBusIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 2, 1, 1, 2),
    _CpqScsiCntlrBusIndex_Type()
)
cpqScsiCntlrBusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiCntlrBusIndex.setStatus("mandatory")


class _CpqScsiCntlrModel_Type(Integer32):
    """Custom type cpqScsiCntlrModel based on Integer32"""
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
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("cpqa789x", 12),
          ("cpqs710", 2),
          ("cpqs810p", 4),
          ("cpqs825e", 5),
          ("cpqs825p", 6),
          ("cpqs875p", 8),
          ("cpqs876t", 13),
          ("cpqs895p", 10),
          ("cpqs896p", 11),
          ("cpqs94", 3),
          ("cpqs974p", 7),
          ("extended", 9),
          ("hpu320", 14),
          ("hpu320r", 15),
          ("other", 1))
    )


_CpqScsiCntlrModel_Type.__name__ = "Integer32"
_CpqScsiCntlrModel_Object = MibTableColumn
cpqScsiCntlrModel = _CpqScsiCntlrModel_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 2, 1, 1, 3),
    _CpqScsiCntlrModel_Type()
)
cpqScsiCntlrModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiCntlrModel.setStatus("mandatory")
_CpqScsiCntlrFWVers_Type = DisplayString
_CpqScsiCntlrFWVers_Object = MibTableColumn
cpqScsiCntlrFWVers = _CpqScsiCntlrFWVers_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 2, 1, 1, 4),
    _CpqScsiCntlrFWVers_Type()
)
cpqScsiCntlrFWVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiCntlrFWVers.setStatus("mandatory")


class _CpqScsiCntlrSWVers_Type(DisplayString):
    """Custom type cpqScsiCntlrSWVers based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_CpqScsiCntlrSWVers_Type.__name__ = "DisplayString"
_CpqScsiCntlrSWVers_Object = MibTableColumn
cpqScsiCntlrSWVers = _CpqScsiCntlrSWVers_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 2, 1, 1, 5),
    _CpqScsiCntlrSWVers_Type()
)
cpqScsiCntlrSWVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiCntlrSWVers.setStatus("deprecated")


class _CpqScsiCntlrSlot_Type(Integer32):
    """Custom type cpqScsiCntlrSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 225),
    )


_CpqScsiCntlrSlot_Type.__name__ = "Integer32"
_CpqScsiCntlrSlot_Object = MibTableColumn
cpqScsiCntlrSlot = _CpqScsiCntlrSlot_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 2, 1, 1, 6),
    _CpqScsiCntlrSlot_Type()
)
cpqScsiCntlrSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiCntlrSlot.setStatus("mandatory")


class _CpqScsiCntlrStatus_Type(Integer32):
    """Custom type cpqScsiCntlrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 3),
          ("ok", 2),
          ("other", 1))
    )


_CpqScsiCntlrStatus_Type.__name__ = "Integer32"
_CpqScsiCntlrStatus_Object = MibTableColumn
cpqScsiCntlrStatus = _CpqScsiCntlrStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 2, 1, 1, 7),
    _CpqScsiCntlrStatus_Type()
)
cpqScsiCntlrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiCntlrStatus.setStatus("mandatory")
_CpqScsiCntlrHardResets_Type = Counter32
_CpqScsiCntlrHardResets_Object = MibTableColumn
cpqScsiCntlrHardResets = _CpqScsiCntlrHardResets_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 2, 1, 1, 8),
    _CpqScsiCntlrHardResets_Type()
)
cpqScsiCntlrHardResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiCntlrHardResets.setStatus("mandatory")
_CpqScsiCntlrSoftResets_Type = Counter32
_CpqScsiCntlrSoftResets_Object = MibTableColumn
cpqScsiCntlrSoftResets = _CpqScsiCntlrSoftResets_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 2, 1, 1, 9),
    _CpqScsiCntlrSoftResets_Type()
)
cpqScsiCntlrSoftResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiCntlrSoftResets.setStatus("mandatory")
_CpqScsiCntlrTimeouts_Type = Counter32
_CpqScsiCntlrTimeouts_Object = MibTableColumn
cpqScsiCntlrTimeouts = _CpqScsiCntlrTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 2, 1, 1, 10),
    _CpqScsiCntlrTimeouts_Type()
)
cpqScsiCntlrTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiCntlrTimeouts.setStatus("mandatory")
_CpqScsiCntlrBaseIOAddr_Type = Integer32
_CpqScsiCntlrBaseIOAddr_Object = MibTableColumn
cpqScsiCntlrBaseIOAddr = _CpqScsiCntlrBaseIOAddr_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 2, 1, 1, 11),
    _CpqScsiCntlrBaseIOAddr_Type()
)
cpqScsiCntlrBaseIOAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiCntlrBaseIOAddr.setStatus("mandatory")


class _CpqScsiCntlrCondition_Type(Integer32):
    """Custom type cpqScsiCntlrCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqScsiCntlrCondition_Type.__name__ = "Integer32"
_CpqScsiCntlrCondition_Object = MibTableColumn
cpqScsiCntlrCondition = _CpqScsiCntlrCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 2, 1, 1, 12),
    _CpqScsiCntlrCondition_Type()
)
cpqScsiCntlrCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiCntlrCondition.setStatus("mandatory")


class _CpqScsiCntlrSerialNum_Type(DisplayString):
    """Custom type cpqScsiCntlrSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CpqScsiCntlrSerialNum_Type.__name__ = "DisplayString"
_CpqScsiCntlrSerialNum_Object = MibTableColumn
cpqScsiCntlrSerialNum = _CpqScsiCntlrSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 2, 1, 1, 13),
    _CpqScsiCntlrSerialNum_Type()
)
cpqScsiCntlrSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiCntlrSerialNum.setStatus("mandatory")


class _CpqScsiCntlrBusWidth_Type(Integer32):
    """Custom type cpqScsiCntlrBusWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("narrow", 2),
          ("other", 1),
          ("wide16", 3))
    )


_CpqScsiCntlrBusWidth_Type.__name__ = "Integer32"
_CpqScsiCntlrBusWidth_Object = MibTableColumn
cpqScsiCntlrBusWidth = _CpqScsiCntlrBusWidth_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 2, 1, 1, 14),
    _CpqScsiCntlrBusWidth_Type()
)
cpqScsiCntlrBusWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiCntlrBusWidth.setStatus("mandatory")


class _CpqScsiCntlrModelExtended_Type(DisplayString):
    """Custom type cpqScsiCntlrModelExtended based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CpqScsiCntlrModelExtended_Type.__name__ = "DisplayString"
_CpqScsiCntlrModelExtended_Object = MibTableColumn
cpqScsiCntlrModelExtended = _CpqScsiCntlrModelExtended_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 2, 1, 1, 15),
    _CpqScsiCntlrModelExtended_Type()
)
cpqScsiCntlrModelExtended.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiCntlrModelExtended.setStatus("mandatory")


class _CpqScsiCntlrHwLocation_Type(DisplayString):
    """Custom type cpqScsiCntlrHwLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqScsiCntlrHwLocation_Type.__name__ = "DisplayString"
_CpqScsiCntlrHwLocation_Object = MibTableColumn
cpqScsiCntlrHwLocation = _CpqScsiCntlrHwLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 2, 1, 1, 16),
    _CpqScsiCntlrHwLocation_Type()
)
cpqScsiCntlrHwLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiCntlrHwLocation.setStatus("optional")
_CpqScsiLogDrv_ObjectIdentity = ObjectIdentity
cpqScsiLogDrv = _CpqScsiLogDrv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 3)
)
_CpqScsiLogDrvTable_Object = MibTable
cpqScsiLogDrvTable = _CpqScsiLogDrvTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 3, 1)
)
if mibBuilder.loadTexts:
    cpqScsiLogDrvTable.setStatus("mandatory")
_CpqScsiLogDrvEntry_Object = MibTableRow
cpqScsiLogDrvEntry = _CpqScsiLogDrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 3, 1, 1)
)
cpqScsiLogDrvEntry.setIndexNames(
    (0, "CPQSCSI-MIB", "cpqScsiLogDrvCntlrIndex"),
    (0, "CPQSCSI-MIB", "cpqScsiLogDrvBusIndex"),
    (0, "CPQSCSI-MIB", "cpqScsiLogDrvIndex"),
)
if mibBuilder.loadTexts:
    cpqScsiLogDrvEntry.setStatus("mandatory")
_CpqScsiLogDrvCntlrIndex_Type = Integer32
_CpqScsiLogDrvCntlrIndex_Object = MibTableColumn
cpqScsiLogDrvCntlrIndex = _CpqScsiLogDrvCntlrIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 3, 1, 1, 1),
    _CpqScsiLogDrvCntlrIndex_Type()
)
cpqScsiLogDrvCntlrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiLogDrvCntlrIndex.setStatus("mandatory")


class _CpqScsiLogDrvBusIndex_Type(Integer32):
    """Custom type cpqScsiLogDrvBusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 225),
    )


_CpqScsiLogDrvBusIndex_Type.__name__ = "Integer32"
_CpqScsiLogDrvBusIndex_Object = MibTableColumn
cpqScsiLogDrvBusIndex = _CpqScsiLogDrvBusIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 3, 1, 1, 2),
    _CpqScsiLogDrvBusIndex_Type()
)
cpqScsiLogDrvBusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiLogDrvBusIndex.setStatus("mandatory")


class _CpqScsiLogDrvIndex_Type(Integer32):
    """Custom type cpqScsiLogDrvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 225),
    )


_CpqScsiLogDrvIndex_Type.__name__ = "Integer32"
_CpqScsiLogDrvIndex_Object = MibTableColumn
cpqScsiLogDrvIndex = _CpqScsiLogDrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 3, 1, 1, 3),
    _CpqScsiLogDrvIndex_Type()
)
cpqScsiLogDrvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiLogDrvIndex.setStatus("mandatory")


class _CpqScsiLogDrvFaultTol_Type(Integer32):
    """Custom type cpqScsiLogDrvFaultTol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("dataGuard", 4),
          ("distribDataGuard", 5),
          ("enhancedMirroring", 6),
          ("mirroring", 3),
          ("none", 2),
          ("other", 1))
    )


_CpqScsiLogDrvFaultTol_Type.__name__ = "Integer32"
_CpqScsiLogDrvFaultTol_Object = MibTableColumn
cpqScsiLogDrvFaultTol = _CpqScsiLogDrvFaultTol_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 3, 1, 1, 4),
    _CpqScsiLogDrvFaultTol_Type()
)
cpqScsiLogDrvFaultTol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiLogDrvFaultTol.setStatus("mandatory")


class _CpqScsiLogDrvStatus_Type(Integer32):
    """Custom type cpqScsiLogDrvStatus based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("badConnect", 9),
          ("degraded", 10),
          ("disabled", 11),
          ("failed", 3),
          ("ok", 2),
          ("other", 1),
          ("readyForRebuild", 6),
          ("rebuilding", 7),
          ("recovering", 5),
          ("unconfigured", 4),
          ("wrongDrive", 8))
    )


_CpqScsiLogDrvStatus_Type.__name__ = "Integer32"
_CpqScsiLogDrvStatus_Object = MibTableColumn
cpqScsiLogDrvStatus = _CpqScsiLogDrvStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 3, 1, 1, 5),
    _CpqScsiLogDrvStatus_Type()
)
cpqScsiLogDrvStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiLogDrvStatus.setStatus("mandatory")


class _CpqScsiLogDrvSize_Type(Integer32):
    """Custom type cpqScsiLogDrvSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpqScsiLogDrvSize_Type.__name__ = "Integer32"
_CpqScsiLogDrvSize_Object = MibTableColumn
cpqScsiLogDrvSize = _CpqScsiLogDrvSize_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 3, 1, 1, 6),
    _CpqScsiLogDrvSize_Type()
)
cpqScsiLogDrvSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiLogDrvSize.setStatus("mandatory")


class _CpqScsiLogDrvPhyDrvIDs_Type(OctetString):
    """Custom type cpqScsiLogDrvPhyDrvIDs based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqScsiLogDrvPhyDrvIDs_Type.__name__ = "OctetString"
_CpqScsiLogDrvPhyDrvIDs_Object = MibTableColumn
cpqScsiLogDrvPhyDrvIDs = _CpqScsiLogDrvPhyDrvIDs_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 3, 1, 1, 7),
    _CpqScsiLogDrvPhyDrvIDs_Type()
)
cpqScsiLogDrvPhyDrvIDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiLogDrvPhyDrvIDs.setStatus("mandatory")


class _CpqScsiLogDrvCondition_Type(Integer32):
    """Custom type cpqScsiLogDrvCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqScsiLogDrvCondition_Type.__name__ = "Integer32"
_CpqScsiLogDrvCondition_Object = MibTableColumn
cpqScsiLogDrvCondition = _CpqScsiLogDrvCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 3, 1, 1, 8),
    _CpqScsiLogDrvCondition_Type()
)
cpqScsiLogDrvCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiLogDrvCondition.setStatus("mandatory")
_CpqScsiLogDrvStripeSize_Type = Integer32
_CpqScsiLogDrvStripeSize_Object = MibTableColumn
cpqScsiLogDrvStripeSize = _CpqScsiLogDrvStripeSize_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 3, 1, 1, 9),
    _CpqScsiLogDrvStripeSize_Type()
)
cpqScsiLogDrvStripeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiLogDrvStripeSize.setStatus("mandatory")


class _CpqScsiLogDrvAvailSpares_Type(OctetString):
    """Custom type cpqScsiLogDrvAvailSpares based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqScsiLogDrvAvailSpares_Type.__name__ = "OctetString"
_CpqScsiLogDrvAvailSpares_Object = MibTableColumn
cpqScsiLogDrvAvailSpares = _CpqScsiLogDrvAvailSpares_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 3, 1, 1, 10),
    _CpqScsiLogDrvAvailSpares_Type()
)
cpqScsiLogDrvAvailSpares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiLogDrvAvailSpares.setStatus("mandatory")
_CpqScsiLogDrvPercentRebuild_Type = Gauge32
_CpqScsiLogDrvPercentRebuild_Object = MibTableColumn
cpqScsiLogDrvPercentRebuild = _CpqScsiLogDrvPercentRebuild_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 3, 1, 1, 11),
    _CpqScsiLogDrvPercentRebuild_Type()
)
cpqScsiLogDrvPercentRebuild.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiLogDrvPercentRebuild.setStatus("mandatory")


class _CpqScsiLogDrvOsName_Type(DisplayString):
    """Custom type cpqScsiLogDrvOsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqScsiLogDrvOsName_Type.__name__ = "DisplayString"
_CpqScsiLogDrvOsName_Object = MibTableColumn
cpqScsiLogDrvOsName = _CpqScsiLogDrvOsName_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 3, 1, 1, 12),
    _CpqScsiLogDrvOsName_Type()
)
cpqScsiLogDrvOsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiLogDrvOsName.setStatus("mandatory")
_CpqScsiPhyDrv_ObjectIdentity = ObjectIdentity
cpqScsiPhyDrv = _CpqScsiPhyDrv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 4)
)
_CpqScsiPhyDrvTable_Object = MibTable
cpqScsiPhyDrvTable = _CpqScsiPhyDrvTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 4, 1)
)
if mibBuilder.loadTexts:
    cpqScsiPhyDrvTable.setStatus("mandatory")
_CpqScsiPhyDrvEntry_Object = MibTableRow
cpqScsiPhyDrvEntry = _CpqScsiPhyDrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 4, 1, 1)
)
cpqScsiPhyDrvEntry.setIndexNames(
    (0, "CPQSCSI-MIB", "cpqScsiPhyDrvCntlrIndex"),
    (0, "CPQSCSI-MIB", "cpqScsiPhyDrvBusIndex"),
    (0, "CPQSCSI-MIB", "cpqScsiPhyDrvIndex"),
)
if mibBuilder.loadTexts:
    cpqScsiPhyDrvEntry.setStatus("mandatory")
_CpqScsiPhyDrvCntlrIndex_Type = Integer32
_CpqScsiPhyDrvCntlrIndex_Object = MibTableColumn
cpqScsiPhyDrvCntlrIndex = _CpqScsiPhyDrvCntlrIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 4, 1, 1, 1),
    _CpqScsiPhyDrvCntlrIndex_Type()
)
cpqScsiPhyDrvCntlrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiPhyDrvCntlrIndex.setStatus("mandatory")


class _CpqScsiPhyDrvBusIndex_Type(Integer32):
    """Custom type cpqScsiPhyDrvBusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 225),
    )


_CpqScsiPhyDrvBusIndex_Type.__name__ = "Integer32"
_CpqScsiPhyDrvBusIndex_Object = MibTableColumn
cpqScsiPhyDrvBusIndex = _CpqScsiPhyDrvBusIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 4, 1, 1, 2),
    _CpqScsiPhyDrvBusIndex_Type()
)
cpqScsiPhyDrvBusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiPhyDrvBusIndex.setStatus("mandatory")


class _CpqScsiPhyDrvIndex_Type(Integer32):
    """Custom type cpqScsiPhyDrvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 225),
    )


_CpqScsiPhyDrvIndex_Type.__name__ = "Integer32"
_CpqScsiPhyDrvIndex_Object = MibTableColumn
cpqScsiPhyDrvIndex = _CpqScsiPhyDrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 4, 1, 1, 3),
    _CpqScsiPhyDrvIndex_Type()
)
cpqScsiPhyDrvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiPhyDrvIndex.setStatus("mandatory")


class _CpqScsiPhyDrvModel_Type(DisplayString):
    """Custom type cpqScsiPhyDrvModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_CpqScsiPhyDrvModel_Type.__name__ = "DisplayString"
_CpqScsiPhyDrvModel_Object = MibTableColumn
cpqScsiPhyDrvModel = _CpqScsiPhyDrvModel_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 4, 1, 1, 4),
    _CpqScsiPhyDrvModel_Type()
)
cpqScsiPhyDrvModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiPhyDrvModel.setStatus("mandatory")


class _CpqScsiPhyDrvFWRev_Type(DisplayString):
    """Custom type cpqScsiPhyDrvFWRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CpqScsiPhyDrvFWRev_Type.__name__ = "DisplayString"
_CpqScsiPhyDrvFWRev_Object = MibTableColumn
cpqScsiPhyDrvFWRev = _CpqScsiPhyDrvFWRev_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 4, 1, 1, 5),
    _CpqScsiPhyDrvFWRev_Type()
)
cpqScsiPhyDrvFWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiPhyDrvFWRev.setStatus("mandatory")


class _CpqScsiPhyDrvVendor_Type(DisplayString):
    """Custom type cpqScsiPhyDrvVendor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_CpqScsiPhyDrvVendor_Type.__name__ = "DisplayString"
_CpqScsiPhyDrvVendor_Object = MibTableColumn
cpqScsiPhyDrvVendor = _CpqScsiPhyDrvVendor_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 4, 1, 1, 6),
    _CpqScsiPhyDrvVendor_Type()
)
cpqScsiPhyDrvVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiPhyDrvVendor.setStatus("mandatory")


class _CpqScsiPhyDrvSize_Type(Integer32):
    """Custom type cpqScsiPhyDrvSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpqScsiPhyDrvSize_Type.__name__ = "Integer32"
_CpqScsiPhyDrvSize_Object = MibTableColumn
cpqScsiPhyDrvSize = _CpqScsiPhyDrvSize_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 4, 1, 1, 7),
    _CpqScsiPhyDrvSize_Type()
)
cpqScsiPhyDrvSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiPhyDrvSize.setStatus("mandatory")


class _CpqScsiPhyDrvScsiID_Type(Integer32):
    """Custom type cpqScsiPhyDrvScsiID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqScsiPhyDrvScsiID_Type.__name__ = "Integer32"
_CpqScsiPhyDrvScsiID_Object = MibTableColumn
cpqScsiPhyDrvScsiID = _CpqScsiPhyDrvScsiID_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 4, 1, 1, 8),
    _CpqScsiPhyDrvScsiID_Type()
)
cpqScsiPhyDrvScsiID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiPhyDrvScsiID.setStatus("mandatory")


class _CpqScsiPhyDrvStatus_Type(Integer32):
    """Custom type cpqScsiPhyDrvStatus based on Integer32"""
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
        *(("badCable", 5),
          ("failed", 3),
          ("hardError", 12),
          ("missingWasFailed", 7),
          ("missingWasOffline", 11),
          ("missingWasOk", 6),
          ("missingWasPredictiveFailure", 9),
          ("notConfigured", 4),
          ("offline", 10),
          ("ok", 2),
          ("other", 1),
          ("predictiveFailure", 8))
    )


_CpqScsiPhyDrvStatus_Type.__name__ = "Integer32"
_CpqScsiPhyDrvStatus_Object = MibTableColumn
cpqScsiPhyDrvStatus = _CpqScsiPhyDrvStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 4, 1, 1, 9),
    _CpqScsiPhyDrvStatus_Type()
)
cpqScsiPhyDrvStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiPhyDrvStatus.setStatus("mandatory")
_CpqScsiPhyDrvServiceHours_Type = Counter32
_CpqScsiPhyDrvServiceHours_Object = MibTableColumn
cpqScsiPhyDrvServiceHours = _CpqScsiPhyDrvServiceHours_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 4, 1, 1, 10),
    _CpqScsiPhyDrvServiceHours_Type()
)
cpqScsiPhyDrvServiceHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiPhyDrvServiceHours.setStatus("mandatory")
_CpqScsiPhyDrvHighReadSectors_Type = Counter32
_CpqScsiPhyDrvHighReadSectors_Object = MibTableColumn
cpqScsiPhyDrvHighReadSectors = _CpqScsiPhyDrvHighReadSectors_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 4, 1, 1, 11),
    _CpqScsiPhyDrvHighReadSectors_Type()
)
cpqScsiPhyDrvHighReadSectors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiPhyDrvHighReadSectors.setStatus("mandatory")
_CpqScsiPhyDrvLowReadSectors_Type = Counter32
_CpqScsiPhyDrvLowReadSectors_Object = MibTableColumn
cpqScsiPhyDrvLowReadSectors = _CpqScsiPhyDrvLowReadSectors_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 4, 1, 1, 12),
    _CpqScsiPhyDrvLowReadSectors_Type()
)
cpqScsiPhyDrvLowReadSectors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiPhyDrvLowReadSectors.setStatus("mandatory")
_CpqScsiPhyDrvHighWriteSectors_Type = Counter32
_CpqScsiPhyDrvHighWriteSectors_Object = MibTableColumn
cpqScsiPhyDrvHighWriteSectors = _CpqScsiPhyDrvHighWriteSectors_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 4, 1, 1, 13),
    _CpqScsiPhyDrvHighWriteSectors_Type()
)
cpqScsiPhyDrvHighWriteSectors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiPhyDrvHighWriteSectors.setStatus("mandatory")
_CpqScsiPhyDrvLowWriteSectors_Type = Counter32
_CpqScsiPhyDrvLowWriteSectors_Object = MibTableColumn
cpqScsiPhyDrvLowWriteSectors = _CpqScsiPhyDrvLowWriteSectors_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 4, 1, 1, 14),
    _CpqScsiPhyDrvLowWriteSectors_Type()
)
cpqScsiPhyDrvLowWriteSectors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiPhyDrvLowWriteSectors.setStatus("mandatory")
_CpqScsiPhyDrvHardReadErrs_Type = Counter32
_CpqScsiPhyDrvHardReadErrs_Object = MibTableColumn
cpqScsiPhyDrvHardReadErrs = _CpqScsiPhyDrvHardReadErrs_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 4, 1, 1, 15),
    _CpqScsiPhyDrvHardReadErrs_Type()
)
cpqScsiPhyDrvHardReadErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiPhyDrvHardReadErrs.setStatus("mandatory")
_CpqScsiPhyDrvHardWriteErrs_Type = Counter32
_CpqScsiPhyDrvHardWriteErrs_Object = MibTableColumn
cpqScsiPhyDrvHardWriteErrs = _CpqScsiPhyDrvHardWriteErrs_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 4, 1, 1, 16),
    _CpqScsiPhyDrvHardWriteErrs_Type()
)
cpqScsiPhyDrvHardWriteErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiPhyDrvHardWriteErrs.setStatus("mandatory")
_CpqScsiPhyDrvEccCorrReads_Type = Counter32
_CpqScsiPhyDrvEccCorrReads_Object = MibTableColumn
cpqScsiPhyDrvEccCorrReads = _CpqScsiPhyDrvEccCorrReads_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 4, 1, 1, 17),
    _CpqScsiPhyDrvEccCorrReads_Type()
)
cpqScsiPhyDrvEccCorrReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiPhyDrvEccCorrReads.setStatus("mandatory")
_CpqScsiPhyDrvRecvReadErrs_Type = Counter32
_CpqScsiPhyDrvRecvReadErrs_Object = MibTableColumn
cpqScsiPhyDrvRecvReadErrs = _CpqScsiPhyDrvRecvReadErrs_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 4, 1, 1, 18),
    _CpqScsiPhyDrvRecvReadErrs_Type()
)
cpqScsiPhyDrvRecvReadErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiPhyDrvRecvReadErrs.setStatus("mandatory")
_CpqScsiPhyDrvRecvWriteErrs_Type = Counter32
_CpqScsiPhyDrvRecvWriteErrs_Object = MibTableColumn
cpqScsiPhyDrvRecvWriteErrs = _CpqScsiPhyDrvRecvWriteErrs_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 4, 1, 1, 19),
    _CpqScsiPhyDrvRecvWriteErrs_Type()
)
cpqScsiPhyDrvRecvWriteErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiPhyDrvRecvWriteErrs.setStatus("mandatory")
_CpqScsiPhyDrvSeekErrs_Type = Counter32
_CpqScsiPhyDrvSeekErrs_Object = MibTableColumn
cpqScsiPhyDrvSeekErrs = _CpqScsiPhyDrvSeekErrs_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 4, 1, 1, 20),
    _CpqScsiPhyDrvSeekErrs_Type()
)
cpqScsiPhyDrvSeekErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiPhyDrvSeekErrs.setStatus("mandatory")
_CpqScsiPhyDrvSpinupTime_Type = Integer32
_CpqScsiPhyDrvSpinupTime_Object = MibTableColumn
cpqScsiPhyDrvSpinupTime = _CpqScsiPhyDrvSpinupTime_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 4, 1, 1, 21),
    _CpqScsiPhyDrvSpinupTime_Type()
)
cpqScsiPhyDrvSpinupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiPhyDrvSpinupTime.setStatus("mandatory")
_CpqScsiPhyDrvUsedReallocs_Type = Counter32
_CpqScsiPhyDrvUsedReallocs_Object = MibTableColumn
cpqScsiPhyDrvUsedReallocs = _CpqScsiPhyDrvUsedReallocs_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 4, 1, 1, 22),
    _CpqScsiPhyDrvUsedReallocs_Type()
)
cpqScsiPhyDrvUsedReallocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiPhyDrvUsedReallocs.setStatus("mandatory")
_CpqScsiPhyDrvTimeouts_Type = Counter32
_CpqScsiPhyDrvTimeouts_Object = MibTableColumn
cpqScsiPhyDrvTimeouts = _CpqScsiPhyDrvTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 4, 1, 1, 23),
    _CpqScsiPhyDrvTimeouts_Type()
)
cpqScsiPhyDrvTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiPhyDrvTimeouts.setStatus("mandatory")
_CpqScsiPhyDrvPostErrs_Type = Counter32
_CpqScsiPhyDrvPostErrs_Object = MibTableColumn
cpqScsiPhyDrvPostErrs = _CpqScsiPhyDrvPostErrs_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 4, 1, 1, 24),
    _CpqScsiPhyDrvPostErrs_Type()
)
cpqScsiPhyDrvPostErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiPhyDrvPostErrs.setStatus("mandatory")
_CpqScsiPhyDrvPostErrCode_Type = Integer32
_CpqScsiPhyDrvPostErrCode_Object = MibTableColumn
cpqScsiPhyDrvPostErrCode = _CpqScsiPhyDrvPostErrCode_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 4, 1, 1, 25),
    _CpqScsiPhyDrvPostErrCode_Type()
)
cpqScsiPhyDrvPostErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiPhyDrvPostErrCode.setStatus("mandatory")


class _CpqScsiPhyDrvCondition_Type(Integer32):
    """Custom type cpqScsiPhyDrvCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqScsiPhyDrvCondition_Type.__name__ = "Integer32"
_CpqScsiPhyDrvCondition_Object = MibTableColumn
cpqScsiPhyDrvCondition = _CpqScsiPhyDrvCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 4, 1, 1, 26),
    _CpqScsiPhyDrvCondition_Type()
)
cpqScsiPhyDrvCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiPhyDrvCondition.setStatus("mandatory")
_CpqScsiPhyDrvFuncTest1_Type = Gauge32
_CpqScsiPhyDrvFuncTest1_Object = MibTableColumn
cpqScsiPhyDrvFuncTest1 = _CpqScsiPhyDrvFuncTest1_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 4, 1, 1, 27),
    _CpqScsiPhyDrvFuncTest1_Type()
)
cpqScsiPhyDrvFuncTest1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiPhyDrvFuncTest1.setStatus("mandatory")
_CpqScsiPhyDrvFuncTest2_Type = Gauge32
_CpqScsiPhyDrvFuncTest2_Object = MibTableColumn
cpqScsiPhyDrvFuncTest2 = _CpqScsiPhyDrvFuncTest2_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 4, 1, 1, 28),
    _CpqScsiPhyDrvFuncTest2_Type()
)
cpqScsiPhyDrvFuncTest2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiPhyDrvFuncTest2.setStatus("mandatory")


class _CpqScsiPhyDrvStatsPreserved_Type(Integer32):
    """Custom type cpqScsiPhyDrvStatsPreserved based on Integer32"""
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
        *(("inNVRAM", 2),
          ("noCPUSupport", 4),
          ("noDrvSupport", 6),
          ("noFreeNVRAM", 5),
          ("noSoftwareSupport", 7),
          ("onDisk", 3),
          ("other", 1))
    )


_CpqScsiPhyDrvStatsPreserved_Type.__name__ = "Integer32"
_CpqScsiPhyDrvStatsPreserved_Object = MibTableColumn
cpqScsiPhyDrvStatsPreserved = _CpqScsiPhyDrvStatsPreserved_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 4, 1, 1, 29),
    _CpqScsiPhyDrvStatsPreserved_Type()
)
cpqScsiPhyDrvStatsPreserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiPhyDrvStatsPreserved.setStatus("mandatory")


class _CpqScsiPhyDrvSerialNum_Type(DisplayString):
    """Custom type cpqScsiPhyDrvSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CpqScsiPhyDrvSerialNum_Type.__name__ = "DisplayString"
_CpqScsiPhyDrvSerialNum_Object = MibTableColumn
cpqScsiPhyDrvSerialNum = _CpqScsiPhyDrvSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 4, 1, 1, 30),
    _CpqScsiPhyDrvSerialNum_Type()
)
cpqScsiPhyDrvSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiPhyDrvSerialNum.setStatus("mandatory")


class _CpqScsiPhyDrvLocation_Type(Integer32):
    """Custom type cpqScsiPhyDrvLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("proliant", 2))
    )


_CpqScsiPhyDrvLocation_Type.__name__ = "Integer32"
_CpqScsiPhyDrvLocation_Object = MibTableColumn
cpqScsiPhyDrvLocation = _CpqScsiPhyDrvLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 4, 1, 1, 31),
    _CpqScsiPhyDrvLocation_Type()
)
cpqScsiPhyDrvLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiPhyDrvLocation.setStatus("deprecated")


class _CpqScsiPhyDrvParent_Type(Integer32):
    """Custom type cpqScsiPhyDrvParent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 225),
    )


_CpqScsiPhyDrvParent_Type.__name__ = "Integer32"
_CpqScsiPhyDrvParent_Object = MibTableColumn
cpqScsiPhyDrvParent = _CpqScsiPhyDrvParent_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 4, 1, 1, 32),
    _CpqScsiPhyDrvParent_Type()
)
cpqScsiPhyDrvParent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiPhyDrvParent.setStatus("mandatory")


class _CpqScsiPhyDrvSectorSize_Type(Integer32):
    """Custom type cpqScsiPhyDrvSectorSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpqScsiPhyDrvSectorSize_Type.__name__ = "Integer32"
_CpqScsiPhyDrvSectorSize_Object = MibTableColumn
cpqScsiPhyDrvSectorSize = _CpqScsiPhyDrvSectorSize_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 4, 1, 1, 33),
    _CpqScsiPhyDrvSectorSize_Type()
)
cpqScsiPhyDrvSectorSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiPhyDrvSectorSize.setStatus("mandatory")


class _CpqScsiPhyDrvHotPlug_Type(Integer32):
    """Custom type cpqScsiPhyDrvHotPlug based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hotPlug", 2),
          ("nonHotPlug", 3),
          ("other", 1))
    )


_CpqScsiPhyDrvHotPlug_Type.__name__ = "Integer32"
_CpqScsiPhyDrvHotPlug_Object = MibTableColumn
cpqScsiPhyDrvHotPlug = _CpqScsiPhyDrvHotPlug_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 4, 1, 1, 34),
    _CpqScsiPhyDrvHotPlug_Type()
)
cpqScsiPhyDrvHotPlug.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiPhyDrvHotPlug.setStatus("mandatory")


class _CpqScsiPhyDrvPlacement_Type(Integer32):
    """Custom type cpqScsiPhyDrvPlacement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("external", 3),
          ("internal", 2),
          ("other", 1))
    )


_CpqScsiPhyDrvPlacement_Type.__name__ = "Integer32"
_CpqScsiPhyDrvPlacement_Object = MibTableColumn
cpqScsiPhyDrvPlacement = _CpqScsiPhyDrvPlacement_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 4, 1, 1, 35),
    _CpqScsiPhyDrvPlacement_Type()
)
cpqScsiPhyDrvPlacement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiPhyDrvPlacement.setStatus("mandatory")


class _CpqScsiPhyDrvPreFailMonitoring_Type(Integer32):
    """Custom type cpqScsiPhyDrvPreFailMonitoring based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("available", 3),
          ("notAvailable", 2),
          ("other", 1))
    )


_CpqScsiPhyDrvPreFailMonitoring_Type.__name__ = "Integer32"
_CpqScsiPhyDrvPreFailMonitoring_Object = MibTableColumn
cpqScsiPhyDrvPreFailMonitoring = _CpqScsiPhyDrvPreFailMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 4, 1, 1, 36),
    _CpqScsiPhyDrvPreFailMonitoring_Type()
)
cpqScsiPhyDrvPreFailMonitoring.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiPhyDrvPreFailMonitoring.setStatus("mandatory")


class _CpqScsiPhyDrvOsName_Type(DisplayString):
    """Custom type cpqScsiPhyDrvOsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqScsiPhyDrvOsName_Type.__name__ = "DisplayString"
_CpqScsiPhyDrvOsName_Object = MibTableColumn
cpqScsiPhyDrvOsName = _CpqScsiPhyDrvOsName_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 4, 1, 1, 37),
    _CpqScsiPhyDrvOsName_Type()
)
cpqScsiPhyDrvOsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiPhyDrvOsName.setStatus("mandatory")


class _CpqScsiPhyDrvRotationalSpeed_Type(Integer32):
    """Custom type cpqScsiPhyDrvRotationalSpeed based on Integer32"""
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
        *(("other", 1),
          ("rpm10K", 3),
          ("rpm15K", 4),
          ("rpm7200", 2))
    )


_CpqScsiPhyDrvRotationalSpeed_Type.__name__ = "Integer32"
_CpqScsiPhyDrvRotationalSpeed_Object = MibTableColumn
cpqScsiPhyDrvRotationalSpeed = _CpqScsiPhyDrvRotationalSpeed_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 4, 1, 1, 38),
    _CpqScsiPhyDrvRotationalSpeed_Type()
)
cpqScsiPhyDrvRotationalSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiPhyDrvRotationalSpeed.setStatus("mandatory")


class _CpqScsiPhyDrvMemberLogDrv_Type(Integer32):
    """Custom type cpqScsiPhyDrvMemberLogDrv based on Integer32"""
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
        *(("member", 2),
          ("nonMember", 4),
          ("other", 1),
          ("spare", 3))
    )


_CpqScsiPhyDrvMemberLogDrv_Type.__name__ = "Integer32"
_CpqScsiPhyDrvMemberLogDrv_Object = MibTableColumn
cpqScsiPhyDrvMemberLogDrv = _CpqScsiPhyDrvMemberLogDrv_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 4, 1, 1, 39),
    _CpqScsiPhyDrvMemberLogDrv_Type()
)
cpqScsiPhyDrvMemberLogDrv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiPhyDrvMemberLogDrv.setStatus("mandatory")
_CpqScsiTarget_ObjectIdentity = ObjectIdentity
cpqScsiTarget = _CpqScsiTarget_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 5)
)
_CpqScsiTargetTable_Object = MibTable
cpqScsiTargetTable = _CpqScsiTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 5, 1)
)
if mibBuilder.loadTexts:
    cpqScsiTargetTable.setStatus("mandatory")
_CpqScsiTargetEntry_Object = MibTableRow
cpqScsiTargetEntry = _CpqScsiTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 5, 1, 1)
)
cpqScsiTargetEntry.setIndexNames(
    (0, "CPQSCSI-MIB", "cpqScsiTargetCntlrIndex"),
    (0, "CPQSCSI-MIB", "cpqScsiTargetBusIndex"),
    (0, "CPQSCSI-MIB", "cpqScsiTargetScsiIdIndex"),
)
if mibBuilder.loadTexts:
    cpqScsiTargetEntry.setStatus("mandatory")
_CpqScsiTargetCntlrIndex_Type = Integer32
_CpqScsiTargetCntlrIndex_Object = MibTableColumn
cpqScsiTargetCntlrIndex = _CpqScsiTargetCntlrIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 5, 1, 1, 1),
    _CpqScsiTargetCntlrIndex_Type()
)
cpqScsiTargetCntlrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiTargetCntlrIndex.setStatus("mandatory")


class _CpqScsiTargetBusIndex_Type(Integer32):
    """Custom type cpqScsiTargetBusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqScsiTargetBusIndex_Type.__name__ = "Integer32"
_CpqScsiTargetBusIndex_Object = MibTableColumn
cpqScsiTargetBusIndex = _CpqScsiTargetBusIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 5, 1, 1, 2),
    _CpqScsiTargetBusIndex_Type()
)
cpqScsiTargetBusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiTargetBusIndex.setStatus("mandatory")


class _CpqScsiTargetScsiIdIndex_Type(Integer32):
    """Custom type cpqScsiTargetScsiIdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqScsiTargetScsiIdIndex_Type.__name__ = "Integer32"
_CpqScsiTargetScsiIdIndex_Object = MibTableColumn
cpqScsiTargetScsiIdIndex = _CpqScsiTargetScsiIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 5, 1, 1, 3),
    _CpqScsiTargetScsiIdIndex_Type()
)
cpqScsiTargetScsiIdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiTargetScsiIdIndex.setStatus("mandatory")


class _CpqScsiTargetType_Type(Integer32):
    """Custom type cpqScsiTargetType based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("cd-rom", 7),
          ("commDev", 11),
          ("disk", 2),
          ("jukeBox", 10),
          ("optical", 9),
          ("other", 1),
          ("printer", 4),
          ("processor", 5),
          ("scanner", 8),
          ("tape", 3),
          ("wormDrive", 6))
    )


_CpqScsiTargetType_Type.__name__ = "Integer32"
_CpqScsiTargetType_Object = MibTableColumn
cpqScsiTargetType = _CpqScsiTargetType_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 5, 1, 1, 4),
    _CpqScsiTargetType_Type()
)
cpqScsiTargetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiTargetType.setStatus("mandatory")


class _CpqScsiTargetModel_Type(DisplayString):
    """Custom type cpqScsiTargetModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_CpqScsiTargetModel_Type.__name__ = "DisplayString"
_CpqScsiTargetModel_Object = MibTableColumn
cpqScsiTargetModel = _CpqScsiTargetModel_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 5, 1, 1, 5),
    _CpqScsiTargetModel_Type()
)
cpqScsiTargetModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiTargetModel.setStatus("mandatory")


class _CpqScsiTargetFWRev_Type(DisplayString):
    """Custom type cpqScsiTargetFWRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CpqScsiTargetFWRev_Type.__name__ = "DisplayString"
_CpqScsiTargetFWRev_Object = MibTableColumn
cpqScsiTargetFWRev = _CpqScsiTargetFWRev_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 5, 1, 1, 6),
    _CpqScsiTargetFWRev_Type()
)
cpqScsiTargetFWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiTargetFWRev.setStatus("mandatory")


class _CpqScsiTargetVendor_Type(DisplayString):
    """Custom type cpqScsiTargetVendor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_CpqScsiTargetVendor_Type.__name__ = "DisplayString"
_CpqScsiTargetVendor_Object = MibTableColumn
cpqScsiTargetVendor = _CpqScsiTargetVendor_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 5, 1, 1, 7),
    _CpqScsiTargetVendor_Type()
)
cpqScsiTargetVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiTargetVendor.setStatus("mandatory")
_CpqScsiTargetParityErrs_Type = Counter32
_CpqScsiTargetParityErrs_Object = MibTableColumn
cpqScsiTargetParityErrs = _CpqScsiTargetParityErrs_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 5, 1, 1, 8),
    _CpqScsiTargetParityErrs_Type()
)
cpqScsiTargetParityErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiTargetParityErrs.setStatus("mandatory")
_CpqScsiTargetPhaseErrs_Type = Counter32
_CpqScsiTargetPhaseErrs_Object = MibTableColumn
cpqScsiTargetPhaseErrs = _CpqScsiTargetPhaseErrs_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 5, 1, 1, 9),
    _CpqScsiTargetPhaseErrs_Type()
)
cpqScsiTargetPhaseErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiTargetPhaseErrs.setStatus("mandatory")
_CpqScsiTargetSelectTimeouts_Type = Counter32
_CpqScsiTargetSelectTimeouts_Object = MibTableColumn
cpqScsiTargetSelectTimeouts = _CpqScsiTargetSelectTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 5, 1, 1, 10),
    _CpqScsiTargetSelectTimeouts_Type()
)
cpqScsiTargetSelectTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiTargetSelectTimeouts.setStatus("mandatory")
_CpqScsiTargetMsgRejects_Type = Counter32
_CpqScsiTargetMsgRejects_Object = MibTableColumn
cpqScsiTargetMsgRejects = _CpqScsiTargetMsgRejects_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 5, 1, 1, 11),
    _CpqScsiTargetMsgRejects_Type()
)
cpqScsiTargetMsgRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiTargetMsgRejects.setStatus("mandatory")


class _CpqScsiTargetNegPeriod_Type(Integer32):
    """Custom type cpqScsiTargetNegPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpqScsiTargetNegPeriod_Type.__name__ = "Integer32"
_CpqScsiTargetNegPeriod_Object = MibTableColumn
cpqScsiTargetNegPeriod = _CpqScsiTargetNegPeriod_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 5, 1, 1, 12),
    _CpqScsiTargetNegPeriod_Type()
)
cpqScsiTargetNegPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiTargetNegPeriod.setStatus("deprecated")


class _CpqScsiTargetLocation_Type(Integer32):
    """Custom type cpqScsiTargetLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("proliant", 2))
    )


_CpqScsiTargetLocation_Type.__name__ = "Integer32"
_CpqScsiTargetLocation_Object = MibTableColumn
cpqScsiTargetLocation = _CpqScsiTargetLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 5, 1, 1, 13),
    _CpqScsiTargetLocation_Type()
)
cpqScsiTargetLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiTargetLocation.setStatus("mandatory")
_CpqScsiTargetNegSpeed_Type = Integer32
_CpqScsiTargetNegSpeed_Object = MibTableColumn
cpqScsiTargetNegSpeed = _CpqScsiTargetNegSpeed_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 5, 1, 1, 14),
    _CpqScsiTargetNegSpeed_Type()
)
cpqScsiTargetNegSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiTargetNegSpeed.setStatus("mandatory")


class _CpqScsiTargetPhysWidth_Type(Integer32):
    """Custom type cpqScsiTargetPhysWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("narrow", 2),
          ("other", 1),
          ("wide16", 3))
    )


_CpqScsiTargetPhysWidth_Type.__name__ = "Integer32"
_CpqScsiTargetPhysWidth_Object = MibTableColumn
cpqScsiTargetPhysWidth = _CpqScsiTargetPhysWidth_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 5, 1, 1, 15),
    _CpqScsiTargetPhysWidth_Type()
)
cpqScsiTargetPhysWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiTargetPhysWidth.setStatus("mandatory")
_CpqScsiTargetNegWidth_Type = Integer32
_CpqScsiTargetNegWidth_Object = MibTableColumn
cpqScsiTargetNegWidth = _CpqScsiTargetNegWidth_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 5, 1, 1, 16),
    _CpqScsiTargetNegWidth_Type()
)
cpqScsiTargetNegWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiTargetNegWidth.setStatus("mandatory")


class _CpqScsiTargetTypeExtended_Type(Integer32):
    """Custom type cpqScsiTargetTypeExtended based on Integer32"""
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
        *(("autoloader", 7),
          ("cdJukebox", 5),
          ("cr3500", 6),
          ("dltAutoloader", 4),
          ("other", 1),
          ("pdcd", 2),
          ("removableDisk", 3))
    )


_CpqScsiTargetTypeExtended_Type.__name__ = "Integer32"
_CpqScsiTargetTypeExtended_Object = MibTableColumn
cpqScsiTargetTypeExtended = _CpqScsiTargetTypeExtended_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 5, 1, 1, 17),
    _CpqScsiTargetTypeExtended_Type()
)
cpqScsiTargetTypeExtended.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiTargetTypeExtended.setStatus("mandatory")


class _CpqScsiTargetCurrentSpeed_Type(Integer32):
    """Custom type cpqScsiTargetCurrentSpeed based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("asynchronous", 2),
          ("fast", 3),
          ("other", 1),
          ("scsi1", 7),
          ("ultra", 4),
          ("ultra2", 5),
          ("ultra3", 6),
          ("ultra4", 8))
    )


_CpqScsiTargetCurrentSpeed_Type.__name__ = "Integer32"
_CpqScsiTargetCurrentSpeed_Object = MibTableColumn
cpqScsiTargetCurrentSpeed = _CpqScsiTargetCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 5, 1, 1, 18),
    _CpqScsiTargetCurrentSpeed_Type()
)
cpqScsiTargetCurrentSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiTargetCurrentSpeed.setStatus("mandatory")
_CpqScsiCd_ObjectIdentity = ObjectIdentity
cpqScsiCd = _CpqScsiCd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 6)
)
_CpqScsiCdDrvTable_Object = MibTable
cpqScsiCdDrvTable = _CpqScsiCdDrvTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 6, 1)
)
if mibBuilder.loadTexts:
    cpqScsiCdDrvTable.setStatus("mandatory")
_CpqScsiCdDrvEntry_Object = MibTableRow
cpqScsiCdDrvEntry = _CpqScsiCdDrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 6, 1, 1)
)
cpqScsiCdDrvEntry.setIndexNames(
    (0, "CPQSCSI-MIB", "cpqScsiCdDrvCntlrIndex"),
    (0, "CPQSCSI-MIB", "cpqScsiCdDrvBusIndex"),
    (0, "CPQSCSI-MIB", "cpqScsiCdDrvScsiIdIndex"),
    (0, "CPQSCSI-MIB", "cpqScsiCdDrvLunIndex"),
)
if mibBuilder.loadTexts:
    cpqScsiCdDrvEntry.setStatus("mandatory")
_CpqScsiCdDrvCntlrIndex_Type = Integer32
_CpqScsiCdDrvCntlrIndex_Object = MibTableColumn
cpqScsiCdDrvCntlrIndex = _CpqScsiCdDrvCntlrIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 6, 1, 1, 1),
    _CpqScsiCdDrvCntlrIndex_Type()
)
cpqScsiCdDrvCntlrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiCdDrvCntlrIndex.setStatus("mandatory")


class _CpqScsiCdDrvBusIndex_Type(Integer32):
    """Custom type cpqScsiCdDrvBusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqScsiCdDrvBusIndex_Type.__name__ = "Integer32"
_CpqScsiCdDrvBusIndex_Object = MibTableColumn
cpqScsiCdDrvBusIndex = _CpqScsiCdDrvBusIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 6, 1, 1, 2),
    _CpqScsiCdDrvBusIndex_Type()
)
cpqScsiCdDrvBusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiCdDrvBusIndex.setStatus("mandatory")


class _CpqScsiCdDrvScsiIdIndex_Type(Integer32):
    """Custom type cpqScsiCdDrvScsiIdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqScsiCdDrvScsiIdIndex_Type.__name__ = "Integer32"
_CpqScsiCdDrvScsiIdIndex_Object = MibTableColumn
cpqScsiCdDrvScsiIdIndex = _CpqScsiCdDrvScsiIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 6, 1, 1, 3),
    _CpqScsiCdDrvScsiIdIndex_Type()
)
cpqScsiCdDrvScsiIdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiCdDrvScsiIdIndex.setStatus("mandatory")


class _CpqScsiCdDrvLunIndex_Type(Integer32):
    """Custom type cpqScsiCdDrvLunIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqScsiCdDrvLunIndex_Type.__name__ = "Integer32"
_CpqScsiCdDrvLunIndex_Object = MibTableColumn
cpqScsiCdDrvLunIndex = _CpqScsiCdDrvLunIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 6, 1, 1, 4),
    _CpqScsiCdDrvLunIndex_Type()
)
cpqScsiCdDrvLunIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiCdDrvLunIndex.setStatus("mandatory")


class _CpqScsiCdDrvModel_Type(DisplayString):
    """Custom type cpqScsiCdDrvModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_CpqScsiCdDrvModel_Type.__name__ = "DisplayString"
_CpqScsiCdDrvModel_Object = MibTableColumn
cpqScsiCdDrvModel = _CpqScsiCdDrvModel_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 6, 1, 1, 5),
    _CpqScsiCdDrvModel_Type()
)
cpqScsiCdDrvModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiCdDrvModel.setStatus("mandatory")


class _CpqScsiCdDrvVendor_Type(DisplayString):
    """Custom type cpqScsiCdDrvVendor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_CpqScsiCdDrvVendor_Type.__name__ = "DisplayString"
_CpqScsiCdDrvVendor_Object = MibTableColumn
cpqScsiCdDrvVendor = _CpqScsiCdDrvVendor_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 6, 1, 1, 6),
    _CpqScsiCdDrvVendor_Type()
)
cpqScsiCdDrvVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiCdDrvVendor.setStatus("mandatory")


class _CpqScsiCdDrvFwRev_Type(DisplayString):
    """Custom type cpqScsiCdDrvFwRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CpqScsiCdDrvFwRev_Type.__name__ = "DisplayString"
_CpqScsiCdDrvFwRev_Object = MibTableColumn
cpqScsiCdDrvFwRev = _CpqScsiCdDrvFwRev_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 6, 1, 1, 7),
    _CpqScsiCdDrvFwRev_Type()
)
cpqScsiCdDrvFwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiCdDrvFwRev.setStatus("mandatory")
_CpqCdLibraryTable_Object = MibTable
cpqCdLibraryTable = _CpqCdLibraryTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 6, 2)
)
if mibBuilder.loadTexts:
    cpqCdLibraryTable.setStatus("mandatory")
_CpqCdLibraryEntry_Object = MibTableRow
cpqCdLibraryEntry = _CpqCdLibraryEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 6, 2, 1)
)
cpqCdLibraryEntry.setIndexNames(
    (0, "CPQSCSI-MIB", "cpqCdLibraryCntlrIndex"),
    (0, "CPQSCSI-MIB", "cpqCdLibraryBusIndex"),
    (0, "CPQSCSI-MIB", "cpqCdLibraryScsiIdIndex"),
    (0, "CPQSCSI-MIB", "cpqCdLibraryLunIndex"),
)
if mibBuilder.loadTexts:
    cpqCdLibraryEntry.setStatus("mandatory")
_CpqCdLibraryCntlrIndex_Type = Integer32
_CpqCdLibraryCntlrIndex_Object = MibTableColumn
cpqCdLibraryCntlrIndex = _CpqCdLibraryCntlrIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 6, 2, 1, 1),
    _CpqCdLibraryCntlrIndex_Type()
)
cpqCdLibraryCntlrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCdLibraryCntlrIndex.setStatus("mandatory")


class _CpqCdLibraryBusIndex_Type(Integer32):
    """Custom type cpqCdLibraryBusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqCdLibraryBusIndex_Type.__name__ = "Integer32"
_CpqCdLibraryBusIndex_Object = MibTableColumn
cpqCdLibraryBusIndex = _CpqCdLibraryBusIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 6, 2, 1, 2),
    _CpqCdLibraryBusIndex_Type()
)
cpqCdLibraryBusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCdLibraryBusIndex.setStatus("mandatory")


class _CpqCdLibraryScsiIdIndex_Type(Integer32):
    """Custom type cpqCdLibraryScsiIdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqCdLibraryScsiIdIndex_Type.__name__ = "Integer32"
_CpqCdLibraryScsiIdIndex_Object = MibTableColumn
cpqCdLibraryScsiIdIndex = _CpqCdLibraryScsiIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 6, 2, 1, 3),
    _CpqCdLibraryScsiIdIndex_Type()
)
cpqCdLibraryScsiIdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCdLibraryScsiIdIndex.setStatus("mandatory")


class _CpqCdLibraryLunIndex_Type(Integer32):
    """Custom type cpqCdLibraryLunIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqCdLibraryLunIndex_Type.__name__ = "Integer32"
_CpqCdLibraryLunIndex_Object = MibTableColumn
cpqCdLibraryLunIndex = _CpqCdLibraryLunIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 6, 2, 1, 4),
    _CpqCdLibraryLunIndex_Type()
)
cpqCdLibraryLunIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCdLibraryLunIndex.setStatus("mandatory")


class _CpqCdLibraryCondition_Type(Integer32):
    """Custom type cpqCdLibraryCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqCdLibraryCondition_Type.__name__ = "Integer32"
_CpqCdLibraryCondition_Object = MibTableColumn
cpqCdLibraryCondition = _CpqCdLibraryCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 6, 2, 1, 5),
    _CpqCdLibraryCondition_Type()
)
cpqCdLibraryCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCdLibraryCondition.setStatus("mandatory")


class _CpqCdLibraryStatus_Type(Integer32):
    """Custom type cpqCdLibraryStatus based on Integer32"""
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
        *(("failed", 3),
          ("offline", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqCdLibraryStatus_Type.__name__ = "Integer32"
_CpqCdLibraryStatus_Object = MibTableColumn
cpqCdLibraryStatus = _CpqCdLibraryStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 6, 2, 1, 6),
    _CpqCdLibraryStatus_Type()
)
cpqCdLibraryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCdLibraryStatus.setStatus("mandatory")


class _CpqCdLibraryModel_Type(DisplayString):
    """Custom type cpqCdLibraryModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_CpqCdLibraryModel_Type.__name__ = "DisplayString"
_CpqCdLibraryModel_Object = MibTableColumn
cpqCdLibraryModel = _CpqCdLibraryModel_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 6, 2, 1, 7),
    _CpqCdLibraryModel_Type()
)
cpqCdLibraryModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCdLibraryModel.setStatus("mandatory")


class _CpqCdLibraryVendor_Type(DisplayString):
    """Custom type cpqCdLibraryVendor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_CpqCdLibraryVendor_Type.__name__ = "DisplayString"
_CpqCdLibraryVendor_Object = MibTableColumn
cpqCdLibraryVendor = _CpqCdLibraryVendor_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 6, 2, 1, 8),
    _CpqCdLibraryVendor_Type()
)
cpqCdLibraryVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCdLibraryVendor.setStatus("mandatory")


class _CpqCdLibrarySerialNumber_Type(DisplayString):
    """Custom type cpqCdLibrarySerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqCdLibrarySerialNumber_Type.__name__ = "DisplayString"
_CpqCdLibrarySerialNumber_Object = MibTableColumn
cpqCdLibrarySerialNumber = _CpqCdLibrarySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 6, 2, 1, 9),
    _CpqCdLibrarySerialNumber_Type()
)
cpqCdLibrarySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCdLibrarySerialNumber.setStatus("mandatory")


class _CpqCdLibraryDriveList_Type(OctetString):
    """Custom type cpqCdLibraryDriveList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqCdLibraryDriveList_Type.__name__ = "OctetString"
_CpqCdLibraryDriveList_Object = MibTableColumn
cpqCdLibraryDriveList = _CpqCdLibraryDriveList_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 6, 2, 1, 10),
    _CpqCdLibraryDriveList_Type()
)
cpqCdLibraryDriveList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCdLibraryDriveList.setStatus("mandatory")


class _CpqCdLibraryFwRev_Type(DisplayString):
    """Custom type cpqCdLibraryFwRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CpqCdLibraryFwRev_Type.__name__ = "DisplayString"
_CpqCdLibraryFwRev_Object = MibTableColumn
cpqCdLibraryFwRev = _CpqCdLibraryFwRev_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 6, 2, 1, 11),
    _CpqCdLibraryFwRev_Type()
)
cpqCdLibraryFwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCdLibraryFwRev.setStatus("mandatory")


class _CpqCdLibraryFwSubtype_Type(Integer32):
    """Custom type cpqCdLibraryFwSubtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqCdLibraryFwSubtype_Type.__name__ = "Integer32"
_CpqCdLibraryFwSubtype_Object = MibTableColumn
cpqCdLibraryFwSubtype = _CpqCdLibraryFwSubtype_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 2, 6, 2, 1, 12),
    _CpqCdLibraryFwSubtype_Type()
)
cpqCdLibraryFwSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCdLibraryFwSubtype.setStatus("mandatory")
_CpqScsiTrap_ObjectIdentity = ObjectIdentity
cpqScsiTrap = _CpqScsiTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 5, 3)
)
_CpqScsiTrapPkts_Type = Counter32
_CpqScsiTrapPkts_Object = MibScalar
cpqScsiTrapPkts = _CpqScsiTrapPkts_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 3, 1),
    _CpqScsiTrapPkts_Type()
)
cpqScsiTrapPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiTrapPkts.setStatus("deprecated")


class _CpqScsiTrapLogMaxSize_Type(Integer32):
    """Custom type cpqScsiTrapLogMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpqScsiTrapLogMaxSize_Type.__name__ = "Integer32"
_CpqScsiTrapLogMaxSize_Object = MibScalar
cpqScsiTrapLogMaxSize = _CpqScsiTrapLogMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 3, 2),
    _CpqScsiTrapLogMaxSize_Type()
)
cpqScsiTrapLogMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiTrapLogMaxSize.setStatus("deprecated")
_CpqScsiTrapLogTable_Object = MibTable
cpqScsiTrapLogTable = _CpqScsiTrapLogTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 3, 3)
)
if mibBuilder.loadTexts:
    cpqScsiTrapLogTable.setStatus("deprecated")
_CpqScsiTrapLogEntry_Object = MibTableRow
cpqScsiTrapLogEntry = _CpqScsiTrapLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 3, 3, 1)
)
cpqScsiTrapLogEntry.setIndexNames(
    (0, "CPQSCSI-MIB", "cpqScsiTrapLogIndex"),
)
if mibBuilder.loadTexts:
    cpqScsiTrapLogEntry.setStatus("deprecated")


class _CpqScsiTrapLogIndex_Type(Integer32):
    """Custom type cpqScsiTrapLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpqScsiTrapLogIndex_Type.__name__ = "Integer32"
_CpqScsiTrapLogIndex_Object = MibTableColumn
cpqScsiTrapLogIndex = _CpqScsiTrapLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 3, 3, 1, 1),
    _CpqScsiTrapLogIndex_Type()
)
cpqScsiTrapLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiTrapLogIndex.setStatus("deprecated")


class _CpqScsiTrapType_Type(Integer32):
    """Custom type cpqScsiTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5001,
              5002,
              5003)
        )
    )
    namedValues = NamedValues(
        *(("cpqScsi2CntlrStatusChange", 5001),
          ("cpqScsi2LogDrvStatusChange", 5002),
          ("cpqScsi2PhyDrvStatusChange", 5003),
          ("cpqScsiCntlrStatusChange", 1),
          ("cpqScsiLogDrvStatusChange", 2),
          ("cpqScsiPhyDrvStatusChange", 3))
    )


_CpqScsiTrapType_Type.__name__ = "Integer32"
_CpqScsiTrapType_Object = MibTableColumn
cpqScsiTrapType = _CpqScsiTrapType_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 3, 3, 1, 2),
    _CpqScsiTrapType_Type()
)
cpqScsiTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiTrapType.setStatus("deprecated")


class _CpqScsiTrapTime_Type(OctetString):
    """Custom type cpqScsiTrapTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_CpqScsiTrapTime_Type.__name__ = "OctetString"
_CpqScsiTrapTime_Object = MibTableColumn
cpqScsiTrapTime = _CpqScsiTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 3, 3, 1, 3),
    _CpqScsiTrapTime_Type()
)
cpqScsiTrapTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqScsiTrapTime.setStatus("deprecated")
_CpqTapeComponent_ObjectIdentity = ObjectIdentity
cpqTapeComponent = _CpqTapeComponent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 5, 4)
)
_CpqTapePhyDrv_ObjectIdentity = ObjectIdentity
cpqTapePhyDrv = _CpqTapePhyDrv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 1)
)
_CpqTapePhyDrvTable_Object = MibTable
cpqTapePhyDrvTable = _CpqTapePhyDrvTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 1, 1)
)
if mibBuilder.loadTexts:
    cpqTapePhyDrvTable.setStatus("mandatory")
_CpqTapePhyDrvEntry_Object = MibTableRow
cpqTapePhyDrvEntry = _CpqTapePhyDrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 1, 1, 1)
)
cpqTapePhyDrvEntry.setIndexNames(
    (0, "CPQSCSI-MIB", "cpqTapePhyDrvCntlrIndex"),
    (0, "CPQSCSI-MIB", "cpqTapePhyDrvBusIndex"),
    (0, "CPQSCSI-MIB", "cpqTapePhyDrvScsiIdIndex"),
    (0, "CPQSCSI-MIB", "cpqTapePhyDrvLunIndex"),
)
if mibBuilder.loadTexts:
    cpqTapePhyDrvEntry.setStatus("mandatory")
_CpqTapePhyDrvCntlrIndex_Type = Integer32
_CpqTapePhyDrvCntlrIndex_Object = MibTableColumn
cpqTapePhyDrvCntlrIndex = _CpqTapePhyDrvCntlrIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 1, 1, 1, 1),
    _CpqTapePhyDrvCntlrIndex_Type()
)
cpqTapePhyDrvCntlrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqTapePhyDrvCntlrIndex.setStatus("mandatory")


class _CpqTapePhyDrvBusIndex_Type(Integer32):
    """Custom type cpqTapePhyDrvBusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqTapePhyDrvBusIndex_Type.__name__ = "Integer32"
_CpqTapePhyDrvBusIndex_Object = MibTableColumn
cpqTapePhyDrvBusIndex = _CpqTapePhyDrvBusIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 1, 1, 1, 2),
    _CpqTapePhyDrvBusIndex_Type()
)
cpqTapePhyDrvBusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqTapePhyDrvBusIndex.setStatus("mandatory")


class _CpqTapePhyDrvScsiIdIndex_Type(Integer32):
    """Custom type cpqTapePhyDrvScsiIdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqTapePhyDrvScsiIdIndex_Type.__name__ = "Integer32"
_CpqTapePhyDrvScsiIdIndex_Object = MibTableColumn
cpqTapePhyDrvScsiIdIndex = _CpqTapePhyDrvScsiIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 1, 1, 1, 3),
    _CpqTapePhyDrvScsiIdIndex_Type()
)
cpqTapePhyDrvScsiIdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqTapePhyDrvScsiIdIndex.setStatus("mandatory")


class _CpqTapePhyDrvLunIndex_Type(Integer32):
    """Custom type cpqTapePhyDrvLunIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqTapePhyDrvLunIndex_Type.__name__ = "Integer32"
_CpqTapePhyDrvLunIndex_Object = MibTableColumn
cpqTapePhyDrvLunIndex = _CpqTapePhyDrvLunIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 1, 1, 1, 4),
    _CpqTapePhyDrvLunIndex_Type()
)
cpqTapePhyDrvLunIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqTapePhyDrvLunIndex.setStatus("mandatory")


class _CpqTapePhyDrvType_Type(Integer32):
    """Custom type cpqTapePhyDrvType based on Integer32"""
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
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("cpqAit35", 14),
          ("cpqAit35Lvd", 20),
          ("cpqAit50", 15),
          ("cpqCompaq", 21),
          ("cpqDat12-24", 11),
          ("cpqDat2-8", 4),
          ("cpqDat20-40", 16),
          ("cpqDat4-16", 2),
          ("cpqDat4-8", 9),
          ("cpqDatAuto", 3),
          ("cpqDatAuto12-24", 12),
          ("cpqDatAuto20-40", 18),
          ("cpqDlt10-20", 5),
          ("cpqDlt15-30", 7),
          ("cpqDlt20-40", 6),
          ("cpqDlt35-70", 8),
          ("cpqDlt40-80", 17),
          ("cpqMlr16-32", 13),
          ("cpqSlr4-8", 10),
          ("cpqSuperDlt1", 19),
          ("other", 1))
    )


_CpqTapePhyDrvType_Type.__name__ = "Integer32"
_CpqTapePhyDrvType_Object = MibTableColumn
cpqTapePhyDrvType = _CpqTapePhyDrvType_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 1, 1, 1, 5),
    _CpqTapePhyDrvType_Type()
)
cpqTapePhyDrvType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqTapePhyDrvType.setStatus("mandatory")


class _CpqTapePhyDrvCondition_Type(Integer32):
    """Custom type cpqTapePhyDrvCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqTapePhyDrvCondition_Type.__name__ = "Integer32"
_CpqTapePhyDrvCondition_Object = MibTableColumn
cpqTapePhyDrvCondition = _CpqTapePhyDrvCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 1, 1, 1, 6),
    _CpqTapePhyDrvCondition_Type()
)
cpqTapePhyDrvCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqTapePhyDrvCondition.setStatus("mandatory")


class _CpqTapePhyDrvMagSize_Type(Integer32):
    """Custom type cpqTapePhyDrvMagSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CpqTapePhyDrvMagSize_Type.__name__ = "Integer32"
_CpqTapePhyDrvMagSize_Object = MibTableColumn
cpqTapePhyDrvMagSize = _CpqTapePhyDrvMagSize_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 1, 1, 1, 7),
    _CpqTapePhyDrvMagSize_Type()
)
cpqTapePhyDrvMagSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqTapePhyDrvMagSize.setStatus("mandatory")


class _CpqTapePhyDrvSerialNumber_Type(DisplayString):
    """Custom type cpqTapePhyDrvSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqTapePhyDrvSerialNumber_Type.__name__ = "DisplayString"
_CpqTapePhyDrvSerialNumber_Object = MibTableColumn
cpqTapePhyDrvSerialNumber = _CpqTapePhyDrvSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 1, 1, 1, 8),
    _CpqTapePhyDrvSerialNumber_Type()
)
cpqTapePhyDrvSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqTapePhyDrvSerialNumber.setStatus("mandatory")


class _CpqTapePhyDrvCleanReq_Type(Integer32):
    """Custom type cpqTapePhyDrvCleanReq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 3),
          ("other", 1),
          ("true", 2))
    )


_CpqTapePhyDrvCleanReq_Type.__name__ = "Integer32"
_CpqTapePhyDrvCleanReq_Object = MibTableColumn
cpqTapePhyDrvCleanReq = _CpqTapePhyDrvCleanReq_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 1, 1, 1, 9),
    _CpqTapePhyDrvCleanReq_Type()
)
cpqTapePhyDrvCleanReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqTapePhyDrvCleanReq.setStatus("mandatory")


class _CpqTapePhyDrvCleanTapeRepl_Type(Integer32):
    """Custom type cpqTapePhyDrvCleanTapeRepl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 3),
          ("other", 1),
          ("true", 2))
    )


_CpqTapePhyDrvCleanTapeRepl_Type.__name__ = "Integer32"
_CpqTapePhyDrvCleanTapeRepl_Object = MibTableColumn
cpqTapePhyDrvCleanTapeRepl = _CpqTapePhyDrvCleanTapeRepl_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 1, 1, 1, 10),
    _CpqTapePhyDrvCleanTapeRepl_Type()
)
cpqTapePhyDrvCleanTapeRepl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqTapePhyDrvCleanTapeRepl.setStatus("mandatory")


class _CpqTapePhyDrvFwSubtype_Type(Integer32):
    """Custom type cpqTapePhyDrvFwSubtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqTapePhyDrvFwSubtype_Type.__name__ = "Integer32"
_CpqTapePhyDrvFwSubtype_Object = MibTableColumn
cpqTapePhyDrvFwSubtype = _CpqTapePhyDrvFwSubtype_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 1, 1, 1, 11),
    _CpqTapePhyDrvFwSubtype_Type()
)
cpqTapePhyDrvFwSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqTapePhyDrvFwSubtype.setStatus("mandatory")


class _CpqTapePhyDrvName_Type(DisplayString):
    """Custom type cpqTapePhyDrvName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CpqTapePhyDrvName_Type.__name__ = "DisplayString"
_CpqTapePhyDrvName_Object = MibTableColumn
cpqTapePhyDrvName = _CpqTapePhyDrvName_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 1, 1, 1, 12),
    _CpqTapePhyDrvName_Type()
)
cpqTapePhyDrvName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqTapePhyDrvName.setStatus("mandatory")
_CpqTapePhyDrvCleanTapeCount_Type = Integer32
_CpqTapePhyDrvCleanTapeCount_Object = MibTableColumn
cpqTapePhyDrvCleanTapeCount = _CpqTapePhyDrvCleanTapeCount_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 1, 1, 1, 13),
    _CpqTapePhyDrvCleanTapeCount_Type()
)
cpqTapePhyDrvCleanTapeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqTapePhyDrvCleanTapeCount.setStatus("mandatory")


class _CpqTapePhyDrvFwRev_Type(DisplayString):
    """Custom type cpqTapePhyDrvFwRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CpqTapePhyDrvFwRev_Type.__name__ = "DisplayString"
_CpqTapePhyDrvFwRev_Object = MibTableColumn
cpqTapePhyDrvFwRev = _CpqTapePhyDrvFwRev_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 1, 1, 1, 14),
    _CpqTapePhyDrvFwRev_Type()
)
cpqTapePhyDrvFwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqTapePhyDrvFwRev.setStatus("mandatory")


class _CpqTapePhyDrvStatus_Type(Integer32):
    """Custom type cpqTapePhyDrvStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("failed", 4),
          ("missingWasFailed", 7),
          ("missingWasOffline", 8),
          ("missingWasOk", 6),
          ("offline", 5),
          ("ok", 2),
          ("other", 1))
    )


_CpqTapePhyDrvStatus_Type.__name__ = "Integer32"
_CpqTapePhyDrvStatus_Object = MibTableColumn
cpqTapePhyDrvStatus = _CpqTapePhyDrvStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 1, 1, 1, 15),
    _CpqTapePhyDrvStatus_Type()
)
cpqTapePhyDrvStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqTapePhyDrvStatus.setStatus("mandatory")


class _CpqTapePhyDrvHotPlug_Type(Integer32):
    """Custom type cpqTapePhyDrvHotPlug based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hotPlug", 2),
          ("nonHotPlug", 3),
          ("other", 1))
    )


_CpqTapePhyDrvHotPlug_Type.__name__ = "Integer32"
_CpqTapePhyDrvHotPlug_Object = MibTableColumn
cpqTapePhyDrvHotPlug = _CpqTapePhyDrvHotPlug_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 1, 1, 1, 16),
    _CpqTapePhyDrvHotPlug_Type()
)
cpqTapePhyDrvHotPlug.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqTapePhyDrvHotPlug.setStatus("mandatory")


class _CpqTapePhyDrvPlacement_Type(Integer32):
    """Custom type cpqTapePhyDrvPlacement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("external", 3),
          ("internal", 2),
          ("other", 1))
    )


_CpqTapePhyDrvPlacement_Type.__name__ = "Integer32"
_CpqTapePhyDrvPlacement_Object = MibTableColumn
cpqTapePhyDrvPlacement = _CpqTapePhyDrvPlacement_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 1, 1, 1, 17),
    _CpqTapePhyDrvPlacement_Type()
)
cpqTapePhyDrvPlacement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqTapePhyDrvPlacement.setStatus("mandatory")


class _CpqTapePhyDrvLibraryDrive_Type(Integer32):
    """Custom type cpqTapePhyDrvLibraryDrive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 3),
          ("other", 1),
          ("true", 2))
    )


_CpqTapePhyDrvLibraryDrive_Type.__name__ = "Integer32"
_CpqTapePhyDrvLibraryDrive_Object = MibTableColumn
cpqTapePhyDrvLibraryDrive = _CpqTapePhyDrvLibraryDrive_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 1, 1, 1, 18),
    _CpqTapePhyDrvLibraryDrive_Type()
)
cpqTapePhyDrvLibraryDrive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqTapePhyDrvLibraryDrive.setStatus("mandatory")


class _CpqTapePhyDrvLoaderName_Type(DisplayString):
    """Custom type cpqTapePhyDrvLoaderName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CpqTapePhyDrvLoaderName_Type.__name__ = "DisplayString"
_CpqTapePhyDrvLoaderName_Object = MibTableColumn
cpqTapePhyDrvLoaderName = _CpqTapePhyDrvLoaderName_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 1, 1, 1, 19),
    _CpqTapePhyDrvLoaderName_Type()
)
cpqTapePhyDrvLoaderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqTapePhyDrvLoaderName.setStatus("mandatory")


class _CpqTapePhyDrvLoaderFwRev_Type(DisplayString):
    """Custom type cpqTapePhyDrvLoaderFwRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CpqTapePhyDrvLoaderFwRev_Type.__name__ = "DisplayString"
_CpqTapePhyDrvLoaderFwRev_Object = MibTableColumn
cpqTapePhyDrvLoaderFwRev = _CpqTapePhyDrvLoaderFwRev_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 1, 1, 1, 20),
    _CpqTapePhyDrvLoaderFwRev_Type()
)
cpqTapePhyDrvLoaderFwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqTapePhyDrvLoaderFwRev.setStatus("mandatory")


class _CpqTapePhyDrvLoaderSerialNum_Type(DisplayString):
    """Custom type cpqTapePhyDrvLoaderSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqTapePhyDrvLoaderSerialNum_Type.__name__ = "DisplayString"
_CpqTapePhyDrvLoaderSerialNum_Object = MibTableColumn
cpqTapePhyDrvLoaderSerialNum = _CpqTapePhyDrvLoaderSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 1, 1, 1, 21),
    _CpqTapePhyDrvLoaderSerialNum_Type()
)
cpqTapePhyDrvLoaderSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqTapePhyDrvLoaderSerialNum.setStatus("mandatory")
_CpqTapeCounters_ObjectIdentity = ObjectIdentity
cpqTapeCounters = _CpqTapeCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 2)
)
_CpqTapeCountersTable_Object = MibTable
cpqTapeCountersTable = _CpqTapeCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 2, 1)
)
if mibBuilder.loadTexts:
    cpqTapeCountersTable.setStatus("mandatory")
_CpqTapeCountersEntry_Object = MibTableRow
cpqTapeCountersEntry = _CpqTapeCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 2, 1, 1)
)
cpqTapeCountersEntry.setIndexNames(
    (0, "CPQSCSI-MIB", "cpqTapeCountersCntlrIndex"),
    (0, "CPQSCSI-MIB", "cpqTapeCountersBusIndex"),
    (0, "CPQSCSI-MIB", "cpqTapeCountersScsiIdIndex"),
    (0, "CPQSCSI-MIB", "cpqTapeCountersLunIndex"),
)
if mibBuilder.loadTexts:
    cpqTapeCountersEntry.setStatus("mandatory")
_CpqTapeCountersCntlrIndex_Type = Integer32
_CpqTapeCountersCntlrIndex_Object = MibTableColumn
cpqTapeCountersCntlrIndex = _CpqTapeCountersCntlrIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 2, 1, 1, 1),
    _CpqTapeCountersCntlrIndex_Type()
)
cpqTapeCountersCntlrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqTapeCountersCntlrIndex.setStatus("mandatory")


class _CpqTapeCountersBusIndex_Type(Integer32):
    """Custom type cpqTapeCountersBusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqTapeCountersBusIndex_Type.__name__ = "Integer32"
_CpqTapeCountersBusIndex_Object = MibTableColumn
cpqTapeCountersBusIndex = _CpqTapeCountersBusIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 2, 1, 1, 2),
    _CpqTapeCountersBusIndex_Type()
)
cpqTapeCountersBusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqTapeCountersBusIndex.setStatus("mandatory")


class _CpqTapeCountersScsiIdIndex_Type(Integer32):
    """Custom type cpqTapeCountersScsiIdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqTapeCountersScsiIdIndex_Type.__name__ = "Integer32"
_CpqTapeCountersScsiIdIndex_Object = MibTableColumn
cpqTapeCountersScsiIdIndex = _CpqTapeCountersScsiIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 2, 1, 1, 3),
    _CpqTapeCountersScsiIdIndex_Type()
)
cpqTapeCountersScsiIdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqTapeCountersScsiIdIndex.setStatus("mandatory")


class _CpqTapeCountersLunIndex_Type(Integer32):
    """Custom type cpqTapeCountersLunIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqTapeCountersLunIndex_Type.__name__ = "Integer32"
_CpqTapeCountersLunIndex_Object = MibTableColumn
cpqTapeCountersLunIndex = _CpqTapeCountersLunIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 2, 1, 1, 4),
    _CpqTapeCountersLunIndex_Type()
)
cpqTapeCountersLunIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqTapeCountersLunIndex.setStatus("mandatory")
_CpqTapeCountersReWrites_Type = Counter32
_CpqTapeCountersReWrites_Object = MibTableColumn
cpqTapeCountersReWrites = _CpqTapeCountersReWrites_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 2, 1, 1, 5),
    _CpqTapeCountersReWrites_Type()
)
cpqTapeCountersReWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqTapeCountersReWrites.setStatus("mandatory")
_CpqTapeCountersReReads_Type = Counter32
_CpqTapeCountersReReads_Object = MibTableColumn
cpqTapeCountersReReads = _CpqTapeCountersReReads_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 2, 1, 1, 6),
    _CpqTapeCountersReReads_Type()
)
cpqTapeCountersReReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqTapeCountersReReads.setStatus("mandatory")
_CpqTapeCountersTotalErrors_Type = Counter32
_CpqTapeCountersTotalErrors_Object = MibTableColumn
cpqTapeCountersTotalErrors = _CpqTapeCountersTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 2, 1, 1, 7),
    _CpqTapeCountersTotalErrors_Type()
)
cpqTapeCountersTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqTapeCountersTotalErrors.setStatus("mandatory")
_CpqTapeCountersTotalUncorrectable_Type = Counter32
_CpqTapeCountersTotalUncorrectable_Object = MibTableColumn
cpqTapeCountersTotalUncorrectable = _CpqTapeCountersTotalUncorrectable_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 2, 1, 1, 8),
    _CpqTapeCountersTotalUncorrectable_Type()
)
cpqTapeCountersTotalUncorrectable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqTapeCountersTotalUncorrectable.setStatus("mandatory")
_CpqTapeCountersTotalBytes_Type = Counter32
_CpqTapeCountersTotalBytes_Object = MibTableColumn
cpqTapeCountersTotalBytes = _CpqTapeCountersTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 2, 1, 1, 9),
    _CpqTapeCountersTotalBytes_Type()
)
cpqTapeCountersTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqTapeCountersTotalBytes.setStatus("mandatory")
_CpqTapeLibrary_ObjectIdentity = ObjectIdentity
cpqTapeLibrary = _CpqTapeLibrary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 3)
)
_CpqTapeLibraryTable_Object = MibTable
cpqTapeLibraryTable = _CpqTapeLibraryTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 3, 1)
)
if mibBuilder.loadTexts:
    cpqTapeLibraryTable.setStatus("mandatory")
_CpqTapeLibraryEntry_Object = MibTableRow
cpqTapeLibraryEntry = _CpqTapeLibraryEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 3, 1, 1)
)
cpqTapeLibraryEntry.setIndexNames(
    (0, "CPQSCSI-MIB", "cpqTapeLibraryCntlrIndex"),
    (0, "CPQSCSI-MIB", "cpqTapeLibraryBusIndex"),
    (0, "CPQSCSI-MIB", "cpqTapeLibraryScsiIdIndex"),
    (0, "CPQSCSI-MIB", "cpqTapeLibraryLunIndex"),
)
if mibBuilder.loadTexts:
    cpqTapeLibraryEntry.setStatus("mandatory")
_CpqTapeLibraryCntlrIndex_Type = Integer32
_CpqTapeLibraryCntlrIndex_Object = MibTableColumn
cpqTapeLibraryCntlrIndex = _CpqTapeLibraryCntlrIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 3, 1, 1, 1),
    _CpqTapeLibraryCntlrIndex_Type()
)
cpqTapeLibraryCntlrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqTapeLibraryCntlrIndex.setStatus("mandatory")


class _CpqTapeLibraryBusIndex_Type(Integer32):
    """Custom type cpqTapeLibraryBusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqTapeLibraryBusIndex_Type.__name__ = "Integer32"
_CpqTapeLibraryBusIndex_Object = MibTableColumn
cpqTapeLibraryBusIndex = _CpqTapeLibraryBusIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 3, 1, 1, 2),
    _CpqTapeLibraryBusIndex_Type()
)
cpqTapeLibraryBusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqTapeLibraryBusIndex.setStatus("mandatory")


class _CpqTapeLibraryScsiIdIndex_Type(Integer32):
    """Custom type cpqTapeLibraryScsiIdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqTapeLibraryScsiIdIndex_Type.__name__ = "Integer32"
_CpqTapeLibraryScsiIdIndex_Object = MibTableColumn
cpqTapeLibraryScsiIdIndex = _CpqTapeLibraryScsiIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 3, 1, 1, 3),
    _CpqTapeLibraryScsiIdIndex_Type()
)
cpqTapeLibraryScsiIdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqTapeLibraryScsiIdIndex.setStatus("mandatory")


class _CpqTapeLibraryLunIndex_Type(Integer32):
    """Custom type cpqTapeLibraryLunIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqTapeLibraryLunIndex_Type.__name__ = "Integer32"
_CpqTapeLibraryLunIndex_Object = MibTableColumn
cpqTapeLibraryLunIndex = _CpqTapeLibraryLunIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 3, 1, 1, 4),
    _CpqTapeLibraryLunIndex_Type()
)
cpqTapeLibraryLunIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqTapeLibraryLunIndex.setStatus("mandatory")


class _CpqTapeLibraryCondition_Type(Integer32):
    """Custom type cpqTapeLibraryCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqTapeLibraryCondition_Type.__name__ = "Integer32"
_CpqTapeLibraryCondition_Object = MibTableColumn
cpqTapeLibraryCondition = _CpqTapeLibraryCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 3, 1, 1, 5),
    _CpqTapeLibraryCondition_Type()
)
cpqTapeLibraryCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqTapeLibraryCondition.setStatus("mandatory")


class _CpqTapeLibraryStatus_Type(Integer32):
    """Custom type cpqTapeLibraryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64535),
    )


_CpqTapeLibraryStatus_Type.__name__ = "Integer32"
_CpqTapeLibraryStatus_Object = MibTableColumn
cpqTapeLibraryStatus = _CpqTapeLibraryStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 3, 1, 1, 6),
    _CpqTapeLibraryStatus_Type()
)
cpqTapeLibraryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqTapeLibraryStatus.setStatus("mandatory")


class _CpqTapeLibraryDoorStatus_Type(Integer32):
    """Custom type cpqTapeLibraryDoorStatus based on Integer32"""
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
        *(("closed", 2),
          ("notSupported", 4),
          ("open", 3),
          ("other", 1))
    )


_CpqTapeLibraryDoorStatus_Type.__name__ = "Integer32"
_CpqTapeLibraryDoorStatus_Object = MibTableColumn
cpqTapeLibraryDoorStatus = _CpqTapeLibraryDoorStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 3, 1, 1, 7),
    _CpqTapeLibraryDoorStatus_Type()
)
cpqTapeLibraryDoorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqTapeLibraryDoorStatus.setStatus("mandatory")
_CpqTapeLibraryStatHours_Type = Counter32
_CpqTapeLibraryStatHours_Object = MibTableColumn
cpqTapeLibraryStatHours = _CpqTapeLibraryStatHours_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 3, 1, 1, 8),
    _CpqTapeLibraryStatHours_Type()
)
cpqTapeLibraryStatHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqTapeLibraryStatHours.setStatus("mandatory")
_CpqTapeLibraryStatMoves_Type = Counter32
_CpqTapeLibraryStatMoves_Object = MibTableColumn
cpqTapeLibraryStatMoves = _CpqTapeLibraryStatMoves_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 3, 1, 1, 9),
    _CpqTapeLibraryStatMoves_Type()
)
cpqTapeLibraryStatMoves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqTapeLibraryStatMoves.setStatus("mandatory")


class _CpqTapeLibraryName_Type(DisplayString):
    """Custom type cpqTapeLibraryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CpqTapeLibraryName_Type.__name__ = "DisplayString"
_CpqTapeLibraryName_Object = MibTableColumn
cpqTapeLibraryName = _CpqTapeLibraryName_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 3, 1, 1, 10),
    _CpqTapeLibraryName_Type()
)
cpqTapeLibraryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqTapeLibraryName.setStatus("mandatory")


class _CpqTapeLibrarySerialNumber_Type(DisplayString):
    """Custom type cpqTapeLibrarySerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqTapeLibrarySerialNumber_Type.__name__ = "DisplayString"
_CpqTapeLibrarySerialNumber_Object = MibTableColumn
cpqTapeLibrarySerialNumber = _CpqTapeLibrarySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 3, 1, 1, 11),
    _CpqTapeLibrarySerialNumber_Type()
)
cpqTapeLibrarySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqTapeLibrarySerialNumber.setStatus("mandatory")


class _CpqTapeLibraryDriveList_Type(OctetString):
    """Custom type cpqTapeLibraryDriveList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 320),
    )


_CpqTapeLibraryDriveList_Type.__name__ = "OctetString"
_CpqTapeLibraryDriveList_Object = MibTableColumn
cpqTapeLibraryDriveList = _CpqTapeLibraryDriveList_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 3, 1, 1, 12),
    _CpqTapeLibraryDriveList_Type()
)
cpqTapeLibraryDriveList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqTapeLibraryDriveList.setStatus("deprecated")


class _CpqTapeLibraryState_Type(Integer32):
    """Custom type cpqTapeLibraryState based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("offline", 5),
          ("ok", 2),
          ("other", 1))
    )


_CpqTapeLibraryState_Type.__name__ = "Integer32"
_CpqTapeLibraryState_Object = MibTableColumn
cpqTapeLibraryState = _CpqTapeLibraryState_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 3, 1, 1, 13),
    _CpqTapeLibraryState_Type()
)
cpqTapeLibraryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqTapeLibraryState.setStatus("mandatory")


class _CpqTapeLibraryTemperature_Type(Integer32):
    """Custom type cpqTapeLibraryTemperature based on Integer32"""
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
        *(("maxTempExceeded", 5),
          ("notSupported", 2),
          ("ok", 3),
          ("other", 1),
          ("safeTempExceeded", 4))
    )


_CpqTapeLibraryTemperature_Type.__name__ = "Integer32"
_CpqTapeLibraryTemperature_Object = MibTableColumn
cpqTapeLibraryTemperature = _CpqTapeLibraryTemperature_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 3, 1, 1, 14),
    _CpqTapeLibraryTemperature_Type()
)
cpqTapeLibraryTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqTapeLibraryTemperature.setStatus("mandatory")


class _CpqTapeLibraryRedundancy_Type(Integer32):
    """Custom type cpqTapeLibraryRedundancy based on Integer32"""
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
        *(("active", 5),
          ("capable", 3),
          ("notCapable", 4),
          ("notSupported", 2),
          ("other", 1))
    )


_CpqTapeLibraryRedundancy_Type.__name__ = "Integer32"
_CpqTapeLibraryRedundancy_Object = MibTableColumn
cpqTapeLibraryRedundancy = _CpqTapeLibraryRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 3, 1, 1, 15),
    _CpqTapeLibraryRedundancy_Type()
)
cpqTapeLibraryRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqTapeLibraryRedundancy.setStatus("mandatory")


class _CpqTapeLibraryHotSwap_Type(Integer32):
    """Custom type cpqTapeLibraryHotSwap based on Integer32"""
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
        *(("capable", 3),
          ("notCapable", 4),
          ("notSupported", 2),
          ("other", 1))
    )


_CpqTapeLibraryHotSwap_Type.__name__ = "Integer32"
_CpqTapeLibraryHotSwap_Object = MibTableColumn
cpqTapeLibraryHotSwap = _CpqTapeLibraryHotSwap_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 3, 1, 1, 16),
    _CpqTapeLibraryHotSwap_Type()
)
cpqTapeLibraryHotSwap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqTapeLibraryHotSwap.setStatus("mandatory")


class _CpqTapeLibraryFwRev_Type(DisplayString):
    """Custom type cpqTapeLibraryFwRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CpqTapeLibraryFwRev_Type.__name__ = "DisplayString"
_CpqTapeLibraryFwRev_Object = MibTableColumn
cpqTapeLibraryFwRev = _CpqTapeLibraryFwRev_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 3, 1, 1, 17),
    _CpqTapeLibraryFwRev_Type()
)
cpqTapeLibraryFwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqTapeLibraryFwRev.setStatus("mandatory")


class _CpqTapeLibraryTapeList_Type(OctetString):
    """Custom type cpqTapeLibraryTapeList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 560),
    )


_CpqTapeLibraryTapeList_Type.__name__ = "OctetString"
_CpqTapeLibraryTapeList_Object = MibTableColumn
cpqTapeLibraryTapeList = _CpqTapeLibraryTapeList_Object(
    (1, 3, 6, 1, 4, 1, 232, 5, 4, 3, 1, 1, 18),
    _CpqTapeLibraryTapeList_Type()
)
cpqTapeLibraryTapeList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqTapeLibraryTapeList.setStatus("mandatory")
_CpqSbScsiBus_ObjectIdentity = ObjectIdentity
cpqSbScsiBus = _CpqSbScsiBus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 7)
)
_CpqSbScsiMibRev_ObjectIdentity = ObjectIdentity
cpqSbScsiMibRev = _CpqSbScsiMibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 7, 1)
)


class _CpqSbMibRevMajor_Type(Integer32):
    """Custom type cpqSbMibRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CpqSbMibRevMajor_Type.__name__ = "Integer32"
_CpqSbMibRevMajor_Object = MibScalar
cpqSbMibRevMajor = _CpqSbMibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 232, 7, 1, 1),
    _CpqSbMibRevMajor_Type()
)
cpqSbMibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSbMibRevMajor.setStatus("deprecated")


class _CpqSbMibRevMinor_Type(Integer32):
    """Custom type cpqSbMibRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSbMibRevMinor_Type.__name__ = "Integer32"
_CpqSbMibRevMinor_Object = MibScalar
cpqSbMibRevMinor = _CpqSbMibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 232, 7, 1, 2),
    _CpqSbMibRevMinor_Type()
)
cpqSbMibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSbMibRevMinor.setStatus("deprecated")
_CpqSbDevice_ObjectIdentity = ObjectIdentity
cpqSbDevice = _CpqSbDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 7, 2)
)
_CpqSbDeviceTable_Object = MibTable
cpqSbDeviceTable = _CpqSbDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 7, 2, 2)
)
if mibBuilder.loadTexts:
    cpqSbDeviceTable.setStatus("deprecated")
_CpqSbDeviceEntry_Object = MibTableRow
cpqSbDeviceEntry = _CpqSbDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 7, 2, 2, 1)
)
cpqSbDeviceEntry.setIndexNames(
    (0, "CPQSCSI-MIB", "cpqSbDevCntlrIndex"),
    (0, "CPQSCSI-MIB", "cpqSbDevBusIndex"),
    (0, "CPQSCSI-MIB", "cpqSbDevScsiIdIndex"),
)
if mibBuilder.loadTexts:
    cpqSbDeviceEntry.setStatus("deprecated")


class _CpqSbDevCntlrIndex_Type(Integer32):
    """Custom type cpqSbDevCntlrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSbDevCntlrIndex_Type.__name__ = "Integer32"
_CpqSbDevCntlrIndex_Object = MibTableColumn
cpqSbDevCntlrIndex = _CpqSbDevCntlrIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 7, 2, 2, 1, 1),
    _CpqSbDevCntlrIndex_Type()
)
cpqSbDevCntlrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSbDevCntlrIndex.setStatus("deprecated")


class _CpqSbDevBusIndex_Type(Integer32):
    """Custom type cpqSbDevBusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSbDevBusIndex_Type.__name__ = "Integer32"
_CpqSbDevBusIndex_Object = MibTableColumn
cpqSbDevBusIndex = _CpqSbDevBusIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 7, 2, 2, 1, 2),
    _CpqSbDevBusIndex_Type()
)
cpqSbDevBusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSbDevBusIndex.setStatus("deprecated")


class _CpqSbDevScsiIdIndex_Type(Integer32):
    """Custom type cpqSbDevScsiIdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSbDevScsiIdIndex_Type.__name__ = "Integer32"
_CpqSbDevScsiIdIndex_Object = MibTableColumn
cpqSbDevScsiIdIndex = _CpqSbDevScsiIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 7, 2, 2, 1, 3),
    _CpqSbDevScsiIdIndex_Type()
)
cpqSbDevScsiIdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSbDevScsiIdIndex.setStatus("deprecated")


class _CpqSbDevType_Type(Integer32):
    """Custom type cpqSbDevType based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("cd-rom", 7),
          ("commDev", 11),
          ("disk", 2),
          ("jukeBox", 10),
          ("optical", 9),
          ("other", 1),
          ("printer", 4),
          ("processor", 5),
          ("scanner", 8),
          ("tape", 3),
          ("wormDrive", 6))
    )


_CpqSbDevType_Type.__name__ = "Integer32"
_CpqSbDevType_Object = MibTableColumn
cpqSbDevType = _CpqSbDevType_Object(
    (1, 3, 6, 1, 4, 1, 232, 7, 2, 2, 1, 4),
    _CpqSbDevType_Type()
)
cpqSbDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSbDevType.setStatus("deprecated")


class _CpqSbDevModel_Type(DisplayString):
    """Custom type cpqSbDevModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_CpqSbDevModel_Type.__name__ = "DisplayString"
_CpqSbDevModel_Object = MibTableColumn
cpqSbDevModel = _CpqSbDevModel_Object(
    (1, 3, 6, 1, 4, 1, 232, 7, 2, 2, 1, 5),
    _CpqSbDevModel_Type()
)
cpqSbDevModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSbDevModel.setStatus("deprecated")


class _CpqSbDevFWRev_Type(DisplayString):
    """Custom type cpqSbDevFWRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CpqSbDevFWRev_Type.__name__ = "DisplayString"
_CpqSbDevFWRev_Object = MibTableColumn
cpqSbDevFWRev = _CpqSbDevFWRev_Object(
    (1, 3, 6, 1, 4, 1, 232, 7, 2, 2, 1, 6),
    _CpqSbDevFWRev_Type()
)
cpqSbDevFWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSbDevFWRev.setStatus("deprecated")


class _CpqSbDevVendor_Type(DisplayString):
    """Custom type cpqSbDevVendor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_CpqSbDevVendor_Type.__name__ = "DisplayString"
_CpqSbDevVendor_Object = MibTableColumn
cpqSbDevVendor = _CpqSbDevVendor_Object(
    (1, 3, 6, 1, 4, 1, 232, 7, 2, 2, 1, 7),
    _CpqSbDevVendor_Type()
)
cpqSbDevVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSbDevVendor.setStatus("deprecated")
_CpqSbDevParityErrs_Type = Counter32
_CpqSbDevParityErrs_Object = MibTableColumn
cpqSbDevParityErrs = _CpqSbDevParityErrs_Object(
    (1, 3, 6, 1, 4, 1, 232, 7, 2, 2, 1, 8),
    _CpqSbDevParityErrs_Type()
)
cpqSbDevParityErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSbDevParityErrs.setStatus("deprecated")
_CpqSbDevPhaseErrs_Type = Counter32
_CpqSbDevPhaseErrs_Object = MibTableColumn
cpqSbDevPhaseErrs = _CpqSbDevPhaseErrs_Object(
    (1, 3, 6, 1, 4, 1, 232, 7, 2, 2, 1, 9),
    _CpqSbDevPhaseErrs_Type()
)
cpqSbDevPhaseErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSbDevPhaseErrs.setStatus("deprecated")
_CpqSbDevSelectTimeouts_Type = Counter32
_CpqSbDevSelectTimeouts_Object = MibTableColumn
cpqSbDevSelectTimeouts = _CpqSbDevSelectTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 232, 7, 2, 2, 1, 10),
    _CpqSbDevSelectTimeouts_Type()
)
cpqSbDevSelectTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSbDevSelectTimeouts.setStatus("deprecated")
_CpqSbDevMsgRejects_Type = Counter32
_CpqSbDevMsgRejects_Object = MibTableColumn
cpqSbDevMsgRejects = _CpqSbDevMsgRejects_Object(
    (1, 3, 6, 1, 4, 1, 232, 7, 2, 2, 1, 11),
    _CpqSbDevMsgRejects_Type()
)
cpqSbDevMsgRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSbDevMsgRejects.setStatus("deprecated")


class _CpqSbDevNegPeriod_Type(Integer32):
    """Custom type cpqSbDevNegPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpqSbDevNegPeriod_Type.__name__ = "Integer32"
_CpqSbDevNegPeriod_Object = MibTableColumn
cpqSbDevNegPeriod = _CpqSbDevNegPeriod_Object(
    (1, 3, 6, 1, 4, 1, 232, 7, 2, 2, 1, 12),
    _CpqSbDevNegPeriod_Type()
)
cpqSbDevNegPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSbDevNegPeriod.setStatus("deprecated")


class _CpqSbDevLocation_Type(Integer32):
    """Custom type cpqSbDevLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("proliant", 2))
    )


_CpqSbDevLocation_Type.__name__ = "Integer32"
_CpqSbDevLocation_Object = MibTableColumn
cpqSbDevLocation = _CpqSbDevLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 7, 2, 2, 1, 13),
    _CpqSbDevLocation_Type()
)
cpqSbDevLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSbDevLocation.setStatus("deprecated")

# Managed Objects groups


# Notification objects

cpqScsi2CntlrStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 5001)
)
cpqScsi2CntlrStatusChange.setObjects(
    ("CPQSCSI-MIB", "cpqScsiCntlrStatus")
)
if mibBuilder.loadTexts:
    cpqScsi2CntlrStatusChange.setStatus(
        ""
    )

cpqScsi2LogDrvStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 5002)
)
cpqScsi2LogDrvStatusChange.setObjects(
    ("CPQSCSI-MIB", "cpqScsiLogDrvStatus")
)
if mibBuilder.loadTexts:
    cpqScsi2LogDrvStatusChange.setStatus(
        ""
    )

cpqScsi2PhyDrvStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 5003)
)
cpqScsi2PhyDrvStatusChange.setObjects(
    ("CPQSCSI-MIB", "cpqScsiPhyDrvStatus")
)
if mibBuilder.loadTexts:
    cpqScsi2PhyDrvStatusChange.setStatus(
        ""
    )

cpqTapePhyDrvStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 5004)
)
cpqTapePhyDrvStatusChange.setObjects(
    ("CPQSCSI-MIB", "cpqTapePhyDrvCondition")
)
if mibBuilder.loadTexts:
    cpqTapePhyDrvStatusChange.setStatus(
        ""
    )

cpqScsi3CntlrStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 5005)
)
cpqScsi3CntlrStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSCSI-MIB", "cpqScsiCntlrStatus"))
)
if mibBuilder.loadTexts:
    cpqScsi3CntlrStatusChange.setStatus(
        ""
    )

cpqScsi3PhyDrvStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 5006)
)
cpqScsi3PhyDrvStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSCSI-MIB", "cpqScsiPhyDrvStatus"))
)
if mibBuilder.loadTexts:
    cpqScsi3PhyDrvStatusChange.setStatus(
        ""
    )

cpqTape3PhyDrvStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 5007)
)
cpqTape3PhyDrvStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSCSI-MIB", "cpqTapePhyDrvCondition"))
)
if mibBuilder.loadTexts:
    cpqTape3PhyDrvStatusChange.setStatus(
        ""
    )

cpqTape3PhyDrvCleaningRequired = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 5008)
)
cpqTape3PhyDrvCleaningRequired.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSCSI-MIB", "cpqTapePhyDrvCondition"))
)
if mibBuilder.loadTexts:
    cpqTape3PhyDrvCleaningRequired.setStatus(
        ""
    )

cpqTape3PhyDrvCleanTapeReplace = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 5009)
)
cpqTape3PhyDrvCleanTapeReplace.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSCSI-MIB", "cpqTapePhyDrvCondition"))
)
if mibBuilder.loadTexts:
    cpqTape3PhyDrvCleanTapeReplace.setStatus(
        ""
    )

cpqTape3LibraryFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 5010)
)
cpqTape3LibraryFailed.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSCSI-MIB", "cpqTapeLibrarySerialNumber"))
)
if mibBuilder.loadTexts:
    cpqTape3LibraryFailed.setStatus(
        ""
    )

cpqTape3LibraryOkay = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 5011)
)
cpqTape3LibraryOkay.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSCSI-MIB", "cpqTapeLibrarySerialNumber"))
)
if mibBuilder.loadTexts:
    cpqTape3LibraryOkay.setStatus(
        ""
    )

cpqTape3LibraryDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 5012)
)
cpqTape3LibraryDegraded.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSCSI-MIB", "cpqTapeLibrarySerialNumber"))
)
if mibBuilder.loadTexts:
    cpqTape3LibraryDegraded.setStatus(
        ""
    )

cpqTape3LibraryDoorOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 5013)
)
cpqTape3LibraryDoorOpen.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSCSI-MIB", "cpqTapeLibrarySerialNumber"))
)
if mibBuilder.loadTexts:
    cpqTape3LibraryDoorOpen.setStatus(
        ""
    )

cpqTape3LibraryDoorClosed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 5014)
)
cpqTape3LibraryDoorClosed.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSCSI-MIB", "cpqTapeLibrarySerialNumber"))
)
if mibBuilder.loadTexts:
    cpqTape3LibraryDoorClosed.setStatus(
        ""
    )

cpqScsiCdLibraryStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 5015)
)
cpqScsiCdLibraryStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSCSI-MIB", "cpqCdLibraryCntlrIndex"),
        ("CPQSCSI-MIB", "cpqCdLibraryBusIndex"),
        ("CPQSCSI-MIB", "cpqCdLibraryScsiIdIndex"),
        ("CPQSCSI-MIB", "cpqCdLibraryStatus"))
)
if mibBuilder.loadTexts:
    cpqScsiCdLibraryStatusChange.setStatus(
        ""
    )

cpqTape4PhyDrvStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 5016)
)
cpqTape4PhyDrvStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSCSI-MIB", "cpqTapePhyDrvCntlrIndex"),
        ("CPQSCSI-MIB", "cpqTapePhyDrvBusIndex"),
        ("CPQSCSI-MIB", "cpqTapePhyDrvScsiIdIndex"),
        ("CPQSCSI-MIB", "cpqTapePhyDrvStatus"))
)
if mibBuilder.loadTexts:
    cpqTape4PhyDrvStatusChange.setStatus(
        ""
    )

cpqScsi4PhyDrvStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 5017)
)
cpqScsi4PhyDrvStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSCSI-MIB", "cpqScsiPhyDrvStatus"),
        ("CPQSCSI-MIB", "cpqScsiPhyDrvCntlrIndex"),
        ("CPQSCSI-MIB", "cpqScsiPhyDrvBusIndex"),
        ("CPQSCSI-MIB", "cpqScsiPhyDrvIndex"),
        ("CPQSCSI-MIB", "cpqScsiPhyDrvVendor"),
        ("CPQSCSI-MIB", "cpqScsiPhyDrvModel"),
        ("CPQSCSI-MIB", "cpqScsiPhyDrvFWRev"),
        ("CPQSCSI-MIB", "cpqScsiPhyDrvSerialNum"))
)
if mibBuilder.loadTexts:
    cpqScsi4PhyDrvStatusChange.setStatus(
        ""
    )

cpqTapeLibraryStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 5018)
)
cpqTapeLibraryStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSCSI-MIB", "cpqTapeLibraryCntlrIndex"),
        ("CPQSCSI-MIB", "cpqTapeLibraryBusIndex"),
        ("CPQSCSI-MIB", "cpqTapeLibraryScsiIdIndex"),
        ("CPQSCSI-MIB", "cpqTapeLibraryLunIndex"),
        ("CPQSCSI-MIB", "cpqTapeLibraryName"),
        ("CPQSCSI-MIB", "cpqTapeLibraryFwRev"),
        ("CPQSCSI-MIB", "cpqTapeLibrarySerialNumber"),
        ("CPQSCSI-MIB", "cpqTapeLibraryState"))
)
if mibBuilder.loadTexts:
    cpqTapeLibraryStatusChange.setStatus(
        ""
    )

cpqTape5PhyDrvStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 5019)
)
cpqTape5PhyDrvStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSCSI-MIB", "cpqTapePhyDrvCntlrIndex"),
        ("CPQSCSI-MIB", "cpqTapePhyDrvBusIndex"),
        ("CPQSCSI-MIB", "cpqTapePhyDrvScsiIdIndex"),
        ("CPQSCSI-MIB", "cpqTapePhyDrvLunIndex"),
        ("CPQSCSI-MIB", "cpqTapePhyDrvName"),
        ("CPQSCSI-MIB", "cpqTapePhyDrvFwRev"),
        ("CPQSCSI-MIB", "cpqTapePhyDrvSerialNumber"),
        ("CPQSCSI-MIB", "cpqTapePhyDrvStatus"))
)
if mibBuilder.loadTexts:
    cpqTape5PhyDrvStatusChange.setStatus(
        ""
    )

cpqScsi5PhyDrvStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 5020)
)
cpqScsi5PhyDrvStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSCSI-MIB", "cpqScsiPhyDrvStatus"),
        ("CPQSCSI-MIB", "cpqScsiPhyDrvCntlrIndex"),
        ("CPQSCSI-MIB", "cpqScsiPhyDrvBusIndex"),
        ("CPQSCSI-MIB", "cpqScsiPhyDrvIndex"),
        ("CPQSCSI-MIB", "cpqScsiPhyDrvVendor"),
        ("CPQSCSI-MIB", "cpqScsiPhyDrvModel"),
        ("CPQSCSI-MIB", "cpqScsiPhyDrvFWRev"),
        ("CPQSCSI-MIB", "cpqScsiPhyDrvSerialNum"),
        ("CPQSCSI-MIB", "cpqScsiPhyDrvOsName"))
)
if mibBuilder.loadTexts:
    cpqScsi5PhyDrvStatusChange.setStatus(
        ""
    )

cpqScsi3LogDrvStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 5021)
)
cpqScsi3LogDrvStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSCSI-MIB", "cpqScsiLogDrvStatus"),
        ("CPQSCSI-MIB", "cpqScsiLogDrvCntlrIndex"),
        ("CPQSCSI-MIB", "cpqScsiLogDrvBusIndex"),
        ("CPQSCSI-MIB", "cpqScsiLogDrvIndex"),
        ("CPQSCSI-MIB", "cpqScsiLogDrvOsName"))
)
if mibBuilder.loadTexts:
    cpqScsi3LogDrvStatusChange.setStatus(
        ""
    )

cpqScsiCntlrStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 5, 0, 1)
)
cpqScsiCntlrStatusChange.setObjects(
    ("CPQSCSI-MIB", "cpqScsiCntlrStatus")
)
if mibBuilder.loadTexts:
    cpqScsiCntlrStatusChange.setStatus(
        ""
    )

cpqScsiLogDrvStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 5, 0, 2)
)
cpqScsiLogDrvStatusChange.setObjects(
    ("CPQSCSI-MIB", "cpqScsiLogDrvStatus")
)
if mibBuilder.loadTexts:
    cpqScsiLogDrvStatusChange.setStatus(
        ""
    )

cpqScsiPhyDrvStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 5, 0, 3)
)
cpqScsiPhyDrvStatusChange.setObjects(
    ("CPQSCSI-MIB", "cpqScsiPhyDrvStatus")
)
if mibBuilder.loadTexts:
    cpqScsiPhyDrvStatusChange.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPQSCSI-MIB",
    **{"cpqScsi2CntlrStatusChange": cpqScsi2CntlrStatusChange,
       "cpqScsi2LogDrvStatusChange": cpqScsi2LogDrvStatusChange,
       "cpqScsi2PhyDrvStatusChange": cpqScsi2PhyDrvStatusChange,
       "cpqTapePhyDrvStatusChange": cpqTapePhyDrvStatusChange,
       "cpqScsi3CntlrStatusChange": cpqScsi3CntlrStatusChange,
       "cpqScsi3PhyDrvStatusChange": cpqScsi3PhyDrvStatusChange,
       "cpqTape3PhyDrvStatusChange": cpqTape3PhyDrvStatusChange,
       "cpqTape3PhyDrvCleaningRequired": cpqTape3PhyDrvCleaningRequired,
       "cpqTape3PhyDrvCleanTapeReplace": cpqTape3PhyDrvCleanTapeReplace,
       "cpqTape3LibraryFailed": cpqTape3LibraryFailed,
       "cpqTape3LibraryOkay": cpqTape3LibraryOkay,
       "cpqTape3LibraryDegraded": cpqTape3LibraryDegraded,
       "cpqTape3LibraryDoorOpen": cpqTape3LibraryDoorOpen,
       "cpqTape3LibraryDoorClosed": cpqTape3LibraryDoorClosed,
       "cpqScsiCdLibraryStatusChange": cpqScsiCdLibraryStatusChange,
       "cpqTape4PhyDrvStatusChange": cpqTape4PhyDrvStatusChange,
       "cpqScsi4PhyDrvStatusChange": cpqScsi4PhyDrvStatusChange,
       "cpqTapeLibraryStatusChange": cpqTapeLibraryStatusChange,
       "cpqTape5PhyDrvStatusChange": cpqTape5PhyDrvStatusChange,
       "cpqScsi5PhyDrvStatusChange": cpqScsi5PhyDrvStatusChange,
       "cpqScsi3LogDrvStatusChange": cpqScsi3LogDrvStatusChange,
       "cpqScsi": cpqScsi,
       "cpqScsiCntlrStatusChange": cpqScsiCntlrStatusChange,
       "cpqScsiLogDrvStatusChange": cpqScsiLogDrvStatusChange,
       "cpqScsiPhyDrvStatusChange": cpqScsiPhyDrvStatusChange,
       "cpqScsiMibRev": cpqScsiMibRev,
       "cpqScsiMibRevMajor": cpqScsiMibRevMajor,
       "cpqScsiMibRevMinor": cpqScsiMibRevMinor,
       "cpqScsiMibCondition": cpqScsiMibCondition,
       "cpqScsiComponent": cpqScsiComponent,
       "cpqScsiInterface": cpqScsiInterface,
       "cpqScsiOsNetWare": cpqScsiOsNetWare,
       "cpqScsiNw3xDriverName": cpqScsiNw3xDriverName,
       "cpqScsiNw3xDriverVers": cpqScsiNw3xDriverVers,
       "cpqScsiNw3xDriverPollType": cpqScsiNw3xDriverPollType,
       "cpqScsiNw3xDriverPollTime": cpqScsiNw3xDriverPollTime,
       "cpqScsiNw3xCntlrInfoTable": cpqScsiNw3xCntlrInfoTable,
       "cpqScsiNw3xCntlrInfoEntry": cpqScsiNw3xCntlrInfoEntry,
       "cpqScsiNw3xCntlrIndex": cpqScsiNw3xCntlrIndex,
       "cpqScsiNw3xBusIndex": cpqScsiNw3xBusIndex,
       "cpqScsiNw3xXptDesc": cpqScsiNw3xXptDesc,
       "cpqScsiNw3xXptVers": cpqScsiNw3xXptVers,
       "cpqScsiNw3xSimDesc": cpqScsiNw3xSimDesc,
       "cpqScsiNw3xSimVers": cpqScsiNw3xSimVers,
       "cpqScsiNw3xHbaDesc": cpqScsiNw3xHbaDesc,
       "cpqScsiLogDrvStatTable": cpqScsiLogDrvStatTable,
       "cpqScsiLogDrvStatEntry": cpqScsiLogDrvStatEntry,
       "cpqScsiNw3xStatCntlrIndex": cpqScsiNw3xStatCntlrIndex,
       "cpqScsiNw3xStatBusIndex": cpqScsiNw3xStatBusIndex,
       "cpqScsiNw3xStatLogDrvIndex": cpqScsiNw3xStatLogDrvIndex,
       "cpqScsiNw3xTotalReads": cpqScsiNw3xTotalReads,
       "cpqScsiNw3xTotalWrites": cpqScsiNw3xTotalWrites,
       "cpqScsiNw3xCorrReads": cpqScsiNw3xCorrReads,
       "cpqScsiNw3xCorrWrites": cpqScsiNw3xCorrWrites,
       "cpqScsiNw3xFatalReads": cpqScsiNw3xFatalReads,
       "cpqScsiNw3xFatalWrites": cpqScsiNw3xFatalWrites,
       "cpqScsiVolMapTable": cpqScsiVolMapTable,
       "cpqScsiVolMapEntry": cpqScsiVolMapEntry,
       "cpqScsiNw3xVolCntlrIndex": cpqScsiNw3xVolCntlrIndex,
       "cpqScsiNw3xVolBusIndex": cpqScsiNw3xVolBusIndex,
       "cpqScsiNw3xVolLogDrvIndex": cpqScsiNw3xVolLogDrvIndex,
       "cpqScsiNw3xVolMap": cpqScsiNw3xVolMap,
       "cpqScsiOsCommon": cpqScsiOsCommon,
       "cpqScsiOsCommonPollFreq": cpqScsiOsCommonPollFreq,
       "cpqScsiOsCommonModuleTable": cpqScsiOsCommonModuleTable,
       "cpqScsiOsCommonModuleEntry": cpqScsiOsCommonModuleEntry,
       "cpqScsiOsCommonModuleIndex": cpqScsiOsCommonModuleIndex,
       "cpqScsiOsCommonModuleName": cpqScsiOsCommonModuleName,
       "cpqScsiOsCommonModuleVersion": cpqScsiOsCommonModuleVersion,
       "cpqScsiOsCommonModuleDate": cpqScsiOsCommonModuleDate,
       "cpqScsiOsCommonModulePurpose": cpqScsiOsCommonModulePurpose,
       "cpqScsiCntlr": cpqScsiCntlr,
       "cpqScsiCntlrTable": cpqScsiCntlrTable,
       "cpqScsiCntlrEntry": cpqScsiCntlrEntry,
       "cpqScsiCntlrIndex": cpqScsiCntlrIndex,
       "cpqScsiCntlrBusIndex": cpqScsiCntlrBusIndex,
       "cpqScsiCntlrModel": cpqScsiCntlrModel,
       "cpqScsiCntlrFWVers": cpqScsiCntlrFWVers,
       "cpqScsiCntlrSWVers": cpqScsiCntlrSWVers,
       "cpqScsiCntlrSlot": cpqScsiCntlrSlot,
       "cpqScsiCntlrStatus": cpqScsiCntlrStatus,
       "cpqScsiCntlrHardResets": cpqScsiCntlrHardResets,
       "cpqScsiCntlrSoftResets": cpqScsiCntlrSoftResets,
       "cpqScsiCntlrTimeouts": cpqScsiCntlrTimeouts,
       "cpqScsiCntlrBaseIOAddr": cpqScsiCntlrBaseIOAddr,
       "cpqScsiCntlrCondition": cpqScsiCntlrCondition,
       "cpqScsiCntlrSerialNum": cpqScsiCntlrSerialNum,
       "cpqScsiCntlrBusWidth": cpqScsiCntlrBusWidth,
       "cpqScsiCntlrModelExtended": cpqScsiCntlrModelExtended,
       "cpqScsiCntlrHwLocation": cpqScsiCntlrHwLocation,
       "cpqScsiLogDrv": cpqScsiLogDrv,
       "cpqScsiLogDrvTable": cpqScsiLogDrvTable,
       "cpqScsiLogDrvEntry": cpqScsiLogDrvEntry,
       "cpqScsiLogDrvCntlrIndex": cpqScsiLogDrvCntlrIndex,
       "cpqScsiLogDrvBusIndex": cpqScsiLogDrvBusIndex,
       "cpqScsiLogDrvIndex": cpqScsiLogDrvIndex,
       "cpqScsiLogDrvFaultTol": cpqScsiLogDrvFaultTol,
       "cpqScsiLogDrvStatus": cpqScsiLogDrvStatus,
       "cpqScsiLogDrvSize": cpqScsiLogDrvSize,
       "cpqScsiLogDrvPhyDrvIDs": cpqScsiLogDrvPhyDrvIDs,
       "cpqScsiLogDrvCondition": cpqScsiLogDrvCondition,
       "cpqScsiLogDrvStripeSize": cpqScsiLogDrvStripeSize,
       "cpqScsiLogDrvAvailSpares": cpqScsiLogDrvAvailSpares,
       "cpqScsiLogDrvPercentRebuild": cpqScsiLogDrvPercentRebuild,
       "cpqScsiLogDrvOsName": cpqScsiLogDrvOsName,
       "cpqScsiPhyDrv": cpqScsiPhyDrv,
       "cpqScsiPhyDrvTable": cpqScsiPhyDrvTable,
       "cpqScsiPhyDrvEntry": cpqScsiPhyDrvEntry,
       "cpqScsiPhyDrvCntlrIndex": cpqScsiPhyDrvCntlrIndex,
       "cpqScsiPhyDrvBusIndex": cpqScsiPhyDrvBusIndex,
       "cpqScsiPhyDrvIndex": cpqScsiPhyDrvIndex,
       "cpqScsiPhyDrvModel": cpqScsiPhyDrvModel,
       "cpqScsiPhyDrvFWRev": cpqScsiPhyDrvFWRev,
       "cpqScsiPhyDrvVendor": cpqScsiPhyDrvVendor,
       "cpqScsiPhyDrvSize": cpqScsiPhyDrvSize,
       "cpqScsiPhyDrvScsiID": cpqScsiPhyDrvScsiID,
       "cpqScsiPhyDrvStatus": cpqScsiPhyDrvStatus,
       "cpqScsiPhyDrvServiceHours": cpqScsiPhyDrvServiceHours,
       "cpqScsiPhyDrvHighReadSectors": cpqScsiPhyDrvHighReadSectors,
       "cpqScsiPhyDrvLowReadSectors": cpqScsiPhyDrvLowReadSectors,
       "cpqScsiPhyDrvHighWriteSectors": cpqScsiPhyDrvHighWriteSectors,
       "cpqScsiPhyDrvLowWriteSectors": cpqScsiPhyDrvLowWriteSectors,
       "cpqScsiPhyDrvHardReadErrs": cpqScsiPhyDrvHardReadErrs,
       "cpqScsiPhyDrvHardWriteErrs": cpqScsiPhyDrvHardWriteErrs,
       "cpqScsiPhyDrvEccCorrReads": cpqScsiPhyDrvEccCorrReads,
       "cpqScsiPhyDrvRecvReadErrs": cpqScsiPhyDrvRecvReadErrs,
       "cpqScsiPhyDrvRecvWriteErrs": cpqScsiPhyDrvRecvWriteErrs,
       "cpqScsiPhyDrvSeekErrs": cpqScsiPhyDrvSeekErrs,
       "cpqScsiPhyDrvSpinupTime": cpqScsiPhyDrvSpinupTime,
       "cpqScsiPhyDrvUsedReallocs": cpqScsiPhyDrvUsedReallocs,
       "cpqScsiPhyDrvTimeouts": cpqScsiPhyDrvTimeouts,
       "cpqScsiPhyDrvPostErrs": cpqScsiPhyDrvPostErrs,
       "cpqScsiPhyDrvPostErrCode": cpqScsiPhyDrvPostErrCode,
       "cpqScsiPhyDrvCondition": cpqScsiPhyDrvCondition,
       "cpqScsiPhyDrvFuncTest1": cpqScsiPhyDrvFuncTest1,
       "cpqScsiPhyDrvFuncTest2": cpqScsiPhyDrvFuncTest2,
       "cpqScsiPhyDrvStatsPreserved": cpqScsiPhyDrvStatsPreserved,
       "cpqScsiPhyDrvSerialNum": cpqScsiPhyDrvSerialNum,
       "cpqScsiPhyDrvLocation": cpqScsiPhyDrvLocation,
       "cpqScsiPhyDrvParent": cpqScsiPhyDrvParent,
       "cpqScsiPhyDrvSectorSize": cpqScsiPhyDrvSectorSize,
       "cpqScsiPhyDrvHotPlug": cpqScsiPhyDrvHotPlug,
       "cpqScsiPhyDrvPlacement": cpqScsiPhyDrvPlacement,
       "cpqScsiPhyDrvPreFailMonitoring": cpqScsiPhyDrvPreFailMonitoring,
       "cpqScsiPhyDrvOsName": cpqScsiPhyDrvOsName,
       "cpqScsiPhyDrvRotationalSpeed": cpqScsiPhyDrvRotationalSpeed,
       "cpqScsiPhyDrvMemberLogDrv": cpqScsiPhyDrvMemberLogDrv,
       "cpqScsiTarget": cpqScsiTarget,
       "cpqScsiTargetTable": cpqScsiTargetTable,
       "cpqScsiTargetEntry": cpqScsiTargetEntry,
       "cpqScsiTargetCntlrIndex": cpqScsiTargetCntlrIndex,
       "cpqScsiTargetBusIndex": cpqScsiTargetBusIndex,
       "cpqScsiTargetScsiIdIndex": cpqScsiTargetScsiIdIndex,
       "cpqScsiTargetType": cpqScsiTargetType,
       "cpqScsiTargetModel": cpqScsiTargetModel,
       "cpqScsiTargetFWRev": cpqScsiTargetFWRev,
       "cpqScsiTargetVendor": cpqScsiTargetVendor,
       "cpqScsiTargetParityErrs": cpqScsiTargetParityErrs,
       "cpqScsiTargetPhaseErrs": cpqScsiTargetPhaseErrs,
       "cpqScsiTargetSelectTimeouts": cpqScsiTargetSelectTimeouts,
       "cpqScsiTargetMsgRejects": cpqScsiTargetMsgRejects,
       "cpqScsiTargetNegPeriod": cpqScsiTargetNegPeriod,
       "cpqScsiTargetLocation": cpqScsiTargetLocation,
       "cpqScsiTargetNegSpeed": cpqScsiTargetNegSpeed,
       "cpqScsiTargetPhysWidth": cpqScsiTargetPhysWidth,
       "cpqScsiTargetNegWidth": cpqScsiTargetNegWidth,
       "cpqScsiTargetTypeExtended": cpqScsiTargetTypeExtended,
       "cpqScsiTargetCurrentSpeed": cpqScsiTargetCurrentSpeed,
       "cpqScsiCd": cpqScsiCd,
       "cpqScsiCdDrvTable": cpqScsiCdDrvTable,
       "cpqScsiCdDrvEntry": cpqScsiCdDrvEntry,
       "cpqScsiCdDrvCntlrIndex": cpqScsiCdDrvCntlrIndex,
       "cpqScsiCdDrvBusIndex": cpqScsiCdDrvBusIndex,
       "cpqScsiCdDrvScsiIdIndex": cpqScsiCdDrvScsiIdIndex,
       "cpqScsiCdDrvLunIndex": cpqScsiCdDrvLunIndex,
       "cpqScsiCdDrvModel": cpqScsiCdDrvModel,
       "cpqScsiCdDrvVendor": cpqScsiCdDrvVendor,
       "cpqScsiCdDrvFwRev": cpqScsiCdDrvFwRev,
       "cpqCdLibraryTable": cpqCdLibraryTable,
       "cpqCdLibraryEntry": cpqCdLibraryEntry,
       "cpqCdLibraryCntlrIndex": cpqCdLibraryCntlrIndex,
       "cpqCdLibraryBusIndex": cpqCdLibraryBusIndex,
       "cpqCdLibraryScsiIdIndex": cpqCdLibraryScsiIdIndex,
       "cpqCdLibraryLunIndex": cpqCdLibraryLunIndex,
       "cpqCdLibraryCondition": cpqCdLibraryCondition,
       "cpqCdLibraryStatus": cpqCdLibraryStatus,
       "cpqCdLibraryModel": cpqCdLibraryModel,
       "cpqCdLibraryVendor": cpqCdLibraryVendor,
       "cpqCdLibrarySerialNumber": cpqCdLibrarySerialNumber,
       "cpqCdLibraryDriveList": cpqCdLibraryDriveList,
       "cpqCdLibraryFwRev": cpqCdLibraryFwRev,
       "cpqCdLibraryFwSubtype": cpqCdLibraryFwSubtype,
       "cpqScsiTrap": cpqScsiTrap,
       "cpqScsiTrapPkts": cpqScsiTrapPkts,
       "cpqScsiTrapLogMaxSize": cpqScsiTrapLogMaxSize,
       "cpqScsiTrapLogTable": cpqScsiTrapLogTable,
       "cpqScsiTrapLogEntry": cpqScsiTrapLogEntry,
       "cpqScsiTrapLogIndex": cpqScsiTrapLogIndex,
       "cpqScsiTrapType": cpqScsiTrapType,
       "cpqScsiTrapTime": cpqScsiTrapTime,
       "cpqTapeComponent": cpqTapeComponent,
       "cpqTapePhyDrv": cpqTapePhyDrv,
       "cpqTapePhyDrvTable": cpqTapePhyDrvTable,
       "cpqTapePhyDrvEntry": cpqTapePhyDrvEntry,
       "cpqTapePhyDrvCntlrIndex": cpqTapePhyDrvCntlrIndex,
       "cpqTapePhyDrvBusIndex": cpqTapePhyDrvBusIndex,
       "cpqTapePhyDrvScsiIdIndex": cpqTapePhyDrvScsiIdIndex,
       "cpqTapePhyDrvLunIndex": cpqTapePhyDrvLunIndex,
       "cpqTapePhyDrvType": cpqTapePhyDrvType,
       "cpqTapePhyDrvCondition": cpqTapePhyDrvCondition,
       "cpqTapePhyDrvMagSize": cpqTapePhyDrvMagSize,
       "cpqTapePhyDrvSerialNumber": cpqTapePhyDrvSerialNumber,
       "cpqTapePhyDrvCleanReq": cpqTapePhyDrvCleanReq,
       "cpqTapePhyDrvCleanTapeRepl": cpqTapePhyDrvCleanTapeRepl,
       "cpqTapePhyDrvFwSubtype": cpqTapePhyDrvFwSubtype,
       "cpqTapePhyDrvName": cpqTapePhyDrvName,
       "cpqTapePhyDrvCleanTapeCount": cpqTapePhyDrvCleanTapeCount,
       "cpqTapePhyDrvFwRev": cpqTapePhyDrvFwRev,
       "cpqTapePhyDrvStatus": cpqTapePhyDrvStatus,
       "cpqTapePhyDrvHotPlug": cpqTapePhyDrvHotPlug,
       "cpqTapePhyDrvPlacement": cpqTapePhyDrvPlacement,
       "cpqTapePhyDrvLibraryDrive": cpqTapePhyDrvLibraryDrive,
       "cpqTapePhyDrvLoaderName": cpqTapePhyDrvLoaderName,
       "cpqTapePhyDrvLoaderFwRev": cpqTapePhyDrvLoaderFwRev,
       "cpqTapePhyDrvLoaderSerialNum": cpqTapePhyDrvLoaderSerialNum,
       "cpqTapeCounters": cpqTapeCounters,
       "cpqTapeCountersTable": cpqTapeCountersTable,
       "cpqTapeCountersEntry": cpqTapeCountersEntry,
       "cpqTapeCountersCntlrIndex": cpqTapeCountersCntlrIndex,
       "cpqTapeCountersBusIndex": cpqTapeCountersBusIndex,
       "cpqTapeCountersScsiIdIndex": cpqTapeCountersScsiIdIndex,
       "cpqTapeCountersLunIndex": cpqTapeCountersLunIndex,
       "cpqTapeCountersReWrites": cpqTapeCountersReWrites,
       "cpqTapeCountersReReads": cpqTapeCountersReReads,
       "cpqTapeCountersTotalErrors": cpqTapeCountersTotalErrors,
       "cpqTapeCountersTotalUncorrectable": cpqTapeCountersTotalUncorrectable,
       "cpqTapeCountersTotalBytes": cpqTapeCountersTotalBytes,
       "cpqTapeLibrary": cpqTapeLibrary,
       "cpqTapeLibraryTable": cpqTapeLibraryTable,
       "cpqTapeLibraryEntry": cpqTapeLibraryEntry,
       "cpqTapeLibraryCntlrIndex": cpqTapeLibraryCntlrIndex,
       "cpqTapeLibraryBusIndex": cpqTapeLibraryBusIndex,
       "cpqTapeLibraryScsiIdIndex": cpqTapeLibraryScsiIdIndex,
       "cpqTapeLibraryLunIndex": cpqTapeLibraryLunIndex,
       "cpqTapeLibraryCondition": cpqTapeLibraryCondition,
       "cpqTapeLibraryStatus": cpqTapeLibraryStatus,
       "cpqTapeLibraryDoorStatus": cpqTapeLibraryDoorStatus,
       "cpqTapeLibraryStatHours": cpqTapeLibraryStatHours,
       "cpqTapeLibraryStatMoves": cpqTapeLibraryStatMoves,
       "cpqTapeLibraryName": cpqTapeLibraryName,
       "cpqTapeLibrarySerialNumber": cpqTapeLibrarySerialNumber,
       "cpqTapeLibraryDriveList": cpqTapeLibraryDriveList,
       "cpqTapeLibraryState": cpqTapeLibraryState,
       "cpqTapeLibraryTemperature": cpqTapeLibraryTemperature,
       "cpqTapeLibraryRedundancy": cpqTapeLibraryRedundancy,
       "cpqTapeLibraryHotSwap": cpqTapeLibraryHotSwap,
       "cpqTapeLibraryFwRev": cpqTapeLibraryFwRev,
       "cpqTapeLibraryTapeList": cpqTapeLibraryTapeList,
       "cpqSbScsiBus": cpqSbScsiBus,
       "cpqSbScsiMibRev": cpqSbScsiMibRev,
       "cpqSbMibRevMajor": cpqSbMibRevMajor,
       "cpqSbMibRevMinor": cpqSbMibRevMinor,
       "cpqSbDevice": cpqSbDevice,
       "cpqSbDeviceTable": cpqSbDeviceTable,
       "cpqSbDeviceEntry": cpqSbDeviceEntry,
       "cpqSbDevCntlrIndex": cpqSbDevCntlrIndex,
       "cpqSbDevBusIndex": cpqSbDevBusIndex,
       "cpqSbDevScsiIdIndex": cpqSbDevScsiIdIndex,
       "cpqSbDevType": cpqSbDevType,
       "cpqSbDevModel": cpqSbDevModel,
       "cpqSbDevFWRev": cpqSbDevFWRev,
       "cpqSbDevVendor": cpqSbDevVendor,
       "cpqSbDevParityErrs": cpqSbDevParityErrs,
       "cpqSbDevPhaseErrs": cpqSbDevPhaseErrs,
       "cpqSbDevSelectTimeouts": cpqSbDevSelectTimeouts,
       "cpqSbDevMsgRejects": cpqSbDevMsgRejects,
       "cpqSbDevNegPeriod": cpqSbDevNegPeriod,
       "cpqSbDevLocation": cpqSbDevLocation}
)
