# SNMP MIB module (NGWX400MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NGWX400MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:27 2024
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
 NotificationType,
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
    "NotificationType",
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Wpcorp_ObjectIdentity = ObjectIdentity
wpcorp = _Wpcorp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 922)
)
_Gateways_ObjectIdentity = ObjectIdentity
gateways = _Gateways_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 922, 2)
)
_Ngwx400_ObjectIdentity = ObjectIdentity
ngwx400 = _Ngwx400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 922, 2, 4)
)
_Ngwx400Info_ObjectIdentity = ObjectIdentity
ngwx400Info = _Ngwx400Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 922, 2, 4, 1)
)


class _Ngwx400GatewayName_Type(DisplayString):
    """Custom type ngwx400GatewayName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Ngwx400GatewayName_Type.__name__ = "DisplayString"
_Ngwx400GatewayName_Object = MibScalar
ngwx400GatewayName = _Ngwx400GatewayName_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 4, 1, 1),
    _Ngwx400GatewayName_Type()
)
ngwx400GatewayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwx400GatewayName.setStatus("mandatory")
_Ngwx400Uptime_Type = TimeTicks
_Ngwx400Uptime_Object = MibScalar
ngwx400Uptime = _Ngwx400Uptime_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 4, 1, 2),
    _Ngwx400Uptime_Type()
)
ngwx400Uptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwx400Uptime.setStatus("mandatory")


class _Ngwx400GroupWiseLink_Type(DisplayString):
    """Custom type ngwx400GroupWiseLink based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_Ngwx400GroupWiseLink_Type.__name__ = "DisplayString"
_Ngwx400GroupWiseLink_Object = MibScalar
ngwx400GroupWiseLink = _Ngwx400GroupWiseLink_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 4, 1, 3),
    _Ngwx400GroupWiseLink_Type()
)
ngwx400GroupWiseLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwx400GroupWiseLink.setStatus("mandatory")


class _Ngwx400FrgnLink_Type(DisplayString):
    """Custom type ngwx400FrgnLink based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_Ngwx400FrgnLink_Type.__name__ = "DisplayString"
_Ngwx400FrgnLink_Object = MibScalar
ngwx400FrgnLink = _Ngwx400FrgnLink_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 4, 1, 4),
    _Ngwx400FrgnLink_Type()
)
ngwx400FrgnLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwx400FrgnLink.setStatus("mandatory")
_Ngwx400OutBytes_Type = Counter32
_Ngwx400OutBytes_Object = MibScalar
ngwx400OutBytes = _Ngwx400OutBytes_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 4, 1, 5),
    _Ngwx400OutBytes_Type()
)
ngwx400OutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwx400OutBytes.setStatus("mandatory")
_Ngwx400InBytes_Type = Counter32
_Ngwx400InBytes_Object = MibScalar
ngwx400InBytes = _Ngwx400InBytes_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 4, 1, 6),
    _Ngwx400InBytes_Type()
)
ngwx400InBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwx400InBytes.setStatus("mandatory")
_Ngwx400OutMsgs_Type = Counter32
_Ngwx400OutMsgs_Object = MibScalar
ngwx400OutMsgs = _Ngwx400OutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 4, 1, 7),
    _Ngwx400OutMsgs_Type()
)
ngwx400OutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwx400OutMsgs.setStatus("mandatory")
_Ngwx400InMsgs_Type = Counter32
_Ngwx400InMsgs_Object = MibScalar
ngwx400InMsgs = _Ngwx400InMsgs_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 4, 1, 8),
    _Ngwx400InMsgs_Type()
)
ngwx400InMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwx400InMsgs.setStatus("mandatory")
_Ngwx400OutStatuses_Type = Counter32
_Ngwx400OutStatuses_Object = MibScalar
ngwx400OutStatuses = _Ngwx400OutStatuses_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 4, 1, 9),
    _Ngwx400OutStatuses_Type()
)
ngwx400OutStatuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwx400OutStatuses.setStatus("mandatory")
_Ngwx400InStatuses_Type = Counter32
_Ngwx400InStatuses_Object = MibScalar
ngwx400InStatuses = _Ngwx400InStatuses_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 4, 1, 10),
    _Ngwx400InStatuses_Type()
)
ngwx400InStatuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwx400InStatuses.setStatus("mandatory")
_Ngwx400OutErrors_Type = Counter32
_Ngwx400OutErrors_Object = MibScalar
ngwx400OutErrors = _Ngwx400OutErrors_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 4, 1, 11),
    _Ngwx400OutErrors_Type()
)
ngwx400OutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwx400OutErrors.setStatus("mandatory")
_Ngwx400InErrors_Type = Counter32
_Ngwx400InErrors_Object = MibScalar
ngwx400InErrors = _Ngwx400InErrors_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 4, 1, 12),
    _Ngwx400InErrors_Type()
)
ngwx400InErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwx400InErrors.setStatus("mandatory")
_Ngwx400TrapInfo_ObjectIdentity = ObjectIdentity
ngwx400TrapInfo = _Ngwx400TrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 922, 2, 4, 2)
)
_Ngwx400TrapTime_Type = Integer32
_Ngwx400TrapTime_Object = MibScalar
ngwx400TrapTime = _Ngwx400TrapTime_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 4, 2, 1),
    _Ngwx400TrapTime_Type()
)
ngwx400TrapTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ngwx400TrapTime.setStatus("mandatory")

# Managed Objects groups


# Notification objects

ngwx400StartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 922, 2, 4, 1, 0, 1)
)
ngwx400StartTrap.setObjects(
      *(("NGWX400MIB", "ngwx400TrapTime"),
        ("NGWX400MIB", "ngwx400GatewayName"))
)
if mibBuilder.loadTexts:
    ngwx400StartTrap.setStatus(
        ""
    )

ngwx400StopTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 922, 2, 4, 1, 0, 2)
)
ngwx400StopTrap.setObjects(
      *(("NGWX400MIB", "ngwx400TrapTime"),
        ("NGWX400MIB", "ngwx400GatewayName"))
)
if mibBuilder.loadTexts:
    ngwx400StopTrap.setStatus(
        ""
    )

ngwx400RestartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 922, 2, 4, 1, 0, 3)
)
ngwx400RestartTrap.setObjects(
      *(("NGWX400MIB", "ngwx400TrapTime"),
        ("NGWX400MIB", "ngwx400GatewayName"))
)
if mibBuilder.loadTexts:
    ngwx400RestartTrap.setStatus(
        ""
    )

ngwx400GroupWiseLinkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 922, 2, 4, 1, 0, 4)
)
ngwx400GroupWiseLinkTrap.setObjects(
      *(("NGWX400MIB", "ngwx400TrapTime"),
        ("NGWX400MIB", "ngwx400GatewayName"))
)
if mibBuilder.loadTexts:
    ngwx400GroupWiseLinkTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NGWX400MIB",
    **{"wpcorp": wpcorp,
       "gateways": gateways,
       "ngwx400": ngwx400,
       "ngwx400Info": ngwx400Info,
       "ngwx400StartTrap": ngwx400StartTrap,
       "ngwx400StopTrap": ngwx400StopTrap,
       "ngwx400RestartTrap": ngwx400RestartTrap,
       "ngwx400GroupWiseLinkTrap": ngwx400GroupWiseLinkTrap,
       "ngwx400GatewayName": ngwx400GatewayName,
       "ngwx400Uptime": ngwx400Uptime,
       "ngwx400GroupWiseLink": ngwx400GroupWiseLink,
       "ngwx400FrgnLink": ngwx400FrgnLink,
       "ngwx400OutBytes": ngwx400OutBytes,
       "ngwx400InBytes": ngwx400InBytes,
       "ngwx400OutMsgs": ngwx400OutMsgs,
       "ngwx400InMsgs": ngwx400InMsgs,
       "ngwx400OutStatuses": ngwx400OutStatuses,
       "ngwx400InStatuses": ngwx400InStatuses,
       "ngwx400OutErrors": ngwx400OutErrors,
       "ngwx400InErrors": ngwx400InErrors,
       "ngwx400TrapInfo": ngwx400TrapInfo,
       "ngwx400TrapTime": ngwx400TrapTime}
)
