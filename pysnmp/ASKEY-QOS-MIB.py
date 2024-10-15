# SNMP MIB module (ASKEY-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASKEY-QOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:50 2024
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

(ipDslam,) = mibBuilder.importSymbols(
    "ASKEY-DSLAM-MIB",
    "ipDslam")

(askeyCosQueueMapping8021p,) = mibBuilder.importSymbols(
    "ASKEY-SYSTEM-MIB",
    "askeyCosQueueMapping8021p")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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


# MODULE-IDENTITY

askeyQoSMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 16)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AskeyQoSLineMIBObjects_ObjectIdentity = ObjectIdentity
askeyQoSLineMIBObjects = _AskeyQoSLineMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 16, 1)
)
_AskeyQoSLineTable_Object = MibTable
askeyQoSLineTable = _AskeyQoSLineTable_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 16, 1, 1)
)
if mibBuilder.loadTexts:
    askeyQoSLineTable.setStatus("current")
_AskeyQoSLineEntry_Object = MibTableRow
askeyQoSLineEntry = _AskeyQoSLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 16, 1, 1, 1)
)
askeyQoSLineEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    askeyQoSLineEntry.setStatus("current")


class _AskeyQoSLineTrafficPolicing_Type(SnmpAdminString):
    """Custom type askeyQoSLineTrafficPolicing based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AskeyQoSLineTrafficPolicing_Type.__name__ = "SnmpAdminString"
_AskeyQoSLineTrafficPolicing_Object = MibTableColumn
askeyQoSLineTrafficPolicing = _AskeyQoSLineTrafficPolicing_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 16, 1, 1, 1, 1),
    _AskeyQoSLineTrafficPolicing_Type()
)
askeyQoSLineTrafficPolicing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    askeyQoSLineTrafficPolicing.setStatus("current")
_AskeyQoSDiffServMIBObjects_ObjectIdentity = ObjectIdentity
askeyQoSDiffServMIBObjects = _AskeyQoSDiffServMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 16, 2)
)


class _DiffServAdminStatus_Type(Integer32):
    """Custom type diffServAdminStatus based on Integer32"""
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


_DiffServAdminStatus_Type.__name__ = "Integer32"
_DiffServAdminStatus_Object = MibScalar
diffServAdminStatus = _DiffServAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 16, 2, 1),
    _DiffServAdminStatus_Type()
)
diffServAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServAdminStatus.setStatus("current")
_DiffServMappingTable_Object = MibTable
diffServMappingTable = _DiffServMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 16, 2, 2)
)
if mibBuilder.loadTexts:
    diffServMappingTable.setStatus("current")
_DiffServMappingEntry_Object = MibTableRow
diffServMappingEntry = _DiffServMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 16, 2, 2, 1)
)
diffServMappingEntry.setIndexNames(
    (0, "ASKEY-SYSTEM-MIB", "askeyCosQueueMapping8021p"),
)
if mibBuilder.loadTexts:
    diffServMappingEntry.setStatus("current")


class _DiffServDSCP_Type(Integer32):
    """Custom type diffServDSCP based on Integer32"""
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
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("af11", 1),
          ("af12", 2),
          ("af13", 3),
          ("af21", 4),
          ("af22", 5),
          ("af23", 6),
          ("af31", 7),
          ("af32", 8),
          ("af33", 9),
          ("af41", 10),
          ("af42", 11),
          ("af43", 12),
          ("be", 0),
          ("ef", 13))
    )


_DiffServDSCP_Type.__name__ = "Integer32"
_DiffServDSCP_Object = MibTableColumn
diffServDSCP = _DiffServDSCP_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 16, 2, 2, 1, 1),
    _DiffServDSCP_Type()
)
diffServDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServDSCP.setStatus("current")
_AskeyQoSTrafficPolicingMIBObjects_ObjectIdentity = ObjectIdentity
askeyQoSTrafficPolicingMIBObjects = _AskeyQoSTrafficPolicingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 16, 3)
)
_TrafficPolicingTable_Object = MibTable
trafficPolicingTable = _TrafficPolicingTable_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 16, 3, 1)
)
if mibBuilder.loadTexts:
    trafficPolicingTable.setStatus("current")
_TrafficPolicingEntry_Object = MibTableRow
trafficPolicingEntry = _TrafficPolicingEntry_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 16, 3, 1, 1)
)
trafficPolicingEntry.setIndexNames(
    (1, "ASKEY-QOS-MIB", "trafficPolicingName"),
)
if mibBuilder.loadTexts:
    trafficPolicingEntry.setStatus("current")


class _TrafficPolicingName_Type(SnmpAdminString):
    """Custom type trafficPolicingName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TrafficPolicingName_Type.__name__ = "SnmpAdminString"
_TrafficPolicingName_Object = MibTableColumn
trafficPolicingName = _TrafficPolicingName_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 16, 3, 1, 1, 1),
    _TrafficPolicingName_Type()
)
trafficPolicingName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trafficPolicingName.setStatus("current")


class _TrafficPolicingCIR_Type(Integer32):
    """Custom type trafficPolicingCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_TrafficPolicingCIR_Type.__name__ = "Integer32"
_TrafficPolicingCIR_Object = MibTableColumn
trafficPolicingCIR = _TrafficPolicingCIR_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 16, 3, 1, 1, 2),
    _TrafficPolicingCIR_Type()
)
trafficPolicingCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trafficPolicingCIR.setStatus("current")


class _TrafficPolicingAction_Type(Integer32):
    """Custom type trafficPolicingAction based on Integer32"""
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
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("af11", 3),
          ("af12", 4),
          ("af13", 5),
          ("af21", 6),
          ("af22", 7),
          ("af23", 8),
          ("af31", 9),
          ("af32", 10),
          ("af33", 11),
          ("af41", 12),
          ("af42", 13),
          ("af43", 14),
          ("be", 2),
          ("drop", 1),
          ("ef", 15),
          ("noAction", 0))
    )


_TrafficPolicingAction_Type.__name__ = "Integer32"
_TrafficPolicingAction_Object = MibTableColumn
trafficPolicingAction = _TrafficPolicingAction_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 16, 3, 1, 1, 4),
    _TrafficPolicingAction_Type()
)
trafficPolicingAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trafficPolicingAction.setStatus("current")
_TrafficPolicingRowStatus_Type = RowStatus
_TrafficPolicingRowStatus_Object = MibTableColumn
trafficPolicingRowStatus = _TrafficPolicingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 16, 3, 1, 1, 5),
    _TrafficPolicingRowStatus_Type()
)
trafficPolicingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trafficPolicingRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASKEY-QOS-MIB",
    **{"askeyQoSMIB": askeyQoSMIB,
       "askeyQoSLineMIBObjects": askeyQoSLineMIBObjects,
       "askeyQoSLineTable": askeyQoSLineTable,
       "askeyQoSLineEntry": askeyQoSLineEntry,
       "askeyQoSLineTrafficPolicing": askeyQoSLineTrafficPolicing,
       "askeyQoSDiffServMIBObjects": askeyQoSDiffServMIBObjects,
       "diffServAdminStatus": diffServAdminStatus,
       "diffServMappingTable": diffServMappingTable,
       "diffServMappingEntry": diffServMappingEntry,
       "diffServDSCP": diffServDSCP,
       "askeyQoSTrafficPolicingMIBObjects": askeyQoSTrafficPolicingMIBObjects,
       "trafficPolicingTable": trafficPolicingTable,
       "trafficPolicingEntry": trafficPolicingEntry,
       "trafficPolicingName": trafficPolicingName,
       "trafficPolicingCIR": trafficPolicingCIR,
       "trafficPolicingAction": trafficPolicingAction,
       "trafficPolicingRowStatus": trafficPolicingRowStatus}
)
