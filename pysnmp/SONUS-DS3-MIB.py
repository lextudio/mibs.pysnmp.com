# SNMP MIB module (SONUS-DS3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONUS-DS3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:56:55 2024
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(sonusDs3Index,
 sonusEventClass,
 sonusEventDescription,
 sonusEventLevel,
 sonusPortIndex,
 sonusShelfIndex,
 sonusSlotIndex) = mibBuilder.importSymbols(
    "SONUS-COMMON-MIB",
    "sonusDs3Index",
    "sonusEventClass",
    "sonusEventDescription",
    "sonusEventLevel",
    "sonusPortIndex",
    "sonusShelfIndex",
    "sonusSlotIndex")

(sonusCircuitMIBs,) = mibBuilder.importSymbols(
    "SONUS-SMI",
    "sonusCircuitMIBs")

(SonusAdminAction,
 SonusAdminState,
 SonusName,
 SonusServiceState) = mibBuilder.importSymbols(
    "SONUS-TC",
    "SonusAdminAction",
    "SonusAdminState",
    "SonusName",
    "SonusServiceState")


# MODULE-IDENTITY

sonusDsx3MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonusDsx3MIBObjects_ObjectIdentity = ObjectIdentity
sonusDsx3MIBObjects = _SonusDsx3MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 2, 1)
)
_SonusDsx3Admn_ObjectIdentity = ObjectIdentity
sonusDsx3Admn = _SonusDsx3Admn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 2, 1, 1)
)
_SonusDsx3AdmnNextIndex_ObjectIdentity = ObjectIdentity
sonusDsx3AdmnNextIndex = _SonusDsx3AdmnNextIndex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 2, 1, 1, 1)
)
_SonusDsx3AdmnTable_Object = MibTable
sonusDsx3AdmnTable = _SonusDsx3AdmnTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    sonusDsx3AdmnTable.setStatus("current")
_SonusDsx3AdmnEntry_Object = MibTableRow
sonusDsx3AdmnEntry = _SonusDsx3AdmnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 2, 1, 1, 2, 1)
)
sonusDsx3AdmnEntry.setIndexNames(
    (0, "SONUS-DS3-MIB", "sonusDsx3AdmnShelfIndex"),
    (0, "SONUS-DS3-MIB", "sonusDsx3AdmnSlotIndex"),
    (0, "SONUS-DS3-MIB", "sonusDsx3AdmnPortIndex"),
    (0, "SONUS-DS3-MIB", "sonusDsx3AdmnDs3Index"),
)
if mibBuilder.loadTexts:
    sonusDsx3AdmnEntry.setStatus("current")
_SonusDsx3AdmnRowStatus_Type = RowStatus
_SonusDsx3AdmnRowStatus_Object = MibTableColumn
sonusDsx3AdmnRowStatus = _SonusDsx3AdmnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 2, 1, 1, 2, 1, 1),
    _SonusDsx3AdmnRowStatus_Type()
)
sonusDsx3AdmnRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsx3AdmnRowStatus.setStatus("current")
_SonusDsx3AdmnName_Type = SonusName
_SonusDsx3AdmnName_Object = MibTableColumn
sonusDsx3AdmnName = _SonusDsx3AdmnName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 2, 1, 1, 2, 1, 2),
    _SonusDsx3AdmnName_Type()
)
sonusDsx3AdmnName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsx3AdmnName.setStatus("current")
_SonusDsx3AdmnShelfIndex_Type = Integer32
_SonusDsx3AdmnShelfIndex_Object = MibTableColumn
sonusDsx3AdmnShelfIndex = _SonusDsx3AdmnShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 2, 1, 1, 2, 1, 3),
    _SonusDsx3AdmnShelfIndex_Type()
)
sonusDsx3AdmnShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx3AdmnShelfIndex.setStatus("current")
_SonusDsx3AdmnSlotIndex_Type = Integer32
_SonusDsx3AdmnSlotIndex_Object = MibTableColumn
sonusDsx3AdmnSlotIndex = _SonusDsx3AdmnSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 2, 1, 1, 2, 1, 4),
    _SonusDsx3AdmnSlotIndex_Type()
)
sonusDsx3AdmnSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx3AdmnSlotIndex.setStatus("current")
_SonusDsx3AdmnPortIndex_Type = Integer32
_SonusDsx3AdmnPortIndex_Object = MibTableColumn
sonusDsx3AdmnPortIndex = _SonusDsx3AdmnPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 2, 1, 1, 2, 1, 5),
    _SonusDsx3AdmnPortIndex_Type()
)
sonusDsx3AdmnPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx3AdmnPortIndex.setStatus("current")
_SonusDsx3AdmnDs3Index_Type = Integer32
_SonusDsx3AdmnDs3Index_Object = MibTableColumn
sonusDsx3AdmnDs3Index = _SonusDsx3AdmnDs3Index_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 2, 1, 1, 2, 1, 6),
    _SonusDsx3AdmnDs3Index_Type()
)
sonusDsx3AdmnDs3Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx3AdmnDs3Index.setStatus("current")
_SonusDsx3AdmnIfIndex_Type = Integer32
_SonusDsx3AdmnIfIndex_Object = MibTableColumn
sonusDsx3AdmnIfIndex = _SonusDsx3AdmnIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 2, 1, 1, 2, 1, 7),
    _SonusDsx3AdmnIfIndex_Type()
)
sonusDsx3AdmnIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx3AdmnIfIndex.setStatus("current")
_SonusDsx3AdmnState_Type = SonusAdminState
_SonusDsx3AdmnState_Object = MibTableColumn
sonusDsx3AdmnState = _SonusDsx3AdmnState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 2, 1, 1, 2, 1, 8),
    _SonusDsx3AdmnState_Type()
)
sonusDsx3AdmnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsx3AdmnState.setStatus("current")


class _SonusDsx3AdmnTimeout_Type(Integer32):
    """Custom type sonusDsx3AdmnTimeout based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_SonusDsx3AdmnTimeout_Type.__name__ = "Integer32"
_SonusDsx3AdmnTimeout_Object = MibTableColumn
sonusDsx3AdmnTimeout = _SonusDsx3AdmnTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 2, 1, 1, 2, 1, 9),
    _SonusDsx3AdmnTimeout_Type()
)
sonusDsx3AdmnTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsx3AdmnTimeout.setStatus("current")


class _SonusDsx3AdmnMode_Type(SonusServiceState):
    """Custom type sonusDsx3AdmnMode based on SonusServiceState"""


_SonusDsx3AdmnMode_Object = MibTableColumn
sonusDsx3AdmnMode = _SonusDsx3AdmnMode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 2, 1, 1, 2, 1, 10),
    _SonusDsx3AdmnMode_Type()
)
sonusDsx3AdmnMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsx3AdmnMode.setStatus("current")


class _SonusDsx3AdmnAction_Type(SonusAdminAction):
    """Custom type sonusDsx3AdmnAction based on SonusAdminAction"""


_SonusDsx3AdmnAction_Object = MibTableColumn
sonusDsx3AdmnAction = _SonusDsx3AdmnAction_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 2, 1, 1, 2, 1, 11),
    _SonusDsx3AdmnAction_Type()
)
sonusDsx3AdmnAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsx3AdmnAction.setStatus("current")


class _SonusDsx3AdmnAvailDs1s_Type(Bits):
    """Custom type sonusDsx3AdmnAvailDs1s based on Bits"""
    namedValues = NamedValues(
        *(("ds1x1", 0),
          ("ds1x10", 9),
          ("ds1x11", 10),
          ("ds1x12", 11),
          ("ds1x13", 12),
          ("ds1x14", 13),
          ("ds1x15", 14),
          ("ds1x16", 15),
          ("ds1x17", 16),
          ("ds1x18", 17),
          ("ds1x19", 18),
          ("ds1x2", 1),
          ("ds1x20", 19),
          ("ds1x21", 20),
          ("ds1x22", 21),
          ("ds1x23", 22),
          ("ds1x24", 23),
          ("ds1x25", 24),
          ("ds1x26", 25),
          ("ds1x27", 26),
          ("ds1x28", 27),
          ("ds1x3", 2),
          ("ds1x4", 3),
          ("ds1x5", 4),
          ("ds1x6", 5),
          ("ds1x7", 6),
          ("ds1x8", 7),
          ("ds1x9", 8))
    )

_SonusDsx3AdmnAvailDs1s_Type.__name__ = "Bits"
_SonusDsx3AdmnAvailDs1s_Object = MibTableColumn
sonusDsx3AdmnAvailDs1s = _SonusDsx3AdmnAvailDs1s_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 2, 1, 1, 2, 1, 12),
    _SonusDsx3AdmnAvailDs1s_Type()
)
sonusDsx3AdmnAvailDs1s.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsx3AdmnAvailDs1s.setStatus("current")


class _SonusDsx3AdmnDs1ModeOverride_Type(SonusAdminState):
    """Custom type sonusDsx3AdmnDs1ModeOverride based on SonusAdminState"""


_SonusDsx3AdmnDs1ModeOverride_Object = MibTableColumn
sonusDsx3AdmnDs1ModeOverride = _SonusDsx3AdmnDs1ModeOverride_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 2, 1, 1, 2, 1, 13),
    _SonusDsx3AdmnDs1ModeOverride_Type()
)
sonusDsx3AdmnDs1ModeOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsx3AdmnDs1ModeOverride.setStatus("current")


class _SonusDsx3AdmnInitCounters_Type(SonusAdminState):
    """Custom type sonusDsx3AdmnInitCounters based on SonusAdminState"""


_SonusDsx3AdmnInitCounters_Object = MibTableColumn
sonusDsx3AdmnInitCounters = _SonusDsx3AdmnInitCounters_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 2, 1, 1, 2, 1, 14),
    _SonusDsx3AdmnInitCounters_Type()
)
sonusDsx3AdmnInitCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsx3AdmnInitCounters.setStatus("current")


class _SonusDsx3AdmnCircuitId_Type(DisplayString):
    """Custom type sonusDsx3AdmnCircuitId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 23),
    )


_SonusDsx3AdmnCircuitId_Type.__name__ = "DisplayString"
_SonusDsx3AdmnCircuitId_Object = MibTableColumn
sonusDsx3AdmnCircuitId = _SonusDsx3AdmnCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 2, 1, 1, 2, 1, 15),
    _SonusDsx3AdmnCircuitId_Type()
)
sonusDsx3AdmnCircuitId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsx3AdmnCircuitId.setStatus("current")
_SonusDsx3StatTable_Object = MibTable
sonusDsx3StatTable = _SonusDsx3StatTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 2, 1, 2)
)
if mibBuilder.loadTexts:
    sonusDsx3StatTable.setStatus("current")
_SonusDsx3StatEntry_Object = MibTableRow
sonusDsx3StatEntry = _SonusDsx3StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 2, 1, 2, 1)
)
sonusDsx3StatEntry.setIndexNames(
    (0, "SONUS-DS3-MIB", "sonusDsx3StatShelfIndex"),
    (0, "SONUS-DS3-MIB", "sonusDsx3StatSlotIndex"),
    (0, "SONUS-DS3-MIB", "sonusDsx3StatPortIndex"),
    (0, "SONUS-DS3-MIB", "sonusDsx3StatDs3Index"),
)
if mibBuilder.loadTexts:
    sonusDsx3StatEntry.setStatus("current")
_SonusDsx3StatShelfIndex_Type = Integer32
_SonusDsx3StatShelfIndex_Object = MibTableColumn
sonusDsx3StatShelfIndex = _SonusDsx3StatShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 2, 1, 2, 1, 1),
    _SonusDsx3StatShelfIndex_Type()
)
sonusDsx3StatShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx3StatShelfIndex.setStatus("current")
_SonusDsx3StatSlotIndex_Type = Integer32
_SonusDsx3StatSlotIndex_Object = MibTableColumn
sonusDsx3StatSlotIndex = _SonusDsx3StatSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 2, 1, 2, 1, 2),
    _SonusDsx3StatSlotIndex_Type()
)
sonusDsx3StatSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx3StatSlotIndex.setStatus("current")
_SonusDsx3StatPortIndex_Type = Integer32
_SonusDsx3StatPortIndex_Object = MibTableColumn
sonusDsx3StatPortIndex = _SonusDsx3StatPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 2, 1, 2, 1, 3),
    _SonusDsx3StatPortIndex_Type()
)
sonusDsx3StatPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx3StatPortIndex.setStatus("current")
_SonusDsx3StatDs3Index_Type = Integer32
_SonusDsx3StatDs3Index_Object = MibTableColumn
sonusDsx3StatDs3Index = _SonusDsx3StatDs3Index_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 2, 1, 2, 1, 4),
    _SonusDsx3StatDs3Index_Type()
)
sonusDsx3StatDs3Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx3StatDs3Index.setStatus("current")
_SonusDsx3StatValidIntervals_Type = Integer32
_SonusDsx3StatValidIntervals_Object = MibTableColumn
sonusDsx3StatValidIntervals = _SonusDsx3StatValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 2, 1, 2, 1, 5),
    _SonusDsx3StatValidIntervals_Type()
)
sonusDsx3StatValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx3StatValidIntervals.setStatus("current")
_SonusDsx3StatDs3LCV_Type = Integer32
_SonusDsx3StatDs3LCV_Object = MibTableColumn
sonusDsx3StatDs3LCV = _SonusDsx3StatDs3LCV_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 2, 1, 2, 1, 6),
    _SonusDsx3StatDs3LCV_Type()
)
sonusDsx3StatDs3LCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx3StatDs3LCV.setStatus("current")
_SonusDsx3StatDs3FERR_Type = Integer32
_SonusDsx3StatDs3FERR_Object = MibTableColumn
sonusDsx3StatDs3FERR = _SonusDsx3StatDs3FERR_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 2, 1, 2, 1, 7),
    _SonusDsx3StatDs3FERR_Type()
)
sonusDsx3StatDs3FERR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx3StatDs3FERR.setStatus("current")
_SonusDsx3StatDs3EXZS_Type = Integer32
_SonusDsx3StatDs3EXZS_Object = MibTableColumn
sonusDsx3StatDs3EXZS = _SonusDsx3StatDs3EXZS_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 2, 1, 2, 1, 8),
    _SonusDsx3StatDs3EXZS_Type()
)
sonusDsx3StatDs3EXZS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx3StatDs3EXZS.setStatus("current")
_SonusDsx3StatDs3PERR_Type = Integer32
_SonusDsx3StatDs3PERR_Object = MibTableColumn
sonusDsx3StatDs3PERR = _SonusDsx3StatDs3PERR_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 2, 1, 2, 1, 9),
    _SonusDsx3StatDs3PERR_Type()
)
sonusDsx3StatDs3PERR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx3StatDs3PERR.setStatus("current")
_SonusDsx3StatDs3CPERR_Type = Integer32
_SonusDsx3StatDs3CPERR_Object = MibTableColumn
sonusDsx3StatDs3CPERR = _SonusDsx3StatDs3CPERR_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 2, 1, 2, 1, 10),
    _SonusDsx3StatDs3CPERR_Type()
)
sonusDsx3StatDs3CPERR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx3StatDs3CPERR.setStatus("current")
_SonusDsx3StatDs3FEBE_Type = Integer32
_SonusDsx3StatDs3FEBE_Object = MibTableColumn
sonusDsx3StatDs3FEBE = _SonusDsx3StatDs3FEBE_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 2, 1, 2, 1, 11),
    _SonusDsx3StatDs3FEBE_Type()
)
sonusDsx3StatDs3FEBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx3StatDs3FEBE.setStatus("current")
_SonusDsx3StatDs3AIS_Type = Integer32
_SonusDsx3StatDs3AIS_Object = MibTableColumn
sonusDsx3StatDs3AIS = _SonusDsx3StatDs3AIS_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 2, 1, 2, 1, 12),
    _SonusDsx3StatDs3AIS_Type()
)
sonusDsx3StatDs3AIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx3StatDs3AIS.setStatus("current")
_SonusDsx3StatDs3LOS_Type = Integer32
_SonusDsx3StatDs3LOS_Object = MibTableColumn
sonusDsx3StatDs3LOS = _SonusDsx3StatDs3LOS_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 2, 1, 2, 1, 13),
    _SonusDsx3StatDs3LOS_Type()
)
sonusDsx3StatDs3LOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx3StatDs3LOS.setStatus("current")


class _SonusDsx3StatLineStatStr_Type(DisplayString):
    """Custom type sonusDsx3StatLineStatStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_SonusDsx3StatLineStatStr_Type.__name__ = "DisplayString"
_SonusDsx3StatLineStatStr_Object = MibTableColumn
sonusDsx3StatLineStatStr = _SonusDsx3StatLineStatStr_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 2, 1, 2, 1, 14),
    _SonusDsx3StatLineStatStr_Type()
)
sonusDsx3StatLineStatStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx3StatLineStatStr.setStatus("current")


class _SonusDsx3StatLoopbackStr_Type(DisplayString):
    """Custom type sonusDsx3StatLoopbackStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SonusDsx3StatLoopbackStr_Type.__name__ = "DisplayString"
_SonusDsx3StatLoopbackStr_Object = MibTableColumn
sonusDsx3StatLoopbackStr = _SonusDsx3StatLoopbackStr_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 2, 1, 2, 1, 15),
    _SonusDsx3StatLoopbackStr_Type()
)
sonusDsx3StatLoopbackStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx3StatLoopbackStr.setStatus("current")


class _SonusDsx3StatOperStatus_Type(Integer32):
    """Custom type sonusDsx3StatOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("dryingUp", 3),
          ("up", 1))
    )


_SonusDsx3StatOperStatus_Type.__name__ = "Integer32"
_SonusDsx3StatOperStatus_Object = MibTableColumn
sonusDsx3StatOperStatus = _SonusDsx3StatOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 2, 1, 2, 1, 16),
    _SonusDsx3StatOperStatus_Type()
)
sonusDsx3StatOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx3StatOperStatus.setStatus("current")
_SonusDsx3MIBNotifications_ObjectIdentity = ObjectIdentity
sonusDsx3MIBNotifications = _SonusDsx3MIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 2, 2)
)
_SonusDsx3MIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
sonusDsx3MIBNotificationsPrefix = _SonusDsx3MIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 2, 2, 0)
)
_SonusDsx3MIBNotificationsObjects_ObjectIdentity = ObjectIdentity
sonusDsx3MIBNotificationsObjects = _SonusDsx3MIBNotificationsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 2, 2, 1)
)


class _SonusDs3OutOfServiceReason_Type(Integer32):
    """Custom type sonusDs3OutOfServiceReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("maintenance", 1)
    )


_SonusDs3OutOfServiceReason_Type.__name__ = "Integer32"
_SonusDs3OutOfServiceReason_Object = MibScalar
sonusDs3OutOfServiceReason = _SonusDs3OutOfServiceReason_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 2, 2, 1, 1),
    _SonusDs3OutOfServiceReason_Type()
)
sonusDs3OutOfServiceReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDs3OutOfServiceReason.setStatus("current")


class _SonusDs3OutOfServiceType_Type(Integer32):
    """Custom type sonusDs3OutOfServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("admin", 1),
          ("hwFailure", 2))
    )


_SonusDs3OutOfServiceType_Type.__name__ = "Integer32"
_SonusDs3OutOfServiceType_Object = MibScalar
sonusDs3OutOfServiceType = _SonusDs3OutOfServiceType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 2, 2, 1, 2),
    _SonusDs3OutOfServiceType_Type()
)
sonusDs3OutOfServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDs3OutOfServiceType.setStatus("current")


class _SonusDs3ThresholdType_Type(Integer32):
    """Custom type sonusDs3ThresholdType based on Integer32"""
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
              20)
        )
    )
    namedValues = NamedValues(
        *(("currentCbitParity", 3),
          ("currentCbitParityErroredSeconds", 7),
          ("currentLineCodeViolation", 1),
          ("currentLineErrorSeconds", 5),
          ("currentLineSeverelyErroredSeconds", 9),
          ("currentPbitParity", 2),
          ("currentPbitParityErroredSeconds", 6),
          ("currentPbitSeverelyErroredSeconds", 8),
          ("currentSeverelyErroredFramingSecs", 4),
          ("currentUnavailableSeconds", 10),
          ("totalCbitParity", 13),
          ("totalCbitParityErroredSeconds", 17),
          ("totalLineCodeViolation", 11),
          ("totalLineErrorSeconds", 15),
          ("totalLineSeverelyErroredSeconds", 19),
          ("totalPbitParity", 12),
          ("totalPbitParityErroredSeconds", 16),
          ("totalPbitSeverelyErroredSeconds", 18),
          ("totalSeverelyErroredFramingSecs", 14),
          ("totalUnavailableSeconds", 20))
    )


_SonusDs3ThresholdType_Type.__name__ = "Integer32"
_SonusDs3ThresholdType_Object = MibScalar
sonusDs3ThresholdType = _SonusDs3ThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 2, 2, 1, 3),
    _SonusDs3ThresholdType_Type()
)
sonusDs3ThresholdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDs3ThresholdType.setStatus("current")


class _SonusDs3LineState_Type(Integer32):
    """Custom type sonusDs3LineState based on Integer32"""
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
        *(("ais", 4),
          ("green", 1),
          ("hwfailure", 5),
          ("rai", 3),
          ("red", 2))
    )


_SonusDs3LineState_Type.__name__ = "Integer32"
_SonusDs3LineState_Object = MibScalar
sonusDs3LineState = _SonusDs3LineState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 2, 2, 1, 4),
    _SonusDs3LineState_Type()
)
sonusDs3LineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDs3LineState.setStatus("current")


class _SonusDs3AdmnState_Type(Integer32):
    """Custom type sonusDs3AdmnState based on Integer32"""
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
        *(("deleted", 3),
          ("disabled", 1),
          ("dryingUp", 5),
          ("enabled", 2),
          ("inservice", 4))
    )


_SonusDs3AdmnState_Type.__name__ = "Integer32"
_SonusDs3AdmnState_Object = MibScalar
sonusDs3AdmnState = _SonusDs3AdmnState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 2, 2, 1, 5),
    _SonusDs3AdmnState_Type()
)
sonusDs3AdmnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDs3AdmnState.setStatus("current")

# Managed Objects groups


# Notification objects

sonusDsx3AdminChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 2, 2, 0, 1)
)
sonusDsx3AdminChangeNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-COMMON-MIB", "sonusPortIndex"),
        ("SONUS-COMMON-MIB", "sonusDs3Index"),
        ("SONUS-DS3-MIB", "sonusDs3AdmnState"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusDsx3AdminChangeNotification.setStatus(
        "current"
    )

sonusDsx3OutOfServiceNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 2, 2, 0, 2)
)
sonusDsx3OutOfServiceNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-COMMON-MIB", "sonusPortIndex"),
        ("SONUS-COMMON-MIB", "sonusDs3Index"),
        ("SONUS-DS3-MIB", "sonusDs3OutOfServiceReason"),
        ("SONUS-DS3-MIB", "sonusDs3OutOfServiceType"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusDsx3OutOfServiceNotification.setStatus(
        "current"
    )

sonusDsx3ThresholdCrossingNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 2, 2, 0, 3)
)
sonusDsx3ThresholdCrossingNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-COMMON-MIB", "sonusPortIndex"),
        ("SONUS-COMMON-MIB", "sonusDs3Index"),
        ("SONUS-DS3-MIB", "sonusDs3ThresholdType"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusDsx3ThresholdCrossingNotification.setStatus(
        "current"
    )

sonusDsx3LineStatusChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 2, 2, 0, 4)
)
sonusDsx3LineStatusChangeNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-COMMON-MIB", "sonusPortIndex"),
        ("SONUS-COMMON-MIB", "sonusDs3Index"),
        ("SONUS-DS3-MIB", "sonusDs3LineState"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusDsx3LineStatusChangeNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONUS-DS3-MIB",
    **{"sonusDsx3MIB": sonusDsx3MIB,
       "sonusDsx3MIBObjects": sonusDsx3MIBObjects,
       "sonusDsx3Admn": sonusDsx3Admn,
       "sonusDsx3AdmnNextIndex": sonusDsx3AdmnNextIndex,
       "sonusDsx3AdmnTable": sonusDsx3AdmnTable,
       "sonusDsx3AdmnEntry": sonusDsx3AdmnEntry,
       "sonusDsx3AdmnRowStatus": sonusDsx3AdmnRowStatus,
       "sonusDsx3AdmnName": sonusDsx3AdmnName,
       "sonusDsx3AdmnShelfIndex": sonusDsx3AdmnShelfIndex,
       "sonusDsx3AdmnSlotIndex": sonusDsx3AdmnSlotIndex,
       "sonusDsx3AdmnPortIndex": sonusDsx3AdmnPortIndex,
       "sonusDsx3AdmnDs3Index": sonusDsx3AdmnDs3Index,
       "sonusDsx3AdmnIfIndex": sonusDsx3AdmnIfIndex,
       "sonusDsx3AdmnState": sonusDsx3AdmnState,
       "sonusDsx3AdmnTimeout": sonusDsx3AdmnTimeout,
       "sonusDsx3AdmnMode": sonusDsx3AdmnMode,
       "sonusDsx3AdmnAction": sonusDsx3AdmnAction,
       "sonusDsx3AdmnAvailDs1s": sonusDsx3AdmnAvailDs1s,
       "sonusDsx3AdmnDs1ModeOverride": sonusDsx3AdmnDs1ModeOverride,
       "sonusDsx3AdmnInitCounters": sonusDsx3AdmnInitCounters,
       "sonusDsx3AdmnCircuitId": sonusDsx3AdmnCircuitId,
       "sonusDsx3StatTable": sonusDsx3StatTable,
       "sonusDsx3StatEntry": sonusDsx3StatEntry,
       "sonusDsx3StatShelfIndex": sonusDsx3StatShelfIndex,
       "sonusDsx3StatSlotIndex": sonusDsx3StatSlotIndex,
       "sonusDsx3StatPortIndex": sonusDsx3StatPortIndex,
       "sonusDsx3StatDs3Index": sonusDsx3StatDs3Index,
       "sonusDsx3StatValidIntervals": sonusDsx3StatValidIntervals,
       "sonusDsx3StatDs3LCV": sonusDsx3StatDs3LCV,
       "sonusDsx3StatDs3FERR": sonusDsx3StatDs3FERR,
       "sonusDsx3StatDs3EXZS": sonusDsx3StatDs3EXZS,
       "sonusDsx3StatDs3PERR": sonusDsx3StatDs3PERR,
       "sonusDsx3StatDs3CPERR": sonusDsx3StatDs3CPERR,
       "sonusDsx3StatDs3FEBE": sonusDsx3StatDs3FEBE,
       "sonusDsx3StatDs3AIS": sonusDsx3StatDs3AIS,
       "sonusDsx3StatDs3LOS": sonusDsx3StatDs3LOS,
       "sonusDsx3StatLineStatStr": sonusDsx3StatLineStatStr,
       "sonusDsx3StatLoopbackStr": sonusDsx3StatLoopbackStr,
       "sonusDsx3StatOperStatus": sonusDsx3StatOperStatus,
       "sonusDsx3MIBNotifications": sonusDsx3MIBNotifications,
       "sonusDsx3MIBNotificationsPrefix": sonusDsx3MIBNotificationsPrefix,
       "sonusDsx3AdminChangeNotification": sonusDsx3AdminChangeNotification,
       "sonusDsx3OutOfServiceNotification": sonusDsx3OutOfServiceNotification,
       "sonusDsx3ThresholdCrossingNotification": sonusDsx3ThresholdCrossingNotification,
       "sonusDsx3LineStatusChangeNotification": sonusDsx3LineStatusChangeNotification,
       "sonusDsx3MIBNotificationsObjects": sonusDsx3MIBNotificationsObjects,
       "sonusDs3OutOfServiceReason": sonusDs3OutOfServiceReason,
       "sonusDs3OutOfServiceType": sonusDs3OutOfServiceType,
       "sonusDs3ThresholdType": sonusDs3ThresholdType,
       "sonusDs3LineState": sonusDs3LineState,
       "sonusDs3AdmnState": sonusDs3AdmnState}
)
