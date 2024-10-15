# SNMP MIB module (HH3C-RRPP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-RRPP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:47 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cRrpp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 45)
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

_Hh3cRrppScalarGroup_ObjectIdentity = ObjectIdentity
hh3cRrppScalarGroup = _Hh3cRrppScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 45, 1)
)
_Hh3cRrppEnableStatus_Type = EnabledStatus
_Hh3cRrppEnableStatus_Object = MibScalar
hh3cRrppEnableStatus = _Hh3cRrppEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 45, 1, 1),
    _Hh3cRrppEnableStatus_Type()
)
hh3cRrppEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cRrppEnableStatus.setStatus("current")


class _Hh3cRrppPassword_Type(OctetString):
    """Custom type hh3cRrppPassword based on OctetString"""
    defaultHexValue = "303030464532303346443735"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Hh3cRrppPassword_Type.__name__ = "OctetString"
_Hh3cRrppPassword_Object = MibScalar
hh3cRrppPassword = _Hh3cRrppPassword_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 45, 1, 2),
    _Hh3cRrppPassword_Type()
)
hh3cRrppPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cRrppPassword.setStatus("current")


class _Hh3cRrppPasswordType_Type(Integer32):
    """Custom type hh3cRrppPasswordType based on Integer32"""
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


_Hh3cRrppPasswordType_Type.__name__ = "Integer32"
_Hh3cRrppPasswordType_Object = MibScalar
hh3cRrppPasswordType = _Hh3cRrppPasswordType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 45, 1, 3),
    _Hh3cRrppPasswordType_Type()
)
hh3cRrppPasswordType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cRrppPasswordType.setStatus("current")


class _Hh3cRrppProtectVlanConfigMode_Type(Integer32):
    """Custom type hh3cRrppProtectVlanConfigMode based on Integer32"""
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


_Hh3cRrppProtectVlanConfigMode_Type.__name__ = "Integer32"
_Hh3cRrppProtectVlanConfigMode_Object = MibScalar
hh3cRrppProtectVlanConfigMode = _Hh3cRrppProtectVlanConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 45, 1, 4),
    _Hh3cRrppProtectVlanConfigMode_Type()
)
hh3cRrppProtectVlanConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRrppProtectVlanConfigMode.setStatus("current")
_Hh3cRrppTable_ObjectIdentity = ObjectIdentity
hh3cRrppTable = _Hh3cRrppTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 45, 2)
)
_Hh3cRrppDomainTable_Object = MibTable
hh3cRrppDomainTable = _Hh3cRrppDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cRrppDomainTable.setStatus("current")
_Hh3cRrppDomainEntry_Object = MibTableRow
hh3cRrppDomainEntry = _Hh3cRrppDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 1, 1)
)
hh3cRrppDomainEntry.setIndexNames(
    (0, "HH3C-RRPP-MIB", "hh3cRrppDomainID"),
)
if mibBuilder.loadTexts:
    hh3cRrppDomainEntry.setStatus("current")


class _Hh3cRrppDomainID_Type(Integer32):
    """Custom type hh3cRrppDomainID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Hh3cRrppDomainID_Type.__name__ = "Integer32"
_Hh3cRrppDomainID_Object = MibTableColumn
hh3cRrppDomainID = _Hh3cRrppDomainID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 1, 1, 1),
    _Hh3cRrppDomainID_Type()
)
hh3cRrppDomainID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cRrppDomainID.setStatus("current")


class _Hh3cRrppDomainControlVlanID_Type(Integer32):
    """Custom type hh3cRrppDomainControlVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4094),
        ValueRangeConstraint(65535, 65535),
    )


_Hh3cRrppDomainControlVlanID_Type.__name__ = "Integer32"
_Hh3cRrppDomainControlVlanID_Object = MibTableColumn
hh3cRrppDomainControlVlanID = _Hh3cRrppDomainControlVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 1, 1, 2),
    _Hh3cRrppDomainControlVlanID_Type()
)
hh3cRrppDomainControlVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRrppDomainControlVlanID.setStatus("current")


class _Hh3cRrppDomainHelloTime_Type(Integer32):
    """Custom type hh3cRrppDomainHelloTime based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Hh3cRrppDomainHelloTime_Type.__name__ = "Integer32"
_Hh3cRrppDomainHelloTime_Object = MibTableColumn
hh3cRrppDomainHelloTime = _Hh3cRrppDomainHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 1, 1, 3),
    _Hh3cRrppDomainHelloTime_Type()
)
hh3cRrppDomainHelloTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRrppDomainHelloTime.setStatus("current")


class _Hh3cRrppDomainFailTime_Type(Integer32):
    """Custom type hh3cRrppDomainFailTime based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 30),
    )


_Hh3cRrppDomainFailTime_Type.__name__ = "Integer32"
_Hh3cRrppDomainFailTime_Object = MibTableColumn
hh3cRrppDomainFailTime = _Hh3cRrppDomainFailTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 1, 1, 4),
    _Hh3cRrppDomainFailTime_Type()
)
hh3cRrppDomainFailTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRrppDomainFailTime.setStatus("current")
_Hh3cRrppDomainRowStatus_Type = RowStatus
_Hh3cRrppDomainRowStatus_Object = MibTableColumn
hh3cRrppDomainRowStatus = _Hh3cRrppDomainRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 1, 1, 5),
    _Hh3cRrppDomainRowStatus_Type()
)
hh3cRrppDomainRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRrppDomainRowStatus.setStatus("current")


class _Hh3cRrppDomainInstanceListLow_Type(OctetString):
    """Custom type hh3cRrppDomainInstanceListLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_Hh3cRrppDomainInstanceListLow_Type.__name__ = "OctetString"
_Hh3cRrppDomainInstanceListLow_Object = MibTableColumn
hh3cRrppDomainInstanceListLow = _Hh3cRrppDomainInstanceListLow_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 1, 1, 6),
    _Hh3cRrppDomainInstanceListLow_Type()
)
hh3cRrppDomainInstanceListLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRrppDomainInstanceListLow.setStatus("current")


class _Hh3cRrppDomainInstanceListHigh_Type(OctetString):
    """Custom type hh3cRrppDomainInstanceListHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_Hh3cRrppDomainInstanceListHigh_Type.__name__ = "OctetString"
_Hh3cRrppDomainInstanceListHigh_Object = MibTableColumn
hh3cRrppDomainInstanceListHigh = _Hh3cRrppDomainInstanceListHigh_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 1, 1, 7),
    _Hh3cRrppDomainInstanceListHigh_Type()
)
hh3cRrppDomainInstanceListHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRrppDomainInstanceListHigh.setStatus("current")


class _Hh3cRrppDomainProtectVlanListLow_Type(OctetString):
    """Custom type hh3cRrppDomainProtectVlanListLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_Hh3cRrppDomainProtectVlanListLow_Type.__name__ = "OctetString"
_Hh3cRrppDomainProtectVlanListLow_Object = MibTableColumn
hh3cRrppDomainProtectVlanListLow = _Hh3cRrppDomainProtectVlanListLow_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 1, 1, 8),
    _Hh3cRrppDomainProtectVlanListLow_Type()
)
hh3cRrppDomainProtectVlanListLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRrppDomainProtectVlanListLow.setStatus("current")


class _Hh3cRrppDomainProtectVlanListHigh_Type(OctetString):
    """Custom type hh3cRrppDomainProtectVlanListHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_Hh3cRrppDomainProtectVlanListHigh_Type.__name__ = "OctetString"
_Hh3cRrppDomainProtectVlanListHigh_Object = MibTableColumn
hh3cRrppDomainProtectVlanListHigh = _Hh3cRrppDomainProtectVlanListHigh_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 1, 1, 9),
    _Hh3cRrppDomainProtectVlanListHigh_Type()
)
hh3cRrppDomainProtectVlanListHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRrppDomainProtectVlanListHigh.setStatus("current")
_Hh3cRrppRingTable_Object = MibTable
hh3cRrppRingTable = _Hh3cRrppRingTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cRrppRingTable.setStatus("current")
_Hh3cRrppRingEntry_Object = MibTableRow
hh3cRrppRingEntry = _Hh3cRrppRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 2, 1)
)
hh3cRrppRingEntry.setIndexNames(
    (0, "HH3C-RRPP-MIB", "hh3cRrppDomainID"),
    (0, "HH3C-RRPP-MIB", "hh3cRrppRingID"),
)
if mibBuilder.loadTexts:
    hh3cRrppRingEntry.setStatus("current")


class _Hh3cRrppRingID_Type(Integer32):
    """Custom type hh3cRrppRingID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Hh3cRrppRingID_Type.__name__ = "Integer32"
_Hh3cRrppRingID_Object = MibTableColumn
hh3cRrppRingID = _Hh3cRrppRingID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 2, 1, 1),
    _Hh3cRrppRingID_Type()
)
hh3cRrppRingID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cRrppRingID.setStatus("current")
_Hh3cRrppRingEnableStatus_Type = EnabledStatus
_Hh3cRrppRingEnableStatus_Object = MibTableColumn
hh3cRrppRingEnableStatus = _Hh3cRrppRingEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 2, 1, 2),
    _Hh3cRrppRingEnableStatus_Type()
)
hh3cRrppRingEnableStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRrppRingEnableStatus.setStatus("current")


class _Hh3cRrppRingActive_Type(Integer32):
    """Custom type hh3cRrppRingActive based on Integer32"""
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


_Hh3cRrppRingActive_Type.__name__ = "Integer32"
_Hh3cRrppRingActive_Object = MibTableColumn
hh3cRrppRingActive = _Hh3cRrppRingActive_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 2, 1, 3),
    _Hh3cRrppRingActive_Type()
)
hh3cRrppRingActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRrppRingActive.setStatus("current")


class _Hh3cRrppRingState_Type(Integer32):
    """Custom type hh3cRrppRingState based on Integer32"""
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


_Hh3cRrppRingState_Type.__name__ = "Integer32"
_Hh3cRrppRingState_Object = MibTableColumn
hh3cRrppRingState = _Hh3cRrppRingState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 2, 1, 4),
    _Hh3cRrppRingState_Type()
)
hh3cRrppRingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRrppRingState.setStatus("current")


class _Hh3cRrppRingNodeMode_Type(Integer32):
    """Custom type hh3cRrppRingNodeMode based on Integer32"""
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


_Hh3cRrppRingNodeMode_Type.__name__ = "Integer32"
_Hh3cRrppRingNodeMode_Object = MibTableColumn
hh3cRrppRingNodeMode = _Hh3cRrppRingNodeMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 2, 1, 5),
    _Hh3cRrppRingNodeMode_Type()
)
hh3cRrppRingNodeMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRrppRingNodeMode.setStatus("current")
_Hh3cRrppRingPrimaryPort_Type = Integer32
_Hh3cRrppRingPrimaryPort_Object = MibTableColumn
hh3cRrppRingPrimaryPort = _Hh3cRrppRingPrimaryPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 2, 1, 6),
    _Hh3cRrppRingPrimaryPort_Type()
)
hh3cRrppRingPrimaryPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRrppRingPrimaryPort.setStatus("current")
_Hh3cRrppRingSecondaryPort_Type = Integer32
_Hh3cRrppRingSecondaryPort_Object = MibTableColumn
hh3cRrppRingSecondaryPort = _Hh3cRrppRingSecondaryPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 2, 1, 7),
    _Hh3cRrppRingSecondaryPort_Type()
)
hh3cRrppRingSecondaryPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRrppRingSecondaryPort.setStatus("current")


class _Hh3cRrppRingLevel_Type(Integer32):
    """Custom type hh3cRrppRingLevel based on Integer32"""
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


_Hh3cRrppRingLevel_Type.__name__ = "Integer32"
_Hh3cRrppRingLevel_Object = MibTableColumn
hh3cRrppRingLevel = _Hh3cRrppRingLevel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 2, 1, 8),
    _Hh3cRrppRingLevel_Type()
)
hh3cRrppRingLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRrppRingLevel.setStatus("current")
_Hh3cRrppRingRowStatus_Type = RowStatus
_Hh3cRrppRingRowStatus_Object = MibTableColumn
hh3cRrppRingRowStatus = _Hh3cRrppRingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 2, 1, 9),
    _Hh3cRrppRingRowStatus_Type()
)
hh3cRrppRingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRrppRingRowStatus.setStatus("current")
_Hh3cRrppPortTable_Object = MibTable
hh3cRrppPortTable = _Hh3cRrppPortTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cRrppPortTable.setStatus("current")
_Hh3cRrppPortEntry_Object = MibTableRow
hh3cRrppPortEntry = _Hh3cRrppPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 3, 1)
)
hh3cRrppPortEntry.setIndexNames(
    (0, "HH3C-RRPP-MIB", "hh3cRrppDomainID"),
    (0, "HH3C-RRPP-MIB", "hh3cRrppRingID"),
    (0, "HH3C-RRPP-MIB", "hh3cRrppPortID"),
)
if mibBuilder.loadTexts:
    hh3cRrppPortEntry.setStatus("current")
_Hh3cRrppPortID_Type = Integer32
_Hh3cRrppPortID_Object = MibTableColumn
hh3cRrppPortID = _Hh3cRrppPortID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 3, 1, 1),
    _Hh3cRrppPortID_Type()
)
hh3cRrppPortID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRrppPortID.setStatus("current")


class _Hh3cRrppPortRole_Type(Integer32):
    """Custom type hh3cRrppPortRole based on Integer32"""
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


_Hh3cRrppPortRole_Type.__name__ = "Integer32"
_Hh3cRrppPortRole_Object = MibTableColumn
hh3cRrppPortRole = _Hh3cRrppPortRole_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 3, 1, 2),
    _Hh3cRrppPortRole_Type()
)
hh3cRrppPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRrppPortRole.setStatus("current")


class _Hh3cRrppPortState_Type(Integer32):
    """Custom type hh3cRrppPortState based on Integer32"""
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


_Hh3cRrppPortState_Type.__name__ = "Integer32"
_Hh3cRrppPortState_Object = MibTableColumn
hh3cRrppPortState = _Hh3cRrppPortState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 3, 1, 3),
    _Hh3cRrppPortState_Type()
)
hh3cRrppPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRrppPortState.setStatus("current")
_Hh3cRrppPortRXError_Type = Counter32
_Hh3cRrppPortRXError_Object = MibTableColumn
hh3cRrppPortRXError = _Hh3cRrppPortRXError_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 3, 1, 4),
    _Hh3cRrppPortRXError_Type()
)
hh3cRrppPortRXError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRrppPortRXError.setStatus("current")
_Hh3cRrppPortRXHello_Type = Counter32
_Hh3cRrppPortRXHello_Object = MibTableColumn
hh3cRrppPortRXHello = _Hh3cRrppPortRXHello_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 3, 1, 5),
    _Hh3cRrppPortRXHello_Type()
)
hh3cRrppPortRXHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRrppPortRXHello.setStatus("current")
_Hh3cRrppPortRXLinkUp_Type = Counter32
_Hh3cRrppPortRXLinkUp_Object = MibTableColumn
hh3cRrppPortRXLinkUp = _Hh3cRrppPortRXLinkUp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 3, 1, 6),
    _Hh3cRrppPortRXLinkUp_Type()
)
hh3cRrppPortRXLinkUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRrppPortRXLinkUp.setStatus("current")
_Hh3cRrppPortRXLinkDown_Type = Counter32
_Hh3cRrppPortRXLinkDown_Object = MibTableColumn
hh3cRrppPortRXLinkDown = _Hh3cRrppPortRXLinkDown_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 3, 1, 7),
    _Hh3cRrppPortRXLinkDown_Type()
)
hh3cRrppPortRXLinkDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRrppPortRXLinkDown.setStatus("current")
_Hh3cRrppPortRXCommonFlush_Type = Counter32
_Hh3cRrppPortRXCommonFlush_Object = MibTableColumn
hh3cRrppPortRXCommonFlush = _Hh3cRrppPortRXCommonFlush_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 3, 1, 8),
    _Hh3cRrppPortRXCommonFlush_Type()
)
hh3cRrppPortRXCommonFlush.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRrppPortRXCommonFlush.setStatus("current")
_Hh3cRrppPortRXCompleteFlush_Type = Counter32
_Hh3cRrppPortRXCompleteFlush_Object = MibTableColumn
hh3cRrppPortRXCompleteFlush = _Hh3cRrppPortRXCompleteFlush_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 3, 1, 9),
    _Hh3cRrppPortRXCompleteFlush_Type()
)
hh3cRrppPortRXCompleteFlush.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRrppPortRXCompleteFlush.setStatus("current")
_Hh3cRrppPortTXHello_Type = Counter32
_Hh3cRrppPortTXHello_Object = MibTableColumn
hh3cRrppPortTXHello = _Hh3cRrppPortTXHello_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 3, 1, 10),
    _Hh3cRrppPortTXHello_Type()
)
hh3cRrppPortTXHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRrppPortTXHello.setStatus("current")
_Hh3cRrppPortTXLinkUp_Type = Counter32
_Hh3cRrppPortTXLinkUp_Object = MibTableColumn
hh3cRrppPortTXLinkUp = _Hh3cRrppPortTXLinkUp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 3, 1, 11),
    _Hh3cRrppPortTXLinkUp_Type()
)
hh3cRrppPortTXLinkUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRrppPortTXLinkUp.setStatus("current")
_Hh3cRrppPortTXLinkDown_Type = Counter32
_Hh3cRrppPortTXLinkDown_Object = MibTableColumn
hh3cRrppPortTXLinkDown = _Hh3cRrppPortTXLinkDown_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 3, 1, 12),
    _Hh3cRrppPortTXLinkDown_Type()
)
hh3cRrppPortTXLinkDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRrppPortTXLinkDown.setStatus("current")
_Hh3cRrppPortTXCommonFlush_Type = Counter32
_Hh3cRrppPortTXCommonFlush_Object = MibTableColumn
hh3cRrppPortTXCommonFlush = _Hh3cRrppPortTXCommonFlush_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 3, 1, 13),
    _Hh3cRrppPortTXCommonFlush_Type()
)
hh3cRrppPortTXCommonFlush.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRrppPortTXCommonFlush.setStatus("current")
_Hh3cRrppPortTXCompleteFlush_Type = Counter32
_Hh3cRrppPortTXCompleteFlush_Object = MibTableColumn
hh3cRrppPortTXCompleteFlush = _Hh3cRrppPortTXCompleteFlush_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 3, 1, 14),
    _Hh3cRrppPortTXCompleteFlush_Type()
)
hh3cRrppPortTXCompleteFlush.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRrppPortTXCompleteFlush.setStatus("current")
_Hh3cRrppPortRXEdgeHello_Type = Counter32
_Hh3cRrppPortRXEdgeHello_Object = MibTableColumn
hh3cRrppPortRXEdgeHello = _Hh3cRrppPortRXEdgeHello_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 3, 1, 15),
    _Hh3cRrppPortRXEdgeHello_Type()
)
hh3cRrppPortRXEdgeHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRrppPortRXEdgeHello.setStatus("current")
_Hh3cRrppPortRXMajorFault_Type = Counter32
_Hh3cRrppPortRXMajorFault_Object = MibTableColumn
hh3cRrppPortRXMajorFault = _Hh3cRrppPortRXMajorFault_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 3, 1, 16),
    _Hh3cRrppPortRXMajorFault_Type()
)
hh3cRrppPortRXMajorFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRrppPortRXMajorFault.setStatus("current")
_Hh3cRrppPortTXEdgeHello_Type = Counter32
_Hh3cRrppPortTXEdgeHello_Object = MibTableColumn
hh3cRrppPortTXEdgeHello = _Hh3cRrppPortTXEdgeHello_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 3, 1, 17),
    _Hh3cRrppPortTXEdgeHello_Type()
)
hh3cRrppPortTXEdgeHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRrppPortTXEdgeHello.setStatus("current")
_Hh3cRrppPortTXMajorFault_Type = Counter32
_Hh3cRrppPortTXMajorFault_Object = MibTableColumn
hh3cRrppPortTXMajorFault = _Hh3cRrppPortTXMajorFault_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 3, 1, 18),
    _Hh3cRrppPortTXMajorFault_Type()
)
hh3cRrppPortTXMajorFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRrppPortTXMajorFault.setStatus("current")
_Hh3cRrppNotifications_ObjectIdentity = ObjectIdentity
hh3cRrppNotifications = _Hh3cRrppNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 45, 3)
)

# Managed Objects groups


# Notification objects

hh3cRrppRingRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 45, 3, 1)
)
hh3cRrppRingRecover.setObjects(
      *(("HH3C-RRPP-MIB", "hh3cRrppDomainID"),
        ("HH3C-RRPP-MIB", "hh3cRrppRingID"))
)
if mibBuilder.loadTexts:
    hh3cRrppRingRecover.setStatus(
        "current"
    )

hh3cRrppRingFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 45, 3, 2)
)
hh3cRrppRingFail.setObjects(
      *(("HH3C-RRPP-MIB", "hh3cRrppDomainID"),
        ("HH3C-RRPP-MIB", "hh3cRrppRingID"))
)
if mibBuilder.loadTexts:
    hh3cRrppRingFail.setStatus(
        "current"
    )

hh3cRrppMultiMaster = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 45, 3, 3)
)
hh3cRrppMultiMaster.setObjects(
      *(("HH3C-RRPP-MIB", "hh3cRrppDomainID"),
        ("HH3C-RRPP-MIB", "hh3cRrppRingID"))
)
if mibBuilder.loadTexts:
    hh3cRrppMultiMaster.setStatus(
        "current"
    )

hh3cRrppMajorFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 45, 3, 4)
)
hh3cRrppMajorFault.setObjects(
      *(("HH3C-RRPP-MIB", "hh3cRrppDomainID"),
        ("HH3C-RRPP-MIB", "hh3cRrppRingID"))
)
if mibBuilder.loadTexts:
    hh3cRrppMajorFault.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-RRPP-MIB",
    **{"EnabledStatus": EnabledStatus,
       "hh3cRrpp": hh3cRrpp,
       "hh3cRrppScalarGroup": hh3cRrppScalarGroup,
       "hh3cRrppEnableStatus": hh3cRrppEnableStatus,
       "hh3cRrppPassword": hh3cRrppPassword,
       "hh3cRrppPasswordType": hh3cRrppPasswordType,
       "hh3cRrppProtectVlanConfigMode": hh3cRrppProtectVlanConfigMode,
       "hh3cRrppTable": hh3cRrppTable,
       "hh3cRrppDomainTable": hh3cRrppDomainTable,
       "hh3cRrppDomainEntry": hh3cRrppDomainEntry,
       "hh3cRrppDomainID": hh3cRrppDomainID,
       "hh3cRrppDomainControlVlanID": hh3cRrppDomainControlVlanID,
       "hh3cRrppDomainHelloTime": hh3cRrppDomainHelloTime,
       "hh3cRrppDomainFailTime": hh3cRrppDomainFailTime,
       "hh3cRrppDomainRowStatus": hh3cRrppDomainRowStatus,
       "hh3cRrppDomainInstanceListLow": hh3cRrppDomainInstanceListLow,
       "hh3cRrppDomainInstanceListHigh": hh3cRrppDomainInstanceListHigh,
       "hh3cRrppDomainProtectVlanListLow": hh3cRrppDomainProtectVlanListLow,
       "hh3cRrppDomainProtectVlanListHigh": hh3cRrppDomainProtectVlanListHigh,
       "hh3cRrppRingTable": hh3cRrppRingTable,
       "hh3cRrppRingEntry": hh3cRrppRingEntry,
       "hh3cRrppRingID": hh3cRrppRingID,
       "hh3cRrppRingEnableStatus": hh3cRrppRingEnableStatus,
       "hh3cRrppRingActive": hh3cRrppRingActive,
       "hh3cRrppRingState": hh3cRrppRingState,
       "hh3cRrppRingNodeMode": hh3cRrppRingNodeMode,
       "hh3cRrppRingPrimaryPort": hh3cRrppRingPrimaryPort,
       "hh3cRrppRingSecondaryPort": hh3cRrppRingSecondaryPort,
       "hh3cRrppRingLevel": hh3cRrppRingLevel,
       "hh3cRrppRingRowStatus": hh3cRrppRingRowStatus,
       "hh3cRrppPortTable": hh3cRrppPortTable,
       "hh3cRrppPortEntry": hh3cRrppPortEntry,
       "hh3cRrppPortID": hh3cRrppPortID,
       "hh3cRrppPortRole": hh3cRrppPortRole,
       "hh3cRrppPortState": hh3cRrppPortState,
       "hh3cRrppPortRXError": hh3cRrppPortRXError,
       "hh3cRrppPortRXHello": hh3cRrppPortRXHello,
       "hh3cRrppPortRXLinkUp": hh3cRrppPortRXLinkUp,
       "hh3cRrppPortRXLinkDown": hh3cRrppPortRXLinkDown,
       "hh3cRrppPortRXCommonFlush": hh3cRrppPortRXCommonFlush,
       "hh3cRrppPortRXCompleteFlush": hh3cRrppPortRXCompleteFlush,
       "hh3cRrppPortTXHello": hh3cRrppPortTXHello,
       "hh3cRrppPortTXLinkUp": hh3cRrppPortTXLinkUp,
       "hh3cRrppPortTXLinkDown": hh3cRrppPortTXLinkDown,
       "hh3cRrppPortTXCommonFlush": hh3cRrppPortTXCommonFlush,
       "hh3cRrppPortTXCompleteFlush": hh3cRrppPortTXCompleteFlush,
       "hh3cRrppPortRXEdgeHello": hh3cRrppPortRXEdgeHello,
       "hh3cRrppPortRXMajorFault": hh3cRrppPortRXMajorFault,
       "hh3cRrppPortTXEdgeHello": hh3cRrppPortTXEdgeHello,
       "hh3cRrppPortTXMajorFault": hh3cRrppPortTXMajorFault,
       "hh3cRrppNotifications": hh3cRrppNotifications,
       "hh3cRrppRingRecover": hh3cRrppRingRecover,
       "hh3cRrppRingFail": hh3cRrppRingFail,
       "hh3cRrppMultiMaster": hh3cRrppMultiMaster,
       "hh3cRrppMajorFault": hh3cRrppMajorFault}
)
