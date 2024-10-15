# SNMP MIB module (ALCATEL-IND1-VRRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-VRRP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:37:36 2024
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

(softentIND1Vrrp,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1Vrrp")

(alaVrrp3OperEntry,
 alaVrrp3OperIpVersion,
 alaVrrp3OperVrId) = mibBuilder.importSymbols(
    "ALCATEL-IND1-VRRP3-MIB",
    "alaVrrp3OperEntry",
    "alaVrrp3OperIpVersion",
    "alaVrrp3OperVrId")

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(vrrpOperEntry,
 vrrpOperVrId) = mibBuilder.importSymbols(
    "VRRP-MIB",
    "vrrpOperEntry",
    "vrrpOperVrId")


# MODULE-IDENTITY

alcatelIND1VRRPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1)
)
alcatelIND1VRRPMIB.setRevisions(
        ("2007-04-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AlaVrTrackId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



class AlaVrGroupId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1VRRPMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1VRRPMIBObjects = _AlcatelIND1VRRPMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1)
)
_AlaVRRPConfig_ObjectIdentity = ObjectIdentity
alaVRRPConfig = _AlaVRRPConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 1)
)


class _AlaVRRPStartDelay_Type(Integer32):
    """Custom type alaVRRPStartDelay based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 180),
    )


_AlaVRRPStartDelay_Type.__name__ = "Integer32"
_AlaVRRPStartDelay_Object = MibScalar
alaVRRPStartDelay = _AlaVRRPStartDelay_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 1, 1),
    _AlaVRRPStartDelay_Type()
)
alaVRRPStartDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVRRPStartDelay.setStatus("current")
if mibBuilder.loadTexts:
    alaVRRPStartDelay.setUnits("seconds")


class _AlaVrrpBfdStatus_Type(Integer32):
    """Custom type alaVrrpBfdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AlaVrrpBfdStatus_Type.__name__ = "Integer32"
_AlaVrrpBfdStatus_Object = MibScalar
alaVrrpBfdStatus = _AlaVrrpBfdStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 1, 2),
    _AlaVrrpBfdStatus_Type()
)
alaVrrpBfdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVrrpBfdStatus.setStatus("current")
_AlaVrrpTracking_ObjectIdentity = ObjectIdentity
alaVrrpTracking = _AlaVrrpTracking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 2)
)
_AlaVrrpTrackTable_Object = MibTable
alaVrrpTrackTable = _AlaVrrpTrackTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alaVrrpTrackTable.setStatus("current")
_AlaVrrpTrackEntry_Object = MibTableRow
alaVrrpTrackEntry = _AlaVrrpTrackEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 2, 1, 1)
)
alaVrrpTrackEntry.setIndexNames(
    (0, "ALCATEL-IND1-VRRP-MIB", "alaVrrpTrackId"),
)
if mibBuilder.loadTexts:
    alaVrrpTrackEntry.setStatus("current")
_AlaVrrpTrackId_Type = AlaVrTrackId
_AlaVrrpTrackId_Object = MibTableColumn
alaVrrpTrackId = _AlaVrrpTrackId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 2, 1, 1, 1),
    _AlaVrrpTrackId_Type()
)
alaVrrpTrackId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaVrrpTrackId.setStatus("current")


class _AlaVrrpTrackState_Type(Integer32):
    """Custom type alaVrrpTrackState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_AlaVrrpTrackState_Type.__name__ = "Integer32"
_AlaVrrpTrackState_Object = MibTableColumn
alaVrrpTrackState = _AlaVrrpTrackState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 2, 1, 1, 2),
    _AlaVrrpTrackState_Type()
)
alaVrrpTrackState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVrrpTrackState.setStatus("current")


class _AlaVrrpTrackAdminState_Type(Integer32):
    """Custom type alaVrrpTrackAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AlaVrrpTrackAdminState_Type.__name__ = "Integer32"
_AlaVrrpTrackAdminState_Object = MibTableColumn
alaVrrpTrackAdminState = _AlaVrrpTrackAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 2, 1, 1, 3),
    _AlaVrrpTrackAdminState_Type()
)
alaVrrpTrackAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaVrrpTrackAdminState.setStatus("current")


class _AlaVrrpTrackEntityType_Type(Integer32):
    """Custom type alaVrrpTrackEntityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("interface", 4),
          ("ipaddress", 3),
          ("ipv6Interface", 5),
          ("port", 2))
    )


_AlaVrrpTrackEntityType_Type.__name__ = "Integer32"
_AlaVrrpTrackEntityType_Object = MibTableColumn
alaVrrpTrackEntityType = _AlaVrrpTrackEntityType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 2, 1, 1, 4),
    _AlaVrrpTrackEntityType_Type()
)
alaVrrpTrackEntityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVrrpTrackEntityType.setStatus("current")
_AlaVrrpTrackEntityPort_Type = InterfaceIndexOrZero
_AlaVrrpTrackEntityPort_Object = MibTableColumn
alaVrrpTrackEntityPort = _AlaVrrpTrackEntityPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 2, 1, 1, 6),
    _AlaVrrpTrackEntityPort_Type()
)
alaVrrpTrackEntityPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaVrrpTrackEntityPort.setStatus("current")


class _AlaVrrpTrackPriority_Type(Integer32):
    """Custom type alaVrrpTrackPriority based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaVrrpTrackPriority_Type.__name__ = "Integer32"
_AlaVrrpTrackPriority_Object = MibTableColumn
alaVrrpTrackPriority = _AlaVrrpTrackPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 2, 1, 1, 8),
    _AlaVrrpTrackPriority_Type()
)
alaVrrpTrackPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaVrrpTrackPriority.setStatus("current")
_AlaVrrpTrackRowStatus_Type = RowStatus
_AlaVrrpTrackRowStatus_Object = MibTableColumn
alaVrrpTrackRowStatus = _AlaVrrpTrackRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 2, 1, 1, 9),
    _AlaVrrpTrackRowStatus_Type()
)
alaVrrpTrackRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaVrrpTrackRowStatus.setStatus("current")
_AlaVrrpTrackEntityInterface_Type = InterfaceIndexOrZero
_AlaVrrpTrackEntityInterface_Object = MibTableColumn
alaVrrpTrackEntityInterface = _AlaVrrpTrackEntityInterface_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 2, 1, 1, 10),
    _AlaVrrpTrackEntityInterface_Type()
)
alaVrrpTrackEntityInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaVrrpTrackEntityInterface.setStatus("current")
_AlaVrrpTrackEntityIpv6Interface_Type = InterfaceIndexOrZero
_AlaVrrpTrackEntityIpv6Interface_Object = MibTableColumn
alaVrrpTrackEntityIpv6Interface = _AlaVrrpTrackEntityIpv6Interface_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 2, 1, 1, 11),
    _AlaVrrpTrackEntityIpv6Interface_Type()
)
alaVrrpTrackEntityIpv6Interface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaVrrpTrackEntityIpv6Interface.setStatus("current")
_AlaVrrpTrackEntityIpAddrType_Type = InetAddressType
_AlaVrrpTrackEntityIpAddrType_Object = MibTableColumn
alaVrrpTrackEntityIpAddrType = _AlaVrrpTrackEntityIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 2, 1, 1, 12),
    _AlaVrrpTrackEntityIpAddrType_Type()
)
alaVrrpTrackEntityIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaVrrpTrackEntityIpAddrType.setStatus("current")
_AlaVrrpTrackEntityIpAddr_Type = InetAddress
_AlaVrrpTrackEntityIpAddr_Object = MibTableColumn
alaVrrpTrackEntityIpAddr = _AlaVrrpTrackEntityIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 2, 1, 1, 13),
    _AlaVrrpTrackEntityIpAddr_Type()
)
alaVrrpTrackEntityIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaVrrpTrackEntityIpAddr.setStatus("current")


class _AlaVrrpTrackBfdStatus_Type(Integer32):
    """Custom type alaVrrpTrackBfdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AlaVrrpTrackBfdStatus_Type.__name__ = "Integer32"
_AlaVrrpTrackBfdStatus_Object = MibTableColumn
alaVrrpTrackBfdStatus = _AlaVrrpTrackBfdStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 2, 1, 1, 14),
    _AlaVrrpTrackBfdStatus_Type()
)
alaVrrpTrackBfdStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaVrrpTrackBfdStatus.setStatus("current")
_AlaVrrpAssoTrackTable_Object = MibTable
alaVrrpAssoTrackTable = _AlaVrrpAssoTrackTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alaVrrpAssoTrackTable.setStatus("current")
_AlaVrrpAssoTrackEntry_Object = MibTableRow
alaVrrpAssoTrackEntry = _AlaVrrpAssoTrackEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 2, 2, 1)
)
alaVrrpAssoTrackEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VRRP-MIB", "vrrpOperVrId"),
    (0, "ALCATEL-IND1-VRRP-MIB", "alaVrrpAssoTrackId"),
)
if mibBuilder.loadTexts:
    alaVrrpAssoTrackEntry.setStatus("current")
_AlaVrrpAssoTrackId_Type = AlaVrTrackId
_AlaVrrpAssoTrackId_Object = MibTableColumn
alaVrrpAssoTrackId = _AlaVrrpAssoTrackId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 2, 2, 1, 1),
    _AlaVrrpAssoTrackId_Type()
)
alaVrrpAssoTrackId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaVrrpAssoTrackId.setStatus("current")
_AlaVrrpAssoTrackRowStatus_Type = RowStatus
_AlaVrrpAssoTrackRowStatus_Object = MibTableColumn
alaVrrpAssoTrackRowStatus = _AlaVrrpAssoTrackRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 2, 2, 1, 2),
    _AlaVrrpAssoTrackRowStatus_Type()
)
alaVrrpAssoTrackRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaVrrpAssoTrackRowStatus.setStatus("current")
_AlaVrrp3AssoTrackTable_Object = MibTable
alaVrrp3AssoTrackTable = _AlaVrrp3AssoTrackTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    alaVrrp3AssoTrackTable.setStatus("current")
_AlaVrrp3AssoTrackEntry_Object = MibTableRow
alaVrrp3AssoTrackEntry = _AlaVrrp3AssoTrackEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 2, 3, 1)
)
alaVrrp3AssoTrackEntry.setIndexNames(
    (0, "ALCATEL-IND1-VRRP3-MIB", "alaVrrp3OperIpVersion"),
    (0, "ALCATEL-IND1-VRRP3-MIB", "alaVrrp3OperVrId"),
    (0, "IF-MIB", "ifIndex"),
    (0, "ALCATEL-IND1-VRRP-MIB", "alaVrrp3AssoTrackId"),
)
if mibBuilder.loadTexts:
    alaVrrp3AssoTrackEntry.setStatus("current")
_AlaVrrp3AssoTrackId_Type = AlaVrTrackId
_AlaVrrp3AssoTrackId_Object = MibTableColumn
alaVrrp3AssoTrackId = _AlaVrrp3AssoTrackId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 2, 3, 1, 1),
    _AlaVrrp3AssoTrackId_Type()
)
alaVrrp3AssoTrackId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaVrrp3AssoTrackId.setStatus("current")
_AlaVrrp3AssoTrackRowStatus_Type = RowStatus
_AlaVrrp3AssoTrackRowStatus_Object = MibTableColumn
alaVrrp3AssoTrackRowStatus = _AlaVrrp3AssoTrackRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 2, 3, 1, 2),
    _AlaVrrp3AssoTrackRowStatus_Type()
)
alaVrrp3AssoTrackRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaVrrp3AssoTrackRowStatus.setStatus("current")
_AlaVrrpOperations_ObjectIdentity = ObjectIdentity
alaVrrpOperations = _AlaVrrpOperations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 3)
)
_AlaVrrpOperTable_Object = MibTable
alaVrrpOperTable = _AlaVrrpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    alaVrrpOperTable.setStatus("current")
_AlaVrrpOperEntry_Object = MibTableRow
alaVrrpOperEntry = _AlaVrrpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    alaVrrpOperEntry.setStatus("current")


class _AlaVrrpCurrentPriority_Type(Integer32):
    """Custom type alaVrrpCurrentPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaVrrpCurrentPriority_Type.__name__ = "Integer32"
_AlaVrrpCurrentPriority_Object = MibTableColumn
alaVrrpCurrentPriority = _AlaVrrpCurrentPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 3, 1, 1, 1),
    _AlaVrrpCurrentPriority_Type()
)
alaVrrpCurrentPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVrrpCurrentPriority.setStatus("current")
_AlaVrrpTrackCount_Type = Integer32
_AlaVrrpTrackCount_Object = MibTableColumn
alaVrrpTrackCount = _AlaVrrpTrackCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 3, 1, 1, 2),
    _AlaVrrpTrackCount_Type()
)
alaVrrpTrackCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVrrpTrackCount.setStatus("current")


class _AlaVrrpGroupIdent_Type(Integer32):
    """Custom type alaVrrpGroupIdent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaVrrpGroupIdent_Type.__name__ = "Integer32"
_AlaVrrpGroupIdent_Object = MibTableColumn
alaVrrpGroupIdent = _AlaVrrpGroupIdent_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 3, 1, 1, 3),
    _AlaVrrpGroupIdent_Type()
)
alaVrrpGroupIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVrrpGroupIdent.setStatus("current")
_AlaVrrp3OperExTable_Object = MibTable
alaVrrp3OperExTable = _AlaVrrp3OperExTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    alaVrrp3OperExTable.setStatus("current")
_AlaVrrp3OperExEntry_Object = MibTableRow
alaVrrp3OperExEntry = _AlaVrrp3OperExEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    alaVrrp3OperExEntry.setStatus("current")


class _AlaVrrp3CurrentPriority_Type(Integer32):
    """Custom type alaVrrp3CurrentPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaVrrp3CurrentPriority_Type.__name__ = "Integer32"
_AlaVrrp3CurrentPriority_Object = MibTableColumn
alaVrrp3CurrentPriority = _AlaVrrp3CurrentPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 3, 2, 1, 1),
    _AlaVrrp3CurrentPriority_Type()
)
alaVrrp3CurrentPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVrrp3CurrentPriority.setStatus("current")
_AlaVrrp3TrackCount_Type = Integer32
_AlaVrrp3TrackCount_Object = MibTableColumn
alaVrrp3TrackCount = _AlaVrrp3TrackCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 3, 2, 1, 2),
    _AlaVrrp3TrackCount_Type()
)
alaVrrp3TrackCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVrrp3TrackCount.setStatus("current")


class _AlaVrrp3GroupIdent_Type(Integer32):
    """Custom type alaVrrp3GroupIdent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaVrrp3GroupIdent_Type.__name__ = "Integer32"
_AlaVrrp3GroupIdent_Object = MibTableColumn
alaVrrp3GroupIdent = _AlaVrrp3GroupIdent_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 3, 2, 1, 3),
    _AlaVrrp3GroupIdent_Type()
)
alaVrrp3GroupIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVrrp3GroupIdent.setStatus("current")
_AlaVRRPv2Config_ObjectIdentity = ObjectIdentity
alaVRRPv2Config = _AlaVRRPv2Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 4)
)


class _AlaVRRPDefaultInterval_Type(Integer32):
    """Custom type alaVRRPDefaultInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AlaVRRPDefaultInterval_Type.__name__ = "Integer32"
_AlaVRRPDefaultInterval_Object = MibScalar
alaVRRPDefaultInterval = _AlaVRRPDefaultInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 4, 1),
    _AlaVRRPDefaultInterval_Type()
)
alaVRRPDefaultInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVRRPDefaultInterval.setStatus("current")
if mibBuilder.loadTexts:
    alaVRRPDefaultInterval.setUnits("seconds")


class _AlaVRRPDefaultPriority_Type(Integer32):
    """Custom type alaVRRPDefaultPriority based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_AlaVRRPDefaultPriority_Type.__name__ = "Integer32"
_AlaVRRPDefaultPriority_Object = MibScalar
alaVRRPDefaultPriority = _AlaVRRPDefaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 4, 2),
    _AlaVRRPDefaultPriority_Type()
)
alaVRRPDefaultPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVRRPDefaultPriority.setStatus("current")


class _AlaVRRPDefaultPreemptMode_Type(TruthValue):
    """Custom type alaVRRPDefaultPreemptMode based on TruthValue"""


_AlaVRRPDefaultPreemptMode_Object = MibScalar
alaVRRPDefaultPreemptMode = _AlaVRRPDefaultPreemptMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 4, 3),
    _AlaVRRPDefaultPreemptMode_Type()
)
alaVRRPDefaultPreemptMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVRRPDefaultPreemptMode.setStatus("current")


class _AlaVRRPAdminState_Type(Integer32):
    """Custom type alaVRRPAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allEnable", 1),
          ("disable", 3),
          ("enable", 2))
    )


_AlaVRRPAdminState_Type.__name__ = "Integer32"
_AlaVRRPAdminState_Object = MibScalar
alaVRRPAdminState = _AlaVRRPAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 4, 4),
    _AlaVRRPAdminState_Type()
)
alaVRRPAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVRRPAdminState.setStatus("current")


class _AlaVRRPSetParam_Type(Integer32):
    """Custom type alaVRRPSetParam based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("all", 2),
          ("interval", 3),
          ("none", 1),
          ("preempt", 5),
          ("priority", 4))
    )


_AlaVRRPSetParam_Type.__name__ = "Integer32"
_AlaVRRPSetParam_Object = MibScalar
alaVRRPSetParam = _AlaVRRPSetParam_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 4, 5),
    _AlaVRRPSetParam_Type()
)
alaVRRPSetParam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVRRPSetParam.setStatus("current")
_AlaVRRPOverride_Type = TruthValue
_AlaVRRPOverride_Object = MibScalar
alaVRRPOverride = _AlaVRRPOverride_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 4, 6),
    _AlaVRRPOverride_Type()
)
alaVRRPOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVRRPOverride.setStatus("current")
_AlaVrrpGroup_ObjectIdentity = ObjectIdentity
alaVrrpGroup = _AlaVrrpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 5)
)
_AlaVrrpGroupTable_Object = MibTable
alaVrrpGroupTable = _AlaVrrpGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    alaVrrpGroupTable.setStatus("current")
_AlaVrrpGroupEntry_Object = MibTableRow
alaVrrpGroupEntry = _AlaVrrpGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 5, 1, 1)
)
alaVrrpGroupEntry.setIndexNames(
    (0, "ALCATEL-IND1-VRRP-MIB", "alaVrrpGroupId"),
)
if mibBuilder.loadTexts:
    alaVrrpGroupEntry.setStatus("current")
_AlaVrrpGroupId_Type = AlaVrGroupId
_AlaVrrpGroupId_Object = MibTableColumn
alaVrrpGroupId = _AlaVrrpGroupId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 5, 1, 1, 1),
    _AlaVrrpGroupId_Type()
)
alaVrrpGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaVrrpGroupId.setStatus("current")


class _AlaVrrpGroupInterval_Type(Integer32):
    """Custom type alaVrrpGroupInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AlaVrrpGroupInterval_Type.__name__ = "Integer32"
_AlaVrrpGroupInterval_Object = MibTableColumn
alaVrrpGroupInterval = _AlaVrrpGroupInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 5, 1, 1, 2),
    _AlaVrrpGroupInterval_Type()
)
alaVrrpGroupInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaVrrpGroupInterval.setStatus("current")
if mibBuilder.loadTexts:
    alaVrrpGroupInterval.setUnits("seconds")


class _AlaVrrpGroupPriority_Type(Integer32):
    """Custom type alaVrrpGroupPriority based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_AlaVrrpGroupPriority_Type.__name__ = "Integer32"
_AlaVrrpGroupPriority_Object = MibTableColumn
alaVrrpGroupPriority = _AlaVrrpGroupPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 5, 1, 1, 3),
    _AlaVrrpGroupPriority_Type()
)
alaVrrpGroupPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaVrrpGroupPriority.setStatus("current")


class _AlaVrrpGroupPreemptMode_Type(TruthValue):
    """Custom type alaVrrpGroupPreemptMode based on TruthValue"""


_AlaVrrpGroupPreemptMode_Object = MibTableColumn
alaVrrpGroupPreemptMode = _AlaVrrpGroupPreemptMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 5, 1, 1, 4),
    _AlaVrrpGroupPreemptMode_Type()
)
alaVrrpGroupPreemptMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaVrrpGroupPreemptMode.setStatus("current")


class _AlaVrrpGroupAdminState_Type(Integer32):
    """Custom type alaVrrpGroupAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allEnable", 1),
          ("disable", 3),
          ("enable", 2))
    )


_AlaVrrpGroupAdminState_Type.__name__ = "Integer32"
_AlaVrrpGroupAdminState_Object = MibTableColumn
alaVrrpGroupAdminState = _AlaVrrpGroupAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 5, 1, 1, 5),
    _AlaVrrpGroupAdminState_Type()
)
alaVrrpGroupAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaVrrpGroupAdminState.setStatus("current")


class _AlaVrrpGroupSetParam_Type(Integer32):
    """Custom type alaVrrpGroupSetParam based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("all", 2),
          ("interval", 3),
          ("none", 1),
          ("preempt", 5),
          ("priority", 4))
    )


_AlaVrrpGroupSetParam_Type.__name__ = "Integer32"
_AlaVrrpGroupSetParam_Object = MibTableColumn
alaVrrpGroupSetParam = _AlaVrrpGroupSetParam_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 5, 1, 1, 6),
    _AlaVrrpGroupSetParam_Type()
)
alaVrrpGroupSetParam.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaVrrpGroupSetParam.setStatus("current")
_AlaVrrpGroupOverride_Type = TruthValue
_AlaVrrpGroupOverride_Object = MibTableColumn
alaVrrpGroupOverride = _AlaVrrpGroupOverride_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 5, 1, 1, 7),
    _AlaVrrpGroupOverride_Type()
)
alaVrrpGroupOverride.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaVrrpGroupOverride.setStatus("current")
_AlaVrrpGroupRowStatus_Type = RowStatus
_AlaVrrpGroupRowStatus_Object = MibTableColumn
alaVrrpGroupRowStatus = _AlaVrrpGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 5, 1, 1, 8),
    _AlaVrrpGroupRowStatus_Type()
)
alaVrrpGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaVrrpGroupRowStatus.setStatus("current")
_AlaVrrpAssoGroupTable_Object = MibTable
alaVrrpAssoGroupTable = _AlaVrrpAssoGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 5, 2)
)
if mibBuilder.loadTexts:
    alaVrrpAssoGroupTable.setStatus("current")
_AlaVrrpAssoGroupEntry_Object = MibTableRow
alaVrrpAssoGroupEntry = _AlaVrrpAssoGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 5, 2, 1)
)
alaVrrpAssoGroupEntry.setIndexNames(
    (0, "ALCATEL-IND1-VRRP-MIB", "alaVrrpGroupId"),
    (0, "IF-MIB", "ifIndex"),
    (0, "VRRP-MIB", "vrrpOperVrId"),
)
if mibBuilder.loadTexts:
    alaVrrpAssoGroupEntry.setStatus("current")
_AlaVrrpAssoGroupRowStatus_Type = RowStatus
_AlaVrrpAssoGroupRowStatus_Object = MibTableColumn
alaVrrpAssoGroupRowStatus = _AlaVrrpAssoGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 1, 5, 2, 1, 1),
    _AlaVrrpAssoGroupRowStatus_Type()
)
alaVrrpAssoGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaVrrpAssoGroupRowStatus.setStatus("current")
_AlcatelIND1VRRPMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1VRRPMIBConformance = _AlcatelIND1VRRPMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 2)
)
_AlcatelIND1VRRPMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1VRRPMIBCompliances = _AlcatelIND1VRRPMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 2, 1)
)
_AlcatelIND1VRRPMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1VRRPMIBGroups = _AlcatelIND1VRRPMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 2, 2)
)
vrrpOperEntry.registerAugmentions(
    ("ALCATEL-IND1-VRRP-MIB",
     "alaVrrpOperEntry")
)
alaVrrpOperEntry.setIndexNames(*vrrpOperEntry.getIndexNames())
alaVrrp3OperEntry.registerAugmentions(
    ("ALCATEL-IND1-VRRP-MIB",
     "alaVrrp3OperExEntry")
)
alaVrrp3OperExEntry.setIndexNames(*alaVrrp3OperEntry.getIndexNames())

# Managed Objects groups

alaVRRPConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 2, 2, 1)
)
alaVRRPConfigGroup.setObjects(
      *(("ALCATEL-IND1-VRRP-MIB", "alaVRRPStartDelay"),
        ("ALCATEL-IND1-VRRP-MIB", "alaVrrpBfdStatus"))
)
if mibBuilder.loadTexts:
    alaVRRPConfigGroup.setStatus("current")

alaVRRPv2ConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 2, 2, 2)
)
alaVRRPv2ConfigGroup.setObjects(
      *(("ALCATEL-IND1-VRRP-MIB", "alaVRRPAdminState"),
        ("ALCATEL-IND1-VRRP-MIB", "alaVRRPDefaultInterval"),
        ("ALCATEL-IND1-VRRP-MIB", "alaVRRPDefaultPreemptMode"),
        ("ALCATEL-IND1-VRRP-MIB", "alaVRRPDefaultPriority"),
        ("ALCATEL-IND1-VRRP-MIB", "alaVRRPOverride"),
        ("ALCATEL-IND1-VRRP-MIB", "alaVRRPSetParam"))
)
if mibBuilder.loadTexts:
    alaVRRPv2ConfigGroup.setStatus("current")

alaVrrp3AssoTrackTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 2, 2, 3)
)
alaVrrp3AssoTrackTableGroup.setObjects(
    ("ALCATEL-IND1-VRRP-MIB", "alaVrrp3AssoTrackRowStatus")
)
if mibBuilder.loadTexts:
    alaVrrp3AssoTrackTableGroup.setStatus("current")

alaVrrp3OperExEntryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 2, 2, 4)
)
alaVrrp3OperExEntryGroup.setObjects(
      *(("ALCATEL-IND1-VRRP-MIB", "alaVrrp3CurrentPriority"),
        ("ALCATEL-IND1-VRRP-MIB", "alaVrrp3GroupIdent"),
        ("ALCATEL-IND1-VRRP-MIB", "alaVrrp3TrackCount"))
)
if mibBuilder.loadTexts:
    alaVrrp3OperExEntryGroup.setStatus("current")

alaVrrpAssoGroupEntryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 2, 2, 5)
)
alaVrrpAssoGroupEntryGroup.setObjects(
    ("ALCATEL-IND1-VRRP-MIB", "alaVrrpAssoGroupRowStatus")
)
if mibBuilder.loadTexts:
    alaVrrpAssoGroupEntryGroup.setStatus("current")

alaVrrpAssoTrackEntryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 2, 2, 6)
)
alaVrrpAssoTrackEntryGroup.setObjects(
    ("ALCATEL-IND1-VRRP-MIB", "alaVrrpAssoTrackRowStatus")
)
if mibBuilder.loadTexts:
    alaVrrpAssoTrackEntryGroup.setStatus("current")

alaVrrpOperEntryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 2, 2, 7)
)
alaVrrpOperEntryGroup.setObjects(
      *(("ALCATEL-IND1-VRRP-MIB", "alaVrrpCurrentPriority"),
        ("ALCATEL-IND1-VRRP-MIB", "alaVrrpTrackCount"),
        ("ALCATEL-IND1-VRRP-MIB", "alaVrrpGroupIdent"))
)
if mibBuilder.loadTexts:
    alaVrrpOperEntryGroup.setStatus("current")

alaVrrpGroupTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 2, 2, 8)
)
alaVrrpGroupTableGroup.setObjects(
      *(("ALCATEL-IND1-VRRP-MIB", "alaVrrpGroupInterval"),
        ("ALCATEL-IND1-VRRP-MIB", "alaVrrpGroupPriority"),
        ("ALCATEL-IND1-VRRP-MIB", "alaVrrpGroupPreemptMode"),
        ("ALCATEL-IND1-VRRP-MIB", "alaVrrpGroupAdminState"),
        ("ALCATEL-IND1-VRRP-MIB", "alaVrrpGroupSetParam"),
        ("ALCATEL-IND1-VRRP-MIB", "alaVrrpGroupOverride"),
        ("ALCATEL-IND1-VRRP-MIB", "alaVrrpGroupRowStatus"))
)
if mibBuilder.loadTexts:
    alaVrrpGroupTableGroup.setStatus("current")

alaVrrpTrackGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 2, 2, 9)
)
alaVrrpTrackGroup.setObjects(
      *(("ALCATEL-IND1-VRRP-MIB", "alaVrrpTrackState"),
        ("ALCATEL-IND1-VRRP-MIB", "alaVrrpTrackAdminState"),
        ("ALCATEL-IND1-VRRP-MIB", "alaVrrpTrackEntityType"),
        ("ALCATEL-IND1-VRRP-MIB", "alaVrrpTrackEntityPort"),
        ("ALCATEL-IND1-VRRP-MIB", "alaVrrpTrackPriority"),
        ("ALCATEL-IND1-VRRP-MIB", "alaVrrpTrackRowStatus"),
        ("ALCATEL-IND1-VRRP-MIB", "alaVrrpTrackEntityInterface"),
        ("ALCATEL-IND1-VRRP-MIB", "alaVrrpTrackEntityIpv6Interface"),
        ("ALCATEL-IND1-VRRP-MIB", "alaVrrpTrackEntityIpAddrType"),
        ("ALCATEL-IND1-VRRP-MIB", "alaVrrpTrackEntityIpAddr"),
        ("ALCATEL-IND1-VRRP-MIB", "alaVrrpTrackBfdStatus"))
)
if mibBuilder.loadTexts:
    alaVrrpTrackGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alaVRRPCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    alaVRRPCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-VRRP-MIB",
    **{"AlaVrTrackId": AlaVrTrackId,
       "AlaVrGroupId": AlaVrGroupId,
       "alcatelIND1VRRPMIB": alcatelIND1VRRPMIB,
       "alcatelIND1VRRPMIBObjects": alcatelIND1VRRPMIBObjects,
       "alaVRRPConfig": alaVRRPConfig,
       "alaVRRPStartDelay": alaVRRPStartDelay,
       "alaVrrpBfdStatus": alaVrrpBfdStatus,
       "alaVrrpTracking": alaVrrpTracking,
       "alaVrrpTrackTable": alaVrrpTrackTable,
       "alaVrrpTrackEntry": alaVrrpTrackEntry,
       "alaVrrpTrackId": alaVrrpTrackId,
       "alaVrrpTrackState": alaVrrpTrackState,
       "alaVrrpTrackAdminState": alaVrrpTrackAdminState,
       "alaVrrpTrackEntityType": alaVrrpTrackEntityType,
       "alaVrrpTrackEntityPort": alaVrrpTrackEntityPort,
       "alaVrrpTrackPriority": alaVrrpTrackPriority,
       "alaVrrpTrackRowStatus": alaVrrpTrackRowStatus,
       "alaVrrpTrackEntityInterface": alaVrrpTrackEntityInterface,
       "alaVrrpTrackEntityIpv6Interface": alaVrrpTrackEntityIpv6Interface,
       "alaVrrpTrackEntityIpAddrType": alaVrrpTrackEntityIpAddrType,
       "alaVrrpTrackEntityIpAddr": alaVrrpTrackEntityIpAddr,
       "alaVrrpTrackBfdStatus": alaVrrpTrackBfdStatus,
       "alaVrrpAssoTrackTable": alaVrrpAssoTrackTable,
       "alaVrrpAssoTrackEntry": alaVrrpAssoTrackEntry,
       "alaVrrpAssoTrackId": alaVrrpAssoTrackId,
       "alaVrrpAssoTrackRowStatus": alaVrrpAssoTrackRowStatus,
       "alaVrrp3AssoTrackTable": alaVrrp3AssoTrackTable,
       "alaVrrp3AssoTrackEntry": alaVrrp3AssoTrackEntry,
       "alaVrrp3AssoTrackId": alaVrrp3AssoTrackId,
       "alaVrrp3AssoTrackRowStatus": alaVrrp3AssoTrackRowStatus,
       "alaVrrpOperations": alaVrrpOperations,
       "alaVrrpOperTable": alaVrrpOperTable,
       "alaVrrpOperEntry": alaVrrpOperEntry,
       "alaVrrpCurrentPriority": alaVrrpCurrentPriority,
       "alaVrrpTrackCount": alaVrrpTrackCount,
       "alaVrrpGroupIdent": alaVrrpGroupIdent,
       "alaVrrp3OperExTable": alaVrrp3OperExTable,
       "alaVrrp3OperExEntry": alaVrrp3OperExEntry,
       "alaVrrp3CurrentPriority": alaVrrp3CurrentPriority,
       "alaVrrp3TrackCount": alaVrrp3TrackCount,
       "alaVrrp3GroupIdent": alaVrrp3GroupIdent,
       "alaVRRPv2Config": alaVRRPv2Config,
       "alaVRRPDefaultInterval": alaVRRPDefaultInterval,
       "alaVRRPDefaultPriority": alaVRRPDefaultPriority,
       "alaVRRPDefaultPreemptMode": alaVRRPDefaultPreemptMode,
       "alaVRRPAdminState": alaVRRPAdminState,
       "alaVRRPSetParam": alaVRRPSetParam,
       "alaVRRPOverride": alaVRRPOverride,
       "alaVrrpGroup": alaVrrpGroup,
       "alaVrrpGroupTable": alaVrrpGroupTable,
       "alaVrrpGroupEntry": alaVrrpGroupEntry,
       "alaVrrpGroupId": alaVrrpGroupId,
       "alaVrrpGroupInterval": alaVrrpGroupInterval,
       "alaVrrpGroupPriority": alaVrrpGroupPriority,
       "alaVrrpGroupPreemptMode": alaVrrpGroupPreemptMode,
       "alaVrrpGroupAdminState": alaVrrpGroupAdminState,
       "alaVrrpGroupSetParam": alaVrrpGroupSetParam,
       "alaVrrpGroupOverride": alaVrrpGroupOverride,
       "alaVrrpGroupRowStatus": alaVrrpGroupRowStatus,
       "alaVrrpAssoGroupTable": alaVrrpAssoGroupTable,
       "alaVrrpAssoGroupEntry": alaVrrpAssoGroupEntry,
       "alaVrrpAssoGroupRowStatus": alaVrrpAssoGroupRowStatus,
       "alcatelIND1VRRPMIBConformance": alcatelIND1VRRPMIBConformance,
       "alcatelIND1VRRPMIBCompliances": alcatelIND1VRRPMIBCompliances,
       "alaVRRPCompliance": alaVRRPCompliance,
       "alcatelIND1VRRPMIBGroups": alcatelIND1VRRPMIBGroups,
       "alaVRRPConfigGroup": alaVRRPConfigGroup,
       "alaVRRPv2ConfigGroup": alaVRRPv2ConfigGroup,
       "alaVrrp3AssoTrackTableGroup": alaVrrp3AssoTrackTableGroup,
       "alaVrrp3OperExEntryGroup": alaVrrp3OperExEntryGroup,
       "alaVrrpAssoGroupEntryGroup": alaVrrpAssoGroupEntryGroup,
       "alaVrrpAssoTrackEntryGroup": alaVrrpAssoTrackEntryGroup,
       "alaVrrpOperEntryGroup": alaVrrpOperEntryGroup,
       "alaVrrpGroupTableGroup": alaVrrpGroupTableGroup,
       "alaVrrpTrackGroup": alaVrrpTrackGroup}
)
