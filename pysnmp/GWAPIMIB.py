# SNMP MIB module (GWAPIMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GWAPIMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:49:22 2024
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
_NgwAPI_ObjectIdentity = ObjectIdentity
ngwAPI = _NgwAPI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 922, 2, 8)
)
_NgwAPIInfo_ObjectIdentity = ObjectIdentity
ngwAPIInfo = _NgwAPIInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 922, 2, 8, 1)
)


class _NgwAPIGatewayName_Type(DisplayString):
    """Custom type ngwAPIGatewayName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NgwAPIGatewayName_Type.__name__ = "DisplayString"
_NgwAPIGatewayName_Object = MibScalar
ngwAPIGatewayName = _NgwAPIGatewayName_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 8, 1, 1),
    _NgwAPIGatewayName_Type()
)
ngwAPIGatewayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwAPIGatewayName.setStatus("mandatory")
_NgwAPIUptime_Type = TimeTicks
_NgwAPIUptime_Object = MibScalar
ngwAPIUptime = _NgwAPIUptime_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 8, 1, 2),
    _NgwAPIUptime_Type()
)
ngwAPIUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwAPIUptime.setStatus("mandatory")


class _NgwAPIGroupWiseLink_Type(DisplayString):
    """Custom type ngwAPIGroupWiseLink based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_NgwAPIGroupWiseLink_Type.__name__ = "DisplayString"
_NgwAPIGroupWiseLink_Object = MibScalar
ngwAPIGroupWiseLink = _NgwAPIGroupWiseLink_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 8, 1, 3),
    _NgwAPIGroupWiseLink_Type()
)
ngwAPIGroupWiseLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwAPIGroupWiseLink.setStatus("mandatory")


class _NgwAPIFrgnLink_Type(DisplayString):
    """Custom type ngwAPIFrgnLink based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_NgwAPIFrgnLink_Type.__name__ = "DisplayString"
_NgwAPIFrgnLink_Object = MibScalar
ngwAPIFrgnLink = _NgwAPIFrgnLink_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 8, 1, 4),
    _NgwAPIFrgnLink_Type()
)
ngwAPIFrgnLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwAPIFrgnLink.setStatus("mandatory")
_NgwAPIOutBytes_Type = Counter32
_NgwAPIOutBytes_Object = MibScalar
ngwAPIOutBytes = _NgwAPIOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 8, 1, 5),
    _NgwAPIOutBytes_Type()
)
ngwAPIOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwAPIOutBytes.setStatus("mandatory")
_NgwAPIInBytes_Type = Counter32
_NgwAPIInBytes_Object = MibScalar
ngwAPIInBytes = _NgwAPIInBytes_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 8, 1, 6),
    _NgwAPIInBytes_Type()
)
ngwAPIInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwAPIInBytes.setStatus("mandatory")
_NgwAPIOutMsgs_Type = Counter32
_NgwAPIOutMsgs_Object = MibScalar
ngwAPIOutMsgs = _NgwAPIOutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 8, 1, 7),
    _NgwAPIOutMsgs_Type()
)
ngwAPIOutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwAPIOutMsgs.setStatus("mandatory")
_NgwAPIInMsgs_Type = Counter32
_NgwAPIInMsgs_Object = MibScalar
ngwAPIInMsgs = _NgwAPIInMsgs_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 8, 1, 8),
    _NgwAPIInMsgs_Type()
)
ngwAPIInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwAPIInMsgs.setStatus("mandatory")
_NgwAPIOutStatuses_Type = Counter32
_NgwAPIOutStatuses_Object = MibScalar
ngwAPIOutStatuses = _NgwAPIOutStatuses_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 8, 1, 9),
    _NgwAPIOutStatuses_Type()
)
ngwAPIOutStatuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwAPIOutStatuses.setStatus("mandatory")
_NgwAPIInStatuses_Type = Counter32
_NgwAPIInStatuses_Object = MibScalar
ngwAPIInStatuses = _NgwAPIInStatuses_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 8, 1, 10),
    _NgwAPIInStatuses_Type()
)
ngwAPIInStatuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwAPIInStatuses.setStatus("mandatory")
_NgwAPIOutErrors_Type = Counter32
_NgwAPIOutErrors_Object = MibScalar
ngwAPIOutErrors = _NgwAPIOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 8, 1, 11),
    _NgwAPIOutErrors_Type()
)
ngwAPIOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwAPIOutErrors.setStatus("mandatory")
_NgwAPIInErrors_Type = Counter32
_NgwAPIInErrors_Object = MibScalar
ngwAPIInErrors = _NgwAPIInErrors_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 8, 1, 12),
    _NgwAPIInErrors_Type()
)
ngwAPIInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwAPIInErrors.setStatus("mandatory")
_NgwAPITrapInfo_ObjectIdentity = ObjectIdentity
ngwAPITrapInfo = _NgwAPITrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 922, 2, 8, 2)
)
_NgwAPITrapTime_Type = Integer32
_NgwAPITrapTime_Object = MibScalar
ngwAPITrapTime = _NgwAPITrapTime_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 8, 2, 1),
    _NgwAPITrapTime_Type()
)
ngwAPITrapTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ngwAPITrapTime.setStatus("mandatory")

# Managed Objects groups


# Notification objects

ngwAPIStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 922, 2, 8, 1, 0, 1)
)
ngwAPIStartTrap.setObjects(
      *(("GWAPIMIB", "ngwAPITrapTime"),
        ("GWAPIMIB", "ngwAPIGatewayName"))
)
if mibBuilder.loadTexts:
    ngwAPIStartTrap.setStatus(
        ""
    )

ngwAPIStopTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 922, 2, 8, 1, 0, 2)
)
ngwAPIStopTrap.setObjects(
      *(("GWAPIMIB", "ngwAPITrapTime"),
        ("GWAPIMIB", "ngwAPIGatewayName"))
)
if mibBuilder.loadTexts:
    ngwAPIStopTrap.setStatus(
        ""
    )

ngwAPIRestartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 922, 2, 8, 1, 0, 3)
)
ngwAPIRestartTrap.setObjects(
      *(("GWAPIMIB", "ngwAPITrapTime"),
        ("GWAPIMIB", "ngwAPIGatewayName"))
)
if mibBuilder.loadTexts:
    ngwAPIRestartTrap.setStatus(
        ""
    )

ngwAPIGroupWiseLinkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 922, 2, 8, 1, 0, 4)
)
ngwAPIGroupWiseLinkTrap.setObjects(
      *(("GWAPIMIB", "ngwAPITrapTime"),
        ("GWAPIMIB", "ngwAPIGatewayName"))
)
if mibBuilder.loadTexts:
    ngwAPIGroupWiseLinkTrap.setStatus(
        ""
    )

ngwAPIFgnLinkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 922, 2, 8, 1, 0, 5)
)
ngwAPIFgnLinkTrap.setObjects(
      *(("GWAPIMIB", "ngwAPITrapTime"),
        ("GWAPIMIB", "ngwAPIGatewayName"))
)
if mibBuilder.loadTexts:
    ngwAPIFgnLinkTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GWAPIMIB",
    **{"wpcorp": wpcorp,
       "gateways": gateways,
       "ngwAPI": ngwAPI,
       "ngwAPIInfo": ngwAPIInfo,
       "ngwAPIStartTrap": ngwAPIStartTrap,
       "ngwAPIStopTrap": ngwAPIStopTrap,
       "ngwAPIRestartTrap": ngwAPIRestartTrap,
       "ngwAPIGroupWiseLinkTrap": ngwAPIGroupWiseLinkTrap,
       "ngwAPIFgnLinkTrap": ngwAPIFgnLinkTrap,
       "ngwAPIGatewayName": ngwAPIGatewayName,
       "ngwAPIUptime": ngwAPIUptime,
       "ngwAPIGroupWiseLink": ngwAPIGroupWiseLink,
       "ngwAPIFrgnLink": ngwAPIFrgnLink,
       "ngwAPIOutBytes": ngwAPIOutBytes,
       "ngwAPIInBytes": ngwAPIInBytes,
       "ngwAPIOutMsgs": ngwAPIOutMsgs,
       "ngwAPIInMsgs": ngwAPIInMsgs,
       "ngwAPIOutStatuses": ngwAPIOutStatuses,
       "ngwAPIInStatuses": ngwAPIInStatuses,
       "ngwAPIOutErrors": ngwAPIOutErrors,
       "ngwAPIInErrors": ngwAPIInErrors,
       "ngwAPITrapInfo": ngwAPITrapInfo,
       "ngwAPITrapTime": ngwAPITrapTime}
)
