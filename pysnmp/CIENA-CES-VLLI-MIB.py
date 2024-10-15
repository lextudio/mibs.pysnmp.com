# SNMP MIB module (CIENA-CES-VLLI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CIENA-CES-VLLI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:08 2024
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

(cienaGlobalMacAddress,
 cienaGlobalSeverity) = mibBuilder.importSymbols(
    "CIENA-GLOBAL-MIB",
    "cienaGlobalMacAddress",
    "cienaGlobalSeverity")

(cienaCesConfig,
 cienaCesNotifications) = mibBuilder.importSymbols(
    "CIENA-SMI",
    "cienaCesConfig",
    "cienaCesNotifications")

(CienaGlobalState,
 CienaMacAddress,
 CienaStatsClear) = mibBuilder.importSymbols(
    "CIENA-TC",
    "CienaGlobalState",
    "CienaMacAddress",
    "CienaStatsClear")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

cienaCesVlliMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 23)
)
cienaCesVlliMIB.setRevisions(
        ("2012-02-28 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VlliAction(Integer32, TextualConvention):
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
        *(("ccmResume", 4),
          ("ccmStop", 3),
          ("portShut", 1),
          ("portUnshut", 2))
    )



class VlliLastEvent(Integer32, TextualConvention):
    status = "current"
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
        *(("adminFault", 4),
          ("adminRecovery", 5),
          ("fault", 2),
          ("recovery", 3),
          ("unknown", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CienaCesVlliMIBObjects_ObjectIdentity = ObjectIdentity
cienaCesVlliMIBObjects = _CienaCesVlliMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 23, 1)
)
_CienaCesVlli_ObjectIdentity = ObjectIdentity
cienaCesVlli = _CienaCesVlli_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 23, 1, 1)
)
_CienaCesVlliAdminState_Type = CienaGlobalState
_CienaCesVlliAdminState_Object = MibScalar
cienaCesVlliAdminState = _CienaCesVlliAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 23, 1, 1, 1),
    _CienaCesVlliAdminState_Type()
)
cienaCesVlliAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesVlliAdminState.setStatus("current")
_CienaCesVlliInstanceGroupTable_Object = MibTable
cienaCesVlliInstanceGroupTable = _CienaCesVlliInstanceGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 23, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cienaCesVlliInstanceGroupTable.setStatus("current")
_CienaCesVlliInstanceGroupEntry_Object = MibTableRow
cienaCesVlliInstanceGroupEntry = _CienaCesVlliInstanceGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 23, 1, 1, 2, 1)
)
cienaCesVlliInstanceGroupEntry.setIndexNames(
    (0, "CIENA-CES-VLLI-MIB", "cienaCesVlliInstanceGroupId"),
)
if mibBuilder.loadTexts:
    cienaCesVlliInstanceGroupEntry.setStatus("current")


class _CienaCesVlliInstanceGroupId_Type(Integer32):
    """Custom type cienaCesVlliInstanceGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_CienaCesVlliInstanceGroupId_Type.__name__ = "Integer32"
_CienaCesVlliInstanceGroupId_Object = MibTableColumn
cienaCesVlliInstanceGroupId = _CienaCesVlliInstanceGroupId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 23, 1, 1, 2, 1, 1),
    _CienaCesVlliInstanceGroupId_Type()
)
cienaCesVlliInstanceGroupId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesVlliInstanceGroupId.setStatus("current")
_CienaCesVlliInstanceGroupName_Type = DisplayString
_CienaCesVlliInstanceGroupName_Object = MibTableColumn
cienaCesVlliInstanceGroupName = _CienaCesVlliInstanceGroupName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 23, 1, 1, 2, 1, 2),
    _CienaCesVlliInstanceGroupName_Type()
)
cienaCesVlliInstanceGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesVlliInstanceGroupName.setStatus("current")


class _CienaCesVlliInstanceGroupDirection_Type(Integer32):
    """Custom type cienaCesVlliInstanceGroupDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional", 2),
          ("unidirectional", 1))
    )


_CienaCesVlliInstanceGroupDirection_Type.__name__ = "Integer32"
_CienaCesVlliInstanceGroupDirection_Object = MibTableColumn
cienaCesVlliInstanceGroupDirection = _CienaCesVlliInstanceGroupDirection_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 23, 1, 1, 2, 1, 3),
    _CienaCesVlliInstanceGroupDirection_Type()
)
cienaCesVlliInstanceGroupDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesVlliInstanceGroupDirection.setStatus("current")


class _CienaCesVlliInstanceGroupTrigger_Type(Integer32):
    """Custom type cienaCesVlliInstanceGroupTrigger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 2),
          ("any", 1))
    )


_CienaCesVlliInstanceGroupTrigger_Type.__name__ = "Integer32"
_CienaCesVlliInstanceGroupTrigger_Object = MibTableColumn
cienaCesVlliInstanceGroupTrigger = _CienaCesVlliInstanceGroupTrigger_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 23, 1, 1, 2, 1, 4),
    _CienaCesVlliInstanceGroupTrigger_Type()
)
cienaCesVlliInstanceGroupTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesVlliInstanceGroupTrigger.setStatus("current")
_CienaCesVlliInstanceGroupState_Type = CienaGlobalState
_CienaCesVlliInstanceGroupState_Object = MibTableColumn
cienaCesVlliInstanceGroupState = _CienaCesVlliInstanceGroupState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 23, 1, 1, 2, 1, 5),
    _CienaCesVlliInstanceGroupState_Type()
)
cienaCesVlliInstanceGroupState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesVlliInstanceGroupState.setStatus("current")
_CienaCesVlliActionGroupTable_Object = MibTable
cienaCesVlliActionGroupTable = _CienaCesVlliActionGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 23, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cienaCesVlliActionGroupTable.setStatus("current")
_CienaCesVlliActionGroupEntry_Object = MibTableRow
cienaCesVlliActionGroupEntry = _CienaCesVlliActionGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 23, 1, 1, 3, 1)
)
cienaCesVlliActionGroupEntry.setIndexNames(
    (0, "CIENA-CES-VLLI-MIB", "cienaCesVlliActionGroupId"),
)
if mibBuilder.loadTexts:
    cienaCesVlliActionGroupEntry.setStatus("current")


class _CienaCesVlliActionGroupId_Type(Integer32):
    """Custom type cienaCesVlliActionGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_CienaCesVlliActionGroupId_Type.__name__ = "Integer32"
_CienaCesVlliActionGroupId_Object = MibTableColumn
cienaCesVlliActionGroupId = _CienaCesVlliActionGroupId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 23, 1, 1, 3, 1, 1),
    _CienaCesVlliActionGroupId_Type()
)
cienaCesVlliActionGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesVlliActionGroupId.setStatus("current")
_CienaCesVlliActionGroupName_Type = DisplayString
_CienaCesVlliActionGroupName_Object = MibTableColumn
cienaCesVlliActionGroupName = _CienaCesVlliActionGroupName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 23, 1, 1, 3, 1, 2),
    _CienaCesVlliActionGroupName_Type()
)
cienaCesVlliActionGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesVlliActionGroupName.setStatus("current")
_CienaCesVlliActRecoveryPreceOne_Type = VlliAction
_CienaCesVlliActRecoveryPreceOne_Object = MibTableColumn
cienaCesVlliActRecoveryPreceOne = _CienaCesVlliActRecoveryPreceOne_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 23, 1, 1, 3, 1, 3),
    _CienaCesVlliActRecoveryPreceOne_Type()
)
cienaCesVlliActRecoveryPreceOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesVlliActRecoveryPreceOne.setStatus("current")
_CienaCesVlliActRecoveryPreceTwo_Type = VlliAction
_CienaCesVlliActRecoveryPreceTwo_Object = MibTableColumn
cienaCesVlliActRecoveryPreceTwo = _CienaCesVlliActRecoveryPreceTwo_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 23, 1, 1, 3, 1, 4),
    _CienaCesVlliActRecoveryPreceTwo_Type()
)
cienaCesVlliActRecoveryPreceTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesVlliActRecoveryPreceTwo.setStatus("current")
_CienaCesVlliActRecoveryPreceThree_Type = VlliAction
_CienaCesVlliActRecoveryPreceThree_Object = MibTableColumn
cienaCesVlliActRecoveryPreceThree = _CienaCesVlliActRecoveryPreceThree_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 23, 1, 1, 3, 1, 5),
    _CienaCesVlliActRecoveryPreceThree_Type()
)
cienaCesVlliActRecoveryPreceThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesVlliActRecoveryPreceThree.setStatus("current")
_CienaCesVlliActRecoveryPreceFour_Type = VlliAction
_CienaCesVlliActRecoveryPreceFour_Object = MibTableColumn
cienaCesVlliActRecoveryPreceFour = _CienaCesVlliActRecoveryPreceFour_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 23, 1, 1, 3, 1, 6),
    _CienaCesVlliActRecoveryPreceFour_Type()
)
cienaCesVlliActRecoveryPreceFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesVlliActRecoveryPreceFour.setStatus("current")
_CienaCesVlliActRecoveryPreceFive_Type = VlliAction
_CienaCesVlliActRecoveryPreceFive_Object = MibTableColumn
cienaCesVlliActRecoveryPreceFive = _CienaCesVlliActRecoveryPreceFive_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 23, 1, 1, 3, 1, 7),
    _CienaCesVlliActRecoveryPreceFive_Type()
)
cienaCesVlliActRecoveryPreceFive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesVlliActRecoveryPreceFive.setStatus("current")
_CienaCesVlliActRecoveryPreceSix_Type = VlliAction
_CienaCesVlliActRecoveryPreceSix_Object = MibTableColumn
cienaCesVlliActRecoveryPreceSix = _CienaCesVlliActRecoveryPreceSix_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 23, 1, 1, 3, 1, 8),
    _CienaCesVlliActRecoveryPreceSix_Type()
)
cienaCesVlliActRecoveryPreceSix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesVlliActRecoveryPreceSix.setStatus("current")
_CienaCesVlliActRecoveryPreceSeven_Type = VlliAction
_CienaCesVlliActRecoveryPreceSeven_Object = MibTableColumn
cienaCesVlliActRecoveryPreceSeven = _CienaCesVlliActRecoveryPreceSeven_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 23, 1, 1, 3, 1, 9),
    _CienaCesVlliActRecoveryPreceSeven_Type()
)
cienaCesVlliActRecoveryPreceSeven.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesVlliActRecoveryPreceSeven.setStatus("current")
_CienaCesVlliActRecoveryPreceEight_Type = VlliAction
_CienaCesVlliActRecoveryPreceEight_Object = MibTableColumn
cienaCesVlliActRecoveryPreceEight = _CienaCesVlliActRecoveryPreceEight_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 23, 1, 1, 3, 1, 10),
    _CienaCesVlliActRecoveryPreceEight_Type()
)
cienaCesVlliActRecoveryPreceEight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesVlliActRecoveryPreceEight.setStatus("current")
_CienaCesVlliActFaultPreceOne_Type = VlliAction
_CienaCesVlliActFaultPreceOne_Object = MibTableColumn
cienaCesVlliActFaultPreceOne = _CienaCesVlliActFaultPreceOne_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 23, 1, 1, 3, 1, 11),
    _CienaCesVlliActFaultPreceOne_Type()
)
cienaCesVlliActFaultPreceOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesVlliActFaultPreceOne.setStatus("current")
_CienaCesVlliActFaultPreceTwo_Type = VlliAction
_CienaCesVlliActFaultPreceTwo_Object = MibTableColumn
cienaCesVlliActFaultPreceTwo = _CienaCesVlliActFaultPreceTwo_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 23, 1, 1, 3, 1, 12),
    _CienaCesVlliActFaultPreceTwo_Type()
)
cienaCesVlliActFaultPreceTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesVlliActFaultPreceTwo.setStatus("current")
_CienaCesVlliActFaultPreceThree_Type = VlliAction
_CienaCesVlliActFaultPreceThree_Object = MibTableColumn
cienaCesVlliActFaultPreceThree = _CienaCesVlliActFaultPreceThree_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 23, 1, 1, 3, 1, 13),
    _CienaCesVlliActFaultPreceThree_Type()
)
cienaCesVlliActFaultPreceThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesVlliActFaultPreceThree.setStatus("current")
_CienaCesVlliActFaultPreceFour_Type = VlliAction
_CienaCesVlliActFaultPreceFour_Object = MibTableColumn
cienaCesVlliActFaultPreceFour = _CienaCesVlliActFaultPreceFour_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 23, 1, 1, 3, 1, 14),
    _CienaCesVlliActFaultPreceFour_Type()
)
cienaCesVlliActFaultPreceFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesVlliActFaultPreceFour.setStatus("current")
_CienaCesVlliActFaultPreceFive_Type = VlliAction
_CienaCesVlliActFaultPreceFive_Object = MibTableColumn
cienaCesVlliActFaultPreceFive = _CienaCesVlliActFaultPreceFive_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 23, 1, 1, 3, 1, 15),
    _CienaCesVlliActFaultPreceFive_Type()
)
cienaCesVlliActFaultPreceFive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesVlliActFaultPreceFive.setStatus("current")
_CienaCesVlliActFaultPreceSix_Type = VlliAction
_CienaCesVlliActFaultPreceSix_Object = MibTableColumn
cienaCesVlliActFaultPreceSix = _CienaCesVlliActFaultPreceSix_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 23, 1, 1, 3, 1, 16),
    _CienaCesVlliActFaultPreceSix_Type()
)
cienaCesVlliActFaultPreceSix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesVlliActFaultPreceSix.setStatus("current")
_CienaCesVlliActFaultPreceSeven_Type = VlliAction
_CienaCesVlliActFaultPreceSeven_Object = MibTableColumn
cienaCesVlliActFaultPreceSeven = _CienaCesVlliActFaultPreceSeven_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 23, 1, 1, 3, 1, 17),
    _CienaCesVlliActFaultPreceSeven_Type()
)
cienaCesVlliActFaultPreceSeven.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesVlliActFaultPreceSeven.setStatus("current")
_CienaCesVlliActFaultPreceEight_Type = VlliAction
_CienaCesVlliActFaultPreceEight_Object = MibTableColumn
cienaCesVlliActFaultPreceEight = _CienaCesVlliActFaultPreceEight_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 23, 1, 1, 3, 1, 18),
    _CienaCesVlliActFaultPreceEight_Type()
)
cienaCesVlliActFaultPreceEight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesVlliActFaultPreceEight.setStatus("current")
_CienaCesVlliInstanceTable_Object = MibTable
cienaCesVlliInstanceTable = _CienaCesVlliInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 23, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cienaCesVlliInstanceTable.setStatus("current")
_CienaCesVlliInstanceEntry_Object = MibTableRow
cienaCesVlliInstanceEntry = _CienaCesVlliInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 23, 1, 1, 4, 1)
)
cienaCesVlliInstanceEntry.setIndexNames(
    (0, "CIENA-CES-VLLI-MIB", "cienaCesVlliInstanceGrpId"),
    (0, "CIENA-CES-VLLI-MIB", "cienaCesVlliInstanceId"),
)
if mibBuilder.loadTexts:
    cienaCesVlliInstanceEntry.setStatus("current")


class _CienaCesVlliInstanceGrpId_Type(Integer32):
    """Custom type cienaCesVlliInstanceGrpId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_CienaCesVlliInstanceGrpId_Type.__name__ = "Integer32"
_CienaCesVlliInstanceGrpId_Object = MibTableColumn
cienaCesVlliInstanceGrpId = _CienaCesVlliInstanceGrpId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 23, 1, 1, 4, 1, 1),
    _CienaCesVlliInstanceGrpId_Type()
)
cienaCesVlliInstanceGrpId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesVlliInstanceGrpId.setStatus("current")


class _CienaCesVlliInstanceId_Type(Integer32):
    """Custom type cienaCesVlliInstanceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_CienaCesVlliInstanceId_Type.__name__ = "Integer32"
_CienaCesVlliInstanceId_Object = MibTableColumn
cienaCesVlliInstanceId = _CienaCesVlliInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 23, 1, 1, 4, 1, 2),
    _CienaCesVlliInstanceId_Type()
)
cienaCesVlliInstanceId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesVlliInstanceId.setStatus("current")


class _CienaCesVlliInstanceMode_Type(Integer32):
    """Custom type cienaCesVlliInstanceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("destination", 1),
          ("source", 2))
    )


_CienaCesVlliInstanceMode_Type.__name__ = "Integer32"
_CienaCesVlliInstanceMode_Object = MibTableColumn
cienaCesVlliInstanceMode = _CienaCesVlliInstanceMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 23, 1, 1, 4, 1, 3),
    _CienaCesVlliInstanceMode_Type()
)
cienaCesVlliInstanceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesVlliInstanceMode.setStatus("current")


class _CienaCesVlliInstanceType_Type(Integer32):
    """Custom type cienaCesVlliInstanceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cfm", 2),
          ("port", 1))
    )


_CienaCesVlliInstanceType_Type.__name__ = "Integer32"
_CienaCesVlliInstanceType_Object = MibTableColumn
cienaCesVlliInstanceType = _CienaCesVlliInstanceType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 23, 1, 1, 4, 1, 4),
    _CienaCesVlliInstanceType_Type()
)
cienaCesVlliInstanceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesVlliInstanceType.setStatus("current")
_CienaCesVlliInstanceName_Type = DisplayString
_CienaCesVlliInstanceName_Object = MibTableColumn
cienaCesVlliInstanceName = _CienaCesVlliInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 23, 1, 1, 4, 1, 5),
    _CienaCesVlliInstanceName_Type()
)
cienaCesVlliInstanceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesVlliInstanceName.setStatus("current")
_CienaCesVlliInstanceActionName_Type = DisplayString
_CienaCesVlliInstanceActionName_Object = MibTableColumn
cienaCesVlliInstanceActionName = _CienaCesVlliInstanceActionName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 23, 1, 1, 4, 1, 6),
    _CienaCesVlliInstanceActionName_Type()
)
cienaCesVlliInstanceActionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesVlliInstanceActionName.setStatus("current")
_CienaCesVlliInstanceLastEvent_Type = VlliLastEvent
_CienaCesVlliInstanceLastEvent_Object = MibTableColumn
cienaCesVlliInstanceLastEvent = _CienaCesVlliInstanceLastEvent_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 23, 1, 1, 4, 1, 7),
    _CienaCesVlliInstanceLastEvent_Type()
)
cienaCesVlliInstanceLastEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesVlliInstanceLastEvent.setStatus("current")
_CienaCesVlliMIBConformance_ObjectIdentity = ObjectIdentity
cienaCesVlliMIBConformance = _CienaCesVlliMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 23, 3)
)
_CienaCesVlliMIBCompliances_ObjectIdentity = ObjectIdentity
cienaCesVlliMIBCompliances = _CienaCesVlliMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 23, 3, 1)
)
_CienaCesVlliMIBGroups_ObjectIdentity = ObjectIdentity
cienaCesVlliMIBGroups = _CienaCesVlliMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 23, 3, 2)
)
_CienaCesVlliNotificationPrefix_ObjectIdentity = ObjectIdentity
cienaCesVlliNotificationPrefix = _CienaCesVlliNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 99)
)
_CienaCesVlliNotifications_ObjectIdentity = ObjectIdentity
cienaCesVlliNotifications = _CienaCesVlliNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 99, 0)
)

# Managed Objects groups


# Notification objects

cienaCesVlliFaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 99, 0, 1)
)
cienaCesVlliFaultTrap.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-VLLI-MIB", "cienaCesVlliInstanceGrpId"),
        ("CIENA-CES-VLLI-MIB", "cienaCesVlliInstanceId"),
        ("CIENA-CES-VLLI-MIB", "cienaCesVlliInstanceGroupName"),
        ("CIENA-CES-VLLI-MIB", "cienaCesVlliInstanceName"))
)
if mibBuilder.loadTexts:
    cienaCesVlliFaultTrap.setStatus(
        "current"
    )

cienaCesVlliRecoveryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 99, 0, 2)
)
cienaCesVlliRecoveryTrap.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-VLLI-MIB", "cienaCesVlliInstanceGrpId"),
        ("CIENA-CES-VLLI-MIB", "cienaCesVlliInstanceId"),
        ("CIENA-CES-VLLI-MIB", "cienaCesVlliInstanceGroupName"),
        ("CIENA-CES-VLLI-MIB", "cienaCesVlliInstanceName"))
)
if mibBuilder.loadTexts:
    cienaCesVlliRecoveryTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-CES-VLLI-MIB",
    **{"VlliAction": VlliAction,
       "VlliLastEvent": VlliLastEvent,
       "cienaCesVlliMIB": cienaCesVlliMIB,
       "cienaCesVlliMIBObjects": cienaCesVlliMIBObjects,
       "cienaCesVlli": cienaCesVlli,
       "cienaCesVlliAdminState": cienaCesVlliAdminState,
       "cienaCesVlliInstanceGroupTable": cienaCesVlliInstanceGroupTable,
       "cienaCesVlliInstanceGroupEntry": cienaCesVlliInstanceGroupEntry,
       "cienaCesVlliInstanceGroupId": cienaCesVlliInstanceGroupId,
       "cienaCesVlliInstanceGroupName": cienaCesVlliInstanceGroupName,
       "cienaCesVlliInstanceGroupDirection": cienaCesVlliInstanceGroupDirection,
       "cienaCesVlliInstanceGroupTrigger": cienaCesVlliInstanceGroupTrigger,
       "cienaCesVlliInstanceGroupState": cienaCesVlliInstanceGroupState,
       "cienaCesVlliActionGroupTable": cienaCesVlliActionGroupTable,
       "cienaCesVlliActionGroupEntry": cienaCesVlliActionGroupEntry,
       "cienaCesVlliActionGroupId": cienaCesVlliActionGroupId,
       "cienaCesVlliActionGroupName": cienaCesVlliActionGroupName,
       "cienaCesVlliActRecoveryPreceOne": cienaCesVlliActRecoveryPreceOne,
       "cienaCesVlliActRecoveryPreceTwo": cienaCesVlliActRecoveryPreceTwo,
       "cienaCesVlliActRecoveryPreceThree": cienaCesVlliActRecoveryPreceThree,
       "cienaCesVlliActRecoveryPreceFour": cienaCesVlliActRecoveryPreceFour,
       "cienaCesVlliActRecoveryPreceFive": cienaCesVlliActRecoveryPreceFive,
       "cienaCesVlliActRecoveryPreceSix": cienaCesVlliActRecoveryPreceSix,
       "cienaCesVlliActRecoveryPreceSeven": cienaCesVlliActRecoveryPreceSeven,
       "cienaCesVlliActRecoveryPreceEight": cienaCesVlliActRecoveryPreceEight,
       "cienaCesVlliActFaultPreceOne": cienaCesVlliActFaultPreceOne,
       "cienaCesVlliActFaultPreceTwo": cienaCesVlliActFaultPreceTwo,
       "cienaCesVlliActFaultPreceThree": cienaCesVlliActFaultPreceThree,
       "cienaCesVlliActFaultPreceFour": cienaCesVlliActFaultPreceFour,
       "cienaCesVlliActFaultPreceFive": cienaCesVlliActFaultPreceFive,
       "cienaCesVlliActFaultPreceSix": cienaCesVlliActFaultPreceSix,
       "cienaCesVlliActFaultPreceSeven": cienaCesVlliActFaultPreceSeven,
       "cienaCesVlliActFaultPreceEight": cienaCesVlliActFaultPreceEight,
       "cienaCesVlliInstanceTable": cienaCesVlliInstanceTable,
       "cienaCesVlliInstanceEntry": cienaCesVlliInstanceEntry,
       "cienaCesVlliInstanceGrpId": cienaCesVlliInstanceGrpId,
       "cienaCesVlliInstanceId": cienaCesVlliInstanceId,
       "cienaCesVlliInstanceMode": cienaCesVlliInstanceMode,
       "cienaCesVlliInstanceType": cienaCesVlliInstanceType,
       "cienaCesVlliInstanceName": cienaCesVlliInstanceName,
       "cienaCesVlliInstanceActionName": cienaCesVlliInstanceActionName,
       "cienaCesVlliInstanceLastEvent": cienaCesVlliInstanceLastEvent,
       "cienaCesVlliMIBConformance": cienaCesVlliMIBConformance,
       "cienaCesVlliMIBCompliances": cienaCesVlliMIBCompliances,
       "cienaCesVlliMIBGroups": cienaCesVlliMIBGroups,
       "cienaCesVlliNotificationPrefix": cienaCesVlliNotificationPrefix,
       "cienaCesVlliNotifications": cienaCesVlliNotifications,
       "cienaCesVlliFaultTrap": cienaCesVlliFaultTrap,
       "cienaCesVlliRecoveryTrap": cienaCesVlliRecoveryTrap}
)
