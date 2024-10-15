# SNMP MIB module (GWOVVMMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GWOVVMMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:49:25 2024
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
_Ngwovvm_ObjectIdentity = ObjectIdentity
ngwovvm = _Ngwovvm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 922, 2, 2)
)
_NgwovvmInfo_ObjectIdentity = ObjectIdentity
ngwovvmInfo = _NgwovvmInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 922, 2, 2, 1)
)


class _NgwovvmGatewayName_Type(DisplayString):
    """Custom type ngwovvmGatewayName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NgwovvmGatewayName_Type.__name__ = "DisplayString"
_NgwovvmGatewayName_Object = MibScalar
ngwovvmGatewayName = _NgwovvmGatewayName_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 2, 1, 1),
    _NgwovvmGatewayName_Type()
)
ngwovvmGatewayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwovvmGatewayName.setStatus("mandatory")
_NgwovvmUptime_Type = TimeTicks
_NgwovvmUptime_Object = MibScalar
ngwovvmUptime = _NgwovvmUptime_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 2, 1, 2),
    _NgwovvmUptime_Type()
)
ngwovvmUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwovvmUptime.setStatus("mandatory")


class _NgwovvmGroupWiseLink_Type(DisplayString):
    """Custom type ngwovvmGroupWiseLink based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_NgwovvmGroupWiseLink_Type.__name__ = "DisplayString"
_NgwovvmGroupWiseLink_Object = MibScalar
ngwovvmGroupWiseLink = _NgwovvmGroupWiseLink_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 2, 1, 3),
    _NgwovvmGroupWiseLink_Type()
)
ngwovvmGroupWiseLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwovvmGroupWiseLink.setStatus("mandatory")


class _NgwovvmFrgnLink_Type(DisplayString):
    """Custom type ngwovvmFrgnLink based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_NgwovvmFrgnLink_Type.__name__ = "DisplayString"
_NgwovvmFrgnLink_Object = MibScalar
ngwovvmFrgnLink = _NgwovvmFrgnLink_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 2, 1, 4),
    _NgwovvmFrgnLink_Type()
)
ngwovvmFrgnLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwovvmFrgnLink.setStatus("mandatory")
_NgwovvmOutBytes_Type = Counter32
_NgwovvmOutBytes_Object = MibScalar
ngwovvmOutBytes = _NgwovvmOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 2, 1, 5),
    _NgwovvmOutBytes_Type()
)
ngwovvmOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwovvmOutBytes.setStatus("mandatory")
_NgwovvmInBytes_Type = Counter32
_NgwovvmInBytes_Object = MibScalar
ngwovvmInBytes = _NgwovvmInBytes_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 2, 1, 6),
    _NgwovvmInBytes_Type()
)
ngwovvmInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwovvmInBytes.setStatus("mandatory")
_NgwovvmOutMsgs_Type = Counter32
_NgwovvmOutMsgs_Object = MibScalar
ngwovvmOutMsgs = _NgwovvmOutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 2, 1, 7),
    _NgwovvmOutMsgs_Type()
)
ngwovvmOutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwovvmOutMsgs.setStatus("mandatory")
_NgwovvmInMsgs_Type = Counter32
_NgwovvmInMsgs_Object = MibScalar
ngwovvmInMsgs = _NgwovvmInMsgs_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 2, 1, 8),
    _NgwovvmInMsgs_Type()
)
ngwovvmInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwovvmInMsgs.setStatus("mandatory")
_NgwovvmOutStatuses_Type = Counter32
_NgwovvmOutStatuses_Object = MibScalar
ngwovvmOutStatuses = _NgwovvmOutStatuses_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 2, 1, 9),
    _NgwovvmOutStatuses_Type()
)
ngwovvmOutStatuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwovvmOutStatuses.setStatus("mandatory")
_NgwovvmInStatuses_Type = Counter32
_NgwovvmInStatuses_Object = MibScalar
ngwovvmInStatuses = _NgwovvmInStatuses_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 2, 1, 10),
    _NgwovvmInStatuses_Type()
)
ngwovvmInStatuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwovvmInStatuses.setStatus("mandatory")
_NgwovvmOutErrors_Type = Counter32
_NgwovvmOutErrors_Object = MibScalar
ngwovvmOutErrors = _NgwovvmOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 2, 1, 11),
    _NgwovvmOutErrors_Type()
)
ngwovvmOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwovvmOutErrors.setStatus("mandatory")
_NgwovvmInErrors_Type = Counter32
_NgwovvmInErrors_Object = MibScalar
ngwovvmInErrors = _NgwovvmInErrors_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 2, 1, 12),
    _NgwovvmInErrors_Type()
)
ngwovvmInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwovvmInErrors.setStatus("mandatory")
_NgwovvmTrapInfo_ObjectIdentity = ObjectIdentity
ngwovvmTrapInfo = _NgwovvmTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 922, 2, 2, 2)
)
_NgwovvmTrapTime_Type = Integer32
_NgwovvmTrapTime_Object = MibScalar
ngwovvmTrapTime = _NgwovvmTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 2, 2, 1),
    _NgwovvmTrapTime_Type()
)
ngwovvmTrapTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ngwovvmTrapTime.setStatus("mandatory")

# Managed Objects groups


# Notification objects

ngwovvmStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 922, 2, 2, 1, 0, 1)
)
ngwovvmStartTrap.setObjects(
      *(("GWOVVMMIB", "ngwovvmTrapTime"),
        ("GWOVVMMIB", "ngwovvmGatewayName"))
)
if mibBuilder.loadTexts:
    ngwovvmStartTrap.setStatus(
        ""
    )

ngwovvmStopTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 922, 2, 2, 1, 0, 2)
)
ngwovvmStopTrap.setObjects(
      *(("GWOVVMMIB", "ngwovvmTrapTime"),
        ("GWOVVMMIB", "ngwovvmGatewayName"))
)
if mibBuilder.loadTexts:
    ngwovvmStopTrap.setStatus(
        ""
    )

ngwovvmRestartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 922, 2, 2, 1, 0, 3)
)
ngwovvmRestartTrap.setObjects(
      *(("GWOVVMMIB", "ngwovvmTrapTime"),
        ("GWOVVMMIB", "ngwovvmGatewayName"))
)
if mibBuilder.loadTexts:
    ngwovvmRestartTrap.setStatus(
        ""
    )

ngwovvmGroupWiseLinkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 922, 2, 2, 1, 0, 4)
)
ngwovvmGroupWiseLinkTrap.setObjects(
      *(("GWOVVMMIB", "ngwovvmTrapTime"),
        ("GWOVVMMIB", "ngwovvmGatewayName"))
)
if mibBuilder.loadTexts:
    ngwovvmGroupWiseLinkTrap.setStatus(
        ""
    )

ngwovvmFgnLinkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 922, 2, 2, 1, 0, 5)
)
ngwovvmFgnLinkTrap.setObjects(
      *(("GWOVVMMIB", "ngwovvmTrapTime"),
        ("GWOVVMMIB", "ngwovvmGatewayName"))
)
if mibBuilder.loadTexts:
    ngwovvmFgnLinkTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GWOVVMMIB",
    **{"wpcorp": wpcorp,
       "gateways": gateways,
       "ngwovvm": ngwovvm,
       "ngwovvmInfo": ngwovvmInfo,
       "ngwovvmStartTrap": ngwovvmStartTrap,
       "ngwovvmStopTrap": ngwovvmStopTrap,
       "ngwovvmRestartTrap": ngwovvmRestartTrap,
       "ngwovvmGroupWiseLinkTrap": ngwovvmGroupWiseLinkTrap,
       "ngwovvmFgnLinkTrap": ngwovvmFgnLinkTrap,
       "ngwovvmGatewayName": ngwovvmGatewayName,
       "ngwovvmUptime": ngwovvmUptime,
       "ngwovvmGroupWiseLink": ngwovvmGroupWiseLink,
       "ngwovvmFrgnLink": ngwovvmFrgnLink,
       "ngwovvmOutBytes": ngwovvmOutBytes,
       "ngwovvmInBytes": ngwovvmInBytes,
       "ngwovvmOutMsgs": ngwovvmOutMsgs,
       "ngwovvmInMsgs": ngwovvmInMsgs,
       "ngwovvmOutStatuses": ngwovvmOutStatuses,
       "ngwovvmInStatuses": ngwovvmInStatuses,
       "ngwovvmOutErrors": ngwovvmOutErrors,
       "ngwovvmInErrors": ngwovvmInErrors,
       "ngwovvmTrapInfo": ngwovvmTrapInfo,
       "ngwovvmTrapTime": ngwovvmTrapTime}
)
