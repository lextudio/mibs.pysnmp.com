# SNMP MIB module (EDIAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EDIAL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:36:35 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

edial = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 19631)
)
edial.setRevisions(
        ("2004-02-25 20:00",
         "2005-10-03 21:44")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Common_ObjectIdentity = ObjectIdentity
common = _Common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19631, 1)
)
_SystemFaults_ObjectIdentity = ObjectIdentity
systemFaults = _SystemFaults_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19631, 1, 1)
)
_FaultFields_ObjectIdentity = ObjectIdentity
faultFields = _FaultFields_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19631, 1, 1, 1)
)
_TimeStamp_Type = DateAndTime
_TimeStamp_Object = MibScalar
timeStamp = _TimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 19631, 1, 1, 1, 2),
    _TimeStamp_Type()
)
timeStamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    timeStamp.setStatus("current")
_MsgString_Type = DisplayString
_MsgString_Object = MibScalar
msgString = _MsgString_Object(
    (1, 3, 6, 1, 4, 1, 19631, 1, 1, 1, 3),
    _MsgString_Type()
)
msgString.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    msgString.setStatus("current")
_SystemName_Type = DisplayString
_SystemName_Object = MibScalar
systemName = _SystemName_Object(
    (1, 3, 6, 1, 4, 1, 19631, 1, 1, 1, 4),
    _SystemName_Type()
)
systemName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    systemName.setStatus("current")
_ProblemText_Type = DisplayString
_ProblemText_Object = MibScalar
problemText = _ProblemText_Object(
    (1, 3, 6, 1, 4, 1, 19631, 1, 1, 1, 9),
    _ProblemText_Type()
)
problemText.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    problemText.setStatus("current")

# Managed Objects groups


# Notification objects

notification = NotificationType(
    (1, 3, 6, 1, 4, 1, 19631, 1, 1, 2)
)
notification.setObjects(
      *(("EDIAL-MIB", "timeStamp"),
        ("EDIAL-MIB", "msgString"),
        ("EDIAL-MIB", "systemName"),
        ("EDIAL-MIB", "problemText"))
)
if mibBuilder.loadTexts:
    notification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EDIAL-MIB",
    **{"edial": edial,
       "common": common,
       "systemFaults": systemFaults,
       "faultFields": faultFields,
       "timeStamp": timeStamp,
       "msgString": msgString,
       "systemName": systemName,
       "problemText": problemText,
       "notification": notification}
)
