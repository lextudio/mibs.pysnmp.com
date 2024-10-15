# SNMP MIB module (CISCO-DOT11-WIDS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DOT11-WIDS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:59 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 MacAddress,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoDot11WidsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 456)
)
ciscoDot11WidsMIB.setRevisions(
        ("2004-11-30 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoDot11WidsMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoDot11WidsMIBNotifs = _CiscoDot11WidsMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 456, 0)
)
_CiscoDot11WidsMIBObjects_ObjectIdentity = ObjectIdentity
ciscoDot11WidsMIBObjects = _CiscoDot11WidsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 456, 1)
)
_CiscoDot11WidsAuthFailures_ObjectIdentity = ObjectIdentity
ciscoDot11WidsAuthFailures = _CiscoDot11WidsAuthFailures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 456, 1, 1)
)
_CDot11WidsFloodDetectEnable_Type = TruthValue
_CDot11WidsFloodDetectEnable_Object = MibScalar
cDot11WidsFloodDetectEnable = _CDot11WidsFloodDetectEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 456, 1, 1, 1),
    _CDot11WidsFloodDetectEnable_Type()
)
cDot11WidsFloodDetectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cDot11WidsFloodDetectEnable.setStatus("current")


class _CDot11WidsEapolFloodThreshold_Type(Unsigned32):
    """Custom type cDot11WidsEapolFloodThreshold based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_CDot11WidsEapolFloodThreshold_Type.__name__ = "Unsigned32"
_CDot11WidsEapolFloodThreshold_Object = MibScalar
cDot11WidsEapolFloodThreshold = _CDot11WidsEapolFloodThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 456, 1, 1, 2),
    _CDot11WidsEapolFloodThreshold_Type()
)
cDot11WidsEapolFloodThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cDot11WidsEapolFloodThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cDot11WidsEapolFloodThreshold.setUnits("attempts")


class _CDot11WidsEapolFloodInterval_Type(Unsigned32):
    """Custom type cDot11WidsEapolFloodInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_CDot11WidsEapolFloodInterval_Type.__name__ = "Unsigned32"
_CDot11WidsEapolFloodInterval_Object = MibScalar
cDot11WidsEapolFloodInterval = _CDot11WidsEapolFloodInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 456, 1, 1, 3),
    _CDot11WidsEapolFloodInterval_Type()
)
cDot11WidsEapolFloodInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cDot11WidsEapolFloodInterval.setStatus("current")
if mibBuilder.loadTexts:
    cDot11WidsEapolFloodInterval.setUnits("seconds")


class _CDot11WidsBlackListThreshold_Type(Unsigned32):
    """Custom type cDot11WidsBlackListThreshold based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_CDot11WidsBlackListThreshold_Type.__name__ = "Unsigned32"
_CDot11WidsBlackListThreshold_Object = MibScalar
cDot11WidsBlackListThreshold = _CDot11WidsBlackListThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 456, 1, 1, 4),
    _CDot11WidsBlackListThreshold_Type()
)
cDot11WidsBlackListThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cDot11WidsBlackListThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cDot11WidsBlackListThreshold.setUnits("attempts")


class _CDot11WidsBlackListDuration_Type(Unsigned32):
    """Custom type cDot11WidsBlackListDuration based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_CDot11WidsBlackListDuration_Type.__name__ = "Unsigned32"
_CDot11WidsBlackListDuration_Object = MibScalar
cDot11WidsBlackListDuration = _CDot11WidsBlackListDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 456, 1, 1, 5),
    _CDot11WidsBlackListDuration_Type()
)
cDot11WidsBlackListDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cDot11WidsBlackListDuration.setStatus("current")
if mibBuilder.loadTexts:
    cDot11WidsBlackListDuration.setUnits("seconds")


class _CDot11WidsFloodMaxEntriesPerIntf_Type(Integer32):
    """Custom type cDot11WidsFloodMaxEntriesPerIntf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CDot11WidsFloodMaxEntriesPerIntf_Type.__name__ = "Integer32"
_CDot11WidsFloodMaxEntriesPerIntf_Object = MibScalar
cDot11WidsFloodMaxEntriesPerIntf = _CDot11WidsFloodMaxEntriesPerIntf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 456, 1, 1, 6),
    _CDot11WidsFloodMaxEntriesPerIntf_Type()
)
cDot11WidsFloodMaxEntriesPerIntf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cDot11WidsFloodMaxEntriesPerIntf.setStatus("current")
_CDot11WidsEapolFloodTable_Object = MibTable
cDot11WidsEapolFloodTable = _CDot11WidsEapolFloodTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 456, 1, 1, 7)
)
if mibBuilder.loadTexts:
    cDot11WidsEapolFloodTable.setStatus("current")
_CDot11WidsEapolFloodEntry_Object = MibTableRow
cDot11WidsEapolFloodEntry = _CDot11WidsEapolFloodEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 456, 1, 1, 7, 1)
)
cDot11WidsEapolFloodEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-DOT11-WIDS-MIB", "cDot11WidsEapolFloodIndex"),
)
if mibBuilder.loadTexts:
    cDot11WidsEapolFloodEntry.setStatus("current")


class _CDot11WidsEapolFloodIndex_Type(Unsigned32):
    """Custom type cDot11WidsEapolFloodIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CDot11WidsEapolFloodIndex_Type.__name__ = "Unsigned32"
_CDot11WidsEapolFloodIndex_Object = MibTableColumn
cDot11WidsEapolFloodIndex = _CDot11WidsEapolFloodIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 456, 1, 1, 7, 1, 1),
    _CDot11WidsEapolFloodIndex_Type()
)
cDot11WidsEapolFloodIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cDot11WidsEapolFloodIndex.setStatus("current")
_CDot11WidsEapolFloodClientMac_Type = MacAddress
_CDot11WidsEapolFloodClientMac_Object = MibTableColumn
cDot11WidsEapolFloodClientMac = _CDot11WidsEapolFloodClientMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 456, 1, 1, 7, 1, 2),
    _CDot11WidsEapolFloodClientMac_Type()
)
cDot11WidsEapolFloodClientMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11WidsEapolFloodClientMac.setStatus("current")
_CDot11WidsEapolFloodClientCount_Type = Unsigned32
_CDot11WidsEapolFloodClientCount_Object = MibTableColumn
cDot11WidsEapolFloodClientCount = _CDot11WidsEapolFloodClientCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 456, 1, 1, 7, 1, 3),
    _CDot11WidsEapolFloodClientCount_Type()
)
cDot11WidsEapolFloodClientCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11WidsEapolFloodClientCount.setStatus("current")
_CDot11WidsEapolFloodStartTime_Type = TimeStamp
_CDot11WidsEapolFloodStartTime_Object = MibTableColumn
cDot11WidsEapolFloodStartTime = _CDot11WidsEapolFloodStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 456, 1, 1, 7, 1, 4),
    _CDot11WidsEapolFloodStartTime_Type()
)
cDot11WidsEapolFloodStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11WidsEapolFloodStartTime.setStatus("current")
_CDot11WidsEapolFloodStopTime_Type = TimeStamp
_CDot11WidsEapolFloodStopTime_Object = MibTableColumn
cDot11WidsEapolFloodStopTime = _CDot11WidsEapolFloodStopTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 456, 1, 1, 7, 1, 5),
    _CDot11WidsEapolFloodStopTime_Type()
)
cDot11WidsEapolFloodStopTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11WidsEapolFloodStopTime.setStatus("current")
_CDot11WidsEapolFloodTotalCount_Type = Counter32
_CDot11WidsEapolFloodTotalCount_Object = MibTableColumn
cDot11WidsEapolFloodTotalCount = _CDot11WidsEapolFloodTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 456, 1, 1, 7, 1, 6),
    _CDot11WidsEapolFloodTotalCount_Type()
)
cDot11WidsEapolFloodTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11WidsEapolFloodTotalCount.setStatus("current")
_CDot11WidsBlackListTable_Object = MibTable
cDot11WidsBlackListTable = _CDot11WidsBlackListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 456, 1, 1, 8)
)
if mibBuilder.loadTexts:
    cDot11WidsBlackListTable.setStatus("current")
_CDot11WidsBlackListEntry_Object = MibTableRow
cDot11WidsBlackListEntry = _CDot11WidsBlackListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 456, 1, 1, 8, 1)
)
cDot11WidsBlackListEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-DOT11-WIDS-MIB", "cDot11WidsBlackListClientMac"),
)
if mibBuilder.loadTexts:
    cDot11WidsBlackListEntry.setStatus("current")
_CDot11WidsBlackListClientMac_Type = MacAddress
_CDot11WidsBlackListClientMac_Object = MibTableColumn
cDot11WidsBlackListClientMac = _CDot11WidsBlackListClientMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 456, 1, 1, 8, 1, 1),
    _CDot11WidsBlackListClientMac_Type()
)
cDot11WidsBlackListClientMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cDot11WidsBlackListClientMac.setStatus("current")
_CDot11WidsBlackListAttemptCount_Type = Counter32
_CDot11WidsBlackListAttemptCount_Object = MibTableColumn
cDot11WidsBlackListAttemptCount = _CDot11WidsBlackListAttemptCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 456, 1, 1, 8, 1, 2),
    _CDot11WidsBlackListAttemptCount_Type()
)
cDot11WidsBlackListAttemptCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11WidsBlackListAttemptCount.setStatus("current")
_CDot11WidsBlackListTime_Type = TimeStamp
_CDot11WidsBlackListTime_Object = MibTableColumn
cDot11WidsBlackListTime = _CDot11WidsBlackListTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 456, 1, 1, 8, 1, 3),
    _CDot11WidsBlackListTime_Type()
)
cDot11WidsBlackListTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11WidsBlackListTime.setStatus("current")
_CiscoDot11WidsProtectFailures_ObjectIdentity = ObjectIdentity
ciscoDot11WidsProtectFailures = _CiscoDot11WidsProtectFailures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 456, 1, 2)
)
_CDot11WidsProtectFailClientTable_Object = MibTable
cDot11WidsProtectFailClientTable = _CDot11WidsProtectFailClientTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 456, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cDot11WidsProtectFailClientTable.setStatus("current")
_CDot11WidsProtectFailClientEntry_Object = MibTableRow
cDot11WidsProtectFailClientEntry = _CDot11WidsProtectFailClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 456, 1, 2, 1, 1)
)
cDot11WidsProtectFailClientEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-DOT11-WIDS-MIB", "cDot11WidsSsid"),
    (0, "CISCO-DOT11-WIDS-MIB", "cDot11WidsClientMacAddress"),
)
if mibBuilder.loadTexts:
    cDot11WidsProtectFailClientEntry.setStatus("current")


class _CDot11WidsSsid_Type(OctetString):
    """Custom type cDot11WidsSsid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CDot11WidsSsid_Type.__name__ = "OctetString"
_CDot11WidsSsid_Object = MibTableColumn
cDot11WidsSsid = _CDot11WidsSsid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 456, 1, 2, 1, 1, 1),
    _CDot11WidsSsid_Type()
)
cDot11WidsSsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cDot11WidsSsid.setStatus("current")
_CDot11WidsClientMacAddress_Type = MacAddress
_CDot11WidsClientMacAddress_Object = MibTableColumn
cDot11WidsClientMacAddress = _CDot11WidsClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 456, 1, 2, 1, 1, 2),
    _CDot11WidsClientMacAddress_Type()
)
cDot11WidsClientMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cDot11WidsClientMacAddress.setStatus("current")


class _CDot11WidsSelPairWiseCipher_Type(OctetString):
    """Custom type cDot11WidsSelPairWiseCipher based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CDot11WidsSelPairWiseCipher_Type.__name__ = "OctetString"
_CDot11WidsSelPairWiseCipher_Object = MibTableColumn
cDot11WidsSelPairWiseCipher = _CDot11WidsSelPairWiseCipher_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 456, 1, 2, 1, 1, 3),
    _CDot11WidsSelPairWiseCipher_Type()
)
cDot11WidsSelPairWiseCipher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11WidsSelPairWiseCipher.setStatus("current")
_CDot11WidsTkipIcvErrors_Type = Counter32
_CDot11WidsTkipIcvErrors_Object = MibTableColumn
cDot11WidsTkipIcvErrors = _CDot11WidsTkipIcvErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 456, 1, 2, 1, 1, 4),
    _CDot11WidsTkipIcvErrors_Type()
)
cDot11WidsTkipIcvErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11WidsTkipIcvErrors.setStatus("current")
_CDot11WidsTkipLocalMicFailures_Type = Counter32
_CDot11WidsTkipLocalMicFailures_Object = MibTableColumn
cDot11WidsTkipLocalMicFailures = _CDot11WidsTkipLocalMicFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 456, 1, 2, 1, 1, 5),
    _CDot11WidsTkipLocalMicFailures_Type()
)
cDot11WidsTkipLocalMicFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11WidsTkipLocalMicFailures.setStatus("current")
_CDot11WidsTkipRemoteMicFailures_Type = Counter32
_CDot11WidsTkipRemoteMicFailures_Object = MibTableColumn
cDot11WidsTkipRemoteMicFailures = _CDot11WidsTkipRemoteMicFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 456, 1, 2, 1, 1, 6),
    _CDot11WidsTkipRemoteMicFailures_Type()
)
cDot11WidsTkipRemoteMicFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11WidsTkipRemoteMicFailures.setStatus("current")
_CDot11WidsCcmpReplays_Type = Counter32
_CDot11WidsCcmpReplays_Object = MibTableColumn
cDot11WidsCcmpReplays = _CDot11WidsCcmpReplays_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 456, 1, 2, 1, 1, 7),
    _CDot11WidsCcmpReplays_Type()
)
cDot11WidsCcmpReplays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11WidsCcmpReplays.setStatus("current")
_CDot11WidsCcmpDecryptErrors_Type = Counter32
_CDot11WidsCcmpDecryptErrors_Object = MibTableColumn
cDot11WidsCcmpDecryptErrors = _CDot11WidsCcmpDecryptErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 456, 1, 2, 1, 1, 8),
    _CDot11WidsCcmpDecryptErrors_Type()
)
cDot11WidsCcmpDecryptErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11WidsCcmpDecryptErrors.setStatus("current")
_CDot11WidsTkipReplays_Type = Counter32
_CDot11WidsTkipReplays_Object = MibTableColumn
cDot11WidsTkipReplays = _CDot11WidsTkipReplays_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 456, 1, 2, 1, 1, 9),
    _CDot11WidsTkipReplays_Type()
)
cDot11WidsTkipReplays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11WidsTkipReplays.setStatus("current")
_CDot11WidsWepReplays_Type = Counter32
_CDot11WidsWepReplays_Object = MibTableColumn
cDot11WidsWepReplays = _CDot11WidsWepReplays_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 456, 1, 2, 1, 1, 10),
    _CDot11WidsWepReplays_Type()
)
cDot11WidsWepReplays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11WidsWepReplays.setStatus("current")
_CDot11WidsWepIcvErrors_Type = Counter32
_CDot11WidsWepIcvErrors_Object = MibTableColumn
cDot11WidsWepIcvErrors = _CDot11WidsWepIcvErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 456, 1, 2, 1, 1, 11),
    _CDot11WidsWepIcvErrors_Type()
)
cDot11WidsWepIcvErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11WidsWepIcvErrors.setStatus("current")
_CDot11WidsCkipReplays_Type = Counter32
_CDot11WidsCkipReplays_Object = MibTableColumn
cDot11WidsCkipReplays = _CDot11WidsCkipReplays_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 456, 1, 2, 1, 1, 12),
    _CDot11WidsCkipReplays_Type()
)
cDot11WidsCkipReplays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11WidsCkipReplays.setStatus("current")
_CDot11WidsCkipCmicErrors_Type = Counter32
_CDot11WidsCkipCmicErrors_Object = MibTableColumn
cDot11WidsCkipCmicErrors = _CDot11WidsCkipCmicErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 456, 1, 2, 1, 1, 13),
    _CDot11WidsCkipCmicErrors_Type()
)
cDot11WidsCkipCmicErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11WidsCkipCmicErrors.setStatus("current")
_CiscoDot11WidsMIBConform_ObjectIdentity = ObjectIdentity
ciscoDot11WidsMIBConform = _CiscoDot11WidsMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 456, 2)
)
_CiscoDot11WidsMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoDot11WidsMIBCompliances = _CiscoDot11WidsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 456, 2, 1)
)
_CiscoDot11WidsMIBGroups_ObjectIdentity = ObjectIdentity
ciscoDot11WidsMIBGroups = _CiscoDot11WidsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 456, 2, 2)
)

# Managed Objects groups

ciscoDot11WidsAuthFailGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 456, 2, 2, 1)
)
ciscoDot11WidsAuthFailGroup.setObjects(
      *(("CISCO-DOT11-WIDS-MIB", "cDot11WidsFloodDetectEnable"),
        ("CISCO-DOT11-WIDS-MIB", "cDot11WidsEapolFloodThreshold"),
        ("CISCO-DOT11-WIDS-MIB", "cDot11WidsEapolFloodInterval"),
        ("CISCO-DOT11-WIDS-MIB", "cDot11WidsBlackListThreshold"),
        ("CISCO-DOT11-WIDS-MIB", "cDot11WidsBlackListDuration"),
        ("CISCO-DOT11-WIDS-MIB", "cDot11WidsFloodMaxEntriesPerIntf"),
        ("CISCO-DOT11-WIDS-MIB", "cDot11WidsEapolFloodTotalCount"),
        ("CISCO-DOT11-WIDS-MIB", "cDot11WidsEapolFloodClientMac"),
        ("CISCO-DOT11-WIDS-MIB", "cDot11WidsEapolFloodClientCount"),
        ("CISCO-DOT11-WIDS-MIB", "cDot11WidsEapolFloodStartTime"),
        ("CISCO-DOT11-WIDS-MIB", "cDot11WidsEapolFloodStopTime"),
        ("CISCO-DOT11-WIDS-MIB", "cDot11WidsBlackListAttemptCount"),
        ("CISCO-DOT11-WIDS-MIB", "cDot11WidsBlackListTime"))
)
if mibBuilder.loadTexts:
    ciscoDot11WidsAuthFailGroup.setStatus("current")

ciscoDot11WidsProtectFailGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 456, 2, 2, 2)
)
ciscoDot11WidsProtectFailGroup.setObjects(
      *(("CISCO-DOT11-WIDS-MIB", "cDot11WidsSelPairWiseCipher"),
        ("CISCO-DOT11-WIDS-MIB", "cDot11WidsTkipIcvErrors"),
        ("CISCO-DOT11-WIDS-MIB", "cDot11WidsTkipLocalMicFailures"),
        ("CISCO-DOT11-WIDS-MIB", "cDot11WidsTkipRemoteMicFailures"),
        ("CISCO-DOT11-WIDS-MIB", "cDot11WidsCcmpReplays"),
        ("CISCO-DOT11-WIDS-MIB", "cDot11WidsCcmpDecryptErrors"),
        ("CISCO-DOT11-WIDS-MIB", "cDot11WidsTkipReplays"),
        ("CISCO-DOT11-WIDS-MIB", "cDot11WidsWepReplays"),
        ("CISCO-DOT11-WIDS-MIB", "cDot11WidsWepIcvErrors"),
        ("CISCO-DOT11-WIDS-MIB", "cDot11WidsCkipReplays"),
        ("CISCO-DOT11-WIDS-MIB", "cDot11WidsCkipCmicErrors"))
)
if mibBuilder.loadTexts:
    ciscoDot11WidsProtectFailGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoDot11WidsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 456, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoDot11WidsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DOT11-WIDS-MIB",
    **{"ciscoDot11WidsMIB": ciscoDot11WidsMIB,
       "ciscoDot11WidsMIBNotifs": ciscoDot11WidsMIBNotifs,
       "ciscoDot11WidsMIBObjects": ciscoDot11WidsMIBObjects,
       "ciscoDot11WidsAuthFailures": ciscoDot11WidsAuthFailures,
       "cDot11WidsFloodDetectEnable": cDot11WidsFloodDetectEnable,
       "cDot11WidsEapolFloodThreshold": cDot11WidsEapolFloodThreshold,
       "cDot11WidsEapolFloodInterval": cDot11WidsEapolFloodInterval,
       "cDot11WidsBlackListThreshold": cDot11WidsBlackListThreshold,
       "cDot11WidsBlackListDuration": cDot11WidsBlackListDuration,
       "cDot11WidsFloodMaxEntriesPerIntf": cDot11WidsFloodMaxEntriesPerIntf,
       "cDot11WidsEapolFloodTable": cDot11WidsEapolFloodTable,
       "cDot11WidsEapolFloodEntry": cDot11WidsEapolFloodEntry,
       "cDot11WidsEapolFloodIndex": cDot11WidsEapolFloodIndex,
       "cDot11WidsEapolFloodClientMac": cDot11WidsEapolFloodClientMac,
       "cDot11WidsEapolFloodClientCount": cDot11WidsEapolFloodClientCount,
       "cDot11WidsEapolFloodStartTime": cDot11WidsEapolFloodStartTime,
       "cDot11WidsEapolFloodStopTime": cDot11WidsEapolFloodStopTime,
       "cDot11WidsEapolFloodTotalCount": cDot11WidsEapolFloodTotalCount,
       "cDot11WidsBlackListTable": cDot11WidsBlackListTable,
       "cDot11WidsBlackListEntry": cDot11WidsBlackListEntry,
       "cDot11WidsBlackListClientMac": cDot11WidsBlackListClientMac,
       "cDot11WidsBlackListAttemptCount": cDot11WidsBlackListAttemptCount,
       "cDot11WidsBlackListTime": cDot11WidsBlackListTime,
       "ciscoDot11WidsProtectFailures": ciscoDot11WidsProtectFailures,
       "cDot11WidsProtectFailClientTable": cDot11WidsProtectFailClientTable,
       "cDot11WidsProtectFailClientEntry": cDot11WidsProtectFailClientEntry,
       "cDot11WidsSsid": cDot11WidsSsid,
       "cDot11WidsClientMacAddress": cDot11WidsClientMacAddress,
       "cDot11WidsSelPairWiseCipher": cDot11WidsSelPairWiseCipher,
       "cDot11WidsTkipIcvErrors": cDot11WidsTkipIcvErrors,
       "cDot11WidsTkipLocalMicFailures": cDot11WidsTkipLocalMicFailures,
       "cDot11WidsTkipRemoteMicFailures": cDot11WidsTkipRemoteMicFailures,
       "cDot11WidsCcmpReplays": cDot11WidsCcmpReplays,
       "cDot11WidsCcmpDecryptErrors": cDot11WidsCcmpDecryptErrors,
       "cDot11WidsTkipReplays": cDot11WidsTkipReplays,
       "cDot11WidsWepReplays": cDot11WidsWepReplays,
       "cDot11WidsWepIcvErrors": cDot11WidsWepIcvErrors,
       "cDot11WidsCkipReplays": cDot11WidsCkipReplays,
       "cDot11WidsCkipCmicErrors": cDot11WidsCkipCmicErrors,
       "ciscoDot11WidsMIBConform": ciscoDot11WidsMIBConform,
       "ciscoDot11WidsMIBCompliances": ciscoDot11WidsMIBCompliances,
       "ciscoDot11WidsMIBCompliance": ciscoDot11WidsMIBCompliance,
       "ciscoDot11WidsMIBGroups": ciscoDot11WidsMIBGroups,
       "ciscoDot11WidsAuthFailGroup": ciscoDot11WidsAuthFailGroup,
       "ciscoDot11WidsProtectFailGroup": ciscoDot11WidsProtectFailGroup}
)
