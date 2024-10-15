# SNMP MIB module (NGWASYNC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NGWASYNC
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
_Ngwasync_ObjectIdentity = ObjectIdentity
ngwasync = _Ngwasync_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 922, 2, 1)
)
_NgwasyncInfo_ObjectIdentity = ObjectIdentity
ngwasyncInfo = _NgwasyncInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 922, 2, 1, 1)
)


class _NgwasyncGatewayName_Type(DisplayString):
    """Custom type ngwasyncGatewayName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NgwasyncGatewayName_Type.__name__ = "DisplayString"
_NgwasyncGatewayName_Object = MibScalar
ngwasyncGatewayName = _NgwasyncGatewayName_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 1, 1, 1),
    _NgwasyncGatewayName_Type()
)
ngwasyncGatewayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwasyncGatewayName.setStatus("mandatory")
_NgwasyncUptime_Type = TimeTicks
_NgwasyncUptime_Object = MibScalar
ngwasyncUptime = _NgwasyncUptime_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 1, 1, 2),
    _NgwasyncUptime_Type()
)
ngwasyncUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwasyncUptime.setStatus("mandatory")


class _NgwasyncGroupWiseLink_Type(DisplayString):
    """Custom type ngwasyncGroupWiseLink based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_NgwasyncGroupWiseLink_Type.__name__ = "DisplayString"
_NgwasyncGroupWiseLink_Object = MibScalar
ngwasyncGroupWiseLink = _NgwasyncGroupWiseLink_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 1, 1, 3),
    _NgwasyncGroupWiseLink_Type()
)
ngwasyncGroupWiseLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwasyncGroupWiseLink.setStatus("mandatory")


class _NgwasyncFrgnLink_Type(DisplayString):
    """Custom type ngwasyncFrgnLink based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_NgwasyncFrgnLink_Type.__name__ = "DisplayString"
_NgwasyncFrgnLink_Object = MibScalar
ngwasyncFrgnLink = _NgwasyncFrgnLink_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 1, 1, 4),
    _NgwasyncFrgnLink_Type()
)
ngwasyncFrgnLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwasyncFrgnLink.setStatus("mandatory")
_NgwasyncOutBytes_Type = Counter32
_NgwasyncOutBytes_Object = MibScalar
ngwasyncOutBytes = _NgwasyncOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 1, 1, 5),
    _NgwasyncOutBytes_Type()
)
ngwasyncOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwasyncOutBytes.setStatus("mandatory")
_NgwasyncInBytes_Type = Counter32
_NgwasyncInBytes_Object = MibScalar
ngwasyncInBytes = _NgwasyncInBytes_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 1, 1, 6),
    _NgwasyncInBytes_Type()
)
ngwasyncInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwasyncInBytes.setStatus("mandatory")
_NgwasyncOutMsgs_Type = Counter32
_NgwasyncOutMsgs_Object = MibScalar
ngwasyncOutMsgs = _NgwasyncOutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 1, 1, 7),
    _NgwasyncOutMsgs_Type()
)
ngwasyncOutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwasyncOutMsgs.setStatus("mandatory")
_NgwasyncInMsgs_Type = Counter32
_NgwasyncInMsgs_Object = MibScalar
ngwasyncInMsgs = _NgwasyncInMsgs_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 1, 1, 8),
    _NgwasyncInMsgs_Type()
)
ngwasyncInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwasyncInMsgs.setStatus("mandatory")
_NgwasyncOutStatuses_Type = Counter32
_NgwasyncOutStatuses_Object = MibScalar
ngwasyncOutStatuses = _NgwasyncOutStatuses_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 1, 1, 9),
    _NgwasyncOutStatuses_Type()
)
ngwasyncOutStatuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwasyncOutStatuses.setStatus("mandatory")
_NgwasyncInStatuses_Type = Counter32
_NgwasyncInStatuses_Object = MibScalar
ngwasyncInStatuses = _NgwasyncInStatuses_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 1, 1, 10),
    _NgwasyncInStatuses_Type()
)
ngwasyncInStatuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwasyncInStatuses.setStatus("mandatory")
_NgwasyncOutErrors_Type = Counter32
_NgwasyncOutErrors_Object = MibScalar
ngwasyncOutErrors = _NgwasyncOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 1, 1, 11),
    _NgwasyncOutErrors_Type()
)
ngwasyncOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwasyncOutErrors.setStatus("mandatory")
_NgwasyncInErrors_Type = Counter32
_NgwasyncInErrors_Object = MibScalar
ngwasyncInErrors = _NgwasyncInErrors_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 1, 1, 12),
    _NgwasyncInErrors_Type()
)
ngwasyncInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwasyncInErrors.setStatus("mandatory")
_NgwasyncTrapInfo_ObjectIdentity = ObjectIdentity
ngwasyncTrapInfo = _NgwasyncTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 922, 2, 1, 2)
)
_NgwasyncTrapTime_Type = Integer32
_NgwasyncTrapTime_Object = MibScalar
ngwasyncTrapTime = _NgwasyncTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 1, 2, 1),
    _NgwasyncTrapTime_Type()
)
ngwasyncTrapTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ngwasyncTrapTime.setStatus("mandatory")

# Managed Objects groups


# Notification objects

ngwasyncStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 922, 2, 1, 1, 0, 1)
)
ngwasyncStartTrap.setObjects(
      *(("NGWASYNC", "ngwasyncTrapTime"),
        ("NGWASYNC", "ngwasyncGatewayName"))
)
if mibBuilder.loadTexts:
    ngwasyncStartTrap.setStatus(
        ""
    )

ngwasyncStopTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 922, 2, 1, 1, 0, 2)
)
ngwasyncStopTrap.setObjects(
      *(("NGWASYNC", "ngwasyncTrapTime"),
        ("NGWASYNC", "ngwasyncGatewayName"))
)
if mibBuilder.loadTexts:
    ngwasyncStopTrap.setStatus(
        ""
    )

ngwasyncRestartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 922, 2, 1, 1, 0, 3)
)
ngwasyncRestartTrap.setObjects(
      *(("NGWASYNC", "ngwasyncTrapTime"),
        ("NGWASYNC", "ngwasyncGatewayName"))
)
if mibBuilder.loadTexts:
    ngwasyncRestartTrap.setStatus(
        ""
    )

ngwasyncGroupWiseLinkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 922, 2, 1, 1, 0, 4)
)
ngwasyncGroupWiseLinkTrap.setObjects(
      *(("NGWASYNC", "ngwasyncTrapTime"),
        ("NGWASYNC", "ngwasyncGatewayName"))
)
if mibBuilder.loadTexts:
    ngwasyncGroupWiseLinkTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NGWASYNC",
    **{"wpcorp": wpcorp,
       "gateways": gateways,
       "ngwasync": ngwasync,
       "ngwasyncInfo": ngwasyncInfo,
       "ngwasyncStartTrap": ngwasyncStartTrap,
       "ngwasyncStopTrap": ngwasyncStopTrap,
       "ngwasyncRestartTrap": ngwasyncRestartTrap,
       "ngwasyncGroupWiseLinkTrap": ngwasyncGroupWiseLinkTrap,
       "ngwasyncGatewayName": ngwasyncGatewayName,
       "ngwasyncUptime": ngwasyncUptime,
       "ngwasyncGroupWiseLink": ngwasyncGroupWiseLink,
       "ngwasyncFrgnLink": ngwasyncFrgnLink,
       "ngwasyncOutBytes": ngwasyncOutBytes,
       "ngwasyncInBytes": ngwasyncInBytes,
       "ngwasyncOutMsgs": ngwasyncOutMsgs,
       "ngwasyncInMsgs": ngwasyncInMsgs,
       "ngwasyncOutStatuses": ngwasyncOutStatuses,
       "ngwasyncInStatuses": ngwasyncInStatuses,
       "ngwasyncOutErrors": ngwasyncOutErrors,
       "ngwasyncInErrors": ngwasyncInErrors,
       "ngwasyncTrapInfo": ngwasyncTrapInfo,
       "ngwasyncTrapTime": ngwasyncTrapTime}
)
