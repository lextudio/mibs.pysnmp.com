# SNMP MIB module (RADLAN-DHCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADLAN-DHCP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:37:36 2024
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

(rnd,) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rnd")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rsDHCP = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 38)
)
rsDHCP.setRevisions(
        ("2003-10-18 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RsDhcpMibVersion_Type = Integer32
_RsDhcpMibVersion_Object = MibScalar
rsDhcpMibVersion = _RsDhcpMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 14),
    _RsDhcpMibVersion_Type()
)
rsDhcpMibVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDhcpMibVersion.setStatus("current")
_RlDhcpRelayEnable_Type = TruthValue
_RlDhcpRelayEnable_Object = MibScalar
rlDhcpRelayEnable = _RlDhcpRelayEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 25),
    _RlDhcpRelayEnable_Type()
)
rlDhcpRelayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpRelayEnable.setStatus("current")
_RlDhcpRelayExists_Type = TruthValue
_RlDhcpRelayExists_Object = MibScalar
rlDhcpRelayExists = _RlDhcpRelayExists_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 26),
    _RlDhcpRelayExists_Type()
)
rlDhcpRelayExists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpRelayExists.setStatus("current")
_RlDhcpRelayNextServerTable_Object = MibTable
rlDhcpRelayNextServerTable = _RlDhcpRelayNextServerTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 27)
)
if mibBuilder.loadTexts:
    rlDhcpRelayNextServerTable.setStatus("current")
_RlDhcpRelayNextServerEntry_Object = MibTableRow
rlDhcpRelayNextServerEntry = _RlDhcpRelayNextServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 27, 1)
)
rlDhcpRelayNextServerEntry.setIndexNames(
    (0, "RADLAN-DHCP-MIB", "rlDhcpRelayNextServerIpAddr"),
)
if mibBuilder.loadTexts:
    rlDhcpRelayNextServerEntry.setStatus("current")
_RlDhcpRelayNextServerIpAddr_Type = IpAddress
_RlDhcpRelayNextServerIpAddr_Object = MibTableColumn
rlDhcpRelayNextServerIpAddr = _RlDhcpRelayNextServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 27, 1, 1),
    _RlDhcpRelayNextServerIpAddr_Type()
)
rlDhcpRelayNextServerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpRelayNextServerIpAddr.setStatus("current")
_RlDhcpRelayNextServerSecThreshold_Type = Unsigned32
_RlDhcpRelayNextServerSecThreshold_Object = MibTableColumn
rlDhcpRelayNextServerSecThreshold = _RlDhcpRelayNextServerSecThreshold_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 27, 1, 2),
    _RlDhcpRelayNextServerSecThreshold_Type()
)
rlDhcpRelayNextServerSecThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpRelayNextServerSecThreshold.setStatus("current")
_RlDhcpRelayNextServerRowStatus_Type = RowStatus
_RlDhcpRelayNextServerRowStatus_Object = MibTableColumn
rlDhcpRelayNextServerRowStatus = _RlDhcpRelayNextServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 27, 1, 3),
    _RlDhcpRelayNextServerRowStatus_Type()
)
rlDhcpRelayNextServerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpRelayNextServerRowStatus.setStatus("current")
_RlDhcpSrvEnable_Type = TruthValue
_RlDhcpSrvEnable_Object = MibScalar
rlDhcpSrvEnable = _RlDhcpSrvEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 30),
    _RlDhcpSrvEnable_Type()
)
rlDhcpSrvEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvEnable.setStatus("current")
_RlDhcpSrvExists_Type = TruthValue
_RlDhcpSrvExists_Object = MibScalar
rlDhcpSrvExists = _RlDhcpSrvExists_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 31),
    _RlDhcpSrvExists_Type()
)
rlDhcpSrvExists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpSrvExists.setStatus("current")


class _RlDhcpSrvDbLocation_Type(Integer32):
    """Custom type rlDhcpSrvDbLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flash", 2),
          ("nvram", 1))
    )


_RlDhcpSrvDbLocation_Type.__name__ = "Integer32"
_RlDhcpSrvDbLocation_Object = MibScalar
rlDhcpSrvDbLocation = _RlDhcpSrvDbLocation_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 32),
    _RlDhcpSrvDbLocation_Type()
)
rlDhcpSrvDbLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpSrvDbLocation.setStatus("current")
_RlDhcpSrvMaxNumOfClients_Type = Unsigned32
_RlDhcpSrvMaxNumOfClients_Object = MibScalar
rlDhcpSrvMaxNumOfClients = _RlDhcpSrvMaxNumOfClients_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 33),
    _RlDhcpSrvMaxNumOfClients_Type()
)
rlDhcpSrvMaxNumOfClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpSrvMaxNumOfClients.setStatus("current")
_RlDhcpSrvDbNumOfActiveEntries_Type = Unsigned32
_RlDhcpSrvDbNumOfActiveEntries_Object = MibScalar
rlDhcpSrvDbNumOfActiveEntries = _RlDhcpSrvDbNumOfActiveEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 34),
    _RlDhcpSrvDbNumOfActiveEntries_Type()
)
rlDhcpSrvDbNumOfActiveEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpSrvDbNumOfActiveEntries.setStatus("current")
_RlDhcpSrvDbErase_Type = TruthValue
_RlDhcpSrvDbErase_Object = MibScalar
rlDhcpSrvDbErase = _RlDhcpSrvDbErase_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 35),
    _RlDhcpSrvDbErase_Type()
)
rlDhcpSrvDbErase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvDbErase.setStatus("current")
_RlDhcpSrvProbeEnable_Type = TruthValue
_RlDhcpSrvProbeEnable_Object = MibScalar
rlDhcpSrvProbeEnable = _RlDhcpSrvProbeEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 36),
    _RlDhcpSrvProbeEnable_Type()
)
rlDhcpSrvProbeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvProbeEnable.setStatus("current")


class _RlDhcpSrvProbeTimeout_Type(Unsigned32):
    """Custom type rlDhcpSrvProbeTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 10000),
    )


_RlDhcpSrvProbeTimeout_Type.__name__ = "Unsigned32"
_RlDhcpSrvProbeTimeout_Object = MibScalar
rlDhcpSrvProbeTimeout = _RlDhcpSrvProbeTimeout_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 37),
    _RlDhcpSrvProbeTimeout_Type()
)
rlDhcpSrvProbeTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvProbeTimeout.setStatus("current")


class _RlDhcpSrvProbeRetries_Type(Unsigned32):
    """Custom type rlDhcpSrvProbeRetries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_RlDhcpSrvProbeRetries_Type.__name__ = "Unsigned32"
_RlDhcpSrvProbeRetries_Object = MibScalar
rlDhcpSrvProbeRetries = _RlDhcpSrvProbeRetries_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 38),
    _RlDhcpSrvProbeRetries_Type()
)
rlDhcpSrvProbeRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvProbeRetries.setStatus("current")
_RlDhcpSrvIpAddrTable_Object = MibTable
rlDhcpSrvIpAddrTable = _RlDhcpSrvIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 45)
)
if mibBuilder.loadTexts:
    rlDhcpSrvIpAddrTable.setStatus("current")
_RlDhcpSrvIpAddrEntry_Object = MibTableRow
rlDhcpSrvIpAddrEntry = _RlDhcpSrvIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 45, 1)
)
rlDhcpSrvIpAddrEntry.setIndexNames(
    (0, "RADLAN-DHCP-MIB", "rlDhcpSrvIpAddrIpAddr"),
)
if mibBuilder.loadTexts:
    rlDhcpSrvIpAddrEntry.setStatus("current")
_RlDhcpSrvIpAddrIpAddr_Type = IpAddress
_RlDhcpSrvIpAddrIpAddr_Object = MibTableColumn
rlDhcpSrvIpAddrIpAddr = _RlDhcpSrvIpAddrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 45, 1, 1),
    _RlDhcpSrvIpAddrIpAddr_Type()
)
rlDhcpSrvIpAddrIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvIpAddrIpAddr.setStatus("current")
_RlDhcpSrvIpAddrIpNetMask_Type = IpAddress
_RlDhcpSrvIpAddrIpNetMask_Object = MibTableColumn
rlDhcpSrvIpAddrIpNetMask = _RlDhcpSrvIpAddrIpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 45, 1, 2),
    _RlDhcpSrvIpAddrIpNetMask_Type()
)
rlDhcpSrvIpAddrIpNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvIpAddrIpNetMask.setStatus("current")


class _RlDhcpSrvIpAddrIdentifier_Type(OctetString):
    """Custom type rlDhcpSrvIpAddrIdentifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlDhcpSrvIpAddrIdentifier_Type.__name__ = "OctetString"
_RlDhcpSrvIpAddrIdentifier_Object = MibTableColumn
rlDhcpSrvIpAddrIdentifier = _RlDhcpSrvIpAddrIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 45, 1, 3),
    _RlDhcpSrvIpAddrIdentifier_Type()
)
rlDhcpSrvIpAddrIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvIpAddrIdentifier.setStatus("current")


class _RlDhcpSrvIpAddrIdentifierType_Type(Integer32):
    """Custom type rlDhcpSrvIpAddrIdentifierType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clientId", 2),
          ("physAddr", 1))
    )


_RlDhcpSrvIpAddrIdentifierType_Type.__name__ = "Integer32"
_RlDhcpSrvIpAddrIdentifierType_Object = MibTableColumn
rlDhcpSrvIpAddrIdentifierType = _RlDhcpSrvIpAddrIdentifierType_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 45, 1, 4),
    _RlDhcpSrvIpAddrIdentifierType_Type()
)
rlDhcpSrvIpAddrIdentifierType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvIpAddrIdentifierType.setStatus("current")


class _RlDhcpSrvIpAddrClnHostName_Type(SnmpAdminString):
    """Custom type rlDhcpSrvIpAddrClnHostName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlDhcpSrvIpAddrClnHostName_Type.__name__ = "SnmpAdminString"
_RlDhcpSrvIpAddrClnHostName_Object = MibTableColumn
rlDhcpSrvIpAddrClnHostName = _RlDhcpSrvIpAddrClnHostName_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 45, 1, 5),
    _RlDhcpSrvIpAddrClnHostName_Type()
)
rlDhcpSrvIpAddrClnHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvIpAddrClnHostName.setStatus("current")


class _RlDhcpSrvIpAddrMechanism_Type(Integer32):
    """Custom type rlDhcpSrvIpAddrMechanism based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 2),
          ("dynamic", 3),
          ("manual", 1))
    )


_RlDhcpSrvIpAddrMechanism_Type.__name__ = "Integer32"
_RlDhcpSrvIpAddrMechanism_Object = MibTableColumn
rlDhcpSrvIpAddrMechanism = _RlDhcpSrvIpAddrMechanism_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 45, 1, 6),
    _RlDhcpSrvIpAddrMechanism_Type()
)
rlDhcpSrvIpAddrMechanism.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvIpAddrMechanism.setStatus("current")
_RlDhcpSrvIpAddrAgeTime_Type = Unsigned32
_RlDhcpSrvIpAddrAgeTime_Object = MibTableColumn
rlDhcpSrvIpAddrAgeTime = _RlDhcpSrvIpAddrAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 45, 1, 7),
    _RlDhcpSrvIpAddrAgeTime_Type()
)
rlDhcpSrvIpAddrAgeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpSrvIpAddrAgeTime.setStatus("current")


class _RlDhcpSrvIpAddrPoolName_Type(DisplayString):
    """Custom type rlDhcpSrvIpAddrPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlDhcpSrvIpAddrPoolName_Type.__name__ = "DisplayString"
_RlDhcpSrvIpAddrPoolName_Object = MibTableColumn
rlDhcpSrvIpAddrPoolName = _RlDhcpSrvIpAddrPoolName_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 45, 1, 8),
    _RlDhcpSrvIpAddrPoolName_Type()
)
rlDhcpSrvIpAddrPoolName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvIpAddrPoolName.setStatus("current")


class _RlDhcpSrvIpAddrConfParamsName_Type(DisplayString):
    """Custom type rlDhcpSrvIpAddrConfParamsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlDhcpSrvIpAddrConfParamsName_Type.__name__ = "DisplayString"
_RlDhcpSrvIpAddrConfParamsName_Object = MibTableColumn
rlDhcpSrvIpAddrConfParamsName = _RlDhcpSrvIpAddrConfParamsName_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 45, 1, 9),
    _RlDhcpSrvIpAddrConfParamsName_Type()
)
rlDhcpSrvIpAddrConfParamsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvIpAddrConfParamsName.setStatus("current")
_RlDhcpSrvIpAddrRowStatus_Type = RowStatus
_RlDhcpSrvIpAddrRowStatus_Object = MibTableColumn
rlDhcpSrvIpAddrRowStatus = _RlDhcpSrvIpAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 45, 1, 10),
    _RlDhcpSrvIpAddrRowStatus_Type()
)
rlDhcpSrvIpAddrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvIpAddrRowStatus.setStatus("current")
_RlDhcpSrvDynamicTable_Object = MibTable
rlDhcpSrvDynamicTable = _RlDhcpSrvDynamicTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 46)
)
if mibBuilder.loadTexts:
    rlDhcpSrvDynamicTable.setStatus("current")
_RlDhcpSrvDynamicEntry_Object = MibTableRow
rlDhcpSrvDynamicEntry = _RlDhcpSrvDynamicEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 46, 1)
)
rlDhcpSrvDynamicEntry.setIndexNames(
    (0, "RADLAN-DHCP-MIB", "rlDhcpSrvDynamicPoolName"),
)
if mibBuilder.loadTexts:
    rlDhcpSrvDynamicEntry.setStatus("current")


class _RlDhcpSrvDynamicPoolName_Type(DisplayString):
    """Custom type rlDhcpSrvDynamicPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlDhcpSrvDynamicPoolName_Type.__name__ = "DisplayString"
_RlDhcpSrvDynamicPoolName_Object = MibTableColumn
rlDhcpSrvDynamicPoolName = _RlDhcpSrvDynamicPoolName_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 46, 1, 1),
    _RlDhcpSrvDynamicPoolName_Type()
)
rlDhcpSrvDynamicPoolName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvDynamicPoolName.setStatus("current")
_RlDhcpSrvDynamicIpAddrFrom_Type = IpAddress
_RlDhcpSrvDynamicIpAddrFrom_Object = MibTableColumn
rlDhcpSrvDynamicIpAddrFrom = _RlDhcpSrvDynamicIpAddrFrom_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 46, 1, 2),
    _RlDhcpSrvDynamicIpAddrFrom_Type()
)
rlDhcpSrvDynamicIpAddrFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvDynamicIpAddrFrom.setStatus("current")
_RlDhcpSrvDynamicIpAddrTo_Type = IpAddress
_RlDhcpSrvDynamicIpAddrTo_Object = MibTableColumn
rlDhcpSrvDynamicIpAddrTo = _RlDhcpSrvDynamicIpAddrTo_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 46, 1, 3),
    _RlDhcpSrvDynamicIpAddrTo_Type()
)
rlDhcpSrvDynamicIpAddrTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvDynamicIpAddrTo.setStatus("current")
_RlDhcpSrvDynamicIpNetMask_Type = IpAddress
_RlDhcpSrvDynamicIpNetMask_Object = MibTableColumn
rlDhcpSrvDynamicIpNetMask = _RlDhcpSrvDynamicIpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 46, 1, 4),
    _RlDhcpSrvDynamicIpNetMask_Type()
)
rlDhcpSrvDynamicIpNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvDynamicIpNetMask.setStatus("current")
_RlDhcpSrvDynamicLeaseTime_Type = Unsigned32
_RlDhcpSrvDynamicLeaseTime_Object = MibTableColumn
rlDhcpSrvDynamicLeaseTime = _RlDhcpSrvDynamicLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 46, 1, 5),
    _RlDhcpSrvDynamicLeaseTime_Type()
)
rlDhcpSrvDynamicLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvDynamicLeaseTime.setStatus("current")
_RlDhcpSrvDynamicProbeEnable_Type = TruthValue
_RlDhcpSrvDynamicProbeEnable_Object = MibTableColumn
rlDhcpSrvDynamicProbeEnable = _RlDhcpSrvDynamicProbeEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 46, 1, 6),
    _RlDhcpSrvDynamicProbeEnable_Type()
)
rlDhcpSrvDynamicProbeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvDynamicProbeEnable.setStatus("current")
_RlDhcpSrvDynamicTotalNumOfAddr_Type = Unsigned32
_RlDhcpSrvDynamicTotalNumOfAddr_Object = MibTableColumn
rlDhcpSrvDynamicTotalNumOfAddr = _RlDhcpSrvDynamicTotalNumOfAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 46, 1, 7),
    _RlDhcpSrvDynamicTotalNumOfAddr_Type()
)
rlDhcpSrvDynamicTotalNumOfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpSrvDynamicTotalNumOfAddr.setStatus("current")
_RlDhcpSrvDynamicFreeNumOfAddr_Type = Unsigned32
_RlDhcpSrvDynamicFreeNumOfAddr_Object = MibTableColumn
rlDhcpSrvDynamicFreeNumOfAddr = _RlDhcpSrvDynamicFreeNumOfAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 46, 1, 8),
    _RlDhcpSrvDynamicFreeNumOfAddr_Type()
)
rlDhcpSrvDynamicFreeNumOfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpSrvDynamicFreeNumOfAddr.setStatus("current")


class _RlDhcpSrvDynamicConfParamsName_Type(DisplayString):
    """Custom type rlDhcpSrvDynamicConfParamsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlDhcpSrvDynamicConfParamsName_Type.__name__ = "DisplayString"
_RlDhcpSrvDynamicConfParamsName_Object = MibTableColumn
rlDhcpSrvDynamicConfParamsName = _RlDhcpSrvDynamicConfParamsName_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 46, 1, 9),
    _RlDhcpSrvDynamicConfParamsName_Type()
)
rlDhcpSrvDynamicConfParamsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvDynamicConfParamsName.setStatus("current")
_RlDhcpSrvDynamicRowStatus_Type = RowStatus
_RlDhcpSrvDynamicRowStatus_Object = MibTableColumn
rlDhcpSrvDynamicRowStatus = _RlDhcpSrvDynamicRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 46, 1, 10),
    _RlDhcpSrvDynamicRowStatus_Type()
)
rlDhcpSrvDynamicRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvDynamicRowStatus.setStatus("current")
_RlDhcpSrvConfParamsTable_Object = MibTable
rlDhcpSrvConfParamsTable = _RlDhcpSrvConfParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 47)
)
if mibBuilder.loadTexts:
    rlDhcpSrvConfParamsTable.setStatus("current")
_RlDhcpSrvConfParamsEntry_Object = MibTableRow
rlDhcpSrvConfParamsEntry = _RlDhcpSrvConfParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 47, 1)
)
rlDhcpSrvConfParamsEntry.setIndexNames(
    (0, "RADLAN-DHCP-MIB", "rlDhcpSrvConfParamsName"),
)
if mibBuilder.loadTexts:
    rlDhcpSrvConfParamsEntry.setStatus("current")


class _RlDhcpSrvConfParamsName_Type(DisplayString):
    """Custom type rlDhcpSrvConfParamsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlDhcpSrvConfParamsName_Type.__name__ = "DisplayString"
_RlDhcpSrvConfParamsName_Object = MibTableColumn
rlDhcpSrvConfParamsName = _RlDhcpSrvConfParamsName_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 47, 1, 1),
    _RlDhcpSrvConfParamsName_Type()
)
rlDhcpSrvConfParamsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvConfParamsName.setStatus("current")
_RlDhcpSrvConfParamsNextServerIp_Type = IpAddress
_RlDhcpSrvConfParamsNextServerIp_Object = MibTableColumn
rlDhcpSrvConfParamsNextServerIp = _RlDhcpSrvConfParamsNextServerIp_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 47, 1, 2),
    _RlDhcpSrvConfParamsNextServerIp_Type()
)
rlDhcpSrvConfParamsNextServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvConfParamsNextServerIp.setStatus("current")


class _RlDhcpSrvConfParamsNextServerName_Type(DisplayString):
    """Custom type rlDhcpSrvConfParamsNextServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RlDhcpSrvConfParamsNextServerName_Type.__name__ = "DisplayString"
_RlDhcpSrvConfParamsNextServerName_Object = MibTableColumn
rlDhcpSrvConfParamsNextServerName = _RlDhcpSrvConfParamsNextServerName_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 47, 1, 3),
    _RlDhcpSrvConfParamsNextServerName_Type()
)
rlDhcpSrvConfParamsNextServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvConfParamsNextServerName.setStatus("current")


class _RlDhcpSrvConfParamsBootfileName_Type(DisplayString):
    """Custom type rlDhcpSrvConfParamsBootfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlDhcpSrvConfParamsBootfileName_Type.__name__ = "DisplayString"
_RlDhcpSrvConfParamsBootfileName_Object = MibTableColumn
rlDhcpSrvConfParamsBootfileName = _RlDhcpSrvConfParamsBootfileName_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 47, 1, 4),
    _RlDhcpSrvConfParamsBootfileName_Type()
)
rlDhcpSrvConfParamsBootfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvConfParamsBootfileName.setStatus("current")
_RlDhcpSrvConfParamsRoutersList_Type = DisplayString
_RlDhcpSrvConfParamsRoutersList_Object = MibTableColumn
rlDhcpSrvConfParamsRoutersList = _RlDhcpSrvConfParamsRoutersList_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 47, 1, 5),
    _RlDhcpSrvConfParamsRoutersList_Type()
)
rlDhcpSrvConfParamsRoutersList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvConfParamsRoutersList.setStatus("current")
_RlDhcpSrvConfParamsTimeSrvList_Type = DisplayString
_RlDhcpSrvConfParamsTimeSrvList_Object = MibTableColumn
rlDhcpSrvConfParamsTimeSrvList = _RlDhcpSrvConfParamsTimeSrvList_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 47, 1, 6),
    _RlDhcpSrvConfParamsTimeSrvList_Type()
)
rlDhcpSrvConfParamsTimeSrvList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvConfParamsTimeSrvList.setStatus("current")
_RlDhcpSrvConfParamsDnsList_Type = DisplayString
_RlDhcpSrvConfParamsDnsList_Object = MibTableColumn
rlDhcpSrvConfParamsDnsList = _RlDhcpSrvConfParamsDnsList_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 47, 1, 7),
    _RlDhcpSrvConfParamsDnsList_Type()
)
rlDhcpSrvConfParamsDnsList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvConfParamsDnsList.setStatus("current")


class _RlDhcpSrvConfParamsDomainName_Type(SnmpAdminString):
    """Custom type rlDhcpSrvConfParamsDomainName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlDhcpSrvConfParamsDomainName_Type.__name__ = "SnmpAdminString"
_RlDhcpSrvConfParamsDomainName_Object = MibTableColumn
rlDhcpSrvConfParamsDomainName = _RlDhcpSrvConfParamsDomainName_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 47, 1, 8),
    _RlDhcpSrvConfParamsDomainName_Type()
)
rlDhcpSrvConfParamsDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvConfParamsDomainName.setStatus("current")
_RlDhcpSrvConfParamsNetbiosNameList_Type = DisplayString
_RlDhcpSrvConfParamsNetbiosNameList_Object = MibTableColumn
rlDhcpSrvConfParamsNetbiosNameList = _RlDhcpSrvConfParamsNetbiosNameList_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 47, 1, 9),
    _RlDhcpSrvConfParamsNetbiosNameList_Type()
)
rlDhcpSrvConfParamsNetbiosNameList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvConfParamsNetbiosNameList.setStatus("current")


class _RlDhcpSrvConfParamsNetbiosNodeType_Type(Integer32):
    """Custom type rlDhcpSrvConfParamsNetbiosNodeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("b-node", 1),
          ("h-node", 8),
          ("m-node", 4),
          ("p-node", 2))
    )


_RlDhcpSrvConfParamsNetbiosNodeType_Type.__name__ = "Integer32"
_RlDhcpSrvConfParamsNetbiosNodeType_Object = MibTableColumn
rlDhcpSrvConfParamsNetbiosNodeType = _RlDhcpSrvConfParamsNetbiosNodeType_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 47, 1, 10),
    _RlDhcpSrvConfParamsNetbiosNodeType_Type()
)
rlDhcpSrvConfParamsNetbiosNodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvConfParamsNetbiosNodeType.setStatus("current")


class _RlDhcpSrvConfParamsCommunity_Type(DisplayString):
    """Custom type rlDhcpSrvConfParamsCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlDhcpSrvConfParamsCommunity_Type.__name__ = "DisplayString"
_RlDhcpSrvConfParamsCommunity_Object = MibTableColumn
rlDhcpSrvConfParamsCommunity = _RlDhcpSrvConfParamsCommunity_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 47, 1, 11),
    _RlDhcpSrvConfParamsCommunity_Type()
)
rlDhcpSrvConfParamsCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvConfParamsCommunity.setStatus("current")
_RlDhcpSrvConfParamsNmsIp_Type = IpAddress
_RlDhcpSrvConfParamsNmsIp_Object = MibTableColumn
rlDhcpSrvConfParamsNmsIp = _RlDhcpSrvConfParamsNmsIp_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 47, 1, 12),
    _RlDhcpSrvConfParamsNmsIp_Type()
)
rlDhcpSrvConfParamsNmsIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvConfParamsNmsIp.setStatus("current")
_RlDhcpSrvConfParamsOptionsList_Type = DisplayString
_RlDhcpSrvConfParamsOptionsList_Object = MibTableColumn
rlDhcpSrvConfParamsOptionsList = _RlDhcpSrvConfParamsOptionsList_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 47, 1, 13),
    _RlDhcpSrvConfParamsOptionsList_Type()
)
rlDhcpSrvConfParamsOptionsList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvConfParamsOptionsList.setStatus("current")
_RlDhcpSrvConfParamsRowStatus_Type = RowStatus
_RlDhcpSrvConfParamsRowStatus_Object = MibTableColumn
rlDhcpSrvConfParamsRowStatus = _RlDhcpSrvConfParamsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 38, 47, 1, 14),
    _RlDhcpSrvConfParamsRowStatus_Type()
)
rlDhcpSrvConfParamsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvConfParamsRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-DHCP-MIB",
    **{"rsDHCP": rsDHCP,
       "rsDhcpMibVersion": rsDhcpMibVersion,
       "rlDhcpRelayEnable": rlDhcpRelayEnable,
       "rlDhcpRelayExists": rlDhcpRelayExists,
       "rlDhcpRelayNextServerTable": rlDhcpRelayNextServerTable,
       "rlDhcpRelayNextServerEntry": rlDhcpRelayNextServerEntry,
       "rlDhcpRelayNextServerIpAddr": rlDhcpRelayNextServerIpAddr,
       "rlDhcpRelayNextServerSecThreshold": rlDhcpRelayNextServerSecThreshold,
       "rlDhcpRelayNextServerRowStatus": rlDhcpRelayNextServerRowStatus,
       "rlDhcpSrvEnable": rlDhcpSrvEnable,
       "rlDhcpSrvExists": rlDhcpSrvExists,
       "rlDhcpSrvDbLocation": rlDhcpSrvDbLocation,
       "rlDhcpSrvMaxNumOfClients": rlDhcpSrvMaxNumOfClients,
       "rlDhcpSrvDbNumOfActiveEntries": rlDhcpSrvDbNumOfActiveEntries,
       "rlDhcpSrvDbErase": rlDhcpSrvDbErase,
       "rlDhcpSrvProbeEnable": rlDhcpSrvProbeEnable,
       "rlDhcpSrvProbeTimeout": rlDhcpSrvProbeTimeout,
       "rlDhcpSrvProbeRetries": rlDhcpSrvProbeRetries,
       "rlDhcpSrvIpAddrTable": rlDhcpSrvIpAddrTable,
       "rlDhcpSrvIpAddrEntry": rlDhcpSrvIpAddrEntry,
       "rlDhcpSrvIpAddrIpAddr": rlDhcpSrvIpAddrIpAddr,
       "rlDhcpSrvIpAddrIpNetMask": rlDhcpSrvIpAddrIpNetMask,
       "rlDhcpSrvIpAddrIdentifier": rlDhcpSrvIpAddrIdentifier,
       "rlDhcpSrvIpAddrIdentifierType": rlDhcpSrvIpAddrIdentifierType,
       "rlDhcpSrvIpAddrClnHostName": rlDhcpSrvIpAddrClnHostName,
       "rlDhcpSrvIpAddrMechanism": rlDhcpSrvIpAddrMechanism,
       "rlDhcpSrvIpAddrAgeTime": rlDhcpSrvIpAddrAgeTime,
       "rlDhcpSrvIpAddrPoolName": rlDhcpSrvIpAddrPoolName,
       "rlDhcpSrvIpAddrConfParamsName": rlDhcpSrvIpAddrConfParamsName,
       "rlDhcpSrvIpAddrRowStatus": rlDhcpSrvIpAddrRowStatus,
       "rlDhcpSrvDynamicTable": rlDhcpSrvDynamicTable,
       "rlDhcpSrvDynamicEntry": rlDhcpSrvDynamicEntry,
       "rlDhcpSrvDynamicPoolName": rlDhcpSrvDynamicPoolName,
       "rlDhcpSrvDynamicIpAddrFrom": rlDhcpSrvDynamicIpAddrFrom,
       "rlDhcpSrvDynamicIpAddrTo": rlDhcpSrvDynamicIpAddrTo,
       "rlDhcpSrvDynamicIpNetMask": rlDhcpSrvDynamicIpNetMask,
       "rlDhcpSrvDynamicLeaseTime": rlDhcpSrvDynamicLeaseTime,
       "rlDhcpSrvDynamicProbeEnable": rlDhcpSrvDynamicProbeEnable,
       "rlDhcpSrvDynamicTotalNumOfAddr": rlDhcpSrvDynamicTotalNumOfAddr,
       "rlDhcpSrvDynamicFreeNumOfAddr": rlDhcpSrvDynamicFreeNumOfAddr,
       "rlDhcpSrvDynamicConfParamsName": rlDhcpSrvDynamicConfParamsName,
       "rlDhcpSrvDynamicRowStatus": rlDhcpSrvDynamicRowStatus,
       "rlDhcpSrvConfParamsTable": rlDhcpSrvConfParamsTable,
       "rlDhcpSrvConfParamsEntry": rlDhcpSrvConfParamsEntry,
       "rlDhcpSrvConfParamsName": rlDhcpSrvConfParamsName,
       "rlDhcpSrvConfParamsNextServerIp": rlDhcpSrvConfParamsNextServerIp,
       "rlDhcpSrvConfParamsNextServerName": rlDhcpSrvConfParamsNextServerName,
       "rlDhcpSrvConfParamsBootfileName": rlDhcpSrvConfParamsBootfileName,
       "rlDhcpSrvConfParamsRoutersList": rlDhcpSrvConfParamsRoutersList,
       "rlDhcpSrvConfParamsTimeSrvList": rlDhcpSrvConfParamsTimeSrvList,
       "rlDhcpSrvConfParamsDnsList": rlDhcpSrvConfParamsDnsList,
       "rlDhcpSrvConfParamsDomainName": rlDhcpSrvConfParamsDomainName,
       "rlDhcpSrvConfParamsNetbiosNameList": rlDhcpSrvConfParamsNetbiosNameList,
       "rlDhcpSrvConfParamsNetbiosNodeType": rlDhcpSrvConfParamsNetbiosNodeType,
       "rlDhcpSrvConfParamsCommunity": rlDhcpSrvConfParamsCommunity,
       "rlDhcpSrvConfParamsNmsIp": rlDhcpSrvConfParamsNmsIp,
       "rlDhcpSrvConfParamsOptionsList": rlDhcpSrvConfParamsOptionsList,
       "rlDhcpSrvConfParamsRowStatus": rlDhcpSrvConfParamsRowStatus}
)
