# SNMP MIB module (GANDALF-ENTERPRISE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GANDALF-ENTERPRISE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:47:39 2024
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Gandalf_ObjectIdentity = ObjectIdentity
gandalf = _Gandalf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64)
)
_Gandalf_hub_ObjectIdentity = ObjectIdentity
gandalf_hub = _Gandalf_hub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 1)
)
_HmBasicCapability_ObjectIdentity = ObjectIdentity
hmBasicCapability = _HmBasicCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 1, 1)
)


class _HubBasicID_Type(OctetString):
    """Custom type hubBasicID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_HubBasicID_Type.__name__ = "OctetString"
_HubBasicID_Object = MibScalar
hubBasicID = _HubBasicID_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 1, 1),
    _HubBasicID_Type()
)
hubBasicID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubBasicID.setStatus("mandatory")
_HubCardCapacity_Type = Integer32
_HubCardCapacity_Object = MibScalar
hubCardCapacity = _HubCardCapacity_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 1, 2),
    _HubCardCapacity_Type()
)
hubCardCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubCardCapacity.setStatus("mandatory")


class _HubCardMap_Type(OctetString):
    """Custom type hubCardMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_HubCardMap_Type.__name__ = "OctetString"
_HubCardMap_Object = MibScalar
hubCardMap = _HubCardMap_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 1, 3),
    _HubCardMap_Type()
)
hubCardMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubCardMap.setStatus("mandatory")
_HubNumOfRelays_Type = Integer32
_HubNumOfRelays_Object = MibScalar
hubNumOfRelays = _HubNumOfRelays_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 1, 4),
    _HubNumOfRelays_Type()
)
hubNumOfRelays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubNumOfRelays.setStatus("mandatory")
_HubRelayActive_Type = Integer32
_HubRelayActive_Object = MibScalar
hubRelayActive = _HubRelayActive_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 1, 5),
    _HubRelayActive_Type()
)
hubRelayActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubRelayActive.setStatus("mandatory")
_HubResourceType_Type = Integer32
_HubResourceType_Object = MibScalar
hubResourceType = _HubResourceType_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 1, 6),
    _HubResourceType_Type()
)
hubResourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubResourceType.setStatus("mandatory")
_HubStandardRevision_Type = Integer32
_HubStandardRevision_Object = MibScalar
hubStandardRevision = _HubStandardRevision_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 1, 7),
    _HubStandardRevision_Type()
)
hubStandardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubStandardRevision.setStatus("mandatory")


class _HubIEEE8023LmeOptions_Type(OctetString):
    """Custom type hubIEEE8023LmeOptions based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_HubIEEE8023LmeOptions_Type.__name__ = "OctetString"
_HubIEEE8023LmeOptions_Object = MibScalar
hubIEEE8023LmeOptions = _HubIEEE8023LmeOptions_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 1, 8),
    _HubIEEE8023LmeOptions_Type()
)
hubIEEE8023LmeOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubIEEE8023LmeOptions.setStatus("mandatory")


class _HubManID_Type(OctetString):
    """Custom type hubManID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_HubManID_Type.__name__ = "OctetString"
_HubManID_Object = MibScalar
hubManID = _HubManID_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 1, 9),
    _HubManID_Type()
)
hubManID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubManID.setStatus("mandatory")


class _HubManProductID_Type(OctetString):
    """Custom type hubManProductID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_HubManProductID_Type.__name__ = "OctetString"
_HubManProductID_Object = MibScalar
hubManProductID = _HubManProductID_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 1, 10),
    _HubManProductID_Type()
)
hubManProductID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubManProductID.setStatus("mandatory")


class _HubManProductVersion_Type(OctetString):
    """Custom type hubManProductVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_HubManProductVersion_Type.__name__ = "OctetString"
_HubManProductVersion_Object = MibScalar
hubManProductVersion = _HubManProductVersion_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 1, 11),
    _HubManProductVersion_Type()
)
hubManProductVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubManProductVersion.setStatus("mandatory")


class _HubManTelephoneNum_Type(OctetString):
    """Custom type hubManTelephoneNum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(33, 33),
    )


_HubManTelephoneNum_Type.__name__ = "OctetString"
_HubManTelephoneNum_Object = MibScalar
hubManTelephoneNum = _HubManTelephoneNum_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 1, 12),
    _HubManTelephoneNum_Type()
)
hubManTelephoneNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hubManTelephoneNum.setStatus("mandatory")


class _HubName_Type(OctetString):
    """Custom type hubName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_HubName_Type.__name__ = "OctetString"
_HubName_Object = MibScalar
hubName = _HubName_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 1, 13),
    _HubName_Type()
)
hubName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hubName.setStatus("mandatory")
_HubIPaddress_Type = IpAddress
_HubIPaddress_Object = MibScalar
hubIPaddress = _HubIPaddress_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 1, 14),
    _HubIPaddress_Type()
)
hubIPaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubIPaddress.setStatus("mandatory")


class _HubEEpromRev_Type(OctetString):
    """Custom type hubEEpromRev based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_HubEEpromRev_Type.__name__ = "OctetString"
_HubEEpromRev_Object = MibScalar
hubEEpromRev = _HubEEpromRev_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 1, 15),
    _HubEEpromRev_Type()
)
hubEEpromRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubEEpromRev.setStatus("mandatory")


class _HubSecureMode_Type(Integer32):
    """Custom type hubSecureMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_HubSecureMode_Type.__name__ = "Integer32"
_HubSecureMode_Object = MibScalar
hubSecureMode = _HubSecureMode_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 1, 16),
    _HubSecureMode_Type()
)
hubSecureMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hubSecureMode.setStatus("mandatory")
_HmBasicCardTable_Object = MibTable
hmBasicCardTable = _HmBasicCardTable_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 1, 17)
)
if mibBuilder.loadTexts:
    hmBasicCardTable.setStatus("mandatory")
_HmBasicCardEntry_Object = MibTableRow
hmBasicCardEntry = _HmBasicCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 1, 17, 1)
)
hmBasicCardEntry.setIndexNames(
    (0, "GANDALF-ENTERPRISE-MIB", "gCardID"),
)
if mibBuilder.loadTexts:
    hmBasicCardEntry.setStatus("mandatory")


class _GCardID_Type(Integer32):
    """Custom type gCardID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_GCardID_Type.__name__ = "Integer32"
_GCardID_Object = MibTableColumn
gCardID = _GCardID_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 1, 17, 1, 1),
    _GCardID_Type()
)
gCardID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gCardID.setStatus("mandatory")


class _GCardNumberOfPorts_Type(Integer32):
    """Custom type gCardNumberOfPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_GCardNumberOfPorts_Type.__name__ = "Integer32"
_GCardNumberOfPorts_Object = MibTableColumn
gCardNumberOfPorts = _GCardNumberOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 1, 17, 1, 2),
    _GCardNumberOfPorts_Type()
)
gCardNumberOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gCardNumberOfPorts.setStatus("mandatory")


class _GCardName_Type(OctetString):
    """Custom type gCardName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_GCardName_Type.__name__ = "OctetString"
_GCardName_Object = MibTableColumn
gCardName = _GCardName_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 1, 17, 1, 3),
    _GCardName_Type()
)
gCardName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gCardName.setStatus("mandatory")
_GCardType_Type = OctetString
_GCardType_Object = MibTableColumn
gCardType = _GCardType_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 1, 17, 1, 4),
    _GCardType_Type()
)
gCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gCardType.setStatus("mandatory")


class _GCardRingNumberA_Type(Integer32):
    """Custom type gCardRingNumberA based on Integer32"""
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
        *(("ring1", 1),
          ("ring2", 2),
          ("ring3", 3),
          ("ring4", 4),
          ("standalone", 5))
    )


_GCardRingNumberA_Type.__name__ = "Integer32"
_GCardRingNumberA_Object = MibTableColumn
gCardRingNumberA = _GCardRingNumberA_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 1, 17, 1, 5),
    _GCardRingNumberA_Type()
)
gCardRingNumberA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gCardRingNumberA.setStatus("mandatory")


class _GCardRingNumberB_Type(Integer32):
    """Custom type gCardRingNumberB based on Integer32"""
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
        *(("ring1", 1),
          ("ring2", 2),
          ("ring3", 3),
          ("ring4", 4),
          ("standalone", 5))
    )


_GCardRingNumberB_Type.__name__ = "Integer32"
_GCardRingNumberB_Object = MibTableColumn
gCardRingNumberB = _GCardRingNumberB_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 1, 17, 1, 6),
    _GCardRingNumberB_Type()
)
gCardRingNumberB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gCardRingNumberB.setStatus("mandatory")


class _GCardIbmModeA_Type(Integer32):
    """Custom type gCardIbmModeA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ibmMode", 2),
          ("nonIbmMode", 1))
    )


_GCardIbmModeA_Type.__name__ = "Integer32"
_GCardIbmModeA_Object = MibTableColumn
gCardIbmModeA = _GCardIbmModeA_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 1, 17, 1, 7),
    _GCardIbmModeA_Type()
)
gCardIbmModeA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gCardIbmModeA.setStatus("mandatory")


class _GCardIbmModeB_Type(Integer32):
    """Custom type gCardIbmModeB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ibmMode", 1),
          ("nonIbmMode", 2))
    )


_GCardIbmModeB_Type.__name__ = "Integer32"
_GCardIbmModeB_Object = MibTableColumn
gCardIbmModeB = _GCardIbmModeB_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 1, 17, 1, 8),
    _GCardIbmModeB_Type()
)
gCardIbmModeB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gCardIbmModeB.setStatus("mandatory")


class _GCardRingSpeedA_Type(Integer32):
    """Custom type gCardRingSpeedA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              16,
              255)
        )
    )
    namedValues = NamedValues(
        *(("fourMbps", 4),
          ("sixteenMbps", 16),
          ("unknown", 255))
    )


_GCardRingSpeedA_Type.__name__ = "Integer32"
_GCardRingSpeedA_Object = MibTableColumn
gCardRingSpeedA = _GCardRingSpeedA_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 1, 17, 1, 9),
    _GCardRingSpeedA_Type()
)
gCardRingSpeedA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gCardRingSpeedA.setStatus("mandatory")


class _GCardRingSpeedB_Type(Integer32):
    """Custom type gCardRingSpeedB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              16,
              255)
        )
    )
    namedValues = NamedValues(
        *(("fourMbps", 4),
          ("sixteenMbps", 16),
          ("unknown", 255))
    )


_GCardRingSpeedB_Type.__name__ = "Integer32"
_GCardRingSpeedB_Object = MibTableColumn
gCardRingSpeedB = _GCardRingSpeedB_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 1, 17, 1, 10),
    _GCardRingSpeedB_Type()
)
gCardRingSpeedB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gCardRingSpeedB.setStatus("mandatory")
_HmBasicPortTable_Object = MibTable
hmBasicPortTable = _HmBasicPortTable_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 1, 18)
)
if mibBuilder.loadTexts:
    hmBasicPortTable.setStatus("mandatory")
_HmBasicPortEntry_Object = MibTableRow
hmBasicPortEntry = _HmBasicPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 1, 18, 1)
)
hmBasicPortEntry.setIndexNames(
    (0, "GANDALF-ENTERPRISE-MIB", "gCardBasicID"),
    (0, "GANDALF-ENTERPRISE-MIB", "gPortID"),
)
if mibBuilder.loadTexts:
    hmBasicPortEntry.setStatus("mandatory")


class _GCardBasicID_Type(Integer32):
    """Custom type gCardBasicID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_GCardBasicID_Type.__name__ = "Integer32"
_GCardBasicID_Object = MibTableColumn
gCardBasicID = _GCardBasicID_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 1, 18, 1, 1),
    _GCardBasicID_Type()
)
gCardBasicID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gCardBasicID.setStatus("mandatory")


class _GPortID_Type(Integer32):
    """Custom type gPortID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_GPortID_Type.__name__ = "Integer32"
_GPortID_Object = MibTableColumn
gPortID = _GPortID_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 1, 18, 1, 2),
    _GPortID_Type()
)
gPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gPortID.setStatus("mandatory")


class _GPortType_Type(Integer32):
    """Custom type gPortType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("aui", 1),
          ("bnc", 2),
          ("fsma", 7),
          ("other", 8),
          ("rj45", 3),
          ("rj71", 4),
          ("st", 6),
          ("thin", 5))
    )


_GPortType_Type.__name__ = "Integer32"
_GPortType_Object = MibTableColumn
gPortType = _GPortType_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 1, 18, 1, 3),
    _GPortType_Type()
)
gPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gPortType.setStatus("mandatory")


class _GPortAdminState_Type(Integer32):
    """Custom type gPortAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_GPortAdminState_Type.__name__ = "Integer32"
_GPortAdminState_Object = MibTableColumn
gPortAdminState = _GPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 1, 18, 1, 4),
    _GPortAdminState_Type()
)
gPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gPortAdminState.setStatus("mandatory")


class _GPortAutoPartitionState_Type(Integer32):
    """Custom type gPortAutoPartitionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoPartitioned", 3),
          ("nonAutoPartitioned", 2),
          ("other", 1))
    )


_GPortAutoPartitionState_Type.__name__ = "Integer32"
_GPortAutoPartitionState_Object = MibTableColumn
gPortAutoPartitionState = _GPortAutoPartitionState_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 1, 18, 1, 5),
    _GPortAutoPartitionState_Type()
)
gPortAutoPartitionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gPortAutoPartitionState.setStatus("mandatory")


class _GPortName_Type(OctetString):
    """Custom type gPortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_GPortName_Type.__name__ = "OctetString"
_GPortName_Object = MibTableColumn
gPortName = _GPortName_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 1, 18, 1, 6),
    _GPortName_Type()
)
gPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gPortName.setStatus("mandatory")


class _GPortEffectiveState_Type(Integer32):
    """Custom type gPortEffectiveState based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("masterActive", 4),
          ("masterDisabled", 6),
          ("masterFaulty", 5),
          ("masterReady", 3),
          ("standbyActive", 8),
          ("standbyDisabled", 10),
          ("standbyFaulty", 9),
          ("standbyReady", 7))
    )


_GPortEffectiveState_Type.__name__ = "Integer32"
_GPortEffectiveState_Object = MibTableColumn
gPortEffectiveState = _GPortEffectiveState_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 1, 18, 1, 7),
    _GPortEffectiveState_Type()
)
gPortEffectiveState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gPortEffectiveState.setStatus("mandatory")


class _GPortConfiguration_Type(Integer32):
    """Custom type gPortConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("master", 2),
          ("nonRedundant", 1),
          ("standby", 3))
    )


_GPortConfiguration_Type.__name__ = "Integer32"
_GPortConfiguration_Object = MibTableColumn
gPortConfiguration = _GPortConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 1, 18, 1, 8),
    _GPortConfiguration_Type()
)
gPortConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gPortConfiguration.setStatus("mandatory")


class _GPortRedundantPort_Type(Integer32):
    """Custom type gPortRedundantPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_GPortRedundantPort_Type.__name__ = "Integer32"
_GPortRedundantPort_Object = MibTableColumn
gPortRedundantPort = _GPortRedundantPort_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 1, 18, 1, 9),
    _GPortRedundantPort_Type()
)
gPortRedundantPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gPortRedundantPort.setStatus("mandatory")


class _GPortRedundantCard_Type(Integer32):
    """Custom type gPortRedundantCard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_GPortRedundantCard_Type.__name__ = "Integer32"
_GPortRedundantCard_Object = MibTableColumn
gPortRedundantCard = _GPortRedundantCard_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 1, 18, 1, 10),
    _GPortRedundantCard_Type()
)
gPortRedundantCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gPortRedundantCard.setStatus("mandatory")


class _GPortLinkStatus_Type(Integer32):
    """Custom type gPortLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 2),
          ("linkUp", 1))
    )


_GPortLinkStatus_Type.__name__ = "Integer32"
_GPortLinkStatus_Object = MibTableColumn
gPortLinkStatus = _GPortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 1, 18, 1, 11),
    _GPortLinkStatus_Type()
)
gPortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gPortLinkStatus.setStatus("mandatory")
_HmSelfTestCapability_ObjectIdentity = ObjectIdentity
hmSelfTestCapability = _HmSelfTestCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 1, 2)
)


class _HubSelfTestID_Type(OctetString):
    """Custom type hubSelfTestID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_HubSelfTestID_Type.__name__ = "OctetString"
_HubSelfTestID_Object = MibScalar
hubSelfTestID = _HubSelfTestID_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 2, 1),
    _HubSelfTestID_Type()
)
hubSelfTestID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubSelfTestID.setStatus("mandatory")
_HubTimeSinceReset_Type = TimeTicks
_HubTimeSinceReset_Object = MibScalar
hubTimeSinceReset = _HubTimeSinceReset_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 2, 2),
    _HubTimeSinceReset_Type()
)
hubTimeSinceReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubTimeSinceReset.setStatus("mandatory")
_HubResetTimeStamp_Type = TimeTicks
_HubResetTimeStamp_Object = MibScalar
hubResetTimeStamp = _HubResetTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 2, 3),
    _HubResetTimeStamp_Type()
)
hubResetTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubResetTimeStamp.setStatus("mandatory")


class _HubHealthState_Type(Integer32):
    """Custom type hubHealthState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 3),
          ("ok", 2),
          ("other", 1))
    )


_HubHealthState_Type.__name__ = "Integer32"
_HubHealthState_Object = MibScalar
hubHealthState = _HubHealthState_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 2, 4),
    _HubHealthState_Type()
)
hubHealthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubHealthState.setStatus("mandatory")


class _HubHealthText_Type(DisplayString):
    """Custom type hubHealthText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HubHealthText_Type.__name__ = "DisplayString"
_HubHealthText_Object = MibScalar
hubHealthText = _HubHealthText_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 2, 5),
    _HubHealthText_Type()
)
hubHealthText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubHealthText.setStatus("mandatory")


class _HubHealthData_Type(OctetString):
    """Custom type hubHealthData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HubHealthData_Type.__name__ = "OctetString"
_HubHealthData_Object = MibScalar
hubHealthData = _HubHealthData_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 2, 6),
    _HubHealthData_Type()
)
hubHealthData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubHealthData.setStatus("mandatory")


class _HubSystemResetting_Type(Integer32):
    """Custom type hubSystemResetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notResetting", 1),
          ("resetting", 2))
    )


_HubSystemResetting_Type.__name__ = "Integer32"
_HubSystemResetting_Object = MibScalar
hubSystemResetting = _HubSystemResetting_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 2, 7),
    _HubSystemResetting_Type()
)
hubSystemResetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubSystemResetting.setStatus("mandatory")


class _HubResetting_Type(Integer32):
    """Custom type hubResetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notResetting", 1),
          ("resetting", 2))
    )


_HubResetting_Type.__name__ = "Integer32"
_HubResetting_Object = MibScalar
hubResetting = _HubResetting_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 2, 8),
    _HubResetting_Type()
)
hubResetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubResetting.setStatus("mandatory")


class _HubExecutingSelfTest_Type(Integer32):
    """Custom type hubExecutingSelfTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSelfTesting", 1),
          ("selfTesting", 2))
    )


_HubExecutingSelfTest_Type.__name__ = "Integer32"
_HubExecutingSelfTest_Object = MibScalar
hubExecutingSelfTest = _HubExecutingSelfTest_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 2, 9),
    _HubExecutingSelfTest_Type()
)
hubExecutingSelfTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubExecutingSelfTest.setStatus("mandatory")


class _HubResetAction_Type(Integer32):
    """Custom type hubResetAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noreset", 1),
          ("reset", 2))
    )


_HubResetAction_Type.__name__ = "Integer32"
_HubResetAction_Object = MibScalar
hubResetAction = _HubResetAction_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 2, 10),
    _HubResetAction_Type()
)
hubResetAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hubResetAction.setStatus("mandatory")
_HmPerfMonCapability_ObjectIdentity = ObjectIdentity
hmPerfMonCapability = _HmPerfMonCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 1, 3)
)
_HmPerfMonRelayTable_Object = MibTable
hmPerfMonRelayTable = _HmPerfMonRelayTable_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hmPerfMonRelayTable.setStatus("mandatory")
_HmPerfMonRelayEntry_Object = MibTableRow
hmPerfMonRelayEntry = _HmPerfMonRelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 3, 1, 1)
)
hmPerfMonRelayEntry.setIndexNames(
    (0, "GANDALF-ENTERPRISE-MIB", "relayPerfID"),
)
if mibBuilder.loadTexts:
    hmPerfMonRelayEntry.setStatus("mandatory")


class _RelayPerfID_Type(Integer32):
    """Custom type relayPerfID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_RelayPerfID_Type.__name__ = "Integer32"
_RelayPerfID_Object = MibTableColumn
relayPerfID = _RelayPerfID_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 3, 1, 1, 1),
    _RelayPerfID_Type()
)
relayPerfID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relayPerfID.setStatus("mandatory")
_RelayTotalCollisions_Type = Counter32
_RelayTotalCollisions_Object = MibTableColumn
relayTotalCollisions = _RelayTotalCollisions_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 3, 1, 1, 2),
    _RelayTotalCollisions_Type()
)
relayTotalCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relayTotalCollisions.setStatus("mandatory")
_HmPerfMonPortTable_Object = MibTable
hmPerfMonPortTable = _HmPerfMonPortTable_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 3, 2)
)
if mibBuilder.loadTexts:
    hmPerfMonPortTable.setStatus("mandatory")
_HmPerfMonPortEntry_Object = MibTableRow
hmPerfMonPortEntry = _HmPerfMonPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 3, 2, 1)
)
hmPerfMonPortEntry.setIndexNames(
    (0, "GANDALF-ENTERPRISE-MIB", "gCardPerfID"),
    (0, "GANDALF-ENTERPRISE-MIB", "gPortPerfID"),
)
if mibBuilder.loadTexts:
    hmPerfMonPortEntry.setStatus("mandatory")


class _GCardPerfID_Type(Integer32):
    """Custom type gCardPerfID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_GCardPerfID_Type.__name__ = "Integer32"
_GCardPerfID_Object = MibTableColumn
gCardPerfID = _GCardPerfID_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 3, 2, 1, 1),
    _GCardPerfID_Type()
)
gCardPerfID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gCardPerfID.setStatus("mandatory")


class _GPortPerfID_Type(Integer32):
    """Custom type gPortPerfID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_GPortPerfID_Type.__name__ = "Integer32"
_GPortPerfID_Object = MibTableColumn
gPortPerfID = _GPortPerfID_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 3, 2, 1, 2),
    _GPortPerfID_Type()
)
gPortPerfID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gPortPerfID.setStatus("mandatory")
_GPortReadableFrames_Type = Counter32
_GPortReadableFrames_Object = MibTableColumn
gPortReadableFrames = _GPortReadableFrames_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 3, 2, 1, 3),
    _GPortReadableFrames_Type()
)
gPortReadableFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gPortReadableFrames.setStatus("mandatory")
_GPortReadableOctets_Type = Counter32
_GPortReadableOctets_Object = MibTableColumn
gPortReadableOctets = _GPortReadableOctets_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 3, 2, 1, 4),
    _GPortReadableOctets_Type()
)
gPortReadableOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gPortReadableOctets.setStatus("mandatory")
_GPortPygmys_Type = Counter32
_GPortPygmys_Object = MibTableColumn
gPortPygmys = _GPortPygmys_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 3, 2, 1, 5),
    _GPortPygmys_Type()
)
gPortPygmys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gPortPygmys.setStatus("mandatory")
_GPortRunts_Type = Counter32
_GPortRunts_Object = MibTableColumn
gPortRunts = _GPortRunts_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 3, 2, 1, 6),
    _GPortRunts_Type()
)
gPortRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gPortRunts.setStatus("mandatory")
_GPortFrameCheckSeqErrs_Type = Counter32
_GPortFrameCheckSeqErrs_Object = MibTableColumn
gPortFrameCheckSeqErrs = _GPortFrameCheckSeqErrs_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 3, 2, 1, 7),
    _GPortFrameCheckSeqErrs_Type()
)
gPortFrameCheckSeqErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gPortFrameCheckSeqErrs.setStatus("mandatory")
_GPortAlignmentErrors_Type = Counter32
_GPortAlignmentErrors_Object = MibTableColumn
gPortAlignmentErrors = _GPortAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 3, 2, 1, 8),
    _GPortAlignmentErrors_Type()
)
gPortAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gPortAlignmentErrors.setStatus("mandatory")
_GPortFramesTooLong_Type = Counter32
_GPortFramesTooLong_Object = MibTableColumn
gPortFramesTooLong = _GPortFramesTooLong_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 3, 2, 1, 9),
    _GPortFramesTooLong_Type()
)
gPortFramesTooLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gPortFramesTooLong.setStatus("mandatory")
_GPortAutoPartitionCount_Type = Counter32
_GPortAutoPartitionCount_Object = MibTableColumn
gPortAutoPartitionCount = _GPortAutoPartitionCount_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 3, 2, 1, 10),
    _GPortAutoPartitionCount_Type()
)
gPortAutoPartitionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gPortAutoPartitionCount.setStatus("mandatory")
_GPortLateCollisions_Type = Counter32
_GPortLateCollisions_Object = MibTableColumn
gPortLateCollisions = _GPortLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 3, 2, 1, 11),
    _GPortLateCollisions_Type()
)
gPortLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gPortLateCollisions.setStatus("mandatory")
_GPortCollisions_Type = Counter32
_GPortCollisions_Object = MibTableColumn
gPortCollisions = _GPortCollisions_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 3, 2, 1, 12),
    _GPortCollisions_Type()
)
gPortCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gPortCollisions.setStatus("mandatory")
_GPortAlarms_Type = Counter32
_GPortAlarms_Object = MibTableColumn
gPortAlarms = _GPortAlarms_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 3, 2, 1, 13),
    _GPortAlarms_Type()
)
gPortAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gPortAlarms.setStatus("mandatory")
_GPortMulticastFrames_Type = Counter32
_GPortMulticastFrames_Object = MibTableColumn
gPortMulticastFrames = _GPortMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 3, 2, 1, 14),
    _GPortMulticastFrames_Type()
)
gPortMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gPortMulticastFrames.setStatus("mandatory")
_GPortBroadcastFrames_Type = Counter32
_GPortBroadcastFrames_Object = MibTableColumn
gPortBroadcastFrames = _GPortBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 3, 2, 1, 15),
    _GPortBroadcastFrames_Type()
)
gPortBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gPortBroadcastFrames.setStatus("mandatory")
_HmAddrTrackCapability_ObjectIdentity = ObjectIdentity
hmAddrTrackCapability = _HmAddrTrackCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 1, 4)
)
_HmAddrTrackPortTable_Object = MibTable
hmAddrTrackPortTable = _HmAddrTrackPortTable_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hmAddrTrackPortTable.setStatus("mandatory")
_HmAddrTrackPortEntry_Object = MibTableRow
hmAddrTrackPortEntry = _HmAddrTrackPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 4, 1, 1)
)
hmAddrTrackPortEntry.setIndexNames(
    (0, "GANDALF-ENTERPRISE-MIB", "gCardAddrID"),
    (0, "GANDALF-ENTERPRISE-MIB", "gPortAddrID"),
)
if mibBuilder.loadTexts:
    hmAddrTrackPortEntry.setStatus("mandatory")


class _GCardAddrID_Type(Integer32):
    """Custom type gCardAddrID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_GCardAddrID_Type.__name__ = "Integer32"
_GCardAddrID_Object = MibTableColumn
gCardAddrID = _GCardAddrID_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 4, 1, 1, 1),
    _GCardAddrID_Type()
)
gCardAddrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gCardAddrID.setStatus("mandatory")


class _GPortAddrID_Type(Integer32):
    """Custom type gPortAddrID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_GPortAddrID_Type.__name__ = "Integer32"
_GPortAddrID_Object = MibTableColumn
gPortAddrID = _GPortAddrID_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 4, 1, 1, 2),
    _GPortAddrID_Type()
)
gPortAddrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gPortAddrID.setStatus("mandatory")


class _GPortLastSourceAddress_Type(OctetString):
    """Custom type gPortLastSourceAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_GPortLastSourceAddress_Type.__name__ = "OctetString"
_GPortLastSourceAddress_Object = MibTableColumn
gPortLastSourceAddress = _GPortLastSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 4, 1, 1, 3),
    _GPortLastSourceAddress_Type()
)
gPortLastSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gPortLastSourceAddress.setStatus("mandatory")
_GPortSourceAddrChanges_Type = Counter32
_GPortSourceAddrChanges_Object = MibTableColumn
gPortSourceAddrChanges = _GPortSourceAddrChanges_Object(
    (1, 3, 6, 1, 4, 1, 64, 1, 4, 1, 1, 4),
    _GPortSourceAddrChanges_Type()
)
gPortSourceAddrChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gPortSourceAddrChanges.setStatus("mandatory")
_Gandalf_bridge_ObjectIdentity = ObjectIdentity
gandalf_bridge = _Gandalf_bridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 2)
)
_BridgeConfigObject_ObjectIdentity = ObjectIdentity
bridgeConfigObject = _BridgeConfigObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 2, 1)
)
_BridgeBaseAddress_Type = OctetString
_BridgeBaseAddress_Object = MibScalar
bridgeBaseAddress = _BridgeBaseAddress_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 1, 1),
    _BridgeBaseAddress_Type()
)
bridgeBaseAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeBaseAddress.setStatus("mandatory")
_BridgeNumPorts_Type = Integer32
_BridgeNumPorts_Object = MibScalar
bridgeNumPorts = _BridgeNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 1, 2),
    _BridgeNumPorts_Type()
)
bridgeNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeNumPorts.setStatus("mandatory")


class _BridgeType_Type(Integer32):
    """Custom type bridgeType based on Integer32"""
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
        *(("sourceroute-only", 3),
          ("srt", 4),
          ("transparent-only", 2),
          ("unknown", 1))
    )


_BridgeType_Type.__name__ = "Integer32"
_BridgeType_Object = MibScalar
bridgeType = _BridgeType_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 1, 3),
    _BridgeType_Type()
)
bridgeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeType.setStatus("mandatory")
_BridgeNumOfInterfaces_Type = Integer32
_BridgeNumOfInterfaces_Object = MibScalar
bridgeNumOfInterfaces = _BridgeNumOfInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 1, 4),
    _BridgeNumOfInterfaces_Type()
)
bridgeNumOfInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeNumOfInterfaces.setStatus("mandatory")


class _BridgePowerUpStatus_Type(Integer32):
    """Custom type bridgePowerUpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 3),
          ("ok", 2),
          ("other", 1))
    )


_BridgePowerUpStatus_Type.__name__ = "Integer32"
_BridgePowerUpStatus_Object = MibScalar
bridgePowerUpStatus = _BridgePowerUpStatus_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 1, 5),
    _BridgePowerUpStatus_Type()
)
bridgePowerUpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgePowerUpStatus.setStatus("mandatory")
_BridgeIpAddr_Type = IpAddress
_BridgeIpAddr_Object = MibScalar
bridgeIpAddr = _BridgeIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 1, 6),
    _BridgeIpAddr_Type()
)
bridgeIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeIpAddr.setStatus("mandatory")
_BridgeManID_Type = OctetString
_BridgeManID_Object = MibScalar
bridgeManID = _BridgeManID_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 1, 7),
    _BridgeManID_Type()
)
bridgeManID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeManID.setStatus("mandatory")
_BridgeManProductVersion_Type = OctetString
_BridgeManProductVersion_Object = MibScalar
bridgeManProductVersion = _BridgeManProductVersion_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 1, 8),
    _BridgeManProductVersion_Type()
)
bridgeManProductVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeManProductVersion.setStatus("mandatory")
_BridgeEEpromRev_Type = OctetString
_BridgeEEpromRev_Object = MibScalar
bridgeEEpromRev = _BridgeEEpromRev_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 1, 9),
    _BridgeEEpromRev_Type()
)
bridgeEEpromRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeEEpromRev.setStatus("mandatory")
_BridgeSerialNum_Type = OctetString
_BridgeSerialNum_Object = MibScalar
bridgeSerialNum = _BridgeSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 1, 10),
    _BridgeSerialNum_Type()
)
bridgeSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeSerialNum.setStatus("mandatory")
_BridgeHubChassis_Type = OctetString
_BridgeHubChassis_Object = MibScalar
bridgeHubChassis = _BridgeHubChassis_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 1, 11),
    _BridgeHubChassis_Type()
)
bridgeHubChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeHubChassis.setStatus("mandatory")
_BridgeTpObject_ObjectIdentity = ObjectIdentity
bridgeTpObject = _BridgeTpObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 2, 2)
)
_FilterDatabaseSize_Type = Integer32
_FilterDatabaseSize_Object = MibScalar
filterDatabaseSize = _FilterDatabaseSize_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 2, 1),
    _FilterDatabaseSize_Type()
)
filterDatabaseSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterDatabaseSize.setStatus("mandatory")
_NumberOfDynamicEntries_Type = Integer32
_NumberOfDynamicEntries_Object = MibScalar
numberOfDynamicEntries = _NumberOfDynamicEntries_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 2, 2),
    _NumberOfDynamicEntries_Type()
)
numberOfDynamicEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfDynamicEntries.setStatus("mandatory")
_NumberOfStaticEntries_Type = Integer32
_NumberOfStaticEntries_Object = MibScalar
numberOfStaticEntries = _NumberOfStaticEntries_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 2, 3),
    _NumberOfStaticEntries_Type()
)
numberOfStaticEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfStaticEntries.setStatus("mandatory")


class _AgingState_Type(Integer32):
    """Custom type agingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_AgingState_Type.__name__ = "Integer32"
_AgingState_Object = MibScalar
agingState = _AgingState_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 2, 4),
    _AgingState_Type()
)
agingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agingState.setStatus("mandatory")
_AgingTime_Type = Integer32
_AgingTime_Object = MibScalar
agingTime = _AgingTime_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 2, 5),
    _AgingTime_Type()
)
agingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agingTime.setStatus("mandatory")


class _LearningState_Type(Integer32):
    """Custom type learningState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_LearningState_Type.__name__ = "Integer32"
_LearningState_Object = MibScalar
learningState = _LearningState_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 2, 6),
    _LearningState_Type()
)
learningState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    learningState.setStatus("mandatory")


class _ProtocolFilterState_Type(Integer32):
    """Custom type protocolFilterState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_ProtocolFilterState_Type.__name__ = "Integer32"
_ProtocolFilterState_Object = MibScalar
protocolFilterState = _ProtocolFilterState_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 2, 7),
    _ProtocolFilterState_Type()
)
protocolFilterState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolFilterState.setStatus("mandatory")


class _BroadcastForwardingState_Type(Integer32):
    """Custom type broadcastForwardingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_BroadcastForwardingState_Type.__name__ = "Integer32"
_BroadcastForwardingState_Object = MibScalar
broadcastForwardingState = _BroadcastForwardingState_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 2, 8),
    _BroadcastForwardingState_Type()
)
broadcastForwardingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    broadcastForwardingState.setStatus("mandatory")


class _MulticastForwardingState_Type(Integer32):
    """Custom type multicastForwardingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_MulticastForwardingState_Type.__name__ = "Integer32"
_MulticastForwardingState_Object = MibScalar
multicastForwardingState = _MulticastForwardingState_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 2, 9),
    _MulticastForwardingState_Type()
)
multicastForwardingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastForwardingState.setStatus("mandatory")
_BridgeTpFdbTable_Object = MibTable
bridgeTpFdbTable = _BridgeTpFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 2, 10)
)
if mibBuilder.loadTexts:
    bridgeTpFdbTable.setStatus("mandatory")
_BridgeTpFdbEntry_Object = MibTableRow
bridgeTpFdbEntry = _BridgeTpFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 2, 10, 1)
)
bridgeTpFdbEntry.setIndexNames(
    (0, "GANDALF-ENTERPRISE-MIB", "bridgeDot1dTpFdbAddress"),
)
if mibBuilder.loadTexts:
    bridgeTpFdbEntry.setStatus("mandatory")
_BridgeDot1dTpFdbAddress_Type = PhysAddress
_BridgeDot1dTpFdbAddress_Object = MibTableColumn
bridgeDot1dTpFdbAddress = _BridgeDot1dTpFdbAddress_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 2, 10, 1, 1),
    _BridgeDot1dTpFdbAddress_Type()
)
bridgeDot1dTpFdbAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeDot1dTpFdbAddress.setStatus("mandatory")
_BridgeDot1dTpFdbPort_Type = Integer32
_BridgeDot1dTpFdbPort_Object = MibTableColumn
bridgeDot1dTpFdbPort = _BridgeDot1dTpFdbPort_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 2, 10, 1, 2),
    _BridgeDot1dTpFdbPort_Type()
)
bridgeDot1dTpFdbPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeDot1dTpFdbPort.setStatus("mandatory")


class _BridgeDot1dTpFdbStatus_Type(Integer32):
    """Custom type bridgeDot1dTpFdbStatus based on Integer32"""
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
        *(("invalid", 2),
          ("learned", 3),
          ("mgmt", 5),
          ("other", 1),
          ("self", 4))
    )


_BridgeDot1dTpFdbStatus_Type.__name__ = "Integer32"
_BridgeDot1dTpFdbStatus_Object = MibTableColumn
bridgeDot1dTpFdbStatus = _BridgeDot1dTpFdbStatus_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 2, 10, 1, 3),
    _BridgeDot1dTpFdbStatus_Type()
)
bridgeDot1dTpFdbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeDot1dTpFdbStatus.setStatus("mandatory")
_BridgeLogicalPortTable_Object = MibTable
bridgeLogicalPortTable = _BridgeLogicalPortTable_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 2, 11)
)
if mibBuilder.loadTexts:
    bridgeLogicalPortTable.setStatus("deprecated")
_BridgeLogicalPortEntry_Object = MibTableRow
bridgeLogicalPortEntry = _BridgeLogicalPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 2, 11, 1)
)
bridgeLogicalPortEntry.setIndexNames(
    (0, "GANDALF-ENTERPRISE-MIB", "bridgeDot1dTpPort"),
)
if mibBuilder.loadTexts:
    bridgeLogicalPortEntry.setStatus("deprecated")
_BridgeDot1dTpPort_Type = Integer32
_BridgeDot1dTpPort_Object = MibTableColumn
bridgeDot1dTpPort = _BridgeDot1dTpPort_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 2, 11, 1, 1),
    _BridgeDot1dTpPort_Type()
)
bridgeDot1dTpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeDot1dTpPort.setStatus("deprecated")
_BridgeDot1dTpPortMaxInfo_Type = Integer32
_BridgeDot1dTpPortMaxInfo_Object = MibTableColumn
bridgeDot1dTpPortMaxInfo = _BridgeDot1dTpPortMaxInfo_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 2, 11, 1, 2),
    _BridgeDot1dTpPortMaxInfo_Type()
)
bridgeDot1dTpPortMaxInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeDot1dTpPortMaxInfo.setStatus("deprecated")
_BridgeDot1dTpPortInFrames_Type = Counter32
_BridgeDot1dTpPortInFrames_Object = MibTableColumn
bridgeDot1dTpPortInFrames = _BridgeDot1dTpPortInFrames_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 2, 11, 1, 3),
    _BridgeDot1dTpPortInFrames_Type()
)
bridgeDot1dTpPortInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeDot1dTpPortInFrames.setStatus("deprecated")
_BridgeDot1dTpPortOutFrames_Type = Counter32
_BridgeDot1dTpPortOutFrames_Object = MibTableColumn
bridgeDot1dTpPortOutFrames = _BridgeDot1dTpPortOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 2, 11, 1, 4),
    _BridgeDot1dTpPortOutFrames_Type()
)
bridgeDot1dTpPortOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeDot1dTpPortOutFrames.setStatus("deprecated")
_BridgeDot1dTpPortInDiscards_Type = Counter32
_BridgeDot1dTpPortInDiscards_Object = MibTableColumn
bridgeDot1dTpPortInDiscards = _BridgeDot1dTpPortInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 2, 11, 1, 5),
    _BridgeDot1dTpPortInDiscards_Type()
)
bridgeDot1dTpPortInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeDot1dTpPortInDiscards.setStatus("deprecated")
_BridgeStpObject_ObjectIdentity = ObjectIdentity
bridgeStpObject = _BridgeStpObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 2, 3)
)


class _BridgeDot1dStpProtocolSpecification_Type(Integer32):
    """Custom type bridgeDot1dStpProtocolSpecification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("decLb100", 2),
          ("ieee8021d", 3),
          ("unknown", 1))
    )


_BridgeDot1dStpProtocolSpecification_Type.__name__ = "Integer32"
_BridgeDot1dStpProtocolSpecification_Object = MibScalar
bridgeDot1dStpProtocolSpecification = _BridgeDot1dStpProtocolSpecification_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 3, 1),
    _BridgeDot1dStpProtocolSpecification_Type()
)
bridgeDot1dStpProtocolSpecification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeDot1dStpProtocolSpecification.setStatus("deprecated")


class _BridgeDot1dStpPriority_Type(Integer32):
    """Custom type bridgeDot1dStpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BridgeDot1dStpPriority_Type.__name__ = "Integer32"
_BridgeDot1dStpPriority_Object = MibScalar
bridgeDot1dStpPriority = _BridgeDot1dStpPriority_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 3, 2),
    _BridgeDot1dStpPriority_Type()
)
bridgeDot1dStpPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeDot1dStpPriority.setStatus("deprecated")
_BridgeDot1dStpTimeSinceTopologyChange_Type = TimeTicks
_BridgeDot1dStpTimeSinceTopologyChange_Object = MibScalar
bridgeDot1dStpTimeSinceTopologyChange = _BridgeDot1dStpTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 3, 3),
    _BridgeDot1dStpTimeSinceTopologyChange_Type()
)
bridgeDot1dStpTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeDot1dStpTimeSinceTopologyChange.setStatus("deprecated")
_BridgeDot1dStpTopChanges_Type = Counter32
_BridgeDot1dStpTopChanges_Object = MibScalar
bridgeDot1dStpTopChanges = _BridgeDot1dStpTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 3, 4),
    _BridgeDot1dStpTopChanges_Type()
)
bridgeDot1dStpTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeDot1dStpTopChanges.setStatus("deprecated")
_BridgeDot1dStpDesignatedRoot_Type = OctetString
_BridgeDot1dStpDesignatedRoot_Object = MibScalar
bridgeDot1dStpDesignatedRoot = _BridgeDot1dStpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 3, 5),
    _BridgeDot1dStpDesignatedRoot_Type()
)
bridgeDot1dStpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeDot1dStpDesignatedRoot.setStatus("deprecated")
_BridgeDot1dStpRootCost_Type = Integer32
_BridgeDot1dStpRootCost_Object = MibScalar
bridgeDot1dStpRootCost = _BridgeDot1dStpRootCost_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 3, 6),
    _BridgeDot1dStpRootCost_Type()
)
bridgeDot1dStpRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeDot1dStpRootCost.setStatus("deprecated")
_BridgeDot1dStpRootPort_Type = Integer32
_BridgeDot1dStpRootPort_Object = MibScalar
bridgeDot1dStpRootPort = _BridgeDot1dStpRootPort_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 3, 7),
    _BridgeDot1dStpRootPort_Type()
)
bridgeDot1dStpRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeDot1dStpRootPort.setStatus("deprecated")
_BridgeDot1dStpMaxAge_Type = Integer32
_BridgeDot1dStpMaxAge_Object = MibScalar
bridgeDot1dStpMaxAge = _BridgeDot1dStpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 3, 8),
    _BridgeDot1dStpMaxAge_Type()
)
bridgeDot1dStpMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeDot1dStpMaxAge.setStatus("deprecated")
_BridgeDot1dStpHelloTime_Type = Integer32
_BridgeDot1dStpHelloTime_Object = MibScalar
bridgeDot1dStpHelloTime = _BridgeDot1dStpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 3, 9),
    _BridgeDot1dStpHelloTime_Type()
)
bridgeDot1dStpHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeDot1dStpHelloTime.setStatus("deprecated")
_BridgeDot1dStpHoldTime_Type = Integer32
_BridgeDot1dStpHoldTime_Object = MibScalar
bridgeDot1dStpHoldTime = _BridgeDot1dStpHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 3, 10),
    _BridgeDot1dStpHoldTime_Type()
)
bridgeDot1dStpHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeDot1dStpHoldTime.setStatus("deprecated")
_BridgeDot1dStpForwardDelay_Type = Integer32
_BridgeDot1dStpForwardDelay_Object = MibScalar
bridgeDot1dStpForwardDelay = _BridgeDot1dStpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 3, 11),
    _BridgeDot1dStpForwardDelay_Type()
)
bridgeDot1dStpForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeDot1dStpForwardDelay.setStatus("deprecated")


class _BridgeDot1dStpBridgeMaxAge_Type(Integer32):
    """Custom type bridgeDot1dStpBridgeMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_BridgeDot1dStpBridgeMaxAge_Type.__name__ = "Integer32"
_BridgeDot1dStpBridgeMaxAge_Object = MibScalar
bridgeDot1dStpBridgeMaxAge = _BridgeDot1dStpBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 3, 12),
    _BridgeDot1dStpBridgeMaxAge_Type()
)
bridgeDot1dStpBridgeMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeDot1dStpBridgeMaxAge.setStatus("deprecated")


class _BridgeDot1dStpBridgeHelloTime_Type(Integer32):
    """Custom type bridgeDot1dStpBridgeHelloTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_BridgeDot1dStpBridgeHelloTime_Type.__name__ = "Integer32"
_BridgeDot1dStpBridgeHelloTime_Object = MibScalar
bridgeDot1dStpBridgeHelloTime = _BridgeDot1dStpBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 3, 13),
    _BridgeDot1dStpBridgeHelloTime_Type()
)
bridgeDot1dStpBridgeHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeDot1dStpBridgeHelloTime.setStatus("deprecated")


class _BridgeDot1dStpBridgeForwardDelay_Type(Integer32):
    """Custom type bridgeDot1dStpBridgeForwardDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_BridgeDot1dStpBridgeForwardDelay_Type.__name__ = "Integer32"
_BridgeDot1dStpBridgeForwardDelay_Object = MibScalar
bridgeDot1dStpBridgeForwardDelay = _BridgeDot1dStpBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 3, 14),
    _BridgeDot1dStpBridgeForwardDelay_Type()
)
bridgeDot1dStpBridgeForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeDot1dStpBridgeForwardDelay.setStatus("deprecated")
_BridgeStpPortTable_Object = MibTable
bridgeStpPortTable = _BridgeStpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 3, 15)
)
if mibBuilder.loadTexts:
    bridgeStpPortTable.setStatus("deprecated")
_BridgeStpPortEntry_Object = MibTableRow
bridgeStpPortEntry = _BridgeStpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 3, 15, 1)
)
bridgeStpPortEntry.setIndexNames(
    (0, "GANDALF-ENTERPRISE-MIB", "bridgeDot1dStpPort"),
)
if mibBuilder.loadTexts:
    bridgeStpPortEntry.setStatus("deprecated")
_BridgeDot1dStpPort_Type = Integer32
_BridgeDot1dStpPort_Object = MibTableColumn
bridgeDot1dStpPort = _BridgeDot1dStpPort_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 3, 15, 1, 1),
    _BridgeDot1dStpPort_Type()
)
bridgeDot1dStpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeDot1dStpPort.setStatus("deprecated")


class _BridgeDot1dStpPortPriority_Type(Integer32):
    """Custom type bridgeDot1dStpPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BridgeDot1dStpPortPriority_Type.__name__ = "Integer32"
_BridgeDot1dStpPortPriority_Object = MibTableColumn
bridgeDot1dStpPortPriority = _BridgeDot1dStpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 3, 15, 1, 2),
    _BridgeDot1dStpPortPriority_Type()
)
bridgeDot1dStpPortPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeDot1dStpPortPriority.setStatus("deprecated")


class _BridgeDot1dStpPortState_Type(Integer32):
    """Custom type bridgeDot1dStpPortState based on Integer32"""
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
        *(("blocking", 2),
          ("broken", 6),
          ("disabled", 1),
          ("forwarding", 5),
          ("learning", 4),
          ("listening", 3))
    )


_BridgeDot1dStpPortState_Type.__name__ = "Integer32"
_BridgeDot1dStpPortState_Object = MibTableColumn
bridgeDot1dStpPortState = _BridgeDot1dStpPortState_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 3, 15, 1, 3),
    _BridgeDot1dStpPortState_Type()
)
bridgeDot1dStpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeDot1dStpPortState.setStatus("deprecated")


class _BridgeDot1dStpPortEnable_Type(Integer32):
    """Custom type bridgeDot1dStpPortEnable based on Integer32"""
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


_BridgeDot1dStpPortEnable_Type.__name__ = "Integer32"
_BridgeDot1dStpPortEnable_Object = MibTableColumn
bridgeDot1dStpPortEnable = _BridgeDot1dStpPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 3, 15, 1, 4),
    _BridgeDot1dStpPortEnable_Type()
)
bridgeDot1dStpPortEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeDot1dStpPortEnable.setStatus("deprecated")


class _BridgeDot1dStpPortPathCost_Type(Integer32):
    """Custom type bridgeDot1dStpPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BridgeDot1dStpPortPathCost_Type.__name__ = "Integer32"
_BridgeDot1dStpPortPathCost_Object = MibTableColumn
bridgeDot1dStpPortPathCost = _BridgeDot1dStpPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 3, 15, 1, 5),
    _BridgeDot1dStpPortPathCost_Type()
)
bridgeDot1dStpPortPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeDot1dStpPortPathCost.setStatus("deprecated")
_BridgeDot1dStpPortDesignatedRoot_Type = OctetString
_BridgeDot1dStpPortDesignatedRoot_Object = MibTableColumn
bridgeDot1dStpPortDesignatedRoot = _BridgeDot1dStpPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 3, 15, 1, 6),
    _BridgeDot1dStpPortDesignatedRoot_Type()
)
bridgeDot1dStpPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeDot1dStpPortDesignatedRoot.setStatus("deprecated")
_BridgeDot1dStpPortDesignatedCost_Type = Integer32
_BridgeDot1dStpPortDesignatedCost_Object = MibTableColumn
bridgeDot1dStpPortDesignatedCost = _BridgeDot1dStpPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 3, 15, 1, 7),
    _BridgeDot1dStpPortDesignatedCost_Type()
)
bridgeDot1dStpPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeDot1dStpPortDesignatedCost.setStatus("deprecated")
_BridgeDot1dStpPortDesignatedBridge_Type = OctetString
_BridgeDot1dStpPortDesignatedBridge_Object = MibTableColumn
bridgeDot1dStpPortDesignatedBridge = _BridgeDot1dStpPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 3, 15, 1, 8),
    _BridgeDot1dStpPortDesignatedBridge_Type()
)
bridgeDot1dStpPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeDot1dStpPortDesignatedBridge.setStatus("deprecated")


class _BridgeDot1dStpPortDesignatedPort_Type(OctetString):
    """Custom type bridgeDot1dStpPortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_BridgeDot1dStpPortDesignatedPort_Type.__name__ = "OctetString"
_BridgeDot1dStpPortDesignatedPort_Object = MibTableColumn
bridgeDot1dStpPortDesignatedPort = _BridgeDot1dStpPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 3, 15, 1, 9),
    _BridgeDot1dStpPortDesignatedPort_Type()
)
bridgeDot1dStpPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeDot1dStpPortDesignatedPort.setStatus("deprecated")
_BridgeDot1dStpPortForwardTransitions_Type = Counter32
_BridgeDot1dStpPortForwardTransitions_Object = MibTableColumn
bridgeDot1dStpPortForwardTransitions = _BridgeDot1dStpPortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 3, 15, 1, 10),
    _BridgeDot1dStpPortForwardTransitions_Type()
)
bridgeDot1dStpPortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeDot1dStpPortForwardTransitions.setStatus("deprecated")
_BridgeStaticObject_ObjectIdentity = ObjectIdentity
bridgeStaticObject = _BridgeStaticObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 2, 4)
)
_BridgeStaticTable_Object = MibTable
bridgeStaticTable = _BridgeStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 4, 1)
)
if mibBuilder.loadTexts:
    bridgeStaticTable.setStatus("deprecated")
_BridgeStaticEntry_Object = MibTableRow
bridgeStaticEntry = _BridgeStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 4, 1, 1)
)
bridgeStaticEntry.setIndexNames(
    (0, "GANDALF-ENTERPRISE-MIB", "bridgeDot1dStaticAddress"),
)
if mibBuilder.loadTexts:
    bridgeStaticEntry.setStatus("deprecated")
_BridgeDot1dStaticAddress_Type = PhysAddress
_BridgeDot1dStaticAddress_Object = MibTableColumn
bridgeDot1dStaticAddress = _BridgeDot1dStaticAddress_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 4, 1, 1, 1),
    _BridgeDot1dStaticAddress_Type()
)
bridgeDot1dStaticAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeDot1dStaticAddress.setStatus("deprecated")
_BridgeDot1dStaticReceivePort_Type = Integer32
_BridgeDot1dStaticReceivePort_Object = MibTableColumn
bridgeDot1dStaticReceivePort = _BridgeDot1dStaticReceivePort_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 4, 1, 1, 2),
    _BridgeDot1dStaticReceivePort_Type()
)
bridgeDot1dStaticReceivePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeDot1dStaticReceivePort.setStatus("deprecated")
_BridgeDot1dStaticAllowedToGoTo_Type = OctetString
_BridgeDot1dStaticAllowedToGoTo_Object = MibTableColumn
bridgeDot1dStaticAllowedToGoTo = _BridgeDot1dStaticAllowedToGoTo_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 4, 1, 1, 3),
    _BridgeDot1dStaticAllowedToGoTo_Type()
)
bridgeDot1dStaticAllowedToGoTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeDot1dStaticAllowedToGoTo.setStatus("deprecated")


class _BridgeDot1dStaticStatus_Type(Integer32):
    """Custom type bridgeDot1dStaticStatus based on Integer32"""
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
        *(("deleteOnReset", 4),
          ("deleteOnTimeout", 5),
          ("invalid", 2),
          ("other", 1),
          ("permanent", 3))
    )


_BridgeDot1dStaticStatus_Type.__name__ = "Integer32"
_BridgeDot1dStaticStatus_Object = MibTableColumn
bridgeDot1dStaticStatus = _BridgeDot1dStaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 4, 1, 1, 4),
    _BridgeDot1dStaticStatus_Type()
)
bridgeDot1dStaticStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeDot1dStaticStatus.setStatus("deprecated")
_BridgeProtFiltTable_Object = MibTable
bridgeProtFiltTable = _BridgeProtFiltTable_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 4, 2)
)
if mibBuilder.loadTexts:
    bridgeProtFiltTable.setStatus("mandatory")
_BridgeProtFiltEntry_Object = MibTableRow
bridgeProtFiltEntry = _BridgeProtFiltEntry_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 4, 2, 1)
)
bridgeProtFiltEntry.setIndexNames(
    (0, "GANDALF-ENTERPRISE-MIB", "brProtFiltIndex"),
)
if mibBuilder.loadTexts:
    bridgeProtFiltEntry.setStatus("mandatory")
_BrProtFiltIndex_Type = Integer32
_BrProtFiltIndex_Object = MibTableColumn
brProtFiltIndex = _BrProtFiltIndex_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 4, 2, 1, 1),
    _BrProtFiltIndex_Type()
)
brProtFiltIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brProtFiltIndex.setStatus("mandatory")


class _BrProtFiltName_Type(OctetString):
    """Custom type brProtFiltName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_BrProtFiltName_Type.__name__ = "OctetString"
_BrProtFiltName_Object = MibTableColumn
brProtFiltName = _BrProtFiltName_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 4, 2, 1, 2),
    _BrProtFiltName_Type()
)
brProtFiltName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brProtFiltName.setStatus("mandatory")


class _BrProtFiltId_Type(OctetString):
    """Custom type brProtFiltId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_BrProtFiltId_Type.__name__ = "OctetString"
_BrProtFiltId_Object = MibTableColumn
brProtFiltId = _BrProtFiltId_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 4, 2, 1, 3),
    _BrProtFiltId_Type()
)
brProtFiltId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brProtFiltId.setStatus("mandatory")
_BrProtFiltPortMap_Type = OctetString
_BrProtFiltPortMap_Object = MibTableColumn
brProtFiltPortMap = _BrProtFiltPortMap_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 4, 2, 1, 4),
    _BrProtFiltPortMap_Type()
)
brProtFiltPortMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brProtFiltPortMap.setStatus("mandatory")
_BridgeProtPriorityTable_Object = MibTable
bridgeProtPriorityTable = _BridgeProtPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 4, 3)
)
if mibBuilder.loadTexts:
    bridgeProtPriorityTable.setStatus("mandatory")
_BridgeProtPriorityEntry_Object = MibTableRow
bridgeProtPriorityEntry = _BridgeProtPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 4, 3, 1)
)
bridgeProtPriorityEntry.setIndexNames(
    (0, "GANDALF-ENTERPRISE-MIB", "brProtPriorityIndex"),
)
if mibBuilder.loadTexts:
    bridgeProtPriorityEntry.setStatus("mandatory")
_BrProtPriorityIndex_Type = Integer32
_BrProtPriorityIndex_Object = MibTableColumn
brProtPriorityIndex = _BrProtPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 4, 3, 1, 1),
    _BrProtPriorityIndex_Type()
)
brProtPriorityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brProtPriorityIndex.setStatus("mandatory")


class _BrProtPriorityName_Type(OctetString):
    """Custom type brProtPriorityName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_BrProtPriorityName_Type.__name__ = "OctetString"
_BrProtPriorityName_Object = MibTableColumn
brProtPriorityName = _BrProtPriorityName_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 4, 3, 1, 2),
    _BrProtPriorityName_Type()
)
brProtPriorityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brProtPriorityName.setStatus("mandatory")


class _BrProtPriorityId_Type(OctetString):
    """Custom type brProtPriorityId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_BrProtPriorityId_Type.__name__ = "OctetString"
_BrProtPriorityId_Object = MibTableColumn
brProtPriorityId = _BrProtPriorityId_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 4, 3, 1, 3),
    _BrProtPriorityId_Type()
)
brProtPriorityId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brProtPriorityId.setStatus("mandatory")


class _BrProtPriorityLevel_Type(Integer32):
    """Custom type brProtPriorityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 3),
          ("low", 1),
          ("medium", 2))
    )


_BrProtPriorityLevel_Type.__name__ = "Integer32"
_BrProtPriorityLevel_Object = MibTableColumn
brProtPriorityLevel = _BrProtPriorityLevel_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 4, 3, 1, 4),
    _BrProtPriorityLevel_Type()
)
brProtPriorityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brProtPriorityLevel.setStatus("mandatory")
_WanPhysicalObject_ObjectIdentity = ObjectIdentity
wanPhysicalObject = _WanPhysicalObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 2, 5)
)
_WanPhysTable_Object = MibTable
wanPhysTable = _WanPhysTable_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 5, 1)
)
if mibBuilder.loadTexts:
    wanPhysTable.setStatus("mandatory")
_WanPhysEntry_Object = MibTableRow
wanPhysEntry = _WanPhysEntry_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 5, 1, 1)
)
wanPhysEntry.setIndexNames(
    (0, "GANDALF-ENTERPRISE-MIB", "wanPhysPortId"),
)
if mibBuilder.loadTexts:
    wanPhysEntry.setStatus("mandatory")
_WanPhysPortId_Type = Integer32
_WanPhysPortId_Object = MibTableColumn
wanPhysPortId = _WanPhysPortId_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 5, 1, 1, 1),
    _WanPhysPortId_Type()
)
wanPhysPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanPhysPortId.setStatus("mandatory")


class _WanPhysPortName_Type(OctetString):
    """Custom type wanPhysPortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_WanPhysPortName_Type.__name__ = "OctetString"
_WanPhysPortName_Object = MibTableColumn
wanPhysPortName = _WanPhysPortName_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 5, 1, 1, 2),
    _WanPhysPortName_Type()
)
wanPhysPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanPhysPortName.setStatus("mandatory")
_WanPhysLogicalPort_Type = Integer32
_WanPhysLogicalPort_Object = MibTableColumn
wanPhysLogicalPort = _WanPhysLogicalPort_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 5, 1, 1, 3),
    _WanPhysLogicalPort_Type()
)
wanPhysLogicalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanPhysLogicalPort.setStatus("mandatory")


class _WanPhysDcdLevel_Type(Integer32):
    """Custom type wanPhysDcdLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_WanPhysDcdLevel_Type.__name__ = "Integer32"
_WanPhysDcdLevel_Object = MibTableColumn
wanPhysDcdLevel = _WanPhysDcdLevel_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 5, 1, 1, 4),
    _WanPhysDcdLevel_Type()
)
wanPhysDcdLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanPhysDcdLevel.setStatus("mandatory")


class _WanPhysLinkLevel_Type(Integer32):
    """Custom type wanPhysLinkLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_WanPhysLinkLevel_Type.__name__ = "Integer32"
_WanPhysLinkLevel_Object = MibTableColumn
wanPhysLinkLevel = _WanPhysLinkLevel_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 5, 1, 1, 5),
    _WanPhysLinkLevel_Type()
)
wanPhysLinkLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanPhysLinkLevel.setStatus("mandatory")
_WanTxLinkUtilization_Type = Gauge32
_WanTxLinkUtilization_Object = MibTableColumn
wanTxLinkUtilization = _WanTxLinkUtilization_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 5, 1, 1, 6),
    _WanTxLinkUtilization_Type()
)
wanTxLinkUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanTxLinkUtilization.setStatus("mandatory")
_WanRxLinkUtilization_Type = Gauge32
_WanRxLinkUtilization_Object = MibTableColumn
wanRxLinkUtilization = _WanRxLinkUtilization_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 5, 1, 1, 7),
    _WanRxLinkUtilization_Type()
)
wanRxLinkUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanRxLinkUtilization.setStatus("mandatory")
_WanPhysFrameErrors_Type = Integer32
_WanPhysFrameErrors_Object = MibTableColumn
wanPhysFrameErrors = _WanPhysFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 5, 1, 1, 8),
    _WanPhysFrameErrors_Type()
)
wanPhysFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanPhysFrameErrors.setStatus("mandatory")


class _WanCompressionState_Type(Integer32):
    """Custom type wanCompressionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_WanCompressionState_Type.__name__ = "Integer32"
_WanCompressionState_Object = MibTableColumn
wanCompressionState = _WanCompressionState_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 5, 1, 1, 9),
    _WanCompressionState_Type()
)
wanCompressionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanCompressionState.setStatus("mandatory")
_WanCompressionRatio_Type = Integer32
_WanCompressionRatio_Object = MibTableColumn
wanCompressionRatio = _WanCompressionRatio_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 5, 1, 1, 10),
    _WanCompressionRatio_Type()
)
wanCompressionRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanCompressionRatio.setStatus("mandatory")
_Ieee8023Object_ObjectIdentity = ObjectIdentity
ieee8023Object = _Ieee8023Object_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 2, 6)
)
_IeeeIfTable_Object = MibTable
ieeeIfTable = _IeeeIfTable_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 6, 1)
)
if mibBuilder.loadTexts:
    ieeeIfTable.setStatus("mandatory")
_IeeeIfEntry_Object = MibTableRow
ieeeIfEntry = _IeeeIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 6, 1, 1)
)
ieeeIfEntry.setIndexNames(
    (0, "GANDALF-ENTERPRISE-MIB", "ieeeIfIndex"),
)
if mibBuilder.loadTexts:
    ieeeIfEntry.setStatus("mandatory")
_IeeeIfIndex_Type = Integer32
_IeeeIfIndex_Object = MibTableColumn
ieeeIfIndex = _IeeeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 6, 1, 1, 1),
    _IeeeIfIndex_Type()
)
ieeeIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieeeIfIndex.setStatus("mandatory")
_IeeeFrmsTxOk_Type = Counter32
_IeeeFrmsTxOk_Object = MibTableColumn
ieeeFrmsTxOk = _IeeeFrmsTxOk_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 6, 1, 1, 2),
    _IeeeFrmsTxOk_Type()
)
ieeeFrmsTxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieeeFrmsTxOk.setStatus("mandatory")
_IeeeSingleCollFrms_Type = Counter32
_IeeeSingleCollFrms_Object = MibTableColumn
ieeeSingleCollFrms = _IeeeSingleCollFrms_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 6, 1, 1, 3),
    _IeeeSingleCollFrms_Type()
)
ieeeSingleCollFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieeeSingleCollFrms.setStatus("mandatory")
_IeeeMultipleCollFrms_Type = Counter32
_IeeeMultipleCollFrms_Object = MibTableColumn
ieeeMultipleCollFrms = _IeeeMultipleCollFrms_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 6, 1, 1, 4),
    _IeeeMultipleCollFrms_Type()
)
ieeeMultipleCollFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieeeMultipleCollFrms.setStatus("mandatory")
_IeeeOctetsTxOk_Type = Counter32
_IeeeOctetsTxOk_Object = MibTableColumn
ieeeOctetsTxOk = _IeeeOctetsTxOk_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 6, 1, 1, 5),
    _IeeeOctetsTxOk_Type()
)
ieeeOctetsTxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieeeOctetsTxOk.setStatus("mandatory")
_IeeeDefTx_Type = Counter32
_IeeeDefTx_Object = MibTableColumn
ieeeDefTx = _IeeeDefTx_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 6, 1, 1, 6),
    _IeeeDefTx_Type()
)
ieeeDefTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieeeDefTx.setStatus("mandatory")
_IeeeMcastFrmsTxOk_Type = Counter32
_IeeeMcastFrmsTxOk_Object = MibTableColumn
ieeeMcastFrmsTxOk = _IeeeMcastFrmsTxOk_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 6, 1, 1, 7),
    _IeeeMcastFrmsTxOk_Type()
)
ieeeMcastFrmsTxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieeeMcastFrmsTxOk.setStatus("mandatory")
_IeeeBcastFrmsTxOk_Type = Counter32
_IeeeBcastFrmsTxOk_Object = MibTableColumn
ieeeBcastFrmsTxOk = _IeeeBcastFrmsTxOk_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 6, 1, 1, 8),
    _IeeeBcastFrmsTxOk_Type()
)
ieeeBcastFrmsTxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieeeBcastFrmsTxOk.setStatus("mandatory")
_IeeeLateColls_Type = Counter32
_IeeeLateColls_Object = MibTableColumn
ieeeLateColls = _IeeeLateColls_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 6, 1, 1, 9),
    _IeeeLateColls_Type()
)
ieeeLateColls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieeeLateColls.setStatus("mandatory")
_IeeeExcessColls_Type = Counter32
_IeeeExcessColls_Object = MibTableColumn
ieeeExcessColls = _IeeeExcessColls_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 6, 1, 1, 10),
    _IeeeExcessColls_Type()
)
ieeeExcessColls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieeeExcessColls.setStatus("mandatory")
_IeeeIntlMacTxError_Type = Counter32
_IeeeIntlMacTxError_Object = MibTableColumn
ieeeIntlMacTxError = _IeeeIntlMacTxError_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 6, 1, 1, 11),
    _IeeeIntlMacTxError_Type()
)
ieeeIntlMacTxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieeeIntlMacTxError.setStatus("mandatory")
_IeeeCsErrors_Type = Counter32
_IeeeCsErrors_Object = MibTableColumn
ieeeCsErrors = _IeeeCsErrors_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 6, 1, 1, 12),
    _IeeeCsErrors_Type()
)
ieeeCsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieeeCsErrors.setStatus("mandatory")
_IeeeExcessDef_Type = Counter32
_IeeeExcessDef_Object = MibTableColumn
ieeeExcessDef = _IeeeExcessDef_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 6, 1, 1, 13),
    _IeeeExcessDef_Type()
)
ieeeExcessDef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieeeExcessDef.setStatus("mandatory")
_IeeeFrmsRxOk_Type = Counter32
_IeeeFrmsRxOk_Object = MibTableColumn
ieeeFrmsRxOk = _IeeeFrmsRxOk_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 6, 1, 1, 14),
    _IeeeFrmsRxOk_Type()
)
ieeeFrmsRxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieeeFrmsRxOk.setStatus("mandatory")
_IeeeOctetsRxOk_Type = Counter32
_IeeeOctetsRxOk_Object = MibTableColumn
ieeeOctetsRxOk = _IeeeOctetsRxOk_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 6, 1, 1, 15),
    _IeeeOctetsRxOk_Type()
)
ieeeOctetsRxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieeeOctetsRxOk.setStatus("mandatory")
_IeeeMcastFrmsRxOk_Type = Counter32
_IeeeMcastFrmsRxOk_Object = MibTableColumn
ieeeMcastFrmsRxOk = _IeeeMcastFrmsRxOk_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 6, 1, 1, 16),
    _IeeeMcastFrmsRxOk_Type()
)
ieeeMcastFrmsRxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieeeMcastFrmsRxOk.setStatus("mandatory")
_IeeeBcastFrmsRxOk_Type = Counter32
_IeeeBcastFrmsRxOk_Object = MibTableColumn
ieeeBcastFrmsRxOk = _IeeeBcastFrmsRxOk_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 6, 1, 1, 17),
    _IeeeBcastFrmsRxOk_Type()
)
ieeeBcastFrmsRxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieeeBcastFrmsRxOk.setStatus("mandatory")
_IeeeTooLongErrors_Type = Counter32
_IeeeTooLongErrors_Object = MibTableColumn
ieeeTooLongErrors = _IeeeTooLongErrors_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 6, 1, 1, 18),
    _IeeeTooLongErrors_Type()
)
ieeeTooLongErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieeeTooLongErrors.setStatus("mandatory")
_IeeeAlignErrors_Type = Counter32
_IeeeAlignErrors_Object = MibTableColumn
ieeeAlignErrors = _IeeeAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 6, 1, 1, 19),
    _IeeeAlignErrors_Type()
)
ieeeAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieeeAlignErrors.setStatus("mandatory")
_IeeeFcsErrors_Type = Counter32
_IeeeFcsErrors_Object = MibTableColumn
ieeeFcsErrors = _IeeeFcsErrors_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 6, 1, 1, 20),
    _IeeeFcsErrors_Type()
)
ieeeFcsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieeeFcsErrors.setStatus("mandatory")
_IeeeIrLengthErrors_Type = Counter32
_IeeeIrLengthErrors_Object = MibTableColumn
ieeeIrLengthErrors = _IeeeIrLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 6, 1, 1, 21),
    _IeeeIrLengthErrors_Type()
)
ieeeIrLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieeeIrLengthErrors.setStatus("mandatory")
_IeeeOorLengthFields_Type = Counter32
_IeeeOorLengthFields_Object = MibTableColumn
ieeeOorLengthFields = _IeeeOorLengthFields_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 6, 1, 1, 22),
    _IeeeOorLengthFields_Type()
)
ieeeOorLengthFields.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieeeOorLengthFields.setStatus("mandatory")
_IeeeIntlMacRcvErrors_Type = Counter32
_IeeeIntlMacRcvErrors_Object = MibTableColumn
ieeeIntlMacRcvErrors = _IeeeIntlMacRcvErrors_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 6, 1, 1, 23),
    _IeeeIntlMacRcvErrors_Type()
)
ieeeIntlMacRcvErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieeeIntlMacRcvErrors.setStatus("mandatory")


class _IeeeInitMac_Type(Integer32):
    """Custom type ieeeInitMac based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("initialize", 1),
          ("uninitialize", 2))
    )


_IeeeInitMac_Type.__name__ = "Integer32"
_IeeeInitMac_Object = MibTableColumn
ieeeInitMac = _IeeeInitMac_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 6, 1, 1, 24),
    _IeeeInitMac_Type()
)
ieeeInitMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieeeInitMac.setStatus("mandatory")


class _IeeePromRxStatus_Type(Integer32):
    """Custom type ieeePromRxStatus based on Integer32"""
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


_IeeePromRxStatus_Type.__name__ = "Integer32"
_IeeePromRxStatus_Object = MibTableColumn
ieeePromRxStatus = _IeeePromRxStatus_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 6, 1, 1, 25),
    _IeeePromRxStatus_Type()
)
ieeePromRxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieeePromRxStatus.setStatus("mandatory")


class _IeeeMacSubLayerStatus_Type(Integer32):
    """Custom type ieeeMacSubLayerStatus based on Integer32"""
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


_IeeeMacSubLayerStatus_Type.__name__ = "Integer32"
_IeeeMacSubLayerStatus_Object = MibTableColumn
ieeeMacSubLayerStatus = _IeeeMacSubLayerStatus_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 6, 1, 1, 26),
    _IeeeMacSubLayerStatus_Type()
)
ieeeMacSubLayerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieeeMacSubLayerStatus.setStatus("mandatory")


class _IeeeTxStatus_Type(Integer32):
    """Custom type ieeeTxStatus based on Integer32"""
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


_IeeeTxStatus_Type.__name__ = "Integer32"
_IeeeTxStatus_Object = MibTableColumn
ieeeTxStatus = _IeeeTxStatus_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 6, 1, 1, 27),
    _IeeeTxStatus_Type()
)
ieeeTxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieeeTxStatus.setStatus("mandatory")


class _IeeeMcastRxStatus_Type(Integer32):
    """Custom type ieeeMcastRxStatus based on Integer32"""
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


_IeeeMcastRxStatus_Type.__name__ = "Integer32"
_IeeeMcastRxStatus_Object = MibTableColumn
ieeeMcastRxStatus = _IeeeMcastRxStatus_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 6, 1, 1, 28),
    _IeeeMcastRxStatus_Type()
)
ieeeMcastRxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieeeMcastRxStatus.setStatus("mandatory")


class _IeeeMacAddress_Type(OctetString):
    """Custom type ieeeMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IeeeMacAddress_Type.__name__ = "OctetString"
_IeeeMacAddress_Object = MibTableColumn
ieeeMacAddress = _IeeeMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 6, 1, 1, 29),
    _IeeeMacAddress_Type()
)
ieeeMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieeeMacAddress.setStatus("mandatory")
_IeeeSqeTestErrors_Type = Counter32
_IeeeSqeTestErrors_Object = MibTableColumn
ieeeSqeTestErrors = _IeeeSqeTestErrors_Object(
    (1, 3, 6, 1, 4, 1, 64, 2, 6, 1, 1, 30),
    _IeeeSqeTestErrors_Type()
)
ieeeSqeTestErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieeeSqeTestErrors.setStatus("mandatory")
_Gandalf_generic_ObjectIdentity = ObjectIdentity
gandalf_generic = _Gandalf_generic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 3)
)
_GandalfLog_ObjectIdentity = ObjectIdentity
gandalfLog = _GandalfLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 3, 1)
)
_GanEventLogTable_Object = MibTable
ganEventLogTable = _GanEventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 64, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ganEventLogTable.setStatus("mandatory")
_GanEventLogEntry_Object = MibTableRow
ganEventLogEntry = _GanEventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 64, 3, 1, 1, 1)
)
ganEventLogEntry.setIndexNames(
    (0, "GANDALF-ENTERPRISE-MIB", "ganEventLogIndex"),
)
if mibBuilder.loadTexts:
    ganEventLogEntry.setStatus("mandatory")
_GanEventLogIndex_Type = Integer32
_GanEventLogIndex_Object = MibTableColumn
ganEventLogIndex = _GanEventLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 64, 3, 1, 1, 1, 1),
    _GanEventLogIndex_Type()
)
ganEventLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ganEventLogIndex.setStatus("mandatory")
_GanEventLogDate_Type = OctetString
_GanEventLogDate_Object = MibTableColumn
ganEventLogDate = _GanEventLogDate_Object(
    (1, 3, 6, 1, 4, 1, 64, 3, 1, 1, 1, 2),
    _GanEventLogDate_Type()
)
ganEventLogDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ganEventLogDate.setStatus("mandatory")
_GanEventLogTime_Type = OctetString
_GanEventLogTime_Object = MibTableColumn
ganEventLogTime = _GanEventLogTime_Object(
    (1, 3, 6, 1, 4, 1, 64, 3, 1, 1, 1, 3),
    _GanEventLogTime_Type()
)
ganEventLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ganEventLogTime.setStatus("mandatory")
_GanEventLogEventNum_Type = Integer32
_GanEventLogEventNum_Object = MibTableColumn
ganEventLogEventNum = _GanEventLogEventNum_Object(
    (1, 3, 6, 1, 4, 1, 64, 3, 1, 1, 1, 4),
    _GanEventLogEventNum_Type()
)
ganEventLogEventNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ganEventLogEventNum.setStatus("deprecated")


class _GanEventLogSeverity_Type(Integer32):
    """Custom type ganEventLogSeverity based on Integer32"""
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
        *(("cleared", 5),
          ("critical", 1),
          ("informational", 6),
          ("major", 2),
          ("minor", 3),
          ("warning", 4))
    )


_GanEventLogSeverity_Type.__name__ = "Integer32"
_GanEventLogSeverity_Object = MibTableColumn
ganEventLogSeverity = _GanEventLogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 64, 3, 1, 1, 1, 5),
    _GanEventLogSeverity_Type()
)
ganEventLogSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ganEventLogSeverity.setStatus("mandatory")
_GanEventLogDescription_Type = OctetString
_GanEventLogDescription_Object = MibTableColumn
ganEventLogDescription = _GanEventLogDescription_Object(
    (1, 3, 6, 1, 4, 1, 64, 3, 1, 1, 1, 6),
    _GanEventLogDescription_Type()
)
ganEventLogDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ganEventLogDescription.setStatus("mandatory")
_SnmpAdminCapability_ObjectIdentity = ObjectIdentity
snmpAdminCapability = _SnmpAdminCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 3, 2)
)
_SnmpCommunityTable_Object = MibTable
snmpCommunityTable = _SnmpCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 64, 3, 2, 1)
)
if mibBuilder.loadTexts:
    snmpCommunityTable.setStatus("mandatory")
_SnmpCommunityEntry_Object = MibTableRow
snmpCommunityEntry = _SnmpCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 64, 3, 2, 1, 1)
)
snmpCommunityEntry.setIndexNames(
    (0, "GANDALF-ENTERPRISE-MIB", "snmpCommunityIndex"),
)
if mibBuilder.loadTexts:
    snmpCommunityEntry.setStatus("mandatory")


class _SnmpCommunityIndex_Type(Integer32):
    """Custom type snmpCommunityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SnmpCommunityIndex_Type.__name__ = "Integer32"
_SnmpCommunityIndex_Object = MibTableColumn
snmpCommunityIndex = _SnmpCommunityIndex_Object(
    (1, 3, 6, 1, 4, 1, 64, 3, 2, 1, 1, 1),
    _SnmpCommunityIndex_Type()
)
snmpCommunityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpCommunityIndex.setStatus("mandatory")
_SnmpCommunityName_Type = OctetString
_SnmpCommunityName_Object = MibTableColumn
snmpCommunityName = _SnmpCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 64, 3, 2, 1, 1, 2),
    _SnmpCommunityName_Type()
)
snmpCommunityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpCommunityName.setStatus("mandatory")
_SnmpCommunityIpAddr_Type = IpAddress
_SnmpCommunityIpAddr_Object = MibTableColumn
snmpCommunityIpAddr = _SnmpCommunityIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 64, 3, 2, 1, 1, 3),
    _SnmpCommunityIpAddr_Type()
)
snmpCommunityIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpCommunityIpAddr.setStatus("mandatory")


class _SnmpCommunityPriv_Type(Integer32):
    """Custom type snmpCommunityPriv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("readOnly", 1),
          ("readWrite", 2))
    )


_SnmpCommunityPriv_Type.__name__ = "Integer32"
_SnmpCommunityPriv_Object = MibTableColumn
snmpCommunityPriv = _SnmpCommunityPriv_Object(
    (1, 3, 6, 1, 4, 1, 64, 3, 2, 1, 1, 4),
    _SnmpCommunityPriv_Type()
)
snmpCommunityPriv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpCommunityPriv.setStatus("mandatory")
_SnmpTrapCommunityTable_Object = MibTable
snmpTrapCommunityTable = _SnmpTrapCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 64, 3, 2, 2)
)
if mibBuilder.loadTexts:
    snmpTrapCommunityTable.setStatus("mandatory")
_SnmpTrapCommunityEntry_Object = MibTableRow
snmpTrapCommunityEntry = _SnmpTrapCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 64, 3, 2, 2, 1)
)
snmpTrapCommunityEntry.setIndexNames(
    (0, "GANDALF-ENTERPRISE-MIB", "snmpTrapCommunityIndex"),
)
if mibBuilder.loadTexts:
    snmpTrapCommunityEntry.setStatus("mandatory")


class _SnmpTrapCommunityIndex_Type(Integer32):
    """Custom type snmpTrapCommunityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SnmpTrapCommunityIndex_Type.__name__ = "Integer32"
_SnmpTrapCommunityIndex_Object = MibTableColumn
snmpTrapCommunityIndex = _SnmpTrapCommunityIndex_Object(
    (1, 3, 6, 1, 4, 1, 64, 3, 2, 2, 1, 1),
    _SnmpTrapCommunityIndex_Type()
)
snmpTrapCommunityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTrapCommunityIndex.setStatus("mandatory")
_SnmpTrapCommunityName_Type = OctetString
_SnmpTrapCommunityName_Object = MibTableColumn
snmpTrapCommunityName = _SnmpTrapCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 64, 3, 2, 2, 1, 2),
    _SnmpTrapCommunityName_Type()
)
snmpTrapCommunityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTrapCommunityName.setStatus("mandatory")
_SnmpTrapIpAddr_Type = IpAddress
_SnmpTrapIpAddr_Object = MibTableColumn
snmpTrapIpAddr = _SnmpTrapIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 64, 3, 2, 2, 1, 3),
    _SnmpTrapIpAddr_Type()
)
snmpTrapIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTrapIpAddr.setStatus("mandatory")
_SnmpTrapRemotePort_Type = Integer32
_SnmpTrapRemotePort_Object = MibTableColumn
snmpTrapRemotePort = _SnmpTrapRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 64, 3, 2, 2, 1, 4),
    _SnmpTrapRemotePort_Type()
)
snmpTrapRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTrapRemotePort.setStatus("mandatory")
_SnmpTrapDescription_Type = OctetString
_SnmpTrapDescription_Object = MibScalar
snmpTrapDescription = _SnmpTrapDescription_Object(
    (1, 3, 6, 1, 4, 1, 64, 3, 2, 3),
    _SnmpTrapDescription_Type()
)
snmpTrapDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTrapDescription.setStatus("mandatory")
_Gandalf_2590_ObjectIdentity = ObjectIdentity
gandalf_2590 = _Gandalf_2590_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 4)
)
_Gandalf_wanNode_ObjectIdentity = ObjectIdentity
gandalf_wanNode = _Gandalf_wanNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 5)
)
_Gandalf_products_ObjectIdentity = ObjectIdentity
gandalf_products = _Gandalf_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 6)
)
_GProd_wan_ObjectIdentity = ObjectIdentity
gProd_wan = _GProd_wan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 6, 1)
)
_GProxy_ObjectIdentity = ObjectIdentity
gProxy = _GProxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 6, 1, 1)
)
_G2300_ObjectIdentity = ObjectIdentity
g2300 = _G2300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 6, 1, 2)
)
_G2050_ObjectIdentity = ObjectIdentity
g2050 = _G2050_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 6, 1, 3)
)
_GProd_hub_ObjectIdentity = ObjectIdentity
gProd_hub = _GProd_hub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 6, 2)
)
_Ecm1000_ObjectIdentity = ObjectIdentity
ecm1000 = _Ecm1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 6, 2, 1)
)
_Rsc9000_ObjectIdentity = ObjectIdentity
rsc9000 = _Rsc9000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 6, 2, 3)
)
_GProd_bridge_ObjectIdentity = ObjectIdentity
gProd_bridge = _GProd_bridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 6, 3)
)
_Lanline5220L_ObjectIdentity = ObjectIdentity
lanline5220L = _Lanline5220L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 6, 3, 2)
)
_Xbr6202_ObjectIdentity = ObjectIdentity
xbr6202 = _Xbr6202_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 6, 3, 3)
)
_Lanline5220e_ObjectIdentity = ObjectIdentity
lanline5220e = _Lanline5220e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 6, 3, 4)
)
_Lanline5225i_ObjectIdentity = ObjectIdentity
lanline5225i = _Lanline5225i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 6, 3, 5)
)
_Lanline5240i_ObjectIdentity = ObjectIdentity
lanline5240i = _Lanline5240i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 6, 3, 6)
)
_Xbr6204_ObjectIdentity = ObjectIdentity
xbr6204 = _Xbr6204_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 6, 3, 7)
)
_Lanline5221_ObjectIdentity = ObjectIdentity
lanline5221 = _Lanline5221_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 6, 3, 8)
)
_Lanline5242_ObjectIdentity = ObjectIdentity
lanline5242 = _Lanline5242_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 6, 3, 9)
)
_GProd_gateway_ObjectIdentity = ObjectIdentity
gProd_gateway = _GProd_gateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 6, 4)
)
_Wgm2590_hub_ObjectIdentity = ObjectIdentity
wgm2590_hub = _Wgm2590_hub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 6, 4, 1)
)
_Wgm2590_standalone_ObjectIdentity = ObjectIdentity
wgm2590_standalone = _Wgm2590_standalone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 6, 4, 2)
)
_GProd_termserver_ObjectIdentity = ObjectIdentity
gProd_termserver = _GProd_termserver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 6, 5)
)
_Gts1000_ObjectIdentity = ObjectIdentity
gts1000 = _Gts1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 6, 5, 1)
)
_Gtsplus_ObjectIdentity = ObjectIdentity
gtsplus = _Gtsplus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 6, 5, 2)
)
_GProd_router_ObjectIdentity = ObjectIdentity
gProd_router = _GProd_router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 6, 6)
)
_Lanline5250i_ObjectIdentity = ObjectIdentity
lanline5250i = _Lanline5250i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 6, 6, 5)
)
_Lanline5250L_ObjectIdentity = ObjectIdentity
lanline5250L = _Lanline5250L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 6, 6, 7)
)
_Lanline5242er_ObjectIdentity = ObjectIdentity
lanline5242er = _Lanline5242er_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 6, 6, 8)
)
_Lanline5250fr_ObjectIdentity = ObjectIdentity
lanline5250fr = _Lanline5250fr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 6, 6, 9)
)
_Xpressway5250isdn_typ1_ObjectIdentity = ObjectIdentity
xpressway5250isdn_typ1 = _Xpressway5250isdn_typ1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 6, 6, 10)
)
_Xpressway5250isdn_typ2_ObjectIdentity = ObjectIdentity
xpressway5250isdn_typ2 = _Xpressway5250isdn_typ2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 6, 6, 11)
)
_Gandalf_nms_ObjectIdentity = ObjectIdentity
gandalf_nms = _Gandalf_nms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 7)
)
_Gandalf_wanProxy_ObjectIdentity = ObjectIdentity
gandalf_wanProxy = _Gandalf_wanProxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 8)
)
_Gandalf_rlanisdn_ObjectIdentity = ObjectIdentity
gandalf_rlanisdn = _Gandalf_rlanisdn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 9)
)
_Gandalf_termserver_ObjectIdentity = ObjectIdentity
gandalf_termserver = _Gandalf_termserver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 10)
)
_Gandalf_router_ObjectIdentity = ObjectIdentity
gandalf_router = _Gandalf_router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 11)
)
_Gandalf_experimental_ObjectIdentity = ObjectIdentity
gandalf_experimental = _Gandalf_experimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 64, 12)
)

# Managed Objects groups


# Notification objects

gCardInstalled = NotificationType(
    (1, 3, 6, 1, 4, 1, 64, 0, 100)
)
if mibBuilder.loadTexts:
    gCardInstalled.setStatus(
        ""
    )

gCardRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 64, 0, 101)
)
if mibBuilder.loadTexts:
    gCardRemoved.setStatus(
        ""
    )

gCardMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 64, 0, 102)
)
if mibBuilder.loadTexts:
    gCardMismatch.setStatus(
        ""
    )

gCardMismatchCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 64, 0, 103)
)
if mibBuilder.loadTexts:
    gCardMismatchCleared.setStatus(
        ""
    )

gPortThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 64, 0, 104)
)
if mibBuilder.loadTexts:
    gPortThresholdExceeded.setStatus(
        ""
    )

gNvramFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 64, 0, 105)
)
if mibBuilder.loadTexts:
    gNvramFault.setStatus(
        ""
    )

gFiltDatabaseFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 64, 0, 106)
)
if mibBuilder.loadTexts:
    gFiltDatabaseFull.setStatus(
        ""
    )

gPowerSupplyFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 64, 0, 107)
)
if mibBuilder.loadTexts:
    gPowerSupplyFailed.setStatus(
        ""
    )

gLogThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 64, 0, 108)
)
if mibBuilder.loadTexts:
    gLogThresholdExceeded.setStatus(
        ""
    )

gLinkMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 64, 0, 109)
)
if mibBuilder.loadTexts:
    gLinkMismatch.setStatus(
        ""
    )

gLinkMismatchCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 64, 0, 110)
)
if mibBuilder.loadTexts:
    gLinkMismatchCleared.setStatus(
        ""
    )

gNewRoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 64, 0, 111)
)
if mibBuilder.loadTexts:
    gNewRoot.setStatus(
        ""
    )

gTopologyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 64, 0, 112)
)
if mibBuilder.loadTexts:
    gTopologyChange.setStatus(
        ""
    )

gPortFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 64, 0, 113)
)
if mibBuilder.loadTexts:
    gPortFailure.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GANDALF-ENTERPRISE-MIB",
    **{"gandalf": gandalf,
       "gCardInstalled": gCardInstalled,
       "gCardRemoved": gCardRemoved,
       "gCardMismatch": gCardMismatch,
       "gCardMismatchCleared": gCardMismatchCleared,
       "gPortThresholdExceeded": gPortThresholdExceeded,
       "gNvramFault": gNvramFault,
       "gFiltDatabaseFull": gFiltDatabaseFull,
       "gPowerSupplyFailed": gPowerSupplyFailed,
       "gLogThresholdExceeded": gLogThresholdExceeded,
       "gLinkMismatch": gLinkMismatch,
       "gLinkMismatchCleared": gLinkMismatchCleared,
       "gNewRoot": gNewRoot,
       "gTopologyChange": gTopologyChange,
       "gPortFailure": gPortFailure,
       "gandalf-hub": gandalf_hub,
       "hmBasicCapability": hmBasicCapability,
       "hubBasicID": hubBasicID,
       "hubCardCapacity": hubCardCapacity,
       "hubCardMap": hubCardMap,
       "hubNumOfRelays": hubNumOfRelays,
       "hubRelayActive": hubRelayActive,
       "hubResourceType": hubResourceType,
       "hubStandardRevision": hubStandardRevision,
       "hubIEEE8023LmeOptions": hubIEEE8023LmeOptions,
       "hubManID": hubManID,
       "hubManProductID": hubManProductID,
       "hubManProductVersion": hubManProductVersion,
       "hubManTelephoneNum": hubManTelephoneNum,
       "hubName": hubName,
       "hubIPaddress": hubIPaddress,
       "hubEEpromRev": hubEEpromRev,
       "hubSecureMode": hubSecureMode,
       "hmBasicCardTable": hmBasicCardTable,
       "hmBasicCardEntry": hmBasicCardEntry,
       "gCardID": gCardID,
       "gCardNumberOfPorts": gCardNumberOfPorts,
       "gCardName": gCardName,
       "gCardType": gCardType,
       "gCardRingNumberA": gCardRingNumberA,
       "gCardRingNumberB": gCardRingNumberB,
       "gCardIbmModeA": gCardIbmModeA,
       "gCardIbmModeB": gCardIbmModeB,
       "gCardRingSpeedA": gCardRingSpeedA,
       "gCardRingSpeedB": gCardRingSpeedB,
       "hmBasicPortTable": hmBasicPortTable,
       "hmBasicPortEntry": hmBasicPortEntry,
       "gCardBasicID": gCardBasicID,
       "gPortID": gPortID,
       "gPortType": gPortType,
       "gPortAdminState": gPortAdminState,
       "gPortAutoPartitionState": gPortAutoPartitionState,
       "gPortName": gPortName,
       "gPortEffectiveState": gPortEffectiveState,
       "gPortConfiguration": gPortConfiguration,
       "gPortRedundantPort": gPortRedundantPort,
       "gPortRedundantCard": gPortRedundantCard,
       "gPortLinkStatus": gPortLinkStatus,
       "hmSelfTestCapability": hmSelfTestCapability,
       "hubSelfTestID": hubSelfTestID,
       "hubTimeSinceReset": hubTimeSinceReset,
       "hubResetTimeStamp": hubResetTimeStamp,
       "hubHealthState": hubHealthState,
       "hubHealthText": hubHealthText,
       "hubHealthData": hubHealthData,
       "hubSystemResetting": hubSystemResetting,
       "hubResetting": hubResetting,
       "hubExecutingSelfTest": hubExecutingSelfTest,
       "hubResetAction": hubResetAction,
       "hmPerfMonCapability": hmPerfMonCapability,
       "hmPerfMonRelayTable": hmPerfMonRelayTable,
       "hmPerfMonRelayEntry": hmPerfMonRelayEntry,
       "relayPerfID": relayPerfID,
       "relayTotalCollisions": relayTotalCollisions,
       "hmPerfMonPortTable": hmPerfMonPortTable,
       "hmPerfMonPortEntry": hmPerfMonPortEntry,
       "gCardPerfID": gCardPerfID,
       "gPortPerfID": gPortPerfID,
       "gPortReadableFrames": gPortReadableFrames,
       "gPortReadableOctets": gPortReadableOctets,
       "gPortPygmys": gPortPygmys,
       "gPortRunts": gPortRunts,
       "gPortFrameCheckSeqErrs": gPortFrameCheckSeqErrs,
       "gPortAlignmentErrors": gPortAlignmentErrors,
       "gPortFramesTooLong": gPortFramesTooLong,
       "gPortAutoPartitionCount": gPortAutoPartitionCount,
       "gPortLateCollisions": gPortLateCollisions,
       "gPortCollisions": gPortCollisions,
       "gPortAlarms": gPortAlarms,
       "gPortMulticastFrames": gPortMulticastFrames,
       "gPortBroadcastFrames": gPortBroadcastFrames,
       "hmAddrTrackCapability": hmAddrTrackCapability,
       "hmAddrTrackPortTable": hmAddrTrackPortTable,
       "hmAddrTrackPortEntry": hmAddrTrackPortEntry,
       "gCardAddrID": gCardAddrID,
       "gPortAddrID": gPortAddrID,
       "gPortLastSourceAddress": gPortLastSourceAddress,
       "gPortSourceAddrChanges": gPortSourceAddrChanges,
       "gandalf-bridge": gandalf_bridge,
       "bridgeConfigObject": bridgeConfigObject,
       "bridgeBaseAddress": bridgeBaseAddress,
       "bridgeNumPorts": bridgeNumPorts,
       "bridgeType": bridgeType,
       "bridgeNumOfInterfaces": bridgeNumOfInterfaces,
       "bridgePowerUpStatus": bridgePowerUpStatus,
       "bridgeIpAddr": bridgeIpAddr,
       "bridgeManID": bridgeManID,
       "bridgeManProductVersion": bridgeManProductVersion,
       "bridgeEEpromRev": bridgeEEpromRev,
       "bridgeSerialNum": bridgeSerialNum,
       "bridgeHubChassis": bridgeHubChassis,
       "bridgeTpObject": bridgeTpObject,
       "filterDatabaseSize": filterDatabaseSize,
       "numberOfDynamicEntries": numberOfDynamicEntries,
       "numberOfStaticEntries": numberOfStaticEntries,
       "agingState": agingState,
       "agingTime": agingTime,
       "learningState": learningState,
       "protocolFilterState": protocolFilterState,
       "broadcastForwardingState": broadcastForwardingState,
       "multicastForwardingState": multicastForwardingState,
       "bridgeTpFdbTable": bridgeTpFdbTable,
       "bridgeTpFdbEntry": bridgeTpFdbEntry,
       "bridgeDot1dTpFdbAddress": bridgeDot1dTpFdbAddress,
       "bridgeDot1dTpFdbPort": bridgeDot1dTpFdbPort,
       "bridgeDot1dTpFdbStatus": bridgeDot1dTpFdbStatus,
       "bridgeLogicalPortTable": bridgeLogicalPortTable,
       "bridgeLogicalPortEntry": bridgeLogicalPortEntry,
       "bridgeDot1dTpPort": bridgeDot1dTpPort,
       "bridgeDot1dTpPortMaxInfo": bridgeDot1dTpPortMaxInfo,
       "bridgeDot1dTpPortInFrames": bridgeDot1dTpPortInFrames,
       "bridgeDot1dTpPortOutFrames": bridgeDot1dTpPortOutFrames,
       "bridgeDot1dTpPortInDiscards": bridgeDot1dTpPortInDiscards,
       "bridgeStpObject": bridgeStpObject,
       "bridgeDot1dStpProtocolSpecification": bridgeDot1dStpProtocolSpecification,
       "bridgeDot1dStpPriority": bridgeDot1dStpPriority,
       "bridgeDot1dStpTimeSinceTopologyChange": bridgeDot1dStpTimeSinceTopologyChange,
       "bridgeDot1dStpTopChanges": bridgeDot1dStpTopChanges,
       "bridgeDot1dStpDesignatedRoot": bridgeDot1dStpDesignatedRoot,
       "bridgeDot1dStpRootCost": bridgeDot1dStpRootCost,
       "bridgeDot1dStpRootPort": bridgeDot1dStpRootPort,
       "bridgeDot1dStpMaxAge": bridgeDot1dStpMaxAge,
       "bridgeDot1dStpHelloTime": bridgeDot1dStpHelloTime,
       "bridgeDot1dStpHoldTime": bridgeDot1dStpHoldTime,
       "bridgeDot1dStpForwardDelay": bridgeDot1dStpForwardDelay,
       "bridgeDot1dStpBridgeMaxAge": bridgeDot1dStpBridgeMaxAge,
       "bridgeDot1dStpBridgeHelloTime": bridgeDot1dStpBridgeHelloTime,
       "bridgeDot1dStpBridgeForwardDelay": bridgeDot1dStpBridgeForwardDelay,
       "bridgeStpPortTable": bridgeStpPortTable,
       "bridgeStpPortEntry": bridgeStpPortEntry,
       "bridgeDot1dStpPort": bridgeDot1dStpPort,
       "bridgeDot1dStpPortPriority": bridgeDot1dStpPortPriority,
       "bridgeDot1dStpPortState": bridgeDot1dStpPortState,
       "bridgeDot1dStpPortEnable": bridgeDot1dStpPortEnable,
       "bridgeDot1dStpPortPathCost": bridgeDot1dStpPortPathCost,
       "bridgeDot1dStpPortDesignatedRoot": bridgeDot1dStpPortDesignatedRoot,
       "bridgeDot1dStpPortDesignatedCost": bridgeDot1dStpPortDesignatedCost,
       "bridgeDot1dStpPortDesignatedBridge": bridgeDot1dStpPortDesignatedBridge,
       "bridgeDot1dStpPortDesignatedPort": bridgeDot1dStpPortDesignatedPort,
       "bridgeDot1dStpPortForwardTransitions": bridgeDot1dStpPortForwardTransitions,
       "bridgeStaticObject": bridgeStaticObject,
       "bridgeStaticTable": bridgeStaticTable,
       "bridgeStaticEntry": bridgeStaticEntry,
       "bridgeDot1dStaticAddress": bridgeDot1dStaticAddress,
       "bridgeDot1dStaticReceivePort": bridgeDot1dStaticReceivePort,
       "bridgeDot1dStaticAllowedToGoTo": bridgeDot1dStaticAllowedToGoTo,
       "bridgeDot1dStaticStatus": bridgeDot1dStaticStatus,
       "bridgeProtFiltTable": bridgeProtFiltTable,
       "bridgeProtFiltEntry": bridgeProtFiltEntry,
       "brProtFiltIndex": brProtFiltIndex,
       "brProtFiltName": brProtFiltName,
       "brProtFiltId": brProtFiltId,
       "brProtFiltPortMap": brProtFiltPortMap,
       "bridgeProtPriorityTable": bridgeProtPriorityTable,
       "bridgeProtPriorityEntry": bridgeProtPriorityEntry,
       "brProtPriorityIndex": brProtPriorityIndex,
       "brProtPriorityName": brProtPriorityName,
       "brProtPriorityId": brProtPriorityId,
       "brProtPriorityLevel": brProtPriorityLevel,
       "wanPhysicalObject": wanPhysicalObject,
       "wanPhysTable": wanPhysTable,
       "wanPhysEntry": wanPhysEntry,
       "wanPhysPortId": wanPhysPortId,
       "wanPhysPortName": wanPhysPortName,
       "wanPhysLogicalPort": wanPhysLogicalPort,
       "wanPhysDcdLevel": wanPhysDcdLevel,
       "wanPhysLinkLevel": wanPhysLinkLevel,
       "wanTxLinkUtilization": wanTxLinkUtilization,
       "wanRxLinkUtilization": wanRxLinkUtilization,
       "wanPhysFrameErrors": wanPhysFrameErrors,
       "wanCompressionState": wanCompressionState,
       "wanCompressionRatio": wanCompressionRatio,
       "ieee8023Object": ieee8023Object,
       "ieeeIfTable": ieeeIfTable,
       "ieeeIfEntry": ieeeIfEntry,
       "ieeeIfIndex": ieeeIfIndex,
       "ieeeFrmsTxOk": ieeeFrmsTxOk,
       "ieeeSingleCollFrms": ieeeSingleCollFrms,
       "ieeeMultipleCollFrms": ieeeMultipleCollFrms,
       "ieeeOctetsTxOk": ieeeOctetsTxOk,
       "ieeeDefTx": ieeeDefTx,
       "ieeeMcastFrmsTxOk": ieeeMcastFrmsTxOk,
       "ieeeBcastFrmsTxOk": ieeeBcastFrmsTxOk,
       "ieeeLateColls": ieeeLateColls,
       "ieeeExcessColls": ieeeExcessColls,
       "ieeeIntlMacTxError": ieeeIntlMacTxError,
       "ieeeCsErrors": ieeeCsErrors,
       "ieeeExcessDef": ieeeExcessDef,
       "ieeeFrmsRxOk": ieeeFrmsRxOk,
       "ieeeOctetsRxOk": ieeeOctetsRxOk,
       "ieeeMcastFrmsRxOk": ieeeMcastFrmsRxOk,
       "ieeeBcastFrmsRxOk": ieeeBcastFrmsRxOk,
       "ieeeTooLongErrors": ieeeTooLongErrors,
       "ieeeAlignErrors": ieeeAlignErrors,
       "ieeeFcsErrors": ieeeFcsErrors,
       "ieeeIrLengthErrors": ieeeIrLengthErrors,
       "ieeeOorLengthFields": ieeeOorLengthFields,
       "ieeeIntlMacRcvErrors": ieeeIntlMacRcvErrors,
       "ieeeInitMac": ieeeInitMac,
       "ieeePromRxStatus": ieeePromRxStatus,
       "ieeeMacSubLayerStatus": ieeeMacSubLayerStatus,
       "ieeeTxStatus": ieeeTxStatus,
       "ieeeMcastRxStatus": ieeeMcastRxStatus,
       "ieeeMacAddress": ieeeMacAddress,
       "ieeeSqeTestErrors": ieeeSqeTestErrors,
       "gandalf-generic": gandalf_generic,
       "gandalfLog": gandalfLog,
       "ganEventLogTable": ganEventLogTable,
       "ganEventLogEntry": ganEventLogEntry,
       "ganEventLogIndex": ganEventLogIndex,
       "ganEventLogDate": ganEventLogDate,
       "ganEventLogTime": ganEventLogTime,
       "ganEventLogEventNum": ganEventLogEventNum,
       "ganEventLogSeverity": ganEventLogSeverity,
       "ganEventLogDescription": ganEventLogDescription,
       "snmpAdminCapability": snmpAdminCapability,
       "snmpCommunityTable": snmpCommunityTable,
       "snmpCommunityEntry": snmpCommunityEntry,
       "snmpCommunityIndex": snmpCommunityIndex,
       "snmpCommunityName": snmpCommunityName,
       "snmpCommunityIpAddr": snmpCommunityIpAddr,
       "snmpCommunityPriv": snmpCommunityPriv,
       "snmpTrapCommunityTable": snmpTrapCommunityTable,
       "snmpTrapCommunityEntry": snmpTrapCommunityEntry,
       "snmpTrapCommunityIndex": snmpTrapCommunityIndex,
       "snmpTrapCommunityName": snmpTrapCommunityName,
       "snmpTrapIpAddr": snmpTrapIpAddr,
       "snmpTrapRemotePort": snmpTrapRemotePort,
       "snmpTrapDescription": snmpTrapDescription,
       "gandalf-2590": gandalf_2590,
       "gandalf-wanNode": gandalf_wanNode,
       "gandalf-products": gandalf_products,
       "gProd-wan": gProd_wan,
       "gProxy": gProxy,
       "g2300": g2300,
       "g2050": g2050,
       "gProd-hub": gProd_hub,
       "ecm1000": ecm1000,
       "rsc9000": rsc9000,
       "gProd-bridge": gProd_bridge,
       "lanline5220L": lanline5220L,
       "xbr6202": xbr6202,
       "lanline5220e": lanline5220e,
       "lanline5225i": lanline5225i,
       "lanline5240i": lanline5240i,
       "xbr6204": xbr6204,
       "lanline5221": lanline5221,
       "lanline5242": lanline5242,
       "gProd-gateway": gProd_gateway,
       "wgm2590-hub": wgm2590_hub,
       "wgm2590-standalone": wgm2590_standalone,
       "gProd-termserver": gProd_termserver,
       "gts1000": gts1000,
       "gtsplus": gtsplus,
       "gProd-router": gProd_router,
       "lanline5250i": lanline5250i,
       "lanline5250L": lanline5250L,
       "lanline5242er": lanline5242er,
       "lanline5250fr": lanline5250fr,
       "xpressway5250isdn-typ1": xpressway5250isdn_typ1,
       "xpressway5250isdn-typ2": xpressway5250isdn_typ2,
       "gandalf-nms": gandalf_nms,
       "gandalf-wanProxy": gandalf_wanProxy,
       "gandalf-rlanisdn": gandalf_rlanisdn,
       "gandalf-termserver": gandalf_termserver,
       "gandalf-router": gandalf_router,
       "gandalf-experimental": gandalf_experimental}
)
