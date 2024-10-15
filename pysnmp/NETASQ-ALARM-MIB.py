# SNMP MIB module (NETASQ-ALARM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETASQ-ALARM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:25:29 2024
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

(ntqAlarm,
 ntqNotifications) = mibBuilder.importSymbols(
    "NETASQ-SMI-MIB",
    "ntqAlarm",
    "ntqNotifications")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtqATable_Object = MibTable
ntqATable = _NtqATable_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 5, 0)
)
if mibBuilder.loadTexts:
    ntqATable.setStatus("current")
_NtqAEntry_Object = MibTableRow
ntqAEntry = _NtqAEntry_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1)
)
ntqAEntry.setIndexNames(
    (0, "NETASQ-ALARM-MIB", "ntqAIndex"),
)
if mibBuilder.loadTexts:
    ntqAEntry.setStatus("current")


class _NtqAIndex_Type(Integer32):
    """Custom type ntqAIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NtqAIndex_Type.__name__ = "Integer32"
_NtqAIndex_Object = MibTableColumn
ntqAIndex = _NtqAIndex_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 0),
    _NtqAIndex_Type()
)
ntqAIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntqAIndex.setStatus("current")
_NtqATime_Type = OctetString
_NtqATime_Object = MibTableColumn
ntqATime = _NtqATime_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 1),
    _NtqATime_Type()
)
ntqATime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqATime.setStatus("current")
_NtqASif_Type = OctetString
_NtqASif_Object = MibTableColumn
ntqASif = _NtqASif_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 2),
    _NtqASif_Type()
)
ntqASif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqASif.setStatus("current")
_NtqADif_Type = OctetString
_NtqADif_Object = MibTableColumn
ntqADif = _NtqADif_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 3),
    _NtqADif_Type()
)
ntqADif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqADif.setStatus("current")
_NtqAProto_Type = OctetString
_NtqAProto_Object = MibTableColumn
ntqAProto = _NtqAProto_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 4),
    _NtqAProto_Type()
)
ntqAProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqAProto.setStatus("current")
_NtqASaddr_Type = OctetString
_NtqASaddr_Object = MibTableColumn
ntqASaddr = _NtqASaddr_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 5),
    _NtqASaddr_Type()
)
ntqASaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqASaddr.setStatus("current")
_NtqADaddr_Type = OctetString
_NtqADaddr_Object = MibTableColumn
ntqADaddr = _NtqADaddr_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 6),
    _NtqADaddr_Type()
)
ntqADaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqADaddr.setStatus("current")
_NtqASport_Type = Integer32
_NtqASport_Object = MibTableColumn
ntqASport = _NtqASport_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 7),
    _NtqASport_Type()
)
ntqASport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqASport.setStatus("current")
_NtqADport_Type = Integer32
_NtqADport_Object = MibTableColumn
ntqADport = _NtqADport_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 8),
    _NtqADport_Type()
)
ntqADport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqADport.setStatus("current")
_NtqASname_Type = OctetString
_NtqASname_Object = MibTableColumn
ntqASname = _NtqASname_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 9),
    _NtqASname_Type()
)
ntqASname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqASname.setStatus("current")
_NtqADname_Type = OctetString
_NtqADname_Object = MibTableColumn
ntqADname = _NtqADname_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 10),
    _NtqADname_Type()
)
ntqADname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqADname.setStatus("current")
_NtqAMessage_Type = SnmpAdminString
_NtqAMessage_Object = MibTableColumn
ntqAMessage = _NtqAMessage_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 11),
    _NtqAMessage_Type()
)
ntqAMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqAMessage.setStatus("current")
_NtqAicmpTable_Object = MibTable
ntqAicmpTable = _NtqAicmpTable_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 5, 1)
)
if mibBuilder.loadTexts:
    ntqAicmpTable.setStatus("current")
_NtqAicmpEntry_Object = MibTableRow
ntqAicmpEntry = _NtqAicmpEntry_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1)
)
ntqAicmpEntry.setIndexNames(
    (0, "NETASQ-ALARM-MIB", "ntqAicmpIndex"),
)
if mibBuilder.loadTexts:
    ntqAicmpEntry.setStatus("current")


class _NtqAicmpIndex_Type(Integer32):
    """Custom type ntqAicmpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NtqAicmpIndex_Type.__name__ = "Integer32"
_NtqAicmpIndex_Object = MibTableColumn
ntqAicmpIndex = _NtqAicmpIndex_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1, 0),
    _NtqAicmpIndex_Type()
)
ntqAicmpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntqAicmpIndex.setStatus("current")
_NtqAicmpTime_Type = OctetString
_NtqAicmpTime_Object = MibTableColumn
ntqAicmpTime = _NtqAicmpTime_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1, 1),
    _NtqAicmpTime_Type()
)
ntqAicmpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqAicmpTime.setStatus("current")
_NtqAicmpSif_Type = OctetString
_NtqAicmpSif_Object = MibTableColumn
ntqAicmpSif = _NtqAicmpSif_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1, 2),
    _NtqAicmpSif_Type()
)
ntqAicmpSif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqAicmpSif.setStatus("current")
_NtqAicmpDif_Type = OctetString
_NtqAicmpDif_Object = MibTableColumn
ntqAicmpDif = _NtqAicmpDif_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1, 3),
    _NtqAicmpDif_Type()
)
ntqAicmpDif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqAicmpDif.setStatus("current")
_NtqAicmpSaddr_Type = OctetString
_NtqAicmpSaddr_Object = MibTableColumn
ntqAicmpSaddr = _NtqAicmpSaddr_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1, 4),
    _NtqAicmpSaddr_Type()
)
ntqAicmpSaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqAicmpSaddr.setStatus("current")
_NtqAicmpDaddr_Type = OctetString
_NtqAicmpDaddr_Object = MibTableColumn
ntqAicmpDaddr = _NtqAicmpDaddr_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1, 5),
    _NtqAicmpDaddr_Type()
)
ntqAicmpDaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqAicmpDaddr.setStatus("current")
_NtqAicmpType_Type = Integer32
_NtqAicmpType_Object = MibTableColumn
ntqAicmpType = _NtqAicmpType_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1, 6),
    _NtqAicmpType_Type()
)
ntqAicmpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqAicmpType.setStatus("current")
_NtqAicmpCode_Type = Integer32
_NtqAicmpCode_Object = MibTableColumn
ntqAicmpCode = _NtqAicmpCode_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1, 7),
    _NtqAicmpCode_Type()
)
ntqAicmpCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqAicmpCode.setStatus("current")
_NtqAicmpSname_Type = OctetString
_NtqAicmpSname_Object = MibTableColumn
ntqAicmpSname = _NtqAicmpSname_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1, 8),
    _NtqAicmpSname_Type()
)
ntqAicmpSname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqAicmpSname.setStatus("current")
_NtqAicmpDname_Type = OctetString
_NtqAicmpDname_Object = MibTableColumn
ntqAicmpDname = _NtqAicmpDname_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1, 9),
    _NtqAicmpDname_Type()
)
ntqAicmpDname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqAicmpDname.setStatus("current")
_NtqAicmpMessage_Type = SnmpAdminString
_NtqAicmpMessage_Object = MibTableColumn
ntqAicmpMessage = _NtqAicmpMessage_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1, 10),
    _NtqAicmpMessage_Type()
)
ntqAicmpMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqAicmpMessage.setStatus("current")

# Managed Objects groups


# Notification objects

ntqNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 11256, 1, 6, 1)
)
ntqNotification.setObjects(
      *(("NETASQ-ALARM-MIB", "ntqATime"),
        ("NETASQ-ALARM-MIB", "ntqASif"),
        ("NETASQ-ALARM-MIB", "ntqASaddr"),
        ("NETASQ-ALARM-MIB", "ntqADaddr"),
        ("NETASQ-ALARM-MIB", "ntqAMessage"))
)
if mibBuilder.loadTexts:
    ntqNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETASQ-ALARM-MIB",
    **{"ntqATable": ntqATable,
       "ntqAEntry": ntqAEntry,
       "ntqAIndex": ntqAIndex,
       "ntqATime": ntqATime,
       "ntqASif": ntqASif,
       "ntqADif": ntqADif,
       "ntqAProto": ntqAProto,
       "ntqASaddr": ntqASaddr,
       "ntqADaddr": ntqADaddr,
       "ntqASport": ntqASport,
       "ntqADport": ntqADport,
       "ntqASname": ntqASname,
       "ntqADname": ntqADname,
       "ntqAMessage": ntqAMessage,
       "ntqAicmpTable": ntqAicmpTable,
       "ntqAicmpEntry": ntqAicmpEntry,
       "ntqAicmpIndex": ntqAicmpIndex,
       "ntqAicmpTime": ntqAicmpTime,
       "ntqAicmpSif": ntqAicmpSif,
       "ntqAicmpDif": ntqAicmpDif,
       "ntqAicmpSaddr": ntqAicmpSaddr,
       "ntqAicmpDaddr": ntqAicmpDaddr,
       "ntqAicmpType": ntqAicmpType,
       "ntqAicmpCode": ntqAicmpCode,
       "ntqAicmpSname": ntqAicmpSname,
       "ntqAicmpDname": ntqAicmpDname,
       "ntqAicmpMessage": ntqAicmpMessage,
       "ntqNotification": ntqNotification}
)
