# SNMP MIB module (HM2-L2REDUNDANCY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HM2-L2REDUNDANCY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:56:01 2024
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

(HmEnabledStatus,
 hm2ConfigurationMibs) = mibBuilder.importSymbols(
    "HM2-TC-MIB",
    "HmEnabledStatus",
    "hm2ConfigurationMibs")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hm2L2RedundancyMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 40)
)
hm2L2RedundancyMib.setRevisions(
        ("2011-11-23 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Hm2CplPortOpState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("not-applicable", 4),
          ("not-connected", 1),
          ("standby", 3))
    )



# MIB Managed Objects in the order of their OIDs

_Hm2L2RedundancyMibNotifications_ObjectIdentity = ObjectIdentity
hm2L2RedundancyMibNotifications = _Hm2L2RedundancyMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 0)
)
_Hm2L2RedundancyMibObjects_ObjectIdentity = ObjectIdentity
hm2L2RedundancyMibObjects = _Hm2L2RedundancyMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1)
)
_Hm2MrpMibGroup_ObjectIdentity = ObjectIdentity
hm2MrpMibGroup = _Hm2MrpMibGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 1)
)
_Hm2MrpTable_Object = MibTable
hm2MrpTable = _Hm2MrpTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hm2MrpTable.setStatus("current")
_Hm2MrpEntry_Object = MibTableRow
hm2MrpEntry = _Hm2MrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 1, 1, 1)
)
hm2MrpEntry.setIndexNames(
    (0, "HM2-L2REDUNDANCY-MIB", "hm2MrpDomainID"),
)
if mibBuilder.loadTexts:
    hm2MrpEntry.setStatus("current")


class _Hm2MrpDomainID_Type(OctetString):
    """Custom type hm2MrpDomainID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_Hm2MrpDomainID_Type.__name__ = "OctetString"
_Hm2MrpDomainID_Object = MibTableColumn
hm2MrpDomainID = _Hm2MrpDomainID_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 1, 1, 1, 1),
    _Hm2MrpDomainID_Type()
)
hm2MrpDomainID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hm2MrpDomainID.setStatus("current")
_Hm2MrpDomainName_Type = SnmpAdminString
_Hm2MrpDomainName_Object = MibTableColumn
hm2MrpDomainName = _Hm2MrpDomainName_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 1, 1, 1, 2),
    _Hm2MrpDomainName_Type()
)
hm2MrpDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2MrpDomainName.setStatus("current")
_Hm2MrpRingport1GroupID_Type = Integer32
_Hm2MrpRingport1GroupID_Object = MibTableColumn
hm2MrpRingport1GroupID = _Hm2MrpRingport1GroupID_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 1, 1, 1, 3),
    _Hm2MrpRingport1GroupID_Type()
)
hm2MrpRingport1GroupID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2MrpRingport1GroupID.setStatus("obsolete")
_Hm2MrpRingport1IfIndex_Type = Integer32
_Hm2MrpRingport1IfIndex_Object = MibTableColumn
hm2MrpRingport1IfIndex = _Hm2MrpRingport1IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 1, 1, 1, 4),
    _Hm2MrpRingport1IfIndex_Type()
)
hm2MrpRingport1IfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2MrpRingport1IfIndex.setStatus("current")


class _Hm2MrpRingport1OperState_Type(Integer32):
    """Custom type hm2MrpRingport1OperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 2),
          ("disabled", 1),
          ("forwarding", 3),
          ("notConnected", 4))
    )


_Hm2MrpRingport1OperState_Type.__name__ = "Integer32"
_Hm2MrpRingport1OperState_Object = MibTableColumn
hm2MrpRingport1OperState = _Hm2MrpRingport1OperState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 1, 1, 1, 5),
    _Hm2MrpRingport1OperState_Type()
)
hm2MrpRingport1OperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2MrpRingport1OperState.setStatus("current")
_Hm2MrpRingport2GroupID_Type = Integer32
_Hm2MrpRingport2GroupID_Object = MibTableColumn
hm2MrpRingport2GroupID = _Hm2MrpRingport2GroupID_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 1, 1, 1, 6),
    _Hm2MrpRingport2GroupID_Type()
)
hm2MrpRingport2GroupID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2MrpRingport2GroupID.setStatus("obsolete")
_Hm2MrpRingport2IfIndex_Type = Integer32
_Hm2MrpRingport2IfIndex_Object = MibTableColumn
hm2MrpRingport2IfIndex = _Hm2MrpRingport2IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 1, 1, 1, 7),
    _Hm2MrpRingport2IfIndex_Type()
)
hm2MrpRingport2IfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2MrpRingport2IfIndex.setStatus("current")


class _Hm2MrpRingport2OperState_Type(Integer32):
    """Custom type hm2MrpRingport2OperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 2),
          ("disabled", 1),
          ("forwarding", 3),
          ("notConnected", 4))
    )


_Hm2MrpRingport2OperState_Type.__name__ = "Integer32"
_Hm2MrpRingport2OperState_Object = MibTableColumn
hm2MrpRingport2OperState = _Hm2MrpRingport2OperState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 1, 1, 1, 8),
    _Hm2MrpRingport2OperState_Type()
)
hm2MrpRingport2OperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2MrpRingport2OperState.setStatus("current")


class _Hm2MrpRoleAdminState_Type(Integer32):
    """Custom type hm2MrpRoleAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("client", 1),
          ("manager", 2))
    )


_Hm2MrpRoleAdminState_Type.__name__ = "Integer32"
_Hm2MrpRoleAdminState_Object = MibTableColumn
hm2MrpRoleAdminState = _Hm2MrpRoleAdminState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 1, 1, 1, 9),
    _Hm2MrpRoleAdminState_Type()
)
hm2MrpRoleAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2MrpRoleAdminState.setStatus("current")


class _Hm2MrpRoleOperState_Type(Integer32):
    """Custom type hm2MrpRoleOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("client", 1),
          ("manager", 2),
          ("undefined", 3))
    )


_Hm2MrpRoleOperState_Type.__name__ = "Integer32"
_Hm2MrpRoleOperState_Object = MibTableColumn
hm2MrpRoleOperState = _Hm2MrpRoleOperState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 1, 1, 1, 10),
    _Hm2MrpRoleOperState_Type()
)
hm2MrpRoleOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2MrpRoleOperState.setStatus("current")


class _Hm2MrpRecoveryDelay_Type(Integer32):
    """Custom type hm2MrpRecoveryDelay based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("delay10", 4),
          ("delay200", 2),
          ("delay30", 3),
          ("delay500", 1))
    )


_Hm2MrpRecoveryDelay_Type.__name__ = "Integer32"
_Hm2MrpRecoveryDelay_Object = MibTableColumn
hm2MrpRecoveryDelay = _Hm2MrpRecoveryDelay_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 1, 1, 1, 11),
    _Hm2MrpRecoveryDelay_Type()
)
hm2MrpRecoveryDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2MrpRecoveryDelay.setStatus("current")


class _Hm2MrpRecoveryDelaySupported_Type(Integer32):
    """Custom type hm2MrpRecoveryDelaySupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("supported200500", 2),
          ("supportedAll", 1))
    )


_Hm2MrpRecoveryDelaySupported_Type.__name__ = "Integer32"
_Hm2MrpRecoveryDelaySupported_Object = MibTableColumn
hm2MrpRecoveryDelaySupported = _Hm2MrpRecoveryDelaySupported_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 1, 1, 1, 12),
    _Hm2MrpRecoveryDelaySupported_Type()
)
hm2MrpRecoveryDelaySupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2MrpRecoveryDelaySupported.setStatus("current")


class _Hm2MrpVlanID_Type(Integer32):
    """Custom type hm2MrpVlanID based on Integer32"""
    defaultValue = 0


_Hm2MrpVlanID_Object = MibTableColumn
hm2MrpVlanID = _Hm2MrpVlanID_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 1, 1, 1, 13),
    _Hm2MrpVlanID_Type()
)
hm2MrpVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2MrpVlanID.setStatus("current")


class _Hm2MrpMRMPriority_Type(Integer32):
    """Custom type hm2MrpMRMPriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hm2MrpMRMPriority_Type.__name__ = "Integer32"
_Hm2MrpMRMPriority_Object = MibTableColumn
hm2MrpMRMPriority = _Hm2MrpMRMPriority_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 1, 1, 1, 14),
    _Hm2MrpMRMPriority_Type()
)
hm2MrpMRMPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2MrpMRMPriority.setStatus("current")


class _Hm2MrpMRMReactOnLinkChange_Type(Integer32):
    """Custom type hm2MrpMRMReactOnLinkChange based on Integer32"""
    defaultValue = 1

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


_Hm2MrpMRMReactOnLinkChange_Type.__name__ = "Integer32"
_Hm2MrpMRMReactOnLinkChange_Object = MibTableColumn
hm2MrpMRMReactOnLinkChange = _Hm2MrpMRMReactOnLinkChange_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 1, 1, 1, 15),
    _Hm2MrpMRMReactOnLinkChange_Type()
)
hm2MrpMRMReactOnLinkChange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2MrpMRMReactOnLinkChange.setStatus("current")
_Hm2MrpMRMRingOpenCount_Type = Counter32
_Hm2MrpMRMRingOpenCount_Object = MibTableColumn
hm2MrpMRMRingOpenCount = _Hm2MrpMRMRingOpenCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 1, 1, 1, 16),
    _Hm2MrpMRMRingOpenCount_Type()
)
hm2MrpMRMRingOpenCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2MrpMRMRingOpenCount.setStatus("current")
_Hm2MrpMRMLastRingOpenChange_Type = Unsigned32
_Hm2MrpMRMLastRingOpenChange_Object = MibTableColumn
hm2MrpMRMLastRingOpenChange = _Hm2MrpMRMLastRingOpenChange_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 1, 1, 1, 17),
    _Hm2MrpMRMLastRingOpenChange_Type()
)
hm2MrpMRMLastRingOpenChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2MrpMRMLastRingOpenChange.setStatus("current")
_Hm2MrpMRMRoundTripDelayMax_Type = Unsigned32
_Hm2MrpMRMRoundTripDelayMax_Object = MibTableColumn
hm2MrpMRMRoundTripDelayMax = _Hm2MrpMRMRoundTripDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 1, 1, 1, 18),
    _Hm2MrpMRMRoundTripDelayMax_Type()
)
hm2MrpMRMRoundTripDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2MrpMRMRoundTripDelayMax.setStatus("current")
_Hm2MrpMRMRoundTripDelayMin_Type = Unsigned32
_Hm2MrpMRMRoundTripDelayMin_Object = MibTableColumn
hm2MrpMRMRoundTripDelayMin = _Hm2MrpMRMRoundTripDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 1, 1, 1, 19),
    _Hm2MrpMRMRoundTripDelayMin_Type()
)
hm2MrpMRMRoundTripDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2MrpMRMRoundTripDelayMin.setStatus("current")


class _Hm2MrpMRMRoundTripDelayReset_Type(Integer32):
    """Custom type hm2MrpMRMRoundTripDelayReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_Hm2MrpMRMRoundTripDelayReset_Type.__name__ = "Integer32"
_Hm2MrpMRMRoundTripDelayReset_Object = MibTableColumn
hm2MrpMRMRoundTripDelayReset = _Hm2MrpMRMRoundTripDelayReset_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 1, 1, 1, 20),
    _Hm2MrpMRMRoundTripDelayReset_Type()
)
hm2MrpMRMRoundTripDelayReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2MrpMRMRoundTripDelayReset.setStatus("current")


class _Hm2MrpMRMNonBlockingMRCSupported_Type(Integer32):
    """Custom type hm2MrpMRMNonBlockingMRCSupported based on Integer32"""
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


_Hm2MrpMRMNonBlockingMRCSupported_Type.__name__ = "Integer32"
_Hm2MrpMRMNonBlockingMRCSupported_Object = MibTableColumn
hm2MrpMRMNonBlockingMRCSupported = _Hm2MrpMRMNonBlockingMRCSupported_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 1, 1, 1, 21),
    _Hm2MrpMRMNonBlockingMRCSupported_Type()
)
hm2MrpMRMNonBlockingMRCSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2MrpMRMNonBlockingMRCSupported.setStatus("current")


class _Hm2MrpMRCBlockedSupported_Type(Integer32):
    """Custom type hm2MrpMRCBlockedSupported based on Integer32"""
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


_Hm2MrpMRCBlockedSupported_Type.__name__ = "Integer32"
_Hm2MrpMRCBlockedSupported_Object = MibTableColumn
hm2MrpMRCBlockedSupported = _Hm2MrpMRCBlockedSupported_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 1, 1, 1, 22),
    _Hm2MrpMRCBlockedSupported_Type()
)
hm2MrpMRCBlockedSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2MrpMRCBlockedSupported.setStatus("current")


class _Hm2MrpRingOperState_Type(Integer32):
    """Custom type hm2MrpRingOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("open", 1),
          ("undefined", 3))
    )


_Hm2MrpRingOperState_Type.__name__ = "Integer32"
_Hm2MrpRingOperState_Object = MibTableColumn
hm2MrpRingOperState = _Hm2MrpRingOperState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 1, 1, 1, 23),
    _Hm2MrpRingOperState_Type()
)
hm2MrpRingOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2MrpRingOperState.setStatus("current")


class _Hm2MrpRedundancyOperState_Type(Integer32):
    """Custom type hm2MrpRedundancyOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("notAvailable", 2))
    )


_Hm2MrpRedundancyOperState_Type.__name__ = "Integer32"
_Hm2MrpRedundancyOperState_Object = MibTableColumn
hm2MrpRedundancyOperState = _Hm2MrpRedundancyOperState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 1, 1, 1, 24),
    _Hm2MrpRedundancyOperState_Type()
)
hm2MrpRedundancyOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2MrpRedundancyOperState.setStatus("current")


class _Hm2MrpConfigOperState_Type(Integer32):
    """Custom type hm2MrpConfigOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("multipleMRM", 3),
          ("noError", 1),
          ("ringportLinkError", 2),
          ("singleSideReceive", 4))
    )


_Hm2MrpConfigOperState_Type.__name__ = "Integer32"
_Hm2MrpConfigOperState_Object = MibTableColumn
hm2MrpConfigOperState = _Hm2MrpConfigOperState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 1, 1, 1, 25),
    _Hm2MrpConfigOperState_Type()
)
hm2MrpConfigOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2MrpConfigOperState.setStatus("current")
_Hm2MrpRowStatus_Type = RowStatus
_Hm2MrpRowStatus_Object = MibTableColumn
hm2MrpRowStatus = _Hm2MrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 1, 1, 1, 26),
    _Hm2MrpRowStatus_Type()
)
hm2MrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2MrpRowStatus.setStatus("current")


class _Hm2MrpRingport2FixedBackup_Type(HmEnabledStatus):
    """Custom type hm2MrpRingport2FixedBackup based on HmEnabledStatus"""


_Hm2MrpRingport2FixedBackup_Object = MibTableColumn
hm2MrpRingport2FixedBackup = _Hm2MrpRingport2FixedBackup_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 1, 1, 1, 27),
    _Hm2MrpRingport2FixedBackup_Type()
)
hm2MrpRingport2FixedBackup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2MrpRingport2FixedBackup.setStatus("current")
_Hm2MrpConformance_ObjectIdentity = ObjectIdentity
hm2MrpConformance = _Hm2MrpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 1, 2)
)
_Hm2MrpCompliances_ObjectIdentity = ObjectIdentity
hm2MrpCompliances = _Hm2MrpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 1, 2, 1)
)
_Hm2MrpGroups_ObjectIdentity = ObjectIdentity
hm2MrpGroups = _Hm2MrpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 1, 2, 2)
)


class _Hm2MrpFastMrp_Type(Integer32):
    """Custom type hm2MrpFastMrp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 2),
          ("supported", 1))
    )


_Hm2MrpFastMrp_Type.__name__ = "Integer32"
_Hm2MrpFastMrp_Object = MibScalar
hm2MrpFastMrp = _Hm2MrpFastMrp_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 1, 3),
    _Hm2MrpFastMrp_Type()
)
hm2MrpFastMrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2MrpFastMrp.setStatus("current")
_Hm2SrmMibGroup_ObjectIdentity = ObjectIdentity
hm2SrmMibGroup = _Hm2SrmMibGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 4)
)


class _Hm2SrmGlobalAdminState_Type(HmEnabledStatus):
    """Custom type hm2SrmGlobalAdminState based on HmEnabledStatus"""


_Hm2SrmGlobalAdminState_Object = MibScalar
hm2SrmGlobalAdminState = _Hm2SrmGlobalAdminState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 4, 1),
    _Hm2SrmGlobalAdminState_Type()
)
hm2SrmGlobalAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2SrmGlobalAdminState.setStatus("current")
_Hm2SrmMaxInstances_Type = Integer32
_Hm2SrmMaxInstances_Object = MibScalar
hm2SrmMaxInstances = _Hm2SrmMaxInstances_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 4, 2),
    _Hm2SrmMaxInstances_Type()
)
hm2SrmMaxInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SrmMaxInstances.setStatus("current")
_Hm2SrmTable_Object = MibTable
hm2SrmTable = _Hm2SrmTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 4, 3)
)
if mibBuilder.loadTexts:
    hm2SrmTable.setStatus("current")
_Hm2SrmEntry_Object = MibTableRow
hm2SrmEntry = _Hm2SrmEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 4, 3, 1)
)
hm2SrmEntry.setIndexNames(
    (0, "HM2-L2REDUNDANCY-MIB", "hm2SrmRingID"),
)
if mibBuilder.loadTexts:
    hm2SrmEntry.setStatus("current")
_Hm2SrmRingID_Type = Integer32
_Hm2SrmRingID_Object = MibTableColumn
hm2SrmRingID = _Hm2SrmRingID_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 4, 3, 1, 1),
    _Hm2SrmRingID_Type()
)
hm2SrmRingID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hm2SrmRingID.setStatus("current")


class _Hm2SrmAdminState_Type(Integer32):
    """Custom type hm2SrmAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("manager", 1),
          ("redundantManager", 2),
          ("singleManager", 3))
    )


_Hm2SrmAdminState_Type.__name__ = "Integer32"
_Hm2SrmAdminState_Object = MibTableColumn
hm2SrmAdminState = _Hm2SrmAdminState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 4, 3, 1, 2),
    _Hm2SrmAdminState_Type()
)
hm2SrmAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2SrmAdminState.setStatus("current")


class _Hm2SrmOperState_Type(Integer32):
    """Custom type hm2SrmOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 4),
          ("manager", 1),
          ("redundantManager", 2),
          ("singleManager", 3))
    )


_Hm2SrmOperState_Type.__name__ = "Integer32"
_Hm2SrmOperState_Object = MibTableColumn
hm2SrmOperState = _Hm2SrmOperState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 4, 3, 1, 3),
    _Hm2SrmOperState_Type()
)
hm2SrmOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SrmOperState.setStatus("current")


class _Hm2SrmVlanID_Type(Integer32):
    """Custom type hm2SrmVlanID based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4042),
    )


_Hm2SrmVlanID_Type.__name__ = "Integer32"
_Hm2SrmVlanID_Object = MibTableColumn
hm2SrmVlanID = _Hm2SrmVlanID_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 4, 3, 1, 4),
    _Hm2SrmVlanID_Type()
)
hm2SrmVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2SrmVlanID.setStatus("current")


class _Hm2SrmMRPDomainID_Type(OctetString):
    """Custom type hm2SrmMRPDomainID based on OctetString"""
    defaultHexValue = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_Hm2SrmMRPDomainID_Type.__name__ = "OctetString"
_Hm2SrmMRPDomainID_Object = MibTableColumn
hm2SrmMRPDomainID = _Hm2SrmMRPDomainID_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 4, 3, 1, 5),
    _Hm2SrmMRPDomainID_Type()
)
hm2SrmMRPDomainID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2SrmMRPDomainID.setStatus("current")
_Hm2SrmPartnerMAC_Type = MacAddress
_Hm2SrmPartnerMAC_Object = MibTableColumn
hm2SrmPartnerMAC = _Hm2SrmPartnerMAC_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 4, 3, 1, 6),
    _Hm2SrmPartnerMAC_Type()
)
hm2SrmPartnerMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SrmPartnerMAC.setStatus("current")


class _Hm2SrmSubRingProtocol_Type(Integer32):
    """Custom type hm2SrmSubRingProtocol based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            4
        )
    )
    namedValues = NamedValues(
        ("iec-62439-mrp", 4)
    )


_Hm2SrmSubRingProtocol_Type.__name__ = "Integer32"
_Hm2SrmSubRingProtocol_Object = MibTableColumn
hm2SrmSubRingProtocol = _Hm2SrmSubRingProtocol_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 4, 3, 1, 7),
    _Hm2SrmSubRingProtocol_Type()
)
hm2SrmSubRingProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2SrmSubRingProtocol.setStatus("current")
_Hm2SrmSubRingName_Type = SnmpAdminString
_Hm2SrmSubRingName_Object = MibTableColumn
hm2SrmSubRingName = _Hm2SrmSubRingName_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 4, 3, 1, 8),
    _Hm2SrmSubRingName_Type()
)
hm2SrmSubRingName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2SrmSubRingName.setStatus("current")
_Hm2SrmSubRingPortIfIndex_Type = Integer32
_Hm2SrmSubRingPortIfIndex_Object = MibTableColumn
hm2SrmSubRingPortIfIndex = _Hm2SrmSubRingPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 4, 3, 1, 9),
    _Hm2SrmSubRingPortIfIndex_Type()
)
hm2SrmSubRingPortIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2SrmSubRingPortIfIndex.setStatus("current")


class _Hm2SrmSubRingPortOperState_Type(Integer32):
    """Custom type hm2SrmSubRingPortOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 2),
          ("disabled", 1),
          ("forwarding", 3),
          ("not-connected", 4))
    )


_Hm2SrmSubRingPortOperState_Type.__name__ = "Integer32"
_Hm2SrmSubRingPortOperState_Object = MibTableColumn
hm2SrmSubRingPortOperState = _Hm2SrmSubRingPortOperState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 4, 3, 1, 10),
    _Hm2SrmSubRingPortOperState_Type()
)
hm2SrmSubRingPortOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SrmSubRingPortOperState.setStatus("current")


class _Hm2SrmSubRingOperState_Type(Integer32):
    """Custom type hm2SrmSubRingOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("closed", 3),
          ("open", 2),
          ("undefined", 1))
    )


_Hm2SrmSubRingOperState_Type.__name__ = "Integer32"
_Hm2SrmSubRingOperState_Object = MibTableColumn
hm2SrmSubRingOperState = _Hm2SrmSubRingOperState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 4, 3, 1, 11),
    _Hm2SrmSubRingOperState_Type()
)
hm2SrmSubRingOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SrmSubRingOperState.setStatus("current")


class _Hm2SrmRedundancyOperState_Type(Integer32):
    """Custom type hm2SrmRedundancyOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("redGuaranteed", 1),
          ("redNotGuaranteed", 2))
    )


_Hm2SrmRedundancyOperState_Type.__name__ = "Integer32"
_Hm2SrmRedundancyOperState_Object = MibTableColumn
hm2SrmRedundancyOperState = _Hm2SrmRedundancyOperState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 4, 3, 1, 12),
    _Hm2SrmRedundancyOperState_Type()
)
hm2SrmRedundancyOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SrmRedundancyOperState.setStatus("current")


class _Hm2SrmConfigOperState_Type(Integer32):
    """Custom type hm2SrmConfigOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("concurrentPort", 6),
          ("concurrentRedundancy", 7),
          ("concurrentVLAN", 5),
          ("multipleSRM", 3),
          ("noError", 1),
          ("noPartnerManager", 4),
          ("ringPortLinkError", 2),
          ("sharedVLAN", 9),
          ("trunkMember", 8))
    )


_Hm2SrmConfigOperState_Type.__name__ = "Integer32"
_Hm2SrmConfigOperState_Object = MibTableColumn
hm2SrmConfigOperState = _Hm2SrmConfigOperState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 4, 3, 1, 13),
    _Hm2SrmConfigOperState_Type()
)
hm2SrmConfigOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SrmConfigOperState.setStatus("current")
_Hm2SrmRowStatus_Type = RowStatus
_Hm2SrmRowStatus_Object = MibTableColumn
hm2SrmRowStatus = _Hm2SrmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 4, 3, 1, 20),
    _Hm2SrmRowStatus_Type()
)
hm2SrmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2SrmRowStatus.setStatus("current")
_Hm2RingRedMibGroup_ObjectIdentity = ObjectIdentity
hm2RingRedMibGroup = _Hm2RingRedMibGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 7)
)


class _Hm2RingRedAdminState_Type(HmEnabledStatus):
    """Custom type hm2RingRedAdminState based on HmEnabledStatus"""


_Hm2RingRedAdminState_Object = MibScalar
hm2RingRedAdminState = _Hm2RingRedAdminState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 7, 1),
    _Hm2RingRedAdminState_Type()
)
hm2RingRedAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2RingRedAdminState.setStatus("current")


class _Hm2RingRedMode_Type(Integer32):
    """Custom type hm2RingRedMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ring-switch", 1)
    )


_Hm2RingRedMode_Type.__name__ = "Integer32"
_Hm2RingRedMode_Object = MibScalar
hm2RingRedMode = _Hm2RingRedMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 7, 2),
    _Hm2RingRedMode_Type()
)
hm2RingRedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2RingRedMode.setStatus("current")


class _Hm2RingRedPrimaryIntf_Type(InterfaceIndexOrZero):
    """Custom type hm2RingRedPrimaryIntf based on InterfaceIndexOrZero"""
    defaultValue = 0


_Hm2RingRedPrimaryIntf_Object = MibScalar
hm2RingRedPrimaryIntf = _Hm2RingRedPrimaryIntf_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 7, 3),
    _Hm2RingRedPrimaryIntf_Type()
)
hm2RingRedPrimaryIntf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2RingRedPrimaryIntf.setStatus("current")


class _Hm2RingRedPrimaryIntfState_Type(Integer32):
    """Custom type hm2RingRedPrimaryIntfState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 3),
          ("not-available", 1))
    )


_Hm2RingRedPrimaryIntfState_Type.__name__ = "Integer32"
_Hm2RingRedPrimaryIntfState_Object = MibScalar
hm2RingRedPrimaryIntfState = _Hm2RingRedPrimaryIntfState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 7, 4),
    _Hm2RingRedPrimaryIntfState_Type()
)
hm2RingRedPrimaryIntfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2RingRedPrimaryIntfState.setStatus("current")


class _Hm2RingRedSecondaryIntf_Type(InterfaceIndexOrZero):
    """Custom type hm2RingRedSecondaryIntf based on InterfaceIndexOrZero"""
    defaultValue = 0


_Hm2RingRedSecondaryIntf_Object = MibScalar
hm2RingRedSecondaryIntf = _Hm2RingRedSecondaryIntf_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 7, 5),
    _Hm2RingRedSecondaryIntf_Type()
)
hm2RingRedSecondaryIntf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2RingRedSecondaryIntf.setStatus("current")


class _Hm2RingRedSecondaryIntfState_Type(Integer32):
    """Custom type hm2RingRedSecondaryIntfState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 3),
          ("not-available", 1))
    )


_Hm2RingRedSecondaryIntfState_Type.__name__ = "Integer32"
_Hm2RingRedSecondaryIntfState_Object = MibScalar
hm2RingRedSecondaryIntfState = _Hm2RingRedSecondaryIntfState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 7, 6),
    _Hm2RingRedSecondaryIntfState_Type()
)
hm2RingRedSecondaryIntfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2RingRedSecondaryIntfState.setStatus("current")
_Hm2RingCouplingMibGroup_ObjectIdentity = ObjectIdentity
hm2RingCouplingMibGroup = _Hm2RingCouplingMibGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 8)
)
_Hm2RingCouplingTable_Object = MibTable
hm2RingCouplingTable = _Hm2RingCouplingTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 8, 1)
)
if mibBuilder.loadTexts:
    hm2RingCouplingTable.setStatus("current")
_Hm2RingCouplingEntry_Object = MibTableRow
hm2RingCouplingEntry = _Hm2RingCouplingEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 8, 1, 1)
)
hm2RingCouplingEntry.setIndexNames(
    (0, "HM2-L2REDUNDANCY-MIB", "hm2RingCplInterconnIfIndex"),
)
if mibBuilder.loadTexts:
    hm2RingCouplingEntry.setStatus("current")
_Hm2RingCplInterconnIfIndex_Type = InterfaceIndexOrZero
_Hm2RingCplInterconnIfIndex_Object = MibTableColumn
hm2RingCplInterconnIfIndex = _Hm2RingCplInterconnIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 8, 1, 1, 1),
    _Hm2RingCplInterconnIfIndex_Type()
)
hm2RingCplInterconnIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2RingCplInterconnIfIndex.setStatus("current")
_Hm2RingCplInterconnIfOpState_Type = Hm2CplPortOpState
_Hm2RingCplInterconnIfOpState_Object = MibTableColumn
hm2RingCplInterconnIfOpState = _Hm2RingCplInterconnIfOpState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 8, 1, 1, 2),
    _Hm2RingCplInterconnIfOpState_Type()
)
hm2RingCplInterconnIfOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2RingCplInterconnIfOpState.setStatus("current")
_Hm2RingCplControlIfIndex_Type = InterfaceIndexOrZero
_Hm2RingCplControlIfIndex_Object = MibTableColumn
hm2RingCplControlIfIndex = _Hm2RingCplControlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 8, 1, 1, 3),
    _Hm2RingCplControlIfIndex_Type()
)
hm2RingCplControlIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2RingCplControlIfIndex.setStatus("current")
_Hm2RingCplControlIfOpState_Type = Hm2CplPortOpState
_Hm2RingCplControlIfOpState_Object = MibTableColumn
hm2RingCplControlIfOpState = _Hm2RingCplControlIfOpState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 8, 1, 1, 4),
    _Hm2RingCplControlIfOpState_Type()
)
hm2RingCplControlIfOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2RingCplControlIfOpState.setStatus("current")
_Hm2RingCplPartnerInterconnIfIndex_Type = InterfaceIndexOrZero
_Hm2RingCplPartnerInterconnIfIndex_Object = MibTableColumn
hm2RingCplPartnerInterconnIfIndex = _Hm2RingCplPartnerInterconnIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 8, 1, 1, 5),
    _Hm2RingCplPartnerInterconnIfIndex_Type()
)
hm2RingCplPartnerInterconnIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2RingCplPartnerInterconnIfIndex.setStatus("current")
_Hm2RingCplPartnerInterconnIfOpState_Type = Hm2CplPortOpState
_Hm2RingCplPartnerInterconnIfOpState_Object = MibTableColumn
hm2RingCplPartnerInterconnIfOpState = _Hm2RingCplPartnerInterconnIfOpState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 8, 1, 1, 6),
    _Hm2RingCplPartnerInterconnIfOpState_Type()
)
hm2RingCplPartnerInterconnIfOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2RingCplPartnerInterconnIfOpState.setStatus("current")


class _Hm2RingCplPartnerIpAddrType_Type(InetAddressType):
    """Custom type hm2RingCplPartnerIpAddrType based on InetAddressType"""


_Hm2RingCplPartnerIpAddrType_Object = MibTableColumn
hm2RingCplPartnerIpAddrType = _Hm2RingCplPartnerIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 8, 1, 1, 7),
    _Hm2RingCplPartnerIpAddrType_Type()
)
hm2RingCplPartnerIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2RingCplPartnerIpAddrType.setStatus("current")


class _Hm2RingCplPartnerIpAddr_Type(InetAddress):
    """Custom type hm2RingCplPartnerIpAddr based on InetAddress"""
    defaultHexValue = "00000000"


_Hm2RingCplPartnerIpAddr_Object = MibTableColumn
hm2RingCplPartnerIpAddr = _Hm2RingCplPartnerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 8, 1, 1, 8),
    _Hm2RingCplPartnerIpAddr_Type()
)
hm2RingCplPartnerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2RingCplPartnerIpAddr.setStatus("current")


class _Hm2RingCplCouplingMode_Type(Integer32):
    """Custom type hm2RingCplCouplingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("dual-master-inband", 2),
          ("dual-master-outband", 3),
          ("dual-slave-inband", 4),
          ("dual-slave-outband", 5),
          ("single", 1),
          ("unknown", 6))
    )


_Hm2RingCplCouplingMode_Type.__name__ = "Integer32"
_Hm2RingCplCouplingMode_Object = MibTableColumn
hm2RingCplCouplingMode = _Hm2RingCplCouplingMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 8, 1, 1, 9),
    _Hm2RingCplCouplingMode_Type()
)
hm2RingCplCouplingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2RingCplCouplingMode.setStatus("current")


class _Hm2RingCplControlModeOperState_Type(Integer32):
    """Custom type hm2RingCplControlModeOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("inband", 2),
          ("local", 4),
          ("outband", 1),
          ("unknown", 3))
    )


_Hm2RingCplControlModeOperState_Type.__name__ = "Integer32"
_Hm2RingCplControlModeOperState_Object = MibTableColumn
hm2RingCplControlModeOperState = _Hm2RingCplControlModeOperState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 8, 1, 1, 10),
    _Hm2RingCplControlModeOperState_Type()
)
hm2RingCplControlModeOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2RingCplControlModeOperState.setStatus("current")


class _Hm2RingCplModeOperState_Type(Integer32):
    """Custom type hm2RingCplModeOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("slaveOff", 1),
          ("slaveOn", 2))
    )


_Hm2RingCplModeOperState_Type.__name__ = "Integer32"
_Hm2RingCplModeOperState_Object = MibTableColumn
hm2RingCplModeOperState = _Hm2RingCplModeOperState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 8, 1, 1, 11),
    _Hm2RingCplModeOperState_Type()
)
hm2RingCplModeOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2RingCplModeOperState.setStatus("current")


class _Hm2RingCplOperState_Type(Integer32):
    """Custom type hm2RingCplOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("local", 4),
          ("master", 3),
          ("slave", 2),
          ("underCreation", 1))
    )


_Hm2RingCplOperState_Type.__name__ = "Integer32"
_Hm2RingCplOperState_Object = MibTableColumn
hm2RingCplOperState = _Hm2RingCplOperState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 8, 1, 1, 12),
    _Hm2RingCplOperState_Type()
)
hm2RingCplOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2RingCplOperState.setStatus("current")


class _Hm2RingCplConfigOperState_Type(Integer32):
    """Custom type hm2RingCplConfigOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("controlPortNotAvailable", 9),
          ("couplingPortNotAvailable", 8),
          ("localInvalidCouplingPort", 7),
          ("localPartnerLinkError", 6),
          ("masterControlLinkError", 4),
          ("noError", 1),
          ("partnerPortNotAvailable", 10),
          ("slaveControlLinkError", 3),
          ("slaveCouplingLinkError", 2),
          ("twoSlaves", 5))
    )


_Hm2RingCplConfigOperState_Type.__name__ = "Integer32"
_Hm2RingCplConfigOperState_Object = MibTableColumn
hm2RingCplConfigOperState = _Hm2RingCplConfigOperState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 8, 1, 1, 13),
    _Hm2RingCplConfigOperState_Type()
)
hm2RingCplConfigOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2RingCplConfigOperState.setStatus("current")


class _Hm2RingCplCouplingLinks_Type(Integer32):
    """Custom type hm2RingCplCouplingLinks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("basicRedundancy", 1),
          ("extendedRedundancy", 2))
    )


_Hm2RingCplCouplingLinks_Type.__name__ = "Integer32"
_Hm2RingCplCouplingLinks_Object = MibTableColumn
hm2RingCplCouplingLinks = _Hm2RingCplCouplingLinks_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 8, 1, 1, 14),
    _Hm2RingCplCouplingLinks_Type()
)
hm2RingCplCouplingLinks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2RingCplCouplingLinks.setStatus("current")


class _Hm2RingCplExtendedDiag_Type(Integer32):
    """Custom type hm2RingCplExtendedDiag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("basicRedundancyInactive", 2),
          ("noError", 1))
    )


_Hm2RingCplExtendedDiag_Type.__name__ = "Integer32"
_Hm2RingCplExtendedDiag_Object = MibTableColumn
hm2RingCplExtendedDiag = _Hm2RingCplExtendedDiag_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 8, 1, 1, 15),
    _Hm2RingCplExtendedDiag_Type()
)
hm2RingCplExtendedDiag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2RingCplExtendedDiag.setStatus("current")


class _Hm2RingCplNetCoupling_Type(Integer32):
    """Custom type hm2RingCplNetCoupling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("netCoupling", 2),
          ("ringCoupling", 1))
    )


_Hm2RingCplNetCoupling_Type.__name__ = "Integer32"
_Hm2RingCplNetCoupling_Object = MibTableColumn
hm2RingCplNetCoupling = _Hm2RingCplNetCoupling_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 8, 1, 1, 16),
    _Hm2RingCplNetCoupling_Type()
)
hm2RingCplNetCoupling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2RingCplNetCoupling.setStatus("current")


class _Hm2RingCplRedOperState_Type(Integer32):
    """Custom type hm2RingCplRedOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("redGuaranteed", 1),
          ("redNotGuaranteed", 2))
    )


_Hm2RingCplRedOperState_Type.__name__ = "Integer32"
_Hm2RingCplRedOperState_Object = MibTableColumn
hm2RingCplRedOperState = _Hm2RingCplRedOperState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 8, 1, 1, 17),
    _Hm2RingCplRedOperState_Type()
)
hm2RingCplRedOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2RingCplRedOperState.setStatus("current")
_Hm2RingCplRowStatus_Type = RowStatus
_Hm2RingCplRowStatus_Object = MibTableColumn
hm2RingCplRowStatus = _Hm2RingCplRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 8, 1, 1, 22),
    _Hm2RingCplRowStatus_Type()
)
hm2RingCplRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2RingCplRowStatus.setStatus("current")
_Hm2RedundantCplConfigMibGroup_ObjectIdentity = ObjectIdentity
hm2RedundantCplConfigMibGroup = _Hm2RedundantCplConfigMibGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 9)
)


class _Hm2RedundantCplAdminState_Type(HmEnabledStatus):
    """Custom type hm2RedundantCplAdminState based on HmEnabledStatus"""


_Hm2RedundantCplAdminState_Object = MibScalar
hm2RedundantCplAdminState = _Hm2RedundantCplAdminState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 9, 1),
    _Hm2RedundantCplAdminState_Type()
)
hm2RedundantCplAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2RedundantCplAdminState.setStatus("current")


class _Hm2RedundantCplInPrimaryPort_Type(InterfaceIndexOrZero):
    """Custom type hm2RedundantCplInPrimaryPort based on InterfaceIndexOrZero"""
    defaultValue = 0


_Hm2RedundantCplInPrimaryPort_Object = MibScalar
hm2RedundantCplInPrimaryPort = _Hm2RedundantCplInPrimaryPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 9, 2),
    _Hm2RedundantCplInPrimaryPort_Type()
)
hm2RedundantCplInPrimaryPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2RedundantCplInPrimaryPort.setStatus("current")


class _Hm2RedundantCplOutPrimaryPort_Type(InterfaceIndexOrZero):
    """Custom type hm2RedundantCplOutPrimaryPort based on InterfaceIndexOrZero"""
    defaultValue = 0


_Hm2RedundantCplOutPrimaryPort_Object = MibScalar
hm2RedundantCplOutPrimaryPort = _Hm2RedundantCplOutPrimaryPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 9, 3),
    _Hm2RedundantCplOutPrimaryPort_Type()
)
hm2RedundantCplOutPrimaryPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2RedundantCplOutPrimaryPort.setStatus("current")


class _Hm2RedundantCplInSecondaryPort_Type(InterfaceIndexOrZero):
    """Custom type hm2RedundantCplInSecondaryPort based on InterfaceIndexOrZero"""
    defaultValue = 0


_Hm2RedundantCplInSecondaryPort_Object = MibScalar
hm2RedundantCplInSecondaryPort = _Hm2RedundantCplInSecondaryPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 9, 4),
    _Hm2RedundantCplInSecondaryPort_Type()
)
hm2RedundantCplInSecondaryPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2RedundantCplInSecondaryPort.setStatus("current")


class _Hm2RedundantCplOutSecondaryPort_Type(InterfaceIndexOrZero):
    """Custom type hm2RedundantCplOutSecondaryPort based on InterfaceIndexOrZero"""
    defaultValue = 0


_Hm2RedundantCplOutSecondaryPort_Object = MibScalar
hm2RedundantCplOutSecondaryPort = _Hm2RedundantCplOutSecondaryPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 9, 5),
    _Hm2RedundantCplOutSecondaryPort_Type()
)
hm2RedundantCplOutSecondaryPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2RedundantCplOutSecondaryPort.setStatus("current")


class _Hm2RedundantCplRole_Type(Integer32):
    """Custom type hm2RedundantCplRole based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("auto", 4),
          ("master", 1),
          ("slave", 2))
    )


_Hm2RedundantCplRole_Type.__name__ = "Integer32"
_Hm2RedundantCplRole_Object = MibScalar
hm2RedundantCplRole = _Hm2RedundantCplRole_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 9, 6),
    _Hm2RedundantCplRole_Type()
)
hm2RedundantCplRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2RedundantCplRole.setStatus("current")


class _Hm2RedundantCplCurrentRole_Type(Integer32):
    """Custom type hm2RedundantCplCurrentRole based on Integer32"""
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
        *(("disabled", 5),
          ("error", 4),
          ("listening", 3),
          ("master", 1),
          ("slave", 2))
    )


_Hm2RedundantCplCurrentRole_Type.__name__ = "Integer32"
_Hm2RedundantCplCurrentRole_Object = MibScalar
hm2RedundantCplCurrentRole = _Hm2RedundantCplCurrentRole_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 9, 7),
    _Hm2RedundantCplCurrentRole_Type()
)
hm2RedundantCplCurrentRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2RedundantCplCurrentRole.setStatus("current")


class _Hm2RedundantCplTimeout_Type(Unsigned32):
    """Custom type hm2RedundantCplTimeout based on Unsigned32"""
    defaultValue = 250

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60000),
    )


_Hm2RedundantCplTimeout_Type.__name__ = "Unsigned32"
_Hm2RedundantCplTimeout_Object = MibScalar
hm2RedundantCplTimeout = _Hm2RedundantCplTimeout_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 9, 8),
    _Hm2RedundantCplTimeout_Type()
)
hm2RedundantCplTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2RedundantCplTimeout.setStatus("current")
_Hm2RedundantCplPartner_Type = MacAddress
_Hm2RedundantCplPartner_Object = MibScalar
hm2RedundantCplPartner = _Hm2RedundantCplPartner_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 9, 9),
    _Hm2RedundantCplPartner_Type()
)
hm2RedundantCplPartner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2RedundantCplPartner.setStatus("current")
_Hm2RedundantCplPartnerPrimaryPort_Type = InterfaceIndexOrZero
_Hm2RedundantCplPartnerPrimaryPort_Object = MibScalar
hm2RedundantCplPartnerPrimaryPort = _Hm2RedundantCplPartnerPrimaryPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 9, 10),
    _Hm2RedundantCplPartnerPrimaryPort_Type()
)
hm2RedundantCplPartnerPrimaryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2RedundantCplPartnerPrimaryPort.setStatus("current")
_Hm2RedundantCplPartnerSecodaryPort_Type = InterfaceIndexOrZero
_Hm2RedundantCplPartnerSecodaryPort_Object = MibScalar
hm2RedundantCplPartnerSecodaryPort = _Hm2RedundantCplPartnerSecodaryPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 9, 11),
    _Hm2RedundantCplPartnerSecodaryPort_Type()
)
hm2RedundantCplPartnerSecodaryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2RedundantCplPartnerSecodaryPort.setStatus("current")


class _Hm2RedundantCplState_Type(Integer32):
    """Custom type hm2RedundantCplState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 2),
          ("forwarding", 1))
    )


_Hm2RedundantCplState_Type.__name__ = "Integer32"
_Hm2RedundantCplState_Object = MibScalar
hm2RedundantCplState = _Hm2RedundantCplState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 9, 12),
    _Hm2RedundantCplState_Type()
)
hm2RedundantCplState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2RedundantCplState.setStatus("current")


class _Hm2RedundantCplRedundancyState_Type(Integer32):
    """Custom type hm2RedundantCplRedundancyState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("redAvailable", 1),
          ("redNotAvailable", 2))
    )


_Hm2RedundantCplRedundancyState_Type.__name__ = "Integer32"
_Hm2RedundantCplRedundancyState_Object = MibScalar
hm2RedundantCplRedundancyState = _Hm2RedundantCplRedundancyState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 9, 13),
    _Hm2RedundantCplRedundancyState_Type()
)
hm2RedundantCplRedundancyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2RedundantCplRedundancyState.setStatus("current")
_Hm2RedundantCplPartnerIPAddrType_Type = InetAddressType
_Hm2RedundantCplPartnerIPAddrType_Object = MibScalar
hm2RedundantCplPartnerIPAddrType = _Hm2RedundantCplPartnerIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 9, 14),
    _Hm2RedundantCplPartnerIPAddrType_Type()
)
hm2RedundantCplPartnerIPAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2RedundantCplPartnerIPAddrType.setStatus("current")
_Hm2RedundantCplPartnerIPAddr_Type = InetAddress
_Hm2RedundantCplPartnerIPAddr_Object = MibScalar
hm2RedundantCplPartnerIPAddr = _Hm2RedundantCplPartnerIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 9, 15),
    _Hm2RedundantCplPartnerIPAddr_Type()
)
hm2RedundantCplPartnerIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2RedundantCplPartnerIPAddr.setStatus("current")
_Hm2L2RedundancyMibSNMPExtensionGroup_ObjectIdentity = ObjectIdentity
hm2L2RedundancyMibSNMPExtensionGroup = _Hm2L2RedundancyMibSNMPExtensionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 3)
)
_Hm2RingCouplingMibSESGroup_ObjectIdentity = ObjectIdentity
hm2RingCouplingMibSESGroup = _Hm2RingCouplingMibSESGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 3, 8)
)
_Hm2RingCouplingInvalidPortConfiguration_ObjectIdentity = ObjectIdentity
hm2RingCouplingInvalidPortConfiguration = _Hm2RingCouplingInvalidPortConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 3, 8, 1)
)
if mibBuilder.loadTexts:
    hm2RingCouplingInvalidPortConfiguration.setStatus("current")
_Hm2RedundantCplSESGroup_ObjectIdentity = ObjectIdentity
hm2RedundantCplSESGroup = _Hm2RedundantCplSESGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 3, 9)
)
_Hm2RedundantCplPortsMissing_ObjectIdentity = ObjectIdentity
hm2RedundantCplPortsMissing = _Hm2RedundantCplPortsMissing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 3, 9, 1)
)
if mibBuilder.loadTexts:
    hm2RedundantCplPortsMissing.setStatus("current")

# Managed Objects groups

hm2MrpDomainBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 1, 2, 2, 1)
)
hm2MrpDomainBasicGroup.setObjects(
      *(("HM2-L2REDUNDANCY-MIB", "hm2MrpDomainID"),
        ("HM2-L2REDUNDANCY-MIB", "hm2MrpDomainName"),
        ("HM2-L2REDUNDANCY-MIB", "hm2MrpRingport1IfIndex"),
        ("HM2-L2REDUNDANCY-MIB", "hm2MrpRingport1OperState"),
        ("HM2-L2REDUNDANCY-MIB", "hm2MrpRingport2IfIndex"),
        ("HM2-L2REDUNDANCY-MIB", "hm2MrpRingport2OperState"),
        ("HM2-L2REDUNDANCY-MIB", "hm2MrpRoleAdminState"),
        ("HM2-L2REDUNDANCY-MIB", "hm2MrpRoleOperState"),
        ("HM2-L2REDUNDANCY-MIB", "hm2MrpRecoveryDelay"),
        ("HM2-L2REDUNDANCY-MIB", "hm2MrpRecoveryDelaySupported"),
        ("HM2-L2REDUNDANCY-MIB", "hm2MrpVlanID"),
        ("HM2-L2REDUNDANCY-MIB", "hm2MrpMRCBlockedSupported"),
        ("HM2-L2REDUNDANCY-MIB", "hm2MrpRedundancyOperState"),
        ("HM2-L2REDUNDANCY-MIB", "hm2MrpConfigOperState"),
        ("HM2-L2REDUNDANCY-MIB", "hm2MrpRowStatus"))
)
if mibBuilder.loadTexts:
    hm2MrpDomainBasicGroup.setStatus("current")

hm2MrpDomainManagerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 1, 2, 2, 2)
)
hm2MrpDomainManagerGroup.setObjects(
      *(("HM2-L2REDUNDANCY-MIB", "hm2MrpMRMPriority"),
        ("HM2-L2REDUNDANCY-MIB", "hm2MrpMRMReactOnLinkChange"),
        ("HM2-L2REDUNDANCY-MIB", "hm2MrpMRMNonBlockingMRCSupported"),
        ("HM2-L2REDUNDANCY-MIB", "hm2MrpRingOperState"))
)
if mibBuilder.loadTexts:
    hm2MrpDomainManagerGroup.setStatus("current")

hm2MrpDomainDiagGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 1, 2, 2, 3)
)
hm2MrpDomainDiagGroup.setObjects(
      *(("HM2-L2REDUNDANCY-MIB", "hm2MrpMRMRingOpenCount"),
        ("HM2-L2REDUNDANCY-MIB", "hm2MrpMRMLastRingOpenChange"),
        ("HM2-L2REDUNDANCY-MIB", "hm2MrpMRMRoundTripDelayMax"),
        ("HM2-L2REDUNDANCY-MIB", "hm2MrpMRMRoundTripDelayMin"),
        ("HM2-L2REDUNDANCY-MIB", "hm2MrpMRMRoundTripDelayReset"))
)
if mibBuilder.loadTexts:
    hm2MrpDomainDiagGroup.setStatus("current")


# Notification objects

hm2MrpReconfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 0, 1)
)
hm2MrpReconfig.setObjects(
    ("HM2-L2REDUNDANCY-MIB", "hm2MrpRingOperState")
)
if mibBuilder.loadTexts:
    hm2MrpReconfig.setStatus(
        "current"
    )

hm2SrmReconfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 0, 2)
)
hm2SrmReconfig.setObjects(
      *(("HM2-L2REDUNDANCY-MIB", "hm2SrmRingID"),
        ("HM2-L2REDUNDANCY-MIB", "hm2SrmSubRingOperState"))
)
if mibBuilder.loadTexts:
    hm2SrmReconfig.setStatus(
        "current"
    )

hm2RingCplReconfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 0, 3)
)
hm2RingCplReconfig.setObjects(
      *(("HM2-L2REDUNDANCY-MIB", "hm2RingCplInterconnIfOpState"),
        ("HM2-L2REDUNDANCY-MIB", "hm2RingCplPartnerInterconnIfOpState"),
        ("HM2-L2REDUNDANCY-MIB", "hm2RingCplPartnerIpAddrType"),
        ("HM2-L2REDUNDANCY-MIB", "hm2RingCplPartnerIpAddr"))
)
if mibBuilder.loadTexts:
    hm2RingCplReconfig.setStatus(
        "current"
    )

hm2RedundantCplReconfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 0, 4)
)
hm2RedundantCplReconfig.setObjects(
      *(("HM2-L2REDUNDANCY-MIB", "hm2RedundantCplCurrentRole"),
        ("HM2-L2REDUNDANCY-MIB", "hm2RedundantCplState"))
)
if mibBuilder.loadTexts:
    hm2RedundantCplReconfig.setStatus(
        "current"
    )


# Notifications groups

hm2MrpNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 1, 2, 2, 4)
)
hm2MrpNotificationsGroup.setObjects(
    ("HM2-L2REDUNDANCY-MIB", "hm2MrpReconfig")
)
if mibBuilder.loadTexts:
    hm2MrpNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hm2MrpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hm2MrpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HM2-L2REDUNDANCY-MIB",
    **{"Hm2CplPortOpState": Hm2CplPortOpState,
       "hm2L2RedundancyMib": hm2L2RedundancyMib,
       "hm2L2RedundancyMibNotifications": hm2L2RedundancyMibNotifications,
       "hm2MrpReconfig": hm2MrpReconfig,
       "hm2SrmReconfig": hm2SrmReconfig,
       "hm2RingCplReconfig": hm2RingCplReconfig,
       "hm2RedundantCplReconfig": hm2RedundantCplReconfig,
       "hm2L2RedundancyMibObjects": hm2L2RedundancyMibObjects,
       "hm2MrpMibGroup": hm2MrpMibGroup,
       "hm2MrpTable": hm2MrpTable,
       "hm2MrpEntry": hm2MrpEntry,
       "hm2MrpDomainID": hm2MrpDomainID,
       "hm2MrpDomainName": hm2MrpDomainName,
       "hm2MrpRingport1GroupID": hm2MrpRingport1GroupID,
       "hm2MrpRingport1IfIndex": hm2MrpRingport1IfIndex,
       "hm2MrpRingport1OperState": hm2MrpRingport1OperState,
       "hm2MrpRingport2GroupID": hm2MrpRingport2GroupID,
       "hm2MrpRingport2IfIndex": hm2MrpRingport2IfIndex,
       "hm2MrpRingport2OperState": hm2MrpRingport2OperState,
       "hm2MrpRoleAdminState": hm2MrpRoleAdminState,
       "hm2MrpRoleOperState": hm2MrpRoleOperState,
       "hm2MrpRecoveryDelay": hm2MrpRecoveryDelay,
       "hm2MrpRecoveryDelaySupported": hm2MrpRecoveryDelaySupported,
       "hm2MrpVlanID": hm2MrpVlanID,
       "hm2MrpMRMPriority": hm2MrpMRMPriority,
       "hm2MrpMRMReactOnLinkChange": hm2MrpMRMReactOnLinkChange,
       "hm2MrpMRMRingOpenCount": hm2MrpMRMRingOpenCount,
       "hm2MrpMRMLastRingOpenChange": hm2MrpMRMLastRingOpenChange,
       "hm2MrpMRMRoundTripDelayMax": hm2MrpMRMRoundTripDelayMax,
       "hm2MrpMRMRoundTripDelayMin": hm2MrpMRMRoundTripDelayMin,
       "hm2MrpMRMRoundTripDelayReset": hm2MrpMRMRoundTripDelayReset,
       "hm2MrpMRMNonBlockingMRCSupported": hm2MrpMRMNonBlockingMRCSupported,
       "hm2MrpMRCBlockedSupported": hm2MrpMRCBlockedSupported,
       "hm2MrpRingOperState": hm2MrpRingOperState,
       "hm2MrpRedundancyOperState": hm2MrpRedundancyOperState,
       "hm2MrpConfigOperState": hm2MrpConfigOperState,
       "hm2MrpRowStatus": hm2MrpRowStatus,
       "hm2MrpRingport2FixedBackup": hm2MrpRingport2FixedBackup,
       "hm2MrpConformance": hm2MrpConformance,
       "hm2MrpCompliances": hm2MrpCompliances,
       "hm2MrpCompliance": hm2MrpCompliance,
       "hm2MrpGroups": hm2MrpGroups,
       "hm2MrpDomainBasicGroup": hm2MrpDomainBasicGroup,
       "hm2MrpDomainManagerGroup": hm2MrpDomainManagerGroup,
       "hm2MrpDomainDiagGroup": hm2MrpDomainDiagGroup,
       "hm2MrpNotificationsGroup": hm2MrpNotificationsGroup,
       "hm2MrpFastMrp": hm2MrpFastMrp,
       "hm2SrmMibGroup": hm2SrmMibGroup,
       "hm2SrmGlobalAdminState": hm2SrmGlobalAdminState,
       "hm2SrmMaxInstances": hm2SrmMaxInstances,
       "hm2SrmTable": hm2SrmTable,
       "hm2SrmEntry": hm2SrmEntry,
       "hm2SrmRingID": hm2SrmRingID,
       "hm2SrmAdminState": hm2SrmAdminState,
       "hm2SrmOperState": hm2SrmOperState,
       "hm2SrmVlanID": hm2SrmVlanID,
       "hm2SrmMRPDomainID": hm2SrmMRPDomainID,
       "hm2SrmPartnerMAC": hm2SrmPartnerMAC,
       "hm2SrmSubRingProtocol": hm2SrmSubRingProtocol,
       "hm2SrmSubRingName": hm2SrmSubRingName,
       "hm2SrmSubRingPortIfIndex": hm2SrmSubRingPortIfIndex,
       "hm2SrmSubRingPortOperState": hm2SrmSubRingPortOperState,
       "hm2SrmSubRingOperState": hm2SrmSubRingOperState,
       "hm2SrmRedundancyOperState": hm2SrmRedundancyOperState,
       "hm2SrmConfigOperState": hm2SrmConfigOperState,
       "hm2SrmRowStatus": hm2SrmRowStatus,
       "hm2RingRedMibGroup": hm2RingRedMibGroup,
       "hm2RingRedAdminState": hm2RingRedAdminState,
       "hm2RingRedMode": hm2RingRedMode,
       "hm2RingRedPrimaryIntf": hm2RingRedPrimaryIntf,
       "hm2RingRedPrimaryIntfState": hm2RingRedPrimaryIntfState,
       "hm2RingRedSecondaryIntf": hm2RingRedSecondaryIntf,
       "hm2RingRedSecondaryIntfState": hm2RingRedSecondaryIntfState,
       "hm2RingCouplingMibGroup": hm2RingCouplingMibGroup,
       "hm2RingCouplingTable": hm2RingCouplingTable,
       "hm2RingCouplingEntry": hm2RingCouplingEntry,
       "hm2RingCplInterconnIfIndex": hm2RingCplInterconnIfIndex,
       "hm2RingCplInterconnIfOpState": hm2RingCplInterconnIfOpState,
       "hm2RingCplControlIfIndex": hm2RingCplControlIfIndex,
       "hm2RingCplControlIfOpState": hm2RingCplControlIfOpState,
       "hm2RingCplPartnerInterconnIfIndex": hm2RingCplPartnerInterconnIfIndex,
       "hm2RingCplPartnerInterconnIfOpState": hm2RingCplPartnerInterconnIfOpState,
       "hm2RingCplPartnerIpAddrType": hm2RingCplPartnerIpAddrType,
       "hm2RingCplPartnerIpAddr": hm2RingCplPartnerIpAddr,
       "hm2RingCplCouplingMode": hm2RingCplCouplingMode,
       "hm2RingCplControlModeOperState": hm2RingCplControlModeOperState,
       "hm2RingCplModeOperState": hm2RingCplModeOperState,
       "hm2RingCplOperState": hm2RingCplOperState,
       "hm2RingCplConfigOperState": hm2RingCplConfigOperState,
       "hm2RingCplCouplingLinks": hm2RingCplCouplingLinks,
       "hm2RingCplExtendedDiag": hm2RingCplExtendedDiag,
       "hm2RingCplNetCoupling": hm2RingCplNetCoupling,
       "hm2RingCplRedOperState": hm2RingCplRedOperState,
       "hm2RingCplRowStatus": hm2RingCplRowStatus,
       "hm2RedundantCplConfigMibGroup": hm2RedundantCplConfigMibGroup,
       "hm2RedundantCplAdminState": hm2RedundantCplAdminState,
       "hm2RedundantCplInPrimaryPort": hm2RedundantCplInPrimaryPort,
       "hm2RedundantCplOutPrimaryPort": hm2RedundantCplOutPrimaryPort,
       "hm2RedundantCplInSecondaryPort": hm2RedundantCplInSecondaryPort,
       "hm2RedundantCplOutSecondaryPort": hm2RedundantCplOutSecondaryPort,
       "hm2RedundantCplRole": hm2RedundantCplRole,
       "hm2RedundantCplCurrentRole": hm2RedundantCplCurrentRole,
       "hm2RedundantCplTimeout": hm2RedundantCplTimeout,
       "hm2RedundantCplPartner": hm2RedundantCplPartner,
       "hm2RedundantCplPartnerPrimaryPort": hm2RedundantCplPartnerPrimaryPort,
       "hm2RedundantCplPartnerSecodaryPort": hm2RedundantCplPartnerSecodaryPort,
       "hm2RedundantCplState": hm2RedundantCplState,
       "hm2RedundantCplRedundancyState": hm2RedundantCplRedundancyState,
       "hm2RedundantCplPartnerIPAddrType": hm2RedundantCplPartnerIPAddrType,
       "hm2RedundantCplPartnerIPAddr": hm2RedundantCplPartnerIPAddr,
       "hm2L2RedundancyMibSNMPExtensionGroup": hm2L2RedundancyMibSNMPExtensionGroup,
       "hm2RingCouplingMibSESGroup": hm2RingCouplingMibSESGroup,
       "hm2RingCouplingInvalidPortConfiguration": hm2RingCouplingInvalidPortConfiguration,
       "hm2RedundantCplSESGroup": hm2RedundantCplSESGroup,
       "hm2RedundantCplPortsMissing": hm2RedundantCplPortsMissing}
)
