# SNMP MIB module (RBN-DHCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBN-DHCP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:45:04 2024
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

(rbnMgmt,) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnMgmt")

(RbnSlot,) = mibBuilder.importSymbols(
    "RBN-TC",
    "RbnSlot")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rbnDhcpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30)
)
rbnDhcpMib.setRevisions(
        ("2010-03-10 17:00",
         "2005-10-14 17:00",
         "2004-05-03 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RbnDhcpMIBNotifications_ObjectIdentity = ObjectIdentity
rbnDhcpMIBNotifications = _RbnDhcpMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 0)
)
_RbnDhcpMIBObjects_ObjectIdentity = ObjectIdentity
rbnDhcpMIBObjects = _RbnDhcpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 1)
)
_RbnDhcpIntfThresholdTable_Object = MibTable
rbnDhcpIntfThresholdTable = _RbnDhcpIntfThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 1)
)
if mibBuilder.loadTexts:
    rbnDhcpIntfThresholdTable.setStatus("current")
_RbnDhcpIntfThresholdEntry_Object = MibTableRow
rbnDhcpIntfThresholdEntry = _RbnDhcpIntfThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 1, 1)
)
rbnDhcpIntfThresholdEntry.setIndexNames(
    (1, "RBN-DHCP-MIB", "rbnDhcpIntfThresholdName"),
)
if mibBuilder.loadTexts:
    rbnDhcpIntfThresholdEntry.setStatus("current")


class _RbnDhcpIntfThresholdName_Type(SnmpAdminString):
    """Custom type rbnDhcpIntfThresholdName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_RbnDhcpIntfThresholdName_Type.__name__ = "SnmpAdminString"
_RbnDhcpIntfThresholdName_Object = MibTableColumn
rbnDhcpIntfThresholdName = _RbnDhcpIntfThresholdName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 1, 1, 1),
    _RbnDhcpIntfThresholdName_Type()
)
rbnDhcpIntfThresholdName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnDhcpIntfThresholdName.setStatus("current")


class _RbnDhcpIntfThresholdContextName_Type(SnmpAdminString):
    """Custom type rbnDhcpIntfThresholdContextName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_RbnDhcpIntfThresholdContextName_Type.__name__ = "SnmpAdminString"
_RbnDhcpIntfThresholdContextName_Object = MibTableColumn
rbnDhcpIntfThresholdContextName = _RbnDhcpIntfThresholdContextName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 1, 1, 2),
    _RbnDhcpIntfThresholdContextName_Type()
)
rbnDhcpIntfThresholdContextName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnDhcpIntfThresholdContextName.setStatus("current")
_RbnDhcpIntfThresholdSize_Type = Unsigned32
_RbnDhcpIntfThresholdSize_Object = MibTableColumn
rbnDhcpIntfThresholdSize = _RbnDhcpIntfThresholdSize_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 1, 1, 3),
    _RbnDhcpIntfThresholdSize_Type()
)
rbnDhcpIntfThresholdSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnDhcpIntfThresholdSize.setStatus("current")
_RbnDhcpIntfThresholdAvailable_Type = Unsigned32
_RbnDhcpIntfThresholdAvailable_Object = MibTableColumn
rbnDhcpIntfThresholdAvailable = _RbnDhcpIntfThresholdAvailable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 1, 1, 4),
    _RbnDhcpIntfThresholdAvailable_Type()
)
rbnDhcpIntfThresholdAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnDhcpIntfThresholdAvailable.setStatus("current")
_RbnDhcpIntfThresholdInuse_Type = Unsigned32
_RbnDhcpIntfThresholdInuse_Object = MibTableColumn
rbnDhcpIntfThresholdInuse = _RbnDhcpIntfThresholdInuse_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 1, 1, 5),
    _RbnDhcpIntfThresholdInuse_Type()
)
rbnDhcpIntfThresholdInuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnDhcpIntfThresholdInuse.setStatus("current")


class _RbnDhcpIntfThresholdFallingThreshold_Type(Unsigned32):
    """Custom type rbnDhcpIntfThresholdFallingThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 196608),
    )


_RbnDhcpIntfThresholdFallingThreshold_Type.__name__ = "Unsigned32"
_RbnDhcpIntfThresholdFallingThreshold_Object = MibTableColumn
rbnDhcpIntfThresholdFallingThreshold = _RbnDhcpIntfThresholdFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 1, 1, 6),
    _RbnDhcpIntfThresholdFallingThreshold_Type()
)
rbnDhcpIntfThresholdFallingThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnDhcpIntfThresholdFallingThreshold.setStatus("current")
_RbnDhcpIntfThresholdFallingSendTrap_Type = TruthValue
_RbnDhcpIntfThresholdFallingSendTrap_Object = MibTableColumn
rbnDhcpIntfThresholdFallingSendTrap = _RbnDhcpIntfThresholdFallingSendTrap_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 1, 1, 7),
    _RbnDhcpIntfThresholdFallingSendTrap_Type()
)
rbnDhcpIntfThresholdFallingSendTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnDhcpIntfThresholdFallingSendTrap.setStatus("current")
_RbnDhcpIntfThresholdFallingLogMessage_Type = TruthValue
_RbnDhcpIntfThresholdFallingLogMessage_Object = MibTableColumn
rbnDhcpIntfThresholdFallingLogMessage = _RbnDhcpIntfThresholdFallingLogMessage_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 1, 1, 8),
    _RbnDhcpIntfThresholdFallingLogMessage_Type()
)
rbnDhcpIntfThresholdFallingLogMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnDhcpIntfThresholdFallingLogMessage.setStatus("current")


class _RbnDhcpIntfThresholdRisingThreshold_Type(Unsigned32):
    """Custom type rbnDhcpIntfThresholdRisingThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 196608),
    )


_RbnDhcpIntfThresholdRisingThreshold_Type.__name__ = "Unsigned32"
_RbnDhcpIntfThresholdRisingThreshold_Object = MibTableColumn
rbnDhcpIntfThresholdRisingThreshold = _RbnDhcpIntfThresholdRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 1, 1, 9),
    _RbnDhcpIntfThresholdRisingThreshold_Type()
)
rbnDhcpIntfThresholdRisingThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnDhcpIntfThresholdRisingThreshold.setStatus("current")
_RbnDhcpIntfThresholdRisingSendTrap_Type = TruthValue
_RbnDhcpIntfThresholdRisingSendTrap_Object = MibTableColumn
rbnDhcpIntfThresholdRisingSendTrap = _RbnDhcpIntfThresholdRisingSendTrap_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 1, 1, 10),
    _RbnDhcpIntfThresholdRisingSendTrap_Type()
)
rbnDhcpIntfThresholdRisingSendTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnDhcpIntfThresholdRisingSendTrap.setStatus("current")
_RbnDhcpIntfThresholdRisingLogMessage_Type = TruthValue
_RbnDhcpIntfThresholdRisingLogMessage_Object = MibTableColumn
rbnDhcpIntfThresholdRisingLogMessage = _RbnDhcpIntfThresholdRisingLogMessage_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 1, 1, 11),
    _RbnDhcpIntfThresholdRisingLogMessage_Type()
)
rbnDhcpIntfThresholdRisingLogMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnDhcpIntfThresholdRisingLogMessage.setStatus("current")
_RbnDhcpCtxThreshold_ObjectIdentity = ObjectIdentity
rbnDhcpCtxThreshold = _RbnDhcpCtxThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 2)
)


class _RbnDhcpCtxThresholdName_Type(SnmpAdminString):
    """Custom type rbnDhcpCtxThresholdName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_RbnDhcpCtxThresholdName_Type.__name__ = "SnmpAdminString"
_RbnDhcpCtxThresholdName_Object = MibScalar
rbnDhcpCtxThresholdName = _RbnDhcpCtxThresholdName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 2, 1),
    _RbnDhcpCtxThresholdName_Type()
)
rbnDhcpCtxThresholdName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnDhcpCtxThresholdName.setStatus("current")
_RbnDhcpCtxThresholdSize_Type = Unsigned32
_RbnDhcpCtxThresholdSize_Object = MibScalar
rbnDhcpCtxThresholdSize = _RbnDhcpCtxThresholdSize_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 2, 2),
    _RbnDhcpCtxThresholdSize_Type()
)
rbnDhcpCtxThresholdSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnDhcpCtxThresholdSize.setStatus("current")
_RbnDhcpCtxThresholdAvailable_Type = Unsigned32
_RbnDhcpCtxThresholdAvailable_Object = MibScalar
rbnDhcpCtxThresholdAvailable = _RbnDhcpCtxThresholdAvailable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 2, 3),
    _RbnDhcpCtxThresholdAvailable_Type()
)
rbnDhcpCtxThresholdAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnDhcpCtxThresholdAvailable.setStatus("current")
_RbnDhcpCtxThresholdInuse_Type = Unsigned32
_RbnDhcpCtxThresholdInuse_Object = MibScalar
rbnDhcpCtxThresholdInuse = _RbnDhcpCtxThresholdInuse_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 2, 4),
    _RbnDhcpCtxThresholdInuse_Type()
)
rbnDhcpCtxThresholdInuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnDhcpCtxThresholdInuse.setStatus("current")


class _RbnDhcpCtxThresholdFallingThreshold_Type(Unsigned32):
    """Custom type rbnDhcpCtxThresholdFallingThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 196608),
    )


_RbnDhcpCtxThresholdFallingThreshold_Type.__name__ = "Unsigned32"
_RbnDhcpCtxThresholdFallingThreshold_Object = MibScalar
rbnDhcpCtxThresholdFallingThreshold = _RbnDhcpCtxThresholdFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 2, 5),
    _RbnDhcpCtxThresholdFallingThreshold_Type()
)
rbnDhcpCtxThresholdFallingThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnDhcpCtxThresholdFallingThreshold.setStatus("current")
_RbnDhcpCtxThresholdFallingSendTrap_Type = TruthValue
_RbnDhcpCtxThresholdFallingSendTrap_Object = MibScalar
rbnDhcpCtxThresholdFallingSendTrap = _RbnDhcpCtxThresholdFallingSendTrap_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 2, 6),
    _RbnDhcpCtxThresholdFallingSendTrap_Type()
)
rbnDhcpCtxThresholdFallingSendTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnDhcpCtxThresholdFallingSendTrap.setStatus("current")
_RbnDhcpCtxThresholdFallingLogMessage_Type = TruthValue
_RbnDhcpCtxThresholdFallingLogMessage_Object = MibScalar
rbnDhcpCtxThresholdFallingLogMessage = _RbnDhcpCtxThresholdFallingLogMessage_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 2, 7),
    _RbnDhcpCtxThresholdFallingLogMessage_Type()
)
rbnDhcpCtxThresholdFallingLogMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnDhcpCtxThresholdFallingLogMessage.setStatus("current")


class _RbnDhcpCtxThresholdRisingThreshold_Type(Unsigned32):
    """Custom type rbnDhcpCtxThresholdRisingThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 196608),
    )


_RbnDhcpCtxThresholdRisingThreshold_Type.__name__ = "Unsigned32"
_RbnDhcpCtxThresholdRisingThreshold_Object = MibScalar
rbnDhcpCtxThresholdRisingThreshold = _RbnDhcpCtxThresholdRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 2, 8),
    _RbnDhcpCtxThresholdRisingThreshold_Type()
)
rbnDhcpCtxThresholdRisingThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnDhcpCtxThresholdRisingThreshold.setStatus("current")
_RbnDhcpCtxThresholdRisingSendTrap_Type = TruthValue
_RbnDhcpCtxThresholdRisingSendTrap_Object = MibScalar
rbnDhcpCtxThresholdRisingSendTrap = _RbnDhcpCtxThresholdRisingSendTrap_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 2, 9),
    _RbnDhcpCtxThresholdRisingSendTrap_Type()
)
rbnDhcpCtxThresholdRisingSendTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnDhcpCtxThresholdRisingSendTrap.setStatus("current")
_RbnDhcpCtxThresholdRisingLogMessage_Type = TruthValue
_RbnDhcpCtxThresholdRisingLogMessage_Object = MibScalar
rbnDhcpCtxThresholdRisingLogMessage = _RbnDhcpCtxThresholdRisingLogMessage_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 2, 10),
    _RbnDhcpCtxThresholdRisingLogMessage_Type()
)
rbnDhcpCtxThresholdRisingLogMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnDhcpCtxThresholdRisingLogMessage.setStatus("current")
_RbnDhcpRangeThresholdTable_Object = MibTable
rbnDhcpRangeThresholdTable = _RbnDhcpRangeThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 3)
)
if mibBuilder.loadTexts:
    rbnDhcpRangeThresholdTable.setStatus("current")
_RbnDhcpRangeThresholdEntry_Object = MibTableRow
rbnDhcpRangeThresholdEntry = _RbnDhcpRangeThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 3, 1)
)
rbnDhcpRangeThresholdEntry.setIndexNames(
    (0, "RBN-DHCP-MIB", "rbnDhcpRangeThresholdInterfaceIdx"),
    (0, "RBN-DHCP-MIB", "rbnDhcpRangeThresholdAddr"),
)
if mibBuilder.loadTexts:
    rbnDhcpRangeThresholdEntry.setStatus("current")
_RbnDhcpRangeThresholdInterfaceIdx_Type = Unsigned32
_RbnDhcpRangeThresholdInterfaceIdx_Object = MibTableColumn
rbnDhcpRangeThresholdInterfaceIdx = _RbnDhcpRangeThresholdInterfaceIdx_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 3, 1, 1),
    _RbnDhcpRangeThresholdInterfaceIdx_Type()
)
rbnDhcpRangeThresholdInterfaceIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnDhcpRangeThresholdInterfaceIdx.setStatus("current")
_RbnDhcpRangeThresholdAddr_Type = IpAddress
_RbnDhcpRangeThresholdAddr_Object = MibTableColumn
rbnDhcpRangeThresholdAddr = _RbnDhcpRangeThresholdAddr_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 3, 1, 2),
    _RbnDhcpRangeThresholdAddr_Type()
)
rbnDhcpRangeThresholdAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnDhcpRangeThresholdAddr.setStatus("current")
_RbnDhcpRangeThresholdEndAddr_Type = IpAddress
_RbnDhcpRangeThresholdEndAddr_Object = MibTableColumn
rbnDhcpRangeThresholdEndAddr = _RbnDhcpRangeThresholdEndAddr_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 3, 1, 3),
    _RbnDhcpRangeThresholdEndAddr_Type()
)
rbnDhcpRangeThresholdEndAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnDhcpRangeThresholdEndAddr.setStatus("current")


class _RbnDhcpRangeThresholdContextName_Type(SnmpAdminString):
    """Custom type rbnDhcpRangeThresholdContextName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_RbnDhcpRangeThresholdContextName_Type.__name__ = "SnmpAdminString"
_RbnDhcpRangeThresholdContextName_Object = MibTableColumn
rbnDhcpRangeThresholdContextName = _RbnDhcpRangeThresholdContextName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 3, 1, 4),
    _RbnDhcpRangeThresholdContextName_Type()
)
rbnDhcpRangeThresholdContextName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnDhcpRangeThresholdContextName.setStatus("current")


class _RbnDhcpRangeThresholdInterfaceName_Type(SnmpAdminString):
    """Custom type rbnDhcpRangeThresholdInterfaceName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_RbnDhcpRangeThresholdInterfaceName_Type.__name__ = "SnmpAdminString"
_RbnDhcpRangeThresholdInterfaceName_Object = MibTableColumn
rbnDhcpRangeThresholdInterfaceName = _RbnDhcpRangeThresholdInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 3, 1, 5),
    _RbnDhcpRangeThresholdInterfaceName_Type()
)
rbnDhcpRangeThresholdInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnDhcpRangeThresholdInterfaceName.setStatus("current")
_RbnDhcpRangeThresholdSize_Type = Unsigned32
_RbnDhcpRangeThresholdSize_Object = MibTableColumn
rbnDhcpRangeThresholdSize = _RbnDhcpRangeThresholdSize_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 3, 1, 6),
    _RbnDhcpRangeThresholdSize_Type()
)
rbnDhcpRangeThresholdSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnDhcpRangeThresholdSize.setStatus("current")
_RbnDhcpRangeThresholdAvailable_Type = Unsigned32
_RbnDhcpRangeThresholdAvailable_Object = MibTableColumn
rbnDhcpRangeThresholdAvailable = _RbnDhcpRangeThresholdAvailable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 3, 1, 7),
    _RbnDhcpRangeThresholdAvailable_Type()
)
rbnDhcpRangeThresholdAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnDhcpRangeThresholdAvailable.setStatus("current")
_RbnDhcpRangeThresholdInuse_Type = Unsigned32
_RbnDhcpRangeThresholdInuse_Object = MibTableColumn
rbnDhcpRangeThresholdInuse = _RbnDhcpRangeThresholdInuse_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 3, 1, 8),
    _RbnDhcpRangeThresholdInuse_Type()
)
rbnDhcpRangeThresholdInuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnDhcpRangeThresholdInuse.setStatus("current")


class _RbnDhcpRangeThresholdFallingThreshold_Type(Unsigned32):
    """Custom type rbnDhcpRangeThresholdFallingThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 196608),
    )


_RbnDhcpRangeThresholdFallingThreshold_Type.__name__ = "Unsigned32"
_RbnDhcpRangeThresholdFallingThreshold_Object = MibTableColumn
rbnDhcpRangeThresholdFallingThreshold = _RbnDhcpRangeThresholdFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 3, 1, 9),
    _RbnDhcpRangeThresholdFallingThreshold_Type()
)
rbnDhcpRangeThresholdFallingThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnDhcpRangeThresholdFallingThreshold.setStatus("current")
_RbnDhcpRangeThresholdFallingSendTrap_Type = TruthValue
_RbnDhcpRangeThresholdFallingSendTrap_Object = MibTableColumn
rbnDhcpRangeThresholdFallingSendTrap = _RbnDhcpRangeThresholdFallingSendTrap_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 3, 1, 10),
    _RbnDhcpRangeThresholdFallingSendTrap_Type()
)
rbnDhcpRangeThresholdFallingSendTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnDhcpRangeThresholdFallingSendTrap.setStatus("current")
_RbnDhcpRangeThresholdFallingLogMessage_Type = TruthValue
_RbnDhcpRangeThresholdFallingLogMessage_Object = MibTableColumn
rbnDhcpRangeThresholdFallingLogMessage = _RbnDhcpRangeThresholdFallingLogMessage_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 3, 1, 11),
    _RbnDhcpRangeThresholdFallingLogMessage_Type()
)
rbnDhcpRangeThresholdFallingLogMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnDhcpRangeThresholdFallingLogMessage.setStatus("current")


class _RbnDhcpRangeThresholdRisingThreshold_Type(Unsigned32):
    """Custom type rbnDhcpRangeThresholdRisingThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 196608),
    )


_RbnDhcpRangeThresholdRisingThreshold_Type.__name__ = "Unsigned32"
_RbnDhcpRangeThresholdRisingThreshold_Object = MibTableColumn
rbnDhcpRangeThresholdRisingThreshold = _RbnDhcpRangeThresholdRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 3, 1, 12),
    _RbnDhcpRangeThresholdRisingThreshold_Type()
)
rbnDhcpRangeThresholdRisingThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnDhcpRangeThresholdRisingThreshold.setStatus("current")
_RbnDhcpRangeThresholdRisingSendTrap_Type = TruthValue
_RbnDhcpRangeThresholdRisingSendTrap_Object = MibTableColumn
rbnDhcpRangeThresholdRisingSendTrap = _RbnDhcpRangeThresholdRisingSendTrap_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 3, 1, 13),
    _RbnDhcpRangeThresholdRisingSendTrap_Type()
)
rbnDhcpRangeThresholdRisingSendTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnDhcpRangeThresholdRisingSendTrap.setStatus("current")
_RbnDhcpRangeThresholdRisingLogMessage_Type = TruthValue
_RbnDhcpRangeThresholdRisingLogMessage_Object = MibTableColumn
rbnDhcpRangeThresholdRisingLogMessage = _RbnDhcpRangeThresholdRisingLogMessage_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 3, 1, 14),
    _RbnDhcpRangeThresholdRisingLogMessage_Type()
)
rbnDhcpRangeThresholdRisingLogMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnDhcpRangeThresholdRisingLogMessage.setStatus("current")
_RbnDhcpLeaseFileStorageSlot_Type = RbnSlot
_RbnDhcpLeaseFileStorageSlot_Object = MibScalar
rbnDhcpLeaseFileStorageSlot = _RbnDhcpLeaseFileStorageSlot_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 4),
    _RbnDhcpLeaseFileStorageSlot_Type()
)
rbnDhcpLeaseFileStorageSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnDhcpLeaseFileStorageSlot.setStatus("current")


class _RbnDhcpLeaseFileErrorType_Type(Integer32):
    """Custom type rbnDhcpLeaseFileErrorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("storageDeviceDegraded", 1),
          ("storageDeviceFailed", 2))
    )


_RbnDhcpLeaseFileErrorType_Type.__name__ = "Integer32"
_RbnDhcpLeaseFileErrorType_Object = MibScalar
rbnDhcpLeaseFileErrorType = _RbnDhcpLeaseFileErrorType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 5),
    _RbnDhcpLeaseFileErrorType_Type()
)
rbnDhcpLeaseFileErrorType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnDhcpLeaseFileErrorType.setStatus("current")
_RbnDhcpMIBConformance_ObjectIdentity = ObjectIdentity
rbnDhcpMIBConformance = _RbnDhcpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 2)
)
_RbnDhcpCompliances_ObjectIdentity = ObjectIdentity
rbnDhcpCompliances = _RbnDhcpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 2, 1)
)
_RbnDhcpGroups_ObjectIdentity = ObjectIdentity
rbnDhcpGroups = _RbnDhcpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 2, 2)
)

# Managed Objects groups

rbnDhcpThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 2, 2, 1)
)
rbnDhcpThresholdGroup.setObjects(
      *(("RBN-DHCP-MIB", "rbnDhcpIntfThresholdContextName"),
        ("RBN-DHCP-MIB", "rbnDhcpIntfThresholdSize"),
        ("RBN-DHCP-MIB", "rbnDhcpIntfThresholdInuse"),
        ("RBN-DHCP-MIB", "rbnDhcpIntfThresholdAvailable"),
        ("RBN-DHCP-MIB", "rbnDhcpIntfThresholdFallingThreshold"),
        ("RBN-DHCP-MIB", "rbnDhcpIntfThresholdFallingSendTrap"),
        ("RBN-DHCP-MIB", "rbnDhcpIntfThresholdFallingLogMessage"),
        ("RBN-DHCP-MIB", "rbnDhcpIntfThresholdRisingThreshold"),
        ("RBN-DHCP-MIB", "rbnDhcpIntfThresholdRisingSendTrap"),
        ("RBN-DHCP-MIB", "rbnDhcpIntfThresholdRisingLogMessage"),
        ("RBN-DHCP-MIB", "rbnDhcpCtxThresholdName"),
        ("RBN-DHCP-MIB", "rbnDhcpCtxThresholdSize"),
        ("RBN-DHCP-MIB", "rbnDhcpCtxThresholdAvailable"),
        ("RBN-DHCP-MIB", "rbnDhcpCtxThresholdInuse"),
        ("RBN-DHCP-MIB", "rbnDhcpCtxThresholdFallingThreshold"),
        ("RBN-DHCP-MIB", "rbnDhcpCtxThresholdFallingSendTrap"),
        ("RBN-DHCP-MIB", "rbnDhcpCtxThresholdFallingLogMessage"),
        ("RBN-DHCP-MIB", "rbnDhcpCtxThresholdRisingThreshold"),
        ("RBN-DHCP-MIB", "rbnDhcpCtxThresholdRisingSendTrap"),
        ("RBN-DHCP-MIB", "rbnDhcpCtxThresholdRisingLogMessage"))
)
if mibBuilder.loadTexts:
    rbnDhcpThresholdGroup.setStatus("current")

rbnDhcpIntfThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 2, 2, 3)
)
rbnDhcpIntfThresholdGroup.setObjects(
      *(("RBN-DHCP-MIB", "rbnDhcpIntfThresholdSize"),
        ("RBN-DHCP-MIB", "rbnDhcpIntfThresholdInuse"),
        ("RBN-DHCP-MIB", "rbnDhcpIntfThresholdAvailable"),
        ("RBN-DHCP-MIB", "rbnDhcpIntfThresholdFallingThreshold"),
        ("RBN-DHCP-MIB", "rbnDhcpIntfThresholdFallingSendTrap"),
        ("RBN-DHCP-MIB", "rbnDhcpIntfThresholdFallingLogMessage"),
        ("RBN-DHCP-MIB", "rbnDhcpIntfThresholdRisingThreshold"),
        ("RBN-DHCP-MIB", "rbnDhcpIntfThresholdRisingSendTrap"),
        ("RBN-DHCP-MIB", "rbnDhcpIntfThresholdRisingLogMessage"))
)
if mibBuilder.loadTexts:
    rbnDhcpIntfThresholdGroup.setStatus("current")

rbnDhcpCtxThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 2, 2, 4)
)
rbnDhcpCtxThresholdGroup.setObjects(
      *(("RBN-DHCP-MIB", "rbnDhcpCtxThresholdName"),
        ("RBN-DHCP-MIB", "rbnDhcpCtxThresholdSize"),
        ("RBN-DHCP-MIB", "rbnDhcpCtxThresholdAvailable"),
        ("RBN-DHCP-MIB", "rbnDhcpCtxThresholdInuse"),
        ("RBN-DHCP-MIB", "rbnDhcpCtxThresholdFallingThreshold"),
        ("RBN-DHCP-MIB", "rbnDhcpCtxThresholdFallingSendTrap"),
        ("RBN-DHCP-MIB", "rbnDhcpCtxThresholdFallingLogMessage"),
        ("RBN-DHCP-MIB", "rbnDhcpCtxThresholdRisingThreshold"),
        ("RBN-DHCP-MIB", "rbnDhcpCtxThresholdRisingSendTrap"),
        ("RBN-DHCP-MIB", "rbnDhcpCtxThresholdRisingLogMessage"))
)
if mibBuilder.loadTexts:
    rbnDhcpCtxThresholdGroup.setStatus("current")

rbnDhcpRangeThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 2, 2, 5)
)
rbnDhcpRangeThresholdGroup.setObjects(
      *(("RBN-DHCP-MIB", "rbnDhcpRangeThresholdEndAddr"),
        ("RBN-DHCP-MIB", "rbnDhcpRangeThresholdContextName"),
        ("RBN-DHCP-MIB", "rbnDhcpRangeThresholdInterfaceName"),
        ("RBN-DHCP-MIB", "rbnDhcpRangeThresholdSize"),
        ("RBN-DHCP-MIB", "rbnDhcpRangeThresholdInuse"),
        ("RBN-DHCP-MIB", "rbnDhcpRangeThresholdAvailable"),
        ("RBN-DHCP-MIB", "rbnDhcpRangeThresholdFallingThreshold"),
        ("RBN-DHCP-MIB", "rbnDhcpRangeThresholdFallingSendTrap"),
        ("RBN-DHCP-MIB", "rbnDhcpRangeThresholdFallingLogMessage"),
        ("RBN-DHCP-MIB", "rbnDhcpRangeThresholdRisingThreshold"),
        ("RBN-DHCP-MIB", "rbnDhcpRangeThresholdRisingSendTrap"),
        ("RBN-DHCP-MIB", "rbnDhcpRangeThresholdRisingLogMessage"))
)
if mibBuilder.loadTexts:
    rbnDhcpRangeThresholdGroup.setStatus("current")

rbnDhcpLeaseFileFailureTrapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 2, 2, 9)
)
rbnDhcpLeaseFileFailureTrapGroup.setObjects(
      *(("RBN-DHCP-MIB", "rbnDhcpLeaseFileStorageSlot"),
        ("RBN-DHCP-MIB", "rbnDhcpLeaseFileErrorType"))
)
if mibBuilder.loadTexts:
    rbnDhcpLeaseFileFailureTrapGroup.setStatus("current")


# Notification objects

rbnDhcpIntfThresholdFallingThresholdMet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 0, 1)
)
rbnDhcpIntfThresholdFallingThresholdMet.setObjects(
      *(("RBN-DHCP-MIB", "rbnDhcpIntfThresholdContextName"),
        ("RBN-DHCP-MIB", "rbnDhcpIntfThresholdAvailable"),
        ("RBN-DHCP-MIB", "rbnDhcpIntfThresholdFallingThreshold"))
)
if mibBuilder.loadTexts:
    rbnDhcpIntfThresholdFallingThresholdMet.setStatus(
        "current"
    )

rbnDhcpIntfThresholdRisingThresholdMet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 0, 2)
)
rbnDhcpIntfThresholdRisingThresholdMet.setObjects(
      *(("RBN-DHCP-MIB", "rbnDhcpIntfThresholdContextName"),
        ("RBN-DHCP-MIB", "rbnDhcpIntfThresholdAvailable"),
        ("RBN-DHCP-MIB", "rbnDhcpIntfThresholdRisingThreshold"))
)
if mibBuilder.loadTexts:
    rbnDhcpIntfThresholdRisingThresholdMet.setStatus(
        "current"
    )

rbnDhcpCtxThresholdFallingThresholdMet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 0, 3)
)
rbnDhcpCtxThresholdFallingThresholdMet.setObjects(
      *(("RBN-DHCP-MIB", "rbnDhcpCtxThresholdName"),
        ("RBN-DHCP-MIB", "rbnDhcpCtxThresholdAvailable"),
        ("RBN-DHCP-MIB", "rbnDhcpCtxThresholdFallingThreshold"))
)
if mibBuilder.loadTexts:
    rbnDhcpCtxThresholdFallingThresholdMet.setStatus(
        "current"
    )

rbnDhcpCtxThresholdRisingThresholdMet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 0, 4)
)
rbnDhcpCtxThresholdRisingThresholdMet.setObjects(
      *(("RBN-DHCP-MIB", "rbnDhcpCtxThresholdName"),
        ("RBN-DHCP-MIB", "rbnDhcpCtxThresholdAvailable"),
        ("RBN-DHCP-MIB", "rbnDhcpCtxThresholdRisingThreshold"))
)
if mibBuilder.loadTexts:
    rbnDhcpCtxThresholdRisingThresholdMet.setStatus(
        "current"
    )

rbnDhcpRangeThresholdFallingThresholdMet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 0, 5)
)
rbnDhcpRangeThresholdFallingThresholdMet.setObjects(
      *(("RBN-DHCP-MIB", "rbnDhcpRangeThresholdContextName"),
        ("RBN-DHCP-MIB", "rbnDhcpRangeThresholdInterfaceName"),
        ("RBN-DHCP-MIB", "rbnDhcpRangeThresholdEndAddr"),
        ("RBN-DHCP-MIB", "rbnDhcpRangeThresholdAvailable"),
        ("RBN-DHCP-MIB", "rbnDhcpRangeThresholdFallingThreshold"))
)
if mibBuilder.loadTexts:
    rbnDhcpRangeThresholdFallingThresholdMet.setStatus(
        "current"
    )

rbnDhcpRangeThresholdRisingThresholdMet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 0, 6)
)
rbnDhcpRangeThresholdRisingThresholdMet.setObjects(
      *(("RBN-DHCP-MIB", "rbnDhcpRangeThresholdContextName"),
        ("RBN-DHCP-MIB", "rbnDhcpRangeThresholdInterfaceName"),
        ("RBN-DHCP-MIB", "rbnDhcpRangeThresholdEndAddr"),
        ("RBN-DHCP-MIB", "rbnDhcpRangeThresholdAvailable"),
        ("RBN-DHCP-MIB", "rbnDhcpRangeThresholdRisingThreshold"))
)
if mibBuilder.loadTexts:
    rbnDhcpRangeThresholdRisingThresholdMet.setStatus(
        "current"
    )

rbnDhcpLeaseFileFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 0, 7)
)
rbnDhcpLeaseFileFailure.setObjects(
      *(("RBN-DHCP-MIB", "rbnDhcpLeaseFileStorageSlot"),
        ("RBN-DHCP-MIB", "rbnDhcpLeaseFileErrorType"))
)
if mibBuilder.loadTexts:
    rbnDhcpLeaseFileFailure.setStatus(
        "current"
    )


# Notifications groups

rbnDhcpThresholdNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 2, 2, 2)
)
rbnDhcpThresholdNotifyGroup.setObjects(
      *(("RBN-DHCP-MIB", "rbnDhcpIntfThresholdFallingThresholdMet"),
        ("RBN-DHCP-MIB", "rbnDhcpIntfThresholdRisingThresholdMet"),
        ("RBN-DHCP-MIB", "rbnDhcpCtxThresholdFallingThresholdMet"),
        ("RBN-DHCP-MIB", "rbnDhcpCtxThresholdRisingThresholdMet"))
)
if mibBuilder.loadTexts:
    rbnDhcpThresholdNotifyGroup.setStatus(
        "current"
    )

rbnDhcpIntfThresholdNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 2, 2, 6)
)
rbnDhcpIntfThresholdNotifyGroup.setObjects(
      *(("RBN-DHCP-MIB", "rbnDhcpIntfThresholdFallingThresholdMet"),
        ("RBN-DHCP-MIB", "rbnDhcpIntfThresholdRisingThresholdMet"))
)
if mibBuilder.loadTexts:
    rbnDhcpIntfThresholdNotifyGroup.setStatus(
        "current"
    )

rbnDhcpCtxThresholdNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 2, 2, 7)
)
rbnDhcpCtxThresholdNotifyGroup.setObjects(
      *(("RBN-DHCP-MIB", "rbnDhcpCtxThresholdFallingThresholdMet"),
        ("RBN-DHCP-MIB", "rbnDhcpCtxThresholdRisingThresholdMet"))
)
if mibBuilder.loadTexts:
    rbnDhcpCtxThresholdNotifyGroup.setStatus(
        "current"
    )

rbnDhcpRangeThresholdNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 2, 2, 8)
)
rbnDhcpRangeThresholdNotifyGroup.setObjects(
      *(("RBN-DHCP-MIB", "rbnDhcpRangeThresholdFallingThresholdMet"),
        ("RBN-DHCP-MIB", "rbnDhcpRangeThresholdRisingThresholdMet"))
)
if mibBuilder.loadTexts:
    rbnDhcpRangeThresholdNotifyGroup.setStatus(
        "current"
    )

rbnDhcpLeaseFileFailureNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 2, 2, 10)
)
rbnDhcpLeaseFileFailureNotifyGroup.setObjects(
    ("RBN-DHCP-MIB", "rbnDhcpLeaseFileFailure")
)
if mibBuilder.loadTexts:
    rbnDhcpLeaseFileFailureNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

rbnDhcpThresholdCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rbnDhcpThresholdCompliance.setStatus(
        "current"
    )

rbnDhcpThresholdCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 2, 1, 2)
)
if mibBuilder.loadTexts:
    rbnDhcpThresholdCompliance2.setStatus(
        "deprecated"
    )

rbnDhcpThresholdCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 30, 2, 1, 3)
)
if mibBuilder.loadTexts:
    rbnDhcpThresholdCompliance3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-DHCP-MIB",
    **{"rbnDhcpMib": rbnDhcpMib,
       "rbnDhcpMIBNotifications": rbnDhcpMIBNotifications,
       "rbnDhcpIntfThresholdFallingThresholdMet": rbnDhcpIntfThresholdFallingThresholdMet,
       "rbnDhcpIntfThresholdRisingThresholdMet": rbnDhcpIntfThresholdRisingThresholdMet,
       "rbnDhcpCtxThresholdFallingThresholdMet": rbnDhcpCtxThresholdFallingThresholdMet,
       "rbnDhcpCtxThresholdRisingThresholdMet": rbnDhcpCtxThresholdRisingThresholdMet,
       "rbnDhcpRangeThresholdFallingThresholdMet": rbnDhcpRangeThresholdFallingThresholdMet,
       "rbnDhcpRangeThresholdRisingThresholdMet": rbnDhcpRangeThresholdRisingThresholdMet,
       "rbnDhcpLeaseFileFailure": rbnDhcpLeaseFileFailure,
       "rbnDhcpMIBObjects": rbnDhcpMIBObjects,
       "rbnDhcpIntfThresholdTable": rbnDhcpIntfThresholdTable,
       "rbnDhcpIntfThresholdEntry": rbnDhcpIntfThresholdEntry,
       "rbnDhcpIntfThresholdName": rbnDhcpIntfThresholdName,
       "rbnDhcpIntfThresholdContextName": rbnDhcpIntfThresholdContextName,
       "rbnDhcpIntfThresholdSize": rbnDhcpIntfThresholdSize,
       "rbnDhcpIntfThresholdAvailable": rbnDhcpIntfThresholdAvailable,
       "rbnDhcpIntfThresholdInuse": rbnDhcpIntfThresholdInuse,
       "rbnDhcpIntfThresholdFallingThreshold": rbnDhcpIntfThresholdFallingThreshold,
       "rbnDhcpIntfThresholdFallingSendTrap": rbnDhcpIntfThresholdFallingSendTrap,
       "rbnDhcpIntfThresholdFallingLogMessage": rbnDhcpIntfThresholdFallingLogMessage,
       "rbnDhcpIntfThresholdRisingThreshold": rbnDhcpIntfThresholdRisingThreshold,
       "rbnDhcpIntfThresholdRisingSendTrap": rbnDhcpIntfThresholdRisingSendTrap,
       "rbnDhcpIntfThresholdRisingLogMessage": rbnDhcpIntfThresholdRisingLogMessage,
       "rbnDhcpCtxThreshold": rbnDhcpCtxThreshold,
       "rbnDhcpCtxThresholdName": rbnDhcpCtxThresholdName,
       "rbnDhcpCtxThresholdSize": rbnDhcpCtxThresholdSize,
       "rbnDhcpCtxThresholdAvailable": rbnDhcpCtxThresholdAvailable,
       "rbnDhcpCtxThresholdInuse": rbnDhcpCtxThresholdInuse,
       "rbnDhcpCtxThresholdFallingThreshold": rbnDhcpCtxThresholdFallingThreshold,
       "rbnDhcpCtxThresholdFallingSendTrap": rbnDhcpCtxThresholdFallingSendTrap,
       "rbnDhcpCtxThresholdFallingLogMessage": rbnDhcpCtxThresholdFallingLogMessage,
       "rbnDhcpCtxThresholdRisingThreshold": rbnDhcpCtxThresholdRisingThreshold,
       "rbnDhcpCtxThresholdRisingSendTrap": rbnDhcpCtxThresholdRisingSendTrap,
       "rbnDhcpCtxThresholdRisingLogMessage": rbnDhcpCtxThresholdRisingLogMessage,
       "rbnDhcpRangeThresholdTable": rbnDhcpRangeThresholdTable,
       "rbnDhcpRangeThresholdEntry": rbnDhcpRangeThresholdEntry,
       "rbnDhcpRangeThresholdInterfaceIdx": rbnDhcpRangeThresholdInterfaceIdx,
       "rbnDhcpRangeThresholdAddr": rbnDhcpRangeThresholdAddr,
       "rbnDhcpRangeThresholdEndAddr": rbnDhcpRangeThresholdEndAddr,
       "rbnDhcpRangeThresholdContextName": rbnDhcpRangeThresholdContextName,
       "rbnDhcpRangeThresholdInterfaceName": rbnDhcpRangeThresholdInterfaceName,
       "rbnDhcpRangeThresholdSize": rbnDhcpRangeThresholdSize,
       "rbnDhcpRangeThresholdAvailable": rbnDhcpRangeThresholdAvailable,
       "rbnDhcpRangeThresholdInuse": rbnDhcpRangeThresholdInuse,
       "rbnDhcpRangeThresholdFallingThreshold": rbnDhcpRangeThresholdFallingThreshold,
       "rbnDhcpRangeThresholdFallingSendTrap": rbnDhcpRangeThresholdFallingSendTrap,
       "rbnDhcpRangeThresholdFallingLogMessage": rbnDhcpRangeThresholdFallingLogMessage,
       "rbnDhcpRangeThresholdRisingThreshold": rbnDhcpRangeThresholdRisingThreshold,
       "rbnDhcpRangeThresholdRisingSendTrap": rbnDhcpRangeThresholdRisingSendTrap,
       "rbnDhcpRangeThresholdRisingLogMessage": rbnDhcpRangeThresholdRisingLogMessage,
       "rbnDhcpLeaseFileStorageSlot": rbnDhcpLeaseFileStorageSlot,
       "rbnDhcpLeaseFileErrorType": rbnDhcpLeaseFileErrorType,
       "rbnDhcpMIBConformance": rbnDhcpMIBConformance,
       "rbnDhcpCompliances": rbnDhcpCompliances,
       "rbnDhcpThresholdCompliance": rbnDhcpThresholdCompliance,
       "rbnDhcpThresholdCompliance2": rbnDhcpThresholdCompliance2,
       "rbnDhcpThresholdCompliance3": rbnDhcpThresholdCompliance3,
       "rbnDhcpGroups": rbnDhcpGroups,
       "rbnDhcpThresholdGroup": rbnDhcpThresholdGroup,
       "rbnDhcpThresholdNotifyGroup": rbnDhcpThresholdNotifyGroup,
       "rbnDhcpIntfThresholdGroup": rbnDhcpIntfThresholdGroup,
       "rbnDhcpCtxThresholdGroup": rbnDhcpCtxThresholdGroup,
       "rbnDhcpRangeThresholdGroup": rbnDhcpRangeThresholdGroup,
       "rbnDhcpIntfThresholdNotifyGroup": rbnDhcpIntfThresholdNotifyGroup,
       "rbnDhcpCtxThresholdNotifyGroup": rbnDhcpCtxThresholdNotifyGroup,
       "rbnDhcpRangeThresholdNotifyGroup": rbnDhcpRangeThresholdNotifyGroup,
       "rbnDhcpLeaseFileFailureTrapGroup": rbnDhcpLeaseFileFailureTrapGroup,
       "rbnDhcpLeaseFileFailureNotifyGroup": rbnDhcpLeaseFileFailureNotifyGroup}
)
