# SNMP MIB module (XEDIA-DHCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEDIA-DHCP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:45 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(xediaMibs,) = mibBuilder.importSymbols(
    "XEDIA-REG",
    "xediaMibs")


# MODULE-IDENTITY

xediaDhcpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 28)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XdhcpObjects_ObjectIdentity = ObjectIdentity
xdhcpObjects = _XdhcpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 28, 1)
)
_XdhcpRelay_ObjectIdentity = ObjectIdentity
xdhcpRelay = _XdhcpRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 28, 1, 1)
)


class _XdhcpRelayMode_Type(Integer32):
    """Custom type xdhcpRelayMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_XdhcpRelayMode_Type.__name__ = "Integer32"
_XdhcpRelayMode_Object = MibScalar
xdhcpRelayMode = _XdhcpRelayMode_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 28, 1, 1, 1),
    _XdhcpRelayMode_Type()
)
xdhcpRelayMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdhcpRelayMode.setStatus("current")


class _XdhcpRelayMaxHops_Type(Integer32):
    """Custom type xdhcpRelayMaxHops based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_XdhcpRelayMaxHops_Type.__name__ = "Integer32"
_XdhcpRelayMaxHops_Object = MibScalar
xdhcpRelayMaxHops = _XdhcpRelayMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 28, 1, 1, 2),
    _XdhcpRelayMaxHops_Type()
)
xdhcpRelayMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdhcpRelayMaxHops.setStatus("current")


class _XdhcpRelayIncludeCircuitID_Type(TruthValue):
    """Custom type xdhcpRelayIncludeCircuitID based on TruthValue"""


_XdhcpRelayIncludeCircuitID_Object = MibScalar
xdhcpRelayIncludeCircuitID = _XdhcpRelayIncludeCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 28, 1, 1, 3),
    _XdhcpRelayIncludeCircuitID_Type()
)
xdhcpRelayIncludeCircuitID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdhcpRelayIncludeCircuitID.setStatus("current")
_XdhcpRelayDestTable_Object = MibTable
xdhcpRelayDestTable = _XdhcpRelayDestTable_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 28, 1, 1, 10)
)
if mibBuilder.loadTexts:
    xdhcpRelayDestTable.setStatus("current")
_XdhcpRelayDestEntry_Object = MibTableRow
xdhcpRelayDestEntry = _XdhcpRelayDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 28, 1, 1, 10, 1)
)
xdhcpRelayDestEntry.setIndexNames(
    (0, "XEDIA-DHCP-MIB", "xdhcpRelayDestIndex"),
)
if mibBuilder.loadTexts:
    xdhcpRelayDestEntry.setStatus("current")


class _XdhcpRelayDestIndex_Type(Integer32):
    """Custom type xdhcpRelayDestIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_XdhcpRelayDestIndex_Type.__name__ = "Integer32"
_XdhcpRelayDestIndex_Object = MibTableColumn
xdhcpRelayDestIndex = _XdhcpRelayDestIndex_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 28, 1, 1, 10, 1, 1),
    _XdhcpRelayDestIndex_Type()
)
xdhcpRelayDestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdhcpRelayDestIndex.setStatus("current")
_XdhcpRelayDestination_Type = DisplayString
_XdhcpRelayDestination_Object = MibTableColumn
xdhcpRelayDestination = _XdhcpRelayDestination_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 28, 1, 1, 10, 1, 2),
    _XdhcpRelayDestination_Type()
)
xdhcpRelayDestination.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdhcpRelayDestination.setStatus("current")


class _XdhcpRelayDestOperAddress_Type(IpAddress):
    """Custom type xdhcpRelayDestOperAddress based on IpAddress"""
    defaultHexValue = "00000000"


_XdhcpRelayDestOperAddress_Object = MibTableColumn
xdhcpRelayDestOperAddress = _XdhcpRelayDestOperAddress_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 28, 1, 1, 10, 1, 3),
    _XdhcpRelayDestOperAddress_Type()
)
xdhcpRelayDestOperAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdhcpRelayDestOperAddress.setStatus("current")
_XdhcpRelayDestRequests_Type = Counter32
_XdhcpRelayDestRequests_Object = MibTableColumn
xdhcpRelayDestRequests = _XdhcpRelayDestRequests_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 28, 1, 1, 10, 1, 4),
    _XdhcpRelayDestRequests_Type()
)
xdhcpRelayDestRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdhcpRelayDestRequests.setStatus("current")
_XdhcpRelayDestReplies_Type = Counter32
_XdhcpRelayDestReplies_Object = MibTableColumn
xdhcpRelayDestReplies = _XdhcpRelayDestReplies_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 28, 1, 1, 10, 1, 5),
    _XdhcpRelayDestReplies_Type()
)
xdhcpRelayDestReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdhcpRelayDestReplies.setStatus("current")


class _XdhcpRelayDestProtocol_Type(Integer32):
    """Custom type xdhcpRelayDestProtocol based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bootp", 2),
          ("dhcp", 1),
          ("dhcpAndBootp", 3))
    )


_XdhcpRelayDestProtocol_Type.__name__ = "Integer32"
_XdhcpRelayDestProtocol_Object = MibTableColumn
xdhcpRelayDestProtocol = _XdhcpRelayDestProtocol_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 28, 1, 1, 10, 1, 6),
    _XdhcpRelayDestProtocol_Type()
)
xdhcpRelayDestProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdhcpRelayDestProtocol.setStatus("current")
_XdhcpRelayDestRowStatus_Type = RowStatus
_XdhcpRelayDestRowStatus_Object = MibTableColumn
xdhcpRelayDestRowStatus = _XdhcpRelayDestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 28, 1, 1, 10, 1, 7),
    _XdhcpRelayDestRowStatus_Type()
)
xdhcpRelayDestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdhcpRelayDestRowStatus.setStatus("current")


class _XdhcpRelayDestInterface_Type(DisplayString):
    """Custom type xdhcpRelayDestInterface based on DisplayString"""
    defaultValue = OctetString("all")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_XdhcpRelayDestInterface_Type.__name__ = "DisplayString"
_XdhcpRelayDestInterface_Object = MibTableColumn
xdhcpRelayDestInterface = _XdhcpRelayDestInterface_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 28, 1, 1, 10, 1, 8),
    _XdhcpRelayDestInterface_Type()
)
xdhcpRelayDestInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdhcpRelayDestInterface.setStatus("current")
_XdhcpConformance_ObjectIdentity = ObjectIdentity
xdhcpConformance = _XdhcpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 28, 2)
)
_XdhcpCompliances_ObjectIdentity = ObjectIdentity
xdhcpCompliances = _XdhcpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 28, 2, 1)
)
_XdhcpGroups_ObjectIdentity = ObjectIdentity
xdhcpGroups = _XdhcpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 28, 2, 2)
)

# Managed Objects groups

xdhcpAllGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 838, 3, 28, 2, 2, 1)
)
xdhcpAllGroup.setObjects(
      *(("XEDIA-DHCP-MIB", "xdhcpRelayMode"),
        ("XEDIA-DHCP-MIB", "xdhcpRelayMaxHops"),
        ("XEDIA-DHCP-MIB", "xdhcpRelayIncludeCircuitID"),
        ("XEDIA-DHCP-MIB", "xdhcpRelayDestination"),
        ("XEDIA-DHCP-MIB", "xdhcpRelayDestOperAddress"),
        ("XEDIA-DHCP-MIB", "xdhcpRelayDestRequests"),
        ("XEDIA-DHCP-MIB", "xdhcpRelayDestReplies"),
        ("XEDIA-DHCP-MIB", "xdhcpRelayDestProtocol"),
        ("XEDIA-DHCP-MIB", "xdhcpRelayDestRowStatus"),
        ("XEDIA-DHCP-MIB", "xdhcpRelayDestInterface"))
)
if mibBuilder.loadTexts:
    xdhcpAllGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

xdhcpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 838, 3, 28, 2, 1, 1)
)
if mibBuilder.loadTexts:
    xdhcpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEDIA-DHCP-MIB",
    **{"xediaDhcpMIB": xediaDhcpMIB,
       "xdhcpObjects": xdhcpObjects,
       "xdhcpRelay": xdhcpRelay,
       "xdhcpRelayMode": xdhcpRelayMode,
       "xdhcpRelayMaxHops": xdhcpRelayMaxHops,
       "xdhcpRelayIncludeCircuitID": xdhcpRelayIncludeCircuitID,
       "xdhcpRelayDestTable": xdhcpRelayDestTable,
       "xdhcpRelayDestEntry": xdhcpRelayDestEntry,
       "xdhcpRelayDestIndex": xdhcpRelayDestIndex,
       "xdhcpRelayDestination": xdhcpRelayDestination,
       "xdhcpRelayDestOperAddress": xdhcpRelayDestOperAddress,
       "xdhcpRelayDestRequests": xdhcpRelayDestRequests,
       "xdhcpRelayDestReplies": xdhcpRelayDestReplies,
       "xdhcpRelayDestProtocol": xdhcpRelayDestProtocol,
       "xdhcpRelayDestRowStatus": xdhcpRelayDestRowStatus,
       "xdhcpRelayDestInterface": xdhcpRelayDestInterface,
       "xdhcpConformance": xdhcpConformance,
       "xdhcpCompliances": xdhcpCompliances,
       "xdhcpCompliance": xdhcpCompliance,
       "xdhcpGroups": xdhcpGroups,
       "xdhcpAllGroup": xdhcpAllGroup}
)
