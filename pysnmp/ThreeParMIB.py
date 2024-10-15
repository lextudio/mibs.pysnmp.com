# SNMP MIB module (ThreeParMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ThreeParMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:08:09 2024
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

(AgentCapabilities,
 ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "AgentCapabilities",
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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

threepar = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12925)
)
threepar.setRevisions(
        ("2013-03-12 11:22",
         "2012-08-02 15:22",
         "2010-10-04 14:45",
         "2007-10-05 15:00",
         "2004-12-13 17:00",
         "2004-12-13 16:40",
         "2004-06-14 15:45",
         "2002-04-16 13:27")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ThreeparLongDisplayString(OctetString, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Inserv_ObjectIdentity = ObjectIdentity
inserv = _Inserv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12925, 1)
)
if mibBuilder.loadTexts:
    inserv.setStatus("current")
_InservAgentCaps_ObjectIdentity = ObjectIdentity
inservAgentCaps = _InservAgentCaps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12925, 1, 4)
)
if mibBuilder.loadTexts:
    inservAgentCaps.setStatus("current")
_AlertTable_Object = MibTable
alertTable = _AlertTable_Object(
    (1, 3, 6, 1, 4, 1, 12925, 1, 7)
)
if mibBuilder.loadTexts:
    alertTable.setStatus("current")
_AlertEntry_Object = MibTableRow
alertEntry = _AlertEntry_Object(
    (1, 3, 6, 1, 4, 1, 12925, 1, 7, 1)
)
alertEntry.setIndexNames(
    (0, "ThreeParMIB", "index"),
)
if mibBuilder.loadTexts:
    alertEntry.setStatus("current")


class _Index_Type(Integer32):
    """Custom type index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Index_Type.__name__ = "Integer32"
_Index_Object = MibTableColumn
index = _Index_Object(
    (1, 3, 6, 1, 4, 1, 12925, 1, 7, 1, 1),
    _Index_Type()
)
index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    index.setStatus("current")


class _Severity_Type(Integer32):
    """Custom type severity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("debug", 6),
          ("degraded", 4),
          ("fatal", 0),
          ("info", 5),
          ("major", 2),
          ("minor", 3))
    )


_Severity_Type.__name__ = "Integer32"
_Severity_Object = MibTableColumn
severity = _Severity_Object(
    (1, 3, 6, 1, 4, 1, 12925, 1, 7, 1, 2),
    _Severity_Type()
)
severity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    severity.setStatus("current")
_TimeOccurred_Type = DisplayString
_TimeOccurred_Object = MibTableColumn
timeOccurred = _TimeOccurred_Object(
    (1, 3, 6, 1, 4, 1, 12925, 1, 7, 1, 3),
    _TimeOccurred_Type()
)
timeOccurred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeOccurred.setStatus("current")


class _NodeID_Type(Unsigned32):
    """Custom type nodeID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_NodeID_Type.__name__ = "Unsigned32"
_NodeID_Object = MibTableColumn
nodeID = _NodeID_Object(
    (1, 3, 6, 1, 4, 1, 12925, 1, 7, 1, 4),
    _NodeID_Type()
)
nodeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeID.setStatus("current")


class _Component_Type(DisplayString):
    """Custom type component based on DisplayString"""
    defaultValue = OctetString("1")


_Component_Object = MibTableColumn
component = _Component_Object(
    (1, 3, 6, 1, 4, 1, 12925, 1, 7, 1, 5),
    _Component_Type()
)
component.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component.setStatus("current")


class _Details_Type(ThreeparLongDisplayString):
    """Custom type details based on ThreeparLongDisplayString"""
    subtypeSpec = ThreeparLongDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 511),
    )


_Details_Type.__name__ = "ThreeparLongDisplayString"
_Details_Object = MibTableColumn
details = _Details_Object(
    (1, 3, 6, 1, 4, 1, 12925, 1, 7, 1, 6),
    _Details_Type()
)
details.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    details.setStatus("current")


class _Id_Type(Unsigned32):
    """Custom type id based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Id_Type.__name__ = "Unsigned32"
_Id_Object = MibTableColumn
id = _Id_Object(
    (1, 3, 6, 1, 4, 1, 12925, 1, 7, 1, 7),
    _Id_Type()
)
id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    id.setStatus("current")


class _MessageCode_Type(Unsigned32):
    """Custom type messageCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(65537, 4294967295),
    )


_MessageCode_Type.__name__ = "Unsigned32"
_MessageCode_Object = MibTableColumn
messageCode = _MessageCode_Object(
    (1, 3, 6, 1, 4, 1, 12925, 1, 7, 1, 8),
    _MessageCode_Type()
)
messageCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    messageCode.setStatus("current")


class _State_Type(Integer32):
    """Custom type state based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("acknowledged", 2),
          ("autofixed", 5),
          ("fixed", 3),
          ("new", 1),
          ("removed", 4),
          ("undefined", 0))
    )


_State_Type.__name__ = "Integer32"
_State_Object = MibTableColumn
state = _State_Object(
    (1, 3, 6, 1, 4, 1, 12925, 1, 7, 1, 9),
    _State_Type()
)
state.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    state.setStatus("current")
_SerialNumber_Type = DisplayString
_SerialNumber_Object = MibTableColumn
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 12925, 1, 7, 1, 10),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("current")

# Managed Objects groups


# Notification objects

alertNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 12925, 1, 8)
)
alertNotify.setObjects(
      *(("ThreeParMIB", "component"),
        ("ThreeParMIB", "details"),
        ("ThreeParMIB", "nodeID"),
        ("ThreeParMIB", "severity"),
        ("ThreeParMIB", "timeOccurred"),
        ("ThreeParMIB", "id"),
        ("ThreeParMIB", "messageCode"),
        ("ThreeParMIB", "state"),
        ("ThreeParMIB", "serialNumber"))
)
if mibBuilder.loadTexts:
    alertNotify.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities

inservAgentCapability = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 12925, 1, 4, 1)
)
if mibBuilder.loadTexts:
    inservAgentCapability.setProductRelease("InServ Release 2.2")
if mibBuilder.loadTexts:
    inservAgentCapability.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ThreeParMIB",
    **{"ThreeparLongDisplayString": ThreeparLongDisplayString,
       "threepar": threepar,
       "inserv": inserv,
       "inservAgentCaps": inservAgentCaps,
       "inservAgentCapability": inservAgentCapability,
       "alertTable": alertTable,
       "alertEntry": alertEntry,
       "index": index,
       "severity": severity,
       "timeOccurred": timeOccurred,
       "nodeID": nodeID,
       "component": component,
       "details": details,
       "id": id,
       "messageCode": messageCode,
       "state": state,
       "serialNumber": serialNumber,
       "alertNotify": alertNotify}
)
