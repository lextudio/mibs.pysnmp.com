# SNMP MIB module (HMRING-MGMT-SNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HMRING-MGMT-SNMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:56:42 2024
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

(hmConfiguration,) = mibBuilder.importSymbols(
    "HMPRIV-MGMT-SNMP-MIB",
    "hmConfiguration")

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

hmRingRedundancy = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 5)
)
hmRingRedundancy.setRevisions(
        ("2008-11-18 12:00",
         "2007-09-13 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HmRingRedundancyEvent_ObjectIdentity = ObjectIdentity
hmRingRedundancyEvent = _HmRingRedundancyEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 0)
)
if mibBuilder.loadTexts:
    hmRingRedundancyEvent.setStatus("current")
_HmRingRedTable_Object = MibTable
hmRingRedTable = _HmRingRedTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 1)
)
if mibBuilder.loadTexts:
    hmRingRedTable.setStatus("current")
_HmRingRedEntry_Object = MibTableRow
hmRingRedEntry = _HmRingRedEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 1, 1)
)
hmRingRedEntry.setIndexNames(
    (0, "HMRING-MGMT-SNMP-MIB", "hmRingRedPrimGroupID"),
    (0, "HMRING-MGMT-SNMP-MIB", "hmRingRedPrimIfIndex"),
)
if mibBuilder.loadTexts:
    hmRingRedEntry.setStatus("current")


class _HmRingRedPrimGroupID_Type(Integer32):
    """Custom type hmRingRedPrimGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_HmRingRedPrimGroupID_Type.__name__ = "Integer32"
_HmRingRedPrimGroupID_Object = MibTableColumn
hmRingRedPrimGroupID = _HmRingRedPrimGroupID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 1, 1, 1),
    _HmRingRedPrimGroupID_Type()
)
hmRingRedPrimGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmRingRedPrimGroupID.setStatus("current")


class _HmRingRedPrimIfIndex_Type(Integer32):
    """Custom type hmRingRedPrimIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_HmRingRedPrimIfIndex_Type.__name__ = "Integer32"
_HmRingRedPrimIfIndex_Object = MibTableColumn
hmRingRedPrimIfIndex = _HmRingRedPrimIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 1, 1, 2),
    _HmRingRedPrimIfIndex_Type()
)
hmRingRedPrimIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmRingRedPrimIfIndex.setStatus("current")


class _HmRingRedPrimIfOpState_Type(Integer32):
    """Custom type hmRingRedPrimIfOpState based on Integer32"""
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


_HmRingRedPrimIfOpState_Type.__name__ = "Integer32"
_HmRingRedPrimIfOpState_Object = MibTableColumn
hmRingRedPrimIfOpState = _HmRingRedPrimIfOpState_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 1, 1, 3),
    _HmRingRedPrimIfOpState_Type()
)
hmRingRedPrimIfOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmRingRedPrimIfOpState.setStatus("current")
_HmRingRedRedGroupID_Type = Integer32
_HmRingRedRedGroupID_Object = MibTableColumn
hmRingRedRedGroupID = _HmRingRedRedGroupID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 1, 1, 4),
    _HmRingRedRedGroupID_Type()
)
hmRingRedRedGroupID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRingRedRedGroupID.setStatus("current")
_HmRingRedRedIfIndex_Type = Integer32
_HmRingRedRedIfIndex_Object = MibTableColumn
hmRingRedRedIfIndex = _HmRingRedRedIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 1, 1, 5),
    _HmRingRedRedIfIndex_Type()
)
hmRingRedRedIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRingRedRedIfIndex.setStatus("current")


class _HmRingRedRedIfOpState_Type(Integer32):
    """Custom type hmRingRedRedIfOpState based on Integer32"""
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


_HmRingRedRedIfOpState_Type.__name__ = "Integer32"
_HmRingRedRedIfOpState_Object = MibTableColumn
hmRingRedRedIfOpState = _HmRingRedRedIfOpState_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 1, 1, 6),
    _HmRingRedRedIfOpState_Type()
)
hmRingRedRedIfOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmRingRedRedIfOpState.setStatus("current")


class _HmRingRedOperState_Type(Integer32):
    """Custom type hmRingRedOperState based on Integer32"""
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
        *(("disable", 5),
          ("rmActive", 2),
          ("rmInactive", 3),
          ("rs", 4),
          ("underCreation", 1))
    )


_HmRingRedOperState_Type.__name__ = "Integer32"
_HmRingRedOperState_Object = MibTableColumn
hmRingRedOperState = _HmRingRedOperState_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 1, 1, 7),
    _HmRingRedOperState_Type()
)
hmRingRedOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmRingRedOperState.setStatus("current")


class _HmRingRedMode_Type(Integer32):
    """Custom type hmRingRedMode based on Integer32"""
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
        *(("create", 1),
          ("delete", 2),
          ("disable", 5),
          ("rm", 3),
          ("rs", 4))
    )


_HmRingRedMode_Type.__name__ = "Integer32"
_HmRingRedMode_Object = MibTableColumn
hmRingRedMode = _HmRingRedMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 1, 1, 8),
    _HmRingRedMode_Type()
)
hmRingRedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRingRedMode.setStatus("current")


class _HmRingRedConfigOperState_Type(Integer32):
    """Custom type hmRingRedConfigOperState based on Integer32"""
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
        *(("anotherRM", 4),
          ("noError", 1),
          ("ringConfigError", 3),
          ("rmConfigError", 2))
    )


_HmRingRedConfigOperState_Type.__name__ = "Integer32"
_HmRingRedConfigOperState_Object = MibTableColumn
hmRingRedConfigOperState = _HmRingRedConfigOperState_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 1, 1, 9),
    _HmRingRedConfigOperState_Type()
)
hmRingRedConfigOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmRingRedConfigOperState.setStatus("current")


class _HmRingRedRecoveryDelay_Type(Integer32):
    """Custom type hmRingRedRecoveryDelay based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delay300", 2),
          ("delay500", 1))
    )


_HmRingRedRecoveryDelay_Type.__name__ = "Integer32"
_HmRingRedRecoveryDelay_Object = MibTableColumn
hmRingRedRecoveryDelay = _HmRingRedRecoveryDelay_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 1, 1, 10),
    _HmRingRedRecoveryDelay_Type()
)
hmRingRedRecoveryDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRingRedRecoveryDelay.setStatus("current")
_HmRingCouplingTable_Object = MibTable
hmRingCouplingTable = _HmRingCouplingTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 2)
)
if mibBuilder.loadTexts:
    hmRingCouplingTable.setStatus("current")
_HmRingCouplingEntry_Object = MibTableRow
hmRingCouplingEntry = _HmRingCouplingEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 2, 1)
)
hmRingCouplingEntry.setIndexNames(
    (0, "HMRING-MGMT-SNMP-MIB", "hmRingCplInterconnGroupID"),
    (0, "HMRING-MGMT-SNMP-MIB", "hmRingCplInterconnIfIndex"),
)
if mibBuilder.loadTexts:
    hmRingCouplingEntry.setStatus("current")
_HmRingCplInterconnGroupID_Type = Integer32
_HmRingCplInterconnGroupID_Object = MibTableColumn
hmRingCplInterconnGroupID = _HmRingCplInterconnGroupID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 2, 1, 1),
    _HmRingCplInterconnGroupID_Type()
)
hmRingCplInterconnGroupID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRingCplInterconnGroupID.setStatus("current")
_HmRingCplInterconnIfIndex_Type = Integer32
_HmRingCplInterconnIfIndex_Object = MibTableColumn
hmRingCplInterconnIfIndex = _HmRingCplInterconnIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 2, 1, 2),
    _HmRingCplInterconnIfIndex_Type()
)
hmRingCplInterconnIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRingCplInterconnIfIndex.setStatus("current")


class _HmRingCplInterconnIfOpState_Type(Integer32):
    """Custom type hmRingCplInterconnIfOpState based on Integer32"""
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
          ("not-connected", 1),
          ("standby", 3))
    )


_HmRingCplInterconnIfOpState_Type.__name__ = "Integer32"
_HmRingCplInterconnIfOpState_Object = MibTableColumn
hmRingCplInterconnIfOpState = _HmRingCplInterconnIfOpState_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 2, 1, 3),
    _HmRingCplInterconnIfOpState_Type()
)
hmRingCplInterconnIfOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmRingCplInterconnIfOpState.setStatus("current")
_HmRingCplControlGroupID_Type = Integer32
_HmRingCplControlGroupID_Object = MibTableColumn
hmRingCplControlGroupID = _HmRingCplControlGroupID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 2, 1, 4),
    _HmRingCplControlGroupID_Type()
)
hmRingCplControlGroupID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRingCplControlGroupID.setStatus("current")
_HmRingCplControlIfIndex_Type = Integer32
_HmRingCplControlIfIndex_Object = MibTableColumn
hmRingCplControlIfIndex = _HmRingCplControlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 2, 1, 5),
    _HmRingCplControlIfIndex_Type()
)
hmRingCplControlIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRingCplControlIfIndex.setStatus("current")


class _HmRingCplControlIfOpState_Type(Integer32):
    """Custom type hmRingCplControlIfOpState based on Integer32"""
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
          ("not-connected", 1),
          ("standby", 3))
    )


_HmRingCplControlIfOpState_Type.__name__ = "Integer32"
_HmRingCplControlIfOpState_Object = MibTableColumn
hmRingCplControlIfOpState = _HmRingCplControlIfOpState_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 2, 1, 6),
    _HmRingCplControlIfOpState_Type()
)
hmRingCplControlIfOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmRingCplControlIfOpState.setStatus("current")


class _HmRingCplControlMode_Type(Integer32):
    """Custom type hmRingCplControlMode based on Integer32"""
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
        *(("disable", 5),
          ("inband", 2),
          ("local", 4),
          ("outband", 1),
          ("unknown", 3))
    )


_HmRingCplControlMode_Type.__name__ = "Integer32"
_HmRingCplControlMode_Object = MibTableColumn
hmRingCplControlMode = _HmRingCplControlMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 2, 1, 7),
    _HmRingCplControlMode_Type()
)
hmRingCplControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRingCplControlMode.setStatus("current")
_HmRingCplPartnerIpAddr_Type = IpAddress
_HmRingCplPartnerIpAddr_Object = MibTableColumn
hmRingCplPartnerIpAddr = _HmRingCplPartnerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 2, 1, 8),
    _HmRingCplPartnerIpAddr_Type()
)
hmRingCplPartnerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmRingCplPartnerIpAddr.setStatus("current")
_HmRingCplPartnerInterconnGroupID_Type = Integer32
_HmRingCplPartnerInterconnGroupID_Object = MibTableColumn
hmRingCplPartnerInterconnGroupID = _HmRingCplPartnerInterconnGroupID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 2, 1, 9),
    _HmRingCplPartnerInterconnGroupID_Type()
)
hmRingCplPartnerInterconnGroupID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRingCplPartnerInterconnGroupID.setStatus("current")
_HmRingCplPartnerInterconnIfIndex_Type = Integer32
_HmRingCplPartnerInterconnIfIndex_Object = MibTableColumn
hmRingCplPartnerInterconnIfIndex = _HmRingCplPartnerInterconnIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 2, 1, 10),
    _HmRingCplPartnerInterconnIfIndex_Type()
)
hmRingCplPartnerInterconnIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRingCplPartnerInterconnIfIndex.setStatus("current")


class _HmRingCplPartnerInterconnIfOpState_Type(Integer32):
    """Custom type hmRingCplPartnerInterconnIfOpState based on Integer32"""
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
          ("not-connected", 1),
          ("standby", 3))
    )


_HmRingCplPartnerInterconnIfOpState_Type.__name__ = "Integer32"
_HmRingCplPartnerInterconnIfOpState_Object = MibTableColumn
hmRingCplPartnerInterconnIfOpState = _HmRingCplPartnerInterconnIfOpState_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 2, 1, 11),
    _HmRingCplPartnerInterconnIfOpState_Type()
)
hmRingCplPartnerInterconnIfOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmRingCplPartnerInterconnIfOpState.setStatus("current")


class _HmRingCplOperState_Type(Integer32):
    """Custom type hmRingCplOperState based on Integer32"""
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
        *(("disable", 5),
          ("local", 4),
          ("master", 3),
          ("slave", 2),
          ("underCreation", 1))
    )


_HmRingCplOperState_Type.__name__ = "Integer32"
_HmRingCplOperState_Object = MibTableColumn
hmRingCplOperState = _HmRingCplOperState_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 2, 1, 12),
    _HmRingCplOperState_Type()
)
hmRingCplOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmRingCplOperState.setStatus("current")


class _HmRingCplMode_Type(Integer32):
    """Custom type hmRingCplMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("slaveOff", 1),
          ("slaveOn", 2))
    )


_HmRingCplMode_Type.__name__ = "Integer32"
_HmRingCplMode_Object = MibTableColumn
hmRingCplMode = _HmRingCplMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 2, 1, 13),
    _HmRingCplMode_Type()
)
hmRingCplMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRingCplMode.setStatus("current")
_HmRingCplRowStatus_Type = RowStatus
_HmRingCplRowStatus_Object = MibTableColumn
hmRingCplRowStatus = _HmRingCplRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 2, 1, 14),
    _HmRingCplRowStatus_Type()
)
hmRingCplRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmRingCplRowStatus.setStatus("current")


class _HmRingCplConfigOperState_Type(Integer32):
    """Custom type hmRingCplConfigOperState based on Integer32"""
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


_HmRingCplConfigOperState_Type.__name__ = "Integer32"
_HmRingCplConfigOperState_Object = MibTableColumn
hmRingCplConfigOperState = _HmRingCplConfigOperState_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 2, 1, 15),
    _HmRingCplConfigOperState_Type()
)
hmRingCplConfigOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmRingCplConfigOperState.setStatus("current")


class _HmRingCplCouplingLinks_Type(Integer32):
    """Custom type hmRingCplCouplingLinks based on Integer32"""
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


_HmRingCplCouplingLinks_Type.__name__ = "Integer32"
_HmRingCplCouplingLinks_Object = MibTableColumn
hmRingCplCouplingLinks = _HmRingCplCouplingLinks_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 2, 1, 16),
    _HmRingCplCouplingLinks_Type()
)
hmRingCplCouplingLinks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRingCplCouplingLinks.setStatus("current")


class _HmRingCplExtendedDiag_Type(Integer32):
    """Custom type hmRingCplExtendedDiag based on Integer32"""
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


_HmRingCplExtendedDiag_Type.__name__ = "Integer32"
_HmRingCplExtendedDiag_Object = MibTableColumn
hmRingCplExtendedDiag = _HmRingCplExtendedDiag_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 2, 1, 17),
    _HmRingCplExtendedDiag_Type()
)
hmRingCplExtendedDiag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmRingCplExtendedDiag.setStatus("current")


class _HmRingCplNetCoupling_Type(Integer32):
    """Custom type hmRingCplNetCoupling based on Integer32"""
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


_HmRingCplNetCoupling_Type.__name__ = "Integer32"
_HmRingCplNetCoupling_Object = MibTableColumn
hmRingCplNetCoupling = _HmRingCplNetCoupling_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 2, 1, 18),
    _HmRingCplNetCoupling_Type()
)
hmRingCplNetCoupling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRingCplNetCoupling.setStatus("current")


class _HmRingCplConfigSource_Type(Integer32):
    """Custom type hmRingCplConfigSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dipSwitch", 1),
          ("management", 2))
    )


_HmRingCplConfigSource_Type.__name__ = "Integer32"
_HmRingCplConfigSource_Object = MibTableColumn
hmRingCplConfigSource = _HmRingCplConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 2, 1, 19),
    _HmRingCplConfigSource_Type()
)
hmRingCplConfigSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmRingCplConfigSource.setStatus("current")
_HmMrpTable_Object = MibTable
hmMrpTable = _HmMrpTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 3)
)
if mibBuilder.loadTexts:
    hmMrpTable.setStatus("current")
_HmMrpEntry_Object = MibTableRow
hmMrpEntry = _HmMrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 3, 1)
)
hmMrpEntry.setIndexNames(
    (1, "HMRING-MGMT-SNMP-MIB", "hmMrpDomainID"),
)
if mibBuilder.loadTexts:
    hmMrpEntry.setStatus("current")


class _HmMrpDomainID_Type(OctetString):
    """Custom type hmMrpDomainID based on OctetString"""
    defaultHexValue = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_HmMrpDomainID_Type.__name__ = "OctetString"
_HmMrpDomainID_Object = MibTableColumn
hmMrpDomainID = _HmMrpDomainID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 3, 1, 1),
    _HmMrpDomainID_Type()
)
hmMrpDomainID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmMrpDomainID.setStatus("current")
_HmMrpRingport1GroupID_Type = Integer32
_HmMrpRingport1GroupID_Object = MibTableColumn
hmMrpRingport1GroupID = _HmMrpRingport1GroupID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 3, 1, 2),
    _HmMrpRingport1GroupID_Type()
)
hmMrpRingport1GroupID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmMrpRingport1GroupID.setStatus("current")
_HmMrpRingport1IfIndex_Type = Integer32
_HmMrpRingport1IfIndex_Object = MibTableColumn
hmMrpRingport1IfIndex = _HmMrpRingport1IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 3, 1, 3),
    _HmMrpRingport1IfIndex_Type()
)
hmMrpRingport1IfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmMrpRingport1IfIndex.setStatus("current")


class _HmMrpRingport1OperState_Type(Integer32):
    """Custom type hmMrpRingport1OperState based on Integer32"""
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


_HmMrpRingport1OperState_Type.__name__ = "Integer32"
_HmMrpRingport1OperState_Object = MibTableColumn
hmMrpRingport1OperState = _HmMrpRingport1OperState_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 3, 1, 4),
    _HmMrpRingport1OperState_Type()
)
hmMrpRingport1OperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmMrpRingport1OperState.setStatus("current")
_HmMrpRingport2GroupID_Type = Integer32
_HmMrpRingport2GroupID_Object = MibTableColumn
hmMrpRingport2GroupID = _HmMrpRingport2GroupID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 3, 1, 5),
    _HmMrpRingport2GroupID_Type()
)
hmMrpRingport2GroupID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmMrpRingport2GroupID.setStatus("current")
_HmMrpRingport2IfIndex_Type = Integer32
_HmMrpRingport2IfIndex_Object = MibTableColumn
hmMrpRingport2IfIndex = _HmMrpRingport2IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 3, 1, 6),
    _HmMrpRingport2IfIndex_Type()
)
hmMrpRingport2IfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmMrpRingport2IfIndex.setStatus("current")


class _HmMrpRingport2OperState_Type(Integer32):
    """Custom type hmMrpRingport2OperState based on Integer32"""
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


_HmMrpRingport2OperState_Type.__name__ = "Integer32"
_HmMrpRingport2OperState_Object = MibTableColumn
hmMrpRingport2OperState = _HmMrpRingport2OperState_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 3, 1, 7),
    _HmMrpRingport2OperState_Type()
)
hmMrpRingport2OperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmMrpRingport2OperState.setStatus("current")
_HmMrpVlanID_Type = Integer32
_HmMrpVlanID_Object = MibTableColumn
hmMrpVlanID = _HmMrpVlanID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 3, 1, 8),
    _HmMrpVlanID_Type()
)
hmMrpVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmMrpVlanID.setStatus("current")


class _HmMrpExpectedRole_Type(Integer32):
    """Custom type hmMrpExpectedRole based on Integer32"""
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


_HmMrpExpectedRole_Type.__name__ = "Integer32"
_HmMrpExpectedRole_Object = MibTableColumn
hmMrpExpectedRole = _HmMrpExpectedRole_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 3, 1, 9),
    _HmMrpExpectedRole_Type()
)
hmMrpExpectedRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmMrpExpectedRole.setStatus("current")
_HmMrpMRCLinkDownInterval_Type = Integer32
_HmMrpMRCLinkDownInterval_Object = MibTableColumn
hmMrpMRCLinkDownInterval = _HmMrpMRCLinkDownInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 3, 1, 10),
    _HmMrpMRCLinkDownInterval_Type()
)
hmMrpMRCLinkDownInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmMrpMRCLinkDownInterval.setStatus("current")
_HmMrpMRCLinkUpInterval_Type = Integer32
_HmMrpMRCLinkUpInterval_Object = MibTableColumn
hmMrpMRCLinkUpInterval = _HmMrpMRCLinkUpInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 3, 1, 11),
    _HmMrpMRCLinkUpInterval_Type()
)
hmMrpMRCLinkUpInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmMrpMRCLinkUpInterval.setStatus("current")
_HmMrpMRCLinkChangeCount_Type = Integer32
_HmMrpMRCLinkChangeCount_Object = MibTableColumn
hmMrpMRCLinkChangeCount = _HmMrpMRCLinkChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 3, 1, 12),
    _HmMrpMRCLinkChangeCount_Type()
)
hmMrpMRCLinkChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmMrpMRCLinkChangeCount.setStatus("current")


class _HmMrpMRCBlockedSupported_Type(Integer32):
    """Custom type hmMrpMRCBlockedSupported based on Integer32"""
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


_HmMrpMRCBlockedSupported_Type.__name__ = "Integer32"
_HmMrpMRCBlockedSupported_Object = MibTableColumn
hmMrpMRCBlockedSupported = _HmMrpMRCBlockedSupported_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 3, 1, 13),
    _HmMrpMRCBlockedSupported_Type()
)
hmMrpMRCBlockedSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmMrpMRCBlockedSupported.setStatus("current")


class _HmMrpMRMPriority_Type(Integer32):
    """Custom type hmMrpMRMPriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HmMrpMRMPriority_Type.__name__ = "Integer32"
_HmMrpMRMPriority_Object = MibTableColumn
hmMrpMRMPriority = _HmMrpMRMPriority_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 3, 1, 14),
    _HmMrpMRMPriority_Type()
)
hmMrpMRMPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmMrpMRMPriority.setStatus("current")
_HmMrpMRMTopologyChangeInterval_Type = Integer32
_HmMrpMRMTopologyChangeInterval_Object = MibTableColumn
hmMrpMRMTopologyChangeInterval = _HmMrpMRMTopologyChangeInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 3, 1, 15),
    _HmMrpMRMTopologyChangeInterval_Type()
)
hmMrpMRMTopologyChangeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmMrpMRMTopologyChangeInterval.setStatus("current")
_HmMrpMRMTopologyChangeRepeatCount_Type = Integer32
_HmMrpMRMTopologyChangeRepeatCount_Object = MibTableColumn
hmMrpMRMTopologyChangeRepeatCount = _HmMrpMRMTopologyChangeRepeatCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 3, 1, 16),
    _HmMrpMRMTopologyChangeRepeatCount_Type()
)
hmMrpMRMTopologyChangeRepeatCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmMrpMRMTopologyChangeRepeatCount.setStatus("current")
_HmMrpMRMShortTestInterval_Type = Integer32
_HmMrpMRMShortTestInterval_Object = MibTableColumn
hmMrpMRMShortTestInterval = _HmMrpMRMShortTestInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 3, 1, 17),
    _HmMrpMRMShortTestInterval_Type()
)
hmMrpMRMShortTestInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmMrpMRMShortTestInterval.setStatus("current")
_HmMrpMRMDefaultTestInterval_Type = Integer32
_HmMrpMRMDefaultTestInterval_Object = MibTableColumn
hmMrpMRMDefaultTestInterval = _HmMrpMRMDefaultTestInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 3, 1, 18),
    _HmMrpMRMDefaultTestInterval_Type()
)
hmMrpMRMDefaultTestInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmMrpMRMDefaultTestInterval.setStatus("current")
_HmMrpMRMTestMonitoringCount_Type = Integer32
_HmMrpMRMTestMonitoringCount_Object = MibTableColumn
hmMrpMRMTestMonitoringCount = _HmMrpMRMTestMonitoringCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 3, 1, 19),
    _HmMrpMRMTestMonitoringCount_Type()
)
hmMrpMRMTestMonitoringCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmMrpMRMTestMonitoringCount.setStatus("current")


class _HmMrpMRMNonBlockingMRCSupported_Type(Integer32):
    """Custom type hmMrpMRMNonBlockingMRCSupported based on Integer32"""
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


_HmMrpMRMNonBlockingMRCSupported_Type.__name__ = "Integer32"
_HmMrpMRMNonBlockingMRCSupported_Object = MibTableColumn
hmMrpMRMNonBlockingMRCSupported = _HmMrpMRMNonBlockingMRCSupported_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 3, 1, 20),
    _HmMrpMRMNonBlockingMRCSupported_Type()
)
hmMrpMRMNonBlockingMRCSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmMrpMRMNonBlockingMRCSupported.setStatus("current")
_HmMrpMRMTestMonitoringExtendedCount_Type = Integer32
_HmMrpMRMTestMonitoringExtendedCount_Object = MibTableColumn
hmMrpMRMTestMonitoringExtendedCount = _HmMrpMRMTestMonitoringExtendedCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 3, 1, 21),
    _HmMrpMRMTestMonitoringExtendedCount_Type()
)
hmMrpMRMTestMonitoringExtendedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmMrpMRMTestMonitoringExtendedCount.setStatus("current")


class _HmMrpMRMReactOnLinkChange_Type(Integer32):
    """Custom type hmMrpMRMReactOnLinkChange based on Integer32"""
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


_HmMrpMRMReactOnLinkChange_Type.__name__ = "Integer32"
_HmMrpMRMReactOnLinkChange_Object = MibTableColumn
hmMrpMRMReactOnLinkChange = _HmMrpMRMReactOnLinkChange_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 3, 1, 22),
    _HmMrpMRMReactOnLinkChange_Type()
)
hmMrpMRMReactOnLinkChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmMrpMRMReactOnLinkChange.setStatus("current")


class _HmMrpMRMCheckMediaRedundancy_Type(Integer32):
    """Custom type hmMrpMRMCheckMediaRedundancy based on Integer32"""
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


_HmMrpMRMCheckMediaRedundancy_Type.__name__ = "Integer32"
_HmMrpMRMCheckMediaRedundancy_Object = MibTableColumn
hmMrpMRMCheckMediaRedundancy = _HmMrpMRMCheckMediaRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 3, 1, 23),
    _HmMrpMRMCheckMediaRedundancy_Type()
)
hmMrpMRMCheckMediaRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmMrpMRMCheckMediaRedundancy.setStatus("current")


class _HmMrpMRMRealRoleState_Type(Integer32):
    """Custom type hmMrpMRMRealRoleState based on Integer32"""
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


_HmMrpMRMRealRoleState_Type.__name__ = "Integer32"
_HmMrpMRMRealRoleState_Object = MibTableColumn
hmMrpMRMRealRoleState = _HmMrpMRMRealRoleState_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 3, 1, 24),
    _HmMrpMRMRealRoleState_Type()
)
hmMrpMRMRealRoleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmMrpMRMRealRoleState.setStatus("current")


class _HmMrpMRMRealRingState_Type(Integer32):
    """Custom type hmMrpMRMRealRingState based on Integer32"""
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


_HmMrpMRMRealRingState_Type.__name__ = "Integer32"
_HmMrpMRMRealRingState_Object = MibTableColumn
hmMrpMRMRealRingState = _HmMrpMRMRealRingState_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 3, 1, 25),
    _HmMrpMRMRealRingState_Type()
)
hmMrpMRMRealRingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmMrpMRMRealRingState.setStatus("current")
_HmMrpRowStatus_Type = RowStatus
_HmMrpRowStatus_Object = MibTableColumn
hmMrpRowStatus = _HmMrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 3, 1, 26),
    _HmMrpRowStatus_Type()
)
hmMrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmMrpRowStatus.setStatus("current")


class _HmMrpRedOperState_Type(Integer32):
    """Custom type hmMrpRedOperState based on Integer32"""
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


_HmMrpRedOperState_Type.__name__ = "Integer32"
_HmMrpRedOperState_Object = MibTableColumn
hmMrpRedOperState = _HmMrpRedOperState_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 3, 1, 27),
    _HmMrpRedOperState_Type()
)
hmMrpRedOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmMrpRedOperState.setStatus("current")


class _HmMrpConfigOperState_Type(Integer32):
    """Custom type hmMrpConfigOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noError", 1),
          ("ringportLinkError", 2))
    )


_HmMrpConfigOperState_Type.__name__ = "Integer32"
_HmMrpConfigOperState_Object = MibTableColumn
hmMrpConfigOperState = _HmMrpConfigOperState_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 3, 1, 28),
    _HmMrpConfigOperState_Type()
)
hmMrpConfigOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmMrpConfigOperState.setStatus("current")
_HmMrpDomainName_Type = DisplayString
_HmMrpDomainName_Object = MibTableColumn
hmMrpDomainName = _HmMrpDomainName_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 3, 1, 29),
    _HmMrpDomainName_Type()
)
hmMrpDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmMrpDomainName.setStatus("current")


class _HmMrpMRMRecoveryDelay_Type(Integer32):
    """Custom type hmMrpMRMRecoveryDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delay200", 2),
          ("delay500", 1))
    )


_HmMrpMRMRecoveryDelay_Type.__name__ = "Integer32"
_HmMrpMRMRecoveryDelay_Object = MibTableColumn
hmMrpMRMRecoveryDelay = _HmMrpMRMRecoveryDelay_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 3, 1, 30),
    _HmMrpMRMRecoveryDelay_Type()
)
hmMrpMRMRecoveryDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmMrpMRMRecoveryDelay.setStatus("current")
_HmRpcTable_Object = MibTable
hmRpcTable = _HmRpcTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 4)
)
if mibBuilder.loadTexts:
    hmRpcTable.setStatus("current")
_HmRpcEntry_Object = MibTableRow
hmRpcEntry = _HmRpcEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 4, 1)
)
hmRpcEntry.setIndexNames(
    (0, "HMRING-MGMT-SNMP-MIB", "hmRpcRingProtocol"),
    (0, "HMRING-MGMT-SNMP-MIB", "hmRpcRingID"),
)
if mibBuilder.loadTexts:
    hmRpcEntry.setStatus("current")


class _HmRpcRingProtocol_Type(Integer32):
    """Custom type hmRpcRingProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            3
        )
    )
    namedValues = NamedValues(
        ("fastHiperRing", 3)
    )


_HmRpcRingProtocol_Type.__name__ = "Integer32"
_HmRpcRingProtocol_Object = MibTableColumn
hmRpcRingProtocol = _HmRpcRingProtocol_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 4, 1, 1),
    _HmRpcRingProtocol_Type()
)
hmRpcRingProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRpcRingProtocol.setStatus("current")
_HmRpcRingID_Type = Integer32
_HmRpcRingID_Object = MibTableColumn
hmRpcRingID = _HmRpcRingID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 4, 1, 2),
    _HmRpcRingID_Type()
)
hmRpcRingID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRpcRingID.setStatus("current")
_HmRpcRingName_Type = DisplayString
_HmRpcRingName_Object = MibTableColumn
hmRpcRingName = _HmRpcRingName_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 4, 1, 3),
    _HmRpcRingName_Type()
)
hmRpcRingName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRpcRingName.setStatus("current")
_HmRpcRingport1GroupID_Type = Integer32
_HmRpcRingport1GroupID_Object = MibTableColumn
hmRpcRingport1GroupID = _HmRpcRingport1GroupID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 4, 1, 4),
    _HmRpcRingport1GroupID_Type()
)
hmRpcRingport1GroupID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRpcRingport1GroupID.setStatus("current")
_HmRpcRingport1IfIndex_Type = Integer32
_HmRpcRingport1IfIndex_Object = MibTableColumn
hmRpcRingport1IfIndex = _HmRpcRingport1IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 4, 1, 5),
    _HmRpcRingport1IfIndex_Type()
)
hmRpcRingport1IfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRpcRingport1IfIndex.setStatus("current")


class _HmRpcRingport1OperState_Type(Integer32):
    """Custom type hmRpcRingport1OperState based on Integer32"""
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


_HmRpcRingport1OperState_Type.__name__ = "Integer32"
_HmRpcRingport1OperState_Object = MibTableColumn
hmRpcRingport1OperState = _HmRpcRingport1OperState_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 4, 1, 6),
    _HmRpcRingport1OperState_Type()
)
hmRpcRingport1OperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmRpcRingport1OperState.setStatus("current")
_HmRpcRingport2GroupID_Type = Integer32
_HmRpcRingport2GroupID_Object = MibTableColumn
hmRpcRingport2GroupID = _HmRpcRingport2GroupID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 4, 1, 7),
    _HmRpcRingport2GroupID_Type()
)
hmRpcRingport2GroupID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRpcRingport2GroupID.setStatus("current")
_HmRpcRingport2IfIndex_Type = Integer32
_HmRpcRingport2IfIndex_Object = MibTableColumn
hmRpcRingport2IfIndex = _HmRpcRingport2IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 4, 1, 8),
    _HmRpcRingport2IfIndex_Type()
)
hmRpcRingport2IfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRpcRingport2IfIndex.setStatus("current")


class _HmRpcRingport2OperState_Type(Integer32):
    """Custom type hmRpcRingport2OperState based on Integer32"""
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


_HmRpcRingport2OperState_Type.__name__ = "Integer32"
_HmRpcRingport2OperState_Object = MibTableColumn
hmRpcRingport2OperState = _HmRpcRingport2OperState_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 4, 1, 9),
    _HmRpcRingport2OperState_Type()
)
hmRpcRingport2OperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmRpcRingport2OperState.setStatus("current")
_HmRpcVlanID_Type = Integer32
_HmRpcVlanID_Object = MibTableColumn
hmRpcVlanID = _HmRpcVlanID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 4, 1, 10),
    _HmRpcVlanID_Type()
)
hmRpcVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRpcVlanID.setStatus("current")


class _HmRpcAdminState_Type(Integer32):
    """Custom type hmRpcAdminState based on Integer32"""
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


_HmRpcAdminState_Type.__name__ = "Integer32"
_HmRpcAdminState_Object = MibTableColumn
hmRpcAdminState = _HmRpcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 4, 1, 11),
    _HmRpcAdminState_Type()
)
hmRpcAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRpcAdminState.setStatus("current")


class _HmRpcOperState_Type(Integer32):
    """Custom type hmRpcOperState based on Integer32"""
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
          ("disabled", 3),
          ("manager", 2))
    )


_HmRpcOperState_Type.__name__ = "Integer32"
_HmRpcOperState_Object = MibTableColumn
hmRpcOperState = _HmRpcOperState_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 4, 1, 12),
    _HmRpcOperState_Type()
)
hmRpcOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmRpcOperState.setStatus("current")


class _HmRpcRingOperState_Type(Integer32):
    """Custom type hmRpcRingOperState based on Integer32"""
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


_HmRpcRingOperState_Type.__name__ = "Integer32"
_HmRpcRingOperState_Object = MibTableColumn
hmRpcRingOperState = _HmRpcRingOperState_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 4, 1, 13),
    _HmRpcRingOperState_Type()
)
hmRpcRingOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmRpcRingOperState.setStatus("current")


class _HmRpcRedundancyOperState_Type(Integer32):
    """Custom type hmRpcRedundancyOperState based on Integer32"""
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


_HmRpcRedundancyOperState_Type.__name__ = "Integer32"
_HmRpcRedundancyOperState_Object = MibTableColumn
hmRpcRedundancyOperState = _HmRpcRedundancyOperState_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 4, 1, 14),
    _HmRpcRedundancyOperState_Type()
)
hmRpcRedundancyOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmRpcRedundancyOperState.setStatus("current")


class _HmRpcConfigOperState_Type(Integer32):
    """Custom type hmRpcConfigOperState based on Integer32"""
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
        *(("multipleRM", 4),
          ("noError", 1),
          ("ringportLinkError", 2),
          ("singleSideReceive", 3))
    )


_HmRpcConfigOperState_Type.__name__ = "Integer32"
_HmRpcConfigOperState_Object = MibTableColumn
hmRpcConfigOperState = _HmRpcConfigOperState_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 4, 1, 15),
    _HmRpcConfigOperState_Type()
)
hmRpcConfigOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmRpcConfigOperState.setStatus("current")
_HmRpcRowStatus_Type = RowStatus
_HmRpcRowStatus_Object = MibTableColumn
hmRpcRowStatus = _HmRpcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 4, 1, 16),
    _HmRpcRowStatus_Type()
)
hmRpcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmRpcRowStatus.setStatus("current")
_HmRpcNodes_Type = Integer32
_HmRpcNodes_Object = MibTableColumn
hmRpcNodes = _HmRpcNodes_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 4, 1, 17),
    _HmRpcNodes_Type()
)
hmRpcNodes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRpcNodes.setStatus("current")
_HmRpcRoundTripDelay_Type = Unsigned32
_HmRpcRoundTripDelay_Object = MibTableColumn
hmRpcRoundTripDelay = _HmRpcRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 4, 1, 18),
    _HmRpcRoundTripDelay_Type()
)
hmRpcRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmRpcRoundTripDelay.setStatus("current")
_HmMultiHiperRing_ObjectIdentity = ObjectIdentity
hmMultiHiperRing = _HmMultiHiperRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 5)
)
_HmSrmMaxInstances_Type = Integer32
_HmSrmMaxInstances_Object = MibScalar
hmSrmMaxInstances = _HmSrmMaxInstances_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 5, 1),
    _HmSrmMaxInstances_Type()
)
hmSrmMaxInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSrmMaxInstances.setStatus("current")
_HmSrmTable_Object = MibTable
hmSrmTable = _HmSrmTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 5, 5)
)
if mibBuilder.loadTexts:
    hmSrmTable.setStatus("current")
_HmSrmEntry_Object = MibTableRow
hmSrmEntry = _HmSrmEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 5, 5, 1)
)
hmSrmEntry.setIndexNames(
    (0, "HMRING-MGMT-SNMP-MIB", "hmSrmRingID"),
)
if mibBuilder.loadTexts:
    hmSrmEntry.setStatus("current")
_HmSrmRingID_Type = Integer32
_HmSrmRingID_Object = MibTableColumn
hmSrmRingID = _HmSrmRingID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 5, 5, 1, 1),
    _HmSrmRingID_Type()
)
hmSrmRingID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSrmRingID.setStatus("current")


class _HmSrmRingProtocol_Type(Integer32):
    """Custom type hmSrmRingProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            4
        )
    )
    namedValues = NamedValues(
        ("standardMRP", 4)
    )


_HmSrmRingProtocol_Type.__name__ = "Integer32"
_HmSrmRingProtocol_Object = MibTableColumn
hmSrmRingProtocol = _HmSrmRingProtocol_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 5, 5, 1, 2),
    _HmSrmRingProtocol_Type()
)
hmSrmRingProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSrmRingProtocol.setStatus("current")
_HmSrmRingName_Type = DisplayString
_HmSrmRingName_Object = MibTableColumn
hmSrmRingName = _HmSrmRingName_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 5, 5, 1, 3),
    _HmSrmRingName_Type()
)
hmSrmRingName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSrmRingName.setStatus("current")
_HmSrmRingport1GroupID_Type = Integer32
_HmSrmRingport1GroupID_Object = MibTableColumn
hmSrmRingport1GroupID = _HmSrmRingport1GroupID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 5, 5, 1, 4),
    _HmSrmRingport1GroupID_Type()
)
hmSrmRingport1GroupID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSrmRingport1GroupID.setStatus("current")
_HmSrmRingport1IfIndex_Type = Integer32
_HmSrmRingport1IfIndex_Object = MibTableColumn
hmSrmRingport1IfIndex = _HmSrmRingport1IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 5, 5, 1, 5),
    _HmSrmRingport1IfIndex_Type()
)
hmSrmRingport1IfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSrmRingport1IfIndex.setStatus("current")


class _HmSrmRingport1OperState_Type(Integer32):
    """Custom type hmSrmRingport1OperState based on Integer32"""
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


_HmSrmRingport1OperState_Type.__name__ = "Integer32"
_HmSrmRingport1OperState_Object = MibTableColumn
hmSrmRingport1OperState = _HmSrmRingport1OperState_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 5, 5, 1, 6),
    _HmSrmRingport1OperState_Type()
)
hmSrmRingport1OperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSrmRingport1OperState.setStatus("current")


class _HmSrmVlanID_Type(Integer32):
    """Custom type hmSrmVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4042),
    )


_HmSrmVlanID_Type.__name__ = "Integer32"
_HmSrmVlanID_Object = MibTableColumn
hmSrmVlanID = _HmSrmVlanID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 5, 5, 1, 7),
    _HmSrmVlanID_Type()
)
hmSrmVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSrmVlanID.setStatus("current")


class _HmSrmAdminState_Type(Integer32):
    """Custom type hmSrmAdminState based on Integer32"""
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


_HmSrmAdminState_Type.__name__ = "Integer32"
_HmSrmAdminState_Object = MibTableColumn
hmSrmAdminState = _HmSrmAdminState_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 5, 5, 1, 8),
    _HmSrmAdminState_Type()
)
hmSrmAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSrmAdminState.setStatus("current")


class _HmSrmOperState_Type(Integer32):
    """Custom type hmSrmOperState based on Integer32"""
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


_HmSrmOperState_Type.__name__ = "Integer32"
_HmSrmOperState_Object = MibTableColumn
hmSrmOperState = _HmSrmOperState_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 5, 5, 1, 9),
    _HmSrmOperState_Type()
)
hmSrmOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSrmOperState.setStatus("current")


class _HmSrmRingOperState_Type(Integer32):
    """Custom type hmSrmRingOperState based on Integer32"""
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


_HmSrmRingOperState_Type.__name__ = "Integer32"
_HmSrmRingOperState_Object = MibTableColumn
hmSrmRingOperState = _HmSrmRingOperState_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 5, 5, 1, 10),
    _HmSrmRingOperState_Type()
)
hmSrmRingOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSrmRingOperState.setStatus("current")


class _HmSrmRedundancyOperState_Type(Integer32):
    """Custom type hmSrmRedundancyOperState based on Integer32"""
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


_HmSrmRedundancyOperState_Type.__name__ = "Integer32"
_HmSrmRedundancyOperState_Object = MibTableColumn
hmSrmRedundancyOperState = _HmSrmRedundancyOperState_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 5, 5, 1, 11),
    _HmSrmRedundancyOperState_Type()
)
hmSrmRedundancyOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSrmRedundancyOperState.setStatus("current")


class _HmSrmConfigOperState_Type(Integer32):
    """Custom type hmSrmConfigOperState based on Integer32"""
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
          ("ringportLinkError", 2),
          ("sharedVLAN", 9),
          ("trunkMember", 8))
    )


_HmSrmConfigOperState_Type.__name__ = "Integer32"
_HmSrmConfigOperState_Object = MibTableColumn
hmSrmConfigOperState = _HmSrmConfigOperState_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 5, 5, 1, 12),
    _HmSrmConfigOperState_Type()
)
hmSrmConfigOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSrmConfigOperState.setStatus("current")
_HmSrmRowStatus_Type = RowStatus
_HmSrmRowStatus_Object = MibTableColumn
hmSrmRowStatus = _HmSrmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 5, 5, 1, 13),
    _HmSrmRowStatus_Type()
)
hmSrmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmSrmRowStatus.setStatus("current")


class _HmSrmNodes_Type(Integer32):
    """Custom type hmSrmNodes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HmSrmNodes_Type.__name__ = "Integer32"
_HmSrmNodes_Object = MibTableColumn
hmSrmNodes = _HmSrmNodes_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 5, 5, 1, 14),
    _HmSrmNodes_Type()
)
hmSrmNodes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSrmNodes.setStatus("current")


class _HmSrmMRPDomainID_Type(OctetString):
    """Custom type hmSrmMRPDomainID based on OctetString"""
    defaultHexValue = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_HmSrmMRPDomainID_Type.__name__ = "OctetString"
_HmSrmMRPDomainID_Object = MibTableColumn
hmSrmMRPDomainID = _HmSrmMRPDomainID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 5, 5, 1, 15),
    _HmSrmMRPDomainID_Type()
)
hmSrmMRPDomainID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSrmMRPDomainID.setStatus("current")


class _HmSrmPartnerMAC_Type(OctetString):
    """Custom type hmSrmPartnerMAC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_HmSrmPartnerMAC_Type.__name__ = "OctetString"
_HmSrmPartnerMAC_Object = MibTableColumn
hmSrmPartnerMAC = _HmSrmPartnerMAC_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 5, 5, 1, 16),
    _HmSrmPartnerMAC_Type()
)
hmSrmPartnerMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSrmPartnerMAC.setStatus("current")

# Managed Objects groups


# Notification objects

hmRingRedReconfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 0, 1)
)
hmRingRedReconfig.setObjects(
    ("HMRING-MGMT-SNMP-MIB", "hmRingRedOperState")
)
if mibBuilder.loadTexts:
    hmRingRedReconfig.setStatus(
        "current"
    )

hmRingCplReconfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 0, 2)
)
hmRingCplReconfig.setObjects(
      *(("HMRING-MGMT-SNMP-MIB", "hmRingCplInterconnIfOpState"),
        ("HMRING-MGMT-SNMP-MIB", "hmRingCplPartnerInterconnIfOpState"),
        ("HMRING-MGMT-SNMP-MIB", "hmRingCplPartnerIpAddr"))
)
if mibBuilder.loadTexts:
    hmRingCplReconfig.setStatus(
        "current"
    )

hmRingRedConfigChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 0, 3)
)
hmRingRedConfigChanged.setObjects(
    ("HMRING-MGMT-SNMP-MIB", "hmRingRedConfigOperState")
)
if mibBuilder.loadTexts:
    hmRingRedConfigChanged.setStatus(
        "current"
    )

hmMrpReconfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 0, 4)
)
hmMrpReconfig.setObjects(
      *(("HMRING-MGMT-SNMP-MIB", "hmMrpDomainID"),
        ("HMRING-MGMT-SNMP-MIB", "hmMrpMRMRealRingState"))
)
if mibBuilder.loadTexts:
    hmMrpReconfig.setStatus(
        "current"
    )

hmRpcReconfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 0, 5)
)
hmRpcReconfig.setObjects(
      *(("HMRING-MGMT-SNMP-MIB", "hmRpcRingProtocol"),
        ("HMRING-MGMT-SNMP-MIB", "hmRpcRingID"),
        ("HMRING-MGMT-SNMP-MIB", "hmRpcRingOperState"))
)
if mibBuilder.loadTexts:
    hmRpcReconfig.setStatus(
        "current"
    )

hmSrmReconfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 0, 6)
)
hmSrmReconfig.setObjects(
      *(("HMRING-MGMT-SNMP-MIB", "hmSrmRingID"),
        ("HMRING-MGMT-SNMP-MIB", "hmSrmRingProtocol"),
        ("HMRING-MGMT-SNMP-MIB", "hmSrmRingOperState"))
)
if mibBuilder.loadTexts:
    hmSrmReconfig.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HMRING-MGMT-SNMP-MIB",
    **{"hmRingRedundancy": hmRingRedundancy,
       "hmRingRedundancyEvent": hmRingRedundancyEvent,
       "hmRingRedReconfig": hmRingRedReconfig,
       "hmRingCplReconfig": hmRingCplReconfig,
       "hmRingRedConfigChanged": hmRingRedConfigChanged,
       "hmMrpReconfig": hmMrpReconfig,
       "hmRpcReconfig": hmRpcReconfig,
       "hmSrmReconfig": hmSrmReconfig,
       "hmRingRedTable": hmRingRedTable,
       "hmRingRedEntry": hmRingRedEntry,
       "hmRingRedPrimGroupID": hmRingRedPrimGroupID,
       "hmRingRedPrimIfIndex": hmRingRedPrimIfIndex,
       "hmRingRedPrimIfOpState": hmRingRedPrimIfOpState,
       "hmRingRedRedGroupID": hmRingRedRedGroupID,
       "hmRingRedRedIfIndex": hmRingRedRedIfIndex,
       "hmRingRedRedIfOpState": hmRingRedRedIfOpState,
       "hmRingRedOperState": hmRingRedOperState,
       "hmRingRedMode": hmRingRedMode,
       "hmRingRedConfigOperState": hmRingRedConfigOperState,
       "hmRingRedRecoveryDelay": hmRingRedRecoveryDelay,
       "hmRingCouplingTable": hmRingCouplingTable,
       "hmRingCouplingEntry": hmRingCouplingEntry,
       "hmRingCplInterconnGroupID": hmRingCplInterconnGroupID,
       "hmRingCplInterconnIfIndex": hmRingCplInterconnIfIndex,
       "hmRingCplInterconnIfOpState": hmRingCplInterconnIfOpState,
       "hmRingCplControlGroupID": hmRingCplControlGroupID,
       "hmRingCplControlIfIndex": hmRingCplControlIfIndex,
       "hmRingCplControlIfOpState": hmRingCplControlIfOpState,
       "hmRingCplControlMode": hmRingCplControlMode,
       "hmRingCplPartnerIpAddr": hmRingCplPartnerIpAddr,
       "hmRingCplPartnerInterconnGroupID": hmRingCplPartnerInterconnGroupID,
       "hmRingCplPartnerInterconnIfIndex": hmRingCplPartnerInterconnIfIndex,
       "hmRingCplPartnerInterconnIfOpState": hmRingCplPartnerInterconnIfOpState,
       "hmRingCplOperState": hmRingCplOperState,
       "hmRingCplMode": hmRingCplMode,
       "hmRingCplRowStatus": hmRingCplRowStatus,
       "hmRingCplConfigOperState": hmRingCplConfigOperState,
       "hmRingCplCouplingLinks": hmRingCplCouplingLinks,
       "hmRingCplExtendedDiag": hmRingCplExtendedDiag,
       "hmRingCplNetCoupling": hmRingCplNetCoupling,
       "hmRingCplConfigSource": hmRingCplConfigSource,
       "hmMrpTable": hmMrpTable,
       "hmMrpEntry": hmMrpEntry,
       "hmMrpDomainID": hmMrpDomainID,
       "hmMrpRingport1GroupID": hmMrpRingport1GroupID,
       "hmMrpRingport1IfIndex": hmMrpRingport1IfIndex,
       "hmMrpRingport1OperState": hmMrpRingport1OperState,
       "hmMrpRingport2GroupID": hmMrpRingport2GroupID,
       "hmMrpRingport2IfIndex": hmMrpRingport2IfIndex,
       "hmMrpRingport2OperState": hmMrpRingport2OperState,
       "hmMrpVlanID": hmMrpVlanID,
       "hmMrpExpectedRole": hmMrpExpectedRole,
       "hmMrpMRCLinkDownInterval": hmMrpMRCLinkDownInterval,
       "hmMrpMRCLinkUpInterval": hmMrpMRCLinkUpInterval,
       "hmMrpMRCLinkChangeCount": hmMrpMRCLinkChangeCount,
       "hmMrpMRCBlockedSupported": hmMrpMRCBlockedSupported,
       "hmMrpMRMPriority": hmMrpMRMPriority,
       "hmMrpMRMTopologyChangeInterval": hmMrpMRMTopologyChangeInterval,
       "hmMrpMRMTopologyChangeRepeatCount": hmMrpMRMTopologyChangeRepeatCount,
       "hmMrpMRMShortTestInterval": hmMrpMRMShortTestInterval,
       "hmMrpMRMDefaultTestInterval": hmMrpMRMDefaultTestInterval,
       "hmMrpMRMTestMonitoringCount": hmMrpMRMTestMonitoringCount,
       "hmMrpMRMNonBlockingMRCSupported": hmMrpMRMNonBlockingMRCSupported,
       "hmMrpMRMTestMonitoringExtendedCount": hmMrpMRMTestMonitoringExtendedCount,
       "hmMrpMRMReactOnLinkChange": hmMrpMRMReactOnLinkChange,
       "hmMrpMRMCheckMediaRedundancy": hmMrpMRMCheckMediaRedundancy,
       "hmMrpMRMRealRoleState": hmMrpMRMRealRoleState,
       "hmMrpMRMRealRingState": hmMrpMRMRealRingState,
       "hmMrpRowStatus": hmMrpRowStatus,
       "hmMrpRedOperState": hmMrpRedOperState,
       "hmMrpConfigOperState": hmMrpConfigOperState,
       "hmMrpDomainName": hmMrpDomainName,
       "hmMrpMRMRecoveryDelay": hmMrpMRMRecoveryDelay,
       "hmRpcTable": hmRpcTable,
       "hmRpcEntry": hmRpcEntry,
       "hmRpcRingProtocol": hmRpcRingProtocol,
       "hmRpcRingID": hmRpcRingID,
       "hmRpcRingName": hmRpcRingName,
       "hmRpcRingport1GroupID": hmRpcRingport1GroupID,
       "hmRpcRingport1IfIndex": hmRpcRingport1IfIndex,
       "hmRpcRingport1OperState": hmRpcRingport1OperState,
       "hmRpcRingport2GroupID": hmRpcRingport2GroupID,
       "hmRpcRingport2IfIndex": hmRpcRingport2IfIndex,
       "hmRpcRingport2OperState": hmRpcRingport2OperState,
       "hmRpcVlanID": hmRpcVlanID,
       "hmRpcAdminState": hmRpcAdminState,
       "hmRpcOperState": hmRpcOperState,
       "hmRpcRingOperState": hmRpcRingOperState,
       "hmRpcRedundancyOperState": hmRpcRedundancyOperState,
       "hmRpcConfigOperState": hmRpcConfigOperState,
       "hmRpcRowStatus": hmRpcRowStatus,
       "hmRpcNodes": hmRpcNodes,
       "hmRpcRoundTripDelay": hmRpcRoundTripDelay,
       "hmMultiHiperRing": hmMultiHiperRing,
       "hmSrmMaxInstances": hmSrmMaxInstances,
       "hmSrmTable": hmSrmTable,
       "hmSrmEntry": hmSrmEntry,
       "hmSrmRingID": hmSrmRingID,
       "hmSrmRingProtocol": hmSrmRingProtocol,
       "hmSrmRingName": hmSrmRingName,
       "hmSrmRingport1GroupID": hmSrmRingport1GroupID,
       "hmSrmRingport1IfIndex": hmSrmRingport1IfIndex,
       "hmSrmRingport1OperState": hmSrmRingport1OperState,
       "hmSrmVlanID": hmSrmVlanID,
       "hmSrmAdminState": hmSrmAdminState,
       "hmSrmOperState": hmSrmOperState,
       "hmSrmRingOperState": hmSrmRingOperState,
       "hmSrmRedundancyOperState": hmSrmRedundancyOperState,
       "hmSrmConfigOperState": hmSrmConfigOperState,
       "hmSrmRowStatus": hmSrmRowStatus,
       "hmSrmNodes": hmSrmNodes,
       "hmSrmMRPDomainID": hmSrmMRPDomainID,
       "hmSrmPartnerMAC": hmSrmPartnerMAC}
)
