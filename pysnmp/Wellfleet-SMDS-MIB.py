# SNMP MIB module (Wellfleet-SMDS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-SMDS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:05 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(wfWanGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfWanGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfSmdsCircuitTable_Object = MibTable
wfSmdsCircuitTable = _WfSmdsCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 3)
)
if mibBuilder.loadTexts:
    wfSmdsCircuitTable.setStatus("mandatory")
_WfSmdsCircuitEntry_Object = MibTableRow
wfSmdsCircuitEntry = _WfSmdsCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 3, 1)
)
wfSmdsCircuitEntry.setIndexNames(
    (0, "Wellfleet-SMDS-MIB", "wfSmdsCircuitID"),
)
if mibBuilder.loadTexts:
    wfSmdsCircuitEntry.setStatus("mandatory")


class _WfSmdsCircuitDelete_Type(Integer32):
    """Custom type wfSmdsCircuitDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfSmdsCircuitDelete_Type.__name__ = "Integer32"
_WfSmdsCircuitDelete_Object = MibTableColumn
wfSmdsCircuitDelete = _WfSmdsCircuitDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 3, 1, 1),
    _WfSmdsCircuitDelete_Type()
)
wfSmdsCircuitDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsCircuitDelete.setStatus("mandatory")


class _WfSmdsCircuitDisable_Type(Integer32):
    """Custom type wfSmdsCircuitDisable based on Integer32"""
    defaultValue = 1

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


_WfSmdsCircuitDisable_Type.__name__ = "Integer32"
_WfSmdsCircuitDisable_Object = MibTableColumn
wfSmdsCircuitDisable = _WfSmdsCircuitDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 3, 1, 2),
    _WfSmdsCircuitDisable_Type()
)
wfSmdsCircuitDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsCircuitDisable.setStatus("mandatory")


class _WfSmdsCircuitState_Type(Integer32):
    """Custom type wfSmdsCircuitState based on Integer32"""
    defaultValue = 4

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
        *(("down", 2),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfSmdsCircuitState_Type.__name__ = "Integer32"
_WfSmdsCircuitState_Object = MibTableColumn
wfSmdsCircuitState = _WfSmdsCircuitState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 3, 1, 3),
    _WfSmdsCircuitState_Type()
)
wfSmdsCircuitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsCircuitState.setStatus("mandatory")


class _WfSmdsCircuitID_Type(Integer32):
    """Custom type wfSmdsCircuitID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_WfSmdsCircuitID_Type.__name__ = "Integer32"
_WfSmdsCircuitID_Object = MibTableColumn
wfSmdsCircuitID = _WfSmdsCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 3, 1, 4),
    _WfSmdsCircuitID_Type()
)
wfSmdsCircuitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsCircuitID.setStatus("mandatory")
_WfSmdsCircuitIndivAddr_Type = OctetString
_WfSmdsCircuitIndivAddr_Object = MibTableColumn
wfSmdsCircuitIndivAddr = _WfSmdsCircuitIndivAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 3, 1, 5),
    _WfSmdsCircuitIndivAddr_Type()
)
wfSmdsCircuitIndivAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsCircuitIndivAddr.setStatus("mandatory")
_WfSmdsCircuitGroupAddr_Type = OctetString
_WfSmdsCircuitGroupAddr_Object = MibTableColumn
wfSmdsCircuitGroupAddr = _WfSmdsCircuitGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 3, 1, 6),
    _WfSmdsCircuitGroupAddr_Type()
)
wfSmdsCircuitGroupAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsCircuitGroupAddr.setStatus("mandatory")
_WfSmdsCircuitArpAddr_Type = OctetString
_WfSmdsCircuitArpAddr_Object = MibTableColumn
wfSmdsCircuitArpAddr = _WfSmdsCircuitArpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 3, 1, 7),
    _WfSmdsCircuitArpAddr_Type()
)
wfSmdsCircuitArpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsCircuitArpAddr.setStatus("mandatory")


class _WfSmdsCircuitDisableHrtbtPoll_Type(Integer32):
    """Custom type wfSmdsCircuitDisableHrtbtPoll based on Integer32"""
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


_WfSmdsCircuitDisableHrtbtPoll_Type.__name__ = "Integer32"
_WfSmdsCircuitDisableHrtbtPoll_Object = MibTableColumn
wfSmdsCircuitDisableHrtbtPoll = _WfSmdsCircuitDisableHrtbtPoll_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 3, 1, 8),
    _WfSmdsCircuitDisableHrtbtPoll_Type()
)
wfSmdsCircuitDisableHrtbtPoll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsCircuitDisableHrtbtPoll.setStatus("mandatory")


class _WfSmdsCircuitHrtbtPollInterval_Type(Integer32):
    """Custom type wfSmdsCircuitHrtbtPollInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 2147483647),
    )


_WfSmdsCircuitHrtbtPollInterval_Type.__name__ = "Integer32"
_WfSmdsCircuitHrtbtPollInterval_Object = MibTableColumn
wfSmdsCircuitHrtbtPollInterval = _WfSmdsCircuitHrtbtPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 3, 1, 9),
    _WfSmdsCircuitHrtbtPollInterval_Type()
)
wfSmdsCircuitHrtbtPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsCircuitHrtbtPollInterval.setStatus("mandatory")


class _WfSmdsCircuitHrtbtPollDownCount_Type(Integer32):
    """Custom type wfSmdsCircuitHrtbtPollDownCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfSmdsCircuitHrtbtPollDownCount_Type.__name__ = "Integer32"
_WfSmdsCircuitHrtbtPollDownCount_Object = MibTableColumn
wfSmdsCircuitHrtbtPollDownCount = _WfSmdsCircuitHrtbtPollDownCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 3, 1, 10),
    _WfSmdsCircuitHrtbtPollDownCount_Type()
)
wfSmdsCircuitHrtbtPollDownCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsCircuitHrtbtPollDownCount.setStatus("mandatory")


class _WfSmdsCircuitDisableNetMgmt_Type(Integer32):
    """Custom type wfSmdsCircuitDisableNetMgmt based on Integer32"""
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


_WfSmdsCircuitDisableNetMgmt_Type.__name__ = "Integer32"
_WfSmdsCircuitDisableNetMgmt_Object = MibTableColumn
wfSmdsCircuitDisableNetMgmt = _WfSmdsCircuitDisableNetMgmt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 3, 1, 11),
    _WfSmdsCircuitDisableNetMgmt_Type()
)
wfSmdsCircuitDisableNetMgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsCircuitDisableNetMgmt.setStatus("mandatory")
_WfSmdsCircuitSipL3ReceivedIndividualDAs_Type = Counter32
_WfSmdsCircuitSipL3ReceivedIndividualDAs_Object = MibTableColumn
wfSmdsCircuitSipL3ReceivedIndividualDAs = _WfSmdsCircuitSipL3ReceivedIndividualDAs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 3, 1, 12),
    _WfSmdsCircuitSipL3ReceivedIndividualDAs_Type()
)
wfSmdsCircuitSipL3ReceivedIndividualDAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsCircuitSipL3ReceivedIndividualDAs.setStatus("mandatory")
_WfSmdsCircuitSipL3ReceivedGAs_Type = Counter32
_WfSmdsCircuitSipL3ReceivedGAs_Object = MibTableColumn
wfSmdsCircuitSipL3ReceivedGAs = _WfSmdsCircuitSipL3ReceivedGAs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 3, 1, 13),
    _WfSmdsCircuitSipL3ReceivedGAs_Type()
)
wfSmdsCircuitSipL3ReceivedGAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsCircuitSipL3ReceivedGAs.setStatus("mandatory")
_WfSmdsCircuitSipL3SentIndividualDAs_Type = Counter32
_WfSmdsCircuitSipL3SentIndividualDAs_Object = MibTableColumn
wfSmdsCircuitSipL3SentIndividualDAs = _WfSmdsCircuitSipL3SentIndividualDAs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 3, 1, 14),
    _WfSmdsCircuitSipL3SentIndividualDAs_Type()
)
wfSmdsCircuitSipL3SentIndividualDAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsCircuitSipL3SentIndividualDAs.setStatus("mandatory")
_WfSmdsCircuitSipL3SentGAs_Type = Counter32
_WfSmdsCircuitSipL3SentGAs_Object = MibTableColumn
wfSmdsCircuitSipL3SentGAs = _WfSmdsCircuitSipL3SentGAs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 3, 1, 15),
    _WfSmdsCircuitSipL3SentGAs_Type()
)
wfSmdsCircuitSipL3SentGAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsCircuitSipL3SentGAs.setStatus("mandatory")


class _WfSmdsCircuitSipL3VersionSupport_Type(Integer32):
    """Custom type wfSmdsCircuitSipL3VersionSupport based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("version", 1)
    )


_WfSmdsCircuitSipL3VersionSupport_Type.__name__ = "Integer32"
_WfSmdsCircuitSipL3VersionSupport_Object = MibTableColumn
wfSmdsCircuitSipL3VersionSupport = _WfSmdsCircuitSipL3VersionSupport_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 3, 1, 16),
    _WfSmdsCircuitSipL3VersionSupport_Type()
)
wfSmdsCircuitSipL3VersionSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsCircuitSipL3VersionSupport.setStatus("mandatory")


class _WfSmdsCircuitDisableAddrVerify_Type(Integer32):
    """Custom type wfSmdsCircuitDisableAddrVerify based on Integer32"""
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


_WfSmdsCircuitDisableAddrVerify_Type.__name__ = "Integer32"
_WfSmdsCircuitDisableAddrVerify_Object = MibTableColumn
wfSmdsCircuitDisableAddrVerify = _WfSmdsCircuitDisableAddrVerify_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 3, 1, 17),
    _WfSmdsCircuitDisableAddrVerify_Type()
)
wfSmdsCircuitDisableAddrVerify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSmdsCircuitDisableAddrVerify.setStatus("mandatory")
_WfSmdsCircuitAddrVerifyDiscards_Type = Counter32
_WfSmdsCircuitAddrVerifyDiscards_Object = MibTableColumn
wfSmdsCircuitAddrVerifyDiscards = _WfSmdsCircuitAddrVerifyDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 3, 1, 18),
    _WfSmdsCircuitAddrVerifyDiscards_Type()
)
wfSmdsCircuitAddrVerifyDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSmdsCircuitAddrVerifyDiscards.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-SMDS-MIB",
    **{"wfSmdsCircuitTable": wfSmdsCircuitTable,
       "wfSmdsCircuitEntry": wfSmdsCircuitEntry,
       "wfSmdsCircuitDelete": wfSmdsCircuitDelete,
       "wfSmdsCircuitDisable": wfSmdsCircuitDisable,
       "wfSmdsCircuitState": wfSmdsCircuitState,
       "wfSmdsCircuitID": wfSmdsCircuitID,
       "wfSmdsCircuitIndivAddr": wfSmdsCircuitIndivAddr,
       "wfSmdsCircuitGroupAddr": wfSmdsCircuitGroupAddr,
       "wfSmdsCircuitArpAddr": wfSmdsCircuitArpAddr,
       "wfSmdsCircuitDisableHrtbtPoll": wfSmdsCircuitDisableHrtbtPoll,
       "wfSmdsCircuitHrtbtPollInterval": wfSmdsCircuitHrtbtPollInterval,
       "wfSmdsCircuitHrtbtPollDownCount": wfSmdsCircuitHrtbtPollDownCount,
       "wfSmdsCircuitDisableNetMgmt": wfSmdsCircuitDisableNetMgmt,
       "wfSmdsCircuitSipL3ReceivedIndividualDAs": wfSmdsCircuitSipL3ReceivedIndividualDAs,
       "wfSmdsCircuitSipL3ReceivedGAs": wfSmdsCircuitSipL3ReceivedGAs,
       "wfSmdsCircuitSipL3SentIndividualDAs": wfSmdsCircuitSipL3SentIndividualDAs,
       "wfSmdsCircuitSipL3SentGAs": wfSmdsCircuitSipL3SentGAs,
       "wfSmdsCircuitSipL3VersionSupport": wfSmdsCircuitSipL3VersionSupport,
       "wfSmdsCircuitDisableAddrVerify": wfSmdsCircuitDisableAddrVerify,
       "wfSmdsCircuitAddrVerifyDiscards": wfSmdsCircuitAddrVerifyDiscards}
)
