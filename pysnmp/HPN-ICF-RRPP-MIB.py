# SNMP MIB module (HPN-ICF-RRPP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-RRPP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:44 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hpnicfRrpp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EnabledStatus(Integer32, TextualConvention):
    status = "current"
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



# MIB Managed Objects in the order of their OIDs

_HpnicfRrppScalarGroup_ObjectIdentity = ObjectIdentity
hpnicfRrppScalarGroup = _HpnicfRrppScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 1)
)
_HpnicfRrppEnableStatus_Type = EnabledStatus
_HpnicfRrppEnableStatus_Object = MibScalar
hpnicfRrppEnableStatus = _HpnicfRrppEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 1, 1),
    _HpnicfRrppEnableStatus_Type()
)
hpnicfRrppEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfRrppEnableStatus.setStatus("current")


class _HpnicfRrppPassword_Type(OctetString):
    """Custom type hpnicfRrppPassword based on OctetString"""
    defaultHexValue = "303030464532303346443735"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_HpnicfRrppPassword_Type.__name__ = "OctetString"
_HpnicfRrppPassword_Object = MibScalar
hpnicfRrppPassword = _HpnicfRrppPassword_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 1, 2),
    _HpnicfRrppPassword_Type()
)
hpnicfRrppPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfRrppPassword.setStatus("current")


class _HpnicfRrppPasswordType_Type(Integer32):
    """Custom type hpnicfRrppPasswordType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cipher", 2),
          ("simple", 1))
    )


_HpnicfRrppPasswordType_Type.__name__ = "Integer32"
_HpnicfRrppPasswordType_Object = MibScalar
hpnicfRrppPasswordType = _HpnicfRrppPasswordType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 1, 3),
    _HpnicfRrppPasswordType_Type()
)
hpnicfRrppPasswordType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfRrppPasswordType.setStatus("current")


class _HpnicfRrppProtectVlanConfigMode_Type(Integer32):
    """Custom type hpnicfRrppProtectVlanConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("instance", 2),
          ("vlan", 1))
    )


_HpnicfRrppProtectVlanConfigMode_Type.__name__ = "Integer32"
_HpnicfRrppProtectVlanConfigMode_Object = MibScalar
hpnicfRrppProtectVlanConfigMode = _HpnicfRrppProtectVlanConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 1, 4),
    _HpnicfRrppProtectVlanConfigMode_Type()
)
hpnicfRrppProtectVlanConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRrppProtectVlanConfigMode.setStatus("current")
_HpnicfRrppTable_ObjectIdentity = ObjectIdentity
hpnicfRrppTable = _HpnicfRrppTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2)
)
_HpnicfRrppDomainTable_Object = MibTable
hpnicfRrppDomainTable = _HpnicfRrppDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfRrppDomainTable.setStatus("current")
_HpnicfRrppDomainEntry_Object = MibTableRow
hpnicfRrppDomainEntry = _HpnicfRrppDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 1, 1)
)
hpnicfRrppDomainEntry.setIndexNames(
    (0, "HPN-ICF-RRPP-MIB", "hpnicfRrppDomainID"),
)
if mibBuilder.loadTexts:
    hpnicfRrppDomainEntry.setStatus("current")


class _HpnicfRrppDomainID_Type(Integer32):
    """Custom type hpnicfRrppDomainID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HpnicfRrppDomainID_Type.__name__ = "Integer32"
_HpnicfRrppDomainID_Object = MibTableColumn
hpnicfRrppDomainID = _HpnicfRrppDomainID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 1, 1, 1),
    _HpnicfRrppDomainID_Type()
)
hpnicfRrppDomainID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfRrppDomainID.setStatus("current")


class _HpnicfRrppDomainControlVlanID_Type(Integer32):
    """Custom type hpnicfRrppDomainControlVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4094),
        ValueRangeConstraint(65535, 65535),
    )


_HpnicfRrppDomainControlVlanID_Type.__name__ = "Integer32"
_HpnicfRrppDomainControlVlanID_Object = MibTableColumn
hpnicfRrppDomainControlVlanID = _HpnicfRrppDomainControlVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 1, 1, 2),
    _HpnicfRrppDomainControlVlanID_Type()
)
hpnicfRrppDomainControlVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRrppDomainControlVlanID.setStatus("current")


class _HpnicfRrppDomainHelloTime_Type(Integer32):
    """Custom type hpnicfRrppDomainHelloTime based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HpnicfRrppDomainHelloTime_Type.__name__ = "Integer32"
_HpnicfRrppDomainHelloTime_Object = MibTableColumn
hpnicfRrppDomainHelloTime = _HpnicfRrppDomainHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 1, 1, 3),
    _HpnicfRrppDomainHelloTime_Type()
)
hpnicfRrppDomainHelloTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRrppDomainHelloTime.setStatus("current")


class _HpnicfRrppDomainFailTime_Type(Integer32):
    """Custom type hpnicfRrppDomainFailTime based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 30),
    )


_HpnicfRrppDomainFailTime_Type.__name__ = "Integer32"
_HpnicfRrppDomainFailTime_Object = MibTableColumn
hpnicfRrppDomainFailTime = _HpnicfRrppDomainFailTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 1, 1, 4),
    _HpnicfRrppDomainFailTime_Type()
)
hpnicfRrppDomainFailTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRrppDomainFailTime.setStatus("current")
_HpnicfRrppDomainRowStatus_Type = RowStatus
_HpnicfRrppDomainRowStatus_Object = MibTableColumn
hpnicfRrppDomainRowStatus = _HpnicfRrppDomainRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 1, 1, 5),
    _HpnicfRrppDomainRowStatus_Type()
)
hpnicfRrppDomainRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRrppDomainRowStatus.setStatus("current")


class _HpnicfRrppDomainInstanceListLow_Type(OctetString):
    """Custom type hpnicfRrppDomainInstanceListLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HpnicfRrppDomainInstanceListLow_Type.__name__ = "OctetString"
_HpnicfRrppDomainInstanceListLow_Object = MibTableColumn
hpnicfRrppDomainInstanceListLow = _HpnicfRrppDomainInstanceListLow_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 1, 1, 6),
    _HpnicfRrppDomainInstanceListLow_Type()
)
hpnicfRrppDomainInstanceListLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRrppDomainInstanceListLow.setStatus("current")


class _HpnicfRrppDomainInstanceListHigh_Type(OctetString):
    """Custom type hpnicfRrppDomainInstanceListHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HpnicfRrppDomainInstanceListHigh_Type.__name__ = "OctetString"
_HpnicfRrppDomainInstanceListHigh_Object = MibTableColumn
hpnicfRrppDomainInstanceListHigh = _HpnicfRrppDomainInstanceListHigh_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 1, 1, 7),
    _HpnicfRrppDomainInstanceListHigh_Type()
)
hpnicfRrppDomainInstanceListHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRrppDomainInstanceListHigh.setStatus("current")


class _HpnicfRrppDomainProtectVlanListLow_Type(OctetString):
    """Custom type hpnicfRrppDomainProtectVlanListLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HpnicfRrppDomainProtectVlanListLow_Type.__name__ = "OctetString"
_HpnicfRrppDomainProtectVlanListLow_Object = MibTableColumn
hpnicfRrppDomainProtectVlanListLow = _HpnicfRrppDomainProtectVlanListLow_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 1, 1, 8),
    _HpnicfRrppDomainProtectVlanListLow_Type()
)
hpnicfRrppDomainProtectVlanListLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRrppDomainProtectVlanListLow.setStatus("current")


class _HpnicfRrppDomainProtectVlanListHigh_Type(OctetString):
    """Custom type hpnicfRrppDomainProtectVlanListHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HpnicfRrppDomainProtectVlanListHigh_Type.__name__ = "OctetString"
_HpnicfRrppDomainProtectVlanListHigh_Object = MibTableColumn
hpnicfRrppDomainProtectVlanListHigh = _HpnicfRrppDomainProtectVlanListHigh_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 1, 1, 9),
    _HpnicfRrppDomainProtectVlanListHigh_Type()
)
hpnicfRrppDomainProtectVlanListHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRrppDomainProtectVlanListHigh.setStatus("current")
_HpnicfRrppRingTable_Object = MibTable
hpnicfRrppRingTable = _HpnicfRrppRingTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfRrppRingTable.setStatus("current")
_HpnicfRrppRingEntry_Object = MibTableRow
hpnicfRrppRingEntry = _HpnicfRrppRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 2, 1)
)
hpnicfRrppRingEntry.setIndexNames(
    (0, "HPN-ICF-RRPP-MIB", "hpnicfRrppDomainID"),
    (0, "HPN-ICF-RRPP-MIB", "hpnicfRrppRingID"),
)
if mibBuilder.loadTexts:
    hpnicfRrppRingEntry.setStatus("current")


class _HpnicfRrppRingID_Type(Integer32):
    """Custom type hpnicfRrppRingID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HpnicfRrppRingID_Type.__name__ = "Integer32"
_HpnicfRrppRingID_Object = MibTableColumn
hpnicfRrppRingID = _HpnicfRrppRingID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 2, 1, 1),
    _HpnicfRrppRingID_Type()
)
hpnicfRrppRingID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfRrppRingID.setStatus("current")
_HpnicfRrppRingEnableStatus_Type = EnabledStatus
_HpnicfRrppRingEnableStatus_Object = MibTableColumn
hpnicfRrppRingEnableStatus = _HpnicfRrppRingEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 2, 1, 2),
    _HpnicfRrppRingEnableStatus_Type()
)
hpnicfRrppRingEnableStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRrppRingEnableStatus.setStatus("current")


class _HpnicfRrppRingActive_Type(Integer32):
    """Custom type hpnicfRrppRingActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_HpnicfRrppRingActive_Type.__name__ = "Integer32"
_HpnicfRrppRingActive_Object = MibTableColumn
hpnicfRrppRingActive = _HpnicfRrppRingActive_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 2, 1, 3),
    _HpnicfRrppRingActive_Type()
)
hpnicfRrppRingActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRrppRingActive.setStatus("current")


class _HpnicfRrppRingState_Type(Integer32):
    """Custom type hpnicfRrppRingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fault", 3),
          ("health", 2),
          ("unknown", 1))
    )


_HpnicfRrppRingState_Type.__name__ = "Integer32"
_HpnicfRrppRingState_Object = MibTableColumn
hpnicfRrppRingState = _HpnicfRrppRingState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 2, 1, 4),
    _HpnicfRrppRingState_Type()
)
hpnicfRrppRingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRrppRingState.setStatus("current")


class _HpnicfRrppRingNodeMode_Type(Integer32):
    """Custom type hpnicfRrppRingNodeMode based on Integer32"""
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
        *(("assistantEdge", 4),
          ("edge", 3),
          ("master", 1),
          ("transit", 2))
    )


_HpnicfRrppRingNodeMode_Type.__name__ = "Integer32"
_HpnicfRrppRingNodeMode_Object = MibTableColumn
hpnicfRrppRingNodeMode = _HpnicfRrppRingNodeMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 2, 1, 5),
    _HpnicfRrppRingNodeMode_Type()
)
hpnicfRrppRingNodeMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRrppRingNodeMode.setStatus("current")
_HpnicfRrppRingPrimaryPort_Type = Integer32
_HpnicfRrppRingPrimaryPort_Object = MibTableColumn
hpnicfRrppRingPrimaryPort = _HpnicfRrppRingPrimaryPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 2, 1, 6),
    _HpnicfRrppRingPrimaryPort_Type()
)
hpnicfRrppRingPrimaryPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRrppRingPrimaryPort.setStatus("current")
_HpnicfRrppRingSecondaryPort_Type = Integer32
_HpnicfRrppRingSecondaryPort_Object = MibTableColumn
hpnicfRrppRingSecondaryPort = _HpnicfRrppRingSecondaryPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 2, 1, 7),
    _HpnicfRrppRingSecondaryPort_Type()
)
hpnicfRrppRingSecondaryPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRrppRingSecondaryPort.setStatus("current")


class _HpnicfRrppRingLevel_Type(Integer32):
    """Custom type hpnicfRrppRingLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("majorRing", 1),
          ("subRing", 2))
    )


_HpnicfRrppRingLevel_Type.__name__ = "Integer32"
_HpnicfRrppRingLevel_Object = MibTableColumn
hpnicfRrppRingLevel = _HpnicfRrppRingLevel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 2, 1, 8),
    _HpnicfRrppRingLevel_Type()
)
hpnicfRrppRingLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRrppRingLevel.setStatus("current")
_HpnicfRrppRingRowStatus_Type = RowStatus
_HpnicfRrppRingRowStatus_Object = MibTableColumn
hpnicfRrppRingRowStatus = _HpnicfRrppRingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 2, 1, 9),
    _HpnicfRrppRingRowStatus_Type()
)
hpnicfRrppRingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRrppRingRowStatus.setStatus("current")
_HpnicfRrppPortTable_Object = MibTable
hpnicfRrppPortTable = _HpnicfRrppPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 3)
)
if mibBuilder.loadTexts:
    hpnicfRrppPortTable.setStatus("current")
_HpnicfRrppPortEntry_Object = MibTableRow
hpnicfRrppPortEntry = _HpnicfRrppPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 3, 1)
)
hpnicfRrppPortEntry.setIndexNames(
    (0, "HPN-ICF-RRPP-MIB", "hpnicfRrppDomainID"),
    (0, "HPN-ICF-RRPP-MIB", "hpnicfRrppRingID"),
    (0, "HPN-ICF-RRPP-MIB", "hpnicfRrppPortID"),
)
if mibBuilder.loadTexts:
    hpnicfRrppPortEntry.setStatus("current")
_HpnicfRrppPortID_Type = Integer32
_HpnicfRrppPortID_Object = MibTableColumn
hpnicfRrppPortID = _HpnicfRrppPortID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 3, 1, 1),
    _HpnicfRrppPortID_Type()
)
hpnicfRrppPortID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfRrppPortID.setStatus("current")


class _HpnicfRrppPortRole_Type(Integer32):
    """Custom type hpnicfRrppPortRole based on Integer32"""
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
        *(("common", 3),
          ("edge", 4),
          ("primary", 1),
          ("secondary", 2))
    )


_HpnicfRrppPortRole_Type.__name__ = "Integer32"
_HpnicfRrppPortRole_Object = MibTableColumn
hpnicfRrppPortRole = _HpnicfRrppPortRole_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 3, 1, 2),
    _HpnicfRrppPortRole_Type()
)
hpnicfRrppPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRrppPortRole.setStatus("current")


class _HpnicfRrppPortState_Type(Integer32):
    """Custom type hpnicfRrppPortState based on Integer32"""
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
        *(("blocked", 3),
          ("down", 4),
          ("unblocked", 2),
          ("unknown", 1))
    )


_HpnicfRrppPortState_Type.__name__ = "Integer32"
_HpnicfRrppPortState_Object = MibTableColumn
hpnicfRrppPortState = _HpnicfRrppPortState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 3, 1, 3),
    _HpnicfRrppPortState_Type()
)
hpnicfRrppPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRrppPortState.setStatus("current")
_HpnicfRrppPortRXError_Type = Counter32
_HpnicfRrppPortRXError_Object = MibTableColumn
hpnicfRrppPortRXError = _HpnicfRrppPortRXError_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 3, 1, 4),
    _HpnicfRrppPortRXError_Type()
)
hpnicfRrppPortRXError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRrppPortRXError.setStatus("current")
_HpnicfRrppPortRXHello_Type = Counter32
_HpnicfRrppPortRXHello_Object = MibTableColumn
hpnicfRrppPortRXHello = _HpnicfRrppPortRXHello_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 3, 1, 5),
    _HpnicfRrppPortRXHello_Type()
)
hpnicfRrppPortRXHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRrppPortRXHello.setStatus("current")
_HpnicfRrppPortRXLinkUp_Type = Counter32
_HpnicfRrppPortRXLinkUp_Object = MibTableColumn
hpnicfRrppPortRXLinkUp = _HpnicfRrppPortRXLinkUp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 3, 1, 6),
    _HpnicfRrppPortRXLinkUp_Type()
)
hpnicfRrppPortRXLinkUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRrppPortRXLinkUp.setStatus("current")
_HpnicfRrppPortRXLinkDown_Type = Counter32
_HpnicfRrppPortRXLinkDown_Object = MibTableColumn
hpnicfRrppPortRXLinkDown = _HpnicfRrppPortRXLinkDown_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 3, 1, 7),
    _HpnicfRrppPortRXLinkDown_Type()
)
hpnicfRrppPortRXLinkDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRrppPortRXLinkDown.setStatus("current")
_HpnicfRrppPortRXCommonFlush_Type = Counter32
_HpnicfRrppPortRXCommonFlush_Object = MibTableColumn
hpnicfRrppPortRXCommonFlush = _HpnicfRrppPortRXCommonFlush_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 3, 1, 8),
    _HpnicfRrppPortRXCommonFlush_Type()
)
hpnicfRrppPortRXCommonFlush.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRrppPortRXCommonFlush.setStatus("current")
_HpnicfRrppPortRXCompleteFlush_Type = Counter32
_HpnicfRrppPortRXCompleteFlush_Object = MibTableColumn
hpnicfRrppPortRXCompleteFlush = _HpnicfRrppPortRXCompleteFlush_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 3, 1, 9),
    _HpnicfRrppPortRXCompleteFlush_Type()
)
hpnicfRrppPortRXCompleteFlush.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRrppPortRXCompleteFlush.setStatus("current")
_HpnicfRrppPortTXHello_Type = Counter32
_HpnicfRrppPortTXHello_Object = MibTableColumn
hpnicfRrppPortTXHello = _HpnicfRrppPortTXHello_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 3, 1, 10),
    _HpnicfRrppPortTXHello_Type()
)
hpnicfRrppPortTXHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRrppPortTXHello.setStatus("current")
_HpnicfRrppPortTXLinkUp_Type = Counter32
_HpnicfRrppPortTXLinkUp_Object = MibTableColumn
hpnicfRrppPortTXLinkUp = _HpnicfRrppPortTXLinkUp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 3, 1, 11),
    _HpnicfRrppPortTXLinkUp_Type()
)
hpnicfRrppPortTXLinkUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRrppPortTXLinkUp.setStatus("current")
_HpnicfRrppPortTXLinkDown_Type = Counter32
_HpnicfRrppPortTXLinkDown_Object = MibTableColumn
hpnicfRrppPortTXLinkDown = _HpnicfRrppPortTXLinkDown_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 3, 1, 12),
    _HpnicfRrppPortTXLinkDown_Type()
)
hpnicfRrppPortTXLinkDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRrppPortTXLinkDown.setStatus("current")
_HpnicfRrppPortTXCommonFlush_Type = Counter32
_HpnicfRrppPortTXCommonFlush_Object = MibTableColumn
hpnicfRrppPortTXCommonFlush = _HpnicfRrppPortTXCommonFlush_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 3, 1, 13),
    _HpnicfRrppPortTXCommonFlush_Type()
)
hpnicfRrppPortTXCommonFlush.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRrppPortTXCommonFlush.setStatus("current")
_HpnicfRrppPortTXCompleteFlush_Type = Counter32
_HpnicfRrppPortTXCompleteFlush_Object = MibTableColumn
hpnicfRrppPortTXCompleteFlush = _HpnicfRrppPortTXCompleteFlush_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 3, 1, 14),
    _HpnicfRrppPortTXCompleteFlush_Type()
)
hpnicfRrppPortTXCompleteFlush.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRrppPortTXCompleteFlush.setStatus("current")
_HpnicfRrppPortRXEdgeHello_Type = Counter32
_HpnicfRrppPortRXEdgeHello_Object = MibTableColumn
hpnicfRrppPortRXEdgeHello = _HpnicfRrppPortRXEdgeHello_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 3, 1, 15),
    _HpnicfRrppPortRXEdgeHello_Type()
)
hpnicfRrppPortRXEdgeHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRrppPortRXEdgeHello.setStatus("current")
_HpnicfRrppPortRXMajorFault_Type = Counter32
_HpnicfRrppPortRXMajorFault_Object = MibTableColumn
hpnicfRrppPortRXMajorFault = _HpnicfRrppPortRXMajorFault_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 3, 1, 16),
    _HpnicfRrppPortRXMajorFault_Type()
)
hpnicfRrppPortRXMajorFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRrppPortRXMajorFault.setStatus("current")
_HpnicfRrppPortTXEdgeHello_Type = Counter32
_HpnicfRrppPortTXEdgeHello_Object = MibTableColumn
hpnicfRrppPortTXEdgeHello = _HpnicfRrppPortTXEdgeHello_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 3, 1, 17),
    _HpnicfRrppPortTXEdgeHello_Type()
)
hpnicfRrppPortTXEdgeHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRrppPortTXEdgeHello.setStatus("current")
_HpnicfRrppPortTXMajorFault_Type = Counter32
_HpnicfRrppPortTXMajorFault_Object = MibTableColumn
hpnicfRrppPortTXMajorFault = _HpnicfRrppPortTXMajorFault_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 3, 1, 18),
    _HpnicfRrppPortTXMajorFault_Type()
)
hpnicfRrppPortTXMajorFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRrppPortTXMajorFault.setStatus("current")
_HpnicfRrppNotifications_ObjectIdentity = ObjectIdentity
hpnicfRrppNotifications = _HpnicfRrppNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 3)
)

# Managed Objects groups


# Notification objects

hpnicfRrppRingRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 3, 1)
)
hpnicfRrppRingRecover.setObjects(
      *(("HPN-ICF-RRPP-MIB", "hpnicfRrppDomainID"),
        ("HPN-ICF-RRPP-MIB", "hpnicfRrppRingID"))
)
if mibBuilder.loadTexts:
    hpnicfRrppRingRecover.setStatus(
        "current"
    )

hpnicfRrppRingFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 3, 2)
)
hpnicfRrppRingFail.setObjects(
      *(("HPN-ICF-RRPP-MIB", "hpnicfRrppDomainID"),
        ("HPN-ICF-RRPP-MIB", "hpnicfRrppRingID"))
)
if mibBuilder.loadTexts:
    hpnicfRrppRingFail.setStatus(
        "current"
    )

hpnicfRrppMultiMaster = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 3, 3)
)
hpnicfRrppMultiMaster.setObjects(
      *(("HPN-ICF-RRPP-MIB", "hpnicfRrppDomainID"),
        ("HPN-ICF-RRPP-MIB", "hpnicfRrppRingID"))
)
if mibBuilder.loadTexts:
    hpnicfRrppMultiMaster.setStatus(
        "current"
    )

hpnicfRrppMajorFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 3, 4)
)
hpnicfRrppMajorFault.setObjects(
      *(("HPN-ICF-RRPP-MIB", "hpnicfRrppDomainID"),
        ("HPN-ICF-RRPP-MIB", "hpnicfRrppRingID"))
)
if mibBuilder.loadTexts:
    hpnicfRrppMajorFault.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-RRPP-MIB",
    **{"EnabledStatus": EnabledStatus,
       "hpnicfRrpp": hpnicfRrpp,
       "hpnicfRrppScalarGroup": hpnicfRrppScalarGroup,
       "hpnicfRrppEnableStatus": hpnicfRrppEnableStatus,
       "hpnicfRrppPassword": hpnicfRrppPassword,
       "hpnicfRrppPasswordType": hpnicfRrppPasswordType,
       "hpnicfRrppProtectVlanConfigMode": hpnicfRrppProtectVlanConfigMode,
       "hpnicfRrppTable": hpnicfRrppTable,
       "hpnicfRrppDomainTable": hpnicfRrppDomainTable,
       "hpnicfRrppDomainEntry": hpnicfRrppDomainEntry,
       "hpnicfRrppDomainID": hpnicfRrppDomainID,
       "hpnicfRrppDomainControlVlanID": hpnicfRrppDomainControlVlanID,
       "hpnicfRrppDomainHelloTime": hpnicfRrppDomainHelloTime,
       "hpnicfRrppDomainFailTime": hpnicfRrppDomainFailTime,
       "hpnicfRrppDomainRowStatus": hpnicfRrppDomainRowStatus,
       "hpnicfRrppDomainInstanceListLow": hpnicfRrppDomainInstanceListLow,
       "hpnicfRrppDomainInstanceListHigh": hpnicfRrppDomainInstanceListHigh,
       "hpnicfRrppDomainProtectVlanListLow": hpnicfRrppDomainProtectVlanListLow,
       "hpnicfRrppDomainProtectVlanListHigh": hpnicfRrppDomainProtectVlanListHigh,
       "hpnicfRrppRingTable": hpnicfRrppRingTable,
       "hpnicfRrppRingEntry": hpnicfRrppRingEntry,
       "hpnicfRrppRingID": hpnicfRrppRingID,
       "hpnicfRrppRingEnableStatus": hpnicfRrppRingEnableStatus,
       "hpnicfRrppRingActive": hpnicfRrppRingActive,
       "hpnicfRrppRingState": hpnicfRrppRingState,
       "hpnicfRrppRingNodeMode": hpnicfRrppRingNodeMode,
       "hpnicfRrppRingPrimaryPort": hpnicfRrppRingPrimaryPort,
       "hpnicfRrppRingSecondaryPort": hpnicfRrppRingSecondaryPort,
       "hpnicfRrppRingLevel": hpnicfRrppRingLevel,
       "hpnicfRrppRingRowStatus": hpnicfRrppRingRowStatus,
       "hpnicfRrppPortTable": hpnicfRrppPortTable,
       "hpnicfRrppPortEntry": hpnicfRrppPortEntry,
       "hpnicfRrppPortID": hpnicfRrppPortID,
       "hpnicfRrppPortRole": hpnicfRrppPortRole,
       "hpnicfRrppPortState": hpnicfRrppPortState,
       "hpnicfRrppPortRXError": hpnicfRrppPortRXError,
       "hpnicfRrppPortRXHello": hpnicfRrppPortRXHello,
       "hpnicfRrppPortRXLinkUp": hpnicfRrppPortRXLinkUp,
       "hpnicfRrppPortRXLinkDown": hpnicfRrppPortRXLinkDown,
       "hpnicfRrppPortRXCommonFlush": hpnicfRrppPortRXCommonFlush,
       "hpnicfRrppPortRXCompleteFlush": hpnicfRrppPortRXCompleteFlush,
       "hpnicfRrppPortTXHello": hpnicfRrppPortTXHello,
       "hpnicfRrppPortTXLinkUp": hpnicfRrppPortTXLinkUp,
       "hpnicfRrppPortTXLinkDown": hpnicfRrppPortTXLinkDown,
       "hpnicfRrppPortTXCommonFlush": hpnicfRrppPortTXCommonFlush,
       "hpnicfRrppPortTXCompleteFlush": hpnicfRrppPortTXCompleteFlush,
       "hpnicfRrppPortRXEdgeHello": hpnicfRrppPortRXEdgeHello,
       "hpnicfRrppPortRXMajorFault": hpnicfRrppPortRXMajorFault,
       "hpnicfRrppPortTXEdgeHello": hpnicfRrppPortTXEdgeHello,
       "hpnicfRrppPortTXMajorFault": hpnicfRrppPortTXMajorFault,
       "hpnicfRrppNotifications": hpnicfRrppNotifications,
       "hpnicfRrppRingRecover": hpnicfRrppRingRecover,
       "hpnicfRrppRingFail": hpnicfRrppRingFail,
       "hpnicfRrppMultiMaster": hpnicfRrppMultiMaster,
       "hpnicfRrppMajorFault": hpnicfRrppMajorFault}
)
