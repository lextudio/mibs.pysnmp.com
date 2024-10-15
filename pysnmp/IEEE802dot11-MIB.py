# SNMP MIB module (IEEE802dot11-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IEEE802dot11-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:46 2024
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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ieee802dot11 = ModuleIdentity(
    (1, 2, 840, 10036)
)


# Types definitions



class WEPKeytype(OctetString):
    """Custom type WEPKeytype based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Member_body_ObjectIdentity = ObjectIdentity
member_body = _Member_body_ObjectIdentity(
    (1, 2)
)
_Us_ObjectIdentity = ObjectIdentity
us = _Us_ObjectIdentity(
    (1, 2, 840)
)
_Dot11smt_ObjectIdentity = ObjectIdentity
dot11smt = _Dot11smt_ObjectIdentity(
    (1, 2, 840, 10036, 1)
)
_Dot11StationConfigTable_Object = MibTable
dot11StationConfigTable = _Dot11StationConfigTable_Object(
    (1, 2, 840, 10036, 1, 1)
)
if mibBuilder.loadTexts:
    dot11StationConfigTable.setStatus("current")
_Dot11StationConfigEntry_Object = MibTableRow
dot11StationConfigEntry = _Dot11StationConfigEntry_Object(
    (1, 2, 840, 10036, 1, 1, 1)
)
dot11StationConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11StationConfigEntry.setStatus("current")
_Dot11StationID_Type = MacAddress
_Dot11StationID_Object = MibTableColumn
dot11StationID = _Dot11StationID_Object(
    (1, 2, 840, 10036, 1, 1, 1, 1),
    _Dot11StationID_Type()
)
dot11StationID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11StationID.setStatus("deprecated")


class _Dot11MediumOccupancyLimit_Type(Integer32):
    """Custom type dot11MediumOccupancyLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dot11MediumOccupancyLimit_Type.__name__ = "Integer32"
_Dot11MediumOccupancyLimit_Object = MibTableColumn
dot11MediumOccupancyLimit = _Dot11MediumOccupancyLimit_Object(
    (1, 2, 840, 10036, 1, 1, 1, 2),
    _Dot11MediumOccupancyLimit_Type()
)
dot11MediumOccupancyLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MediumOccupancyLimit.setStatus("current")
_Dot11CFPollable_Type = TruthValue
_Dot11CFPollable_Object = MibTableColumn
dot11CFPollable = _Dot11CFPollable_Object(
    (1, 2, 840, 10036, 1, 1, 1, 3),
    _Dot11CFPollable_Type()
)
dot11CFPollable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11CFPollable.setStatus("current")


class _Dot11CFPPeriod_Type(Integer32):
    """Custom type dot11CFPPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Dot11CFPPeriod_Type.__name__ = "Integer32"
_Dot11CFPPeriod_Object = MibTableColumn
dot11CFPPeriod = _Dot11CFPPeriod_Object(
    (1, 2, 840, 10036, 1, 1, 1, 4),
    _Dot11CFPPeriod_Type()
)
dot11CFPPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11CFPPeriod.setStatus("current")


class _Dot11CFPMaxDuration_Type(Integer32):
    """Custom type dot11CFPMaxDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot11CFPMaxDuration_Type.__name__ = "Integer32"
_Dot11CFPMaxDuration_Object = MibTableColumn
dot11CFPMaxDuration = _Dot11CFPMaxDuration_Object(
    (1, 2, 840, 10036, 1, 1, 1, 5),
    _Dot11CFPMaxDuration_Type()
)
dot11CFPMaxDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11CFPMaxDuration.setStatus("current")


class _Dot11AuthenticationResponseTimeOut_Type(Unsigned32):
    """Custom type dot11AuthenticationResponseTimeOut based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Dot11AuthenticationResponseTimeOut_Type.__name__ = "Unsigned32"
_Dot11AuthenticationResponseTimeOut_Object = MibTableColumn
dot11AuthenticationResponseTimeOut = _Dot11AuthenticationResponseTimeOut_Object(
    (1, 2, 840, 10036, 1, 1, 1, 6),
    _Dot11AuthenticationResponseTimeOut_Type()
)
dot11AuthenticationResponseTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11AuthenticationResponseTimeOut.setStatus("current")
_Dot11PrivacyOptionImplemented_Type = TruthValue
_Dot11PrivacyOptionImplemented_Object = MibTableColumn
dot11PrivacyOptionImplemented = _Dot11PrivacyOptionImplemented_Object(
    (1, 2, 840, 10036, 1, 1, 1, 7),
    _Dot11PrivacyOptionImplemented_Type()
)
dot11PrivacyOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11PrivacyOptionImplemented.setStatus("current")


class _Dot11PowerManagementMode_Type(Integer32):
    """Custom type dot11PowerManagementMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("powersave", 2))
    )


_Dot11PowerManagementMode_Type.__name__ = "Integer32"
_Dot11PowerManagementMode_Object = MibTableColumn
dot11PowerManagementMode = _Dot11PowerManagementMode_Object(
    (1, 2, 840, 10036, 1, 1, 1, 8),
    _Dot11PowerManagementMode_Type()
)
dot11PowerManagementMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11PowerManagementMode.setStatus("current")


class _Dot11DesiredSSID_Type(OctetString):
    """Custom type dot11DesiredSSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Dot11DesiredSSID_Type.__name__ = "OctetString"
_Dot11DesiredSSID_Object = MibTableColumn
dot11DesiredSSID = _Dot11DesiredSSID_Object(
    (1, 2, 840, 10036, 1, 1, 1, 9),
    _Dot11DesiredSSID_Type()
)
dot11DesiredSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11DesiredSSID.setStatus("current")


class _Dot11DesiredBSSType_Type(Integer32):
    """Custom type dot11DesiredBSSType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 3),
          ("independent", 2),
          ("infrastructure", 1))
    )


_Dot11DesiredBSSType_Type.__name__ = "Integer32"
_Dot11DesiredBSSType_Object = MibTableColumn
dot11DesiredBSSType = _Dot11DesiredBSSType_Object(
    (1, 2, 840, 10036, 1, 1, 1, 10),
    _Dot11DesiredBSSType_Type()
)
dot11DesiredBSSType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11DesiredBSSType.setStatus("current")


class _Dot11OperationalRateSet_Type(OctetString):
    """Custom type dot11OperationalRateSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 126),
    )


_Dot11OperationalRateSet_Type.__name__ = "OctetString"
_Dot11OperationalRateSet_Object = MibTableColumn
dot11OperationalRateSet = _Dot11OperationalRateSet_Object(
    (1, 2, 840, 10036, 1, 1, 1, 11),
    _Dot11OperationalRateSet_Type()
)
dot11OperationalRateSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11OperationalRateSet.setStatus("current")


class _Dot11BeaconPeriod_Type(Integer32):
    """Custom type dot11BeaconPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot11BeaconPeriod_Type.__name__ = "Integer32"
_Dot11BeaconPeriod_Object = MibTableColumn
dot11BeaconPeriod = _Dot11BeaconPeriod_Object(
    (1, 2, 840, 10036, 1, 1, 1, 12),
    _Dot11BeaconPeriod_Type()
)
dot11BeaconPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11BeaconPeriod.setStatus("current")


class _Dot11DTIMPeriod_Type(Integer32):
    """Custom type dot11DTIMPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Dot11DTIMPeriod_Type.__name__ = "Integer32"
_Dot11DTIMPeriod_Object = MibTableColumn
dot11DTIMPeriod = _Dot11DTIMPeriod_Object(
    (1, 2, 840, 10036, 1, 1, 1, 13),
    _Dot11DTIMPeriod_Type()
)
dot11DTIMPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11DTIMPeriod.setStatus("current")


class _Dot11AssociationResponseTimeOut_Type(Unsigned32):
    """Custom type dot11AssociationResponseTimeOut based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Dot11AssociationResponseTimeOut_Type.__name__ = "Unsigned32"
_Dot11AssociationResponseTimeOut_Object = MibTableColumn
dot11AssociationResponseTimeOut = _Dot11AssociationResponseTimeOut_Object(
    (1, 2, 840, 10036, 1, 1, 1, 14),
    _Dot11AssociationResponseTimeOut_Type()
)
dot11AssociationResponseTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11AssociationResponseTimeOut.setStatus("current")


class _Dot11DisassociateReason_Type(Integer32):
    """Custom type dot11DisassociateReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot11DisassociateReason_Type.__name__ = "Integer32"
_Dot11DisassociateReason_Object = MibTableColumn
dot11DisassociateReason = _Dot11DisassociateReason_Object(
    (1, 2, 840, 10036, 1, 1, 1, 15),
    _Dot11DisassociateReason_Type()
)
dot11DisassociateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11DisassociateReason.setStatus("current")
_Dot11DisassociateStation_Type = MacAddress
_Dot11DisassociateStation_Object = MibTableColumn
dot11DisassociateStation = _Dot11DisassociateStation_Object(
    (1, 2, 840, 10036, 1, 1, 1, 16),
    _Dot11DisassociateStation_Type()
)
dot11DisassociateStation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11DisassociateStation.setStatus("current")


class _Dot11DeauthenticateReason_Type(Integer32):
    """Custom type dot11DeauthenticateReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot11DeauthenticateReason_Type.__name__ = "Integer32"
_Dot11DeauthenticateReason_Object = MibTableColumn
dot11DeauthenticateReason = _Dot11DeauthenticateReason_Object(
    (1, 2, 840, 10036, 1, 1, 1, 17),
    _Dot11DeauthenticateReason_Type()
)
dot11DeauthenticateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11DeauthenticateReason.setStatus("current")
_Dot11DeauthenticateStation_Type = MacAddress
_Dot11DeauthenticateStation_Object = MibTableColumn
dot11DeauthenticateStation = _Dot11DeauthenticateStation_Object(
    (1, 2, 840, 10036, 1, 1, 1, 18),
    _Dot11DeauthenticateStation_Type()
)
dot11DeauthenticateStation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11DeauthenticateStation.setStatus("current")


class _Dot11AuthenticateFailStatus_Type(Integer32):
    """Custom type dot11AuthenticateFailStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot11AuthenticateFailStatus_Type.__name__ = "Integer32"
_Dot11AuthenticateFailStatus_Object = MibTableColumn
dot11AuthenticateFailStatus = _Dot11AuthenticateFailStatus_Object(
    (1, 2, 840, 10036, 1, 1, 1, 19),
    _Dot11AuthenticateFailStatus_Type()
)
dot11AuthenticateFailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11AuthenticateFailStatus.setStatus("current")
_Dot11AuthenticateFailStation_Type = MacAddress
_Dot11AuthenticateFailStation_Object = MibTableColumn
dot11AuthenticateFailStation = _Dot11AuthenticateFailStation_Object(
    (1, 2, 840, 10036, 1, 1, 1, 20),
    _Dot11AuthenticateFailStation_Type()
)
dot11AuthenticateFailStation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11AuthenticateFailStation.setStatus("current")
_Dot11MultiDomainCapabilityImplemented_Type = TruthValue
_Dot11MultiDomainCapabilityImplemented_Object = MibTableColumn
dot11MultiDomainCapabilityImplemented = _Dot11MultiDomainCapabilityImplemented_Object(
    (1, 2, 840, 10036, 1, 1, 1, 21),
    _Dot11MultiDomainCapabilityImplemented_Type()
)
dot11MultiDomainCapabilityImplemented.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MultiDomainCapabilityImplemented.setStatus("current")
_Dot11MultiDomainCapabilityEnabled_Type = TruthValue
_Dot11MultiDomainCapabilityEnabled_Object = MibTableColumn
dot11MultiDomainCapabilityEnabled = _Dot11MultiDomainCapabilityEnabled_Object(
    (1, 2, 840, 10036, 1, 1, 1, 22),
    _Dot11MultiDomainCapabilityEnabled_Type()
)
dot11MultiDomainCapabilityEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MultiDomainCapabilityEnabled.setStatus("current")


class _Dot11CountryString_Type(OctetString):
    """Custom type dot11CountryString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_Dot11CountryString_Type.__name__ = "OctetString"
_Dot11CountryString_Object = MibTableColumn
dot11CountryString = _Dot11CountryString_Object(
    (1, 2, 840, 10036, 1, 1, 1, 23),
    _Dot11CountryString_Type()
)
dot11CountryString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11CountryString.setStatus("current")
_Dot11SpectrumManagementImplemented_Type = TruthValue
_Dot11SpectrumManagementImplemented_Object = MibTableColumn
dot11SpectrumManagementImplemented = _Dot11SpectrumManagementImplemented_Object(
    (1, 2, 840, 10036, 1, 1, 1, 24),
    _Dot11SpectrumManagementImplemented_Type()
)
dot11SpectrumManagementImplemented.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11SpectrumManagementImplemented.setStatus("current")
_Dot11SpectrumManagementRequired_Type = TruthValue
_Dot11SpectrumManagementRequired_Object = MibTableColumn
dot11SpectrumManagementRequired = _Dot11SpectrumManagementRequired_Object(
    (1, 2, 840, 10036, 1, 1, 1, 25),
    _Dot11SpectrumManagementRequired_Type()
)
dot11SpectrumManagementRequired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11SpectrumManagementRequired.setStatus("current")
_Dot11RSNAOptionImplemented_Type = TruthValue
_Dot11RSNAOptionImplemented_Object = MibTableColumn
dot11RSNAOptionImplemented = _Dot11RSNAOptionImplemented_Object(
    (1, 2, 840, 10036, 1, 1, 1, 26),
    _Dot11RSNAOptionImplemented_Type()
)
dot11RSNAOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RSNAOptionImplemented.setStatus("current")
_Dot11RSNAPreauthenticationImplemented_Type = TruthValue
_Dot11RSNAPreauthenticationImplemented_Object = MibTableColumn
dot11RSNAPreauthenticationImplemented = _Dot11RSNAPreauthenticationImplemented_Object(
    (1, 2, 840, 10036, 1, 1, 1, 27),
    _Dot11RSNAPreauthenticationImplemented_Type()
)
dot11RSNAPreauthenticationImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RSNAPreauthenticationImplemented.setStatus("current")


class _Dot11QosOptionImplemented_Type(TruthValue):
    """Custom type dot11QosOptionImplemented based on TruthValue"""


_Dot11QosOptionImplemented_Object = MibTableColumn
dot11QosOptionImplemented = _Dot11QosOptionImplemented_Object(
    (1, 2, 840, 10036, 1, 1, 1, 30),
    _Dot11QosOptionImplemented_Type()
)
dot11QosOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11QosOptionImplemented.setStatus("current")


class _Dot11ImmediateBlockAckOptionImplemented_Type(TruthValue):
    """Custom type dot11ImmediateBlockAckOptionImplemented based on TruthValue"""


_Dot11ImmediateBlockAckOptionImplemented_Object = MibTableColumn
dot11ImmediateBlockAckOptionImplemented = _Dot11ImmediateBlockAckOptionImplemented_Object(
    (1, 2, 840, 10036, 1, 1, 1, 31),
    _Dot11ImmediateBlockAckOptionImplemented_Type()
)
dot11ImmediateBlockAckOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ImmediateBlockAckOptionImplemented.setStatus("current")


class _Dot11DelayedBlockAckOptionImplemented_Type(TruthValue):
    """Custom type dot11DelayedBlockAckOptionImplemented based on TruthValue"""


_Dot11DelayedBlockAckOptionImplemented_Object = MibTableColumn
dot11DelayedBlockAckOptionImplemented = _Dot11DelayedBlockAckOptionImplemented_Object(
    (1, 2, 840, 10036, 1, 1, 1, 32),
    _Dot11DelayedBlockAckOptionImplemented_Type()
)
dot11DelayedBlockAckOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11DelayedBlockAckOptionImplemented.setStatus("current")


class _Dot11DirectOptionImplemented_Type(TruthValue):
    """Custom type dot11DirectOptionImplemented based on TruthValue"""


_Dot11DirectOptionImplemented_Object = MibTableColumn
dot11DirectOptionImplemented = _Dot11DirectOptionImplemented_Object(
    (1, 2, 840, 10036, 1, 1, 1, 33),
    _Dot11DirectOptionImplemented_Type()
)
dot11DirectOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11DirectOptionImplemented.setStatus("current")


class _Dot11APSDOptionImplemented_Type(TruthValue):
    """Custom type dot11APSDOptionImplemented based on TruthValue"""


_Dot11APSDOptionImplemented_Object = MibTableColumn
dot11APSDOptionImplemented = _Dot11APSDOptionImplemented_Object(
    (1, 2, 840, 10036, 1, 1, 1, 34),
    _Dot11APSDOptionImplemented_Type()
)
dot11APSDOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11APSDOptionImplemented.setStatus("current")


class _Dot11QAckOptionImplemented_Type(TruthValue):
    """Custom type dot11QAckOptionImplemented based on TruthValue"""


_Dot11QAckOptionImplemented_Object = MibTableColumn
dot11QAckOptionImplemented = _Dot11QAckOptionImplemented_Object(
    (1, 2, 840, 10036, 1, 1, 1, 35),
    _Dot11QAckOptionImplemented_Type()
)
dot11QAckOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11QAckOptionImplemented.setStatus("current")


class _Dot11QBSSLoadOptionImplemented_Type(TruthValue):
    """Custom type dot11QBSSLoadOptionImplemented based on TruthValue"""


_Dot11QBSSLoadOptionImplemented_Object = MibTableColumn
dot11QBSSLoadOptionImplemented = _Dot11QBSSLoadOptionImplemented_Object(
    (1, 2, 840, 10036, 1, 1, 1, 36),
    _Dot11QBSSLoadOptionImplemented_Type()
)
dot11QBSSLoadOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11QBSSLoadOptionImplemented.setStatus("current")


class _Dot11QueueRequestOptionImplemented_Type(TruthValue):
    """Custom type dot11QueueRequestOptionImplemented based on TruthValue"""


_Dot11QueueRequestOptionImplemented_Object = MibTableColumn
dot11QueueRequestOptionImplemented = _Dot11QueueRequestOptionImplemented_Object(
    (1, 2, 840, 10036, 1, 1, 1, 37),
    _Dot11QueueRequestOptionImplemented_Type()
)
dot11QueueRequestOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11QueueRequestOptionImplemented.setStatus("current")


class _Dot11TXOPRequestOptionImplemented_Type(TruthValue):
    """Custom type dot11TXOPRequestOptionImplemented based on TruthValue"""


_Dot11TXOPRequestOptionImplemented_Object = MibTableColumn
dot11TXOPRequestOptionImplemented = _Dot11TXOPRequestOptionImplemented_Object(
    (1, 2, 840, 10036, 1, 1, 1, 38),
    _Dot11TXOPRequestOptionImplemented_Type()
)
dot11TXOPRequestOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TXOPRequestOptionImplemented.setStatus("current")


class _Dot11MoreDataAckOptionImplemented_Type(TruthValue):
    """Custom type dot11MoreDataAckOptionImplemented based on TruthValue"""


_Dot11MoreDataAckOptionImplemented_Object = MibTableColumn
dot11MoreDataAckOptionImplemented = _Dot11MoreDataAckOptionImplemented_Object(
    (1, 2, 840, 10036, 1, 1, 1, 39),
    _Dot11MoreDataAckOptionImplemented_Type()
)
dot11MoreDataAckOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11MoreDataAckOptionImplemented.setStatus("current")


class _Dot11AssociateinNQBSS_Type(TruthValue):
    """Custom type dot11AssociateinNQBSS based on TruthValue"""


_Dot11AssociateinNQBSS_Object = MibTableColumn
dot11AssociateinNQBSS = _Dot11AssociateinNQBSS_Object(
    (1, 2, 840, 10036, 1, 1, 1, 40),
    _Dot11AssociateinNQBSS_Type()
)
dot11AssociateinNQBSS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11AssociateinNQBSS.setStatus("current")


class _Dot11DLSAllowedInQBSS_Type(TruthValue):
    """Custom type dot11DLSAllowedInQBSS based on TruthValue"""


_Dot11DLSAllowedInQBSS_Object = MibTableColumn
dot11DLSAllowedInQBSS = _Dot11DLSAllowedInQBSS_Object(
    (1, 2, 840, 10036, 1, 1, 1, 41),
    _Dot11DLSAllowedInQBSS_Type()
)
dot11DLSAllowedInQBSS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11DLSAllowedInQBSS.setStatus("current")


class _Dot11DLSAllowed_Type(TruthValue):
    """Custom type dot11DLSAllowed based on TruthValue"""


_Dot11DLSAllowed_Object = MibTableColumn
dot11DLSAllowed = _Dot11DLSAllowed_Object(
    (1, 2, 840, 10036, 1, 1, 1, 42),
    _Dot11DLSAllowed_Type()
)
dot11DLSAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11DLSAllowed.setStatus("current")


class _Dot11HighThroughputOptionImplemented_Type(TruthValue):
    """Custom type dot11HighThroughputOptionImplemented based on TruthValue"""


_Dot11HighThroughputOptionImplemented_Object = MibTableColumn
dot11HighThroughputOptionImplemented = _Dot11HighThroughputOptionImplemented_Object(
    (1, 2, 840, 10036, 1, 1, 1, 58),
    _Dot11HighThroughputOptionImplemented_Type()
)
dot11HighThroughputOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11HighThroughputOptionImplemented.setStatus("current")
_Dot11AuthenticationAlgorithmsTable_Object = MibTable
dot11AuthenticationAlgorithmsTable = _Dot11AuthenticationAlgorithmsTable_Object(
    (1, 2, 840, 10036, 1, 2)
)
if mibBuilder.loadTexts:
    dot11AuthenticationAlgorithmsTable.setStatus("current")
_Dot11AuthenticationAlgorithmsEntry_Object = MibTableRow
dot11AuthenticationAlgorithmsEntry = _Dot11AuthenticationAlgorithmsEntry_Object(
    (1, 2, 840, 10036, 1, 2, 1)
)
dot11AuthenticationAlgorithmsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "IEEE802dot11-MIB", "dot11AuthenticationAlgorithmsIndex"),
)
if mibBuilder.loadTexts:
    dot11AuthenticationAlgorithmsEntry.setStatus("current")


class _Dot11AuthenticationAlgorithmsIndex_Type(Integer32):
    """Custom type dot11AuthenticationAlgorithmsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dot11AuthenticationAlgorithmsIndex_Type.__name__ = "Integer32"
_Dot11AuthenticationAlgorithmsIndex_Object = MibTableColumn
dot11AuthenticationAlgorithmsIndex = _Dot11AuthenticationAlgorithmsIndex_Object(
    (1, 2, 840, 10036, 1, 2, 1, 1),
    _Dot11AuthenticationAlgorithmsIndex_Type()
)
dot11AuthenticationAlgorithmsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11AuthenticationAlgorithmsIndex.setStatus("current")


class _Dot11AuthenticationAlgorithm_Type(Integer32):
    """Custom type dot11AuthenticationAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("openSystem", 1),
          ("sharedKey", 2))
    )


_Dot11AuthenticationAlgorithm_Type.__name__ = "Integer32"
_Dot11AuthenticationAlgorithm_Object = MibTableColumn
dot11AuthenticationAlgorithm = _Dot11AuthenticationAlgorithm_Object(
    (1, 2, 840, 10036, 1, 2, 1, 2),
    _Dot11AuthenticationAlgorithm_Type()
)
dot11AuthenticationAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11AuthenticationAlgorithm.setStatus("current")
_Dot11AuthenticationAlgorithmsEnable_Type = TruthValue
_Dot11AuthenticationAlgorithmsEnable_Object = MibTableColumn
dot11AuthenticationAlgorithmsEnable = _Dot11AuthenticationAlgorithmsEnable_Object(
    (1, 2, 840, 10036, 1, 2, 1, 3),
    _Dot11AuthenticationAlgorithmsEnable_Type()
)
dot11AuthenticationAlgorithmsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11AuthenticationAlgorithmsEnable.setStatus("current")
_Dot11WEPDefaultKeysTable_Object = MibTable
dot11WEPDefaultKeysTable = _Dot11WEPDefaultKeysTable_Object(
    (1, 2, 840, 10036, 1, 3)
)
if mibBuilder.loadTexts:
    dot11WEPDefaultKeysTable.setStatus("current")
_Dot11WEPDefaultKeysEntry_Object = MibTableRow
dot11WEPDefaultKeysEntry = _Dot11WEPDefaultKeysEntry_Object(
    (1, 2, 840, 10036, 1, 3, 1)
)
dot11WEPDefaultKeysEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "IEEE802dot11-MIB", "dot11WEPDefaultKeyIndex"),
)
if mibBuilder.loadTexts:
    dot11WEPDefaultKeysEntry.setStatus("current")


class _Dot11WEPDefaultKeyIndex_Type(Integer32):
    """Custom type dot11WEPDefaultKeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Dot11WEPDefaultKeyIndex_Type.__name__ = "Integer32"
_Dot11WEPDefaultKeyIndex_Object = MibTableColumn
dot11WEPDefaultKeyIndex = _Dot11WEPDefaultKeyIndex_Object(
    (1, 2, 840, 10036, 1, 3, 1, 1),
    _Dot11WEPDefaultKeyIndex_Type()
)
dot11WEPDefaultKeyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11WEPDefaultKeyIndex.setStatus("current")
_Dot11WEPDefaultKeyValue_Type = WEPKeytype
_Dot11WEPDefaultKeyValue_Object = MibTableColumn
dot11WEPDefaultKeyValue = _Dot11WEPDefaultKeyValue_Object(
    (1, 2, 840, 10036, 1, 3, 1, 2),
    _Dot11WEPDefaultKeyValue_Type()
)
dot11WEPDefaultKeyValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11WEPDefaultKeyValue.setStatus("current")
_Dot11WEPKeyMappingsTable_Object = MibTable
dot11WEPKeyMappingsTable = _Dot11WEPKeyMappingsTable_Object(
    (1, 2, 840, 10036, 1, 4)
)
if mibBuilder.loadTexts:
    dot11WEPKeyMappingsTable.setStatus("current")
_Dot11WEPKeyMappingsEntry_Object = MibTableRow
dot11WEPKeyMappingsEntry = _Dot11WEPKeyMappingsEntry_Object(
    (1, 2, 840, 10036, 1, 4, 1)
)
dot11WEPKeyMappingsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "IEEE802dot11-MIB", "dot11WEPKeyMappingIndex"),
)
if mibBuilder.loadTexts:
    dot11WEPKeyMappingsEntry.setStatus("current")


class _Dot11WEPKeyMappingIndex_Type(Integer32):
    """Custom type dot11WEPKeyMappingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dot11WEPKeyMappingIndex_Type.__name__ = "Integer32"
_Dot11WEPKeyMappingIndex_Object = MibTableColumn
dot11WEPKeyMappingIndex = _Dot11WEPKeyMappingIndex_Object(
    (1, 2, 840, 10036, 1, 4, 1, 1),
    _Dot11WEPKeyMappingIndex_Type()
)
dot11WEPKeyMappingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11WEPKeyMappingIndex.setStatus("current")
_Dot11WEPKeyMappingAddress_Type = MacAddress
_Dot11WEPKeyMappingAddress_Object = MibTableColumn
dot11WEPKeyMappingAddress = _Dot11WEPKeyMappingAddress_Object(
    (1, 2, 840, 10036, 1, 4, 1, 2),
    _Dot11WEPKeyMappingAddress_Type()
)
dot11WEPKeyMappingAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot11WEPKeyMappingAddress.setStatus("current")
_Dot11WEPKeyMappingWEPOn_Type = TruthValue
_Dot11WEPKeyMappingWEPOn_Object = MibTableColumn
dot11WEPKeyMappingWEPOn = _Dot11WEPKeyMappingWEPOn_Object(
    (1, 2, 840, 10036, 1, 4, 1, 3),
    _Dot11WEPKeyMappingWEPOn_Type()
)
dot11WEPKeyMappingWEPOn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot11WEPKeyMappingWEPOn.setStatus("current")
_Dot11WEPKeyMappingValue_Type = WEPKeytype
_Dot11WEPKeyMappingValue_Object = MibTableColumn
dot11WEPKeyMappingValue = _Dot11WEPKeyMappingValue_Object(
    (1, 2, 840, 10036, 1, 4, 1, 4),
    _Dot11WEPKeyMappingValue_Type()
)
dot11WEPKeyMappingValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot11WEPKeyMappingValue.setStatus("current")


class _Dot11WEPKeyMappingStatus_Type(RowStatus):
    """Custom type dot11WEPKeyMappingStatus based on RowStatus"""


_Dot11WEPKeyMappingStatus_Object = MibTableColumn
dot11WEPKeyMappingStatus = _Dot11WEPKeyMappingStatus_Object(
    (1, 2, 840, 10036, 1, 4, 1, 5),
    _Dot11WEPKeyMappingStatus_Type()
)
dot11WEPKeyMappingStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot11WEPKeyMappingStatus.setStatus("current")
_Dot11PrivacyTable_Object = MibTable
dot11PrivacyTable = _Dot11PrivacyTable_Object(
    (1, 2, 840, 10036, 1, 5)
)
if mibBuilder.loadTexts:
    dot11PrivacyTable.setStatus("current")
_Dot11PrivacyEntry_Object = MibTableRow
dot11PrivacyEntry = _Dot11PrivacyEntry_Object(
    (1, 2, 840, 10036, 1, 5, 1)
)
dot11PrivacyEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11PrivacyEntry.setStatus("current")
_Dot11PrivacyInvoked_Type = TruthValue
_Dot11PrivacyInvoked_Object = MibTableColumn
dot11PrivacyInvoked = _Dot11PrivacyInvoked_Object(
    (1, 2, 840, 10036, 1, 5, 1, 1),
    _Dot11PrivacyInvoked_Type()
)
dot11PrivacyInvoked.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11PrivacyInvoked.setStatus("current")


class _Dot11WEPDefaultKeyID_Type(Integer32):
    """Custom type dot11WEPDefaultKeyID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Dot11WEPDefaultKeyID_Type.__name__ = "Integer32"
_Dot11WEPDefaultKeyID_Object = MibTableColumn
dot11WEPDefaultKeyID = _Dot11WEPDefaultKeyID_Object(
    (1, 2, 840, 10036, 1, 5, 1, 2),
    _Dot11WEPDefaultKeyID_Type()
)
dot11WEPDefaultKeyID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11WEPDefaultKeyID.setStatus("current")


class _Dot11WEPKeyMappingLength_Type(Unsigned32):
    """Custom type dot11WEPKeyMappingLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 4294967295),
    )


_Dot11WEPKeyMappingLength_Type.__name__ = "Unsigned32"
_Dot11WEPKeyMappingLength_Object = MibTableColumn
dot11WEPKeyMappingLength = _Dot11WEPKeyMappingLength_Object(
    (1, 2, 840, 10036, 1, 5, 1, 3),
    _Dot11WEPKeyMappingLength_Type()
)
dot11WEPKeyMappingLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11WEPKeyMappingLength.setStatus("current")
_Dot11ExcludeUnencrypted_Type = TruthValue
_Dot11ExcludeUnencrypted_Object = MibTableColumn
dot11ExcludeUnencrypted = _Dot11ExcludeUnencrypted_Object(
    (1, 2, 840, 10036, 1, 5, 1, 4),
    _Dot11ExcludeUnencrypted_Type()
)
dot11ExcludeUnencrypted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ExcludeUnencrypted.setStatus("current")
_Dot11WEPICVErrorCount_Type = Counter32
_Dot11WEPICVErrorCount_Object = MibTableColumn
dot11WEPICVErrorCount = _Dot11WEPICVErrorCount_Object(
    (1, 2, 840, 10036, 1, 5, 1, 5),
    _Dot11WEPICVErrorCount_Type()
)
dot11WEPICVErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11WEPICVErrorCount.setStatus("current")
_Dot11WEPExcludedCount_Type = Counter32
_Dot11WEPExcludedCount_Object = MibTableColumn
dot11WEPExcludedCount = _Dot11WEPExcludedCount_Object(
    (1, 2, 840, 10036, 1, 5, 1, 6),
    _Dot11WEPExcludedCount_Type()
)
dot11WEPExcludedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11WEPExcludedCount.setStatus("current")
_Dot11RSNAEnabled_Type = TruthValue
_Dot11RSNAEnabled_Object = MibTableColumn
dot11RSNAEnabled = _Dot11RSNAEnabled_Object(
    (1, 2, 840, 10036, 1, 5, 1, 7),
    _Dot11RSNAEnabled_Type()
)
dot11RSNAEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11RSNAEnabled.setStatus("current")
_Dot11RSNAPreAuthenticationEnabled_Type = TruthValue
_Dot11RSNAPreAuthenticationEnabled_Object = MibTableColumn
dot11RSNAPreAuthenticationEnabled = _Dot11RSNAPreAuthenticationEnabled_Object(
    (1, 2, 840, 10036, 1, 5, 1, 8),
    _Dot11RSNAPreAuthenticationEnabled_Type()
)
dot11RSNAPreAuthenticationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11RSNAPreAuthenticationEnabled.setStatus("current")
_Dot11SMTnotification_ObjectIdentity = ObjectIdentity
dot11SMTnotification = _Dot11SMTnotification_ObjectIdentity(
    (1, 2, 840, 10036, 1, 6)
)
_Dot11SMT_unknown_ObjectIdentity = ObjectIdentity
dot11SMT_unknown = _Dot11SMT_unknown_ObjectIdentity(
    (1, 2, 840, 10036, 1, 6, 0)
)
_Dot11MultiDomainCapabilityTable_Object = MibTable
dot11MultiDomainCapabilityTable = _Dot11MultiDomainCapabilityTable_Object(
    (1, 2, 840, 10036, 1, 7)
)
if mibBuilder.loadTexts:
    dot11MultiDomainCapabilityTable.setStatus("current")
_Dot11MultiDomainCapabilityEntry_Object = MibTableRow
dot11MultiDomainCapabilityEntry = _Dot11MultiDomainCapabilityEntry_Object(
    (1, 2, 840, 10036, 1, 7, 1)
)
dot11MultiDomainCapabilityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "IEEE802dot11-MIB", "dot11MultiDomainCapabilityIndex"),
)
if mibBuilder.loadTexts:
    dot11MultiDomainCapabilityEntry.setStatus("current")


class _Dot11MultiDomainCapabilityIndex_Type(Integer32):
    """Custom type dot11MultiDomainCapabilityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dot11MultiDomainCapabilityIndex_Type.__name__ = "Integer32"
_Dot11MultiDomainCapabilityIndex_Object = MibTableColumn
dot11MultiDomainCapabilityIndex = _Dot11MultiDomainCapabilityIndex_Object(
    (1, 2, 840, 10036, 1, 7, 1, 1),
    _Dot11MultiDomainCapabilityIndex_Type()
)
dot11MultiDomainCapabilityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11MultiDomainCapabilityIndex.setStatus("current")
_Dot11FirstChannelNumber_Type = Integer32
_Dot11FirstChannelNumber_Object = MibTableColumn
dot11FirstChannelNumber = _Dot11FirstChannelNumber_Object(
    (1, 2, 840, 10036, 1, 7, 1, 2),
    _Dot11FirstChannelNumber_Type()
)
dot11FirstChannelNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11FirstChannelNumber.setStatus("current")
_Dot11NumberofChannels_Type = Integer32
_Dot11NumberofChannels_Object = MibTableColumn
dot11NumberofChannels = _Dot11NumberofChannels_Object(
    (1, 2, 840, 10036, 1, 7, 1, 3),
    _Dot11NumberofChannels_Type()
)
dot11NumberofChannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11NumberofChannels.setStatus("current")
_Dot11MaximumTransmitPowerLevel_Type = Integer32
_Dot11MaximumTransmitPowerLevel_Object = MibTableColumn
dot11MaximumTransmitPowerLevel = _Dot11MaximumTransmitPowerLevel_Object(
    (1, 2, 840, 10036, 1, 7, 1, 4),
    _Dot11MaximumTransmitPowerLevel_Type()
)
dot11MaximumTransmitPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MaximumTransmitPowerLevel.setStatus("current")
_Dot11SpectrumManagementTable_Object = MibTable
dot11SpectrumManagementTable = _Dot11SpectrumManagementTable_Object(
    (1, 2, 840, 10036, 1, 8)
)
if mibBuilder.loadTexts:
    dot11SpectrumManagementTable.setStatus("current")
_Dot11SpectrumManagementEntry_Object = MibTableRow
dot11SpectrumManagementEntry = _Dot11SpectrumManagementEntry_Object(
    (1, 2, 840, 10036, 1, 8, 1)
)
dot11SpectrumManagementEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "IEEE802dot11-MIB", "dot11SpectrumManagementIndex"),
)
if mibBuilder.loadTexts:
    dot11SpectrumManagementEntry.setStatus("current")


class _Dot11SpectrumManagementIndex_Type(Integer32):
    """Custom type dot11SpectrumManagementIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dot11SpectrumManagementIndex_Type.__name__ = "Integer32"
_Dot11SpectrumManagementIndex_Object = MibTableColumn
dot11SpectrumManagementIndex = _Dot11SpectrumManagementIndex_Object(
    (1, 2, 840, 10036, 1, 8, 1, 1),
    _Dot11SpectrumManagementIndex_Type()
)
dot11SpectrumManagementIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11SpectrumManagementIndex.setStatus("current")
_Dot11MitigationRequirement_Type = Integer32
_Dot11MitigationRequirement_Object = MibTableColumn
dot11MitigationRequirement = _Dot11MitigationRequirement_Object(
    (1, 2, 840, 10036, 1, 8, 1, 2),
    _Dot11MitigationRequirement_Type()
)
dot11MitigationRequirement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MitigationRequirement.setStatus("current")
_Dot11ChannelSwitchTime_Type = Integer32
_Dot11ChannelSwitchTime_Object = MibTableColumn
dot11ChannelSwitchTime = _Dot11ChannelSwitchTime_Object(
    (1, 2, 840, 10036, 1, 8, 1, 3),
    _Dot11ChannelSwitchTime_Type()
)
dot11ChannelSwitchTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ChannelSwitchTime.setStatus("current")
_Dot11PowerCapabilityMax_Type = Integer32
_Dot11PowerCapabilityMax_Object = MibTableColumn
dot11PowerCapabilityMax = _Dot11PowerCapabilityMax_Object(
    (1, 2, 840, 10036, 1, 8, 1, 4),
    _Dot11PowerCapabilityMax_Type()
)
dot11PowerCapabilityMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11PowerCapabilityMax.setStatus("current")
_Dot11PowerCapabilityMin_Type = Integer32
_Dot11PowerCapabilityMin_Object = MibTableColumn
dot11PowerCapabilityMin = _Dot11PowerCapabilityMin_Object(
    (1, 2, 840, 10036, 1, 8, 1, 5),
    _Dot11PowerCapabilityMin_Type()
)
dot11PowerCapabilityMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11PowerCapabilityMin.setStatus("current")
_Dot11RSNAConfigTable_Object = MibTable
dot11RSNAConfigTable = _Dot11RSNAConfigTable_Object(
    (1, 2, 840, 10036, 1, 9)
)
if mibBuilder.loadTexts:
    dot11RSNAConfigTable.setStatus("current")
_Dot11RSNAConfigEntry_Object = MibTableRow
dot11RSNAConfigEntry = _Dot11RSNAConfigEntry_Object(
    (1, 2, 840, 10036, 1, 9, 1)
)
dot11RSNAConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11RSNAConfigEntry.setStatus("current")
_Dot11RSNAConfigVersion_Type = Integer32
_Dot11RSNAConfigVersion_Object = MibTableColumn
dot11RSNAConfigVersion = _Dot11RSNAConfigVersion_Object(
    (1, 2, 840, 10036, 1, 9, 1, 2),
    _Dot11RSNAConfigVersion_Type()
)
dot11RSNAConfigVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RSNAConfigVersion.setStatus("current")
_Dot11RSNAConfigPairwiseKeysSupported_Type = Unsigned32
_Dot11RSNAConfigPairwiseKeysSupported_Object = MibTableColumn
dot11RSNAConfigPairwiseKeysSupported = _Dot11RSNAConfigPairwiseKeysSupported_Object(
    (1, 2, 840, 10036, 1, 9, 1, 3),
    _Dot11RSNAConfigPairwiseKeysSupported_Type()
)
dot11RSNAConfigPairwiseKeysSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RSNAConfigPairwiseKeysSupported.setStatus("current")


class _Dot11RSNAConfigGroupCipher_Type(OctetString):
    """Custom type dot11RSNAConfigGroupCipher based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Dot11RSNAConfigGroupCipher_Type.__name__ = "OctetString"
_Dot11RSNAConfigGroupCipher_Object = MibTableColumn
dot11RSNAConfigGroupCipher = _Dot11RSNAConfigGroupCipher_Object(
    (1, 2, 840, 10036, 1, 9, 1, 4),
    _Dot11RSNAConfigGroupCipher_Type()
)
dot11RSNAConfigGroupCipher.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11RSNAConfigGroupCipher.setStatus("current")


class _Dot11RSNAConfigGroupRekeyMethod_Type(Integer32):
    """Custom type dot11RSNAConfigGroupRekeyMethod based on Integer32"""
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
        *(("disabled", 1),
          ("packetBased", 3),
          ("timeBased", 2),
          ("timepacket-Based", 4))
    )


_Dot11RSNAConfigGroupRekeyMethod_Type.__name__ = "Integer32"
_Dot11RSNAConfigGroupRekeyMethod_Object = MibTableColumn
dot11RSNAConfigGroupRekeyMethod = _Dot11RSNAConfigGroupRekeyMethod_Object(
    (1, 2, 840, 10036, 1, 9, 1, 5),
    _Dot11RSNAConfigGroupRekeyMethod_Type()
)
dot11RSNAConfigGroupRekeyMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11RSNAConfigGroupRekeyMethod.setStatus("current")


class _Dot11RSNAConfigGroupRekeyTime_Type(Unsigned32):
    """Custom type dot11RSNAConfigGroupRekeyTime based on Unsigned32"""
    defaultValue = 86400

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Dot11RSNAConfigGroupRekeyTime_Type.__name__ = "Unsigned32"
_Dot11RSNAConfigGroupRekeyTime_Object = MibTableColumn
dot11RSNAConfigGroupRekeyTime = _Dot11RSNAConfigGroupRekeyTime_Object(
    (1, 2, 840, 10036, 1, 9, 1, 6),
    _Dot11RSNAConfigGroupRekeyTime_Type()
)
dot11RSNAConfigGroupRekeyTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11RSNAConfigGroupRekeyTime.setStatus("current")
if mibBuilder.loadTexts:
    dot11RSNAConfigGroupRekeyTime.setUnits("seconds")


class _Dot11RSNAConfigGroupRekeyPackets_Type(Unsigned32):
    """Custom type dot11RSNAConfigGroupRekeyPackets based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Dot11RSNAConfigGroupRekeyPackets_Type.__name__ = "Unsigned32"
_Dot11RSNAConfigGroupRekeyPackets_Object = MibTableColumn
dot11RSNAConfigGroupRekeyPackets = _Dot11RSNAConfigGroupRekeyPackets_Object(
    (1, 2, 840, 10036, 1, 9, 1, 7),
    _Dot11RSNAConfigGroupRekeyPackets_Type()
)
dot11RSNAConfigGroupRekeyPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11RSNAConfigGroupRekeyPackets.setStatus("current")
if mibBuilder.loadTexts:
    dot11RSNAConfigGroupRekeyPackets.setUnits("1000 packets")
_Dot11RSNAConfigGroupRekeyStrict_Type = TruthValue
_Dot11RSNAConfigGroupRekeyStrict_Object = MibTableColumn
dot11RSNAConfigGroupRekeyStrict = _Dot11RSNAConfigGroupRekeyStrict_Object(
    (1, 2, 840, 10036, 1, 9, 1, 8),
    _Dot11RSNAConfigGroupRekeyStrict_Type()
)
dot11RSNAConfigGroupRekeyStrict.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11RSNAConfigGroupRekeyStrict.setStatus("current")


class _Dot11RSNAConfigPSKValue_Type(OctetString):
    """Custom type dot11RSNAConfigPSKValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_Dot11RSNAConfigPSKValue_Type.__name__ = "OctetString"
_Dot11RSNAConfigPSKValue_Object = MibTableColumn
dot11RSNAConfigPSKValue = _Dot11RSNAConfigPSKValue_Object(
    (1, 2, 840, 10036, 1, 9, 1, 9),
    _Dot11RSNAConfigPSKValue_Type()
)
dot11RSNAConfigPSKValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11RSNAConfigPSKValue.setStatus("current")
_Dot11RSNAConfigPSKPassPhrase_Type = DisplayString
_Dot11RSNAConfigPSKPassPhrase_Object = MibTableColumn
dot11RSNAConfigPSKPassPhrase = _Dot11RSNAConfigPSKPassPhrase_Object(
    (1, 2, 840, 10036, 1, 9, 1, 10),
    _Dot11RSNAConfigPSKPassPhrase_Type()
)
dot11RSNAConfigPSKPassPhrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11RSNAConfigPSKPassPhrase.setStatus("current")


class _Dot11RSNAConfigGroupUpdateCount_Type(Unsigned32):
    """Custom type dot11RSNAConfigGroupUpdateCount based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Dot11RSNAConfigGroupUpdateCount_Type.__name__ = "Unsigned32"
_Dot11RSNAConfigGroupUpdateCount_Object = MibTableColumn
dot11RSNAConfigGroupUpdateCount = _Dot11RSNAConfigGroupUpdateCount_Object(
    (1, 2, 840, 10036, 1, 9, 1, 13),
    _Dot11RSNAConfigGroupUpdateCount_Type()
)
dot11RSNAConfigGroupUpdateCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11RSNAConfigGroupUpdateCount.setStatus("current")


class _Dot11RSNAConfigPairwiseUpdateCount_Type(Unsigned32):
    """Custom type dot11RSNAConfigPairwiseUpdateCount based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Dot11RSNAConfigPairwiseUpdateCount_Type.__name__ = "Unsigned32"
_Dot11RSNAConfigPairwiseUpdateCount_Object = MibTableColumn
dot11RSNAConfigPairwiseUpdateCount = _Dot11RSNAConfigPairwiseUpdateCount_Object(
    (1, 2, 840, 10036, 1, 9, 1, 14),
    _Dot11RSNAConfigPairwiseUpdateCount_Type()
)
dot11RSNAConfigPairwiseUpdateCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11RSNAConfigPairwiseUpdateCount.setStatus("current")


class _Dot11RSNAConfigGroupCipherSize_Type(Unsigned32):
    """Custom type dot11RSNAConfigGroupCipherSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Dot11RSNAConfigGroupCipherSize_Type.__name__ = "Unsigned32"
_Dot11RSNAConfigGroupCipherSize_Object = MibTableColumn
dot11RSNAConfigGroupCipherSize = _Dot11RSNAConfigGroupCipherSize_Object(
    (1, 2, 840, 10036, 1, 9, 1, 15),
    _Dot11RSNAConfigGroupCipherSize_Type()
)
dot11RSNAConfigGroupCipherSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RSNAConfigGroupCipherSize.setStatus("current")


class _Dot11RSNAConfigPMKLifetime_Type(Unsigned32):
    """Custom type dot11RSNAConfigPMKLifetime based on Unsigned32"""
    defaultValue = 43200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Dot11RSNAConfigPMKLifetime_Type.__name__ = "Unsigned32"
_Dot11RSNAConfigPMKLifetime_Object = MibTableColumn
dot11RSNAConfigPMKLifetime = _Dot11RSNAConfigPMKLifetime_Object(
    (1, 2, 840, 10036, 1, 9, 1, 16),
    _Dot11RSNAConfigPMKLifetime_Type()
)
dot11RSNAConfigPMKLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11RSNAConfigPMKLifetime.setStatus("current")
if mibBuilder.loadTexts:
    dot11RSNAConfigPMKLifetime.setUnits("seconds")


class _Dot11RSNAConfigPMKReauthThreshold_Type(Unsigned32):
    """Custom type dot11RSNAConfigPMKReauthThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Dot11RSNAConfigPMKReauthThreshold_Type.__name__ = "Unsigned32"
_Dot11RSNAConfigPMKReauthThreshold_Object = MibTableColumn
dot11RSNAConfigPMKReauthThreshold = _Dot11RSNAConfigPMKReauthThreshold_Object(
    (1, 2, 840, 10036, 1, 9, 1, 17),
    _Dot11RSNAConfigPMKReauthThreshold_Type()
)
dot11RSNAConfigPMKReauthThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11RSNAConfigPMKReauthThreshold.setStatus("current")
if mibBuilder.loadTexts:
    dot11RSNAConfigPMKReauthThreshold.setUnits("percentage")
_Dot11RSNAConfigNumberOfPTKSAReplayCounters_Type = Integer32
_Dot11RSNAConfigNumberOfPTKSAReplayCounters_Object = MibTableColumn
dot11RSNAConfigNumberOfPTKSAReplayCounters = _Dot11RSNAConfigNumberOfPTKSAReplayCounters_Object(
    (1, 2, 840, 10036, 1, 9, 1, 18),
    _Dot11RSNAConfigNumberOfPTKSAReplayCounters_Type()
)
dot11RSNAConfigNumberOfPTKSAReplayCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RSNAConfigNumberOfPTKSAReplayCounters.setStatus("current")


class _Dot11RSNAConfigSATimeout_Type(Unsigned32):
    """Custom type dot11RSNAConfigSATimeout based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Dot11RSNAConfigSATimeout_Type.__name__ = "Unsigned32"
_Dot11RSNAConfigSATimeout_Object = MibTableColumn
dot11RSNAConfigSATimeout = _Dot11RSNAConfigSATimeout_Object(
    (1, 2, 840, 10036, 1, 9, 1, 19),
    _Dot11RSNAConfigSATimeout_Type()
)
dot11RSNAConfigSATimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11RSNAConfigSATimeout.setStatus("current")
if mibBuilder.loadTexts:
    dot11RSNAConfigSATimeout.setUnits("seconds")


class _Dot11RSNAAuthenticationSuiteSelected_Type(OctetString):
    """Custom type dot11RSNAAuthenticationSuiteSelected based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Dot11RSNAAuthenticationSuiteSelected_Type.__name__ = "OctetString"
_Dot11RSNAAuthenticationSuiteSelected_Object = MibTableColumn
dot11RSNAAuthenticationSuiteSelected = _Dot11RSNAAuthenticationSuiteSelected_Object(
    (1, 2, 840, 10036, 1, 9, 1, 20),
    _Dot11RSNAAuthenticationSuiteSelected_Type()
)
dot11RSNAAuthenticationSuiteSelected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RSNAAuthenticationSuiteSelected.setStatus("current")


class _Dot11RSNAPairwiseCipherSelected_Type(OctetString):
    """Custom type dot11RSNAPairwiseCipherSelected based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Dot11RSNAPairwiseCipherSelected_Type.__name__ = "OctetString"
_Dot11RSNAPairwiseCipherSelected_Object = MibTableColumn
dot11RSNAPairwiseCipherSelected = _Dot11RSNAPairwiseCipherSelected_Object(
    (1, 2, 840, 10036, 1, 9, 1, 21),
    _Dot11RSNAPairwiseCipherSelected_Type()
)
dot11RSNAPairwiseCipherSelected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RSNAPairwiseCipherSelected.setStatus("current")


class _Dot11RSNAGroupCipherSelected_Type(OctetString):
    """Custom type dot11RSNAGroupCipherSelected based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Dot11RSNAGroupCipherSelected_Type.__name__ = "OctetString"
_Dot11RSNAGroupCipherSelected_Object = MibTableColumn
dot11RSNAGroupCipherSelected = _Dot11RSNAGroupCipherSelected_Object(
    (1, 2, 840, 10036, 1, 9, 1, 22),
    _Dot11RSNAGroupCipherSelected_Type()
)
dot11RSNAGroupCipherSelected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RSNAGroupCipherSelected.setStatus("current")


class _Dot11RSNAPMKIDUsed_Type(OctetString):
    """Custom type dot11RSNAPMKIDUsed based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_Dot11RSNAPMKIDUsed_Type.__name__ = "OctetString"
_Dot11RSNAPMKIDUsed_Object = MibTableColumn
dot11RSNAPMKIDUsed = _Dot11RSNAPMKIDUsed_Object(
    (1, 2, 840, 10036, 1, 9, 1, 23),
    _Dot11RSNAPMKIDUsed_Type()
)
dot11RSNAPMKIDUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RSNAPMKIDUsed.setStatus("current")


class _Dot11RSNAAuthenticationSuiteRequested_Type(OctetString):
    """Custom type dot11RSNAAuthenticationSuiteRequested based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Dot11RSNAAuthenticationSuiteRequested_Type.__name__ = "OctetString"
_Dot11RSNAAuthenticationSuiteRequested_Object = MibTableColumn
dot11RSNAAuthenticationSuiteRequested = _Dot11RSNAAuthenticationSuiteRequested_Object(
    (1, 2, 840, 10036, 1, 9, 1, 24),
    _Dot11RSNAAuthenticationSuiteRequested_Type()
)
dot11RSNAAuthenticationSuiteRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RSNAAuthenticationSuiteRequested.setStatus("current")


class _Dot11RSNAPairwiseCipherRequested_Type(OctetString):
    """Custom type dot11RSNAPairwiseCipherRequested based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Dot11RSNAPairwiseCipherRequested_Type.__name__ = "OctetString"
_Dot11RSNAPairwiseCipherRequested_Object = MibTableColumn
dot11RSNAPairwiseCipherRequested = _Dot11RSNAPairwiseCipherRequested_Object(
    (1, 2, 840, 10036, 1, 9, 1, 25),
    _Dot11RSNAPairwiseCipherRequested_Type()
)
dot11RSNAPairwiseCipherRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RSNAPairwiseCipherRequested.setStatus("current")


class _Dot11RSNAGroupCipherRequested_Type(OctetString):
    """Custom type dot11RSNAGroupCipherRequested based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Dot11RSNAGroupCipherRequested_Type.__name__ = "OctetString"
_Dot11RSNAGroupCipherRequested_Object = MibTableColumn
dot11RSNAGroupCipherRequested = _Dot11RSNAGroupCipherRequested_Object(
    (1, 2, 840, 10036, 1, 9, 1, 26),
    _Dot11RSNAGroupCipherRequested_Type()
)
dot11RSNAGroupCipherRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RSNAGroupCipherRequested.setStatus("current")


class _Dot11RSNATKIPCounterMeasuresInvoked_Type(Unsigned32):
    """Custom type dot11RSNATKIPCounterMeasuresInvoked based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Dot11RSNATKIPCounterMeasuresInvoked_Type.__name__ = "Unsigned32"
_Dot11RSNATKIPCounterMeasuresInvoked_Object = MibTableColumn
dot11RSNATKIPCounterMeasuresInvoked = _Dot11RSNATKIPCounterMeasuresInvoked_Object(
    (1, 2, 840, 10036, 1, 9, 1, 27),
    _Dot11RSNATKIPCounterMeasuresInvoked_Type()
)
dot11RSNATKIPCounterMeasuresInvoked.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11RSNATKIPCounterMeasuresInvoked.setStatus("current")


class _Dot11RSNA4WayHandshakeFailures_Type(Unsigned32):
    """Custom type dot11RSNA4WayHandshakeFailures based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Dot11RSNA4WayHandshakeFailures_Type.__name__ = "Unsigned32"
_Dot11RSNA4WayHandshakeFailures_Object = MibTableColumn
dot11RSNA4WayHandshakeFailures = _Dot11RSNA4WayHandshakeFailures_Object(
    (1, 2, 840, 10036, 1, 9, 1, 28),
    _Dot11RSNA4WayHandshakeFailures_Type()
)
dot11RSNA4WayHandshakeFailures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11RSNA4WayHandshakeFailures.setStatus("current")
_Dot11RSNAConfigNumberOfGTKSAReplayCounters_Type = Integer32
_Dot11RSNAConfigNumberOfGTKSAReplayCounters_Object = MibTableColumn
dot11RSNAConfigNumberOfGTKSAReplayCounters = _Dot11RSNAConfigNumberOfGTKSAReplayCounters_Object(
    (1, 2, 840, 10036, 1, 9, 1, 29),
    _Dot11RSNAConfigNumberOfGTKSAReplayCounters_Type()
)
dot11RSNAConfigNumberOfGTKSAReplayCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RSNAConfigNumberOfGTKSAReplayCounters.setStatus("current")
_Dot11RSNAConfigPairwiseCiphersTable_Object = MibTable
dot11RSNAConfigPairwiseCiphersTable = _Dot11RSNAConfigPairwiseCiphersTable_Object(
    (1, 2, 840, 10036, 1, 10)
)
if mibBuilder.loadTexts:
    dot11RSNAConfigPairwiseCiphersTable.setStatus("current")
_Dot11RSNAConfigPairwiseCiphersEntry_Object = MibTableRow
dot11RSNAConfigPairwiseCiphersEntry = _Dot11RSNAConfigPairwiseCiphersEntry_Object(
    (1, 2, 840, 10036, 1, 10, 1)
)
dot11RSNAConfigPairwiseCiphersEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "IEEE802dot11-MIB", "dot11RSNAConfigPairwiseCipherIndex"),
)
if mibBuilder.loadTexts:
    dot11RSNAConfigPairwiseCiphersEntry.setStatus("current")


class _Dot11RSNAConfigPairwiseCipherIndex_Type(Unsigned32):
    """Custom type dot11RSNAConfigPairwiseCipherIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Dot11RSNAConfigPairwiseCipherIndex_Type.__name__ = "Unsigned32"
_Dot11RSNAConfigPairwiseCipherIndex_Object = MibTableColumn
dot11RSNAConfigPairwiseCipherIndex = _Dot11RSNAConfigPairwiseCipherIndex_Object(
    (1, 2, 840, 10036, 1, 10, 1, 1),
    _Dot11RSNAConfigPairwiseCipherIndex_Type()
)
dot11RSNAConfigPairwiseCipherIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RSNAConfigPairwiseCipherIndex.setStatus("current")


class _Dot11RSNAConfigPairwiseCipher_Type(OctetString):
    """Custom type dot11RSNAConfigPairwiseCipher based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Dot11RSNAConfigPairwiseCipher_Type.__name__ = "OctetString"
_Dot11RSNAConfigPairwiseCipher_Object = MibTableColumn
dot11RSNAConfigPairwiseCipher = _Dot11RSNAConfigPairwiseCipher_Object(
    (1, 2, 840, 10036, 1, 10, 1, 2),
    _Dot11RSNAConfigPairwiseCipher_Type()
)
dot11RSNAConfigPairwiseCipher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RSNAConfigPairwiseCipher.setStatus("current")
_Dot11RSNAConfigPairwiseCipherEnabled_Type = TruthValue
_Dot11RSNAConfigPairwiseCipherEnabled_Object = MibTableColumn
dot11RSNAConfigPairwiseCipherEnabled = _Dot11RSNAConfigPairwiseCipherEnabled_Object(
    (1, 2, 840, 10036, 1, 10, 1, 3),
    _Dot11RSNAConfigPairwiseCipherEnabled_Type()
)
dot11RSNAConfigPairwiseCipherEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11RSNAConfigPairwiseCipherEnabled.setStatus("current")


class _Dot11RSNAConfigPairwiseCipherSize_Type(Unsigned32):
    """Custom type dot11RSNAConfigPairwiseCipherSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Dot11RSNAConfigPairwiseCipherSize_Type.__name__ = "Unsigned32"
_Dot11RSNAConfigPairwiseCipherSize_Object = MibTableColumn
dot11RSNAConfigPairwiseCipherSize = _Dot11RSNAConfigPairwiseCipherSize_Object(
    (1, 2, 840, 10036, 1, 10, 1, 4),
    _Dot11RSNAConfigPairwiseCipherSize_Type()
)
dot11RSNAConfigPairwiseCipherSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RSNAConfigPairwiseCipherSize.setStatus("current")
_Dot11RSNAConfigAuthenticationSuitesTable_Object = MibTable
dot11RSNAConfigAuthenticationSuitesTable = _Dot11RSNAConfigAuthenticationSuitesTable_Object(
    (1, 2, 840, 10036, 1, 11)
)
if mibBuilder.loadTexts:
    dot11RSNAConfigAuthenticationSuitesTable.setStatus("current")
_Dot11RSNAConfigAuthenticationSuitesEntry_Object = MibTableRow
dot11RSNAConfigAuthenticationSuitesEntry = _Dot11RSNAConfigAuthenticationSuitesEntry_Object(
    (1, 2, 840, 10036, 1, 11, 1)
)
dot11RSNAConfigAuthenticationSuitesEntry.setIndexNames(
    (0, "IEEE802dot11-MIB", "dot11RSNAConfigAuthenticationSuiteIndex"),
)
if mibBuilder.loadTexts:
    dot11RSNAConfigAuthenticationSuitesEntry.setStatus("current")


class _Dot11RSNAConfigAuthenticationSuiteIndex_Type(Unsigned32):
    """Custom type dot11RSNAConfigAuthenticationSuiteIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Dot11RSNAConfigAuthenticationSuiteIndex_Type.__name__ = "Unsigned32"
_Dot11RSNAConfigAuthenticationSuiteIndex_Object = MibTableColumn
dot11RSNAConfigAuthenticationSuiteIndex = _Dot11RSNAConfigAuthenticationSuiteIndex_Object(
    (1, 2, 840, 10036, 1, 11, 1, 1),
    _Dot11RSNAConfigAuthenticationSuiteIndex_Type()
)
dot11RSNAConfigAuthenticationSuiteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RSNAConfigAuthenticationSuiteIndex.setStatus("current")


class _Dot11RSNAConfigAuthenticationSuite_Type(OctetString):
    """Custom type dot11RSNAConfigAuthenticationSuite based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Dot11RSNAConfigAuthenticationSuite_Type.__name__ = "OctetString"
_Dot11RSNAConfigAuthenticationSuite_Object = MibTableColumn
dot11RSNAConfigAuthenticationSuite = _Dot11RSNAConfigAuthenticationSuite_Object(
    (1, 2, 840, 10036, 1, 11, 1, 2),
    _Dot11RSNAConfigAuthenticationSuite_Type()
)
dot11RSNAConfigAuthenticationSuite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RSNAConfigAuthenticationSuite.setStatus("current")
_Dot11RSNAConfigAuthenticationSuiteEnabled_Type = TruthValue
_Dot11RSNAConfigAuthenticationSuiteEnabled_Object = MibTableColumn
dot11RSNAConfigAuthenticationSuiteEnabled = _Dot11RSNAConfigAuthenticationSuiteEnabled_Object(
    (1, 2, 840, 10036, 1, 11, 1, 3),
    _Dot11RSNAConfigAuthenticationSuiteEnabled_Type()
)
dot11RSNAConfigAuthenticationSuiteEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11RSNAConfigAuthenticationSuiteEnabled.setStatus("current")
_Dot11RSNAStatsTable_Object = MibTable
dot11RSNAStatsTable = _Dot11RSNAStatsTable_Object(
    (1, 2, 840, 10036, 1, 12)
)
if mibBuilder.loadTexts:
    dot11RSNAStatsTable.setStatus("current")
_Dot11RSNAStatsEntry_Object = MibTableRow
dot11RSNAStatsEntry = _Dot11RSNAStatsEntry_Object(
    (1, 2, 840, 10036, 1, 12, 1)
)
dot11RSNAStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "IEEE802dot11-MIB", "dot11RSNAStatsIndex"),
)
if mibBuilder.loadTexts:
    dot11RSNAStatsEntry.setStatus("current")


class _Dot11RSNAStatsIndex_Type(Unsigned32):
    """Custom type dot11RSNAStatsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Dot11RSNAStatsIndex_Type.__name__ = "Unsigned32"
_Dot11RSNAStatsIndex_Object = MibTableColumn
dot11RSNAStatsIndex = _Dot11RSNAStatsIndex_Object(
    (1, 2, 840, 10036, 1, 12, 1, 1),
    _Dot11RSNAStatsIndex_Type()
)
dot11RSNAStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RSNAStatsIndex.setStatus("current")
_Dot11RSNAStatsSTAAddress_Type = MacAddress
_Dot11RSNAStatsSTAAddress_Object = MibTableColumn
dot11RSNAStatsSTAAddress = _Dot11RSNAStatsSTAAddress_Object(
    (1, 2, 840, 10036, 1, 12, 1, 2),
    _Dot11RSNAStatsSTAAddress_Type()
)
dot11RSNAStatsSTAAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RSNAStatsSTAAddress.setStatus("current")


class _Dot11RSNAStatsVersion_Type(Unsigned32):
    """Custom type dot11RSNAStatsVersion based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Dot11RSNAStatsVersion_Type.__name__ = "Unsigned32"
_Dot11RSNAStatsVersion_Object = MibTableColumn
dot11RSNAStatsVersion = _Dot11RSNAStatsVersion_Object(
    (1, 2, 840, 10036, 1, 12, 1, 3),
    _Dot11RSNAStatsVersion_Type()
)
dot11RSNAStatsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RSNAStatsVersion.setStatus("current")


class _Dot11RSNAStatsSelectedPairwiseCipher_Type(OctetString):
    """Custom type dot11RSNAStatsSelectedPairwiseCipher based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Dot11RSNAStatsSelectedPairwiseCipher_Type.__name__ = "OctetString"
_Dot11RSNAStatsSelectedPairwiseCipher_Object = MibTableColumn
dot11RSNAStatsSelectedPairwiseCipher = _Dot11RSNAStatsSelectedPairwiseCipher_Object(
    (1, 2, 840, 10036, 1, 12, 1, 4),
    _Dot11RSNAStatsSelectedPairwiseCipher_Type()
)
dot11RSNAStatsSelectedPairwiseCipher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RSNAStatsSelectedPairwiseCipher.setStatus("current")
_Dot11RSNAStatsTKIPICVErrors_Type = Counter32
_Dot11RSNAStatsTKIPICVErrors_Object = MibTableColumn
dot11RSNAStatsTKIPICVErrors = _Dot11RSNAStatsTKIPICVErrors_Object(
    (1, 2, 840, 10036, 1, 12, 1, 5),
    _Dot11RSNAStatsTKIPICVErrors_Type()
)
dot11RSNAStatsTKIPICVErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RSNAStatsTKIPICVErrors.setStatus("current")
_Dot11RSNAStatsTKIPLocalMICFailures_Type = Counter32
_Dot11RSNAStatsTKIPLocalMICFailures_Object = MibTableColumn
dot11RSNAStatsTKIPLocalMICFailures = _Dot11RSNAStatsTKIPLocalMICFailures_Object(
    (1, 2, 840, 10036, 1, 12, 1, 6),
    _Dot11RSNAStatsTKIPLocalMICFailures_Type()
)
dot11RSNAStatsTKIPLocalMICFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RSNAStatsTKIPLocalMICFailures.setStatus("current")
_Dot11RSNAStatsTKIPRemoteMICFailures_Type = Counter32
_Dot11RSNAStatsTKIPRemoteMICFailures_Object = MibTableColumn
dot11RSNAStatsTKIPRemoteMICFailures = _Dot11RSNAStatsTKIPRemoteMICFailures_Object(
    (1, 2, 840, 10036, 1, 12, 1, 7),
    _Dot11RSNAStatsTKIPRemoteMICFailures_Type()
)
dot11RSNAStatsTKIPRemoteMICFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RSNAStatsTKIPRemoteMICFailures.setStatus("current")
_Dot11RSNAStatsCCMPReplays_Type = Counter32
_Dot11RSNAStatsCCMPReplays_Object = MibTableColumn
dot11RSNAStatsCCMPReplays = _Dot11RSNAStatsCCMPReplays_Object(
    (1, 2, 840, 10036, 1, 12, 1, 8),
    _Dot11RSNAStatsCCMPReplays_Type()
)
dot11RSNAStatsCCMPReplays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RSNAStatsCCMPReplays.setStatus("current")
_Dot11RSNAStatsCCMPDecryptErrors_Type = Counter32
_Dot11RSNAStatsCCMPDecryptErrors_Object = MibTableColumn
dot11RSNAStatsCCMPDecryptErrors = _Dot11RSNAStatsCCMPDecryptErrors_Object(
    (1, 2, 840, 10036, 1, 12, 1, 9),
    _Dot11RSNAStatsCCMPDecryptErrors_Type()
)
dot11RSNAStatsCCMPDecryptErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RSNAStatsCCMPDecryptErrors.setStatus("current")
_Dot11RSNAStatsTKIPReplays_Type = Counter32
_Dot11RSNAStatsTKIPReplays_Object = MibTableColumn
dot11RSNAStatsTKIPReplays = _Dot11RSNAStatsTKIPReplays_Object(
    (1, 2, 840, 10036, 1, 12, 1, 10),
    _Dot11RSNAStatsTKIPReplays_Type()
)
dot11RSNAStatsTKIPReplays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RSNAStatsTKIPReplays.setStatus("current")
_Dot11HTStationConfigTable_Object = MibTable
dot11HTStationConfigTable = _Dot11HTStationConfigTable_Object(
    (1, 2, 840, 10036, 1, 16)
)
if mibBuilder.loadTexts:
    dot11HTStationConfigTable.setStatus("current")
_Dot11HTStationConfigEntry_Object = MibTableRow
dot11HTStationConfigEntry = _Dot11HTStationConfigEntry_Object(
    (1, 2, 840, 10036, 1, 16, 1)
)
dot11HTStationConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11HTStationConfigEntry.setStatus("current")


class _Dot11HTOperationalMCSSet_Type(OctetString):
    """Custom type dot11HTOperationalMCSSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_Dot11HTOperationalMCSSet_Type.__name__ = "OctetString"
_Dot11HTOperationalMCSSet_Object = MibTableColumn
dot11HTOperationalMCSSet = _Dot11HTOperationalMCSSet_Object(
    (1, 2, 840, 10036, 1, 16, 1, 1),
    _Dot11HTOperationalMCSSet_Type()
)
dot11HTOperationalMCSSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11HTOperationalMCSSet.setStatus("current")


class _Dot11MIMOPowerSave_Type(Integer32):
    """Custom type dot11MIMOPowerSave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("mimo", 3),
          ("static", 1))
    )


_Dot11MIMOPowerSave_Type.__name__ = "Integer32"
_Dot11MIMOPowerSave_Object = MibTableColumn
dot11MIMOPowerSave = _Dot11MIMOPowerSave_Object(
    (1, 2, 840, 10036, 1, 16, 1, 2),
    _Dot11MIMOPowerSave_Type()
)
dot11MIMOPowerSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11MIMOPowerSave.setStatus("current")


class _Dot11NDelayedBlockAckOptionImplemented_Type(TruthValue):
    """Custom type dot11NDelayedBlockAckOptionImplemented based on TruthValue"""


_Dot11NDelayedBlockAckOptionImplemented_Object = MibTableColumn
dot11NDelayedBlockAckOptionImplemented = _Dot11NDelayedBlockAckOptionImplemented_Object(
    (1, 2, 840, 10036, 1, 16, 1, 3),
    _Dot11NDelayedBlockAckOptionImplemented_Type()
)
dot11NDelayedBlockAckOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11NDelayedBlockAckOptionImplemented.setStatus("current")


class _Dot11MaxAMSDULength_Type(Integer32):
    """Custom type dot11MaxAMSDULength based on Integer32"""
    defaultValue = 3839

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3839, 7935),
    )


_Dot11MaxAMSDULength_Type.__name__ = "Integer32"
_Dot11MaxAMSDULength_Object = MibTableColumn
dot11MaxAMSDULength = _Dot11MaxAMSDULength_Object(
    (1, 2, 840, 10036, 1, 16, 1, 4),
    _Dot11MaxAMSDULength_Type()
)
dot11MaxAMSDULength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11MaxAMSDULength.setStatus("current")


class _Dot11PSMPOptionImplemented_Type(TruthValue):
    """Custom type dot11PSMPOptionImplemented based on TruthValue"""


_Dot11PSMPOptionImplemented_Object = MibTableColumn
dot11PSMPOptionImplemented = _Dot11PSMPOptionImplemented_Object(
    (1, 2, 840, 10036, 1, 16, 1, 5),
    _Dot11PSMPOptionImplemented_Type()
)
dot11PSMPOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11PSMPOptionImplemented.setStatus("current")


class _Dot11STBCControlFrameOptionImplemented_Type(TruthValue):
    """Custom type dot11STBCControlFrameOptionImplemented based on TruthValue"""


_Dot11STBCControlFrameOptionImplemented_Object = MibTableColumn
dot11STBCControlFrameOptionImplemented = _Dot11STBCControlFrameOptionImplemented_Object(
    (1, 2, 840, 10036, 1, 16, 1, 6),
    _Dot11STBCControlFrameOptionImplemented_Type()
)
dot11STBCControlFrameOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11STBCControlFrameOptionImplemented.setStatus("current")


class _Dot11LsigTxopProtectionOptionImplemented_Type(TruthValue):
    """Custom type dot11LsigTxopProtectionOptionImplemented based on TruthValue"""


_Dot11LsigTxopProtectionOptionImplemented_Object = MibTableColumn
dot11LsigTxopProtectionOptionImplemented = _Dot11LsigTxopProtectionOptionImplemented_Object(
    (1, 2, 840, 10036, 1, 16, 1, 7),
    _Dot11LsigTxopProtectionOptionImplemented_Type()
)
dot11LsigTxopProtectionOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11LsigTxopProtectionOptionImplemented.setStatus("current")


class _Dot11MaxRxAMPDUFactor_Type(Integer32):
    """Custom type dot11MaxRxAMPDUFactor based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Dot11MaxRxAMPDUFactor_Type.__name__ = "Integer32"
_Dot11MaxRxAMPDUFactor_Object = MibTableColumn
dot11MaxRxAMPDUFactor = _Dot11MaxRxAMPDUFactor_Object(
    (1, 2, 840, 10036, 1, 16, 1, 8),
    _Dot11MaxRxAMPDUFactor_Type()
)
dot11MaxRxAMPDUFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11MaxRxAMPDUFactor.setStatus("current")


class _Dot11MinimumMPDUStartSpacing_Type(Integer32):
    """Custom type dot11MinimumMPDUStartSpacing based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dot11MinimumMPDUStartSpacing_Type.__name__ = "Integer32"
_Dot11MinimumMPDUStartSpacing_Object = MibTableColumn
dot11MinimumMPDUStartSpacing = _Dot11MinimumMPDUStartSpacing_Object(
    (1, 2, 840, 10036, 1, 16, 1, 9),
    _Dot11MinimumMPDUStartSpacing_Type()
)
dot11MinimumMPDUStartSpacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11MinimumMPDUStartSpacing.setStatus("current")


class _Dot11PCOOptionImplemented_Type(TruthValue):
    """Custom type dot11PCOOptionImplemented based on TruthValue"""


_Dot11PCOOptionImplemented_Object = MibTableColumn
dot11PCOOptionImplemented = _Dot11PCOOptionImplemented_Object(
    (1, 2, 840, 10036, 1, 16, 1, 10),
    _Dot11PCOOptionImplemented_Type()
)
dot11PCOOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11PCOOptionImplemented.setStatus("current")


class _Dot11TransitionTime_Type(Integer32):
    """Custom type dot11TransitionTime based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Dot11TransitionTime_Type.__name__ = "Integer32"
_Dot11TransitionTime_Object = MibTableColumn
dot11TransitionTime = _Dot11TransitionTime_Object(
    (1, 2, 840, 10036, 1, 16, 1, 11),
    _Dot11TransitionTime_Type()
)
dot11TransitionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TransitionTime.setStatus("current")


class _Dot11MCSFeedbackOptionImplemented_Type(Integer32):
    """Custom type dot11MCSFeedbackOptionImplemented based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("none", 0),
          ("unsolicited", 2))
    )


_Dot11MCSFeedbackOptionImplemented_Type.__name__ = "Integer32"
_Dot11MCSFeedbackOptionImplemented_Object = MibTableColumn
dot11MCSFeedbackOptionImplemented = _Dot11MCSFeedbackOptionImplemented_Object(
    (1, 2, 840, 10036, 1, 16, 1, 12),
    _Dot11MCSFeedbackOptionImplemented_Type()
)
dot11MCSFeedbackOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11MCSFeedbackOptionImplemented.setStatus("current")


class _Dot11HTControlFieldSupported_Type(TruthValue):
    """Custom type dot11HTControlFieldSupported based on TruthValue"""


_Dot11HTControlFieldSupported_Object = MibTableColumn
dot11HTControlFieldSupported = _Dot11HTControlFieldSupported_Object(
    (1, 2, 840, 10036, 1, 16, 1, 13),
    _Dot11HTControlFieldSupported_Type()
)
dot11HTControlFieldSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11HTControlFieldSupported.setStatus("current")


class _Dot11RDResponderOptionImplemented_Type(TruthValue):
    """Custom type dot11RDResponderOptionImplemented based on TruthValue"""


_Dot11RDResponderOptionImplemented_Object = MibTableColumn
dot11RDResponderOptionImplemented = _Dot11RDResponderOptionImplemented_Object(
    (1, 2, 840, 10036, 1, 16, 1, 14),
    _Dot11RDResponderOptionImplemented_Type()
)
dot11RDResponderOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RDResponderOptionImplemented.setStatus("current")
_Dot11mac_ObjectIdentity = ObjectIdentity
dot11mac = _Dot11mac_ObjectIdentity(
    (1, 2, 840, 10036, 2)
)
_Dot11OperationTable_Object = MibTable
dot11OperationTable = _Dot11OperationTable_Object(
    (1, 2, 840, 10036, 2, 1)
)
if mibBuilder.loadTexts:
    dot11OperationTable.setStatus("current")
_Dot11OperationEntry_Object = MibTableRow
dot11OperationEntry = _Dot11OperationEntry_Object(
    (1, 2, 840, 10036, 2, 1, 1)
)
dot11OperationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11OperationEntry.setStatus("current")
_Dot11MACAddress_Type = MacAddress
_Dot11MACAddress_Object = MibTableColumn
dot11MACAddress = _Dot11MACAddress_Object(
    (1, 2, 840, 10036, 2, 1, 1, 1),
    _Dot11MACAddress_Type()
)
dot11MACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11MACAddress.setStatus("current")


class _Dot11RTSThreshold_Type(Integer32):
    """Custom type dot11RTSThreshold based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot11RTSThreshold_Type.__name__ = "Integer32"
_Dot11RTSThreshold_Object = MibTableColumn
dot11RTSThreshold = _Dot11RTSThreshold_Object(
    (1, 2, 840, 10036, 2, 1, 1, 2),
    _Dot11RTSThreshold_Type()
)
dot11RTSThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11RTSThreshold.setStatus("current")


class _Dot11ShortRetryLimit_Type(Integer32):
    """Custom type dot11ShortRetryLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Dot11ShortRetryLimit_Type.__name__ = "Integer32"
_Dot11ShortRetryLimit_Object = MibTableColumn
dot11ShortRetryLimit = _Dot11ShortRetryLimit_Object(
    (1, 2, 840, 10036, 2, 1, 1, 3),
    _Dot11ShortRetryLimit_Type()
)
dot11ShortRetryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ShortRetryLimit.setStatus("current")


class _Dot11LongRetryLimit_Type(Integer32):
    """Custom type dot11LongRetryLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Dot11LongRetryLimit_Type.__name__ = "Integer32"
_Dot11LongRetryLimit_Object = MibTableColumn
dot11LongRetryLimit = _Dot11LongRetryLimit_Object(
    (1, 2, 840, 10036, 2, 1, 1, 4),
    _Dot11LongRetryLimit_Type()
)
dot11LongRetryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11LongRetryLimit.setStatus("current")


class _Dot11FragmentationThreshold_Type(Integer32):
    """Custom type dot11FragmentationThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 8000),
    )


_Dot11FragmentationThreshold_Type.__name__ = "Integer32"
_Dot11FragmentationThreshold_Object = MibTableColumn
dot11FragmentationThreshold = _Dot11FragmentationThreshold_Object(
    (1, 2, 840, 10036, 2, 1, 1, 5),
    _Dot11FragmentationThreshold_Type()
)
dot11FragmentationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11FragmentationThreshold.setStatus("current")


class _Dot11MaxTransmitMSDULifetime_Type(Unsigned32):
    """Custom type dot11MaxTransmitMSDULifetime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Dot11MaxTransmitMSDULifetime_Type.__name__ = "Unsigned32"
_Dot11MaxTransmitMSDULifetime_Object = MibTableColumn
dot11MaxTransmitMSDULifetime = _Dot11MaxTransmitMSDULifetime_Object(
    (1, 2, 840, 10036, 2, 1, 1, 6),
    _Dot11MaxTransmitMSDULifetime_Type()
)
dot11MaxTransmitMSDULifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MaxTransmitMSDULifetime.setStatus("current")


class _Dot11MaxReceiveLifetime_Type(Unsigned32):
    """Custom type dot11MaxReceiveLifetime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Dot11MaxReceiveLifetime_Type.__name__ = "Unsigned32"
_Dot11MaxReceiveLifetime_Object = MibTableColumn
dot11MaxReceiveLifetime = _Dot11MaxReceiveLifetime_Object(
    (1, 2, 840, 10036, 2, 1, 1, 7),
    _Dot11MaxReceiveLifetime_Type()
)
dot11MaxReceiveLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MaxReceiveLifetime.setStatus("current")


class _Dot11ManufacturerID_Type(DisplayString):
    """Custom type dot11ManufacturerID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Dot11ManufacturerID_Type.__name__ = "DisplayString"
_Dot11ManufacturerID_Object = MibTableColumn
dot11ManufacturerID = _Dot11ManufacturerID_Object(
    (1, 2, 840, 10036, 2, 1, 1, 8),
    _Dot11ManufacturerID_Type()
)
dot11ManufacturerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ManufacturerID.setStatus("current")


class _Dot11ProductID_Type(DisplayString):
    """Custom type dot11ProductID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Dot11ProductID_Type.__name__ = "DisplayString"
_Dot11ProductID_Object = MibTableColumn
dot11ProductID = _Dot11ProductID_Object(
    (1, 2, 840, 10036, 2, 1, 1, 9),
    _Dot11ProductID_Type()
)
dot11ProductID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ProductID.setStatus("current")
_Dot11CAPLimit_Type = Integer32
_Dot11CAPLimit_Object = MibTableColumn
dot11CAPLimit = _Dot11CAPLimit_Object(
    (1, 2, 840, 10036, 2, 1, 1, 10),
    _Dot11CAPLimit_Type()
)
dot11CAPLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11CAPLimit.setStatus("current")


class _Dot11HCCWmin_Type(Integer32):
    """Custom type dot11HCCWmin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Dot11HCCWmin_Type.__name__ = "Integer32"
_Dot11HCCWmin_Object = MibTableColumn
dot11HCCWmin = _Dot11HCCWmin_Object(
    (1, 2, 840, 10036, 2, 1, 1, 11),
    _Dot11HCCWmin_Type()
)
dot11HCCWmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11HCCWmin.setStatus("current")


class _Dot11HCCWmax_Type(Integer32):
    """Custom type dot11HCCWmax based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Dot11HCCWmax_Type.__name__ = "Integer32"
_Dot11HCCWmax_Object = MibTableColumn
dot11HCCWmax = _Dot11HCCWmax_Object(
    (1, 2, 840, 10036, 2, 1, 1, 12),
    _Dot11HCCWmax_Type()
)
dot11HCCWmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11HCCWmax.setStatus("current")


class _Dot11HCCAIFSN_Type(Integer32):
    """Custom type dot11HCCAIFSN based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Dot11HCCAIFSN_Type.__name__ = "Integer32"
_Dot11HCCAIFSN_Object = MibTableColumn
dot11HCCAIFSN = _Dot11HCCAIFSN_Object(
    (1, 2, 840, 10036, 2, 1, 1, 13),
    _Dot11HCCAIFSN_Type()
)
dot11HCCAIFSN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11HCCAIFSN.setStatus("current")


class _Dot11ADDBAResponseTimeout_Type(Integer32):
    """Custom type dot11ADDBAResponseTimeout based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot11ADDBAResponseTimeout_Type.__name__ = "Integer32"
_Dot11ADDBAResponseTimeout_Object = MibTableColumn
dot11ADDBAResponseTimeout = _Dot11ADDBAResponseTimeout_Object(
    (1, 2, 840, 10036, 2, 1, 1, 14),
    _Dot11ADDBAResponseTimeout_Type()
)
dot11ADDBAResponseTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ADDBAResponseTimeout.setStatus("current")


class _Dot11ADDTSResponseTimeout_Type(Integer32):
    """Custom type dot11ADDTSResponseTimeout based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot11ADDTSResponseTimeout_Type.__name__ = "Integer32"
_Dot11ADDTSResponseTimeout_Object = MibTableColumn
dot11ADDTSResponseTimeout = _Dot11ADDTSResponseTimeout_Object(
    (1, 2, 840, 10036, 2, 1, 1, 15),
    _Dot11ADDTSResponseTimeout_Type()
)
dot11ADDTSResponseTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ADDTSResponseTimeout.setStatus("current")


class _Dot11ChannelUtilizationBeaconInterval_Type(Integer32):
    """Custom type dot11ChannelUtilizationBeaconInterval based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Dot11ChannelUtilizationBeaconInterval_Type.__name__ = "Integer32"
_Dot11ChannelUtilizationBeaconInterval_Object = MibTableColumn
dot11ChannelUtilizationBeaconInterval = _Dot11ChannelUtilizationBeaconInterval_Object(
    (1, 2, 840, 10036, 2, 1, 1, 16),
    _Dot11ChannelUtilizationBeaconInterval_Type()
)
dot11ChannelUtilizationBeaconInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ChannelUtilizationBeaconInterval.setStatus("current")


class _Dot11ScheduleTimeout_Type(Integer32):
    """Custom type dot11ScheduleTimeout based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Dot11ScheduleTimeout_Type.__name__ = "Integer32"
_Dot11ScheduleTimeout_Object = MibTableColumn
dot11ScheduleTimeout = _Dot11ScheduleTimeout_Object(
    (1, 2, 840, 10036, 2, 1, 1, 17),
    _Dot11ScheduleTimeout_Type()
)
dot11ScheduleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ScheduleTimeout.setStatus("current")


class _Dot11DLSResponseTimeout_Type(Integer32):
    """Custom type dot11DLSResponseTimeout based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot11DLSResponseTimeout_Type.__name__ = "Integer32"
_Dot11DLSResponseTimeout_Object = MibTableColumn
dot11DLSResponseTimeout = _Dot11DLSResponseTimeout_Object(
    (1, 2, 840, 10036, 2, 1, 1, 18),
    _Dot11DLSResponseTimeout_Type()
)
dot11DLSResponseTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11DLSResponseTimeout.setStatus("current")


class _Dot11QAPMissingAckRetryLimit_Type(Integer32):
    """Custom type dot11QAPMissingAckRetryLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Dot11QAPMissingAckRetryLimit_Type.__name__ = "Integer32"
_Dot11QAPMissingAckRetryLimit_Object = MibTableColumn
dot11QAPMissingAckRetryLimit = _Dot11QAPMissingAckRetryLimit_Object(
    (1, 2, 840, 10036, 2, 1, 1, 19),
    _Dot11QAPMissingAckRetryLimit_Type()
)
dot11QAPMissingAckRetryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11QAPMissingAckRetryLimit.setStatus("current")


class _Dot11EDCAAveragingPeriod_Type(Integer32):
    """Custom type dot11EDCAAveragingPeriod based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Dot11EDCAAveragingPeriod_Type.__name__ = "Integer32"
_Dot11EDCAAveragingPeriod_Object = MibTableColumn
dot11EDCAAveragingPeriod = _Dot11EDCAAveragingPeriod_Object(
    (1, 2, 840, 10036, 2, 1, 1, 20),
    _Dot11EDCAAveragingPeriod_Type()
)
dot11EDCAAveragingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11EDCAAveragingPeriod.setStatus("current")


class _Dot11HTOperatingMode_Type(Integer32):
    """Custom type dot11HTOperatingMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("htPure", 0),
          ("mandatoryAllProtection", 3),
          ("mandatoryFortyProtection", 2),
          ("optionalProtection", 1))
    )


_Dot11HTOperatingMode_Type.__name__ = "Integer32"
_Dot11HTOperatingMode_Object = MibTableColumn
dot11HTOperatingMode = _Dot11HTOperatingMode_Object(
    (1, 2, 840, 10036, 2, 1, 1, 21),
    _Dot11HTOperatingMode_Type()
)
dot11HTOperatingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11HTOperatingMode.setStatus("current")


class _Dot11RIFSMode_Type(TruthValue):
    """Custom type dot11RIFSMode based on TruthValue"""


_Dot11RIFSMode_Object = MibTableColumn
dot11RIFSMode = _Dot11RIFSMode_Object(
    (1, 2, 840, 10036, 2, 1, 1, 22),
    _Dot11RIFSMode_Type()
)
dot11RIFSMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11RIFSMode.setStatus("current")


class _Dot11PSMPControlledAccess_Type(TruthValue):
    """Custom type dot11PSMPControlledAccess based on TruthValue"""


_Dot11PSMPControlledAccess_Object = MibTableColumn
dot11PSMPControlledAccess = _Dot11PSMPControlledAccess_Object(
    (1, 2, 840, 10036, 2, 1, 1, 23),
    _Dot11PSMPControlledAccess_Type()
)
dot11PSMPControlledAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11PSMPControlledAccess.setStatus("current")


class _Dot11ServiceIntervalGranularity_Type(Integer32):
    """Custom type dot11ServiceIntervalGranularity based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dot11ServiceIntervalGranularity_Type.__name__ = "Integer32"
_Dot11ServiceIntervalGranularity_Object = MibTableColumn
dot11ServiceIntervalGranularity = _Dot11ServiceIntervalGranularity_Object(
    (1, 2, 840, 10036, 2, 1, 1, 24),
    _Dot11ServiceIntervalGranularity_Type()
)
dot11ServiceIntervalGranularity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ServiceIntervalGranularity.setStatus("current")


class _Dot11DualCTSProtection_Type(TruthValue):
    """Custom type dot11DualCTSProtection based on TruthValue"""


_Dot11DualCTSProtection_Object = MibTableColumn
dot11DualCTSProtection = _Dot11DualCTSProtection_Object(
    (1, 2, 840, 10036, 2, 1, 1, 25),
    _Dot11DualCTSProtection_Type()
)
dot11DualCTSProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11DualCTSProtection.setStatus("current")


class _Dot11LSigTxopFullProtectionEnabled_Type(TruthValue):
    """Custom type dot11LSigTxopFullProtectionEnabled based on TruthValue"""


_Dot11LSigTxopFullProtectionEnabled_Object = MibTableColumn
dot11LSigTxopFullProtectionEnabled = _Dot11LSigTxopFullProtectionEnabled_Object(
    (1, 2, 840, 10036, 2, 1, 1, 26),
    _Dot11LSigTxopFullProtectionEnabled_Type()
)
dot11LSigTxopFullProtectionEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11LSigTxopFullProtectionEnabled.setStatus("current")


class _Dot11NonGFEntitiesPresent_Type(TruthValue):
    """Custom type dot11NonGFEntitiesPresent based on TruthValue"""


_Dot11NonGFEntitiesPresent_Object = MibTableColumn
dot11NonGFEntitiesPresent = _Dot11NonGFEntitiesPresent_Object(
    (1, 2, 840, 10036, 2, 1, 1, 27),
    _Dot11NonGFEntitiesPresent_Type()
)
dot11NonGFEntitiesPresent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11NonGFEntitiesPresent.setStatus("current")


class _Dot11PCOActivated_Type(TruthValue):
    """Custom type dot11PCOActivated based on TruthValue"""


_Dot11PCOActivated_Object = MibTableColumn
dot11PCOActivated = _Dot11PCOActivated_Object(
    (1, 2, 840, 10036, 2, 1, 1, 28),
    _Dot11PCOActivated_Type()
)
dot11PCOActivated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11PCOActivated.setStatus("current")


class _Dot11PCO40MaxDuration_Type(Integer32):
    """Custom type dot11PCO40MaxDuration based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot11PCO40MaxDuration_Type.__name__ = "Integer32"
_Dot11PCO40MaxDuration_Object = MibTableColumn
dot11PCO40MaxDuration = _Dot11PCO40MaxDuration_Object(
    (1, 2, 840, 10036, 2, 1, 1, 29),
    _Dot11PCO40MaxDuration_Type()
)
dot11PCO40MaxDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11PCO40MaxDuration.setStatus("current")


class _Dot11PCO20MaxDuration_Type(Integer32):
    """Custom type dot11PCO20MaxDuration based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot11PCO20MaxDuration_Type.__name__ = "Integer32"
_Dot11PCO20MaxDuration_Object = MibTableColumn
dot11PCO20MaxDuration = _Dot11PCO20MaxDuration_Object(
    (1, 2, 840, 10036, 2, 1, 1, 30),
    _Dot11PCO20MaxDuration_Type()
)
dot11PCO20MaxDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11PCO20MaxDuration.setStatus("current")


class _Dot11PCO40MinDuration_Type(Integer32):
    """Custom type dot11PCO40MinDuration based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot11PCO40MinDuration_Type.__name__ = "Integer32"
_Dot11PCO40MinDuration_Object = MibTableColumn
dot11PCO40MinDuration = _Dot11PCO40MinDuration_Object(
    (1, 2, 840, 10036, 2, 1, 1, 31),
    _Dot11PCO40MinDuration_Type()
)
dot11PCO40MinDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11PCO40MinDuration.setStatus("current")


class _Dot11PCO20MinDuration_Type(Integer32):
    """Custom type dot11PCO20MinDuration based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot11PCO20MinDuration_Type.__name__ = "Integer32"
_Dot11PCO20MinDuration_Object = MibTableColumn
dot11PCO20MinDuration = _Dot11PCO20MinDuration_Object(
    (1, 2, 840, 10036, 2, 1, 1, 32),
    _Dot11PCO20MinDuration_Type()
)
dot11PCO20MinDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11PCO20MinDuration.setStatus("current")
_Dot11CountersTable_Object = MibTable
dot11CountersTable = _Dot11CountersTable_Object(
    (1, 2, 840, 10036, 2, 2)
)
if mibBuilder.loadTexts:
    dot11CountersTable.setStatus("current")
_Dot11CountersEntry_Object = MibTableRow
dot11CountersEntry = _Dot11CountersEntry_Object(
    (1, 2, 840, 10036, 2, 2, 1)
)
dot11CountersEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11CountersEntry.setStatus("current")
_Dot11TransmittedFragmentCount_Type = Counter32
_Dot11TransmittedFragmentCount_Object = MibTableColumn
dot11TransmittedFragmentCount = _Dot11TransmittedFragmentCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 1),
    _Dot11TransmittedFragmentCount_Type()
)
dot11TransmittedFragmentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TransmittedFragmentCount.setStatus("current")
_Dot11MulticastTransmittedFrameCount_Type = Counter32
_Dot11MulticastTransmittedFrameCount_Object = MibTableColumn
dot11MulticastTransmittedFrameCount = _Dot11MulticastTransmittedFrameCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 2),
    _Dot11MulticastTransmittedFrameCount_Type()
)
dot11MulticastTransmittedFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11MulticastTransmittedFrameCount.setStatus("current")
_Dot11FailedCount_Type = Counter32
_Dot11FailedCount_Object = MibTableColumn
dot11FailedCount = _Dot11FailedCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 3),
    _Dot11FailedCount_Type()
)
dot11FailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11FailedCount.setStatus("current")
_Dot11RetryCount_Type = Counter32
_Dot11RetryCount_Object = MibTableColumn
dot11RetryCount = _Dot11RetryCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 4),
    _Dot11RetryCount_Type()
)
dot11RetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RetryCount.setStatus("current")
_Dot11MultipleRetryCount_Type = Counter32
_Dot11MultipleRetryCount_Object = MibTableColumn
dot11MultipleRetryCount = _Dot11MultipleRetryCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 5),
    _Dot11MultipleRetryCount_Type()
)
dot11MultipleRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11MultipleRetryCount.setStatus("current")
_Dot11FrameDuplicateCount_Type = Counter32
_Dot11FrameDuplicateCount_Object = MibTableColumn
dot11FrameDuplicateCount = _Dot11FrameDuplicateCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 6),
    _Dot11FrameDuplicateCount_Type()
)
dot11FrameDuplicateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11FrameDuplicateCount.setStatus("current")
_Dot11RTSSuccessCount_Type = Counter32
_Dot11RTSSuccessCount_Object = MibTableColumn
dot11RTSSuccessCount = _Dot11RTSSuccessCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 7),
    _Dot11RTSSuccessCount_Type()
)
dot11RTSSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RTSSuccessCount.setStatus("current")
_Dot11RTSFailureCount_Type = Counter32
_Dot11RTSFailureCount_Object = MibTableColumn
dot11RTSFailureCount = _Dot11RTSFailureCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 8),
    _Dot11RTSFailureCount_Type()
)
dot11RTSFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RTSFailureCount.setStatus("current")
_Dot11ACKFailureCount_Type = Counter32
_Dot11ACKFailureCount_Object = MibTableColumn
dot11ACKFailureCount = _Dot11ACKFailureCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 9),
    _Dot11ACKFailureCount_Type()
)
dot11ACKFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ACKFailureCount.setStatus("current")
_Dot11ReceivedFragmentCount_Type = Counter32
_Dot11ReceivedFragmentCount_Object = MibTableColumn
dot11ReceivedFragmentCount = _Dot11ReceivedFragmentCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 10),
    _Dot11ReceivedFragmentCount_Type()
)
dot11ReceivedFragmentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ReceivedFragmentCount.setStatus("current")
_Dot11MulticastReceivedFrameCount_Type = Counter32
_Dot11MulticastReceivedFrameCount_Object = MibTableColumn
dot11MulticastReceivedFrameCount = _Dot11MulticastReceivedFrameCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 11),
    _Dot11MulticastReceivedFrameCount_Type()
)
dot11MulticastReceivedFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11MulticastReceivedFrameCount.setStatus("current")
_Dot11FCSErrorCount_Type = Counter32
_Dot11FCSErrorCount_Object = MibTableColumn
dot11FCSErrorCount = _Dot11FCSErrorCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 12),
    _Dot11FCSErrorCount_Type()
)
dot11FCSErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11FCSErrorCount.setStatus("current")
_Dot11TransmittedFrameCount_Type = Counter32
_Dot11TransmittedFrameCount_Object = MibTableColumn
dot11TransmittedFrameCount = _Dot11TransmittedFrameCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 13),
    _Dot11TransmittedFrameCount_Type()
)
dot11TransmittedFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TransmittedFrameCount.setStatus("current")
_Dot11WEPUndecryptableCount_Type = Counter32
_Dot11WEPUndecryptableCount_Object = MibTableColumn
dot11WEPUndecryptableCount = _Dot11WEPUndecryptableCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 14),
    _Dot11WEPUndecryptableCount_Type()
)
dot11WEPUndecryptableCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11WEPUndecryptableCount.setStatus("current")
_Dot11QosDiscardedFragmentCount_Type = Counter32
_Dot11QosDiscardedFragmentCount_Object = MibTableColumn
dot11QosDiscardedFragmentCount = _Dot11QosDiscardedFragmentCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 15),
    _Dot11QosDiscardedFragmentCount_Type()
)
dot11QosDiscardedFragmentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11QosDiscardedFragmentCount.setStatus("current")
_Dot11AssociatedStationCount_Type = Counter32
_Dot11AssociatedStationCount_Object = MibTableColumn
dot11AssociatedStationCount = _Dot11AssociatedStationCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 16),
    _Dot11AssociatedStationCount_Type()
)
dot11AssociatedStationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11AssociatedStationCount.setStatus("current")
_Dot11QosCFPollsReceivedCount_Type = Counter32
_Dot11QosCFPollsReceivedCount_Object = MibTableColumn
dot11QosCFPollsReceivedCount = _Dot11QosCFPollsReceivedCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 17),
    _Dot11QosCFPollsReceivedCount_Type()
)
dot11QosCFPollsReceivedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11QosCFPollsReceivedCount.setStatus("current")
_Dot11QosCFPollsUnusedCount_Type = Counter32
_Dot11QosCFPollsUnusedCount_Object = MibTableColumn
dot11QosCFPollsUnusedCount = _Dot11QosCFPollsUnusedCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 18),
    _Dot11QosCFPollsUnusedCount_Type()
)
dot11QosCFPollsUnusedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11QosCFPollsUnusedCount.setStatus("current")
_Dot11QosCFPollsUnusableCount_Type = Counter32
_Dot11QosCFPollsUnusableCount_Object = MibTableColumn
dot11QosCFPollsUnusableCount = _Dot11QosCFPollsUnusableCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 19),
    _Dot11QosCFPollsUnusableCount_Type()
)
dot11QosCFPollsUnusableCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11QosCFPollsUnusableCount.setStatus("current")
_Dot11TransmittedAMSDUCount_Type = Counter32
_Dot11TransmittedAMSDUCount_Object = MibTableColumn
dot11TransmittedAMSDUCount = _Dot11TransmittedAMSDUCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 21),
    _Dot11TransmittedAMSDUCount_Type()
)
dot11TransmittedAMSDUCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TransmittedAMSDUCount.setStatus("current")
_Dot11FailedAMSDUCount_Type = Counter32
_Dot11FailedAMSDUCount_Object = MibTableColumn
dot11FailedAMSDUCount = _Dot11FailedAMSDUCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 22),
    _Dot11FailedAMSDUCount_Type()
)
dot11FailedAMSDUCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11FailedAMSDUCount.setStatus("current")
_Dot11RetryAMSDUCount_Type = Counter32
_Dot11RetryAMSDUCount_Object = MibTableColumn
dot11RetryAMSDUCount = _Dot11RetryAMSDUCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 23),
    _Dot11RetryAMSDUCount_Type()
)
dot11RetryAMSDUCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RetryAMSDUCount.setStatus("current")
_Dot11MultipleRetryAMSDUCount_Type = Counter32
_Dot11MultipleRetryAMSDUCount_Object = MibTableColumn
dot11MultipleRetryAMSDUCount = _Dot11MultipleRetryAMSDUCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 24),
    _Dot11MultipleRetryAMSDUCount_Type()
)
dot11MultipleRetryAMSDUCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11MultipleRetryAMSDUCount.setStatus("current")
_Dot11TransmittedOctetsInAMSDUCount_Type = Counter64
_Dot11TransmittedOctetsInAMSDUCount_Object = MibTableColumn
dot11TransmittedOctetsInAMSDUCount = _Dot11TransmittedOctetsInAMSDUCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 25),
    _Dot11TransmittedOctetsInAMSDUCount_Type()
)
dot11TransmittedOctetsInAMSDUCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TransmittedOctetsInAMSDUCount.setStatus("current")
_Dot11AMSDUAckFailureCount_Type = Counter32
_Dot11AMSDUAckFailureCount_Object = MibTableColumn
dot11AMSDUAckFailureCount = _Dot11AMSDUAckFailureCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 26),
    _Dot11AMSDUAckFailureCount_Type()
)
dot11AMSDUAckFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11AMSDUAckFailureCount.setStatus("current")
_Dot11ReceivedAMSDUCount_Type = Counter32
_Dot11ReceivedAMSDUCount_Object = MibTableColumn
dot11ReceivedAMSDUCount = _Dot11ReceivedAMSDUCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 27),
    _Dot11ReceivedAMSDUCount_Type()
)
dot11ReceivedAMSDUCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ReceivedAMSDUCount.setStatus("current")
_Dot11ReceivedOctetsInAMSDUCount_Type = Counter64
_Dot11ReceivedOctetsInAMSDUCount_Object = MibTableColumn
dot11ReceivedOctetsInAMSDUCount = _Dot11ReceivedOctetsInAMSDUCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 28),
    _Dot11ReceivedOctetsInAMSDUCount_Type()
)
dot11ReceivedOctetsInAMSDUCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ReceivedOctetsInAMSDUCount.setStatus("current")
_Dot11TransmittedAMPDUCount_Type = Counter32
_Dot11TransmittedAMPDUCount_Object = MibTableColumn
dot11TransmittedAMPDUCount = _Dot11TransmittedAMPDUCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 29),
    _Dot11TransmittedAMPDUCount_Type()
)
dot11TransmittedAMPDUCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TransmittedAMPDUCount.setStatus("current")
_Dot11TransmittedMPDUsInAMPDUCount_Type = Counter32
_Dot11TransmittedMPDUsInAMPDUCount_Object = MibTableColumn
dot11TransmittedMPDUsInAMPDUCount = _Dot11TransmittedMPDUsInAMPDUCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 30),
    _Dot11TransmittedMPDUsInAMPDUCount_Type()
)
dot11TransmittedMPDUsInAMPDUCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TransmittedMPDUsInAMPDUCount.setStatus("current")
_Dot11TransmittedOctetsInAMPDUCount_Type = Counter64
_Dot11TransmittedOctetsInAMPDUCount_Object = MibTableColumn
dot11TransmittedOctetsInAMPDUCount = _Dot11TransmittedOctetsInAMPDUCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 31),
    _Dot11TransmittedOctetsInAMPDUCount_Type()
)
dot11TransmittedOctetsInAMPDUCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TransmittedOctetsInAMPDUCount.setStatus("current")
_Dot11AMPDUReceivedCount_Type = Counter32
_Dot11AMPDUReceivedCount_Object = MibTableColumn
dot11AMPDUReceivedCount = _Dot11AMPDUReceivedCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 32),
    _Dot11AMPDUReceivedCount_Type()
)
dot11AMPDUReceivedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11AMPDUReceivedCount.setStatus("current")
_Dot11MPDUInReceivedAMPDUCount_Type = Counter32
_Dot11MPDUInReceivedAMPDUCount_Object = MibTableColumn
dot11MPDUInReceivedAMPDUCount = _Dot11MPDUInReceivedAMPDUCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 33),
    _Dot11MPDUInReceivedAMPDUCount_Type()
)
dot11MPDUInReceivedAMPDUCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11MPDUInReceivedAMPDUCount.setStatus("current")
_Dot11ReceivedOctetsInAMPDUCount_Type = Counter64
_Dot11ReceivedOctetsInAMPDUCount_Object = MibTableColumn
dot11ReceivedOctetsInAMPDUCount = _Dot11ReceivedOctetsInAMPDUCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 34),
    _Dot11ReceivedOctetsInAMPDUCount_Type()
)
dot11ReceivedOctetsInAMPDUCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ReceivedOctetsInAMPDUCount.setStatus("current")
_Dot11AMPDUDelimiterCRCErrorCount_Type = Counter32
_Dot11AMPDUDelimiterCRCErrorCount_Object = MibTableColumn
dot11AMPDUDelimiterCRCErrorCount = _Dot11AMPDUDelimiterCRCErrorCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 35),
    _Dot11AMPDUDelimiterCRCErrorCount_Type()
)
dot11AMPDUDelimiterCRCErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11AMPDUDelimiterCRCErrorCount.setStatus("current")
_Dot11ImplicitBARFailureCount_Type = Counter32
_Dot11ImplicitBARFailureCount_Object = MibTableColumn
dot11ImplicitBARFailureCount = _Dot11ImplicitBARFailureCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 36),
    _Dot11ImplicitBARFailureCount_Type()
)
dot11ImplicitBARFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ImplicitBARFailureCount.setStatus("current")
_Dot11ExplicitBARFailureCount_Type = Counter32
_Dot11ExplicitBARFailureCount_Object = MibTableColumn
dot11ExplicitBARFailureCount = _Dot11ExplicitBARFailureCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 37),
    _Dot11ExplicitBARFailureCount_Type()
)
dot11ExplicitBARFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ExplicitBARFailureCount.setStatus("current")
_Dot11ChannelWidthSwitchCount_Type = Counter32
_Dot11ChannelWidthSwitchCount_Object = MibTableColumn
dot11ChannelWidthSwitchCount = _Dot11ChannelWidthSwitchCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 38),
    _Dot11ChannelWidthSwitchCount_Type()
)
dot11ChannelWidthSwitchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ChannelWidthSwitchCount.setStatus("current")
_Dot11TwentyMHzFrameTransmittedCount_Type = Counter32
_Dot11TwentyMHzFrameTransmittedCount_Object = MibTableColumn
dot11TwentyMHzFrameTransmittedCount = _Dot11TwentyMHzFrameTransmittedCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 39),
    _Dot11TwentyMHzFrameTransmittedCount_Type()
)
dot11TwentyMHzFrameTransmittedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TwentyMHzFrameTransmittedCount.setStatus("current")
_Dot11FortyMHzFrameTransmittedCount_Type = Counter32
_Dot11FortyMHzFrameTransmittedCount_Object = MibTableColumn
dot11FortyMHzFrameTransmittedCount = _Dot11FortyMHzFrameTransmittedCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 40),
    _Dot11FortyMHzFrameTransmittedCount_Type()
)
dot11FortyMHzFrameTransmittedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11FortyMHzFrameTransmittedCount.setStatus("current")
_Dot11TwentyMHzFrameReceivedCount_Type = Counter32
_Dot11TwentyMHzFrameReceivedCount_Object = MibTableColumn
dot11TwentyMHzFrameReceivedCount = _Dot11TwentyMHzFrameReceivedCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 41),
    _Dot11TwentyMHzFrameReceivedCount_Type()
)
dot11TwentyMHzFrameReceivedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TwentyMHzFrameReceivedCount.setStatus("current")
_Dot11FortyMHzFrameReceivedCount_Type = Counter32
_Dot11FortyMHzFrameReceivedCount_Object = MibTableColumn
dot11FortyMHzFrameReceivedCount = _Dot11FortyMHzFrameReceivedCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 42),
    _Dot11FortyMHzFrameReceivedCount_Type()
)
dot11FortyMHzFrameReceivedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11FortyMHzFrameReceivedCount.setStatus("current")
_Dot11PSMPSuccessCount_Type = Counter32
_Dot11PSMPSuccessCount_Object = MibTableColumn
dot11PSMPSuccessCount = _Dot11PSMPSuccessCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 43),
    _Dot11PSMPSuccessCount_Type()
)
dot11PSMPSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11PSMPSuccessCount.setStatus("current")
_Dot11PSMPFailureCount_Type = Counter32
_Dot11PSMPFailureCount_Object = MibTableColumn
dot11PSMPFailureCount = _Dot11PSMPFailureCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 44),
    _Dot11PSMPFailureCount_Type()
)
dot11PSMPFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11PSMPFailureCount.setStatus("current")
_Dot11GrantedRDGUsedCount_Type = Counter32
_Dot11GrantedRDGUsedCount_Object = MibTableColumn
dot11GrantedRDGUsedCount = _Dot11GrantedRDGUsedCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 45),
    _Dot11GrantedRDGUsedCount_Type()
)
dot11GrantedRDGUsedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11GrantedRDGUsedCount.setStatus("current")
_Dot11GrantedRDGUnusedCount_Type = Counter32
_Dot11GrantedRDGUnusedCount_Object = MibTableColumn
dot11GrantedRDGUnusedCount = _Dot11GrantedRDGUnusedCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 46),
    _Dot11GrantedRDGUnusedCount_Type()
)
dot11GrantedRDGUnusedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11GrantedRDGUnusedCount.setStatus("current")
_Dot11TransmittedFramesInGrantedRDGCount_Type = Counter32
_Dot11TransmittedFramesInGrantedRDGCount_Object = MibTableColumn
dot11TransmittedFramesInGrantedRDGCount = _Dot11TransmittedFramesInGrantedRDGCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 47),
    _Dot11TransmittedFramesInGrantedRDGCount_Type()
)
dot11TransmittedFramesInGrantedRDGCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TransmittedFramesInGrantedRDGCount.setStatus("current")
_Dot11TransmittedOctetsInGrantedRDGCount_Type = Counter64
_Dot11TransmittedOctetsInGrantedRDGCount_Object = MibTableColumn
dot11TransmittedOctetsInGrantedRDGCount = _Dot11TransmittedOctetsInGrantedRDGCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 48),
    _Dot11TransmittedOctetsInGrantedRDGCount_Type()
)
dot11TransmittedOctetsInGrantedRDGCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TransmittedOctetsInGrantedRDGCount.setStatus("current")
_Dot11BeamformingFrameCount_Type = Counter32
_Dot11BeamformingFrameCount_Object = MibTableColumn
dot11BeamformingFrameCount = _Dot11BeamformingFrameCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 49),
    _Dot11BeamformingFrameCount_Type()
)
dot11BeamformingFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11BeamformingFrameCount.setStatus("current")
_Dot11DualCTSSuccessCount_Type = Counter32
_Dot11DualCTSSuccessCount_Object = MibTableColumn
dot11DualCTSSuccessCount = _Dot11DualCTSSuccessCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 50),
    _Dot11DualCTSSuccessCount_Type()
)
dot11DualCTSSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11DualCTSSuccessCount.setStatus("current")
_Dot11DualCTSFailureCount_Type = Counter32
_Dot11DualCTSFailureCount_Object = MibTableColumn
dot11DualCTSFailureCount = _Dot11DualCTSFailureCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 51),
    _Dot11DualCTSFailureCount_Type()
)
dot11DualCTSFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11DualCTSFailureCount.setStatus("current")
_Dot11STBCCTSSuccessCount_Type = Counter32
_Dot11STBCCTSSuccessCount_Object = MibTableColumn
dot11STBCCTSSuccessCount = _Dot11STBCCTSSuccessCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 52),
    _Dot11STBCCTSSuccessCount_Type()
)
dot11STBCCTSSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11STBCCTSSuccessCount.setStatus("current")
_Dot11STBCCTSFailureCount_Type = Counter32
_Dot11STBCCTSFailureCount_Object = MibTableColumn
dot11STBCCTSFailureCount = _Dot11STBCCTSFailureCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 53),
    _Dot11STBCCTSFailureCount_Type()
)
dot11STBCCTSFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11STBCCTSFailureCount.setStatus("current")
_Dot11nonSTBCCTSSuccessCount_Type = Counter32
_Dot11nonSTBCCTSSuccessCount_Object = MibTableColumn
dot11nonSTBCCTSSuccessCount = _Dot11nonSTBCCTSSuccessCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 54),
    _Dot11nonSTBCCTSSuccessCount_Type()
)
dot11nonSTBCCTSSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11nonSTBCCTSSuccessCount.setStatus("current")
_Dot11nonSTBCCTSFailureCount_Type = Counter32
_Dot11nonSTBCCTSFailureCount_Object = MibTableColumn
dot11nonSTBCCTSFailureCount = _Dot11nonSTBCCTSFailureCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 55),
    _Dot11nonSTBCCTSFailureCount_Type()
)
dot11nonSTBCCTSFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11nonSTBCCTSFailureCount.setStatus("current")
_Dot11RTSLSIGSuccessCount_Type = Counter32
_Dot11RTSLSIGSuccessCount_Object = MibTableColumn
dot11RTSLSIGSuccessCount = _Dot11RTSLSIGSuccessCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 56),
    _Dot11RTSLSIGSuccessCount_Type()
)
dot11RTSLSIGSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RTSLSIGSuccessCount.setStatus("current")
_Dot11RTSLSIGFailureCount_Type = Counter32
_Dot11RTSLSIGFailureCount_Object = MibTableColumn
dot11RTSLSIGFailureCount = _Dot11RTSLSIGFailureCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 57),
    _Dot11RTSLSIGFailureCount_Type()
)
dot11RTSLSIGFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RTSLSIGFailureCount.setStatus("current")
_Dot11GroupAddressesTable_Object = MibTable
dot11GroupAddressesTable = _Dot11GroupAddressesTable_Object(
    (1, 2, 840, 10036, 2, 3)
)
if mibBuilder.loadTexts:
    dot11GroupAddressesTable.setStatus("current")
_Dot11GroupAddressesEntry_Object = MibTableRow
dot11GroupAddressesEntry = _Dot11GroupAddressesEntry_Object(
    (1, 2, 840, 10036, 2, 3, 1)
)
dot11GroupAddressesEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "IEEE802dot11-MIB", "dot11GroupAddressesIndex"),
)
if mibBuilder.loadTexts:
    dot11GroupAddressesEntry.setStatus("current")


class _Dot11GroupAddressesIndex_Type(Integer32):
    """Custom type dot11GroupAddressesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dot11GroupAddressesIndex_Type.__name__ = "Integer32"
_Dot11GroupAddressesIndex_Object = MibTableColumn
dot11GroupAddressesIndex = _Dot11GroupAddressesIndex_Object(
    (1, 2, 840, 10036, 2, 3, 1, 1),
    _Dot11GroupAddressesIndex_Type()
)
dot11GroupAddressesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11GroupAddressesIndex.setStatus("current")
_Dot11Address_Type = MacAddress
_Dot11Address_Object = MibTableColumn
dot11Address = _Dot11Address_Object(
    (1, 2, 840, 10036, 2, 3, 1, 2),
    _Dot11Address_Type()
)
dot11Address.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot11Address.setStatus("current")


class _Dot11GroupAddressesStatus_Type(RowStatus):
    """Custom type dot11GroupAddressesStatus based on RowStatus"""


_Dot11GroupAddressesStatus_Object = MibTableColumn
dot11GroupAddressesStatus = _Dot11GroupAddressesStatus_Object(
    (1, 2, 840, 10036, 2, 3, 1, 3),
    _Dot11GroupAddressesStatus_Type()
)
dot11GroupAddressesStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot11GroupAddressesStatus.setStatus("current")
_Dot11EDCATable_Object = MibTable
dot11EDCATable = _Dot11EDCATable_Object(
    (1, 2, 840, 10036, 2, 4)
)
if mibBuilder.loadTexts:
    dot11EDCATable.setStatus("current")
_Dot11EDCATableEntry_Object = MibTableRow
dot11EDCATableEntry = _Dot11EDCATableEntry_Object(
    (1, 2, 840, 10036, 2, 4, 1)
)
dot11EDCATableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "IEEE802dot11-MIB", "dot11EDCATableIndex"),
)
if mibBuilder.loadTexts:
    dot11EDCATableEntry.setStatus("current")


class _Dot11EDCATableIndex_Type(Integer32):
    """Custom type dot11EDCATableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Dot11EDCATableIndex_Type.__name__ = "Integer32"
_Dot11EDCATableIndex_Object = MibTableColumn
dot11EDCATableIndex = _Dot11EDCATableIndex_Object(
    (1, 2, 840, 10036, 2, 4, 1, 1),
    _Dot11EDCATableIndex_Type()
)
dot11EDCATableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11EDCATableIndex.setStatus("current")


class _Dot11EDCATableCWmin_Type(Integer32):
    """Custom type dot11EDCATableCWmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Dot11EDCATableCWmin_Type.__name__ = "Integer32"
_Dot11EDCATableCWmin_Object = MibTableColumn
dot11EDCATableCWmin = _Dot11EDCATableCWmin_Object(
    (1, 2, 840, 10036, 2, 4, 1, 2),
    _Dot11EDCATableCWmin_Type()
)
dot11EDCATableCWmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11EDCATableCWmin.setStatus("current")


class _Dot11EDCATableCWmax_Type(Integer32):
    """Custom type dot11EDCATableCWmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot11EDCATableCWmax_Type.__name__ = "Integer32"
_Dot11EDCATableCWmax_Object = MibTableColumn
dot11EDCATableCWmax = _Dot11EDCATableCWmax_Object(
    (1, 2, 840, 10036, 2, 4, 1, 3),
    _Dot11EDCATableCWmax_Type()
)
dot11EDCATableCWmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11EDCATableCWmax.setStatus("current")


class _Dot11EDCATableAIFSN_Type(Integer32):
    """Custom type dot11EDCATableAIFSN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 15),
    )


_Dot11EDCATableAIFSN_Type.__name__ = "Integer32"
_Dot11EDCATableAIFSN_Object = MibTableColumn
dot11EDCATableAIFSN = _Dot11EDCATableAIFSN_Object(
    (1, 2, 840, 10036, 2, 4, 1, 4),
    _Dot11EDCATableAIFSN_Type()
)
dot11EDCATableAIFSN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11EDCATableAIFSN.setStatus("current")


class _Dot11EDCATableTXOPLimit_Type(Integer32):
    """Custom type dot11EDCATableTXOPLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot11EDCATableTXOPLimit_Type.__name__ = "Integer32"
_Dot11EDCATableTXOPLimit_Object = MibTableColumn
dot11EDCATableTXOPLimit = _Dot11EDCATableTXOPLimit_Object(
    (1, 2, 840, 10036, 2, 4, 1, 5),
    _Dot11EDCATableTXOPLimit_Type()
)
dot11EDCATableTXOPLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11EDCATableTXOPLimit.setStatus("current")


class _Dot11EDCATableMSDULifetime_Type(Integer32):
    """Custom type dot11EDCATableMSDULifetime based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_Dot11EDCATableMSDULifetime_Type.__name__ = "Integer32"
_Dot11EDCATableMSDULifetime_Object = MibTableColumn
dot11EDCATableMSDULifetime = _Dot11EDCATableMSDULifetime_Object(
    (1, 2, 840, 10036, 2, 4, 1, 6),
    _Dot11EDCATableMSDULifetime_Type()
)
dot11EDCATableMSDULifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11EDCATableMSDULifetime.setStatus("current")


class _Dot11EDCATableMandatory_Type(TruthValue):
    """Custom type dot11EDCATableMandatory based on TruthValue"""


_Dot11EDCATableMandatory_Object = MibTableColumn
dot11EDCATableMandatory = _Dot11EDCATableMandatory_Object(
    (1, 2, 840, 10036, 2, 4, 1, 7),
    _Dot11EDCATableMandatory_Type()
)
dot11EDCATableMandatory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11EDCATableMandatory.setStatus("current")
_Dot11QAPEDCATable_Object = MibTable
dot11QAPEDCATable = _Dot11QAPEDCATable_Object(
    (1, 2, 840, 10036, 2, 5)
)
if mibBuilder.loadTexts:
    dot11QAPEDCATable.setStatus("current")
_Dot11QAPEDCATableEntry_Object = MibTableRow
dot11QAPEDCATableEntry = _Dot11QAPEDCATableEntry_Object(
    (1, 2, 840, 10036, 2, 5, 1)
)
dot11QAPEDCATableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "IEEE802dot11-MIB", "dot11QAPEDCATableIndex"),
)
if mibBuilder.loadTexts:
    dot11QAPEDCATableEntry.setStatus("current")


class _Dot11QAPEDCATableIndex_Type(Integer32):
    """Custom type dot11QAPEDCATableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Dot11QAPEDCATableIndex_Type.__name__ = "Integer32"
_Dot11QAPEDCATableIndex_Object = MibTableColumn
dot11QAPEDCATableIndex = _Dot11QAPEDCATableIndex_Object(
    (1, 2, 840, 10036, 2, 5, 1, 1),
    _Dot11QAPEDCATableIndex_Type()
)
dot11QAPEDCATableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11QAPEDCATableIndex.setStatus("current")


class _Dot11QAPEDCATableCWmin_Type(Integer32):
    """Custom type dot11QAPEDCATableCWmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Dot11QAPEDCATableCWmin_Type.__name__ = "Integer32"
_Dot11QAPEDCATableCWmin_Object = MibTableColumn
dot11QAPEDCATableCWmin = _Dot11QAPEDCATableCWmin_Object(
    (1, 2, 840, 10036, 2, 5, 1, 2),
    _Dot11QAPEDCATableCWmin_Type()
)
dot11QAPEDCATableCWmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11QAPEDCATableCWmin.setStatus("current")


class _Dot11QAPEDCATableCWmax_Type(Integer32):
    """Custom type dot11QAPEDCATableCWmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot11QAPEDCATableCWmax_Type.__name__ = "Integer32"
_Dot11QAPEDCATableCWmax_Object = MibTableColumn
dot11QAPEDCATableCWmax = _Dot11QAPEDCATableCWmax_Object(
    (1, 2, 840, 10036, 2, 5, 1, 3),
    _Dot11QAPEDCATableCWmax_Type()
)
dot11QAPEDCATableCWmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11QAPEDCATableCWmax.setStatus("current")


class _Dot11QAPEDCATableAIFSN_Type(Integer32):
    """Custom type dot11QAPEDCATableAIFSN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Dot11QAPEDCATableAIFSN_Type.__name__ = "Integer32"
_Dot11QAPEDCATableAIFSN_Object = MibTableColumn
dot11QAPEDCATableAIFSN = _Dot11QAPEDCATableAIFSN_Object(
    (1, 2, 840, 10036, 2, 5, 1, 4),
    _Dot11QAPEDCATableAIFSN_Type()
)
dot11QAPEDCATableAIFSN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11QAPEDCATableAIFSN.setStatus("current")


class _Dot11QAPEDCATableTXOPLimit_Type(Integer32):
    """Custom type dot11QAPEDCATableTXOPLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot11QAPEDCATableTXOPLimit_Type.__name__ = "Integer32"
_Dot11QAPEDCATableTXOPLimit_Object = MibTableColumn
dot11QAPEDCATableTXOPLimit = _Dot11QAPEDCATableTXOPLimit_Object(
    (1, 2, 840, 10036, 2, 5, 1, 5),
    _Dot11QAPEDCATableTXOPLimit_Type()
)
dot11QAPEDCATableTXOPLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11QAPEDCATableTXOPLimit.setStatus("current")


class _Dot11QAPEDCATableMSDULifetime_Type(Integer32):
    """Custom type dot11QAPEDCATableMSDULifetime based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_Dot11QAPEDCATableMSDULifetime_Type.__name__ = "Integer32"
_Dot11QAPEDCATableMSDULifetime_Object = MibTableColumn
dot11QAPEDCATableMSDULifetime = _Dot11QAPEDCATableMSDULifetime_Object(
    (1, 2, 840, 10036, 2, 5, 1, 6),
    _Dot11QAPEDCATableMSDULifetime_Type()
)
dot11QAPEDCATableMSDULifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11QAPEDCATableMSDULifetime.setStatus("current")


class _Dot11QAPEDCATableMandatory_Type(TruthValue):
    """Custom type dot11QAPEDCATableMandatory based on TruthValue"""


_Dot11QAPEDCATableMandatory_Object = MibTableColumn
dot11QAPEDCATableMandatory = _Dot11QAPEDCATableMandatory_Object(
    (1, 2, 840, 10036, 2, 5, 1, 7),
    _Dot11QAPEDCATableMandatory_Type()
)
dot11QAPEDCATableMandatory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11QAPEDCATableMandatory.setStatus("current")
_Dot11QosCountersTable_Object = MibTable
dot11QosCountersTable = _Dot11QosCountersTable_Object(
    (1, 2, 840, 10036, 2, 6)
)
if mibBuilder.loadTexts:
    dot11QosCountersTable.setStatus("current")
_Dot11QosCountersEntry_Object = MibTableRow
dot11QosCountersEntry = _Dot11QosCountersEntry_Object(
    (1, 2, 840, 10036, 2, 6, 1)
)
dot11QosCountersEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "IEEE802dot11-MIB", "dot11QosCountersIndex"),
)
if mibBuilder.loadTexts:
    dot11QosCountersEntry.setStatus("current")


class _Dot11QosCountersIndex_Type(Integer32):
    """Custom type dot11QosCountersIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Dot11QosCountersIndex_Type.__name__ = "Integer32"
_Dot11QosCountersIndex_Object = MibTableColumn
dot11QosCountersIndex = _Dot11QosCountersIndex_Object(
    (1, 2, 840, 10036, 2, 6, 1, 1),
    _Dot11QosCountersIndex_Type()
)
dot11QosCountersIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11QosCountersIndex.setStatus("current")
_Dot11QosTransmittedFragmentCount_Type = Counter32
_Dot11QosTransmittedFragmentCount_Object = MibTableColumn
dot11QosTransmittedFragmentCount = _Dot11QosTransmittedFragmentCount_Object(
    (1, 2, 840, 10036, 2, 6, 1, 2),
    _Dot11QosTransmittedFragmentCount_Type()
)
dot11QosTransmittedFragmentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11QosTransmittedFragmentCount.setStatus("current")
_Dot11QosFailedCount_Type = Counter32
_Dot11QosFailedCount_Object = MibTableColumn
dot11QosFailedCount = _Dot11QosFailedCount_Object(
    (1, 2, 840, 10036, 2, 6, 1, 3),
    _Dot11QosFailedCount_Type()
)
dot11QosFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11QosFailedCount.setStatus("current")
_Dot11QosRetryCount_Type = Counter32
_Dot11QosRetryCount_Object = MibTableColumn
dot11QosRetryCount = _Dot11QosRetryCount_Object(
    (1, 2, 840, 10036, 2, 6, 1, 4),
    _Dot11QosRetryCount_Type()
)
dot11QosRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11QosRetryCount.setStatus("current")
_Dot11QosMultipleRetryCount_Type = Counter32
_Dot11QosMultipleRetryCount_Object = MibTableColumn
dot11QosMultipleRetryCount = _Dot11QosMultipleRetryCount_Object(
    (1, 2, 840, 10036, 2, 6, 1, 5),
    _Dot11QosMultipleRetryCount_Type()
)
dot11QosMultipleRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11QosMultipleRetryCount.setStatus("current")
_Dot11QosFrameDuplicateCount_Type = Counter32
_Dot11QosFrameDuplicateCount_Object = MibTableColumn
dot11QosFrameDuplicateCount = _Dot11QosFrameDuplicateCount_Object(
    (1, 2, 840, 10036, 2, 6, 1, 6),
    _Dot11QosFrameDuplicateCount_Type()
)
dot11QosFrameDuplicateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11QosFrameDuplicateCount.setStatus("current")
_Dot11QosRTSSuccessCount_Type = Counter32
_Dot11QosRTSSuccessCount_Object = MibTableColumn
dot11QosRTSSuccessCount = _Dot11QosRTSSuccessCount_Object(
    (1, 2, 840, 10036, 2, 6, 1, 7),
    _Dot11QosRTSSuccessCount_Type()
)
dot11QosRTSSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11QosRTSSuccessCount.setStatus("current")
_Dot11QosRTSFailureCount_Type = Counter32
_Dot11QosRTSFailureCount_Object = MibTableColumn
dot11QosRTSFailureCount = _Dot11QosRTSFailureCount_Object(
    (1, 2, 840, 10036, 2, 6, 1, 8),
    _Dot11QosRTSFailureCount_Type()
)
dot11QosRTSFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11QosRTSFailureCount.setStatus("current")
_Dot11QosACKFailureCount_Type = Counter32
_Dot11QosACKFailureCount_Object = MibTableColumn
dot11QosACKFailureCount = _Dot11QosACKFailureCount_Object(
    (1, 2, 840, 10036, 2, 6, 1, 9),
    _Dot11QosACKFailureCount_Type()
)
dot11QosACKFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11QosACKFailureCount.setStatus("current")
_Dot11QosReceivedFragmentCount_Type = Counter32
_Dot11QosReceivedFragmentCount_Object = MibTableColumn
dot11QosReceivedFragmentCount = _Dot11QosReceivedFragmentCount_Object(
    (1, 2, 840, 10036, 2, 6, 1, 10),
    _Dot11QosReceivedFragmentCount_Type()
)
dot11QosReceivedFragmentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11QosReceivedFragmentCount.setStatus("current")
_Dot11QosTransmittedFrameCount_Type = Counter32
_Dot11QosTransmittedFrameCount_Object = MibTableColumn
dot11QosTransmittedFrameCount = _Dot11QosTransmittedFrameCount_Object(
    (1, 2, 840, 10036, 2, 6, 1, 11),
    _Dot11QosTransmittedFrameCount_Type()
)
dot11QosTransmittedFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11QosTransmittedFrameCount.setStatus("current")
_Dot11QosDiscardedFrameCount_Type = Counter32
_Dot11QosDiscardedFrameCount_Object = MibTableColumn
dot11QosDiscardedFrameCount = _Dot11QosDiscardedFrameCount_Object(
    (1, 2, 840, 10036, 2, 6, 1, 12),
    _Dot11QosDiscardedFrameCount_Type()
)
dot11QosDiscardedFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11QosDiscardedFrameCount.setStatus("current")
_Dot11QosMPDUsReceivedCount_Type = Counter32
_Dot11QosMPDUsReceivedCount_Object = MibTableColumn
dot11QosMPDUsReceivedCount = _Dot11QosMPDUsReceivedCount_Object(
    (1, 2, 840, 10036, 2, 6, 1, 13),
    _Dot11QosMPDUsReceivedCount_Type()
)
dot11QosMPDUsReceivedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11QosMPDUsReceivedCount.setStatus("current")
_Dot11QosRetriesReceivedCount_Type = Counter32
_Dot11QosRetriesReceivedCount_Object = MibTableColumn
dot11QosRetriesReceivedCount = _Dot11QosRetriesReceivedCount_Object(
    (1, 2, 840, 10036, 2, 6, 1, 14),
    _Dot11QosRetriesReceivedCount_Type()
)
dot11QosRetriesReceivedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11QosRetriesReceivedCount.setStatus("current")
_Dot11res_ObjectIdentity = ObjectIdentity
dot11res = _Dot11res_ObjectIdentity(
    (1, 2, 840, 10036, 3)
)
_Dot11resAttribute_ObjectIdentity = ObjectIdentity
dot11resAttribute = _Dot11resAttribute_ObjectIdentity(
    (1, 2, 840, 10036, 3, 1)
)


class _Dot11ResourceTypeIDName_Type(DisplayString):
    """Custom type dot11ResourceTypeIDName based on DisplayString"""
    defaultValue = OctetString("RTID")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Dot11ResourceTypeIDName_Type.__name__ = "DisplayString"
_Dot11ResourceTypeIDName_Object = MibScalar
dot11ResourceTypeIDName = _Dot11ResourceTypeIDName_Object(
    (1, 2, 840, 10036, 3, 1, 1),
    _Dot11ResourceTypeIDName_Type()
)
dot11ResourceTypeIDName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ResourceTypeIDName.setStatus("current")
_Dot11ResourceInfoTable_Object = MibTable
dot11ResourceInfoTable = _Dot11ResourceInfoTable_Object(
    (1, 2, 840, 10036, 3, 1, 2)
)
if mibBuilder.loadTexts:
    dot11ResourceInfoTable.setStatus("current")
_Dot11ResourceInfoEntry_Object = MibTableRow
dot11ResourceInfoEntry = _Dot11ResourceInfoEntry_Object(
    (1, 2, 840, 10036, 3, 1, 2, 1)
)
dot11ResourceInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11ResourceInfoEntry.setStatus("current")


class _Dot11manufacturerOUI_Type(OctetString):
    """Custom type dot11manufacturerOUI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_Dot11manufacturerOUI_Type.__name__ = "OctetString"
_Dot11manufacturerOUI_Object = MibTableColumn
dot11manufacturerOUI = _Dot11manufacturerOUI_Object(
    (1, 2, 840, 10036, 3, 1, 2, 1, 1),
    _Dot11manufacturerOUI_Type()
)
dot11manufacturerOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11manufacturerOUI.setStatus("current")


class _Dot11manufacturerName_Type(DisplayString):
    """Custom type dot11manufacturerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Dot11manufacturerName_Type.__name__ = "DisplayString"
_Dot11manufacturerName_Object = MibTableColumn
dot11manufacturerName = _Dot11manufacturerName_Object(
    (1, 2, 840, 10036, 3, 1, 2, 1, 2),
    _Dot11manufacturerName_Type()
)
dot11manufacturerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11manufacturerName.setStatus("current")


class _Dot11manufacturerProductName_Type(DisplayString):
    """Custom type dot11manufacturerProductName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Dot11manufacturerProductName_Type.__name__ = "DisplayString"
_Dot11manufacturerProductName_Object = MibTableColumn
dot11manufacturerProductName = _Dot11manufacturerProductName_Object(
    (1, 2, 840, 10036, 3, 1, 2, 1, 3),
    _Dot11manufacturerProductName_Type()
)
dot11manufacturerProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11manufacturerProductName.setStatus("current")


class _Dot11manufacturerProductVersion_Type(DisplayString):
    """Custom type dot11manufacturerProductVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Dot11manufacturerProductVersion_Type.__name__ = "DisplayString"
_Dot11manufacturerProductVersion_Object = MibTableColumn
dot11manufacturerProductVersion = _Dot11manufacturerProductVersion_Object(
    (1, 2, 840, 10036, 3, 1, 2, 1, 4),
    _Dot11manufacturerProductVersion_Type()
)
dot11manufacturerProductVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11manufacturerProductVersion.setStatus("current")
_Dot11phy_ObjectIdentity = ObjectIdentity
dot11phy = _Dot11phy_ObjectIdentity(
    (1, 2, 840, 10036, 4)
)
_Dot11PhyOperationTable_Object = MibTable
dot11PhyOperationTable = _Dot11PhyOperationTable_Object(
    (1, 2, 840, 10036, 4, 1)
)
if mibBuilder.loadTexts:
    dot11PhyOperationTable.setStatus("current")
_Dot11PhyOperationEntry_Object = MibTableRow
dot11PhyOperationEntry = _Dot11PhyOperationEntry_Object(
    (1, 2, 840, 10036, 4, 1, 1)
)
dot11PhyOperationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11PhyOperationEntry.setStatus("current")


class _Dot11PHYType_Type(Integer32):
    """Custom type dot11PHYType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("dsss", 2),
          ("erp", 6),
          ("fhss", 1),
          ("hrdsss", 5),
          ("ht", 7),
          ("irbaseband", 3),
          ("ofdm", 4))
    )


_Dot11PHYType_Type.__name__ = "Integer32"
_Dot11PHYType_Object = MibTableColumn
dot11PHYType = _Dot11PHYType_Object(
    (1, 2, 840, 10036, 4, 1, 1, 1),
    _Dot11PHYType_Type()
)
dot11PHYType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11PHYType.setStatus("current")


class _Dot11CurrentRegDomain_Type(Integer32):
    """Custom type dot11CurrentRegDomain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dot11CurrentRegDomain_Type.__name__ = "Integer32"
_Dot11CurrentRegDomain_Object = MibTableColumn
dot11CurrentRegDomain = _Dot11CurrentRegDomain_Object(
    (1, 2, 840, 10036, 4, 1, 1, 2),
    _Dot11CurrentRegDomain_Type()
)
dot11CurrentRegDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11CurrentRegDomain.setStatus("current")


class _Dot11TempType_Type(Integer32):
    """Custom type dot11TempType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tempType1", 1),
          ("tempType2", 2))
    )


_Dot11TempType_Type.__name__ = "Integer32"
_Dot11TempType_Object = MibTableColumn
dot11TempType = _Dot11TempType_Object(
    (1, 2, 840, 10036, 4, 1, 1, 3),
    _Dot11TempType_Type()
)
dot11TempType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TempType.setStatus("current")
_Dot11PhyAntennaTable_Object = MibTable
dot11PhyAntennaTable = _Dot11PhyAntennaTable_Object(
    (1, 2, 840, 10036, 4, 2)
)
if mibBuilder.loadTexts:
    dot11PhyAntennaTable.setStatus("current")
_Dot11PhyAntennaEntry_Object = MibTableRow
dot11PhyAntennaEntry = _Dot11PhyAntennaEntry_Object(
    (1, 2, 840, 10036, 4, 2, 1)
)
dot11PhyAntennaEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11PhyAntennaEntry.setStatus("current")


class _Dot11CurrentTxAntenna_Type(Integer32):
    """Custom type dot11CurrentTxAntenna based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Dot11CurrentTxAntenna_Type.__name__ = "Integer32"
_Dot11CurrentTxAntenna_Object = MibTableColumn
dot11CurrentTxAntenna = _Dot11CurrentTxAntenna_Object(
    (1, 2, 840, 10036, 4, 2, 1, 1),
    _Dot11CurrentTxAntenna_Type()
)
dot11CurrentTxAntenna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11CurrentTxAntenna.setStatus("current")


class _Dot11DiversitySupport_Type(Integer32):
    """Custom type dot11DiversitySupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 3),
          ("fixedlist", 1),
          ("notsupported", 2))
    )


_Dot11DiversitySupport_Type.__name__ = "Integer32"
_Dot11DiversitySupport_Object = MibTableColumn
dot11DiversitySupport = _Dot11DiversitySupport_Object(
    (1, 2, 840, 10036, 4, 2, 1, 2),
    _Dot11DiversitySupport_Type()
)
dot11DiversitySupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11DiversitySupport.setStatus("current")


class _Dot11CurrentRxAntenna_Type(Integer32):
    """Custom type dot11CurrentRxAntenna based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Dot11CurrentRxAntenna_Type.__name__ = "Integer32"
_Dot11CurrentRxAntenna_Object = MibTableColumn
dot11CurrentRxAntenna = _Dot11CurrentRxAntenna_Object(
    (1, 2, 840, 10036, 4, 2, 1, 3),
    _Dot11CurrentRxAntenna_Type()
)
dot11CurrentRxAntenna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11CurrentRxAntenna.setStatus("current")


class _Dot11AntennaSelectionOptionImplemented_Type(TruthValue):
    """Custom type dot11AntennaSelectionOptionImplemented based on TruthValue"""


_Dot11AntennaSelectionOptionImplemented_Object = MibTableColumn
dot11AntennaSelectionOptionImplemented = _Dot11AntennaSelectionOptionImplemented_Object(
    (1, 2, 840, 10036, 4, 2, 1, 4),
    _Dot11AntennaSelectionOptionImplemented_Type()
)
dot11AntennaSelectionOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11AntennaSelectionOptionImplemented.setStatus("current")


class _Dot11TransmitExplicitCSIFeedbackASOptionImplemented_Type(TruthValue):
    """Custom type dot11TransmitExplicitCSIFeedbackASOptionImplemented based on TruthValue"""


_Dot11TransmitExplicitCSIFeedbackASOptionImplemented_Object = MibTableColumn
dot11TransmitExplicitCSIFeedbackASOptionImplemented = _Dot11TransmitExplicitCSIFeedbackASOptionImplemented_Object(
    (1, 2, 840, 10036, 4, 2, 1, 5),
    _Dot11TransmitExplicitCSIFeedbackASOptionImplemented_Type()
)
dot11TransmitExplicitCSIFeedbackASOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TransmitExplicitCSIFeedbackASOptionImplemented.setStatus("current")


class _Dot11TransmitIndicesFeedbackASOptionImplemented_Type(TruthValue):
    """Custom type dot11TransmitIndicesFeedbackASOptionImplemented based on TruthValue"""


_Dot11TransmitIndicesFeedbackASOptionImplemented_Object = MibTableColumn
dot11TransmitIndicesFeedbackASOptionImplemented = _Dot11TransmitIndicesFeedbackASOptionImplemented_Object(
    (1, 2, 840, 10036, 4, 2, 1, 6),
    _Dot11TransmitIndicesFeedbackASOptionImplemented_Type()
)
dot11TransmitIndicesFeedbackASOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TransmitIndicesFeedbackASOptionImplemented.setStatus("current")


class _Dot11ExplicitCSIFeedbackASOptionImplemented_Type(TruthValue):
    """Custom type dot11ExplicitCSIFeedbackASOptionImplemented based on TruthValue"""


_Dot11ExplicitCSIFeedbackASOptionImplemented_Object = MibTableColumn
dot11ExplicitCSIFeedbackASOptionImplemented = _Dot11ExplicitCSIFeedbackASOptionImplemented_Object(
    (1, 2, 840, 10036, 4, 2, 1, 7),
    _Dot11ExplicitCSIFeedbackASOptionImplemented_Type()
)
dot11ExplicitCSIFeedbackASOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ExplicitCSIFeedbackASOptionImplemented.setStatus("current")


class _Dot11TransmitIndicesComputationFeedbackASOptionImplemented_Type(TruthValue):
    """Custom type dot11TransmitIndicesComputationFeedbackASOptionImplemented based on TruthValue"""


_Dot11TransmitIndicesComputationFeedbackASOptionImplemented_Object = MibTableColumn
dot11TransmitIndicesComputationFeedbackASOptionImplemented = _Dot11TransmitIndicesComputationFeedbackASOptionImplemented_Object(
    (1, 2, 840, 10036, 4, 2, 1, 8),
    _Dot11TransmitIndicesComputationFeedbackASOptionImplemented_Type()
)
dot11TransmitIndicesComputationFeedbackASOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TransmitIndicesComputationFeedbackASOptionImplemented.setStatus("current")


class _Dot11ReceiveAntennaSelectionOptionImplemented_Type(TruthValue):
    """Custom type dot11ReceiveAntennaSelectionOptionImplemented based on TruthValue"""


_Dot11ReceiveAntennaSelectionOptionImplemented_Object = MibTableColumn
dot11ReceiveAntennaSelectionOptionImplemented = _Dot11ReceiveAntennaSelectionOptionImplemented_Object(
    (1, 2, 840, 10036, 4, 2, 1, 9),
    _Dot11ReceiveAntennaSelectionOptionImplemented_Type()
)
dot11ReceiveAntennaSelectionOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ReceiveAntennaSelectionOptionImplemented.setStatus("current")


class _Dot11TransmitSoundingPPDUOptionImplemented_Type(TruthValue):
    """Custom type dot11TransmitSoundingPPDUOptionImplemented based on TruthValue"""


_Dot11TransmitSoundingPPDUOptionImplemented_Object = MibTableColumn
dot11TransmitSoundingPPDUOptionImplemented = _Dot11TransmitSoundingPPDUOptionImplemented_Object(
    (1, 2, 840, 10036, 4, 2, 1, 10),
    _Dot11TransmitSoundingPPDUOptionImplemented_Type()
)
dot11TransmitSoundingPPDUOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TransmitSoundingPPDUOptionImplemented.setStatus("current")
_Dot11PhyTxPowerTable_Object = MibTable
dot11PhyTxPowerTable = _Dot11PhyTxPowerTable_Object(
    (1, 2, 840, 10036, 4, 3)
)
if mibBuilder.loadTexts:
    dot11PhyTxPowerTable.setStatus("current")
_Dot11PhyTxPowerEntry_Object = MibTableRow
dot11PhyTxPowerEntry = _Dot11PhyTxPowerEntry_Object(
    (1, 2, 840, 10036, 4, 3, 1)
)
dot11PhyTxPowerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11PhyTxPowerEntry.setStatus("current")


class _Dot11NumberSupportedPowerLevels_Type(Integer32):
    """Custom type dot11NumberSupportedPowerLevels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Dot11NumberSupportedPowerLevels_Type.__name__ = "Integer32"
_Dot11NumberSupportedPowerLevels_Object = MibTableColumn
dot11NumberSupportedPowerLevels = _Dot11NumberSupportedPowerLevels_Object(
    (1, 2, 840, 10036, 4, 3, 1, 1),
    _Dot11NumberSupportedPowerLevels_Type()
)
dot11NumberSupportedPowerLevels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11NumberSupportedPowerLevels.setStatus("current")


class _Dot11TxPowerLevel1_Type(Integer32):
    """Custom type dot11TxPowerLevel1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_Dot11TxPowerLevel1_Type.__name__ = "Integer32"
_Dot11TxPowerLevel1_Object = MibTableColumn
dot11TxPowerLevel1 = _Dot11TxPowerLevel1_Object(
    (1, 2, 840, 10036, 4, 3, 1, 2),
    _Dot11TxPowerLevel1_Type()
)
dot11TxPowerLevel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TxPowerLevel1.setStatus("current")


class _Dot11TxPowerLevel2_Type(Integer32):
    """Custom type dot11TxPowerLevel2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_Dot11TxPowerLevel2_Type.__name__ = "Integer32"
_Dot11TxPowerLevel2_Object = MibTableColumn
dot11TxPowerLevel2 = _Dot11TxPowerLevel2_Object(
    (1, 2, 840, 10036, 4, 3, 1, 3),
    _Dot11TxPowerLevel2_Type()
)
dot11TxPowerLevel2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TxPowerLevel2.setStatus("current")


class _Dot11TxPowerLevel3_Type(Integer32):
    """Custom type dot11TxPowerLevel3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_Dot11TxPowerLevel3_Type.__name__ = "Integer32"
_Dot11TxPowerLevel3_Object = MibTableColumn
dot11TxPowerLevel3 = _Dot11TxPowerLevel3_Object(
    (1, 2, 840, 10036, 4, 3, 1, 4),
    _Dot11TxPowerLevel3_Type()
)
dot11TxPowerLevel3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TxPowerLevel3.setStatus("current")


class _Dot11TxPowerLevel4_Type(Integer32):
    """Custom type dot11TxPowerLevel4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_Dot11TxPowerLevel4_Type.__name__ = "Integer32"
_Dot11TxPowerLevel4_Object = MibTableColumn
dot11TxPowerLevel4 = _Dot11TxPowerLevel4_Object(
    (1, 2, 840, 10036, 4, 3, 1, 5),
    _Dot11TxPowerLevel4_Type()
)
dot11TxPowerLevel4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TxPowerLevel4.setStatus("current")


class _Dot11TxPowerLevel5_Type(Integer32):
    """Custom type dot11TxPowerLevel5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_Dot11TxPowerLevel5_Type.__name__ = "Integer32"
_Dot11TxPowerLevel5_Object = MibTableColumn
dot11TxPowerLevel5 = _Dot11TxPowerLevel5_Object(
    (1, 2, 840, 10036, 4, 3, 1, 6),
    _Dot11TxPowerLevel5_Type()
)
dot11TxPowerLevel5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TxPowerLevel5.setStatus("current")


class _Dot11TxPowerLevel6_Type(Integer32):
    """Custom type dot11TxPowerLevel6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_Dot11TxPowerLevel6_Type.__name__ = "Integer32"
_Dot11TxPowerLevel6_Object = MibTableColumn
dot11TxPowerLevel6 = _Dot11TxPowerLevel6_Object(
    (1, 2, 840, 10036, 4, 3, 1, 7),
    _Dot11TxPowerLevel6_Type()
)
dot11TxPowerLevel6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TxPowerLevel6.setStatus("current")


class _Dot11TxPowerLevel7_Type(Integer32):
    """Custom type dot11TxPowerLevel7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_Dot11TxPowerLevel7_Type.__name__ = "Integer32"
_Dot11TxPowerLevel7_Object = MibTableColumn
dot11TxPowerLevel7 = _Dot11TxPowerLevel7_Object(
    (1, 2, 840, 10036, 4, 3, 1, 8),
    _Dot11TxPowerLevel7_Type()
)
dot11TxPowerLevel7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TxPowerLevel7.setStatus("current")


class _Dot11TxPowerLevel8_Type(Integer32):
    """Custom type dot11TxPowerLevel8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_Dot11TxPowerLevel8_Type.__name__ = "Integer32"
_Dot11TxPowerLevel8_Object = MibTableColumn
dot11TxPowerLevel8 = _Dot11TxPowerLevel8_Object(
    (1, 2, 840, 10036, 4, 3, 1, 9),
    _Dot11TxPowerLevel8_Type()
)
dot11TxPowerLevel8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TxPowerLevel8.setStatus("current")


class _Dot11CurrentTxPowerLevel_Type(Integer32):
    """Custom type dot11CurrentTxPowerLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Dot11CurrentTxPowerLevel_Type.__name__ = "Integer32"
_Dot11CurrentTxPowerLevel_Object = MibTableColumn
dot11CurrentTxPowerLevel = _Dot11CurrentTxPowerLevel_Object(
    (1, 2, 840, 10036, 4, 3, 1, 10),
    _Dot11CurrentTxPowerLevel_Type()
)
dot11CurrentTxPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11CurrentTxPowerLevel.setStatus("current")
_Dot11PhyFHSSTable_Object = MibTable
dot11PhyFHSSTable = _Dot11PhyFHSSTable_Object(
    (1, 2, 840, 10036, 4, 4)
)
if mibBuilder.loadTexts:
    dot11PhyFHSSTable.setStatus("current")
_Dot11PhyFHSSEntry_Object = MibTableRow
dot11PhyFHSSEntry = _Dot11PhyFHSSEntry_Object(
    (1, 2, 840, 10036, 4, 4, 1)
)
dot11PhyFHSSEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11PhyFHSSEntry.setStatus("current")


class _Dot11HopTime_Type(Integer32):
    """Custom type dot11HopTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(224, 224),
    )


_Dot11HopTime_Type.__name__ = "Integer32"
_Dot11HopTime_Object = MibTableColumn
dot11HopTime = _Dot11HopTime_Object(
    (1, 2, 840, 10036, 4, 4, 1, 1),
    _Dot11HopTime_Type()
)
dot11HopTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11HopTime.setStatus("current")


class _Dot11CurrentChannelNumber_Type(Integer32):
    """Custom type dot11CurrentChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_Dot11CurrentChannelNumber_Type.__name__ = "Integer32"
_Dot11CurrentChannelNumber_Object = MibTableColumn
dot11CurrentChannelNumber = _Dot11CurrentChannelNumber_Object(
    (1, 2, 840, 10036, 4, 4, 1, 2),
    _Dot11CurrentChannelNumber_Type()
)
dot11CurrentChannelNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11CurrentChannelNumber.setStatus("current")


class _Dot11MaxDwellTime_Type(Integer32):
    """Custom type dot11MaxDwellTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot11MaxDwellTime_Type.__name__ = "Integer32"
_Dot11MaxDwellTime_Object = MibTableColumn
dot11MaxDwellTime = _Dot11MaxDwellTime_Object(
    (1, 2, 840, 10036, 4, 4, 1, 3),
    _Dot11MaxDwellTime_Type()
)
dot11MaxDwellTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11MaxDwellTime.setStatus("current")


class _Dot11CurrentDwellTime_Type(Integer32):
    """Custom type dot11CurrentDwellTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot11CurrentDwellTime_Type.__name__ = "Integer32"
_Dot11CurrentDwellTime_Object = MibTableColumn
dot11CurrentDwellTime = _Dot11CurrentDwellTime_Object(
    (1, 2, 840, 10036, 4, 4, 1, 4),
    _Dot11CurrentDwellTime_Type()
)
dot11CurrentDwellTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11CurrentDwellTime.setStatus("current")


class _Dot11CurrentSet_Type(Integer32):
    """Custom type dot11CurrentSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Dot11CurrentSet_Type.__name__ = "Integer32"
_Dot11CurrentSet_Object = MibTableColumn
dot11CurrentSet = _Dot11CurrentSet_Object(
    (1, 2, 840, 10036, 4, 4, 1, 5),
    _Dot11CurrentSet_Type()
)
dot11CurrentSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11CurrentSet.setStatus("current")


class _Dot11CurrentPattern_Type(Integer32):
    """Custom type dot11CurrentPattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Dot11CurrentPattern_Type.__name__ = "Integer32"
_Dot11CurrentPattern_Object = MibTableColumn
dot11CurrentPattern = _Dot11CurrentPattern_Object(
    (1, 2, 840, 10036, 4, 4, 1, 6),
    _Dot11CurrentPattern_Type()
)
dot11CurrentPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11CurrentPattern.setStatus("current")


class _Dot11CurrentIndex_Type(Integer32):
    """Custom type dot11CurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Dot11CurrentIndex_Type.__name__ = "Integer32"
_Dot11CurrentIndex_Object = MibTableColumn
dot11CurrentIndex = _Dot11CurrentIndex_Object(
    (1, 2, 840, 10036, 4, 4, 1, 7),
    _Dot11CurrentIndex_Type()
)
dot11CurrentIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11CurrentIndex.setStatus("current")
_Dot11EHCCPrimeRadix_Type = Integer32
_Dot11EHCCPrimeRadix_Object = MibTableColumn
dot11EHCCPrimeRadix = _Dot11EHCCPrimeRadix_Object(
    (1, 2, 840, 10036, 4, 4, 1, 8),
    _Dot11EHCCPrimeRadix_Type()
)
dot11EHCCPrimeRadix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11EHCCPrimeRadix.setStatus("current")
_Dot11EHCCNumberofChannelsFamilyIndex_Type = Integer32
_Dot11EHCCNumberofChannelsFamilyIndex_Object = MibTableColumn
dot11EHCCNumberofChannelsFamilyIndex = _Dot11EHCCNumberofChannelsFamilyIndex_Object(
    (1, 2, 840, 10036, 4, 4, 1, 9),
    _Dot11EHCCNumberofChannelsFamilyIndex_Type()
)
dot11EHCCNumberofChannelsFamilyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11EHCCNumberofChannelsFamilyIndex.setStatus("current")
_Dot11EHCCCapabilityImplemented_Type = TruthValue
_Dot11EHCCCapabilityImplemented_Object = MibTableColumn
dot11EHCCCapabilityImplemented = _Dot11EHCCCapabilityImplemented_Object(
    (1, 2, 840, 10036, 4, 4, 1, 10),
    _Dot11EHCCCapabilityImplemented_Type()
)
dot11EHCCCapabilityImplemented.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11EHCCCapabilityImplemented.setStatus("current")
_Dot11EHCCCapabilityEnabled_Type = TruthValue
_Dot11EHCCCapabilityEnabled_Object = MibTableColumn
dot11EHCCCapabilityEnabled = _Dot11EHCCCapabilityEnabled_Object(
    (1, 2, 840, 10036, 4, 4, 1, 11),
    _Dot11EHCCCapabilityEnabled_Type()
)
dot11EHCCCapabilityEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11EHCCCapabilityEnabled.setStatus("current")


class _Dot11HopAlgorithmAdopted_Type(Integer32):
    """Custom type dot11HopAlgorithmAdopted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("current", 0),
          ("hcc", 2),
          ("hop-index", 1))
    )


_Dot11HopAlgorithmAdopted_Type.__name__ = "Integer32"
_Dot11HopAlgorithmAdopted_Object = MibTableColumn
dot11HopAlgorithmAdopted = _Dot11HopAlgorithmAdopted_Object(
    (1, 2, 840, 10036, 4, 4, 1, 12),
    _Dot11HopAlgorithmAdopted_Type()
)
dot11HopAlgorithmAdopted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11HopAlgorithmAdopted.setStatus("current")
_Dot11RandomTableFlag_Type = TruthValue
_Dot11RandomTableFlag_Object = MibTableColumn
dot11RandomTableFlag = _Dot11RandomTableFlag_Object(
    (1, 2, 840, 10036, 4, 4, 1, 13),
    _Dot11RandomTableFlag_Type()
)
dot11RandomTableFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11RandomTableFlag.setStatus("current")
_Dot11NumberofHoppingSets_Type = Integer32
_Dot11NumberofHoppingSets_Object = MibTableColumn
dot11NumberofHoppingSets = _Dot11NumberofHoppingSets_Object(
    (1, 2, 840, 10036, 4, 4, 1, 14),
    _Dot11NumberofHoppingSets_Type()
)
dot11NumberofHoppingSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11NumberofHoppingSets.setStatus("current")
_Dot11HopModulus_Type = Integer32
_Dot11HopModulus_Object = MibTableColumn
dot11HopModulus = _Dot11HopModulus_Object(
    (1, 2, 840, 10036, 4, 4, 1, 15),
    _Dot11HopModulus_Type()
)
dot11HopModulus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11HopModulus.setStatus("current")
_Dot11HopOffset_Type = Integer32
_Dot11HopOffset_Object = MibTableColumn
dot11HopOffset = _Dot11HopOffset_Object(
    (1, 2, 840, 10036, 4, 4, 1, 16),
    _Dot11HopOffset_Type()
)
dot11HopOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11HopOffset.setStatus("current")
_Dot11PhyDSSSTable_Object = MibTable
dot11PhyDSSSTable = _Dot11PhyDSSSTable_Object(
    (1, 2, 840, 10036, 4, 5)
)
if mibBuilder.loadTexts:
    dot11PhyDSSSTable.setStatus("current")
_Dot11PhyDSSSEntry_Object = MibTableRow
dot11PhyDSSSEntry = _Dot11PhyDSSSEntry_Object(
    (1, 2, 840, 10036, 4, 5, 1)
)
dot11PhyDSSSEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11PhyDSSSEntry.setStatus("current")


class _Dot11CurrentChannel_Type(Integer32):
    """Custom type dot11CurrentChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_Dot11CurrentChannel_Type.__name__ = "Integer32"
_Dot11CurrentChannel_Object = MibTableColumn
dot11CurrentChannel = _Dot11CurrentChannel_Object(
    (1, 2, 840, 10036, 4, 5, 1, 1),
    _Dot11CurrentChannel_Type()
)
dot11CurrentChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11CurrentChannel.setStatus("current")


class _Dot11CCAModeSupported_Type(Integer32):
    """Custom type dot11CCAModeSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_Dot11CCAModeSupported_Type.__name__ = "Integer32"
_Dot11CCAModeSupported_Object = MibTableColumn
dot11CCAModeSupported = _Dot11CCAModeSupported_Object(
    (1, 2, 840, 10036, 4, 5, 1, 2),
    _Dot11CCAModeSupported_Type()
)
dot11CCAModeSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11CCAModeSupported.setStatus("current")


class _Dot11CurrentCCAMode_Type(Integer32):
    """Custom type dot11CurrentCCAMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("csonly", 2),
          ("cswithtimer", 8),
          ("edandcs", 4),
          ("edonly", 1),
          ("hrcsanded", 16))
    )


_Dot11CurrentCCAMode_Type.__name__ = "Integer32"
_Dot11CurrentCCAMode_Object = MibTableColumn
dot11CurrentCCAMode = _Dot11CurrentCCAMode_Object(
    (1, 2, 840, 10036, 4, 5, 1, 3),
    _Dot11CurrentCCAMode_Type()
)
dot11CurrentCCAMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11CurrentCCAMode.setStatus("current")
_Dot11EDThreshold_Type = Integer32
_Dot11EDThreshold_Object = MibTableColumn
dot11EDThreshold = _Dot11EDThreshold_Object(
    (1, 2, 840, 10036, 4, 5, 1, 4),
    _Dot11EDThreshold_Type()
)
dot11EDThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11EDThreshold.setStatus("current")
_Dot11PhyIRTable_Object = MibTable
dot11PhyIRTable = _Dot11PhyIRTable_Object(
    (1, 2, 840, 10036, 4, 6)
)
if mibBuilder.loadTexts:
    dot11PhyIRTable.setStatus("current")
_Dot11PhyIREntry_Object = MibTableRow
dot11PhyIREntry = _Dot11PhyIREntry_Object(
    (1, 2, 840, 10036, 4, 6, 1)
)
dot11PhyIREntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11PhyIREntry.setStatus("current")
_Dot11CCAWatchdogTimerMax_Type = Integer32
_Dot11CCAWatchdogTimerMax_Object = MibTableColumn
dot11CCAWatchdogTimerMax = _Dot11CCAWatchdogTimerMax_Object(
    (1, 2, 840, 10036, 4, 6, 1, 1),
    _Dot11CCAWatchdogTimerMax_Type()
)
dot11CCAWatchdogTimerMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11CCAWatchdogTimerMax.setStatus("current")
_Dot11CCAWatchdogCountMax_Type = Integer32
_Dot11CCAWatchdogCountMax_Object = MibTableColumn
dot11CCAWatchdogCountMax = _Dot11CCAWatchdogCountMax_Object(
    (1, 2, 840, 10036, 4, 6, 1, 2),
    _Dot11CCAWatchdogCountMax_Type()
)
dot11CCAWatchdogCountMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11CCAWatchdogCountMax.setStatus("current")
_Dot11CCAWatchdogTimerMin_Type = Integer32
_Dot11CCAWatchdogTimerMin_Object = MibTableColumn
dot11CCAWatchdogTimerMin = _Dot11CCAWatchdogTimerMin_Object(
    (1, 2, 840, 10036, 4, 6, 1, 3),
    _Dot11CCAWatchdogTimerMin_Type()
)
dot11CCAWatchdogTimerMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11CCAWatchdogTimerMin.setStatus("current")
_Dot11CCAWatchdogCountMin_Type = Integer32
_Dot11CCAWatchdogCountMin_Object = MibTableColumn
dot11CCAWatchdogCountMin = _Dot11CCAWatchdogCountMin_Object(
    (1, 2, 840, 10036, 4, 6, 1, 4),
    _Dot11CCAWatchdogCountMin_Type()
)
dot11CCAWatchdogCountMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11CCAWatchdogCountMin.setStatus("current")
_Dot11RegDomainsSupportedTable_Object = MibTable
dot11RegDomainsSupportedTable = _Dot11RegDomainsSupportedTable_Object(
    (1, 2, 840, 10036, 4, 7)
)
if mibBuilder.loadTexts:
    dot11RegDomainsSupportedTable.setStatus("current")
_Dot11RegDomainsSupportEntry_Object = MibTableRow
dot11RegDomainsSupportEntry = _Dot11RegDomainsSupportEntry_Object(
    (1, 2, 840, 10036, 4, 7, 1)
)
dot11RegDomainsSupportEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "IEEE802dot11-MIB", "dot11RegDomainsSupportIndex"),
)
if mibBuilder.loadTexts:
    dot11RegDomainsSupportEntry.setStatus("current")


class _Dot11RegDomainsSupportIndex_Type(Integer32):
    """Custom type dot11RegDomainsSupportIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dot11RegDomainsSupportIndex_Type.__name__ = "Integer32"
_Dot11RegDomainsSupportIndex_Object = MibTableColumn
dot11RegDomainsSupportIndex = _Dot11RegDomainsSupportIndex_Object(
    (1, 2, 840, 10036, 4, 7, 1, 1),
    _Dot11RegDomainsSupportIndex_Type()
)
dot11RegDomainsSupportIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RegDomainsSupportIndex.setStatus("current")


class _Dot11RegDomainsSupportValue_Type(Integer32):
    """Custom type dot11RegDomainsSupportValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              32,
              48,
              49,
              50,
              64)
        )
    )
    namedValues = NamedValues(
        *(("doc", 32),
          ("etsi", 48),
          ("fcc", 16),
          ("france", 50),
          ("mkk", 64),
          ("spain", 49))
    )


_Dot11RegDomainsSupportValue_Type.__name__ = "Integer32"
_Dot11RegDomainsSupportValue_Object = MibTableColumn
dot11RegDomainsSupportValue = _Dot11RegDomainsSupportValue_Object(
    (1, 2, 840, 10036, 4, 7, 1, 2),
    _Dot11RegDomainsSupportValue_Type()
)
dot11RegDomainsSupportValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RegDomainsSupportValue.setStatus("current")
_Dot11AntennasListTable_Object = MibTable
dot11AntennasListTable = _Dot11AntennasListTable_Object(
    (1, 2, 840, 10036, 4, 8)
)
if mibBuilder.loadTexts:
    dot11AntennasListTable.setStatus("current")
_Dot11AntennasListEntry_Object = MibTableRow
dot11AntennasListEntry = _Dot11AntennasListEntry_Object(
    (1, 2, 840, 10036, 4, 8, 1)
)
dot11AntennasListEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "IEEE802dot11-MIB", "dot11AntennaListIndex"),
)
if mibBuilder.loadTexts:
    dot11AntennasListEntry.setStatus("current")


class _Dot11AntennaListIndex_Type(Integer32):
    """Custom type dot11AntennaListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Dot11AntennaListIndex_Type.__name__ = "Integer32"
_Dot11AntennaListIndex_Object = MibTableColumn
dot11AntennaListIndex = _Dot11AntennaListIndex_Object(
    (1, 2, 840, 10036, 4, 8, 1, 1),
    _Dot11AntennaListIndex_Type()
)
dot11AntennaListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11AntennaListIndex.setStatus("current")
_Dot11SupportedTxAntenna_Type = TruthValue
_Dot11SupportedTxAntenna_Object = MibTableColumn
dot11SupportedTxAntenna = _Dot11SupportedTxAntenna_Object(
    (1, 2, 840, 10036, 4, 8, 1, 2),
    _Dot11SupportedTxAntenna_Type()
)
dot11SupportedTxAntenna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11SupportedTxAntenna.setStatus("current")
_Dot11SupportedRxAntenna_Type = TruthValue
_Dot11SupportedRxAntenna_Object = MibTableColumn
dot11SupportedRxAntenna = _Dot11SupportedRxAntenna_Object(
    (1, 2, 840, 10036, 4, 8, 1, 3),
    _Dot11SupportedRxAntenna_Type()
)
dot11SupportedRxAntenna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11SupportedRxAntenna.setStatus("current")
_Dot11DiversitySelectionRx_Type = TruthValue
_Dot11DiversitySelectionRx_Object = MibTableColumn
dot11DiversitySelectionRx = _Dot11DiversitySelectionRx_Object(
    (1, 2, 840, 10036, 4, 8, 1, 4),
    _Dot11DiversitySelectionRx_Type()
)
dot11DiversitySelectionRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11DiversitySelectionRx.setStatus("current")
_Dot11SupportedDataRatesTxTable_Object = MibTable
dot11SupportedDataRatesTxTable = _Dot11SupportedDataRatesTxTable_Object(
    (1, 2, 840, 10036, 4, 9)
)
if mibBuilder.loadTexts:
    dot11SupportedDataRatesTxTable.setStatus("current")
_Dot11SupportedDataRatesTxEntry_Object = MibTableRow
dot11SupportedDataRatesTxEntry = _Dot11SupportedDataRatesTxEntry_Object(
    (1, 2, 840, 10036, 4, 9, 1)
)
dot11SupportedDataRatesTxEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "IEEE802dot11-MIB", "dot11SupportedDataRatesTxIndex"),
)
if mibBuilder.loadTexts:
    dot11SupportedDataRatesTxEntry.setStatus("current")


class _Dot11SupportedDataRatesTxIndex_Type(Integer32):
    """Custom type dot11SupportedDataRatesTxIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Dot11SupportedDataRatesTxIndex_Type.__name__ = "Integer32"
_Dot11SupportedDataRatesTxIndex_Object = MibTableColumn
dot11SupportedDataRatesTxIndex = _Dot11SupportedDataRatesTxIndex_Object(
    (1, 2, 840, 10036, 4, 9, 1, 1),
    _Dot11SupportedDataRatesTxIndex_Type()
)
dot11SupportedDataRatesTxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11SupportedDataRatesTxIndex.setStatus("current")


class _Dot11SupportedDataRatesTxValue_Type(Integer32):
    """Custom type dot11SupportedDataRatesTxValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 127),
    )


_Dot11SupportedDataRatesTxValue_Type.__name__ = "Integer32"
_Dot11SupportedDataRatesTxValue_Object = MibTableColumn
dot11SupportedDataRatesTxValue = _Dot11SupportedDataRatesTxValue_Object(
    (1, 2, 840, 10036, 4, 9, 1, 2),
    _Dot11SupportedDataRatesTxValue_Type()
)
dot11SupportedDataRatesTxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11SupportedDataRatesTxValue.setStatus("current")
_Dot11SupportedDataRatesRxTable_Object = MibTable
dot11SupportedDataRatesRxTable = _Dot11SupportedDataRatesRxTable_Object(
    (1, 2, 840, 10036, 4, 10)
)
if mibBuilder.loadTexts:
    dot11SupportedDataRatesRxTable.setStatus("current")
_Dot11SupportedDataRatesRxEntry_Object = MibTableRow
dot11SupportedDataRatesRxEntry = _Dot11SupportedDataRatesRxEntry_Object(
    (1, 2, 840, 10036, 4, 10, 1)
)
dot11SupportedDataRatesRxEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "IEEE802dot11-MIB", "dot11SupportedDataRatesRxIndex"),
)
if mibBuilder.loadTexts:
    dot11SupportedDataRatesRxEntry.setStatus("current")


class _Dot11SupportedDataRatesRxIndex_Type(Integer32):
    """Custom type dot11SupportedDataRatesRxIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Dot11SupportedDataRatesRxIndex_Type.__name__ = "Integer32"
_Dot11SupportedDataRatesRxIndex_Object = MibTableColumn
dot11SupportedDataRatesRxIndex = _Dot11SupportedDataRatesRxIndex_Object(
    (1, 2, 840, 10036, 4, 10, 1, 1),
    _Dot11SupportedDataRatesRxIndex_Type()
)
dot11SupportedDataRatesRxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11SupportedDataRatesRxIndex.setStatus("current")


class _Dot11SupportedDataRatesRxValue_Type(Integer32):
    """Custom type dot11SupportedDataRatesRxValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 127),
    )


_Dot11SupportedDataRatesRxValue_Type.__name__ = "Integer32"
_Dot11SupportedDataRatesRxValue_Object = MibTableColumn
dot11SupportedDataRatesRxValue = _Dot11SupportedDataRatesRxValue_Object(
    (1, 2, 840, 10036, 4, 10, 1, 2),
    _Dot11SupportedDataRatesRxValue_Type()
)
dot11SupportedDataRatesRxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11SupportedDataRatesRxValue.setStatus("current")
_Dot11PhyOFDMTable_Object = MibTable
dot11PhyOFDMTable = _Dot11PhyOFDMTable_Object(
    (1, 2, 840, 10036, 4, 11)
)
if mibBuilder.loadTexts:
    dot11PhyOFDMTable.setStatus("current")
_Dot11PhyOFDMEntry_Object = MibTableRow
dot11PhyOFDMEntry = _Dot11PhyOFDMEntry_Object(
    (1, 2, 840, 10036, 4, 11, 1)
)
dot11PhyOFDMEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11PhyOFDMEntry.setStatus("current")


class _Dot11CurrentFrequency_Type(Integer32):
    """Custom type dot11CurrentFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Dot11CurrentFrequency_Type.__name__ = "Integer32"
_Dot11CurrentFrequency_Object = MibTableColumn
dot11CurrentFrequency = _Dot11CurrentFrequency_Object(
    (1, 2, 840, 10036, 4, 11, 1, 1),
    _Dot11CurrentFrequency_Type()
)
dot11CurrentFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11CurrentFrequency.setStatus("current")
_Dot11TIThreshold_Type = Integer32
_Dot11TIThreshold_Object = MibTableColumn
dot11TIThreshold = _Dot11TIThreshold_Object(
    (1, 2, 840, 10036, 4, 11, 1, 2),
    _Dot11TIThreshold_Type()
)
dot11TIThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11TIThreshold.setStatus("current")


class _Dot11FrequencyBandsSupported_Type(Integer32):
    """Custom type dot11FrequencyBandsSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_Dot11FrequencyBandsSupported_Type.__name__ = "Integer32"
_Dot11FrequencyBandsSupported_Object = MibTableColumn
dot11FrequencyBandsSupported = _Dot11FrequencyBandsSupported_Object(
    (1, 2, 840, 10036, 4, 11, 1, 3),
    _Dot11FrequencyBandsSupported_Type()
)
dot11FrequencyBandsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11FrequencyBandsSupported.setStatus("current")
_Dot11PhyHRDSSSTable_Object = MibTable
dot11PhyHRDSSSTable = _Dot11PhyHRDSSSTable_Object(
    (1, 2, 840, 10036, 4, 12)
)
if mibBuilder.loadTexts:
    dot11PhyHRDSSSTable.setStatus("current")
_Dot11PhyHRDSSSEntry_Object = MibTableRow
dot11PhyHRDSSSEntry = _Dot11PhyHRDSSSEntry_Object(
    (1, 2, 840, 10036, 4, 12, 1)
)
dot11PhyHRDSSSEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11PhyHRDSSSEntry.setStatus("current")
_Dot11ChannelAgilityPresent_Type = TruthValue
_Dot11ChannelAgilityPresent_Object = MibTableColumn
dot11ChannelAgilityPresent = _Dot11ChannelAgilityPresent_Object(
    (1, 2, 840, 10036, 4, 12, 1, 3),
    _Dot11ChannelAgilityPresent_Type()
)
dot11ChannelAgilityPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ChannelAgilityPresent.setStatus("current")
_Dot11ChannelAgilityEnabled_Type = TruthValue
_Dot11ChannelAgilityEnabled_Object = MibTableColumn
dot11ChannelAgilityEnabled = _Dot11ChannelAgilityEnabled_Object(
    (1, 2, 840, 10036, 4, 12, 1, 4),
    _Dot11ChannelAgilityEnabled_Type()
)
dot11ChannelAgilityEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ChannelAgilityEnabled.setStatus("current")


class _Dot11HRCCAModeSupported_Type(Integer32):
    """Custom type dot11HRCCAModeSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_Dot11HRCCAModeSupported_Type.__name__ = "Integer32"
_Dot11HRCCAModeSupported_Object = MibTableColumn
dot11HRCCAModeSupported = _Dot11HRCCAModeSupported_Object(
    (1, 2, 840, 10036, 4, 12, 1, 5),
    _Dot11HRCCAModeSupported_Type()
)
dot11HRCCAModeSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11HRCCAModeSupported.setStatus("current")
_Dot11ShortPreambleOptionImplemented_Type = TruthValue
_Dot11ShortPreambleOptionImplemented_Object = MibTableColumn
dot11ShortPreambleOptionImplemented = _Dot11ShortPreambleOptionImplemented_Object(
    (1, 2, 840, 10036, 4, 12, 1, 16),
    _Dot11ShortPreambleOptionImplemented_Type()
)
dot11ShortPreambleOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ShortPreambleOptionImplemented.setStatus("current")
_Dot11PBCCOptionImplemented_Type = TruthValue
_Dot11PBCCOptionImplemented_Object = MibTableColumn
dot11PBCCOptionImplemented = _Dot11PBCCOptionImplemented_Object(
    (1, 2, 840, 10036, 4, 12, 1, 27),
    _Dot11PBCCOptionImplemented_Type()
)
dot11PBCCOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11PBCCOptionImplemented.setStatus("current")
_Dot11HoppingPatternTable_Object = MibTable
dot11HoppingPatternTable = _Dot11HoppingPatternTable_Object(
    (1, 2, 840, 10036, 4, 13)
)
if mibBuilder.loadTexts:
    dot11HoppingPatternTable.setStatus("current")
_Dot11HoppingPatternEntry_Object = MibTableRow
dot11HoppingPatternEntry = _Dot11HoppingPatternEntry_Object(
    (1, 2, 840, 10036, 4, 13, 1)
)
dot11HoppingPatternEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "IEEE802dot11-MIB", "dot11HoppingPatternIndex"),
)
if mibBuilder.loadTexts:
    dot11HoppingPatternEntry.setStatus("current")


class _Dot11HoppingPatternIndex_Type(Integer32):
    """Custom type dot11HoppingPatternIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dot11HoppingPatternIndex_Type.__name__ = "Integer32"
_Dot11HoppingPatternIndex_Object = MibTableColumn
dot11HoppingPatternIndex = _Dot11HoppingPatternIndex_Object(
    (1, 2, 840, 10036, 4, 13, 1, 1),
    _Dot11HoppingPatternIndex_Type()
)
dot11HoppingPatternIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11HoppingPatternIndex.setStatus("current")
_Dot11RandomTableFieldNumber_Type = Integer32
_Dot11RandomTableFieldNumber_Object = MibTableColumn
dot11RandomTableFieldNumber = _Dot11RandomTableFieldNumber_Object(
    (1, 2, 840, 10036, 4, 13, 1, 2),
    _Dot11RandomTableFieldNumber_Type()
)
dot11RandomTableFieldNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11RandomTableFieldNumber.setStatus("current")
_Dot11PhyERPTable_Object = MibTable
dot11PhyERPTable = _Dot11PhyERPTable_Object(
    (1, 2, 840, 10036, 4, 14)
)
if mibBuilder.loadTexts:
    dot11PhyERPTable.setStatus("current")
_Dot11PhyERPEntry_Object = MibTableRow
dot11PhyERPEntry = _Dot11PhyERPEntry_Object(
    (1, 2, 840, 10036, 4, 14, 1)
)
dot11PhyERPEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11PhyERPEntry.setStatus("current")
_Dot11ERPPBCCOptionImplemented_Type = TruthValue
_Dot11ERPPBCCOptionImplemented_Object = MibTableColumn
dot11ERPPBCCOptionImplemented = _Dot11ERPPBCCOptionImplemented_Object(
    (1, 2, 840, 10036, 4, 14, 1, 1),
    _Dot11ERPPBCCOptionImplemented_Type()
)
dot11ERPPBCCOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ERPPBCCOptionImplemented.setStatus("current")
_Dot11ERPBCCOptionEnabled_Type = TruthValue
_Dot11ERPBCCOptionEnabled_Object = MibTableColumn
dot11ERPBCCOptionEnabled = _Dot11ERPBCCOptionEnabled_Object(
    (1, 2, 840, 10036, 4, 14, 1, 2),
    _Dot11ERPBCCOptionEnabled_Type()
)
dot11ERPBCCOptionEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ERPBCCOptionEnabled.setStatus("current")
_Dot11DSSSOFDMOptionImplemented_Type = TruthValue
_Dot11DSSSOFDMOptionImplemented_Object = MibTableColumn
dot11DSSSOFDMOptionImplemented = _Dot11DSSSOFDMOptionImplemented_Object(
    (1, 2, 840, 10036, 4, 14, 1, 3),
    _Dot11DSSSOFDMOptionImplemented_Type()
)
dot11DSSSOFDMOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11DSSSOFDMOptionImplemented.setStatus("current")
_Dot11DSSSOFDMOptionEnabled_Type = TruthValue
_Dot11DSSSOFDMOptionEnabled_Object = MibTableColumn
dot11DSSSOFDMOptionEnabled = _Dot11DSSSOFDMOptionEnabled_Object(
    (1, 2, 840, 10036, 4, 14, 1, 4),
    _Dot11DSSSOFDMOptionEnabled_Type()
)
dot11DSSSOFDMOptionEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11DSSSOFDMOptionEnabled.setStatus("current")
_Dot11ShortSlotTimeOptionImplemented_Type = TruthValue
_Dot11ShortSlotTimeOptionImplemented_Object = MibTableColumn
dot11ShortSlotTimeOptionImplemented = _Dot11ShortSlotTimeOptionImplemented_Object(
    (1, 2, 840, 10036, 4, 14, 1, 5),
    _Dot11ShortSlotTimeOptionImplemented_Type()
)
dot11ShortSlotTimeOptionImplemented.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ShortSlotTimeOptionImplemented.setStatus("current")
_Dot11ShortSlotTimeOptionEnabled_Type = TruthValue
_Dot11ShortSlotTimeOptionEnabled_Object = MibTableColumn
dot11ShortSlotTimeOptionEnabled = _Dot11ShortSlotTimeOptionEnabled_Object(
    (1, 2, 840, 10036, 4, 14, 1, 6),
    _Dot11ShortSlotTimeOptionEnabled_Type()
)
dot11ShortSlotTimeOptionEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ShortSlotTimeOptionEnabled.setStatus("current")
_Dot11PhyHTTable_Object = MibTable
dot11PhyHTTable = _Dot11PhyHTTable_Object(
    (1, 2, 840, 10036, 4, 15)
)
if mibBuilder.loadTexts:
    dot11PhyHTTable.setStatus("current")
_Dot11PhyHTEntry_Object = MibTableRow
dot11PhyHTEntry = _Dot11PhyHTEntry_Object(
    (1, 2, 840, 10036, 4, 15, 1)
)
dot11PhyHTEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11PhyHTEntry.setStatus("current")


class _Dot11FortyMHzOperationImplemented_Type(TruthValue):
    """Custom type dot11FortyMHzOperationImplemented based on TruthValue"""


_Dot11FortyMHzOperationImplemented_Object = MibTableColumn
dot11FortyMHzOperationImplemented = _Dot11FortyMHzOperationImplemented_Object(
    (1, 2, 840, 10036, 4, 15, 1, 1),
    _Dot11FortyMHzOperationImplemented_Type()
)
dot11FortyMHzOperationImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11FortyMHzOperationImplemented.setStatus("current")


class _Dot11FortyMHzOperationEnabled_Type(TruthValue):
    """Custom type dot11FortyMHzOperationEnabled based on TruthValue"""


_Dot11FortyMHzOperationEnabled_Object = MibTableColumn
dot11FortyMHzOperationEnabled = _Dot11FortyMHzOperationEnabled_Object(
    (1, 2, 840, 10036, 4, 15, 1, 2),
    _Dot11FortyMHzOperationEnabled_Type()
)
dot11FortyMHzOperationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11FortyMHzOperationEnabled.setStatus("current")
_Dot11CurrentPrimaryChannel_Type = Integer32
_Dot11CurrentPrimaryChannel_Object = MibTableColumn
dot11CurrentPrimaryChannel = _Dot11CurrentPrimaryChannel_Object(
    (1, 2, 840, 10036, 4, 15, 1, 3),
    _Dot11CurrentPrimaryChannel_Type()
)
dot11CurrentPrimaryChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11CurrentPrimaryChannel.setStatus("current")
_Dot11CurrentSecondaryChannel_Type = Integer32
_Dot11CurrentSecondaryChannel_Object = MibTableColumn
dot11CurrentSecondaryChannel = _Dot11CurrentSecondaryChannel_Object(
    (1, 2, 840, 10036, 4, 15, 1, 4),
    _Dot11CurrentSecondaryChannel_Type()
)
dot11CurrentSecondaryChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11CurrentSecondaryChannel.setStatus("current")


class _Dot11NumberOfSpatialStreamsImplemented_Type(Integer32):
    """Custom type dot11NumberOfSpatialStreamsImplemented based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Dot11NumberOfSpatialStreamsImplemented_Type.__name__ = "Integer32"
_Dot11NumberOfSpatialStreamsImplemented_Object = MibTableColumn
dot11NumberOfSpatialStreamsImplemented = _Dot11NumberOfSpatialStreamsImplemented_Object(
    (1, 2, 840, 10036, 4, 15, 1, 5),
    _Dot11NumberOfSpatialStreamsImplemented_Type()
)
dot11NumberOfSpatialStreamsImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11NumberOfSpatialStreamsImplemented.setStatus("current")


class _Dot11NumberOfSpatialStreamsEnabled_Type(Integer32):
    """Custom type dot11NumberOfSpatialStreamsEnabled based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Dot11NumberOfSpatialStreamsEnabled_Type.__name__ = "Integer32"
_Dot11NumberOfSpatialStreamsEnabled_Object = MibTableColumn
dot11NumberOfSpatialStreamsEnabled = _Dot11NumberOfSpatialStreamsEnabled_Object(
    (1, 2, 840, 10036, 4, 15, 1, 6),
    _Dot11NumberOfSpatialStreamsEnabled_Type()
)
dot11NumberOfSpatialStreamsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11NumberOfSpatialStreamsEnabled.setStatus("current")


class _Dot11GreenfieldOptionImplemented_Type(TruthValue):
    """Custom type dot11GreenfieldOptionImplemented based on TruthValue"""


_Dot11GreenfieldOptionImplemented_Object = MibTableColumn
dot11GreenfieldOptionImplemented = _Dot11GreenfieldOptionImplemented_Object(
    (1, 2, 840, 10036, 4, 15, 1, 7),
    _Dot11GreenfieldOptionImplemented_Type()
)
dot11GreenfieldOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11GreenfieldOptionImplemented.setStatus("current")


class _Dot11GreenfieldOptionEnabled_Type(TruthValue):
    """Custom type dot11GreenfieldOptionEnabled based on TruthValue"""


_Dot11GreenfieldOptionEnabled_Object = MibTableColumn
dot11GreenfieldOptionEnabled = _Dot11GreenfieldOptionEnabled_Object(
    (1, 2, 840, 10036, 4, 15, 1, 8),
    _Dot11GreenfieldOptionEnabled_Type()
)
dot11GreenfieldOptionEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11GreenfieldOptionEnabled.setStatus("current")


class _Dot11ShortGIOptionInTwentyImplemented_Type(TruthValue):
    """Custom type dot11ShortGIOptionInTwentyImplemented based on TruthValue"""


_Dot11ShortGIOptionInTwentyImplemented_Object = MibTableColumn
dot11ShortGIOptionInTwentyImplemented = _Dot11ShortGIOptionInTwentyImplemented_Object(
    (1, 2, 840, 10036, 4, 15, 1, 9),
    _Dot11ShortGIOptionInTwentyImplemented_Type()
)
dot11ShortGIOptionInTwentyImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ShortGIOptionInTwentyImplemented.setStatus("current")


class _Dot11ShortGIOptionInTwentyEnabled_Type(TruthValue):
    """Custom type dot11ShortGIOptionInTwentyEnabled based on TruthValue"""


_Dot11ShortGIOptionInTwentyEnabled_Object = MibTableColumn
dot11ShortGIOptionInTwentyEnabled = _Dot11ShortGIOptionInTwentyEnabled_Object(
    (1, 2, 840, 10036, 4, 15, 1, 10),
    _Dot11ShortGIOptionInTwentyEnabled_Type()
)
dot11ShortGIOptionInTwentyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ShortGIOptionInTwentyEnabled.setStatus("current")


class _Dot11ShortGIOptionInFortyImplemented_Type(TruthValue):
    """Custom type dot11ShortGIOptionInFortyImplemented based on TruthValue"""


_Dot11ShortGIOptionInFortyImplemented_Object = MibTableColumn
dot11ShortGIOptionInFortyImplemented = _Dot11ShortGIOptionInFortyImplemented_Object(
    (1, 2, 840, 10036, 4, 15, 1, 11),
    _Dot11ShortGIOptionInFortyImplemented_Type()
)
dot11ShortGIOptionInFortyImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ShortGIOptionInFortyImplemented.setStatus("current")


class _Dot11ShortGIOptionInFortyEnabled_Type(TruthValue):
    """Custom type dot11ShortGIOptionInFortyEnabled based on TruthValue"""


_Dot11ShortGIOptionInFortyEnabled_Object = MibTableColumn
dot11ShortGIOptionInFortyEnabled = _Dot11ShortGIOptionInFortyEnabled_Object(
    (1, 2, 840, 10036, 4, 15, 1, 12),
    _Dot11ShortGIOptionInFortyEnabled_Type()
)
dot11ShortGIOptionInFortyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ShortGIOptionInFortyEnabled.setStatus("current")


class _Dot11LDPCCodingOptionImplemented_Type(TruthValue):
    """Custom type dot11LDPCCodingOptionImplemented based on TruthValue"""


_Dot11LDPCCodingOptionImplemented_Object = MibTableColumn
dot11LDPCCodingOptionImplemented = _Dot11LDPCCodingOptionImplemented_Object(
    (1, 2, 840, 10036, 4, 15, 1, 13),
    _Dot11LDPCCodingOptionImplemented_Type()
)
dot11LDPCCodingOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11LDPCCodingOptionImplemented.setStatus("current")


class _Dot11LDPCCodingOptionEnabled_Type(TruthValue):
    """Custom type dot11LDPCCodingOptionEnabled based on TruthValue"""


_Dot11LDPCCodingOptionEnabled_Object = MibTableColumn
dot11LDPCCodingOptionEnabled = _Dot11LDPCCodingOptionEnabled_Object(
    (1, 2, 840, 10036, 4, 15, 1, 14),
    _Dot11LDPCCodingOptionEnabled_Type()
)
dot11LDPCCodingOptionEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11LDPCCodingOptionEnabled.setStatus("current")


class _Dot11TxSTBCOptionImplemented_Type(TruthValue):
    """Custom type dot11TxSTBCOptionImplemented based on TruthValue"""


_Dot11TxSTBCOptionImplemented_Object = MibTableColumn
dot11TxSTBCOptionImplemented = _Dot11TxSTBCOptionImplemented_Object(
    (1, 2, 840, 10036, 4, 15, 1, 15),
    _Dot11TxSTBCOptionImplemented_Type()
)
dot11TxSTBCOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TxSTBCOptionImplemented.setStatus("current")


class _Dot11TxSTBCOptionEnabled_Type(TruthValue):
    """Custom type dot11TxSTBCOptionEnabled based on TruthValue"""


_Dot11TxSTBCOptionEnabled_Object = MibTableColumn
dot11TxSTBCOptionEnabled = _Dot11TxSTBCOptionEnabled_Object(
    (1, 2, 840, 10036, 4, 15, 1, 16),
    _Dot11TxSTBCOptionEnabled_Type()
)
dot11TxSTBCOptionEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11TxSTBCOptionEnabled.setStatus("current")


class _Dot11RxSTBCOptionImplemented_Type(TruthValue):
    """Custom type dot11RxSTBCOptionImplemented based on TruthValue"""


_Dot11RxSTBCOptionImplemented_Object = MibTableColumn
dot11RxSTBCOptionImplemented = _Dot11RxSTBCOptionImplemented_Object(
    (1, 2, 840, 10036, 4, 15, 1, 17),
    _Dot11RxSTBCOptionImplemented_Type()
)
dot11RxSTBCOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RxSTBCOptionImplemented.setStatus("current")


class _Dot11RxSTBCOptionEnabled_Type(TruthValue):
    """Custom type dot11RxSTBCOptionEnabled based on TruthValue"""


_Dot11RxSTBCOptionEnabled_Object = MibTableColumn
dot11RxSTBCOptionEnabled = _Dot11RxSTBCOptionEnabled_Object(
    (1, 2, 840, 10036, 4, 15, 1, 18),
    _Dot11RxSTBCOptionEnabled_Type()
)
dot11RxSTBCOptionEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11RxSTBCOptionEnabled.setStatus("current")


class _Dot11BeamFormingOptionImplemented_Type(TruthValue):
    """Custom type dot11BeamFormingOptionImplemented based on TruthValue"""


_Dot11BeamFormingOptionImplemented_Object = MibTableColumn
dot11BeamFormingOptionImplemented = _Dot11BeamFormingOptionImplemented_Object(
    (1, 2, 840, 10036, 4, 15, 1, 19),
    _Dot11BeamFormingOptionImplemented_Type()
)
dot11BeamFormingOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11BeamFormingOptionImplemented.setStatus("current")


class _Dot11BeamFormingOptionEnabled_Type(TruthValue):
    """Custom type dot11BeamFormingOptionEnabled based on TruthValue"""


_Dot11BeamFormingOptionEnabled_Object = MibTableColumn
dot11BeamFormingOptionEnabled = _Dot11BeamFormingOptionEnabled_Object(
    (1, 2, 840, 10036, 4, 15, 1, 20),
    _Dot11BeamFormingOptionEnabled_Type()
)
dot11BeamFormingOptionEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11BeamFormingOptionEnabled.setStatus("current")


class _Dot11HighestSupportedDataRate_Type(Integer32):
    """Custom type dot11HighestSupportedDataRate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_Dot11HighestSupportedDataRate_Type.__name__ = "Integer32"
_Dot11HighestSupportedDataRate_Object = MibTableColumn
dot11HighestSupportedDataRate = _Dot11HighestSupportedDataRate_Object(
    (1, 2, 840, 10036, 4, 15, 1, 21),
    _Dot11HighestSupportedDataRate_Type()
)
dot11HighestSupportedDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11HighestSupportedDataRate.setStatus("current")


class _Dot11TxMCSSetDefined_Type(TruthValue):
    """Custom type dot11TxMCSSetDefined based on TruthValue"""


_Dot11TxMCSSetDefined_Object = MibTableColumn
dot11TxMCSSetDefined = _Dot11TxMCSSetDefined_Object(
    (1, 2, 840, 10036, 4, 15, 1, 22),
    _Dot11TxMCSSetDefined_Type()
)
dot11TxMCSSetDefined.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11TxMCSSetDefined.setStatus("current")


class _Dot11TxRxMCSSetNotEqual_Type(TruthValue):
    """Custom type dot11TxRxMCSSetNotEqual based on TruthValue"""


_Dot11TxRxMCSSetNotEqual_Object = MibTableColumn
dot11TxRxMCSSetNotEqual = _Dot11TxRxMCSSetNotEqual_Object(
    (1, 2, 840, 10036, 4, 15, 1, 23),
    _Dot11TxRxMCSSetNotEqual_Type()
)
dot11TxRxMCSSetNotEqual.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11TxRxMCSSetNotEqual.setStatus("current")


class _Dot11TxMaximumNumberSpatialStreamsSupported_Type(Integer32):
    """Custom type dot11TxMaximumNumberSpatialStreamsSupported based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Dot11TxMaximumNumberSpatialStreamsSupported_Type.__name__ = "Integer32"
_Dot11TxMaximumNumberSpatialStreamsSupported_Object = MibTableColumn
dot11TxMaximumNumberSpatialStreamsSupported = _Dot11TxMaximumNumberSpatialStreamsSupported_Object(
    (1, 2, 840, 10036, 4, 15, 1, 24),
    _Dot11TxMaximumNumberSpatialStreamsSupported_Type()
)
dot11TxMaximumNumberSpatialStreamsSupported.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11TxMaximumNumberSpatialStreamsSupported.setStatus("current")


class _Dot11TxUnequalModulationSupported_Type(TruthValue):
    """Custom type dot11TxUnequalModulationSupported based on TruthValue"""


_Dot11TxUnequalModulationSupported_Object = MibTableColumn
dot11TxUnequalModulationSupported = _Dot11TxUnequalModulationSupported_Object(
    (1, 2, 840, 10036, 4, 15, 1, 25),
    _Dot11TxUnequalModulationSupported_Type()
)
dot11TxUnequalModulationSupported.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11TxUnequalModulationSupported.setStatus("current")
_Dot11SupportedMCSTxTable_Object = MibTable
dot11SupportedMCSTxTable = _Dot11SupportedMCSTxTable_Object(
    (1, 2, 840, 10036, 4, 16)
)
if mibBuilder.loadTexts:
    dot11SupportedMCSTxTable.setStatus("current")
_Dot11SupportedMCSTxEntry_Object = MibTableRow
dot11SupportedMCSTxEntry = _Dot11SupportedMCSTxEntry_Object(
    (1, 2, 840, 10036, 4, 16, 1)
)
dot11SupportedMCSTxEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "IEEE802dot11-MIB", "dot11SupportedMCSTxIndex"),
)
if mibBuilder.loadTexts:
    dot11SupportedMCSTxEntry.setStatus("current")


class _Dot11SupportedMCSTxIndex_Type(Integer32):
    """Custom type dot11SupportedMCSTxIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Dot11SupportedMCSTxIndex_Type.__name__ = "Integer32"
_Dot11SupportedMCSTxIndex_Object = MibTableColumn
dot11SupportedMCSTxIndex = _Dot11SupportedMCSTxIndex_Object(
    (1, 2, 840, 10036, 4, 16, 1, 1),
    _Dot11SupportedMCSTxIndex_Type()
)
dot11SupportedMCSTxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11SupportedMCSTxIndex.setStatus("current")


class _Dot11SupportedMCSTxValue_Type(Integer32):
    """Custom type dot11SupportedMCSTxValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_Dot11SupportedMCSTxValue_Type.__name__ = "Integer32"
_Dot11SupportedMCSTxValue_Object = MibTableColumn
dot11SupportedMCSTxValue = _Dot11SupportedMCSTxValue_Object(
    (1, 2, 840, 10036, 4, 16, 1, 2),
    _Dot11SupportedMCSTxValue_Type()
)
dot11SupportedMCSTxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11SupportedMCSTxValue.setStatus("current")
_Dot11SupportedMCSRxTable_Object = MibTable
dot11SupportedMCSRxTable = _Dot11SupportedMCSRxTable_Object(
    (1, 2, 840, 10036, 4, 17)
)
if mibBuilder.loadTexts:
    dot11SupportedMCSRxTable.setStatus("current")
_Dot11SupportedMCSRxEntry_Object = MibTableRow
dot11SupportedMCSRxEntry = _Dot11SupportedMCSRxEntry_Object(
    (1, 2, 840, 10036, 4, 17, 1)
)
dot11SupportedMCSRxEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "IEEE802dot11-MIB", "dot11SupportedMCSRxIndex"),
)
if mibBuilder.loadTexts:
    dot11SupportedMCSRxEntry.setStatus("current")


class _Dot11SupportedMCSRxIndex_Type(Integer32):
    """Custom type dot11SupportedMCSRxIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Dot11SupportedMCSRxIndex_Type.__name__ = "Integer32"
_Dot11SupportedMCSRxIndex_Object = MibTableColumn
dot11SupportedMCSRxIndex = _Dot11SupportedMCSRxIndex_Object(
    (1, 2, 840, 10036, 4, 17, 1, 1),
    _Dot11SupportedMCSRxIndex_Type()
)
dot11SupportedMCSRxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11SupportedMCSRxIndex.setStatus("current")


class _Dot11SupportedMCSRxValue_Type(Integer32):
    """Custom type dot11SupportedMCSRxValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_Dot11SupportedMCSRxValue_Type.__name__ = "Integer32"
_Dot11SupportedMCSRxValue_Object = MibTableColumn
dot11SupportedMCSRxValue = _Dot11SupportedMCSRxValue_Object(
    (1, 2, 840, 10036, 4, 17, 1, 2),
    _Dot11SupportedMCSRxValue_Type()
)
dot11SupportedMCSRxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11SupportedMCSRxValue.setStatus("current")
_Dot11TxBFConfigTable_Object = MibTable
dot11TxBFConfigTable = _Dot11TxBFConfigTable_Object(
    (1, 2, 840, 10036, 4, 18)
)
if mibBuilder.loadTexts:
    dot11TxBFConfigTable.setStatus("current")
_Dot11TxBFConfigEntry_Object = MibTableRow
dot11TxBFConfigEntry = _Dot11TxBFConfigEntry_Object(
    (1, 2, 840, 10036, 4, 18, 1)
)
dot11TxBFConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11TxBFConfigEntry.setStatus("current")


class _Dot11ReceiveStaggerSoundingOptionImplemented_Type(TruthValue):
    """Custom type dot11ReceiveStaggerSoundingOptionImplemented based on TruthValue"""


_Dot11ReceiveStaggerSoundingOptionImplemented_Object = MibTableColumn
dot11ReceiveStaggerSoundingOptionImplemented = _Dot11ReceiveStaggerSoundingOptionImplemented_Object(
    (1, 2, 840, 10036, 4, 18, 1, 1),
    _Dot11ReceiveStaggerSoundingOptionImplemented_Type()
)
dot11ReceiveStaggerSoundingOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ReceiveStaggerSoundingOptionImplemented.setStatus("current")


class _Dot11TransmitStaggerSoundingOptionImplemented_Type(TruthValue):
    """Custom type dot11TransmitStaggerSoundingOptionImplemented based on TruthValue"""


_Dot11TransmitStaggerSoundingOptionImplemented_Object = MibTableColumn
dot11TransmitStaggerSoundingOptionImplemented = _Dot11TransmitStaggerSoundingOptionImplemented_Object(
    (1, 2, 840, 10036, 4, 18, 1, 2),
    _Dot11TransmitStaggerSoundingOptionImplemented_Type()
)
dot11TransmitStaggerSoundingOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TransmitStaggerSoundingOptionImplemented.setStatus("current")


class _Dot11ReceiveNDPOptionImplemented_Type(TruthValue):
    """Custom type dot11ReceiveNDPOptionImplemented based on TruthValue"""


_Dot11ReceiveNDPOptionImplemented_Object = MibTableColumn
dot11ReceiveNDPOptionImplemented = _Dot11ReceiveNDPOptionImplemented_Object(
    (1, 2, 840, 10036, 4, 18, 1, 3),
    _Dot11ReceiveNDPOptionImplemented_Type()
)
dot11ReceiveNDPOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ReceiveNDPOptionImplemented.setStatus("current")


class _Dot11TransmitNDPOptionImplemented_Type(TruthValue):
    """Custom type dot11TransmitNDPOptionImplemented based on TruthValue"""


_Dot11TransmitNDPOptionImplemented_Object = MibTableColumn
dot11TransmitNDPOptionImplemented = _Dot11TransmitNDPOptionImplemented_Object(
    (1, 2, 840, 10036, 4, 18, 1, 4),
    _Dot11TransmitNDPOptionImplemented_Type()
)
dot11TransmitNDPOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TransmitNDPOptionImplemented.setStatus("current")


class _Dot11ImplicitTxBFOptionImplemented_Type(TruthValue):
    """Custom type dot11ImplicitTxBFOptionImplemented based on TruthValue"""


_Dot11ImplicitTxBFOptionImplemented_Object = MibTableColumn
dot11ImplicitTxBFOptionImplemented = _Dot11ImplicitTxBFOptionImplemented_Object(
    (1, 2, 840, 10036, 4, 18, 1, 5),
    _Dot11ImplicitTxBFOptionImplemented_Type()
)
dot11ImplicitTxBFOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ImplicitTxBFOptionImplemented.setStatus("current")


class _Dot11CalibrationOptionImplemented_Type(Integer32):
    """Custom type dot11CalibrationOptionImplemented based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ableToInitiate", 2),
          ("fullyCapable", 3),
          ("inCapable", 0),
          ("unableToInitiate", 1))
    )


_Dot11CalibrationOptionImplemented_Type.__name__ = "Integer32"
_Dot11CalibrationOptionImplemented_Object = MibTableColumn
dot11CalibrationOptionImplemented = _Dot11CalibrationOptionImplemented_Object(
    (1, 2, 840, 10036, 4, 18, 1, 6),
    _Dot11CalibrationOptionImplemented_Type()
)
dot11CalibrationOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11CalibrationOptionImplemented.setStatus("current")


class _Dot11ExplicitCSITxBFOptionImplemented_Type(TruthValue):
    """Custom type dot11ExplicitCSITxBFOptionImplemented based on TruthValue"""


_Dot11ExplicitCSITxBFOptionImplemented_Object = MibTableColumn
dot11ExplicitCSITxBFOptionImplemented = _Dot11ExplicitCSITxBFOptionImplemented_Object(
    (1, 2, 840, 10036, 4, 18, 1, 7),
    _Dot11ExplicitCSITxBFOptionImplemented_Type()
)
dot11ExplicitCSITxBFOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ExplicitCSITxBFOptionImplemented.setStatus("current")


class _Dot11ExplicitNonCompressedbeamformingMatrixOptionImplemented_Type(TruthValue):
    """Custom type dot11ExplicitNonCompressedbeamformingMatrixOptionImplemented based on TruthValue"""


_Dot11ExplicitNonCompressedbeamformingMatrixOptionImplemented_Object = MibTableColumn
dot11ExplicitNonCompressedbeamformingMatrixOptionImplemented = _Dot11ExplicitNonCompressedbeamformingMatrixOptionImplemented_Object(
    (1, 2, 840, 10036, 4, 18, 1, 8),
    _Dot11ExplicitNonCompressedbeamformingMatrixOptionImplemented_Type()
)
dot11ExplicitNonCompressedbeamformingMatrixOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ExplicitNonCompressedbeamformingMatrixOptionImplemented.setStatus("current")


class _Dot11ExplicitBFCSIFeedbackOptionImplemented_Type(Integer32):
    """Custom type dot11ExplicitBFCSIFeedbackOptionImplemented based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("aggregated", 4),
          ("delayed", 1),
          ("delayedAggregated", 5),
          ("immediate", 2),
          ("immediateAggregated", 6),
          ("inCapable", 0),
          ("unsolicitedImmediate", 3),
          ("unsolicitedImmediateAggregated", 7))
    )


_Dot11ExplicitBFCSIFeedbackOptionImplemented_Type.__name__ = "Integer32"
_Dot11ExplicitBFCSIFeedbackOptionImplemented_Object = MibTableColumn
dot11ExplicitBFCSIFeedbackOptionImplemented = _Dot11ExplicitBFCSIFeedbackOptionImplemented_Object(
    (1, 2, 840, 10036, 4, 18, 1, 9),
    _Dot11ExplicitBFCSIFeedbackOptionImplemented_Type()
)
dot11ExplicitBFCSIFeedbackOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ExplicitBFCSIFeedbackOptionImplemented.setStatus("current")


class _Dot11ExplicitNonCompressedbeamformingMatrixFeedbackOptionImplemented_Type(Integer32):
    """Custom type dot11ExplicitNonCompressedbeamformingMatrixFeedbackOptionImplemented based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("aggregated", 4),
          ("delayed", 1),
          ("delayedAggregated", 5),
          ("immediate", 2),
          ("immediateAggregated", 6),
          ("inCapable", 0),
          ("unsolicitedImmediate", 3),
          ("unsolicitedImmediateAggregated", 7))
    )


_Dot11ExplicitNonCompressedbeamformingMatrixFeedbackOptionImplemented_Type.__name__ = "Integer32"
_Dot11ExplicitNonCompressedbeamformingMatrixFeedbackOptionImplemented_Object = MibTableColumn
dot11ExplicitNonCompressedbeamformingMatrixFeedbackOptionImplemented = _Dot11ExplicitNonCompressedbeamformingMatrixFeedbackOptionImplemented_Object(
    (1, 2, 840, 10036, 4, 18, 1, 10),
    _Dot11ExplicitNonCompressedbeamformingMatrixFeedbackOptionImplemented_Type()
)
dot11ExplicitNonCompressedbeamformingMatrixFeedbackOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ExplicitNonCompressedbeamformingMatrixFeedbackOptionImplemented.setStatus("current")


class _Dot11ExplicitCompressedbeamformingMatrixFeedbackOptionImplemented_Type(Integer32):
    """Custom type dot11ExplicitCompressedbeamformingMatrixFeedbackOptionImplemented based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("aggregated", 4),
          ("delayed", 1),
          ("delayedAggregated", 5),
          ("immediate", 2),
          ("immediateAggregated", 6),
          ("inCapable", 0),
          ("unsolicitedImmediate", 3),
          ("unsolicitedImmediateAggregated", 7))
    )


_Dot11ExplicitCompressedbeamformingMatrixFeedbackOptionImplemented_Type.__name__ = "Integer32"
_Dot11ExplicitCompressedbeamformingMatrixFeedbackOptionImplemented_Object = MibTableColumn
dot11ExplicitCompressedbeamformingMatrixFeedbackOptionImplemented = _Dot11ExplicitCompressedbeamformingMatrixFeedbackOptionImplemented_Object(
    (1, 2, 840, 10036, 4, 18, 1, 11),
    _Dot11ExplicitCompressedbeamformingMatrixFeedbackOptionImplemented_Type()
)
dot11ExplicitCompressedbeamformingMatrixFeedbackOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ExplicitCompressedbeamformingMatrixFeedbackOptionImplemented.setStatus("current")


class _Dot11NumberBeamFormingCSISupportAntenna_Type(Integer32):
    """Custom type dot11NumberBeamFormingCSISupportAntenna based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Dot11NumberBeamFormingCSISupportAntenna_Type.__name__ = "Integer32"
_Dot11NumberBeamFormingCSISupportAntenna_Object = MibTableColumn
dot11NumberBeamFormingCSISupportAntenna = _Dot11NumberBeamFormingCSISupportAntenna_Object(
    (1, 2, 840, 10036, 4, 18, 1, 12),
    _Dot11NumberBeamFormingCSISupportAntenna_Type()
)
dot11NumberBeamFormingCSISupportAntenna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11NumberBeamFormingCSISupportAntenna.setStatus("current")


class _Dot11NumberNonCompressedbeamformingMatrixSupportAntenna_Type(Integer32):
    """Custom type dot11NumberNonCompressedbeamformingMatrixSupportAntenna based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Dot11NumberNonCompressedbeamformingMatrixSupportAntenna_Type.__name__ = "Integer32"
_Dot11NumberNonCompressedbeamformingMatrixSupportAntenna_Object = MibTableColumn
dot11NumberNonCompressedbeamformingMatrixSupportAntenna = _Dot11NumberNonCompressedbeamformingMatrixSupportAntenna_Object(
    (1, 2, 840, 10036, 4, 18, 1, 13),
    _Dot11NumberNonCompressedbeamformingMatrixSupportAntenna_Type()
)
dot11NumberNonCompressedbeamformingMatrixSupportAntenna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11NumberNonCompressedbeamformingMatrixSupportAntenna.setStatus("current")


class _Dot11NumberCompressedbeamformingMatrixSupportAntenna_Type(Integer32):
    """Custom type dot11NumberCompressedbeamformingMatrixSupportAntenna based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Dot11NumberCompressedbeamformingMatrixSupportAntenna_Type.__name__ = "Integer32"
_Dot11NumberCompressedbeamformingMatrixSupportAntenna_Object = MibTableColumn
dot11NumberCompressedbeamformingMatrixSupportAntenna = _Dot11NumberCompressedbeamformingMatrixSupportAntenna_Object(
    (1, 2, 840, 10036, 4, 18, 1, 14),
    _Dot11NumberCompressedbeamformingMatrixSupportAntenna_Type()
)
dot11NumberCompressedbeamformingMatrixSupportAntenna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11NumberCompressedbeamformingMatrixSupportAntenna.setStatus("current")


class _Dot11MaxCSIFeedbackDelay_Type(Unsigned32):
    """Custom type dot11MaxCSIFeedbackDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Dot11MaxCSIFeedbackDelay_Type.__name__ = "Unsigned32"
_Dot11MaxCSIFeedbackDelay_Object = MibTableColumn
dot11MaxCSIFeedbackDelay = _Dot11MaxCSIFeedbackDelay_Object(
    (1, 2, 840, 10036, 4, 18, 1, 15),
    _Dot11MaxCSIFeedbackDelay_Type()
)
dot11MaxCSIFeedbackDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11MaxCSIFeedbackDelay.setStatus("current")
_Dot11Conformance_ObjectIdentity = ObjectIdentity
dot11Conformance = _Dot11Conformance_ObjectIdentity(
    (1, 2, 840, 10036, 5)
)
_Dot11Groups_ObjectIdentity = ObjectIdentity
dot11Groups = _Dot11Groups_ObjectIdentity(
    (1, 2, 840, 10036, 5, 1)
)
_Dot11Compliances_ObjectIdentity = ObjectIdentity
dot11Compliances = _Dot11Compliances_ObjectIdentity(
    (1, 2, 840, 10036, 5, 2)
)

# Managed Objects groups

dot11SMTbase = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 1)
)
dot11SMTbase.setObjects(
      *(("IEEE802dot11-MIB", "dot11StationID"),
        ("IEEE802dot11-MIB", "dot11MediumOccupancyLimit"),
        ("IEEE802dot11-MIB", "dot11CFPollable"),
        ("IEEE802dot11-MIB", "dot11CFPPeriod"),
        ("IEEE802dot11-MIB", "dot11CFPMaxDuration"),
        ("IEEE802dot11-MIB", "dot11AuthenticationResponseTimeOut"),
        ("IEEE802dot11-MIB", "dot11PrivacyOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11PowerManagementMode"),
        ("IEEE802dot11-MIB", "dot11DesiredSSID"),
        ("IEEE802dot11-MIB", "dot11DesiredBSSType"),
        ("IEEE802dot11-MIB", "dot11OperationalRateSet"),
        ("IEEE802dot11-MIB", "dot11BeaconPeriod"),
        ("IEEE802dot11-MIB", "dot11DTIMPeriod"),
        ("IEEE802dot11-MIB", "dot11AssociationResponseTimeOut"))
)
if mibBuilder.loadTexts:
    dot11SMTbase.setStatus("deprecated")

dot11SMTprivacy = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 2)
)
dot11SMTprivacy.setObjects(
      *(("IEEE802dot11-MIB", "dot11PrivacyInvoked"),
        ("IEEE802dot11-MIB", "dot11WEPKeyMappingLength"),
        ("IEEE802dot11-MIB", "dot11ExcludeUnencrypted"),
        ("IEEE802dot11-MIB", "dot11WEPICVErrorCount"),
        ("IEEE802dot11-MIB", "dot11WEPExcludedCount"),
        ("IEEE802dot11-MIB", "dot11WEPDefaultKeyID"),
        ("IEEE802dot11-MIB", "dot11WEPDefaultKeyValue"),
        ("IEEE802dot11-MIB", "dot11WEPKeyMappingWEPOn"),
        ("IEEE802dot11-MIB", "dot11WEPKeyMappingValue"),
        ("IEEE802dot11-MIB", "dot11WEPKeyMappingAddress"),
        ("IEEE802dot11-MIB", "dot11WEPKeyMappingStatus"))
)
if mibBuilder.loadTexts:
    dot11SMTprivacy.setStatus("current")

dot11MACbase = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 3)
)
dot11MACbase.setObjects(
      *(("IEEE802dot11-MIB", "dot11MACAddress"),
        ("IEEE802dot11-MIB", "dot11Address"),
        ("IEEE802dot11-MIB", "dot11GroupAddressesStatus"),
        ("IEEE802dot11-MIB", "dot11RTSThreshold"),
        ("IEEE802dot11-MIB", "dot11ShortRetryLimit"),
        ("IEEE802dot11-MIB", "dot11LongRetryLimit"),
        ("IEEE802dot11-MIB", "dot11FragmentationThreshold"),
        ("IEEE802dot11-MIB", "dot11MaxTransmitMSDULifetime"),
        ("IEEE802dot11-MIB", "dot11MaxReceiveLifetime"),
        ("IEEE802dot11-MIB", "dot11ManufacturerID"),
        ("IEEE802dot11-MIB", "dot11ProductID"))
)
if mibBuilder.loadTexts:
    dot11MACbase.setStatus("deprecated")

dot11MACStatistics = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 4)
)
dot11MACStatistics.setObjects(
      *(("IEEE802dot11-MIB", "dot11RetryCount"),
        ("IEEE802dot11-MIB", "dot11MultipleRetryCount"),
        ("IEEE802dot11-MIB", "dot11RTSSuccessCount"),
        ("IEEE802dot11-MIB", "dot11RTSFailureCount"),
        ("IEEE802dot11-MIB", "dot11ACKFailureCount"),
        ("IEEE802dot11-MIB", "dot11FrameDuplicateCount"))
)
if mibBuilder.loadTexts:
    dot11MACStatistics.setStatus("current")

dot11ResourceTypeID = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 5)
)
dot11ResourceTypeID.setObjects(
      *(("IEEE802dot11-MIB", "dot11ResourceTypeIDName"),
        ("IEEE802dot11-MIB", "dot11manufacturerOUI"),
        ("IEEE802dot11-MIB", "dot11manufacturerName"),
        ("IEEE802dot11-MIB", "dot11manufacturerProductName"),
        ("IEEE802dot11-MIB", "dot11manufacturerProductVersion"))
)
if mibBuilder.loadTexts:
    dot11ResourceTypeID.setStatus("current")

dot11SmtAuthenticationAlgorithms = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 6)
)
dot11SmtAuthenticationAlgorithms.setObjects(
      *(("IEEE802dot11-MIB", "dot11AuthenticationAlgorithm"),
        ("IEEE802dot11-MIB", "dot11AuthenticationAlgorithmsEnable"))
)
if mibBuilder.loadTexts:
    dot11SmtAuthenticationAlgorithms.setStatus("current")

dot11PhyOperationComplianceGroup = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 7)
)
dot11PhyOperationComplianceGroup.setObjects(
      *(("IEEE802dot11-MIB", "dot11PHYType"),
        ("IEEE802dot11-MIB", "dot11CurrentRegDomain"),
        ("IEEE802dot11-MIB", "dot11TempType"))
)
if mibBuilder.loadTexts:
    dot11PhyOperationComplianceGroup.setStatus("current")

dot11PhyAntennaComplianceGroup = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 8)
)
dot11PhyAntennaComplianceGroup.setObjects(
      *(("IEEE802dot11-MIB", "dot11CurrentTxAntenna"),
        ("IEEE802dot11-MIB", "dot11DiversitySupport"),
        ("IEEE802dot11-MIB", "dot11CurrentRxAntenna"))
)
if mibBuilder.loadTexts:
    dot11PhyAntennaComplianceGroup.setStatus("deprecated")

dot11PhyTxPowerComplianceGroup = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 9)
)
dot11PhyTxPowerComplianceGroup.setObjects(
      *(("IEEE802dot11-MIB", "dot11NumberSupportedPowerLevels"),
        ("IEEE802dot11-MIB", "dot11TxPowerLevel1"),
        ("IEEE802dot11-MIB", "dot11TxPowerLevel2"),
        ("IEEE802dot11-MIB", "dot11TxPowerLevel3"),
        ("IEEE802dot11-MIB", "dot11TxPowerLevel4"),
        ("IEEE802dot11-MIB", "dot11TxPowerLevel5"),
        ("IEEE802dot11-MIB", "dot11TxPowerLevel6"),
        ("IEEE802dot11-MIB", "dot11TxPowerLevel7"),
        ("IEEE802dot11-MIB", "dot11TxPowerLevel8"),
        ("IEEE802dot11-MIB", "dot11CurrentTxPowerLevel"))
)
if mibBuilder.loadTexts:
    dot11PhyTxPowerComplianceGroup.setStatus("current")

dot11PhyFHSSComplianceGroup = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 10)
)
dot11PhyFHSSComplianceGroup.setObjects(
      *(("IEEE802dot11-MIB", "dot11HopTime"),
        ("IEEE802dot11-MIB", "dot11CurrentChannelNumber"),
        ("IEEE802dot11-MIB", "dot11MaxDwellTime"),
        ("IEEE802dot11-MIB", "dot11CurrentDwellTime"),
        ("IEEE802dot11-MIB", "dot11CurrentSet"),
        ("IEEE802dot11-MIB", "dot11CurrentPattern"),
        ("IEEE802dot11-MIB", "dot11CurrentIndex"))
)
if mibBuilder.loadTexts:
    dot11PhyFHSSComplianceGroup.setStatus("current")

dot11PhyDSSSComplianceGroup = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 11)
)
dot11PhyDSSSComplianceGroup.setObjects(
      *(("IEEE802dot11-MIB", "dot11CurrentChannel"),
        ("IEEE802dot11-MIB", "dot11CCAModeSupported"),
        ("IEEE802dot11-MIB", "dot11CurrentCCAMode"),
        ("IEEE802dot11-MIB", "dot11EDThreshold"))
)
if mibBuilder.loadTexts:
    dot11PhyDSSSComplianceGroup.setStatus("current")

dot11PhyIRComplianceGroup = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 12)
)
dot11PhyIRComplianceGroup.setObjects(
      *(("IEEE802dot11-MIB", "dot11CCAWatchdogTimerMax"),
        ("IEEE802dot11-MIB", "dot11CCAWatchdogCountMax"),
        ("IEEE802dot11-MIB", "dot11CCAWatchdogTimerMin"),
        ("IEEE802dot11-MIB", "dot11CCAWatchdogCountMin"))
)
if mibBuilder.loadTexts:
    dot11PhyIRComplianceGroup.setStatus("current")

dot11PhyRegDomainsSupportGroup = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 13)
)
dot11PhyRegDomainsSupportGroup.setObjects(
    ("IEEE802dot11-MIB", "dot11RegDomainsSupportValue")
)
if mibBuilder.loadTexts:
    dot11PhyRegDomainsSupportGroup.setStatus("current")

dot11PhyAntennasListGroup = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 14)
)
dot11PhyAntennasListGroup.setObjects(
      *(("IEEE802dot11-MIB", "dot11SupportedTxAntenna"),
        ("IEEE802dot11-MIB", "dot11SupportedRxAntenna"),
        ("IEEE802dot11-MIB", "dot11DiversitySelectionRx"))
)
if mibBuilder.loadTexts:
    dot11PhyAntennasListGroup.setStatus("current")

dot11PhyRateGroup = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 15)
)
dot11PhyRateGroup.setObjects(
      *(("IEEE802dot11-MIB", "dot11SupportedDataRatesTxValue"),
        ("IEEE802dot11-MIB", "dot11SupportedDataRatesRxValue"))
)
if mibBuilder.loadTexts:
    dot11PhyRateGroup.setStatus("current")

dot11CountersGroup = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 16)
)
dot11CountersGroup.setObjects(
      *(("IEEE802dot11-MIB", "dot11TransmittedFragmentCount"),
        ("IEEE802dot11-MIB", "dot11MulticastTransmittedFrameCount"),
        ("IEEE802dot11-MIB", "dot11FailedCount"),
        ("IEEE802dot11-MIB", "dot11ReceivedFragmentCount"),
        ("IEEE802dot11-MIB", "dot11MulticastReceivedFrameCount"),
        ("IEEE802dot11-MIB", "dot11FCSErrorCount"),
        ("IEEE802dot11-MIB", "dot11WEPUndecryptableCount"),
        ("IEEE802dot11-MIB", "dot11TransmittedFrameCount"))
)
if mibBuilder.loadTexts:
    dot11CountersGroup.setStatus("deprecated")

dot11SMTbase2 = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 18)
)
dot11SMTbase2.setObjects(
      *(("IEEE802dot11-MIB", "dot11MediumOccupancyLimit"),
        ("IEEE802dot11-MIB", "dot11CFPollable"),
        ("IEEE802dot11-MIB", "dot11CFPPeriod"),
        ("IEEE802dot11-MIB", "dot11CFPMaxDuration"),
        ("IEEE802dot11-MIB", "dot11AuthenticationResponseTimeOut"),
        ("IEEE802dot11-MIB", "dot11PrivacyOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11PowerManagementMode"),
        ("IEEE802dot11-MIB", "dot11DesiredSSID"),
        ("IEEE802dot11-MIB", "dot11DesiredBSSType"),
        ("IEEE802dot11-MIB", "dot11OperationalRateSet"),
        ("IEEE802dot11-MIB", "dot11BeaconPeriod"),
        ("IEEE802dot11-MIB", "dot11DTIMPeriod"),
        ("IEEE802dot11-MIB", "dot11AssociationResponseTimeOut"),
        ("IEEE802dot11-MIB", "dot11DisassociateReason"),
        ("IEEE802dot11-MIB", "dot11DisassociateStation"),
        ("IEEE802dot11-MIB", "dot11DeauthenticateReason"),
        ("IEEE802dot11-MIB", "dot11DeauthenticateStation"),
        ("IEEE802dot11-MIB", "dot11AuthenticateFailStatus"),
        ("IEEE802dot11-MIB", "dot11AuthenticateFailStation"))
)
if mibBuilder.loadTexts:
    dot11SMTbase2.setStatus("deprecated")

dot11PhyHRDSSSComplianceGroup = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 19)
)
dot11PhyHRDSSSComplianceGroup.setObjects(
      *(("IEEE802dot11-MIB", "dot11CurrentChannel"),
        ("IEEE802dot11-MIB", "dot11CCAModeSupported"),
        ("IEEE802dot11-MIB", "dot11CurrentCCAMode"),
        ("IEEE802dot11-MIB", "dot11EDThreshold"),
        ("IEEE802dot11-MIB", "dot11ShortPreambleOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11PBCCOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11ChannelAgilityPresent"),
        ("IEEE802dot11-MIB", "dot11ChannelAgilityEnabled"),
        ("IEEE802dot11-MIB", "dot11HRCCAModeSupported"))
)
if mibBuilder.loadTexts:
    dot11PhyHRDSSSComplianceGroup.setStatus("current")

dot11SMTbase3 = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 20)
)
dot11SMTbase3.setObjects(
      *(("IEEE802dot11-MIB", "dot11MediumOccupancyLimit"),
        ("IEEE802dot11-MIB", "dot11CFPollable"),
        ("IEEE802dot11-MIB", "dot11CFPPeriod"),
        ("IEEE802dot11-MIB", "dot11CFPMaxDuration"),
        ("IEEE802dot11-MIB", "dot11AuthenticationResponseTimeOut"),
        ("IEEE802dot11-MIB", "dot11PrivacyOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11PowerManagementMode"),
        ("IEEE802dot11-MIB", "dot11DesiredSSID"),
        ("IEEE802dot11-MIB", "dot11DesiredBSSType"),
        ("IEEE802dot11-MIB", "dot11OperationalRateSet"),
        ("IEEE802dot11-MIB", "dot11BeaconPeriod"),
        ("IEEE802dot11-MIB", "dot11DTIMPeriod"),
        ("IEEE802dot11-MIB", "dot11AssociationResponseTimeOut"),
        ("IEEE802dot11-MIB", "dot11DisassociateReason"),
        ("IEEE802dot11-MIB", "dot11DisassociateStation"),
        ("IEEE802dot11-MIB", "dot11DeauthenticateReason"),
        ("IEEE802dot11-MIB", "dot11DeauthenticateStation"),
        ("IEEE802dot11-MIB", "dot11AuthenticateFailStatus"),
        ("IEEE802dot11-MIB", "dot11AuthenticateFailStation"),
        ("IEEE802dot11-MIB", "dot11MultiDomainCapabilityImplemented"),
        ("IEEE802dot11-MIB", "dot11MultiDomainCapabilityEnabled"),
        ("IEEE802dot11-MIB", "dot11CountryString"))
)
if mibBuilder.loadTexts:
    dot11SMTbase3.setStatus("current")

dot11MultiDomainCapabilityGroup = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 21)
)
dot11MultiDomainCapabilityGroup.setObjects(
      *(("IEEE802dot11-MIB", "dot11FirstChannelNumber"),
        ("IEEE802dot11-MIB", "dot11NumberofChannels"),
        ("IEEE802dot11-MIB", "dot11MaximumTransmitPowerLevel"))
)
if mibBuilder.loadTexts:
    dot11MultiDomainCapabilityGroup.setStatus("current")

dot11PhyFHSSComplianceGroup2 = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 22)
)
dot11PhyFHSSComplianceGroup2.setObjects(
      *(("IEEE802dot11-MIB", "dot11HopTime"),
        ("IEEE802dot11-MIB", "dot11CurrentChannelNumber"),
        ("IEEE802dot11-MIB", "dot11MaxDwellTime"),
        ("IEEE802dot11-MIB", "dot11CurrentDwellTime"),
        ("IEEE802dot11-MIB", "dot11CurrentSet"),
        ("IEEE802dot11-MIB", "dot11CurrentPattern"),
        ("IEEE802dot11-MIB", "dot11CurrentIndex"),
        ("IEEE802dot11-MIB", "dot11EHCCPrimeRadix"),
        ("IEEE802dot11-MIB", "dot11EHCCNumberofChannelsFamilyIndex"),
        ("IEEE802dot11-MIB", "dot11EHCCCapabilityImplemented"),
        ("IEEE802dot11-MIB", "dot11EHCCCapabilityEnabled"),
        ("IEEE802dot11-MIB", "dot11HopAlgorithmAdopted"),
        ("IEEE802dot11-MIB", "dot11RandomTableFlag"),
        ("IEEE802dot11-MIB", "dot11NumberofHoppingSets"),
        ("IEEE802dot11-MIB", "dot11HopModulus"),
        ("IEEE802dot11-MIB", "dot11HopOffset"),
        ("IEEE802dot11-MIB", "dot11RandomTableFieldNumber"))
)
if mibBuilder.loadTexts:
    dot11PhyFHSSComplianceGroup2.setStatus("current")

dot11PhyOFDMComplianceGroup = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 23)
)
dot11PhyOFDMComplianceGroup.setObjects(
      *(("IEEE802dot11-MIB", "dot11CurrentFrequency"),
        ("IEEE802dot11-MIB", "dot11TIThreshold"),
        ("IEEE802dot11-MIB", "dot11FrequencyBandsSupported"))
)
if mibBuilder.loadTexts:
    dot11PhyOFDMComplianceGroup.setStatus("current")

dot11PhyERPComplianceGroup = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 24)
)
dot11PhyERPComplianceGroup.setObjects(
      *(("IEEE802dot11-MIB", "dot11CurrentChannel"),
        ("IEEE802dot11-MIB", "dot11ShortPreambleOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11ChannelAgilityPresent"),
        ("IEEE802dot11-MIB", "dot11ChannelAgilityEnabled"),
        ("IEEE802dot11-MIB", "dot11DSSSOFDMOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11DSSSOFDMOptionEnabled"),
        ("IEEE802dot11-MIB", "dot11PBCCOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11ERPPBCCOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11ShortSlotTimeOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11ShortSlotTimeOptionEnabled"))
)
if mibBuilder.loadTexts:
    dot11PhyERPComplianceGroup.setStatus("current")

dot11RSNAadditions = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 25)
)
dot11RSNAadditions.setObjects(
      *(("IEEE802dot11-MIB", "dot11RSNAEnabled"),
        ("IEEE802dot11-MIB", "dot11RSNAPreAuthenticationEnabled"))
)
if mibBuilder.loadTexts:
    dot11RSNAadditions.setStatus("current")

dot11SMTbase4 = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 26)
)
dot11SMTbase4.setObjects(
      *(("IEEE802dot11-MIB", "dot11MediumOccupancyLimit"),
        ("IEEE802dot11-MIB", "dot11CFPollable"),
        ("IEEE802dot11-MIB", "dot11CFPPeriod"),
        ("IEEE802dot11-MIB", "dot11CFPMaxDuration"),
        ("IEEE802dot11-MIB", "dot11AuthenticationResponseTimeOut"),
        ("IEEE802dot11-MIB", "dot11PrivacyOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11PowerManagementMode"),
        ("IEEE802dot11-MIB", "dot11DesiredSSID"),
        ("IEEE802dot11-MIB", "dot11DesiredBSSType"),
        ("IEEE802dot11-MIB", "dot11OperationalRateSet"),
        ("IEEE802dot11-MIB", "dot11BeaconPeriod"),
        ("IEEE802dot11-MIB", "dot11DTIMPeriod"),
        ("IEEE802dot11-MIB", "dot11AssociationResponseTimeOut"),
        ("IEEE802dot11-MIB", "dot11DisassociateReason"),
        ("IEEE802dot11-MIB", "dot11DisassociateStation"),
        ("IEEE802dot11-MIB", "dot11DeauthenticateReason"),
        ("IEEE802dot11-MIB", "dot11DeauthenticateStation"),
        ("IEEE802dot11-MIB", "dot11AuthenticateFailStatus"),
        ("IEEE802dot11-MIB", "dot11AuthenticateFailStation"),
        ("IEEE802dot11-MIB", "dot11MultiDomainCapabilityImplemented"),
        ("IEEE802dot11-MIB", "dot11MultiDomainCapabilityEnabled"),
        ("IEEE802dot11-MIB", "dot11CountryString"),
        ("IEEE802dot11-MIB", "dot11RSNAOptionImplemented"))
)
if mibBuilder.loadTexts:
    dot11SMTbase4.setStatus("deprecated")

dot11RSNPMKcachingGroup = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 27)
)
dot11RSNPMKcachingGroup.setObjects(
      *(("IEEE802dot11-MIB", "dot11RSNAConfigPMKLifetime"),
        ("IEEE802dot11-MIB", "dot11RSNAConfigPMKReauthThreshold"))
)
if mibBuilder.loadTexts:
    dot11RSNPMKcachingGroup.setStatus("current")

dot11MACbase2 = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 31)
)
dot11MACbase2.setObjects(
      *(("IEEE802dot11-MIB", "dot11MACAddress"),
        ("IEEE802dot11-MIB", "dot11Address"),
        ("IEEE802dot11-MIB", "dot11GroupAddressesStatus"),
        ("IEEE802dot11-MIB", "dot11RTSThreshold"),
        ("IEEE802dot11-MIB", "dot11ShortRetryLimit"),
        ("IEEE802dot11-MIB", "dot11LongRetryLimit"),
        ("IEEE802dot11-MIB", "dot11FragmentationThreshold"),
        ("IEEE802dot11-MIB", "dot11MaxTransmitMSDULifetime"),
        ("IEEE802dot11-MIB", "dot11MaxReceiveLifetime"),
        ("IEEE802dot11-MIB", "dot11ManufacturerID"),
        ("IEEE802dot11-MIB", "dot11ProductID"),
        ("IEEE802dot11-MIB", "dot11CAPLimit"),
        ("IEEE802dot11-MIB", "dot11HCCWmin"),
        ("IEEE802dot11-MIB", "dot11HCCWmax"),
        ("IEEE802dot11-MIB", "dot11HCCAIFSN"),
        ("IEEE802dot11-MIB", "dot11ADDBAResponseTimeout"),
        ("IEEE802dot11-MIB", "dot11ADDTSResponseTimeout"),
        ("IEEE802dot11-MIB", "dot11ChannelUtilizationBeaconInterval"),
        ("IEEE802dot11-MIB", "dot11ScheduleTimeout"),
        ("IEEE802dot11-MIB", "dot11DLSResponseTimeout"),
        ("IEEE802dot11-MIB", "dot11QAPMissingAckRetryLimit"),
        ("IEEE802dot11-MIB", "dot11EDCAAveragingPeriod"))
)
if mibBuilder.loadTexts:
    dot11MACbase2.setStatus("deprecated")

dot11CountersGroup2 = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 32)
)
dot11CountersGroup2.setObjects(
      *(("IEEE802dot11-MIB", "dot11TransmittedFragmentCount"),
        ("IEEE802dot11-MIB", "dot11MulticastTransmittedFrameCount"),
        ("IEEE802dot11-MIB", "dot11FailedCount"),
        ("IEEE802dot11-MIB", "dot11ReceivedFragmentCount"),
        ("IEEE802dot11-MIB", "dot11MulticastReceivedFrameCount"),
        ("IEEE802dot11-MIB", "dot11FCSErrorCount"),
        ("IEEE802dot11-MIB", "dot11WEPUndecryptableCount"),
        ("IEEE802dot11-MIB", "dot11TransmittedFrameCount"),
        ("IEEE802dot11-MIB", "dot11QosDiscardedFragmentCount"),
        ("IEEE802dot11-MIB", "dot11AssociatedStationCount"),
        ("IEEE802dot11-MIB", "dot11QosCFPollsReceivedCount"),
        ("IEEE802dot11-MIB", "dot11QosCFPollsUnusedCount"),
        ("IEEE802dot11-MIB", "dot11QosCFPollsUnusableCount"))
)
if mibBuilder.loadTexts:
    dot11CountersGroup2.setStatus("deprecated")

dot11Qosadditions = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 33)
)
dot11Qosadditions.setObjects(
      *(("IEEE802dot11-MIB", "dot11EDCATable"),
        ("IEEE802dot11-MIB", "dot11QAPEDCATable"))
)
if mibBuilder.loadTexts:
    dot11Qosadditions.setStatus("current")

dot11SMTbase6 = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 34)
)
dot11SMTbase6.setObjects(
      *(("IEEE802dot11-MIB", "dot11MediumOccupancyLimit"),
        ("IEEE802dot11-MIB", "dot11CFPollable"),
        ("IEEE802dot11-MIB", "dot11CFPPeriod"),
        ("IEEE802dot11-MIB", "dot11CFPMaxDuration"),
        ("IEEE802dot11-MIB", "dot11AuthenticationResponseTimeOut"),
        ("IEEE802dot11-MIB", "dot11PrivacyOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11PowerManagementMode"),
        ("IEEE802dot11-MIB", "dot11DesiredSSID"),
        ("IEEE802dot11-MIB", "dot11DesiredBSSType"),
        ("IEEE802dot11-MIB", "dot11OperationalRateSet"),
        ("IEEE802dot11-MIB", "dot11BeaconPeriod"),
        ("IEEE802dot11-MIB", "dot11DTIMPeriod"),
        ("IEEE802dot11-MIB", "dot11AssociationResponseTimeOut"),
        ("IEEE802dot11-MIB", "dot11DisassociateReason"),
        ("IEEE802dot11-MIB", "dot11DisassociateStation"),
        ("IEEE802dot11-MIB", "dot11DeauthenticateReason"),
        ("IEEE802dot11-MIB", "dot11DeauthenticateStation"),
        ("IEEE802dot11-MIB", "dot11AuthenticateFailStatus"),
        ("IEEE802dot11-MIB", "dot11AuthenticateFailStation"),
        ("IEEE802dot11-MIB", "dot11MultiDomainCapabilityImplemented"),
        ("IEEE802dot11-MIB", "dot11MultiDomainCapabilityEnabled"),
        ("IEEE802dot11-MIB", "dot11CountryString"),
        ("IEEE802dot11-MIB", "dot11RSNAOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11QosOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11ImmediateBlockAckOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11DelayedBlockAckOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11DirectOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11APSDOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11QAckOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11QBSSLoadOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11QueueRequestOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11TXOPRequestOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11MoreDataAckOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11AssociateinNQBSS"),
        ("IEEE802dot11-MIB", "dot11DLSAllowedInQBSS"),
        ("IEEE802dot11-MIB", "dot11DLSAllowed"))
)
if mibBuilder.loadTexts:
    dot11SMTbase6.setStatus("current")

dot11PhyAntennaComplianceGroup2 = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 41)
)
dot11PhyAntennaComplianceGroup2.setObjects(
      *(("IEEE802dot11-MIB", "dot11CurrentTxAntenna"),
        ("IEEE802dot11-MIB", "dot11DiversitySupport"),
        ("IEEE802dot11-MIB", "dot11CurrentRxAntenna"),
        ("IEEE802dot11-MIB", "dot11TransmitExplicitCSIFeedbackASOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11TransmitIndicesFeedbackASOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11ExplicitCSIFeedbackASOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11TransmitIndicesComputationFeedbackASOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11ReceiveAntennaSelectionOptionImplemented"))
)
if mibBuilder.loadTexts:
    dot11PhyAntennaComplianceGroup2.setStatus("current")

dot11MACbase3 = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 42)
)
dot11MACbase3.setObjects(
      *(("IEEE802dot11-MIB", "dot11MACAddress"),
        ("IEEE802dot11-MIB", "dot11Address"),
        ("IEEE802dot11-MIB", "dot11GroupAddressesStatus"),
        ("IEEE802dot11-MIB", "dot11RTSThreshold"),
        ("IEEE802dot11-MIB", "dot11ShortRetryLimit"),
        ("IEEE802dot11-MIB", "dot11LongRetryLimit"),
        ("IEEE802dot11-MIB", "dot11FragmentationThreshold"),
        ("IEEE802dot11-MIB", "dot11MaxTransmitMSDULifetime"),
        ("IEEE802dot11-MIB", "dot11MaxReceiveLifetime"),
        ("IEEE802dot11-MIB", "dot11ManufacturerID"),
        ("IEEE802dot11-MIB", "dot11ProductID"),
        ("IEEE802dot11-MIB", "dot11CAPLimit"),
        ("IEEE802dot11-MIB", "dot11HCCWmin"),
        ("IEEE802dot11-MIB", "dot11HCCWmax"),
        ("IEEE802dot11-MIB", "dot11HCCAIFSN"),
        ("IEEE802dot11-MIB", "dot11ADDBAResponseTimeout"),
        ("IEEE802dot11-MIB", "dot11ADDTSResponseTimeout"),
        ("IEEE802dot11-MIB", "dot11ChannelUtilizationBeaconInterval"),
        ("IEEE802dot11-MIB", "dot11ScheduleTimeout"),
        ("IEEE802dot11-MIB", "dot11DLSResponseTimeout"),
        ("IEEE802dot11-MIB", "dot11QAPMissingAckRetryLimit"),
        ("IEEE802dot11-MIB", "dot11EDCAAveragingPeriod"),
        ("IEEE802dot11-MIB", "dot11HTOperatingMode"),
        ("IEEE802dot11-MIB", "dot11RIFSMode"),
        ("IEEE802dot11-MIB", "dot11PSMPControlledAccess"),
        ("IEEE802dot11-MIB", "dot11ServiceIntervalGranularity"),
        ("IEEE802dot11-MIB", "dot11DualCTSProtection"),
        ("IEEE802dot11-MIB", "dot11LSigTxopFullProtectionEnabled"),
        ("IEEE802dot11-MIB", "dot11NonGFEntitiesPresent"),
        ("IEEE802dot11-MIB", "dot11PCOActivated"),
        ("IEEE802dot11-MIB", "dot11PCO40MaxDuration"),
        ("IEEE802dot11-MIB", "dot11PCO20MaxDuration"),
        ("IEEE802dot11-MIB", "dot11PCO40MinDuration"),
        ("IEEE802dot11-MIB", "dot11PCO20MinDuration"))
)
if mibBuilder.loadTexts:
    dot11MACbase3.setStatus("current")

dot11CountersGroup3 = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 43)
)
dot11CountersGroup3.setObjects(
      *(("IEEE802dot11-MIB", "dot11TransmittedFragmentCount"),
        ("IEEE802dot11-MIB", "dot11MulticastTransmittedFrameCount"),
        ("IEEE802dot11-MIB", "dot11FailedCount"),
        ("IEEE802dot11-MIB", "dot11ReceivedFragmentCount"),
        ("IEEE802dot11-MIB", "dot11MulticastReceivedFrameCount"),
        ("IEEE802dot11-MIB", "dot11FCSErrorCount"),
        ("IEEE802dot11-MIB", "dot11WEPUndecryptableCount"),
        ("IEEE802dot11-MIB", "dot11TransmittedFrameCount"),
        ("IEEE802dot11-MIB", "dot11QosDiscardedFragmentCount"),
        ("IEEE802dot11-MIB", "dot11AssociatedStationCount"),
        ("IEEE802dot11-MIB", "dot11QosCFPollsReceivedCount"),
        ("IEEE802dot11-MIB", "dot11QosCFPollsUnusedCount"),
        ("IEEE802dot11-MIB", "dot11QosCFPollsUnusableCount"),
        ("IEEE802dot11-MIB", "dot11TransmittedAMSDUCount"),
        ("IEEE802dot11-MIB", "dot11FailedAMSDUCount"),
        ("IEEE802dot11-MIB", "dot11RetryAMSDUCount"),
        ("IEEE802dot11-MIB", "dot11MultipleRetryAMSDUCount"),
        ("IEEE802dot11-MIB", "dot11AMSDUAckFailureCount"),
        ("IEEE802dot11-MIB", "dot11ReceivedAMSDUCount"),
        ("IEEE802dot11-MIB", "dot11TransmittedAMPDUCount"),
        ("IEEE802dot11-MIB", "dot11TransmittedMPDUsInAMPDUCount"),
        ("IEEE802dot11-MIB", "dot11TransmittedOctetsInAMPDUCount"),
        ("IEEE802dot11-MIB", "dot11AMPDUReceivedCount"),
        ("IEEE802dot11-MIB", "dot11MPDUInReceivedAMPDUCount"),
        ("IEEE802dot11-MIB", "dot11ReceivedOctetsInAMPDUCount"),
        ("IEEE802dot11-MIB", "dot11AMPDUDelimiterCRCErrorCount"),
        ("IEEE802dot11-MIB", "dot11ImplicitBARFailureCount"),
        ("IEEE802dot11-MIB", "dot11ExplicitBARFailureCount"),
        ("IEEE802dot11-MIB", "dot11ChannelWidthSwitchCount"),
        ("IEEE802dot11-MIB", "dot11TwentyMHzFrameTransmittedCount"),
        ("IEEE802dot11-MIB", "dot11FortyMHzFrameTransmittedCount"),
        ("IEEE802dot11-MIB", "dot11TwentyMHzFrameReceivedCount"),
        ("IEEE802dot11-MIB", "dot11FortyMHzFrameReceivedCount"),
        ("IEEE802dot11-MIB", "dot11PSMPSuccessCount"),
        ("IEEE802dot11-MIB", "dot11PSMPFailureCount"),
        ("IEEE802dot11-MIB", "dot11GrantedRDGUsedCount"),
        ("IEEE802dot11-MIB", "dot11GrantedRDGUnusedCount"),
        ("IEEE802dot11-MIB", "dot11TransmittedFramesInGrantedRDGCount"),
        ("IEEE802dot11-MIB", "dot11TransmittedOctetsInGrantedRDGCount"),
        ("IEEE802dot11-MIB", "dot11DualCTSSuccessCount"),
        ("IEEE802dot11-MIB", "dot11DualCTSFailureCount"),
        ("IEEE802dot11-MIB", "dot11STBCCTSSuccessCount"),
        ("IEEE802dot11-MIB", "dot11STBCCTSFailureCount"),
        ("IEEE802dot11-MIB", "dot11nonSTBCCTSSuccessCount"),
        ("IEEE802dot11-MIB", "dot11nonSTBCCTSFailureCount"),
        ("IEEE802dot11-MIB", "dot11RTSLSIGSuccessCount"),
        ("IEEE802dot11-MIB", "dot11RTSLSIGFailureCount"))
)
if mibBuilder.loadTexts:
    dot11CountersGroup3.setStatus("current")

dot11SMTbase9 = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 44)
)
dot11SMTbase9.setObjects(
      *(("IEEE802dot11-MIB", "dot11MediumOccupancyLimit"),
        ("IEEE802dot11-MIB", "dot11CFPollable"),
        ("IEEE802dot11-MIB", "dot11CFPPeriod"),
        ("IEEE802dot11-MIB", "dot11CFPMaxDuration"),
        ("IEEE802dot11-MIB", "dot11AuthenticationResponseTimeOut"),
        ("IEEE802dot11-MIB", "dot11PrivacyOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11PowerManagementMode"),
        ("IEEE802dot11-MIB", "dot11DesiredSSID"),
        ("IEEE802dot11-MIB", "dot11DesiredBSSType"),
        ("IEEE802dot11-MIB", "dot11OperationalRateSet"),
        ("IEEE802dot11-MIB", "dot11BeaconPeriod"),
        ("IEEE802dot11-MIB", "dot11DTIMPeriod"),
        ("IEEE802dot11-MIB", "dot11AssociationResponseTimeOut"),
        ("IEEE802dot11-MIB", "dot11DisassociateReason"),
        ("IEEE802dot11-MIB", "dot11DisassociateStation"),
        ("IEEE802dot11-MIB", "dot11DeauthenticateReason"),
        ("IEEE802dot11-MIB", "dot11DeauthenticateStation"),
        ("IEEE802dot11-MIB", "dot11AuthenticateFailStatus"),
        ("IEEE802dot11-MIB", "dot11AuthenticateFailStation"),
        ("IEEE802dot11-MIB", "dot11MultiDomainCapabilityImplemented"),
        ("IEEE802dot11-MIB", "dot11MultiDomainCapabilityEnabled"),
        ("IEEE802dot11-MIB", "dot11CountryString"),
        ("IEEE802dot11-MIB", "dot11RSNAOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11QosOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11ImmediateBlockAckOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11DelayedBlockAckOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11DirectOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11APSDOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11QAckOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11QBSSLoadOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11QueueRequestOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11TXOPRequestOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11MoreDataAckOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11AssociateinNQBSS"),
        ("IEEE802dot11-MIB", "dot11DLSAllowedInQBSS"),
        ("IEEE802dot11-MIB", "dot11DLSAllowed"))
)
if mibBuilder.loadTexts:
    dot11SMTbase9.setStatus("current")

dot11PhyMCSGroup = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 45)
)
dot11PhyMCSGroup.setObjects(
      *(("IEEE802dot11-MIB", "dot11SupportedMCSTxValue"),
        ("IEEE802dot11-MIB", "dot11SupportedMCSRxValue"))
)
if mibBuilder.loadTexts:
    dot11PhyMCSGroup.setStatus("current")

dot1PhyHTComplianceGroup = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 46)
)
dot1PhyHTComplianceGroup.setObjects(
      *(("IEEE802dot11-MIB", "dot11HighThroughputOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11FortyMHzOperationImplemented"),
        ("IEEE802dot11-MIB", "dot11FortyMHzOperationEnabled"),
        ("IEEE802dot11-MIB", "dot11CurrentPrimaryChannel"),
        ("IEEE802dot11-MIB", "dot11CurrentSecondaryChannel"),
        ("IEEE802dot11-MIB", "dot11GreenfieldOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11GreenfieldOptionEnabled"),
        ("IEEE802dot11-MIB", "dot11ShortGIOptionInTwentyImplemented"),
        ("IEEE802dot11-MIB", "dot11ShortGIOptionInTwentyEnabled"),
        ("IEEE802dot11-MIB", "dot11ShortGIOptionInFortyImplemented"),
        ("IEEE802dot11-MIB", "dot11ShortGIOptionInFortyEnabled"),
        ("IEEE802dot11-MIB", "dot11LDPCCodingOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11LDPCCodingOptionEnabled"),
        ("IEEE802dot11-MIB", "dot11TxSTBCOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11TxSTBCOptionEnabled"),
        ("IEEE802dot11-MIB", "dot11RxSTBCOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11RxSTBCOptionEnabled"),
        ("IEEE802dot11-MIB", "dot11BeamFormingOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11BeamFormingOptionImplemented"))
)
if mibBuilder.loadTexts:
    dot1PhyHTComplianceGroup.setStatus("current")

dot11HTMACAdditions = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 47)
)
dot11HTMACAdditions.setObjects(
      *(("IEEE802dot11-MIB", "dot11HTOperationalMCSSet"),
        ("IEEE802dot11-MIB", "dot11MIMOPowerSave"),
        ("IEEE802dot11-MIB", "dot11NDelayedBlockAckOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11MaxAMSDULength"),
        ("IEEE802dot11-MIB", "dot11PSMPOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11STBCControlFrameOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11LsigTxopProtectionOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11MaxRxAMPDUFactor"),
        ("IEEE802dot11-MIB", "dot11MinimumMPDUStartSpacing"),
        ("IEEE802dot11-MIB", "dot11PCOOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11TransitionTime"),
        ("IEEE802dot11-MIB", "dot11MCSFeedbackOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11HTControlFieldSupported"),
        ("IEEE802dot11-MIB", "dot11RDResponderOptionImplemented"))
)
if mibBuilder.loadTexts:
    dot11HTMACAdditions.setStatus("current")

dot11TxBFGroup = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 48)
)
dot11TxBFGroup.setObjects(
      *(("IEEE802dot11-MIB", "dot11ReceiveStaggerSoundingOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11TransmitStaggerSoundingOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11ReceiveNDPOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11TransmitNDPOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11ImplicitTxBFOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11CalibrationOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11ExplicitCSITxBFOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11ExplicitNonCompressedbeamformingMatrixOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11ExplicitBFCSIFeedbackOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11ExplicitNonCompressedbeamformingMatrixFeedbackOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11ExplicitCompressedbeamformingMatrixFeedbackOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11NumberBeamFormingCSISupportAntenna"),
        ("IEEE802dot11-MIB", "dot11NumberNonCompressedbeamformingMatrixSupportAntenna"),
        ("IEEE802dot11-MIB", "dot11NumberCompressedbeamformingMatrixSupportAntenna"))
)
if mibBuilder.loadTexts:
    dot11TxBFGroup.setStatus("current")

dot11RSNBase = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 126)
)
dot11RSNBase.setObjects(
      *(("IEEE802dot11-MIB", "dot11RSNAConfigVersion"),
        ("IEEE802dot11-MIB", "dot11RSNAConfigPairwiseKeysSupported"),
        ("IEEE802dot11-MIB", "dot11RSNAConfigGroupCipher"),
        ("IEEE802dot11-MIB", "dot11RSNAConfigGroupRekeyMethod"),
        ("IEEE802dot11-MIB", "dot11RSNAConfigGroupRekeyTime"),
        ("IEEE802dot11-MIB", "dot11RSNAConfigGroupRekeyPackets"),
        ("IEEE802dot11-MIB", "dot11RSNAConfigGroupRekeyStrict"),
        ("IEEE802dot11-MIB", "dot11RSNAConfigPSKValue"),
        ("IEEE802dot11-MIB", "dot11RSNAConfigPSKPassPhrase"),
        ("IEEE802dot11-MIB", "dot11RSNAConfigGroupUpdateCount"),
        ("IEEE802dot11-MIB", "dot11RSNAConfigPairwiseUpdateCount"),
        ("IEEE802dot11-MIB", "dot11RSNAConfigGroupCipherSize"),
        ("IEEE802dot11-MIB", "dot11RSNAConfigPairwiseCipher"),
        ("IEEE802dot11-MIB", "dot11RSNAConfigPairwiseCipherEnabled"),
        ("IEEE802dot11-MIB", "dot11RSNAConfigPairwiseCipherSize"),
        ("IEEE802dot11-MIB", "dot11RSNAConfigAuthenticationSuite"),
        ("IEEE802dot11-MIB", "dot11RSNAConfigAuthenticationSuiteEnabled"),
        ("IEEE802dot11-MIB", "dot11RSNAConfigNumberOfPTKSAReplayCounters"),
        ("IEEE802dot11-MIB", "dot11RSNAConfigSATimeout"),
        ("IEEE802dot11-MIB", "dot11RSNAConfigNumberOfGTKSAReplayCounters"),
        ("IEEE802dot11-MIB", "dot11RSNAAuthenticationSuiteSelected"),
        ("IEEE802dot11-MIB", "dot11RSNAPairwiseCipherSelected"),
        ("IEEE802dot11-MIB", "dot11RSNAGroupCipherSelected"),
        ("IEEE802dot11-MIB", "dot11RSNAPMKIDUsed"),
        ("IEEE802dot11-MIB", "dot11RSNAAuthenticationSuiteRequested"),
        ("IEEE802dot11-MIB", "dot11RSNAPairwiseCipherRequested"),
        ("IEEE802dot11-MIB", "dot11RSNAGroupCipherRequested"),
        ("IEEE802dot11-MIB", "dot11RSNAStatsSTAAddress"),
        ("IEEE802dot11-MIB", "dot11RSNAStatsVersion"),
        ("IEEE802dot11-MIB", "dot11RSNAStatsSelectedPairwiseCipher"),
        ("IEEE802dot11-MIB", "dot11RSNAStatsTKIPICVErrors"),
        ("IEEE802dot11-MIB", "dot11RSNAStatsTKIPLocalMICFailures"),
        ("IEEE802dot11-MIB", "dot11RSNAStatsTKIPRemoteMICFailures"),
        ("IEEE802dot11-MIB", "dot11RSNAStatsCCMPReplays"),
        ("IEEE802dot11-MIB", "dot11RSNAStatsCCMPDecryptErrors"))
)
if mibBuilder.loadTexts:
    dot11RSNBase.setStatus("current")


# Notification objects

dot11Disassociate = NotificationType(
    (1, 2, 840, 10036, 1, 6, 0, 1)
)
dot11Disassociate.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IEEE802dot11-MIB", "dot11DisassociateReason"),
        ("IEEE802dot11-MIB", "dot11DisassociateStation"))
)
if mibBuilder.loadTexts:
    dot11Disassociate.setStatus(
        "current"
    )

dot11Deauthenticate = NotificationType(
    (1, 2, 840, 10036, 1, 6, 0, 2)
)
dot11Deauthenticate.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IEEE802dot11-MIB", "dot11DeauthenticateReason"),
        ("IEEE802dot11-MIB", "dot11DeauthenticateStation"))
)
if mibBuilder.loadTexts:
    dot11Deauthenticate.setStatus(
        "current"
    )

dot11AuthenticateFail = NotificationType(
    (1, 2, 840, 10036, 1, 6, 0, 3)
)
dot11AuthenticateFail.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IEEE802dot11-MIB", "dot11AuthenticateFailStatus"),
        ("IEEE802dot11-MIB", "dot11AuthenticateFailStation"))
)
if mibBuilder.loadTexts:
    dot11AuthenticateFail.setStatus(
        "current"
    )


# Notifications groups

dot11NotificationGroup = NotificationGroup(
    (1, 2, 840, 10036, 5, 1, 17)
)
dot11NotificationGroup.setObjects(
      *(("IEEE802dot11-MIB", "dot11Disassociate"),
        ("IEEE802dot11-MIB", "dot11Deauthenticate"),
        ("IEEE802dot11-MIB", "dot11AuthenticateFail"))
)
if mibBuilder.loadTexts:
    dot11NotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

dot11Compliance = ModuleCompliance(
    (1, 2, 840, 10036, 5, 2, 1)
)
if mibBuilder.loadTexts:
    dot11Compliance.setStatus(
        "current"
    )

dot11RSNCompliance = ModuleCompliance(
    (1, 2, 840, 10036, 5, 2, 2)
)
if mibBuilder.loadTexts:
    dot11RSNCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IEEE802dot11-MIB",
    **{"WEPKeytype": WEPKeytype,
       "member-body": member_body,
       "us": us,
       "ieee802dot11": ieee802dot11,
       "dot11smt": dot11smt,
       "dot11StationConfigTable": dot11StationConfigTable,
       "dot11StationConfigEntry": dot11StationConfigEntry,
       "dot11StationID": dot11StationID,
       "dot11MediumOccupancyLimit": dot11MediumOccupancyLimit,
       "dot11CFPollable": dot11CFPollable,
       "dot11CFPPeriod": dot11CFPPeriod,
       "dot11CFPMaxDuration": dot11CFPMaxDuration,
       "dot11AuthenticationResponseTimeOut": dot11AuthenticationResponseTimeOut,
       "dot11PrivacyOptionImplemented": dot11PrivacyOptionImplemented,
       "dot11PowerManagementMode": dot11PowerManagementMode,
       "dot11DesiredSSID": dot11DesiredSSID,
       "dot11DesiredBSSType": dot11DesiredBSSType,
       "dot11OperationalRateSet": dot11OperationalRateSet,
       "dot11BeaconPeriod": dot11BeaconPeriod,
       "dot11DTIMPeriod": dot11DTIMPeriod,
       "dot11AssociationResponseTimeOut": dot11AssociationResponseTimeOut,
       "dot11DisassociateReason": dot11DisassociateReason,
       "dot11DisassociateStation": dot11DisassociateStation,
       "dot11DeauthenticateReason": dot11DeauthenticateReason,
       "dot11DeauthenticateStation": dot11DeauthenticateStation,
       "dot11AuthenticateFailStatus": dot11AuthenticateFailStatus,
       "dot11AuthenticateFailStation": dot11AuthenticateFailStation,
       "dot11MultiDomainCapabilityImplemented": dot11MultiDomainCapabilityImplemented,
       "dot11MultiDomainCapabilityEnabled": dot11MultiDomainCapabilityEnabled,
       "dot11CountryString": dot11CountryString,
       "dot11SpectrumManagementImplemented": dot11SpectrumManagementImplemented,
       "dot11SpectrumManagementRequired": dot11SpectrumManagementRequired,
       "dot11RSNAOptionImplemented": dot11RSNAOptionImplemented,
       "dot11RSNAPreauthenticationImplemented": dot11RSNAPreauthenticationImplemented,
       "dot11QosOptionImplemented": dot11QosOptionImplemented,
       "dot11ImmediateBlockAckOptionImplemented": dot11ImmediateBlockAckOptionImplemented,
       "dot11DelayedBlockAckOptionImplemented": dot11DelayedBlockAckOptionImplemented,
       "dot11DirectOptionImplemented": dot11DirectOptionImplemented,
       "dot11APSDOptionImplemented": dot11APSDOptionImplemented,
       "dot11QAckOptionImplemented": dot11QAckOptionImplemented,
       "dot11QBSSLoadOptionImplemented": dot11QBSSLoadOptionImplemented,
       "dot11QueueRequestOptionImplemented": dot11QueueRequestOptionImplemented,
       "dot11TXOPRequestOptionImplemented": dot11TXOPRequestOptionImplemented,
       "dot11MoreDataAckOptionImplemented": dot11MoreDataAckOptionImplemented,
       "dot11AssociateinNQBSS": dot11AssociateinNQBSS,
       "dot11DLSAllowedInQBSS": dot11DLSAllowedInQBSS,
       "dot11DLSAllowed": dot11DLSAllowed,
       "dot11HighThroughputOptionImplemented": dot11HighThroughputOptionImplemented,
       "dot11AuthenticationAlgorithmsTable": dot11AuthenticationAlgorithmsTable,
       "dot11AuthenticationAlgorithmsEntry": dot11AuthenticationAlgorithmsEntry,
       "dot11AuthenticationAlgorithmsIndex": dot11AuthenticationAlgorithmsIndex,
       "dot11AuthenticationAlgorithm": dot11AuthenticationAlgorithm,
       "dot11AuthenticationAlgorithmsEnable": dot11AuthenticationAlgorithmsEnable,
       "dot11WEPDefaultKeysTable": dot11WEPDefaultKeysTable,
       "dot11WEPDefaultKeysEntry": dot11WEPDefaultKeysEntry,
       "dot11WEPDefaultKeyIndex": dot11WEPDefaultKeyIndex,
       "dot11WEPDefaultKeyValue": dot11WEPDefaultKeyValue,
       "dot11WEPKeyMappingsTable": dot11WEPKeyMappingsTable,
       "dot11WEPKeyMappingsEntry": dot11WEPKeyMappingsEntry,
       "dot11WEPKeyMappingIndex": dot11WEPKeyMappingIndex,
       "dot11WEPKeyMappingAddress": dot11WEPKeyMappingAddress,
       "dot11WEPKeyMappingWEPOn": dot11WEPKeyMappingWEPOn,
       "dot11WEPKeyMappingValue": dot11WEPKeyMappingValue,
       "dot11WEPKeyMappingStatus": dot11WEPKeyMappingStatus,
       "dot11PrivacyTable": dot11PrivacyTable,
       "dot11PrivacyEntry": dot11PrivacyEntry,
       "dot11PrivacyInvoked": dot11PrivacyInvoked,
       "dot11WEPDefaultKeyID": dot11WEPDefaultKeyID,
       "dot11WEPKeyMappingLength": dot11WEPKeyMappingLength,
       "dot11ExcludeUnencrypted": dot11ExcludeUnencrypted,
       "dot11WEPICVErrorCount": dot11WEPICVErrorCount,
       "dot11WEPExcludedCount": dot11WEPExcludedCount,
       "dot11RSNAEnabled": dot11RSNAEnabled,
       "dot11RSNAPreAuthenticationEnabled": dot11RSNAPreAuthenticationEnabled,
       "dot11SMTnotification": dot11SMTnotification,
       "dot11SMT-unknown": dot11SMT_unknown,
       "dot11Disassociate": dot11Disassociate,
       "dot11Deauthenticate": dot11Deauthenticate,
       "dot11AuthenticateFail": dot11AuthenticateFail,
       "dot11MultiDomainCapabilityTable": dot11MultiDomainCapabilityTable,
       "dot11MultiDomainCapabilityEntry": dot11MultiDomainCapabilityEntry,
       "dot11MultiDomainCapabilityIndex": dot11MultiDomainCapabilityIndex,
       "dot11FirstChannelNumber": dot11FirstChannelNumber,
       "dot11NumberofChannels": dot11NumberofChannels,
       "dot11MaximumTransmitPowerLevel": dot11MaximumTransmitPowerLevel,
       "dot11SpectrumManagementTable": dot11SpectrumManagementTable,
       "dot11SpectrumManagementEntry": dot11SpectrumManagementEntry,
       "dot11SpectrumManagementIndex": dot11SpectrumManagementIndex,
       "dot11MitigationRequirement": dot11MitigationRequirement,
       "dot11ChannelSwitchTime": dot11ChannelSwitchTime,
       "dot11PowerCapabilityMax": dot11PowerCapabilityMax,
       "dot11PowerCapabilityMin": dot11PowerCapabilityMin,
       "dot11RSNAConfigTable": dot11RSNAConfigTable,
       "dot11RSNAConfigEntry": dot11RSNAConfigEntry,
       "dot11RSNAConfigVersion": dot11RSNAConfigVersion,
       "dot11RSNAConfigPairwiseKeysSupported": dot11RSNAConfigPairwiseKeysSupported,
       "dot11RSNAConfigGroupCipher": dot11RSNAConfigGroupCipher,
       "dot11RSNAConfigGroupRekeyMethod": dot11RSNAConfigGroupRekeyMethod,
       "dot11RSNAConfigGroupRekeyTime": dot11RSNAConfigGroupRekeyTime,
       "dot11RSNAConfigGroupRekeyPackets": dot11RSNAConfigGroupRekeyPackets,
       "dot11RSNAConfigGroupRekeyStrict": dot11RSNAConfigGroupRekeyStrict,
       "dot11RSNAConfigPSKValue": dot11RSNAConfigPSKValue,
       "dot11RSNAConfigPSKPassPhrase": dot11RSNAConfigPSKPassPhrase,
       "dot11RSNAConfigGroupUpdateCount": dot11RSNAConfigGroupUpdateCount,
       "dot11RSNAConfigPairwiseUpdateCount": dot11RSNAConfigPairwiseUpdateCount,
       "dot11RSNAConfigGroupCipherSize": dot11RSNAConfigGroupCipherSize,
       "dot11RSNAConfigPMKLifetime": dot11RSNAConfigPMKLifetime,
       "dot11RSNAConfigPMKReauthThreshold": dot11RSNAConfigPMKReauthThreshold,
       "dot11RSNAConfigNumberOfPTKSAReplayCounters": dot11RSNAConfigNumberOfPTKSAReplayCounters,
       "dot11RSNAConfigSATimeout": dot11RSNAConfigSATimeout,
       "dot11RSNAAuthenticationSuiteSelected": dot11RSNAAuthenticationSuiteSelected,
       "dot11RSNAPairwiseCipherSelected": dot11RSNAPairwiseCipherSelected,
       "dot11RSNAGroupCipherSelected": dot11RSNAGroupCipherSelected,
       "dot11RSNAPMKIDUsed": dot11RSNAPMKIDUsed,
       "dot11RSNAAuthenticationSuiteRequested": dot11RSNAAuthenticationSuiteRequested,
       "dot11RSNAPairwiseCipherRequested": dot11RSNAPairwiseCipherRequested,
       "dot11RSNAGroupCipherRequested": dot11RSNAGroupCipherRequested,
       "dot11RSNATKIPCounterMeasuresInvoked": dot11RSNATKIPCounterMeasuresInvoked,
       "dot11RSNA4WayHandshakeFailures": dot11RSNA4WayHandshakeFailures,
       "dot11RSNAConfigNumberOfGTKSAReplayCounters": dot11RSNAConfigNumberOfGTKSAReplayCounters,
       "dot11RSNAConfigPairwiseCiphersTable": dot11RSNAConfigPairwiseCiphersTable,
       "dot11RSNAConfigPairwiseCiphersEntry": dot11RSNAConfigPairwiseCiphersEntry,
       "dot11RSNAConfigPairwiseCipherIndex": dot11RSNAConfigPairwiseCipherIndex,
       "dot11RSNAConfigPairwiseCipher": dot11RSNAConfigPairwiseCipher,
       "dot11RSNAConfigPairwiseCipherEnabled": dot11RSNAConfigPairwiseCipherEnabled,
       "dot11RSNAConfigPairwiseCipherSize": dot11RSNAConfigPairwiseCipherSize,
       "dot11RSNAConfigAuthenticationSuitesTable": dot11RSNAConfigAuthenticationSuitesTable,
       "dot11RSNAConfigAuthenticationSuitesEntry": dot11RSNAConfigAuthenticationSuitesEntry,
       "dot11RSNAConfigAuthenticationSuiteIndex": dot11RSNAConfigAuthenticationSuiteIndex,
       "dot11RSNAConfigAuthenticationSuite": dot11RSNAConfigAuthenticationSuite,
       "dot11RSNAConfigAuthenticationSuiteEnabled": dot11RSNAConfigAuthenticationSuiteEnabled,
       "dot11RSNAStatsTable": dot11RSNAStatsTable,
       "dot11RSNAStatsEntry": dot11RSNAStatsEntry,
       "dot11RSNAStatsIndex": dot11RSNAStatsIndex,
       "dot11RSNAStatsSTAAddress": dot11RSNAStatsSTAAddress,
       "dot11RSNAStatsVersion": dot11RSNAStatsVersion,
       "dot11RSNAStatsSelectedPairwiseCipher": dot11RSNAStatsSelectedPairwiseCipher,
       "dot11RSNAStatsTKIPICVErrors": dot11RSNAStatsTKIPICVErrors,
       "dot11RSNAStatsTKIPLocalMICFailures": dot11RSNAStatsTKIPLocalMICFailures,
       "dot11RSNAStatsTKIPRemoteMICFailures": dot11RSNAStatsTKIPRemoteMICFailures,
       "dot11RSNAStatsCCMPReplays": dot11RSNAStatsCCMPReplays,
       "dot11RSNAStatsCCMPDecryptErrors": dot11RSNAStatsCCMPDecryptErrors,
       "dot11RSNAStatsTKIPReplays": dot11RSNAStatsTKIPReplays,
       "dot11HTStationConfigTable": dot11HTStationConfigTable,
       "dot11HTStationConfigEntry": dot11HTStationConfigEntry,
       "dot11HTOperationalMCSSet": dot11HTOperationalMCSSet,
       "dot11MIMOPowerSave": dot11MIMOPowerSave,
       "dot11NDelayedBlockAckOptionImplemented": dot11NDelayedBlockAckOptionImplemented,
       "dot11MaxAMSDULength": dot11MaxAMSDULength,
       "dot11PSMPOptionImplemented": dot11PSMPOptionImplemented,
       "dot11STBCControlFrameOptionImplemented": dot11STBCControlFrameOptionImplemented,
       "dot11LsigTxopProtectionOptionImplemented": dot11LsigTxopProtectionOptionImplemented,
       "dot11MaxRxAMPDUFactor": dot11MaxRxAMPDUFactor,
       "dot11MinimumMPDUStartSpacing": dot11MinimumMPDUStartSpacing,
       "dot11PCOOptionImplemented": dot11PCOOptionImplemented,
       "dot11TransitionTime": dot11TransitionTime,
       "dot11MCSFeedbackOptionImplemented": dot11MCSFeedbackOptionImplemented,
       "dot11HTControlFieldSupported": dot11HTControlFieldSupported,
       "dot11RDResponderOptionImplemented": dot11RDResponderOptionImplemented,
       "dot11mac": dot11mac,
       "dot11OperationTable": dot11OperationTable,
       "dot11OperationEntry": dot11OperationEntry,
       "dot11MACAddress": dot11MACAddress,
       "dot11RTSThreshold": dot11RTSThreshold,
       "dot11ShortRetryLimit": dot11ShortRetryLimit,
       "dot11LongRetryLimit": dot11LongRetryLimit,
       "dot11FragmentationThreshold": dot11FragmentationThreshold,
       "dot11MaxTransmitMSDULifetime": dot11MaxTransmitMSDULifetime,
       "dot11MaxReceiveLifetime": dot11MaxReceiveLifetime,
       "dot11ManufacturerID": dot11ManufacturerID,
       "dot11ProductID": dot11ProductID,
       "dot11CAPLimit": dot11CAPLimit,
       "dot11HCCWmin": dot11HCCWmin,
       "dot11HCCWmax": dot11HCCWmax,
       "dot11HCCAIFSN": dot11HCCAIFSN,
       "dot11ADDBAResponseTimeout": dot11ADDBAResponseTimeout,
       "dot11ADDTSResponseTimeout": dot11ADDTSResponseTimeout,
       "dot11ChannelUtilizationBeaconInterval": dot11ChannelUtilizationBeaconInterval,
       "dot11ScheduleTimeout": dot11ScheduleTimeout,
       "dot11DLSResponseTimeout": dot11DLSResponseTimeout,
       "dot11QAPMissingAckRetryLimit": dot11QAPMissingAckRetryLimit,
       "dot11EDCAAveragingPeriod": dot11EDCAAveragingPeriod,
       "dot11HTOperatingMode": dot11HTOperatingMode,
       "dot11RIFSMode": dot11RIFSMode,
       "dot11PSMPControlledAccess": dot11PSMPControlledAccess,
       "dot11ServiceIntervalGranularity": dot11ServiceIntervalGranularity,
       "dot11DualCTSProtection": dot11DualCTSProtection,
       "dot11LSigTxopFullProtectionEnabled": dot11LSigTxopFullProtectionEnabled,
       "dot11NonGFEntitiesPresent": dot11NonGFEntitiesPresent,
       "dot11PCOActivated": dot11PCOActivated,
       "dot11PCO40MaxDuration": dot11PCO40MaxDuration,
       "dot11PCO20MaxDuration": dot11PCO20MaxDuration,
       "dot11PCO40MinDuration": dot11PCO40MinDuration,
       "dot11PCO20MinDuration": dot11PCO20MinDuration,
       "dot11CountersTable": dot11CountersTable,
       "dot11CountersEntry": dot11CountersEntry,
       "dot11TransmittedFragmentCount": dot11TransmittedFragmentCount,
       "dot11MulticastTransmittedFrameCount": dot11MulticastTransmittedFrameCount,
       "dot11FailedCount": dot11FailedCount,
       "dot11RetryCount": dot11RetryCount,
       "dot11MultipleRetryCount": dot11MultipleRetryCount,
       "dot11FrameDuplicateCount": dot11FrameDuplicateCount,
       "dot11RTSSuccessCount": dot11RTSSuccessCount,
       "dot11RTSFailureCount": dot11RTSFailureCount,
       "dot11ACKFailureCount": dot11ACKFailureCount,
       "dot11ReceivedFragmentCount": dot11ReceivedFragmentCount,
       "dot11MulticastReceivedFrameCount": dot11MulticastReceivedFrameCount,
       "dot11FCSErrorCount": dot11FCSErrorCount,
       "dot11TransmittedFrameCount": dot11TransmittedFrameCount,
       "dot11WEPUndecryptableCount": dot11WEPUndecryptableCount,
       "dot11QosDiscardedFragmentCount": dot11QosDiscardedFragmentCount,
       "dot11AssociatedStationCount": dot11AssociatedStationCount,
       "dot11QosCFPollsReceivedCount": dot11QosCFPollsReceivedCount,
       "dot11QosCFPollsUnusedCount": dot11QosCFPollsUnusedCount,
       "dot11QosCFPollsUnusableCount": dot11QosCFPollsUnusableCount,
       "dot11TransmittedAMSDUCount": dot11TransmittedAMSDUCount,
       "dot11FailedAMSDUCount": dot11FailedAMSDUCount,
       "dot11RetryAMSDUCount": dot11RetryAMSDUCount,
       "dot11MultipleRetryAMSDUCount": dot11MultipleRetryAMSDUCount,
       "dot11TransmittedOctetsInAMSDUCount": dot11TransmittedOctetsInAMSDUCount,
       "dot11AMSDUAckFailureCount": dot11AMSDUAckFailureCount,
       "dot11ReceivedAMSDUCount": dot11ReceivedAMSDUCount,
       "dot11ReceivedOctetsInAMSDUCount": dot11ReceivedOctetsInAMSDUCount,
       "dot11TransmittedAMPDUCount": dot11TransmittedAMPDUCount,
       "dot11TransmittedMPDUsInAMPDUCount": dot11TransmittedMPDUsInAMPDUCount,
       "dot11TransmittedOctetsInAMPDUCount": dot11TransmittedOctetsInAMPDUCount,
       "dot11AMPDUReceivedCount": dot11AMPDUReceivedCount,
       "dot11MPDUInReceivedAMPDUCount": dot11MPDUInReceivedAMPDUCount,
       "dot11ReceivedOctetsInAMPDUCount": dot11ReceivedOctetsInAMPDUCount,
       "dot11AMPDUDelimiterCRCErrorCount": dot11AMPDUDelimiterCRCErrorCount,
       "dot11ImplicitBARFailureCount": dot11ImplicitBARFailureCount,
       "dot11ExplicitBARFailureCount": dot11ExplicitBARFailureCount,
       "dot11ChannelWidthSwitchCount": dot11ChannelWidthSwitchCount,
       "dot11TwentyMHzFrameTransmittedCount": dot11TwentyMHzFrameTransmittedCount,
       "dot11FortyMHzFrameTransmittedCount": dot11FortyMHzFrameTransmittedCount,
       "dot11TwentyMHzFrameReceivedCount": dot11TwentyMHzFrameReceivedCount,
       "dot11FortyMHzFrameReceivedCount": dot11FortyMHzFrameReceivedCount,
       "dot11PSMPSuccessCount": dot11PSMPSuccessCount,
       "dot11PSMPFailureCount": dot11PSMPFailureCount,
       "dot11GrantedRDGUsedCount": dot11GrantedRDGUsedCount,
       "dot11GrantedRDGUnusedCount": dot11GrantedRDGUnusedCount,
       "dot11TransmittedFramesInGrantedRDGCount": dot11TransmittedFramesInGrantedRDGCount,
       "dot11TransmittedOctetsInGrantedRDGCount": dot11TransmittedOctetsInGrantedRDGCount,
       "dot11BeamformingFrameCount": dot11BeamformingFrameCount,
       "dot11DualCTSSuccessCount": dot11DualCTSSuccessCount,
       "dot11DualCTSFailureCount": dot11DualCTSFailureCount,
       "dot11STBCCTSSuccessCount": dot11STBCCTSSuccessCount,
       "dot11STBCCTSFailureCount": dot11STBCCTSFailureCount,
       "dot11nonSTBCCTSSuccessCount": dot11nonSTBCCTSSuccessCount,
       "dot11nonSTBCCTSFailureCount": dot11nonSTBCCTSFailureCount,
       "dot11RTSLSIGSuccessCount": dot11RTSLSIGSuccessCount,
       "dot11RTSLSIGFailureCount": dot11RTSLSIGFailureCount,
       "dot11GroupAddressesTable": dot11GroupAddressesTable,
       "dot11GroupAddressesEntry": dot11GroupAddressesEntry,
       "dot11GroupAddressesIndex": dot11GroupAddressesIndex,
       "dot11Address": dot11Address,
       "dot11GroupAddressesStatus": dot11GroupAddressesStatus,
       "dot11EDCATable": dot11EDCATable,
       "dot11EDCATableEntry": dot11EDCATableEntry,
       "dot11EDCATableIndex": dot11EDCATableIndex,
       "dot11EDCATableCWmin": dot11EDCATableCWmin,
       "dot11EDCATableCWmax": dot11EDCATableCWmax,
       "dot11EDCATableAIFSN": dot11EDCATableAIFSN,
       "dot11EDCATableTXOPLimit": dot11EDCATableTXOPLimit,
       "dot11EDCATableMSDULifetime": dot11EDCATableMSDULifetime,
       "dot11EDCATableMandatory": dot11EDCATableMandatory,
       "dot11QAPEDCATable": dot11QAPEDCATable,
       "dot11QAPEDCATableEntry": dot11QAPEDCATableEntry,
       "dot11QAPEDCATableIndex": dot11QAPEDCATableIndex,
       "dot11QAPEDCATableCWmin": dot11QAPEDCATableCWmin,
       "dot11QAPEDCATableCWmax": dot11QAPEDCATableCWmax,
       "dot11QAPEDCATableAIFSN": dot11QAPEDCATableAIFSN,
       "dot11QAPEDCATableTXOPLimit": dot11QAPEDCATableTXOPLimit,
       "dot11QAPEDCATableMSDULifetime": dot11QAPEDCATableMSDULifetime,
       "dot11QAPEDCATableMandatory": dot11QAPEDCATableMandatory,
       "dot11QosCountersTable": dot11QosCountersTable,
       "dot11QosCountersEntry": dot11QosCountersEntry,
       "dot11QosCountersIndex": dot11QosCountersIndex,
       "dot11QosTransmittedFragmentCount": dot11QosTransmittedFragmentCount,
       "dot11QosFailedCount": dot11QosFailedCount,
       "dot11QosRetryCount": dot11QosRetryCount,
       "dot11QosMultipleRetryCount": dot11QosMultipleRetryCount,
       "dot11QosFrameDuplicateCount": dot11QosFrameDuplicateCount,
       "dot11QosRTSSuccessCount": dot11QosRTSSuccessCount,
       "dot11QosRTSFailureCount": dot11QosRTSFailureCount,
       "dot11QosACKFailureCount": dot11QosACKFailureCount,
       "dot11QosReceivedFragmentCount": dot11QosReceivedFragmentCount,
       "dot11QosTransmittedFrameCount": dot11QosTransmittedFrameCount,
       "dot11QosDiscardedFrameCount": dot11QosDiscardedFrameCount,
       "dot11QosMPDUsReceivedCount": dot11QosMPDUsReceivedCount,
       "dot11QosRetriesReceivedCount": dot11QosRetriesReceivedCount,
       "dot11res": dot11res,
       "dot11resAttribute": dot11resAttribute,
       "dot11ResourceTypeIDName": dot11ResourceTypeIDName,
       "dot11ResourceInfoTable": dot11ResourceInfoTable,
       "dot11ResourceInfoEntry": dot11ResourceInfoEntry,
       "dot11manufacturerOUI": dot11manufacturerOUI,
       "dot11manufacturerName": dot11manufacturerName,
       "dot11manufacturerProductName": dot11manufacturerProductName,
       "dot11manufacturerProductVersion": dot11manufacturerProductVersion,
       "dot11phy": dot11phy,
       "dot11PhyOperationTable": dot11PhyOperationTable,
       "dot11PhyOperationEntry": dot11PhyOperationEntry,
       "dot11PHYType": dot11PHYType,
       "dot11CurrentRegDomain": dot11CurrentRegDomain,
       "dot11TempType": dot11TempType,
       "dot11PhyAntennaTable": dot11PhyAntennaTable,
       "dot11PhyAntennaEntry": dot11PhyAntennaEntry,
       "dot11CurrentTxAntenna": dot11CurrentTxAntenna,
       "dot11DiversitySupport": dot11DiversitySupport,
       "dot11CurrentRxAntenna": dot11CurrentRxAntenna,
       "dot11AntennaSelectionOptionImplemented": dot11AntennaSelectionOptionImplemented,
       "dot11TransmitExplicitCSIFeedbackASOptionImplemented": dot11TransmitExplicitCSIFeedbackASOptionImplemented,
       "dot11TransmitIndicesFeedbackASOptionImplemented": dot11TransmitIndicesFeedbackASOptionImplemented,
       "dot11ExplicitCSIFeedbackASOptionImplemented": dot11ExplicitCSIFeedbackASOptionImplemented,
       "dot11TransmitIndicesComputationFeedbackASOptionImplemented": dot11TransmitIndicesComputationFeedbackASOptionImplemented,
       "dot11ReceiveAntennaSelectionOptionImplemented": dot11ReceiveAntennaSelectionOptionImplemented,
       "dot11TransmitSoundingPPDUOptionImplemented": dot11TransmitSoundingPPDUOptionImplemented,
       "dot11PhyTxPowerTable": dot11PhyTxPowerTable,
       "dot11PhyTxPowerEntry": dot11PhyTxPowerEntry,
       "dot11NumberSupportedPowerLevels": dot11NumberSupportedPowerLevels,
       "dot11TxPowerLevel1": dot11TxPowerLevel1,
       "dot11TxPowerLevel2": dot11TxPowerLevel2,
       "dot11TxPowerLevel3": dot11TxPowerLevel3,
       "dot11TxPowerLevel4": dot11TxPowerLevel4,
       "dot11TxPowerLevel5": dot11TxPowerLevel5,
       "dot11TxPowerLevel6": dot11TxPowerLevel6,
       "dot11TxPowerLevel7": dot11TxPowerLevel7,
       "dot11TxPowerLevel8": dot11TxPowerLevel8,
       "dot11CurrentTxPowerLevel": dot11CurrentTxPowerLevel,
       "dot11PhyFHSSTable": dot11PhyFHSSTable,
       "dot11PhyFHSSEntry": dot11PhyFHSSEntry,
       "dot11HopTime": dot11HopTime,
       "dot11CurrentChannelNumber": dot11CurrentChannelNumber,
       "dot11MaxDwellTime": dot11MaxDwellTime,
       "dot11CurrentDwellTime": dot11CurrentDwellTime,
       "dot11CurrentSet": dot11CurrentSet,
       "dot11CurrentPattern": dot11CurrentPattern,
       "dot11CurrentIndex": dot11CurrentIndex,
       "dot11EHCCPrimeRadix": dot11EHCCPrimeRadix,
       "dot11EHCCNumberofChannelsFamilyIndex": dot11EHCCNumberofChannelsFamilyIndex,
       "dot11EHCCCapabilityImplemented": dot11EHCCCapabilityImplemented,
       "dot11EHCCCapabilityEnabled": dot11EHCCCapabilityEnabled,
       "dot11HopAlgorithmAdopted": dot11HopAlgorithmAdopted,
       "dot11RandomTableFlag": dot11RandomTableFlag,
       "dot11NumberofHoppingSets": dot11NumberofHoppingSets,
       "dot11HopModulus": dot11HopModulus,
       "dot11HopOffset": dot11HopOffset,
       "dot11PhyDSSSTable": dot11PhyDSSSTable,
       "dot11PhyDSSSEntry": dot11PhyDSSSEntry,
       "dot11CurrentChannel": dot11CurrentChannel,
       "dot11CCAModeSupported": dot11CCAModeSupported,
       "dot11CurrentCCAMode": dot11CurrentCCAMode,
       "dot11EDThreshold": dot11EDThreshold,
       "dot11PhyIRTable": dot11PhyIRTable,
       "dot11PhyIREntry": dot11PhyIREntry,
       "dot11CCAWatchdogTimerMax": dot11CCAWatchdogTimerMax,
       "dot11CCAWatchdogCountMax": dot11CCAWatchdogCountMax,
       "dot11CCAWatchdogTimerMin": dot11CCAWatchdogTimerMin,
       "dot11CCAWatchdogCountMin": dot11CCAWatchdogCountMin,
       "dot11RegDomainsSupportedTable": dot11RegDomainsSupportedTable,
       "dot11RegDomainsSupportEntry": dot11RegDomainsSupportEntry,
       "dot11RegDomainsSupportIndex": dot11RegDomainsSupportIndex,
       "dot11RegDomainsSupportValue": dot11RegDomainsSupportValue,
       "dot11AntennasListTable": dot11AntennasListTable,
       "dot11AntennasListEntry": dot11AntennasListEntry,
       "dot11AntennaListIndex": dot11AntennaListIndex,
       "dot11SupportedTxAntenna": dot11SupportedTxAntenna,
       "dot11SupportedRxAntenna": dot11SupportedRxAntenna,
       "dot11DiversitySelectionRx": dot11DiversitySelectionRx,
       "dot11SupportedDataRatesTxTable": dot11SupportedDataRatesTxTable,
       "dot11SupportedDataRatesTxEntry": dot11SupportedDataRatesTxEntry,
       "dot11SupportedDataRatesTxIndex": dot11SupportedDataRatesTxIndex,
       "dot11SupportedDataRatesTxValue": dot11SupportedDataRatesTxValue,
       "dot11SupportedDataRatesRxTable": dot11SupportedDataRatesRxTable,
       "dot11SupportedDataRatesRxEntry": dot11SupportedDataRatesRxEntry,
       "dot11SupportedDataRatesRxIndex": dot11SupportedDataRatesRxIndex,
       "dot11SupportedDataRatesRxValue": dot11SupportedDataRatesRxValue,
       "dot11PhyOFDMTable": dot11PhyOFDMTable,
       "dot11PhyOFDMEntry": dot11PhyOFDMEntry,
       "dot11CurrentFrequency": dot11CurrentFrequency,
       "dot11TIThreshold": dot11TIThreshold,
       "dot11FrequencyBandsSupported": dot11FrequencyBandsSupported,
       "dot11PhyHRDSSSTable": dot11PhyHRDSSSTable,
       "dot11PhyHRDSSSEntry": dot11PhyHRDSSSEntry,
       "dot11ChannelAgilityPresent": dot11ChannelAgilityPresent,
       "dot11ChannelAgilityEnabled": dot11ChannelAgilityEnabled,
       "dot11HRCCAModeSupported": dot11HRCCAModeSupported,
       "dot11ShortPreambleOptionImplemented": dot11ShortPreambleOptionImplemented,
       "dot11PBCCOptionImplemented": dot11PBCCOptionImplemented,
       "dot11HoppingPatternTable": dot11HoppingPatternTable,
       "dot11HoppingPatternEntry": dot11HoppingPatternEntry,
       "dot11HoppingPatternIndex": dot11HoppingPatternIndex,
       "dot11RandomTableFieldNumber": dot11RandomTableFieldNumber,
       "dot11PhyERPTable": dot11PhyERPTable,
       "dot11PhyERPEntry": dot11PhyERPEntry,
       "dot11ERPPBCCOptionImplemented": dot11ERPPBCCOptionImplemented,
       "dot11ERPBCCOptionEnabled": dot11ERPBCCOptionEnabled,
       "dot11DSSSOFDMOptionImplemented": dot11DSSSOFDMOptionImplemented,
       "dot11DSSSOFDMOptionEnabled": dot11DSSSOFDMOptionEnabled,
       "dot11ShortSlotTimeOptionImplemented": dot11ShortSlotTimeOptionImplemented,
       "dot11ShortSlotTimeOptionEnabled": dot11ShortSlotTimeOptionEnabled,
       "dot11PhyHTTable": dot11PhyHTTable,
       "dot11PhyHTEntry": dot11PhyHTEntry,
       "dot11FortyMHzOperationImplemented": dot11FortyMHzOperationImplemented,
       "dot11FortyMHzOperationEnabled": dot11FortyMHzOperationEnabled,
       "dot11CurrentPrimaryChannel": dot11CurrentPrimaryChannel,
       "dot11CurrentSecondaryChannel": dot11CurrentSecondaryChannel,
       "dot11NumberOfSpatialStreamsImplemented": dot11NumberOfSpatialStreamsImplemented,
       "dot11NumberOfSpatialStreamsEnabled": dot11NumberOfSpatialStreamsEnabled,
       "dot11GreenfieldOptionImplemented": dot11GreenfieldOptionImplemented,
       "dot11GreenfieldOptionEnabled": dot11GreenfieldOptionEnabled,
       "dot11ShortGIOptionInTwentyImplemented": dot11ShortGIOptionInTwentyImplemented,
       "dot11ShortGIOptionInTwentyEnabled": dot11ShortGIOptionInTwentyEnabled,
       "dot11ShortGIOptionInFortyImplemented": dot11ShortGIOptionInFortyImplemented,
       "dot11ShortGIOptionInFortyEnabled": dot11ShortGIOptionInFortyEnabled,
       "dot11LDPCCodingOptionImplemented": dot11LDPCCodingOptionImplemented,
       "dot11LDPCCodingOptionEnabled": dot11LDPCCodingOptionEnabled,
       "dot11TxSTBCOptionImplemented": dot11TxSTBCOptionImplemented,
       "dot11TxSTBCOptionEnabled": dot11TxSTBCOptionEnabled,
       "dot11RxSTBCOptionImplemented": dot11RxSTBCOptionImplemented,
       "dot11RxSTBCOptionEnabled": dot11RxSTBCOptionEnabled,
       "dot11BeamFormingOptionImplemented": dot11BeamFormingOptionImplemented,
       "dot11BeamFormingOptionEnabled": dot11BeamFormingOptionEnabled,
       "dot11HighestSupportedDataRate": dot11HighestSupportedDataRate,
       "dot11TxMCSSetDefined": dot11TxMCSSetDefined,
       "dot11TxRxMCSSetNotEqual": dot11TxRxMCSSetNotEqual,
       "dot11TxMaximumNumberSpatialStreamsSupported": dot11TxMaximumNumberSpatialStreamsSupported,
       "dot11TxUnequalModulationSupported": dot11TxUnequalModulationSupported,
       "dot11SupportedMCSTxTable": dot11SupportedMCSTxTable,
       "dot11SupportedMCSTxEntry": dot11SupportedMCSTxEntry,
       "dot11SupportedMCSTxIndex": dot11SupportedMCSTxIndex,
       "dot11SupportedMCSTxValue": dot11SupportedMCSTxValue,
       "dot11SupportedMCSRxTable": dot11SupportedMCSRxTable,
       "dot11SupportedMCSRxEntry": dot11SupportedMCSRxEntry,
       "dot11SupportedMCSRxIndex": dot11SupportedMCSRxIndex,
       "dot11SupportedMCSRxValue": dot11SupportedMCSRxValue,
       "dot11TxBFConfigTable": dot11TxBFConfigTable,
       "dot11TxBFConfigEntry": dot11TxBFConfigEntry,
       "dot11ReceiveStaggerSoundingOptionImplemented": dot11ReceiveStaggerSoundingOptionImplemented,
       "dot11TransmitStaggerSoundingOptionImplemented": dot11TransmitStaggerSoundingOptionImplemented,
       "dot11ReceiveNDPOptionImplemented": dot11ReceiveNDPOptionImplemented,
       "dot11TransmitNDPOptionImplemented": dot11TransmitNDPOptionImplemented,
       "dot11ImplicitTxBFOptionImplemented": dot11ImplicitTxBFOptionImplemented,
       "dot11CalibrationOptionImplemented": dot11CalibrationOptionImplemented,
       "dot11ExplicitCSITxBFOptionImplemented": dot11ExplicitCSITxBFOptionImplemented,
       "dot11ExplicitNonCompressedbeamformingMatrixOptionImplemented": dot11ExplicitNonCompressedbeamformingMatrixOptionImplemented,
       "dot11ExplicitBFCSIFeedbackOptionImplemented": dot11ExplicitBFCSIFeedbackOptionImplemented,
       "dot11ExplicitNonCompressedbeamformingMatrixFeedbackOptionImplemented": dot11ExplicitNonCompressedbeamformingMatrixFeedbackOptionImplemented,
       "dot11ExplicitCompressedbeamformingMatrixFeedbackOptionImplemented": dot11ExplicitCompressedbeamformingMatrixFeedbackOptionImplemented,
       "dot11NumberBeamFormingCSISupportAntenna": dot11NumberBeamFormingCSISupportAntenna,
       "dot11NumberNonCompressedbeamformingMatrixSupportAntenna": dot11NumberNonCompressedbeamformingMatrixSupportAntenna,
       "dot11NumberCompressedbeamformingMatrixSupportAntenna": dot11NumberCompressedbeamformingMatrixSupportAntenna,
       "dot11MaxCSIFeedbackDelay": dot11MaxCSIFeedbackDelay,
       "dot11Conformance": dot11Conformance,
       "dot11Groups": dot11Groups,
       "dot11SMTbase": dot11SMTbase,
       "dot11SMTprivacy": dot11SMTprivacy,
       "dot11MACbase": dot11MACbase,
       "dot11MACStatistics": dot11MACStatistics,
       "dot11ResourceTypeID": dot11ResourceTypeID,
       "dot11SmtAuthenticationAlgorithms": dot11SmtAuthenticationAlgorithms,
       "dot11PhyOperationComplianceGroup": dot11PhyOperationComplianceGroup,
       "dot11PhyAntennaComplianceGroup": dot11PhyAntennaComplianceGroup,
       "dot11PhyTxPowerComplianceGroup": dot11PhyTxPowerComplianceGroup,
       "dot11PhyFHSSComplianceGroup": dot11PhyFHSSComplianceGroup,
       "dot11PhyDSSSComplianceGroup": dot11PhyDSSSComplianceGroup,
       "dot11PhyIRComplianceGroup": dot11PhyIRComplianceGroup,
       "dot11PhyRegDomainsSupportGroup": dot11PhyRegDomainsSupportGroup,
       "dot11PhyAntennasListGroup": dot11PhyAntennasListGroup,
       "dot11PhyRateGroup": dot11PhyRateGroup,
       "dot11CountersGroup": dot11CountersGroup,
       "dot11NotificationGroup": dot11NotificationGroup,
       "dot11SMTbase2": dot11SMTbase2,
       "dot11PhyHRDSSSComplianceGroup": dot11PhyHRDSSSComplianceGroup,
       "dot11SMTbase3": dot11SMTbase3,
       "dot11MultiDomainCapabilityGroup": dot11MultiDomainCapabilityGroup,
       "dot11PhyFHSSComplianceGroup2": dot11PhyFHSSComplianceGroup2,
       "dot11PhyOFDMComplianceGroup": dot11PhyOFDMComplianceGroup,
       "dot11PhyERPComplianceGroup": dot11PhyERPComplianceGroup,
       "dot11RSNAadditions": dot11RSNAadditions,
       "dot11SMTbase4": dot11SMTbase4,
       "dot11RSNPMKcachingGroup": dot11RSNPMKcachingGroup,
       "dot11MACbase2": dot11MACbase2,
       "dot11CountersGroup2": dot11CountersGroup2,
       "dot11Qosadditions": dot11Qosadditions,
       "dot11SMTbase6": dot11SMTbase6,
       "dot11PhyAntennaComplianceGroup2": dot11PhyAntennaComplianceGroup2,
       "dot11MACbase3": dot11MACbase3,
       "dot11CountersGroup3": dot11CountersGroup3,
       "dot11SMTbase9": dot11SMTbase9,
       "dot11PhyMCSGroup": dot11PhyMCSGroup,
       "dot1PhyHTComplianceGroup": dot1PhyHTComplianceGroup,
       "dot11HTMACAdditions": dot11HTMACAdditions,
       "dot11TxBFGroup": dot11TxBFGroup,
       "dot11RSNBase": dot11RSNBase,
       "dot11Compliances": dot11Compliances,
       "dot11Compliance": dot11Compliance,
       "dot11RSNCompliance": dot11RSNCompliance}
)
