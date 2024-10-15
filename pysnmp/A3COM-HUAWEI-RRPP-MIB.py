# SNMP MIB module (A3COM-HUAWEI-RRPP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-RRPP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:29:01 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cCommon")

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

h3cRrpp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 45)
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

_H3cRrppScalarGroup_ObjectIdentity = ObjectIdentity
h3cRrppScalarGroup = _H3cRrppScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 45, 1)
)
_H3cRrppEnableStatus_Type = EnabledStatus
_H3cRrppEnableStatus_Object = MibScalar
h3cRrppEnableStatus = _H3cRrppEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 45, 1, 1),
    _H3cRrppEnableStatus_Type()
)
h3cRrppEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cRrppEnableStatus.setStatus("current")


class _H3cRrppPassword_Type(OctetString):
    """Custom type h3cRrppPassword based on OctetString"""
    defaultHexValue = "303030464532303346443735"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_H3cRrppPassword_Type.__name__ = "OctetString"
_H3cRrppPassword_Object = MibScalar
h3cRrppPassword = _H3cRrppPassword_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 45, 1, 2),
    _H3cRrppPassword_Type()
)
h3cRrppPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cRrppPassword.setStatus("current")


class _H3cRrppPasswordType_Type(Integer32):
    """Custom type h3cRrppPasswordType based on Integer32"""
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


_H3cRrppPasswordType_Type.__name__ = "Integer32"
_H3cRrppPasswordType_Object = MibScalar
h3cRrppPasswordType = _H3cRrppPasswordType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 45, 1, 3),
    _H3cRrppPasswordType_Type()
)
h3cRrppPasswordType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cRrppPasswordType.setStatus("current")


class _H3cRrppProtectVlanConfigMode_Type(Integer32):
    """Custom type h3cRrppProtectVlanConfigMode based on Integer32"""
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


_H3cRrppProtectVlanConfigMode_Type.__name__ = "Integer32"
_H3cRrppProtectVlanConfigMode_Object = MibScalar
h3cRrppProtectVlanConfigMode = _H3cRrppProtectVlanConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 45, 1, 4),
    _H3cRrppProtectVlanConfigMode_Type()
)
h3cRrppProtectVlanConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRrppProtectVlanConfigMode.setStatus("current")
_H3cRrppTable_ObjectIdentity = ObjectIdentity
h3cRrppTable = _H3cRrppTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 45, 2)
)
_H3cRrppDomainTable_Object = MibTable
h3cRrppDomainTable = _H3cRrppDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 45, 2, 1)
)
if mibBuilder.loadTexts:
    h3cRrppDomainTable.setStatus("current")
_H3cRrppDomainEntry_Object = MibTableRow
h3cRrppDomainEntry = _H3cRrppDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 45, 2, 1, 1)
)
h3cRrppDomainEntry.setIndexNames(
    (0, "A3COM-HUAWEI-RRPP-MIB", "h3cRrppDomainID"),
)
if mibBuilder.loadTexts:
    h3cRrppDomainEntry.setStatus("current")


class _H3cRrppDomainID_Type(Integer32):
    """Custom type h3cRrppDomainID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_H3cRrppDomainID_Type.__name__ = "Integer32"
_H3cRrppDomainID_Object = MibTableColumn
h3cRrppDomainID = _H3cRrppDomainID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 45, 2, 1, 1, 1),
    _H3cRrppDomainID_Type()
)
h3cRrppDomainID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cRrppDomainID.setStatus("current")


class _H3cRrppDomainControlVlanID_Type(Integer32):
    """Custom type h3cRrppDomainControlVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4094),
        ValueRangeConstraint(65535, 65535),
    )


_H3cRrppDomainControlVlanID_Type.__name__ = "Integer32"
_H3cRrppDomainControlVlanID_Object = MibTableColumn
h3cRrppDomainControlVlanID = _H3cRrppDomainControlVlanID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 45, 2, 1, 1, 2),
    _H3cRrppDomainControlVlanID_Type()
)
h3cRrppDomainControlVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRrppDomainControlVlanID.setStatus("current")


class _H3cRrppDomainHelloTime_Type(Integer32):
    """Custom type h3cRrppDomainHelloTime based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_H3cRrppDomainHelloTime_Type.__name__ = "Integer32"
_H3cRrppDomainHelloTime_Object = MibTableColumn
h3cRrppDomainHelloTime = _H3cRrppDomainHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 45, 2, 1, 1, 3),
    _H3cRrppDomainHelloTime_Type()
)
h3cRrppDomainHelloTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRrppDomainHelloTime.setStatus("current")


class _H3cRrppDomainFailTime_Type(Integer32):
    """Custom type h3cRrppDomainFailTime based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 30),
    )


_H3cRrppDomainFailTime_Type.__name__ = "Integer32"
_H3cRrppDomainFailTime_Object = MibTableColumn
h3cRrppDomainFailTime = _H3cRrppDomainFailTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 45, 2, 1, 1, 4),
    _H3cRrppDomainFailTime_Type()
)
h3cRrppDomainFailTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRrppDomainFailTime.setStatus("current")
_H3cRrppDomainRowStatus_Type = RowStatus
_H3cRrppDomainRowStatus_Object = MibTableColumn
h3cRrppDomainRowStatus = _H3cRrppDomainRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 45, 2, 1, 1, 5),
    _H3cRrppDomainRowStatus_Type()
)
h3cRrppDomainRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRrppDomainRowStatus.setStatus("current")


class _H3cRrppDomainInstanceListLow_Type(OctetString):
    """Custom type h3cRrppDomainInstanceListLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_H3cRrppDomainInstanceListLow_Type.__name__ = "OctetString"
_H3cRrppDomainInstanceListLow_Object = MibTableColumn
h3cRrppDomainInstanceListLow = _H3cRrppDomainInstanceListLow_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 45, 2, 1, 1, 6),
    _H3cRrppDomainInstanceListLow_Type()
)
h3cRrppDomainInstanceListLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRrppDomainInstanceListLow.setStatus("current")


class _H3cRrppDomainInstanceListHigh_Type(OctetString):
    """Custom type h3cRrppDomainInstanceListHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_H3cRrppDomainInstanceListHigh_Type.__name__ = "OctetString"
_H3cRrppDomainInstanceListHigh_Object = MibTableColumn
h3cRrppDomainInstanceListHigh = _H3cRrppDomainInstanceListHigh_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 45, 2, 1, 1, 7),
    _H3cRrppDomainInstanceListHigh_Type()
)
h3cRrppDomainInstanceListHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRrppDomainInstanceListHigh.setStatus("current")


class _H3cRrppDomainProtectVlanListLow_Type(OctetString):
    """Custom type h3cRrppDomainProtectVlanListLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_H3cRrppDomainProtectVlanListLow_Type.__name__ = "OctetString"
_H3cRrppDomainProtectVlanListLow_Object = MibTableColumn
h3cRrppDomainProtectVlanListLow = _H3cRrppDomainProtectVlanListLow_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 45, 2, 1, 1, 8),
    _H3cRrppDomainProtectVlanListLow_Type()
)
h3cRrppDomainProtectVlanListLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRrppDomainProtectVlanListLow.setStatus("current")


class _H3cRrppDomainProtectVlanListHigh_Type(OctetString):
    """Custom type h3cRrppDomainProtectVlanListHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_H3cRrppDomainProtectVlanListHigh_Type.__name__ = "OctetString"
_H3cRrppDomainProtectVlanListHigh_Object = MibTableColumn
h3cRrppDomainProtectVlanListHigh = _H3cRrppDomainProtectVlanListHigh_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 45, 2, 1, 1, 9),
    _H3cRrppDomainProtectVlanListHigh_Type()
)
h3cRrppDomainProtectVlanListHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRrppDomainProtectVlanListHigh.setStatus("current")
_H3cRrppRingTable_Object = MibTable
h3cRrppRingTable = _H3cRrppRingTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 45, 2, 2)
)
if mibBuilder.loadTexts:
    h3cRrppRingTable.setStatus("current")
_H3cRrppRingEntry_Object = MibTableRow
h3cRrppRingEntry = _H3cRrppRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 45, 2, 2, 1)
)
h3cRrppRingEntry.setIndexNames(
    (0, "A3COM-HUAWEI-RRPP-MIB", "h3cRrppDomainID"),
    (0, "A3COM-HUAWEI-RRPP-MIB", "h3cRrppRingID"),
)
if mibBuilder.loadTexts:
    h3cRrppRingEntry.setStatus("current")


class _H3cRrppRingID_Type(Integer32):
    """Custom type h3cRrppRingID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_H3cRrppRingID_Type.__name__ = "Integer32"
_H3cRrppRingID_Object = MibTableColumn
h3cRrppRingID = _H3cRrppRingID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 45, 2, 2, 1, 1),
    _H3cRrppRingID_Type()
)
h3cRrppRingID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cRrppRingID.setStatus("current")
_H3cRrppRingEnableStatus_Type = EnabledStatus
_H3cRrppRingEnableStatus_Object = MibTableColumn
h3cRrppRingEnableStatus = _H3cRrppRingEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 45, 2, 2, 1, 2),
    _H3cRrppRingEnableStatus_Type()
)
h3cRrppRingEnableStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRrppRingEnableStatus.setStatus("current")


class _H3cRrppRingActive_Type(Integer32):
    """Custom type h3cRrppRingActive based on Integer32"""
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


_H3cRrppRingActive_Type.__name__ = "Integer32"
_H3cRrppRingActive_Object = MibTableColumn
h3cRrppRingActive = _H3cRrppRingActive_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 45, 2, 2, 1, 3),
    _H3cRrppRingActive_Type()
)
h3cRrppRingActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRrppRingActive.setStatus("current")


class _H3cRrppRingState_Type(Integer32):
    """Custom type h3cRrppRingState based on Integer32"""
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


_H3cRrppRingState_Type.__name__ = "Integer32"
_H3cRrppRingState_Object = MibTableColumn
h3cRrppRingState = _H3cRrppRingState_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 45, 2, 2, 1, 4),
    _H3cRrppRingState_Type()
)
h3cRrppRingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRrppRingState.setStatus("current")


class _H3cRrppRingNodeMode_Type(Integer32):
    """Custom type h3cRrppRingNodeMode based on Integer32"""
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


_H3cRrppRingNodeMode_Type.__name__ = "Integer32"
_H3cRrppRingNodeMode_Object = MibTableColumn
h3cRrppRingNodeMode = _H3cRrppRingNodeMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 45, 2, 2, 1, 5),
    _H3cRrppRingNodeMode_Type()
)
h3cRrppRingNodeMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRrppRingNodeMode.setStatus("current")
_H3cRrppRingPrimaryPort_Type = Integer32
_H3cRrppRingPrimaryPort_Object = MibTableColumn
h3cRrppRingPrimaryPort = _H3cRrppRingPrimaryPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 45, 2, 2, 1, 6),
    _H3cRrppRingPrimaryPort_Type()
)
h3cRrppRingPrimaryPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRrppRingPrimaryPort.setStatus("current")
_H3cRrppRingSecondaryPort_Type = Integer32
_H3cRrppRingSecondaryPort_Object = MibTableColumn
h3cRrppRingSecondaryPort = _H3cRrppRingSecondaryPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 45, 2, 2, 1, 7),
    _H3cRrppRingSecondaryPort_Type()
)
h3cRrppRingSecondaryPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRrppRingSecondaryPort.setStatus("current")


class _H3cRrppRingLevel_Type(Integer32):
    """Custom type h3cRrppRingLevel based on Integer32"""
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


_H3cRrppRingLevel_Type.__name__ = "Integer32"
_H3cRrppRingLevel_Object = MibTableColumn
h3cRrppRingLevel = _H3cRrppRingLevel_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 45, 2, 2, 1, 8),
    _H3cRrppRingLevel_Type()
)
h3cRrppRingLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRrppRingLevel.setStatus("current")
_H3cRrppRingRowStatus_Type = RowStatus
_H3cRrppRingRowStatus_Object = MibTableColumn
h3cRrppRingRowStatus = _H3cRrppRingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 45, 2, 2, 1, 9),
    _H3cRrppRingRowStatus_Type()
)
h3cRrppRingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRrppRingRowStatus.setStatus("current")
_H3cRrppPortTable_Object = MibTable
h3cRrppPortTable = _H3cRrppPortTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 45, 2, 3)
)
if mibBuilder.loadTexts:
    h3cRrppPortTable.setStatus("current")
_H3cRrppPortEntry_Object = MibTableRow
h3cRrppPortEntry = _H3cRrppPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 45, 2, 3, 1)
)
h3cRrppPortEntry.setIndexNames(
    (0, "A3COM-HUAWEI-RRPP-MIB", "h3cRrppDomainID"),
    (0, "A3COM-HUAWEI-RRPP-MIB", "h3cRrppRingID"),
    (0, "A3COM-HUAWEI-RRPP-MIB", "h3cRrppPortID"),
)
if mibBuilder.loadTexts:
    h3cRrppPortEntry.setStatus("current")
_H3cRrppPortID_Type = Integer32
_H3cRrppPortID_Object = MibTableColumn
h3cRrppPortID = _H3cRrppPortID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 45, 2, 3, 1, 1),
    _H3cRrppPortID_Type()
)
h3cRrppPortID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRrppPortID.setStatus("current")


class _H3cRrppPortRole_Type(Integer32):
    """Custom type h3cRrppPortRole based on Integer32"""
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


_H3cRrppPortRole_Type.__name__ = "Integer32"
_H3cRrppPortRole_Object = MibTableColumn
h3cRrppPortRole = _H3cRrppPortRole_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 45, 2, 3, 1, 2),
    _H3cRrppPortRole_Type()
)
h3cRrppPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRrppPortRole.setStatus("current")


class _H3cRrppPortState_Type(Integer32):
    """Custom type h3cRrppPortState based on Integer32"""
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


_H3cRrppPortState_Type.__name__ = "Integer32"
_H3cRrppPortState_Object = MibTableColumn
h3cRrppPortState = _H3cRrppPortState_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 45, 2, 3, 1, 3),
    _H3cRrppPortState_Type()
)
h3cRrppPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRrppPortState.setStatus("current")
_H3cRrppPortRXError_Type = Counter32
_H3cRrppPortRXError_Object = MibTableColumn
h3cRrppPortRXError = _H3cRrppPortRXError_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 45, 2, 3, 1, 4),
    _H3cRrppPortRXError_Type()
)
h3cRrppPortRXError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRrppPortRXError.setStatus("current")
_H3cRrppPortRXHello_Type = Counter32
_H3cRrppPortRXHello_Object = MibTableColumn
h3cRrppPortRXHello = _H3cRrppPortRXHello_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 45, 2, 3, 1, 5),
    _H3cRrppPortRXHello_Type()
)
h3cRrppPortRXHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRrppPortRXHello.setStatus("current")
_H3cRrppPortRXLinkUp_Type = Counter32
_H3cRrppPortRXLinkUp_Object = MibTableColumn
h3cRrppPortRXLinkUp = _H3cRrppPortRXLinkUp_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 45, 2, 3, 1, 6),
    _H3cRrppPortRXLinkUp_Type()
)
h3cRrppPortRXLinkUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRrppPortRXLinkUp.setStatus("current")
_H3cRrppPortRXLinkDown_Type = Counter32
_H3cRrppPortRXLinkDown_Object = MibTableColumn
h3cRrppPortRXLinkDown = _H3cRrppPortRXLinkDown_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 45, 2, 3, 1, 7),
    _H3cRrppPortRXLinkDown_Type()
)
h3cRrppPortRXLinkDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRrppPortRXLinkDown.setStatus("current")
_H3cRrppPortRXCommonFlush_Type = Counter32
_H3cRrppPortRXCommonFlush_Object = MibTableColumn
h3cRrppPortRXCommonFlush = _H3cRrppPortRXCommonFlush_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 45, 2, 3, 1, 8),
    _H3cRrppPortRXCommonFlush_Type()
)
h3cRrppPortRXCommonFlush.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRrppPortRXCommonFlush.setStatus("current")
_H3cRrppPortRXCompleteFlush_Type = Counter32
_H3cRrppPortRXCompleteFlush_Object = MibTableColumn
h3cRrppPortRXCompleteFlush = _H3cRrppPortRXCompleteFlush_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 45, 2, 3, 1, 9),
    _H3cRrppPortRXCompleteFlush_Type()
)
h3cRrppPortRXCompleteFlush.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRrppPortRXCompleteFlush.setStatus("current")
_H3cRrppPortTXHello_Type = Counter32
_H3cRrppPortTXHello_Object = MibTableColumn
h3cRrppPortTXHello = _H3cRrppPortTXHello_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 45, 2, 3, 1, 10),
    _H3cRrppPortTXHello_Type()
)
h3cRrppPortTXHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRrppPortTXHello.setStatus("current")
_H3cRrppPortTXLinkUp_Type = Counter32
_H3cRrppPortTXLinkUp_Object = MibTableColumn
h3cRrppPortTXLinkUp = _H3cRrppPortTXLinkUp_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 45, 2, 3, 1, 11),
    _H3cRrppPortTXLinkUp_Type()
)
h3cRrppPortTXLinkUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRrppPortTXLinkUp.setStatus("current")
_H3cRrppPortTXLinkDown_Type = Counter32
_H3cRrppPortTXLinkDown_Object = MibTableColumn
h3cRrppPortTXLinkDown = _H3cRrppPortTXLinkDown_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 45, 2, 3, 1, 12),
    _H3cRrppPortTXLinkDown_Type()
)
h3cRrppPortTXLinkDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRrppPortTXLinkDown.setStatus("current")
_H3cRrppPortTXCommonFlush_Type = Counter32
_H3cRrppPortTXCommonFlush_Object = MibTableColumn
h3cRrppPortTXCommonFlush = _H3cRrppPortTXCommonFlush_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 45, 2, 3, 1, 13),
    _H3cRrppPortTXCommonFlush_Type()
)
h3cRrppPortTXCommonFlush.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRrppPortTXCommonFlush.setStatus("current")
_H3cRrppPortTXCompleteFlush_Type = Counter32
_H3cRrppPortTXCompleteFlush_Object = MibTableColumn
h3cRrppPortTXCompleteFlush = _H3cRrppPortTXCompleteFlush_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 45, 2, 3, 1, 14),
    _H3cRrppPortTXCompleteFlush_Type()
)
h3cRrppPortTXCompleteFlush.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRrppPortTXCompleteFlush.setStatus("current")
_H3cRrppPortRXEdgeHello_Type = Counter32
_H3cRrppPortRXEdgeHello_Object = MibTableColumn
h3cRrppPortRXEdgeHello = _H3cRrppPortRXEdgeHello_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 45, 2, 3, 1, 15),
    _H3cRrppPortRXEdgeHello_Type()
)
h3cRrppPortRXEdgeHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRrppPortRXEdgeHello.setStatus("current")
_H3cRrppPortRXMajorFault_Type = Counter32
_H3cRrppPortRXMajorFault_Object = MibTableColumn
h3cRrppPortRXMajorFault = _H3cRrppPortRXMajorFault_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 45, 2, 3, 1, 16),
    _H3cRrppPortRXMajorFault_Type()
)
h3cRrppPortRXMajorFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRrppPortRXMajorFault.setStatus("current")
_H3cRrppPortTXEdgeHello_Type = Counter32
_H3cRrppPortTXEdgeHello_Object = MibTableColumn
h3cRrppPortTXEdgeHello = _H3cRrppPortTXEdgeHello_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 45, 2, 3, 1, 17),
    _H3cRrppPortTXEdgeHello_Type()
)
h3cRrppPortTXEdgeHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRrppPortTXEdgeHello.setStatus("current")
_H3cRrppPortTXMajorFault_Type = Counter32
_H3cRrppPortTXMajorFault_Object = MibTableColumn
h3cRrppPortTXMajorFault = _H3cRrppPortTXMajorFault_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 45, 2, 3, 1, 18),
    _H3cRrppPortTXMajorFault_Type()
)
h3cRrppPortTXMajorFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRrppPortTXMajorFault.setStatus("current")
_H3cRrppNotifications_ObjectIdentity = ObjectIdentity
h3cRrppNotifications = _H3cRrppNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 45, 3)
)

# Managed Objects groups


# Notification objects

h3cRrppRingRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 45, 3, 1)
)
h3cRrppRingRecover.setObjects(
      *(("A3COM-HUAWEI-RRPP-MIB", "h3cRrppDomainID"),
        ("A3COM-HUAWEI-RRPP-MIB", "h3cRrppRingID"))
)
if mibBuilder.loadTexts:
    h3cRrppRingRecover.setStatus(
        "current"
    )

h3cRrppRingFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 45, 3, 2)
)
h3cRrppRingFail.setObjects(
      *(("A3COM-HUAWEI-RRPP-MIB", "h3cRrppDomainID"),
        ("A3COM-HUAWEI-RRPP-MIB", "h3cRrppRingID"))
)
if mibBuilder.loadTexts:
    h3cRrppRingFail.setStatus(
        "current"
    )

h3cRrppMultiMaster = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 45, 3, 3)
)
h3cRrppMultiMaster.setObjects(
      *(("A3COM-HUAWEI-RRPP-MIB", "h3cRrppDomainID"),
        ("A3COM-HUAWEI-RRPP-MIB", "h3cRrppRingID"))
)
if mibBuilder.loadTexts:
    h3cRrppMultiMaster.setStatus(
        "current"
    )

h3cRrppMajorFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 45, 3, 4)
)
h3cRrppMajorFault.setObjects(
      *(("A3COM-HUAWEI-RRPP-MIB", "h3cRrppDomainID"),
        ("A3COM-HUAWEI-RRPP-MIB", "h3cRrppRingID"))
)
if mibBuilder.loadTexts:
    h3cRrppMajorFault.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-RRPP-MIB",
    **{"EnabledStatus": EnabledStatus,
       "h3cRrpp": h3cRrpp,
       "h3cRrppScalarGroup": h3cRrppScalarGroup,
       "h3cRrppEnableStatus": h3cRrppEnableStatus,
       "h3cRrppPassword": h3cRrppPassword,
       "h3cRrppPasswordType": h3cRrppPasswordType,
       "h3cRrppProtectVlanConfigMode": h3cRrppProtectVlanConfigMode,
       "h3cRrppTable": h3cRrppTable,
       "h3cRrppDomainTable": h3cRrppDomainTable,
       "h3cRrppDomainEntry": h3cRrppDomainEntry,
       "h3cRrppDomainID": h3cRrppDomainID,
       "h3cRrppDomainControlVlanID": h3cRrppDomainControlVlanID,
       "h3cRrppDomainHelloTime": h3cRrppDomainHelloTime,
       "h3cRrppDomainFailTime": h3cRrppDomainFailTime,
       "h3cRrppDomainRowStatus": h3cRrppDomainRowStatus,
       "h3cRrppDomainInstanceListLow": h3cRrppDomainInstanceListLow,
       "h3cRrppDomainInstanceListHigh": h3cRrppDomainInstanceListHigh,
       "h3cRrppDomainProtectVlanListLow": h3cRrppDomainProtectVlanListLow,
       "h3cRrppDomainProtectVlanListHigh": h3cRrppDomainProtectVlanListHigh,
       "h3cRrppRingTable": h3cRrppRingTable,
       "h3cRrppRingEntry": h3cRrppRingEntry,
       "h3cRrppRingID": h3cRrppRingID,
       "h3cRrppRingEnableStatus": h3cRrppRingEnableStatus,
       "h3cRrppRingActive": h3cRrppRingActive,
       "h3cRrppRingState": h3cRrppRingState,
       "h3cRrppRingNodeMode": h3cRrppRingNodeMode,
       "h3cRrppRingPrimaryPort": h3cRrppRingPrimaryPort,
       "h3cRrppRingSecondaryPort": h3cRrppRingSecondaryPort,
       "h3cRrppRingLevel": h3cRrppRingLevel,
       "h3cRrppRingRowStatus": h3cRrppRingRowStatus,
       "h3cRrppPortTable": h3cRrppPortTable,
       "h3cRrppPortEntry": h3cRrppPortEntry,
       "h3cRrppPortID": h3cRrppPortID,
       "h3cRrppPortRole": h3cRrppPortRole,
       "h3cRrppPortState": h3cRrppPortState,
       "h3cRrppPortRXError": h3cRrppPortRXError,
       "h3cRrppPortRXHello": h3cRrppPortRXHello,
       "h3cRrppPortRXLinkUp": h3cRrppPortRXLinkUp,
       "h3cRrppPortRXLinkDown": h3cRrppPortRXLinkDown,
       "h3cRrppPortRXCommonFlush": h3cRrppPortRXCommonFlush,
       "h3cRrppPortRXCompleteFlush": h3cRrppPortRXCompleteFlush,
       "h3cRrppPortTXHello": h3cRrppPortTXHello,
       "h3cRrppPortTXLinkUp": h3cRrppPortTXLinkUp,
       "h3cRrppPortTXLinkDown": h3cRrppPortTXLinkDown,
       "h3cRrppPortTXCommonFlush": h3cRrppPortTXCommonFlush,
       "h3cRrppPortTXCompleteFlush": h3cRrppPortTXCompleteFlush,
       "h3cRrppPortRXEdgeHello": h3cRrppPortRXEdgeHello,
       "h3cRrppPortRXMajorFault": h3cRrppPortRXMajorFault,
       "h3cRrppPortTXEdgeHello": h3cRrppPortTXEdgeHello,
       "h3cRrppPortTXMajorFault": h3cRrppPortTXMajorFault,
       "h3cRrppNotifications": h3cRrppNotifications,
       "h3cRrppRingRecover": h3cRrppRingRecover,
       "h3cRrppRingFail": h3cRrppRingFail,
       "h3cRrppMultiMaster": h3cRrppMultiMaster,
       "h3cRrppMajorFault": h3cRrppMajorFault}
)
