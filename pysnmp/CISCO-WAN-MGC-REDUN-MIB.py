# SNMP MIB module (CISCO-WAN-MGC-REDUN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WAN-MGC-REDUN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:00 2024
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

(mgProtocolNumber,
 mgcNumber) = mibBuilder.importSymbols(
    "CISCO-WAN-MG-MIB",
    "mgProtocolNumber",
    "mgcNumber")

(ciscoWan,) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "ciscoWan")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoWanMgcRedunMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 22)
)
ciscoWanMgcRedunMIB.setRevisions(
        ("2004-01-19 00:00",
         "2001-12-26 00:00",
         "2001-07-19 15:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MgcRedundancyObjects_ObjectIdentity = ObjectIdentity
mgcRedundancyObjects = _MgcRedundancyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 22, 1)
)
_MgcRedundancyGrpTable_Object = MibTable
mgcRedundancyGrpTable = _MgcRedundancyGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 22, 1, 1)
)
if mibBuilder.loadTexts:
    mgcRedundancyGrpTable.setStatus("current")
_MgcRedundancyGrpEntry_Object = MibTableRow
mgcRedundancyGrpEntry = _MgcRedundancyGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 22, 1, 1, 1)
)
mgcRedundancyGrpEntry.setIndexNames(
    (0, "CISCO-WAN-MGC-REDUN-MIB", "mgcRedundancyGrpNum"),
    (0, "CISCO-WAN-MG-MIB", "mgcNumber"),
)
if mibBuilder.loadTexts:
    mgcRedundancyGrpEntry.setStatus("current")


class _MgcRedundancyGrpNum_Type(Integer32):
    """Custom type mgcRedundancyGrpNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MgcRedundancyGrpNum_Type.__name__ = "Integer32"
_MgcRedundancyGrpNum_Object = MibTableColumn
mgcRedundancyGrpNum = _MgcRedundancyGrpNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 22, 1, 1, 1, 1),
    _MgcRedundancyGrpNum_Type()
)
mgcRedundancyGrpNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgcRedundancyGrpNum.setStatus("current")


class _MgcRedundancyGrpPref_Type(Integer32):
    """Custom type mgcRedundancyGrpPref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MgcRedundancyGrpPref_Type.__name__ = "Integer32"
_MgcRedundancyGrpPref_Object = MibTableColumn
mgcRedundancyGrpPref = _MgcRedundancyGrpPref_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 22, 1, 1, 1, 2),
    _MgcRedundancyGrpPref_Type()
)
mgcRedundancyGrpPref.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgcRedundancyGrpPref.setStatus("current")


class _MgcRedundancyGrpActState_Type(Integer32):
    """Custom type mgcRedundancyGrpActState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mgcActive", 1),
          ("mgcInactive", 2))
    )


_MgcRedundancyGrpActState_Type.__name__ = "Integer32"
_MgcRedundancyGrpActState_Object = MibTableColumn
mgcRedundancyGrpActState = _MgcRedundancyGrpActState_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 22, 1, 1, 1, 3),
    _MgcRedundancyGrpActState_Type()
)
mgcRedundancyGrpActState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgcRedundancyGrpActState.setStatus("current")
_MgcRedundancyGrpRowStatus_Type = RowStatus
_MgcRedundancyGrpRowStatus_Object = MibTableColumn
mgcRedundancyGrpRowStatus = _MgcRedundancyGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 22, 1, 1, 1, 4),
    _MgcRedundancyGrpRowStatus_Type()
)
mgcRedundancyGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgcRedundancyGrpRowStatus.setStatus("current")
_MgcRedundancyGrpParamTable_Object = MibTable
mgcRedundancyGrpParamTable = _MgcRedundancyGrpParamTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 22, 1, 2)
)
if mibBuilder.loadTexts:
    mgcRedundancyGrpParamTable.setStatus("current")
_MgcRedundancyGrpParamEntry_Object = MibTableRow
mgcRedundancyGrpParamEntry = _MgcRedundancyGrpParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 22, 1, 2, 1)
)
mgcRedundancyGrpParamEntry.setIndexNames(
    (0, "CISCO-WAN-MGC-REDUN-MIB", "mgcRedundancyGrpNum"),
)
if mibBuilder.loadTexts:
    mgcRedundancyGrpParamEntry.setStatus("current")


class _MgcRedundancyGrpStateChangeNtfy_Type(TruthValue):
    """Custom type mgcRedundancyGrpStateChangeNtfy based on TruthValue"""


_MgcRedundancyGrpStateChangeNtfy_Object = MibTableColumn
mgcRedundancyGrpStateChangeNtfy = _MgcRedundancyGrpStateChangeNtfy_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 22, 1, 2, 1, 1),
    _MgcRedundancyGrpStateChangeNtfy_Type()
)
mgcRedundancyGrpStateChangeNtfy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcRedundancyGrpStateChangeNtfy.setStatus("current")


class _MgcRedundancyGrpCommState_Type(Integer32):
    """Custom type mgcRedundancyGrpCommState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("commLoss", 2),
          ("commOk", 1))
    )


_MgcRedundancyGrpCommState_Type.__name__ = "Integer32"
_MgcRedundancyGrpCommState_Object = MibTableColumn
mgcRedundancyGrpCommState = _MgcRedundancyGrpCommState_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 22, 1, 2, 1, 2),
    _MgcRedundancyGrpCommState_Type()
)
mgcRedundancyGrpCommState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgcRedundancyGrpCommState.setStatus("current")


class _MgcRedundancyGrpPriority_Type(Integer32):
    """Custom type mgcRedundancyGrpPriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MgcRedundancyGrpPriority_Type.__name__ = "Integer32"
_MgcRedundancyGrpPriority_Object = MibTableColumn
mgcRedundancyGrpPriority = _MgcRedundancyGrpPriority_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 22, 1, 2, 1, 3),
    _MgcRedundancyGrpPriority_Type()
)
mgcRedundancyGrpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcRedundancyGrpPriority.setStatus("current")
_MgcRedundancyGrpProtocolTable_Object = MibTable
mgcRedundancyGrpProtocolTable = _MgcRedundancyGrpProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 22, 1, 3)
)
if mibBuilder.loadTexts:
    mgcRedundancyGrpProtocolTable.setStatus("current")
_MgcRedundancyGrpProtocolEntry_Object = MibTableRow
mgcRedundancyGrpProtocolEntry = _MgcRedundancyGrpProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 22, 1, 3, 1)
)
mgcRedundancyGrpProtocolEntry.setIndexNames(
    (0, "CISCO-WAN-MGC-REDUN-MIB", "mgcRedundancyGrpNum"),
    (0, "CISCO-WAN-MG-MIB", "mgProtocolNumber"),
)
if mibBuilder.loadTexts:
    mgcRedundancyGrpProtocolEntry.setStatus("current")
_MgcRedundancyGrpProtocolRowStatus_Type = RowStatus
_MgcRedundancyGrpProtocolRowStatus_Object = MibTableColumn
mgcRedundancyGrpProtocolRowStatus = _MgcRedundancyGrpProtocolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 22, 1, 3, 1, 1),
    _MgcRedundancyGrpProtocolRowStatus_Type()
)
mgcRedundancyGrpProtocolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgcRedundancyGrpProtocolRowStatus.setStatus("current")


class _MgcRedGrpProtPersistEvtPolicy_Type(Integer32):
    """Custom type mgcRedGrpProtPersistEvtPolicy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notQuarantinePersistEvts", 2),
          ("quarantinePersistEvts", 1))
    )


_MgcRedGrpProtPersistEvtPolicy_Type.__name__ = "Integer32"
_MgcRedGrpProtPersistEvtPolicy_Object = MibTableColumn
mgcRedGrpProtPersistEvtPolicy = _MgcRedGrpProtPersistEvtPolicy_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 22, 1, 3, 1, 2),
    _MgcRedGrpProtPersistEvtPolicy_Type()
)
mgcRedGrpProtPersistEvtPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgcRedGrpProtPersistEvtPolicy.setStatus("current")


class _MgcRedGrpProtQuarantinePolicy_Type(Integer32):
    """Custom type mgcRedGrpProtQuarantinePolicy based on Integer32"""
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
        *(("loopDiscard", 4),
          ("loopProcess", 3),
          ("stepDiscard", 2),
          ("stepProcess", 1))
    )


_MgcRedGrpProtQuarantinePolicy_Type.__name__ = "Integer32"
_MgcRedGrpProtQuarantinePolicy_Object = MibTableColumn
mgcRedGrpProtQuarantinePolicy = _MgcRedGrpProtQuarantinePolicy_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 22, 1, 3, 1, 3),
    _MgcRedGrpProtQuarantinePolicy_Type()
)
mgcRedGrpProtQuarantinePolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgcRedGrpProtQuarantinePolicy.setStatus("current")


class _MgcRedGrpProtSigEvtOnOffPolicy_Type(Integer32):
    """Custom type mgcRedGrpProtSigEvtOnOffPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deleteEventNotPresent", 1),
          ("deleteOnlyNegatedEvent", 2))
    )


_MgcRedGrpProtSigEvtOnOffPolicy_Type.__name__ = "Integer32"
_MgcRedGrpProtSigEvtOnOffPolicy_Object = MibTableColumn
mgcRedGrpProtSigEvtOnOffPolicy = _MgcRedGrpProtSigEvtOnOffPolicy_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 22, 1, 3, 1, 4),
    _MgcRedGrpProtSigEvtOnOffPolicy_Type()
)
mgcRedGrpProtSigEvtOnOffPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgcRedGrpProtSigEvtOnOffPolicy.setStatus("current")


class _MgcRedGrpProtProvisionalResponse_Type(Integer32):
    """Custom type mgcRedGrpProtProvisionalResponse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSendProvisionalResponse", 2),
          ("sendProvisionalResponse", 1))
    )


_MgcRedGrpProtProvisionalResponse_Type.__name__ = "Integer32"
_MgcRedGrpProtProvisionalResponse_Object = MibTableColumn
mgcRedGrpProtProvisionalResponse = _MgcRedGrpProtProvisionalResponse_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 22, 1, 3, 1, 5),
    _MgcRedGrpProtProvisionalResponse_Type()
)
mgcRedGrpProtProvisionalResponse.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgcRedGrpProtProvisionalResponse.setStatus("current")


class _MgcRedGrpProtResponseAckAttr_Type(Integer32):
    """Custom type mgcRedGrpProtResponseAckAttr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSendResponseAckAttr", 2),
          ("sendResponseAckAttr", 1))
    )


_MgcRedGrpProtResponseAckAttr_Type.__name__ = "Integer32"
_MgcRedGrpProtResponseAckAttr_Object = MibTableColumn
mgcRedGrpProtResponseAckAttr = _MgcRedGrpProtResponseAckAttr_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 22, 1, 3, 1, 6),
    _MgcRedGrpProtResponseAckAttr_Type()
)
mgcRedGrpProtResponseAckAttr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgcRedGrpProtResponseAckAttr.setStatus("current")


class _MgcRedGrpProtDisconnectProcedure_Type(Integer32):
    """Custom type mgcRedGrpProtDisconnectProcedure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doDisconnectProcedure", 1),
          ("notDoDisconnectProcedure", 2))
    )


_MgcRedGrpProtDisconnectProcedure_Type.__name__ = "Integer32"
_MgcRedGrpProtDisconnectProcedure_Object = MibTableColumn
mgcRedGrpProtDisconnectProcedure = _MgcRedGrpProtDisconnectProcedure_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 22, 1, 3, 1, 7),
    _MgcRedGrpProtDisconnectProcedure_Type()
)
mgcRedGrpProtDisconnectProcedure.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgcRedGrpProtDisconnectProcedure.setStatus("current")


class _MgcRedGrpProtCancelGraceful_Type(Integer32):
    """Custom type mgcRedGrpProtCancelGraceful based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSendCancelGraceful", 2),
          ("sendCancelGraceful", 1))
    )


_MgcRedGrpProtCancelGraceful_Type.__name__ = "Integer32"
_MgcRedGrpProtCancelGraceful_Object = MibTableColumn
mgcRedGrpProtCancelGraceful = _MgcRedGrpProtCancelGraceful_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 22, 1, 3, 1, 8),
    _MgcRedGrpProtCancelGraceful_Type()
)
mgcRedGrpProtCancelGraceful.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgcRedGrpProtCancelGraceful.setStatus("current")
_MgcRedunNotificationPrefix_ObjectIdentity = ObjectIdentity
mgcRedunNotificationPrefix = _MgcRedunNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 22, 2)
)
_MgcRedunNotifications_ObjectIdentity = ObjectIdentity
mgcRedunNotifications = _MgcRedunNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 22, 2, 0)
)
_MgcRedunMIBConformance_ObjectIdentity = ObjectIdentity
mgcRedunMIBConformance = _MgcRedunMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 22, 3)
)
_MgcRedunMIBCompliances_ObjectIdentity = ObjectIdentity
mgcRedunMIBCompliances = _MgcRedunMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 22, 3, 1)
)
_MgcRedunMIBGroups_ObjectIdentity = ObjectIdentity
mgcRedunMIBGroups = _MgcRedunMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 22, 3, 2)
)

# Managed Objects groups

mgcRedundancyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 22, 3, 2, 1)
)
mgcRedundancyGroup.setObjects(
      *(("CISCO-WAN-MGC-REDUN-MIB", "mgcRedundancyGrpPref"),
        ("CISCO-WAN-MGC-REDUN-MIB", "mgcRedundancyGrpActState"),
        ("CISCO-WAN-MGC-REDUN-MIB", "mgcRedundancyGrpRowStatus"))
)
if mibBuilder.loadTexts:
    mgcRedundancyGroup.setStatus("current")

mgcRedundancyParamGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 22, 3, 2, 2)
)
mgcRedundancyParamGroup.setObjects(
      *(("CISCO-WAN-MGC-REDUN-MIB", "mgcRedundancyGrpStateChangeNtfy"),
        ("CISCO-WAN-MGC-REDUN-MIB", "mgcRedundancyGrpCommState"),
        ("CISCO-WAN-MGC-REDUN-MIB", "mgcRedundancyGrpPriority"))
)
if mibBuilder.loadTexts:
    mgcRedundancyParamGroup.setStatus("current")

mgcRedundancyProtocolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 22, 3, 2, 3)
)
mgcRedundancyProtocolGroup.setObjects(
      *(("CISCO-WAN-MGC-REDUN-MIB", "mgcRedundancyGrpProtocolRowStatus"),
        ("CISCO-WAN-MGC-REDUN-MIB", "mgcRedGrpProtPersistEvtPolicy"),
        ("CISCO-WAN-MGC-REDUN-MIB", "mgcRedGrpProtQuarantinePolicy"),
        ("CISCO-WAN-MGC-REDUN-MIB", "mgcRedGrpProtSigEvtOnOffPolicy"),
        ("CISCO-WAN-MGC-REDUN-MIB", "mgcRedGrpProtProvisionalResponse"),
        ("CISCO-WAN-MGC-REDUN-MIB", "mgcRedGrpProtResponseAckAttr"),
        ("CISCO-WAN-MGC-REDUN-MIB", "mgcRedGrpProtDisconnectProcedure"),
        ("CISCO-WAN-MGC-REDUN-MIB", "mgcRedGrpProtCancelGraceful"))
)
if mibBuilder.loadTexts:
    mgcRedundancyProtocolGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mgcRedunMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 22, 3, 1, 1)
)
if mibBuilder.loadTexts:
    mgcRedunMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WAN-MGC-REDUN-MIB",
    **{"ciscoWanMgcRedunMIB": ciscoWanMgcRedunMIB,
       "mgcRedundancyObjects": mgcRedundancyObjects,
       "mgcRedundancyGrpTable": mgcRedundancyGrpTable,
       "mgcRedundancyGrpEntry": mgcRedundancyGrpEntry,
       "mgcRedundancyGrpNum": mgcRedundancyGrpNum,
       "mgcRedundancyGrpPref": mgcRedundancyGrpPref,
       "mgcRedundancyGrpActState": mgcRedundancyGrpActState,
       "mgcRedundancyGrpRowStatus": mgcRedundancyGrpRowStatus,
       "mgcRedundancyGrpParamTable": mgcRedundancyGrpParamTable,
       "mgcRedundancyGrpParamEntry": mgcRedundancyGrpParamEntry,
       "mgcRedundancyGrpStateChangeNtfy": mgcRedundancyGrpStateChangeNtfy,
       "mgcRedundancyGrpCommState": mgcRedundancyGrpCommState,
       "mgcRedundancyGrpPriority": mgcRedundancyGrpPriority,
       "mgcRedundancyGrpProtocolTable": mgcRedundancyGrpProtocolTable,
       "mgcRedundancyGrpProtocolEntry": mgcRedundancyGrpProtocolEntry,
       "mgcRedundancyGrpProtocolRowStatus": mgcRedundancyGrpProtocolRowStatus,
       "mgcRedGrpProtPersistEvtPolicy": mgcRedGrpProtPersistEvtPolicy,
       "mgcRedGrpProtQuarantinePolicy": mgcRedGrpProtQuarantinePolicy,
       "mgcRedGrpProtSigEvtOnOffPolicy": mgcRedGrpProtSigEvtOnOffPolicy,
       "mgcRedGrpProtProvisionalResponse": mgcRedGrpProtProvisionalResponse,
       "mgcRedGrpProtResponseAckAttr": mgcRedGrpProtResponseAckAttr,
       "mgcRedGrpProtDisconnectProcedure": mgcRedGrpProtDisconnectProcedure,
       "mgcRedGrpProtCancelGraceful": mgcRedGrpProtCancelGraceful,
       "mgcRedunNotificationPrefix": mgcRedunNotificationPrefix,
       "mgcRedunNotifications": mgcRedunNotifications,
       "mgcRedunMIBConformance": mgcRedunMIBConformance,
       "mgcRedunMIBCompliances": mgcRedunMIBCompliances,
       "mgcRedunMIBCompliance": mgcRedunMIBCompliance,
       "mgcRedunMIBGroups": mgcRedunMIBGroups,
       "mgcRedundancyGroup": mgcRedundancyGroup,
       "mgcRedundancyParamGroup": mgcRedundancyParamGroup,
       "mgcRedundancyProtocolGroup": mgcRedundancyProtocolGroup}
)
