# SNMP MIB module (WS-INFRA-NTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WS-INFRA-NTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:28 2024
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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")

(wsInfraNTP,) = mibBuilder.importSymbols(
    "WS-INFRA-SMI-MIB",
    "wsInfraNTP")


# MODULE-IDENTITY

wsInfraNTPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 10, 1)
)
wsInfraNTPMIB.setRevisions(
        ("2006-05-26 12:37",
         "2005-10-12 14:21",
         "2005-08-12 13:58",
         "2005-06-28 11:58",
         "2005-06-27 14:34",
         "2005-06-24 12:07",
         "2005-06-23 13:17",
         "2005-06-22 10:34",
         "2005-06-20 11:05",
         "2005-06-09 15:24",
         "2005-06-07 18:43",
         "2005-05-04 16:13",
         "2005-05-04 10:58")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WsInfraNtpEnable_Type = TruthValue
_WsInfraNtpEnable_Object = MibScalar
wsInfraNtpEnable = _WsInfraNtpEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 10, 1, 1),
    _WsInfraNtpEnable_Type()
)
wsInfraNtpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraNtpEnable.setStatus("obsolete")
_WsInfraNtp1Server_Type = IpAddress
_WsInfraNtp1Server_Object = MibScalar
wsInfraNtp1Server = _WsInfraNtp1Server_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 10, 1, 2),
    _WsInfraNtp1Server_Type()
)
wsInfraNtp1Server.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraNtp1Server.setStatus("obsolete")
_WsInfraNtp2Server_Type = IpAddress
_WsInfraNtp2Server_Object = MibScalar
wsInfraNtp2Server = _WsInfraNtp2Server_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 10, 1, 3),
    _WsInfraNtp2Server_Type()
)
wsInfraNtp2Server.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraNtp2Server.setStatus("obsolete")
_WsInfraNtp3Server_Type = IpAddress
_WsInfraNtp3Server_Object = MibScalar
wsInfraNtp3Server = _WsInfraNtp3Server_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 10, 1, 4),
    _WsInfraNtp3Server_Type()
)
wsInfraNtp3Server.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraNtp3Server.setStatus("obsolete")
_WsInfraNtpTimeZone_Type = DisplayString
_WsInfraNtpTimeZone_Object = MibScalar
wsInfraNtpTimeZone = _WsInfraNtpTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 10, 1, 5),
    _WsInfraNtpTimeZone_Type()
)
wsInfraNtpTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraNtpTimeZone.setStatus("current")
_WsInfraNtpCurrentDateTime_Type = DateAndTime
_WsInfraNtpCurrentDateTime_Object = MibScalar
wsInfraNtpCurrentDateTime = _WsInfraNtpCurrentDateTime_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 10, 1, 6),
    _WsInfraNtpCurrentDateTime_Type()
)
wsInfraNtpCurrentDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraNtpCurrentDateTime.setStatus("current")


class _WsInfraNtpAllTimeZones_Type(OctetString):
    """Custom type wsInfraNtpAllTimeZones based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5000),
    )


_WsInfraNtpAllTimeZones_Type.__name__ = "OctetString"
_WsInfraNtpAllTimeZones_Object = MibScalar
wsInfraNtpAllTimeZones = _WsInfraNtpAllTimeZones_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 10, 1, 7),
    _WsInfraNtpAllTimeZones_Type()
)
wsInfraNtpAllTimeZones.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraNtpAllTimeZones.setStatus("current")
_WsInfraNTPMIBConformance_ObjectIdentity = ObjectIdentity
wsInfraNTPMIBConformance = _WsInfraNTPMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 10, 1, 100)
)
_WsInfraNTPMIBGroups_ObjectIdentity = ObjectIdentity
wsInfraNTPMIBGroups = _WsInfraNTPMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 10, 1, 100, 1)
)
_WsInfraNTPMIBCompliances_ObjectIdentity = ObjectIdentity
wsInfraNTPMIBCompliances = _WsInfraNTPMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 10, 1, 100, 2)
)

# Managed Objects groups

wsInfraNTPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 10, 1, 100, 1, 1)
)
wsInfraNTPGroup.setObjects(
      *(("WS-INFRA-NTP-MIB", "wsInfraNtpAllTimeZones"),
        ("WS-INFRA-NTP-MIB", "wsInfraNtpCurrentDateTime"),
        ("WS-INFRA-NTP-MIB", "wsInfraNtpTimeZone"))
)
if mibBuilder.loadTexts:
    wsInfraNTPGroup.setStatus("current")

wsInfraNTPGroupObsolete = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 10, 1, 100, 1, 2)
)
wsInfraNTPGroupObsolete.setObjects(
      *(("WS-INFRA-NTP-MIB", "wsInfraNtpEnable"),
        ("WS-INFRA-NTP-MIB", "wsInfraNtp1Server"),
        ("WS-INFRA-NTP-MIB", "wsInfraNtp2Server"),
        ("WS-INFRA-NTP-MIB", "wsInfraNtp3Server"))
)
if mibBuilder.loadTexts:
    wsInfraNTPGroupObsolete.setStatus("obsolete")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

wsInfraNTPMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 10, 1, 100, 2, 1)
)
if mibBuilder.loadTexts:
    wsInfraNTPMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WS-INFRA-NTP-MIB",
    **{"wsInfraNTPMIB": wsInfraNTPMIB,
       "wsInfraNtpEnable": wsInfraNtpEnable,
       "wsInfraNtp1Server": wsInfraNtp1Server,
       "wsInfraNtp2Server": wsInfraNtp2Server,
       "wsInfraNtp3Server": wsInfraNtp3Server,
       "wsInfraNtpTimeZone": wsInfraNtpTimeZone,
       "wsInfraNtpCurrentDateTime": wsInfraNtpCurrentDateTime,
       "wsInfraNtpAllTimeZones": wsInfraNtpAllTimeZones,
       "wsInfraNTPMIBConformance": wsInfraNTPMIBConformance,
       "wsInfraNTPMIBGroups": wsInfraNTPMIBGroups,
       "wsInfraNTPGroup": wsInfraNTPGroup,
       "wsInfraNTPGroupObsolete": wsInfraNTPGroupObsolete,
       "wsInfraNTPMIBCompliances": wsInfraNTPMIBCompliances,
       "wsInfraNTPMIBCompliance": wsInfraNTPMIBCompliance}
)
