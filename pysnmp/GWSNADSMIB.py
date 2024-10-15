# SNMP MIB module (GWSNADSMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GWSNADSMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:49:28 2024
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

_Novell_ObjectIdentity = ObjectIdentity
novell = _Novell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 922)
)
_Gateways_ObjectIdentity = ObjectIdentity
gateways = _Gateways_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 922, 2)
)
_Ngwsnads_ObjectIdentity = ObjectIdentity
ngwsnads = _Ngwsnads_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 922, 2, 42)
)
_NgwsnadsInfo_ObjectIdentity = ObjectIdentity
ngwsnadsInfo = _NgwsnadsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 922, 2, 42, 1)
)


class _NgwsnadsGatewayName_Type(DisplayString):
    """Custom type ngwsnadsGatewayName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NgwsnadsGatewayName_Type.__name__ = "DisplayString"
_NgwsnadsGatewayName_Object = MibScalar
ngwsnadsGatewayName = _NgwsnadsGatewayName_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 42, 1, 1),
    _NgwsnadsGatewayName_Type()
)
ngwsnadsGatewayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwsnadsGatewayName.setStatus("mandatory")
_NgwsnadsUptime_Type = TimeTicks
_NgwsnadsUptime_Object = MibScalar
ngwsnadsUptime = _NgwsnadsUptime_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 42, 1, 2),
    _NgwsnadsUptime_Type()
)
ngwsnadsUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwsnadsUptime.setStatus("mandatory")


class _NgwsnadsGroupWiseLink_Type(DisplayString):
    """Custom type ngwsnadsGroupWiseLink based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_NgwsnadsGroupWiseLink_Type.__name__ = "DisplayString"
_NgwsnadsGroupWiseLink_Object = MibScalar
ngwsnadsGroupWiseLink = _NgwsnadsGroupWiseLink_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 42, 1, 3),
    _NgwsnadsGroupWiseLink_Type()
)
ngwsnadsGroupWiseLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwsnadsGroupWiseLink.setStatus("mandatory")


class _NgwsnadsFrgnLink_Type(DisplayString):
    """Custom type ngwsnadsFrgnLink based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_NgwsnadsFrgnLink_Type.__name__ = "DisplayString"
_NgwsnadsFrgnLink_Object = MibScalar
ngwsnadsFrgnLink = _NgwsnadsFrgnLink_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 42, 1, 4),
    _NgwsnadsFrgnLink_Type()
)
ngwsnadsFrgnLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwsnadsFrgnLink.setStatus("mandatory")
_NgwsnadsOutBytes_Type = Counter32
_NgwsnadsOutBytes_Object = MibScalar
ngwsnadsOutBytes = _NgwsnadsOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 42, 1, 5),
    _NgwsnadsOutBytes_Type()
)
ngwsnadsOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwsnadsOutBytes.setStatus("mandatory")
_NgwsnadsInBytes_Type = Counter32
_NgwsnadsInBytes_Object = MibScalar
ngwsnadsInBytes = _NgwsnadsInBytes_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 42, 1, 6),
    _NgwsnadsInBytes_Type()
)
ngwsnadsInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwsnadsInBytes.setStatus("mandatory")
_NgwsnadsOutMsgs_Type = Counter32
_NgwsnadsOutMsgs_Object = MibScalar
ngwsnadsOutMsgs = _NgwsnadsOutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 42, 1, 7),
    _NgwsnadsOutMsgs_Type()
)
ngwsnadsOutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwsnadsOutMsgs.setStatus("mandatory")
_NgwsnadsInMsgs_Type = Counter32
_NgwsnadsInMsgs_Object = MibScalar
ngwsnadsInMsgs = _NgwsnadsInMsgs_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 42, 1, 8),
    _NgwsnadsInMsgs_Type()
)
ngwsnadsInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwsnadsInMsgs.setStatus("mandatory")
_NgwsnadsOutStatuses_Type = Counter32
_NgwsnadsOutStatuses_Object = MibScalar
ngwsnadsOutStatuses = _NgwsnadsOutStatuses_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 42, 1, 9),
    _NgwsnadsOutStatuses_Type()
)
ngwsnadsOutStatuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwsnadsOutStatuses.setStatus("mandatory")
_NgwsnadsInStatuses_Type = Counter32
_NgwsnadsInStatuses_Object = MibScalar
ngwsnadsInStatuses = _NgwsnadsInStatuses_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 42, 1, 10),
    _NgwsnadsInStatuses_Type()
)
ngwsnadsInStatuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwsnadsInStatuses.setStatus("mandatory")
_NgwsnadsOutErrors_Type = Counter32
_NgwsnadsOutErrors_Object = MibScalar
ngwsnadsOutErrors = _NgwsnadsOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 42, 1, 11),
    _NgwsnadsOutErrors_Type()
)
ngwsnadsOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwsnadsOutErrors.setStatus("mandatory")
_NgwsnadsInErrors_Type = Counter32
_NgwsnadsInErrors_Object = MibScalar
ngwsnadsInErrors = _NgwsnadsInErrors_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 42, 1, 12),
    _NgwsnadsInErrors_Type()
)
ngwsnadsInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ngwsnadsInErrors.setStatus("mandatory")
_NgwsnadsTrapInfo_ObjectIdentity = ObjectIdentity
ngwsnadsTrapInfo = _NgwsnadsTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 922, 2, 42, 2)
)
_NgwsnadsTrapTime_Type = Integer32
_NgwsnadsTrapTime_Object = MibScalar
ngwsnadsTrapTime = _NgwsnadsTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 922, 2, 42, 2, 1),
    _NgwsnadsTrapTime_Type()
)
ngwsnadsTrapTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ngwsnadsTrapTime.setStatus("mandatory")

# Managed Objects groups


# Notification objects

ngwsnadsStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 922, 2, 42, 1, 0, 1)
)
ngwsnadsStartTrap.setObjects(
      *(("GWSNADSMIB", "ngwsnadsTrapTime"),
        ("GWSNADSMIB", "ngwsnadsGatewayName"))
)
if mibBuilder.loadTexts:
    ngwsnadsStartTrap.setStatus(
        ""
    )

ngwsnadsStopTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 922, 2, 42, 1, 0, 2)
)
ngwsnadsStopTrap.setObjects(
      *(("GWSNADSMIB", "ngwsnadsTrapTime"),
        ("GWSNADSMIB", "ngwsnadsGatewayName"))
)
if mibBuilder.loadTexts:
    ngwsnadsStopTrap.setStatus(
        ""
    )

ngwsnadsRestartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 922, 2, 42, 1, 0, 3)
)
ngwsnadsRestartTrap.setObjects(
      *(("GWSNADSMIB", "ngwsnadsTrapTime"),
        ("GWSNADSMIB", "ngwsnadsGatewayName"))
)
if mibBuilder.loadTexts:
    ngwsnadsRestartTrap.setStatus(
        ""
    )

ngwsnadsGroupWiseLinkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 922, 2, 42, 1, 0, 4)
)
ngwsnadsGroupWiseLinkTrap.setObjects(
      *(("GWSNADSMIB", "ngwsnadsTrapTime"),
        ("GWSNADSMIB", "ngwsnadsGatewayName"))
)
if mibBuilder.loadTexts:
    ngwsnadsGroupWiseLinkTrap.setStatus(
        ""
    )

ngwsnadsFgnLinkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 922, 2, 42, 1, 0, 5)
)
ngwsnadsFgnLinkTrap.setObjects(
      *(("GWSNADSMIB", "ngwsnadsTrapTime"),
        ("GWSNADSMIB", "ngwsnadsGatewayName"))
)
if mibBuilder.loadTexts:
    ngwsnadsFgnLinkTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GWSNADSMIB",
    **{"novell": novell,
       "gateways": gateways,
       "ngwsnads": ngwsnads,
       "ngwsnadsInfo": ngwsnadsInfo,
       "ngwsnadsStartTrap": ngwsnadsStartTrap,
       "ngwsnadsStopTrap": ngwsnadsStopTrap,
       "ngwsnadsRestartTrap": ngwsnadsRestartTrap,
       "ngwsnadsGroupWiseLinkTrap": ngwsnadsGroupWiseLinkTrap,
       "ngwsnadsFgnLinkTrap": ngwsnadsFgnLinkTrap,
       "ngwsnadsGatewayName": ngwsnadsGatewayName,
       "ngwsnadsUptime": ngwsnadsUptime,
       "ngwsnadsGroupWiseLink": ngwsnadsGroupWiseLink,
       "ngwsnadsFrgnLink": ngwsnadsFrgnLink,
       "ngwsnadsOutBytes": ngwsnadsOutBytes,
       "ngwsnadsInBytes": ngwsnadsInBytes,
       "ngwsnadsOutMsgs": ngwsnadsOutMsgs,
       "ngwsnadsInMsgs": ngwsnadsInMsgs,
       "ngwsnadsOutStatuses": ngwsnadsOutStatuses,
       "ngwsnadsInStatuses": ngwsnadsInStatuses,
       "ngwsnadsOutErrors": ngwsnadsOutErrors,
       "ngwsnadsInErrors": ngwsnadsInErrors,
       "ngwsnadsTrapInfo": ngwsnadsTrapInfo,
       "ngwsnadsTrapTime": ngwsnadsTrapTime}
)
