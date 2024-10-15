# SNMP MIB module (GWPAGERMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GWPAGERMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:49:26 2024
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
    (1, 3, 6, 1, 4, 1, 23)
)
_Gateways_ObjectIdentity = ObjectIdentity
gateways = _Gateways_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2)
)
_GwPAGER_ObjectIdentity = ObjectIdentity
gwPAGER = _GwPAGER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 43)
)
_GwPAGERInfo_ObjectIdentity = ObjectIdentity
gwPAGERInfo = _GwPAGERInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 43, 1)
)


class _GwPAGERGatewayName_Type(DisplayString):
    """Custom type gwPAGERGatewayName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GwPAGERGatewayName_Type.__name__ = "DisplayString"
_GwPAGERGatewayName_Object = MibScalar
gwPAGERGatewayName = _GwPAGERGatewayName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 43, 1, 1),
    _GwPAGERGatewayName_Type()
)
gwPAGERGatewayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwPAGERGatewayName.setStatus("mandatory")
_GwPAGERUptime_Type = TimeTicks
_GwPAGERUptime_Object = MibScalar
gwPAGERUptime = _GwPAGERUptime_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 43, 1, 2),
    _GwPAGERUptime_Type()
)
gwPAGERUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwPAGERUptime.setStatus("mandatory")


class _GwPAGERGroupWiseLink_Type(DisplayString):
    """Custom type gwPAGERGroupWiseLink based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_GwPAGERGroupWiseLink_Type.__name__ = "DisplayString"
_GwPAGERGroupWiseLink_Object = MibScalar
gwPAGERGroupWiseLink = _GwPAGERGroupWiseLink_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 43, 1, 3),
    _GwPAGERGroupWiseLink_Type()
)
gwPAGERGroupWiseLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwPAGERGroupWiseLink.setStatus("mandatory")


class _GwPAGERFrgnLink_Type(DisplayString):
    """Custom type gwPAGERFrgnLink based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_GwPAGERFrgnLink_Type.__name__ = "DisplayString"
_GwPAGERFrgnLink_Object = MibScalar
gwPAGERFrgnLink = _GwPAGERFrgnLink_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 43, 1, 4),
    _GwPAGERFrgnLink_Type()
)
gwPAGERFrgnLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwPAGERFrgnLink.setStatus("mandatory")
_GwPAGEROutBytes_Type = Counter32
_GwPAGEROutBytes_Object = MibScalar
gwPAGEROutBytes = _GwPAGEROutBytes_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 43, 1, 5),
    _GwPAGEROutBytes_Type()
)
gwPAGEROutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwPAGEROutBytes.setStatus("mandatory")
_GwPAGERInBytes_Type = Counter32
_GwPAGERInBytes_Object = MibScalar
gwPAGERInBytes = _GwPAGERInBytes_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 43, 1, 6),
    _GwPAGERInBytes_Type()
)
gwPAGERInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwPAGERInBytes.setStatus("mandatory")
_GwPAGEROutMsgs_Type = Counter32
_GwPAGEROutMsgs_Object = MibScalar
gwPAGEROutMsgs = _GwPAGEROutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 43, 1, 7),
    _GwPAGEROutMsgs_Type()
)
gwPAGEROutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwPAGEROutMsgs.setStatus("mandatory")
_GwPAGERInMsgs_Type = Counter32
_GwPAGERInMsgs_Object = MibScalar
gwPAGERInMsgs = _GwPAGERInMsgs_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 43, 1, 8),
    _GwPAGERInMsgs_Type()
)
gwPAGERInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwPAGERInMsgs.setStatus("mandatory")
_GwPAGEROutStatuses_Type = Counter32
_GwPAGEROutStatuses_Object = MibScalar
gwPAGEROutStatuses = _GwPAGEROutStatuses_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 43, 1, 9),
    _GwPAGEROutStatuses_Type()
)
gwPAGEROutStatuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwPAGEROutStatuses.setStatus("mandatory")
_GwPAGERInStatuses_Type = Counter32
_GwPAGERInStatuses_Object = MibScalar
gwPAGERInStatuses = _GwPAGERInStatuses_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 43, 1, 10),
    _GwPAGERInStatuses_Type()
)
gwPAGERInStatuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwPAGERInStatuses.setStatus("mandatory")
_GwPAGEROutErrors_Type = Counter32
_GwPAGEROutErrors_Object = MibScalar
gwPAGEROutErrors = _GwPAGEROutErrors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 43, 1, 11),
    _GwPAGEROutErrors_Type()
)
gwPAGEROutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwPAGEROutErrors.setStatus("mandatory")
_GwPAGERInErrors_Type = Counter32
_GwPAGERInErrors_Object = MibScalar
gwPAGERInErrors = _GwPAGERInErrors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 43, 1, 12),
    _GwPAGERInErrors_Type()
)
gwPAGERInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwPAGERInErrors.setStatus("mandatory")
_GwPAGERTrapInfo_ObjectIdentity = ObjectIdentity
gwPAGERTrapInfo = _GwPAGERTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 43, 2)
)
_GwPAGERTrapTime_Type = Integer32
_GwPAGERTrapTime_Object = MibScalar
gwPAGERTrapTime = _GwPAGERTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 43, 2, 1),
    _GwPAGERTrapTime_Type()
)
gwPAGERTrapTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gwPAGERTrapTime.setStatus("mandatory")

# Managed Objects groups


# Notification objects

gwPAGERStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 43, 1, 0, 1)
)
gwPAGERStartTrap.setObjects(
      *(("GWPAGERMIB", "gwPAGERTrapTime"),
        ("GWPAGERMIB", "gwPAGERGatewayName"))
)
if mibBuilder.loadTexts:
    gwPAGERStartTrap.setStatus(
        ""
    )

gwPAGERStopTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 43, 1, 0, 2)
)
gwPAGERStopTrap.setObjects(
      *(("GWPAGERMIB", "gwPAGERTrapTime"),
        ("GWPAGERMIB", "gwPAGERGatewayName"))
)
if mibBuilder.loadTexts:
    gwPAGERStopTrap.setStatus(
        ""
    )

gwPAGERRestartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 43, 1, 0, 3)
)
gwPAGERRestartTrap.setObjects(
      *(("GWPAGERMIB", "gwPAGERTrapTime"),
        ("GWPAGERMIB", "gwPAGERGatewayName"))
)
if mibBuilder.loadTexts:
    gwPAGERRestartTrap.setStatus(
        ""
    )

gwPAGERGroupWiseLinkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 43, 1, 0, 4)
)
gwPAGERGroupWiseLinkTrap.setObjects(
      *(("GWPAGERMIB", "gwPAGERTrapTime"),
        ("GWPAGERMIB", "gwPAGERGatewayName"))
)
if mibBuilder.loadTexts:
    gwPAGERGroupWiseLinkTrap.setStatus(
        ""
    )

gwPAGERFgnLinkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 43, 1, 0, 5)
)
gwPAGERFgnLinkTrap.setObjects(
      *(("GWPAGERMIB", "gwPAGERTrapTime"),
        ("GWPAGERMIB", "gwPAGERGatewayName"))
)
if mibBuilder.loadTexts:
    gwPAGERFgnLinkTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GWPAGERMIB",
    **{"novell": novell,
       "gateways": gateways,
       "gwPAGER": gwPAGER,
       "gwPAGERInfo": gwPAGERInfo,
       "gwPAGERStartTrap": gwPAGERStartTrap,
       "gwPAGERStopTrap": gwPAGERStopTrap,
       "gwPAGERRestartTrap": gwPAGERRestartTrap,
       "gwPAGERGroupWiseLinkTrap": gwPAGERGroupWiseLinkTrap,
       "gwPAGERFgnLinkTrap": gwPAGERFgnLinkTrap,
       "gwPAGERGatewayName": gwPAGERGatewayName,
       "gwPAGERUptime": gwPAGERUptime,
       "gwPAGERGroupWiseLink": gwPAGERGroupWiseLink,
       "gwPAGERFrgnLink": gwPAGERFrgnLink,
       "gwPAGEROutBytes": gwPAGEROutBytes,
       "gwPAGERInBytes": gwPAGERInBytes,
       "gwPAGEROutMsgs": gwPAGEROutMsgs,
       "gwPAGERInMsgs": gwPAGERInMsgs,
       "gwPAGEROutStatuses": gwPAGEROutStatuses,
       "gwPAGERInStatuses": gwPAGERInStatuses,
       "gwPAGEROutErrors": gwPAGEROutErrors,
       "gwPAGERInErrors": gwPAGERInErrors,
       "gwPAGERTrapInfo": gwPAGERTrapInfo,
       "gwPAGERTrapTime": gwPAGERTrapTime}
)
