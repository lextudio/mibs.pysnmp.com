# SNMP MIB module (TUBS-TNM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TUBS-TNM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:08:02 2024
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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 RowStatus,
 TAddress,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

tnmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1575, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class URL(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_TnmStatus_ObjectIdentity = ObjectIdentity
tnmStatus = _TnmStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1575, 1, 1, 1)
)
_TnmVersion_Type = DisplayString
_TnmVersion_Object = MibScalar
tnmVersion = _TnmVersion_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 1, 1, 1),
    _TnmVersion_Type()
)
tnmVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnmVersion.setStatus("current")
_TnmTclVersion_Type = DisplayString
_TnmTclVersion_Object = MibScalar
tnmTclVersion = _TnmTclVersion_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 1, 1, 2),
    _TnmTclVersion_Type()
)
tnmTclVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnmTclVersion.setStatus("current")
_TnmTclCmdCount_Type = Counter32
_TnmTclCmdCount_Object = MibScalar
tnmTclCmdCount = _TnmTclCmdCount_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 1, 1, 3),
    _TnmTclCmdCount_Type()
)
tnmTclCmdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnmTclCmdCount.setStatus("current")
_TnmDate_Type = DateAndTime
_TnmDate_Object = MibScalar
tnmDate = _TnmDate_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 1, 1, 4),
    _TnmDate_Type()
)
tnmDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnmDate.setStatus("current")
_TnmTrapDst_Type = DisplayString
_TnmTrapDst_Object = MibScalar
tnmTrapDst = _TnmTrapDst_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 1, 1, 5),
    _TnmTrapDst_Type()
)
tnmTrapDst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnmTrapDst.setStatus("current")
_TnmTrapMsg_Type = DisplayString
_TnmTrapMsg_Object = MibScalar
tnmTrapMsg = _TnmTrapMsg_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 1, 1, 6),
    _TnmTrapMsg_Type()
)
tnmTrapMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnmTrapMsg.setStatus("current")
_TnmDownload_ObjectIdentity = ObjectIdentity
tnmDownload = _TnmDownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1575, 1, 1, 2)
)
_TnmHttpProxy_Type = DisplayString
_TnmHttpProxy_Object = MibScalar
tnmHttpProxy = _TnmHttpProxy_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 1, 2, 1),
    _TnmHttpProxy_Type()
)
tnmHttpProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnmHttpProxy.setStatus("current")
_TnmHttpSource_Type = URL
_TnmHttpSource_Object = MibScalar
tnmHttpSource = _TnmHttpSource_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 1, 2, 2),
    _TnmHttpSource_Type()
)
tnmHttpSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnmHttpSource.setStatus("current")
_TnmHttpError_Type = DisplayString
_TnmHttpError_Object = MibScalar
tnmHttpError = _TnmHttpError_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 1, 2, 3),
    _TnmHttpError_Type()
)
tnmHttpError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnmHttpError.setStatus("current")
_TnmPeers_ObjectIdentity = ObjectIdentity
tnmPeers = _TnmPeers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1575, 1, 1, 3)
)
_TnmPeerTable_Object = MibTable
tnmPeerTable = _TnmPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    tnmPeerTable.setStatus("current")
_TnmPeerEntry_Object = MibTableRow
tnmPeerEntry = _TnmPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 1, 3, 1, 1)
)
tnmPeerEntry.setIndexNames(
    (0, "TUBS-TNM-MIB", "tnmPeerTAddress"),
)
if mibBuilder.loadTexts:
    tnmPeerEntry.setStatus("current")
_TnmPeerTAddress_Type = TAddress
_TnmPeerTAddress_Object = MibTableColumn
tnmPeerTAddress = _TnmPeerTAddress_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 1, 3, 1, 1, 1),
    _TnmPeerTAddress_Type()
)
tnmPeerTAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnmPeerTAddress.setStatus("current")
_TnmPeerAuth_Type = OctetString
_TnmPeerAuth_Object = MibTableColumn
tnmPeerAuth = _TnmPeerAuth_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 1, 3, 1, 1, 2),
    _TnmPeerAuth_Type()
)
tnmPeerAuth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnmPeerAuth.setStatus("current")


class _TnmPeerState_Type(Integer32):
    """Custom type tnmPeerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_TnmPeerState_Type.__name__ = "Integer32"
_TnmPeerState_Object = MibTableColumn
tnmPeerState = _TnmPeerState_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 1, 3, 1, 1, 3),
    _TnmPeerState_Type()
)
tnmPeerState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnmPeerState.setStatus("current")
_TnmPeerLastChecked_Type = TimeStamp
_TnmPeerLastChecked_Object = MibTableColumn
tnmPeerLastChecked = _TnmPeerLastChecked_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 1, 3, 1, 1, 4),
    _TnmPeerLastChecked_Type()
)
tnmPeerLastChecked.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnmPeerLastChecked.setStatus("current")


class _TnmPeerStatus_Type(RowStatus):
    """Custom type tnmPeerStatus based on RowStatus"""


_TnmPeerStatus_Object = MibTableColumn
tnmPeerStatus = _TnmPeerStatus_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 1, 3, 1, 1, 5),
    _TnmPeerStatus_Type()
)
tnmPeerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnmPeerStatus.setStatus("current")
_TnmElection_ObjectIdentity = ObjectIdentity
tnmElection = _TnmElection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1575, 1, 1, 4)
)
_TnmElectionIndex_Type = Unsigned32
_TnmElectionIndex_Object = MibScalar
tnmElectionIndex = _TnmElectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 1, 4, 1),
    _TnmElectionIndex_Type()
)
tnmElectionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnmElectionIndex.setStatus("current")
_TnmElectionPanic_Type = TruthValue
_TnmElectionPanic_Object = MibScalar
tnmElectionPanic = _TnmElectionPanic_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 1, 4, 2),
    _TnmElectionPanic_Type()
)
tnmElectionPanic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnmElectionPanic.setStatus("current")
_TnmElectionMaster_Type = TAddress
_TnmElectionMaster_Object = MibScalar
tnmElectionMaster = _TnmElectionMaster_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 1, 4, 3),
    _TnmElectionMaster_Type()
)
tnmElectionMaster.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnmElectionMaster.setStatus("current")
_TnmEval_ObjectIdentity = ObjectIdentity
tnmEval = _TnmEval_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1575, 1, 1, 5)
)
_TnmEvalSlot_Type = Integer32
_TnmEvalSlot_Object = MibScalar
tnmEvalSlot = _TnmEvalSlot_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 1, 5, 1),
    _TnmEvalSlot_Type()
)
tnmEvalSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnmEvalSlot.setStatus("current")
_TnmEvalTable_Object = MibTable
tnmEvalTable = _TnmEvalTable_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 1, 5, 2)
)
if mibBuilder.loadTexts:
    tnmEvalTable.setStatus("current")
_TnmEvalEntry_Object = MibTableRow
tnmEvalEntry = _TnmEvalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 1, 5, 2, 1)
)
tnmEvalEntry.setIndexNames(
    (0, "TUBS-TNM-MIB", "tnmEvalIndex"),
)
if mibBuilder.loadTexts:
    tnmEvalEntry.setStatus("current")
_TnmEvalIndex_Type = Integer32
_TnmEvalIndex_Object = MibTableColumn
tnmEvalIndex = _TnmEvalIndex_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 1, 5, 2, 1, 1),
    _TnmEvalIndex_Type()
)
tnmEvalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnmEvalIndex.setStatus("current")
_TnmEvalString_Type = DisplayString
_TnmEvalString_Object = MibTableColumn
tnmEvalString = _TnmEvalString_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 1, 5, 2, 1, 2),
    _TnmEvalString_Type()
)
tnmEvalString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnmEvalString.setStatus("current")
_TnmEvalValue_Type = DisplayString
_TnmEvalValue_Object = MibTableColumn
tnmEvalValue = _TnmEvalValue_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 1, 5, 2, 1, 3),
    _TnmEvalValue_Type()
)
tnmEvalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnmEvalValue.setStatus("current")


class _TnmEvalStatus_Type(RowStatus):
    """Custom type tnmEvalStatus based on RowStatus"""


_TnmEvalStatus_Object = MibTableColumn
tnmEvalStatus = _TnmEvalStatus_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 1, 5, 2, 1, 4),
    _TnmEvalStatus_Type()
)
tnmEvalStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnmEvalStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TUBS-TNM-MIB",
    **{"URL": URL,
       "tnmMIB": tnmMIB,
       "tnmStatus": tnmStatus,
       "tnmVersion": tnmVersion,
       "tnmTclVersion": tnmTclVersion,
       "tnmTclCmdCount": tnmTclCmdCount,
       "tnmDate": tnmDate,
       "tnmTrapDst": tnmTrapDst,
       "tnmTrapMsg": tnmTrapMsg,
       "tnmDownload": tnmDownload,
       "tnmHttpProxy": tnmHttpProxy,
       "tnmHttpSource": tnmHttpSource,
       "tnmHttpError": tnmHttpError,
       "tnmPeers": tnmPeers,
       "tnmPeerTable": tnmPeerTable,
       "tnmPeerEntry": tnmPeerEntry,
       "tnmPeerTAddress": tnmPeerTAddress,
       "tnmPeerAuth": tnmPeerAuth,
       "tnmPeerState": tnmPeerState,
       "tnmPeerLastChecked": tnmPeerLastChecked,
       "tnmPeerStatus": tnmPeerStatus,
       "tnmElection": tnmElection,
       "tnmElectionIndex": tnmElectionIndex,
       "tnmElectionPanic": tnmElectionPanic,
       "tnmElectionMaster": tnmElectionMaster,
       "tnmEval": tnmEval,
       "tnmEvalSlot": tnmEvalSlot,
       "tnmEvalTable": tnmEvalTable,
       "tnmEvalEntry": tnmEvalEntry,
       "tnmEvalIndex": tnmEvalIndex,
       "tnmEvalString": tnmEvalString,
       "tnmEvalValue": tnmEvalValue,
       "tnmEvalStatus": tnmEvalStatus}
)
