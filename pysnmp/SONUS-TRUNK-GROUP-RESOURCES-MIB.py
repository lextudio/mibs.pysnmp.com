# SNMP MIB module (SONUS-TRUNK-GROUP-RESOURCES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONUS-TRUNK-GROUP-RESOURCES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:57:15 2024
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

(sonusEventClass,
 sonusEventDescription,
 sonusEventLevel) = mibBuilder.importSymbols(
    "SONUS-COMMON-MIB",
    "sonusEventClass",
    "sonusEventDescription",
    "sonusEventLevel")

(sonusResourcesMIBs,) = mibBuilder.importSymbols(
    "SONUS-SMI",
    "sonusResourcesMIBs")

(SonusBoolean,
 SonusName) = mibBuilder.importSymbols(
    "SONUS-TC",
    "SonusBoolean",
    "SonusName")


# MODULE-IDENTITY

sonusTrunkGroupResourcesMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonusTrunkGroupResourcesMIBObjects_ObjectIdentity = ObjectIdentity
sonusTrunkGroupResourcesMIBObjects = _SonusTrunkGroupResourcesMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1)
)
_SonusTrunkObjects_ObjectIdentity = ObjectIdentity
sonusTrunkObjects = _SonusTrunkObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1)
)
_SonusTrunkConfigObjects_ObjectIdentity = ObjectIdentity
sonusTrunkConfigObjects = _SonusTrunkConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 1)
)


class _SonusTgMaxRpcLpcs_Type(Integer32):
    """Custom type sonusTgMaxRpcLpcs based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonusTgMaxRpcLpcs_Type.__name__ = "Integer32"
_SonusTgMaxRpcLpcs_Object = MibScalar
sonusTgMaxRpcLpcs = _SonusTgMaxRpcLpcs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 1, 1),
    _SonusTgMaxRpcLpcs_Type()
)
sonusTgMaxRpcLpcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTgMaxRpcLpcs.setStatus("current")


class _SonusTgMaxCics_Type(Integer32):
    """Custom type sonusTgMaxCics based on Integer32"""
    defaultValue = 10000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonusTgMaxCics_Type.__name__ = "Integer32"
_SonusTgMaxCics_Object = MibScalar
sonusTgMaxCics = _SonusTgMaxCics_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 1, 2),
    _SonusTgMaxCics_Type()
)
sonusTgMaxCics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTgMaxCics.setStatus("current")


class _SonusTgMaxTrunkGroups_Type(Integer32):
    """Custom type sonusTgMaxTrunkGroups based on Integer32"""
    defaultValue = 250

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_SonusTgMaxTrunkGroups_Type.__name__ = "Integer32"
_SonusTgMaxTrunkGroups_Object = MibScalar
sonusTgMaxTrunkGroups = _SonusTgMaxTrunkGroups_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 1, 3),
    _SonusTgMaxTrunkGroups_Type()
)
sonusTgMaxTrunkGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTgMaxTrunkGroups.setStatus("current")


class _SonusTgMaxServiceGroups_Type(Integer32):
    """Custom type sonusTgMaxServiceGroups based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonusTgMaxServiceGroups_Type.__name__ = "Integer32"
_SonusTgMaxServiceGroups_Object = MibScalar
sonusTgMaxServiceGroups = _SonusTgMaxServiceGroups_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 1, 4),
    _SonusTgMaxServiceGroups_Type()
)
sonusTgMaxServiceGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTgMaxServiceGroups.setStatus("current")


class _SonusTgMaxSgInstances_Type(Integer32):
    """Custom type sonusTgMaxSgInstances based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonusTgMaxSgInstances_Type.__name__ = "Integer32"
_SonusTgMaxSgInstances_Object = MibScalar
sonusTgMaxSgInstances = _SonusTgMaxSgInstances_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 1, 5),
    _SonusTgMaxSgInstances_Type()
)
sonusTgMaxSgInstances.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTgMaxSgInstances.setStatus("current")
_SonusTgObjects_ObjectIdentity = ObjectIdentity
sonusTgObjects = _SonusTgObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 2)
)
_SonusTgNextIndex_Type = Integer32
_SonusTgNextIndex_Object = MibScalar
sonusTgNextIndex = _SonusTgNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 2, 1),
    _SonusTgNextIndex_Type()
)
sonusTgNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTgNextIndex.setStatus("current")
_SonusTgTable_Object = MibTable
sonusTgTable = _SonusTgTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    sonusTgTable.setStatus("current")
_SonusTgEntry_Object = MibTableRow
sonusTgEntry = _SonusTgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 2, 2, 1)
)
sonusTgEntry.setIndexNames(
    (0, "SONUS-TRUNK-GROUP-RESOURCES-MIB", "sonusTgIndex"),
)
if mibBuilder.loadTexts:
    sonusTgEntry.setStatus("current")
_SonusTgIndex_Type = Integer32
_SonusTgIndex_Object = MibTableColumn
sonusTgIndex = _SonusTgIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 2, 2, 1, 1),
    _SonusTgIndex_Type()
)
sonusTgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTgIndex.setStatus("current")
_SonusTgName_Type = SonusName
_SonusTgName_Object = MibTableColumn
sonusTgName = _SonusTgName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 2, 2, 1, 2),
    _SonusTgName_Type()
)
sonusTgName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTgName.setStatus("current")


class _SonusTgProfName_Type(DisplayString):
    """Custom type sonusTgProfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_SonusTgProfName_Type.__name__ = "DisplayString"
_SonusTgProfName_Object = MibTableColumn
sonusTgProfName = _SonusTgProfName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 2, 2, 1, 3),
    _SonusTgProfName_Type()
)
sonusTgProfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTgProfName.setStatus("current")


class _SonusTgSgSelect_Type(Integer32):
    """Custom type sonusTgSgSelect based on Integer32"""
    defaultValue = 1

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
        *(("circularbackward", 4),
          ("circularforward", 3),
          ("configured", 2),
          ("leastcost", 1))
    )


_SonusTgSgSelect_Type.__name__ = "Integer32"
_SonusTgSgSelect_Object = MibTableColumn
sonusTgSgSelect = _SonusTgSgSelect_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 2, 2, 1, 4),
    _SonusTgSgSelect_Type()
)
sonusTgSgSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTgSgSelect.setStatus("current")


class _SonusTgLnpTranslate_Type(SonusBoolean):
    """Custom type sonusTgLnpTranslate based on SonusBoolean"""


_SonusTgLnpTranslate_Object = MibTableColumn
sonusTgLnpTranslate = _SonusTgLnpTranslate_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 2, 2, 1, 5),
    _SonusTgLnpTranslate_Type()
)
sonusTgLnpTranslate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTgLnpTranslate.setStatus("current")


class _SonusTg800Translate_Type(SonusBoolean):
    """Custom type sonusTg800Translate based on SonusBoolean"""


_SonusTg800Translate_Object = MibTableColumn
sonusTg800Translate = _SonusTg800Translate_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 2, 2, 1, 6),
    _SonusTg800Translate_Type()
)
sonusTg800Translate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTg800Translate.setStatus("current")


class _SonusTgCallingNumVerify_Type(SonusBoolean):
    """Custom type sonusTgCallingNumVerify based on SonusBoolean"""


_SonusTgCallingNumVerify_Object = MibTableColumn
sonusTgCallingNumVerify = _SonusTgCallingNumVerify_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 2, 2, 1, 7),
    _SonusTgCallingNumVerify_Type()
)
sonusTgCallingNumVerify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTgCallingNumVerify.setStatus("current")


class _SonusTgInboundReserved_Type(Integer32):
    """Custom type sonusTgInboundReserved based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SonusTgInboundReserved_Type.__name__ = "Integer32"
_SonusTgInboundReserved_Object = MibTableColumn
sonusTgInboundReserved = _SonusTgInboundReserved_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 2, 2, 1, 8),
    _SonusTgInboundReserved_Type()
)
sonusTgInboundReserved.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTgInboundReserved.setStatus("current")


class _SonusTgIsupOnly_Type(SonusBoolean):
    """Custom type sonusTgIsupOnly based on SonusBoolean"""


_SonusTgIsupOnly_Object = MibTableColumn
sonusTgIsupOnly = _SonusTgIsupOnly_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 2, 2, 1, 9),
    _SonusTgIsupOnly_Type()
)
sonusTgIsupOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTgIsupOnly.setStatus("current")


class _SonusTgCarrier_Type(DisplayString):
    """Custom type sonusTgCarrier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_SonusTgCarrier_Type.__name__ = "DisplayString"
_SonusTgCarrier_Object = MibTableColumn
sonusTgCarrier = _SonusTgCarrier_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 2, 2, 1, 10),
    _SonusTgCarrier_Type()
)
sonusTgCarrier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTgCarrier.setStatus("current")


class _SonusTgIsupNode_Type(DisplayString):
    """Custom type sonusTgIsupNode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_SonusTgIsupNode_Type.__name__ = "DisplayString"
_SonusTgIsupNode_Object = MibTableColumn
sonusTgIsupNode = _SonusTgIsupNode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 2, 2, 1, 11),
    _SonusTgIsupNode_Type()
)
sonusTgIsupNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTgIsupNode.setStatus("current")


class _SonusTgAdminState_Type(Integer32):
    """Custom type sonusTgAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SonusTgAdminState_Type.__name__ = "Integer32"
_SonusTgAdminState_Object = MibTableColumn
sonusTgAdminState = _SonusTgAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 2, 2, 1, 12),
    _SonusTgAdminState_Type()
)
sonusTgAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTgAdminState.setStatus("current")


class _SonusTgMode_Type(Integer32):
    """Custom type sonusTgMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inService", 1),
          ("outOfService", 2))
    )


_SonusTgMode_Type.__name__ = "Integer32"
_SonusTgMode_Object = MibTableColumn
sonusTgMode = _SonusTgMode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 2, 2, 1, 13),
    _SonusTgMode_Type()
)
sonusTgMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTgMode.setStatus("current")


class _SonusTgAction_Type(Integer32):
    """Custom type sonusTgAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dryUp", 1),
          ("force", 2))
    )


_SonusTgAction_Type.__name__ = "Integer32"
_SonusTgAction_Object = MibTableColumn
sonusTgAction = _SonusTgAction_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 2, 2, 1, 14),
    _SonusTgAction_Type()
)
sonusTgAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTgAction.setStatus("current")


class _SonusTgTimeout_Type(Integer32):
    """Custom type sonusTgTimeout based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_SonusTgTimeout_Type.__name__ = "Integer32"
_SonusTgTimeout_Object = MibTableColumn
sonusTgTimeout = _SonusTgTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 2, 2, 1, 15),
    _SonusTgTimeout_Type()
)
sonusTgTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTgTimeout.setStatus("current")
_SonusTgRowStatus_Type = RowStatus
_SonusTgRowStatus_Object = MibTableColumn
sonusTgRowStatus = _SonusTgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 2, 2, 1, 16),
    _SonusTgRowStatus_Type()
)
sonusTgRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTgRowStatus.setStatus("current")


class _SonusTgCirResvState_Type(Integer32):
    """Custom type sonusTgCirResvState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SonusTgCirResvState_Type.__name__ = "Integer32"
_SonusTgCirResvState_Object = MibTableColumn
sonusTgCirResvState = _SonusTgCirResvState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 2, 2, 1, 17),
    _SonusTgCirResvState_Type()
)
sonusTgCirResvState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTgCirResvState.setStatus("current")


class _SonusTgPriorityCallReserve_Type(Integer32):
    """Custom type sonusTgPriorityCallReserve based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SonusTgPriorityCallReserve_Type.__name__ = "Integer32"
_SonusTgPriorityCallReserve_Object = MibTableColumn
sonusTgPriorityCallReserve = _SonusTgPriorityCallReserve_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 2, 2, 1, 18),
    _SonusTgPriorityCallReserve_Type()
)
sonusTgPriorityCallReserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTgPriorityCallReserve.setStatus("current")


class _SonusTgIncomingCallReserve_Type(Integer32):
    """Custom type sonusTgIncomingCallReserve based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SonusTgIncomingCallReserve_Type.__name__ = "Integer32"
_SonusTgIncomingCallReserve_Object = MibTableColumn
sonusTgIncomingCallReserve = _SonusTgIncomingCallReserve_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 2, 2, 1, 19),
    _SonusTgIncomingCallReserve_Type()
)
sonusTgIncomingCallReserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTgIncomingCallReserve.setStatus("current")


class _SonusTgOutgoingCallReserve_Type(Integer32):
    """Custom type sonusTgOutgoingCallReserve based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SonusTgOutgoingCallReserve_Type.__name__ = "Integer32"
_SonusTgOutgoingCallReserve_Object = MibTableColumn
sonusTgOutgoingCallReserve = _SonusTgOutgoingCallReserve_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 2, 2, 1, 20),
    _SonusTgOutgoingCallReserve_Type()
)
sonusTgOutgoingCallReserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTgOutgoingCallReserve.setStatus("current")
_SonusTgStatusTable_Object = MibTable
sonusTgStatusTable = _SonusTgStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 3)
)
if mibBuilder.loadTexts:
    sonusTgStatusTable.setStatus("current")
_SonusTgStatusEntry_Object = MibTableRow
sonusTgStatusEntry = _SonusTgStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 3, 1)
)
sonusTgStatusEntry.setIndexNames(
    (0, "SONUS-TRUNK-GROUP-RESOURCES-MIB", "sonusTgStatusIndex"),
)
if mibBuilder.loadTexts:
    sonusTgStatusEntry.setStatus("current")
_SonusTgStatusIndex_Type = Integer32
_SonusTgStatusIndex_Object = MibTableColumn
sonusTgStatusIndex = _SonusTgStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 3, 1, 1),
    _SonusTgStatusIndex_Type()
)
sonusTgStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTgStatusIndex.setStatus("current")


class _SonusTgOperState_Type(Integer32):
    """Custom type sonusTgOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inService", 1),
          ("oosPending", 3),
          ("outOfService", 2))
    )


_SonusTgOperState_Type.__name__ = "Integer32"
_SonusTgOperState_Object = MibTableColumn
sonusTgOperState = _SonusTgOperState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 3, 1, 2),
    _SonusTgOperState_Type()
)
sonusTgOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTgOperState.setStatus("current")
_SonusTgPstnTotalAvailable_Type = Integer32
_SonusTgPstnTotalAvailable_Object = MibTableColumn
sonusTgPstnTotalAvailable = _SonusTgPstnTotalAvailable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 3, 1, 3),
    _SonusTgPstnTotalAvailable_Type()
)
sonusTgPstnTotalAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTgPstnTotalAvailable.setStatus("current")
_SonusTgPstnTotalInboundRsv_Type = Integer32
_SonusTgPstnTotalInboundRsv_Object = MibTableColumn
sonusTgPstnTotalInboundRsv = _SonusTgPstnTotalInboundRsv_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 3, 1, 4),
    _SonusTgPstnTotalInboundRsv_Type()
)
sonusTgPstnTotalInboundRsv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTgPstnTotalInboundRsv.setStatus("current")
_SonusTgPstnInboundUsage_Type = Integer32
_SonusTgPstnInboundUsage_Object = MibTableColumn
sonusTgPstnInboundUsage = _SonusTgPstnInboundUsage_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 3, 1, 5),
    _SonusTgPstnInboundUsage_Type()
)
sonusTgPstnInboundUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTgPstnInboundUsage.setStatus("current")
_SonusTgPstnOutboundUsage_Type = Integer32
_SonusTgPstnOutboundUsage_Object = MibTableColumn
sonusTgPstnOutboundUsage = _SonusTgPstnOutboundUsage_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 3, 1, 6),
    _SonusTgPstnOutboundUsage_Type()
)
sonusTgPstnOutboundUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTgPstnOutboundUsage.setStatus("current")
_SonusTgPstnTotalConfigured_Type = Integer32
_SonusTgPstnTotalConfigured_Object = MibTableColumn
sonusTgPstnTotalConfigured = _SonusTgPstnTotalConfigured_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 3, 1, 7),
    _SonusTgPstnTotalConfigured_Type()
)
sonusTgPstnTotalConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTgPstnTotalConfigured.setStatus("current")
_SonusTgAccCurrentACL_Type = Integer32
_SonusTgAccCurrentACL_Object = MibTableColumn
sonusTgAccCurrentACL = _SonusTgAccCurrentACL_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 3, 1, 8),
    _SonusTgAccCurrentACL_Type()
)
sonusTgAccCurrentACL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTgAccCurrentACL.setStatus("current")
_SonusTgPriorityCallUsage_Type = Integer32
_SonusTgPriorityCallUsage_Object = MibTableColumn
sonusTgPriorityCallUsage = _SonusTgPriorityCallUsage_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 3, 1, 9),
    _SonusTgPriorityCallUsage_Type()
)
sonusTgPriorityCallUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTgPriorityCallUsage.setStatus("current")
_SonusTgSgTable_Object = MibTable
sonusTgSgTable = _SonusTgSgTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 4)
)
if mibBuilder.loadTexts:
    sonusTgSgTable.setStatus("current")
_SonusTgSgEntry_Object = MibTableRow
sonusTgSgEntry = _SonusTgSgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 4, 1)
)
sonusTgSgEntry.setIndexNames(
    (0, "SONUS-TRUNK-GROUP-RESOURCES-MIB", "sonusTgSgTgIndex"),
    (0, "SONUS-TRUNK-GROUP-RESOURCES-MIB", "sonusTgSgIndex"),
)
if mibBuilder.loadTexts:
    sonusTgSgEntry.setStatus("current")
_SonusTgSgTgIndex_Type = Integer32
_SonusTgSgTgIndex_Object = MibTableColumn
sonusTgSgTgIndex = _SonusTgSgTgIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 4, 1, 1),
    _SonusTgSgTgIndex_Type()
)
sonusTgSgTgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTgSgTgIndex.setStatus("current")
_SonusTgSgIndex_Type = Integer32
_SonusTgSgIndex_Object = MibTableColumn
sonusTgSgIndex = _SonusTgSgIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 4, 1, 2),
    _SonusTgSgIndex_Type()
)
sonusTgSgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTgSgIndex.setStatus("current")


class _SonusTgSgName_Type(DisplayString):
    """Custom type sonusTgSgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_SonusTgSgName_Type.__name__ = "DisplayString"
_SonusTgSgName_Object = MibTableColumn
sonusTgSgName = _SonusTgSgName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 4, 1, 3),
    _SonusTgSgName_Type()
)
sonusTgSgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTgSgName.setStatus("current")


class _SonusTgSgType_Type(Integer32):
    """Custom type sonusTgSgType based on Integer32"""
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
        *(("cas", 2),
          ("dedicated", 6),
          ("gateway", 5),
          ("h323", 4),
          ("isdn", 3),
          ("ras", 8),
          ("ss7", 1),
          ("twostagedial", 7))
    )


_SonusTgSgType_Type.__name__ = "Integer32"
_SonusTgSgType_Object = MibTableColumn
sonusTgSgType = _SonusTgSgType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 4, 1, 4),
    _SonusTgSgType_Type()
)
sonusTgSgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTgSgType.setStatus("current")
_SonusTgProfileObjects_ObjectIdentity = ObjectIdentity
sonusTgProfileObjects = _SonusTgProfileObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 5)
)
_SonusTgProfileNextIndex_Type = Integer32
_SonusTgProfileNextIndex_Object = MibScalar
sonusTgProfileNextIndex = _SonusTgProfileNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 5, 5),
    _SonusTgProfileNextIndex_Type()
)
sonusTgProfileNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTgProfileNextIndex.setStatus("current")
_SonusTgProfileTable_Object = MibTable
sonusTgProfileTable = _SonusTgProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 5, 6)
)
if mibBuilder.loadTexts:
    sonusTgProfileTable.setStatus("current")
_SonusTgProfileEntry_Object = MibTableRow
sonusTgProfileEntry = _SonusTgProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 5, 6, 1)
)
sonusTgProfileEntry.setIndexNames(
    (0, "SONUS-TRUNK-GROUP-RESOURCES-MIB", "sonusTgProfileIndex"),
)
if mibBuilder.loadTexts:
    sonusTgProfileEntry.setStatus("current")
_SonusTgProfileIndex_Type = Integer32
_SonusTgProfileIndex_Object = MibTableColumn
sonusTgProfileIndex = _SonusTgProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 5, 6, 1, 1),
    _SonusTgProfileIndex_Type()
)
sonusTgProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTgProfileIndex.setStatus("current")
_SonusTgProfileName_Type = SonusName
_SonusTgProfileName_Object = MibTableColumn
sonusTgProfileName = _SonusTgProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 5, 6, 1, 2),
    _SonusTgProfileName_Type()
)
sonusTgProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTgProfileName.setStatus("current")


class _SonusTgProfileSgSelect_Type(Integer32):
    """Custom type sonusTgProfileSgSelect based on Integer32"""
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
        *(("circularbackward", 4),
          ("circularforward", 3),
          ("configured", 2),
          ("leastcost", 1))
    )


_SonusTgProfileSgSelect_Type.__name__ = "Integer32"
_SonusTgProfileSgSelect_Object = MibTableColumn
sonusTgProfileSgSelect = _SonusTgProfileSgSelect_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 5, 6, 1, 3),
    _SonusTgProfileSgSelect_Type()
)
sonusTgProfileSgSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTgProfileSgSelect.setStatus("current")


class _SonusTgProfileAdminState_Type(Integer32):
    """Custom type sonusTgProfileAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SonusTgProfileAdminState_Type.__name__ = "Integer32"
_SonusTgProfileAdminState_Object = MibTableColumn
sonusTgProfileAdminState = _SonusTgProfileAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 5, 6, 1, 4),
    _SonusTgProfileAdminState_Type()
)
sonusTgProfileAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTgProfileAdminState.setStatus("current")


class _SonusTgProfileInboundReserved_Type(Integer32):
    """Custom type sonusTgProfileInboundReserved based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SonusTgProfileInboundReserved_Type.__name__ = "Integer32"
_SonusTgProfileInboundReserved_Object = MibTableColumn
sonusTgProfileInboundReserved = _SonusTgProfileInboundReserved_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 5, 6, 1, 5),
    _SonusTgProfileInboundReserved_Type()
)
sonusTgProfileInboundReserved.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTgProfileInboundReserved.setStatus("current")
_SonusTgProfileLnpTranslate_Type = SonusBoolean
_SonusTgProfileLnpTranslate_Object = MibTableColumn
sonusTgProfileLnpTranslate = _SonusTgProfileLnpTranslate_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 5, 6, 1, 6),
    _SonusTgProfileLnpTranslate_Type()
)
sonusTgProfileLnpTranslate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTgProfileLnpTranslate.setStatus("current")
_SonusTgProfile800Translate_Type = SonusBoolean
_SonusTgProfile800Translate_Object = MibTableColumn
sonusTgProfile800Translate = _SonusTgProfile800Translate_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 5, 6, 1, 7),
    _SonusTgProfile800Translate_Type()
)
sonusTgProfile800Translate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTgProfile800Translate.setStatus("current")
_SonusTgProfileCallingNumVerify_Type = SonusBoolean
_SonusTgProfileCallingNumVerify_Object = MibTableColumn
sonusTgProfileCallingNumVerify = _SonusTgProfileCallingNumVerify_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 5, 6, 1, 8),
    _SonusTgProfileCallingNumVerify_Type()
)
sonusTgProfileCallingNumVerify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTgProfileCallingNumVerify.setStatus("current")
_SonusTgProfileIsupOnly_Type = SonusBoolean
_SonusTgProfileIsupOnly_Object = MibTableColumn
sonusTgProfileIsupOnly = _SonusTgProfileIsupOnly_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 5, 6, 1, 9),
    _SonusTgProfileIsupOnly_Type()
)
sonusTgProfileIsupOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTgProfileIsupOnly.setStatus("current")


class _SonusTgProfileCarrier_Type(DisplayString):
    """Custom type sonusTgProfileCarrier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_SonusTgProfileCarrier_Type.__name__ = "DisplayString"
_SonusTgProfileCarrier_Object = MibTableColumn
sonusTgProfileCarrier = _SonusTgProfileCarrier_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 5, 6, 1, 10),
    _SonusTgProfileCarrier_Type()
)
sonusTgProfileCarrier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTgProfileCarrier.setStatus("current")


class _SonusTgProfileIsupNode_Type(DisplayString):
    """Custom type sonusTgProfileIsupNode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_SonusTgProfileIsupNode_Type.__name__ = "DisplayString"
_SonusTgProfileIsupNode_Object = MibTableColumn
sonusTgProfileIsupNode = _SonusTgProfileIsupNode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 5, 6, 1, 11),
    _SonusTgProfileIsupNode_Type()
)
sonusTgProfileIsupNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTgProfileIsupNode.setStatus("current")


class _SonusTgProfSgSelectState_Type(Integer32):
    """Custom type sonusTgProfSgSelectState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SonusTgProfSgSelectState_Type.__name__ = "Integer32"
_SonusTgProfSgSelectState_Object = MibTableColumn
sonusTgProfSgSelectState = _SonusTgProfSgSelectState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 5, 6, 1, 12),
    _SonusTgProfSgSelectState_Type()
)
sonusTgProfSgSelectState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTgProfSgSelectState.setStatus("current")


class _SonusTgProfInboundReservedState_Type(Integer32):
    """Custom type sonusTgProfInboundReservedState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SonusTgProfInboundReservedState_Type.__name__ = "Integer32"
_SonusTgProfInboundReservedState_Object = MibTableColumn
sonusTgProfInboundReservedState = _SonusTgProfInboundReservedState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 5, 6, 1, 13),
    _SonusTgProfInboundReservedState_Type()
)
sonusTgProfInboundReservedState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTgProfInboundReservedState.setStatus("current")


class _SonusTgProfLnpTranslateState_Type(Integer32):
    """Custom type sonusTgProfLnpTranslateState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SonusTgProfLnpTranslateState_Type.__name__ = "Integer32"
_SonusTgProfLnpTranslateState_Object = MibTableColumn
sonusTgProfLnpTranslateState = _SonusTgProfLnpTranslateState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 5, 6, 1, 14),
    _SonusTgProfLnpTranslateState_Type()
)
sonusTgProfLnpTranslateState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTgProfLnpTranslateState.setStatus("current")


class _SonusTgProf800TranslateState_Type(Integer32):
    """Custom type sonusTgProf800TranslateState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SonusTgProf800TranslateState_Type.__name__ = "Integer32"
_SonusTgProf800TranslateState_Object = MibTableColumn
sonusTgProf800TranslateState = _SonusTgProf800TranslateState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 5, 6, 1, 15),
    _SonusTgProf800TranslateState_Type()
)
sonusTgProf800TranslateState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTgProf800TranslateState.setStatus("current")


class _SonusTgProfCallingNumVerifyState_Type(Integer32):
    """Custom type sonusTgProfCallingNumVerifyState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SonusTgProfCallingNumVerifyState_Type.__name__ = "Integer32"
_SonusTgProfCallingNumVerifyState_Object = MibTableColumn
sonusTgProfCallingNumVerifyState = _SonusTgProfCallingNumVerifyState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 5, 6, 1, 16),
    _SonusTgProfCallingNumVerifyState_Type()
)
sonusTgProfCallingNumVerifyState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTgProfCallingNumVerifyState.setStatus("current")


class _SonusTgProfIsupOnlyState_Type(Integer32):
    """Custom type sonusTgProfIsupOnlyState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SonusTgProfIsupOnlyState_Type.__name__ = "Integer32"
_SonusTgProfIsupOnlyState_Object = MibTableColumn
sonusTgProfIsupOnlyState = _SonusTgProfIsupOnlyState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 5, 6, 1, 17),
    _SonusTgProfIsupOnlyState_Type()
)
sonusTgProfIsupOnlyState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTgProfIsupOnlyState.setStatus("current")


class _SonusTgProfCarrierState_Type(Integer32):
    """Custom type sonusTgProfCarrierState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SonusTgProfCarrierState_Type.__name__ = "Integer32"
_SonusTgProfCarrierState_Object = MibTableColumn
sonusTgProfCarrierState = _SonusTgProfCarrierState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 5, 6, 1, 18),
    _SonusTgProfCarrierState_Type()
)
sonusTgProfCarrierState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTgProfCarrierState.setStatus("current")


class _SonusTgProfIsupNodeState_Type(Integer32):
    """Custom type sonusTgProfIsupNodeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SonusTgProfIsupNodeState_Type.__name__ = "Integer32"
_SonusTgProfIsupNodeState_Object = MibTableColumn
sonusTgProfIsupNodeState = _SonusTgProfIsupNodeState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 5, 6, 1, 19),
    _SonusTgProfIsupNodeState_Type()
)
sonusTgProfIsupNodeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTgProfIsupNodeState.setStatus("current")
_SonusTgProfileRowStatus_Type = RowStatus
_SonusTgProfileRowStatus_Object = MibTableColumn
sonusTgProfileRowStatus = _SonusTgProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 1, 5, 6, 1, 20),
    _SonusTgProfileRowStatus_Type()
)
sonusTgProfileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTgProfileRowStatus.setStatus("current")
_SonusGatewayObjects_ObjectIdentity = ObjectIdentity
sonusGatewayObjects = _SonusGatewayObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 2)
)
_SonusGatewayConfigObjects_ObjectIdentity = ObjectIdentity
sonusGatewayConfigObjects = _SonusGatewayConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 2, 1)
)


class _SonusTgMaxGateways_Type(Integer32):
    """Custom type sonusTgMaxGateways based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_SonusTgMaxGateways_Type.__name__ = "Integer32"
_SonusTgMaxGateways_Object = MibScalar
sonusTgMaxGateways = _SonusTgMaxGateways_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 2, 1, 1),
    _SonusTgMaxGateways_Type()
)
sonusTgMaxGateways.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTgMaxGateways.setStatus("current")
_SonusDestGatewayObjects_ObjectIdentity = ObjectIdentity
sonusDestGatewayObjects = _SonusDestGatewayObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 2, 2)
)
_SonusGatewayNextIndex_Type = Integer32
_SonusGatewayNextIndex_Object = MibScalar
sonusGatewayNextIndex = _SonusGatewayNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 2, 2, 1),
    _SonusGatewayNextIndex_Type()
)
sonusGatewayNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusGatewayNextIndex.setStatus("current")
_SonusGatewayTable_Object = MibTable
sonusGatewayTable = _SonusGatewayTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    sonusGatewayTable.setStatus("current")
_SonusGatewayEntry_Object = MibTableRow
sonusGatewayEntry = _SonusGatewayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 2, 2, 2, 1)
)
sonusGatewayEntry.setIndexNames(
    (0, "SONUS-TRUNK-GROUP-RESOURCES-MIB", "sonusGatewayIndex"),
)
if mibBuilder.loadTexts:
    sonusGatewayEntry.setStatus("current")
_SonusGatewayIndex_Type = Integer32
_SonusGatewayIndex_Object = MibTableColumn
sonusGatewayIndex = _SonusGatewayIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 2, 2, 2, 1, 1),
    _SonusGatewayIndex_Type()
)
sonusGatewayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusGatewayIndex.setStatus("current")
_SonusGatewayName_Type = SonusName
_SonusGatewayName_Object = MibTableColumn
sonusGatewayName = _SonusGatewayName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 2, 2, 2, 1, 2),
    _SonusGatewayName_Type()
)
sonusGatewayName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusGatewayName.setStatus("current")


class _SonusGatewayProfName_Type(DisplayString):
    """Custom type sonusGatewayProfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_SonusGatewayProfName_Type.__name__ = "DisplayString"
_SonusGatewayProfName_Object = MibTableColumn
sonusGatewayProfName = _SonusGatewayProfName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 2, 2, 2, 1, 3),
    _SonusGatewayProfName_Type()
)
sonusGatewayProfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusGatewayProfName.setStatus("current")


class _SonusGatewayType_Type(Integer32):
    """Custom type sonusGatewayType based on Integer32"""
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
        *(("gsx9000", 1),
          ("h323", 2),
          ("sip", 3))
    )


_SonusGatewayType_Type.__name__ = "Integer32"
_SonusGatewayType_Object = MibTableColumn
sonusGatewayType = _SonusGatewayType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 2, 2, 2, 1, 4),
    _SonusGatewayType_Type()
)
sonusGatewayType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusGatewayType.setStatus("current")
_SonusGatewayIpAddress_Type = IpAddress
_SonusGatewayIpAddress_Object = MibTableColumn
sonusGatewayIpAddress = _SonusGatewayIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 2, 2, 2, 1, 5),
    _SonusGatewayIpAddress_Type()
)
sonusGatewayIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusGatewayIpAddress.setStatus("current")


class _SonusGatewayPortNum_Type(Integer32):
    """Custom type sonusGatewayPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonusGatewayPortNum_Type.__name__ = "Integer32"
_SonusGatewayPortNum_Object = MibTableColumn
sonusGatewayPortNum = _SonusGatewayPortNum_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 2, 2, 2, 1, 6),
    _SonusGatewayPortNum_Type()
)
sonusGatewayPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusGatewayPortNum.setStatus("current")


class _SonusGatewayMaxConn_Type(Integer32):
    """Custom type sonusGatewayMaxConn based on Integer32"""
    defaultValue = 20000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20000),
    )


_SonusGatewayMaxConn_Type.__name__ = "Integer32"
_SonusGatewayMaxConn_Object = MibTableColumn
sonusGatewayMaxConn = _SonusGatewayMaxConn_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 2, 2, 2, 1, 7),
    _SonusGatewayMaxConn_Type()
)
sonusGatewayMaxConn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusGatewayMaxConn.setStatus("current")


class _SonusGatewayAdminState_Type(Integer32):
    """Custom type sonusGatewayAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SonusGatewayAdminState_Type.__name__ = "Integer32"
_SonusGatewayAdminState_Object = MibTableColumn
sonusGatewayAdminState = _SonusGatewayAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 2, 2, 2, 1, 8),
    _SonusGatewayAdminState_Type()
)
sonusGatewayAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusGatewayAdminState.setStatus("current")
_SonusGatewayRowStatus_Type = RowStatus
_SonusGatewayRowStatus_Object = MibTableColumn
sonusGatewayRowStatus = _SonusGatewayRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 2, 2, 2, 1, 9),
    _SonusGatewayRowStatus_Type()
)
sonusGatewayRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusGatewayRowStatus.setStatus("current")
_SonusDestGatewayStatusObjects_ObjectIdentity = ObjectIdentity
sonusDestGatewayStatusObjects = _SonusDestGatewayStatusObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 2, 3)
)
_SonusGwStatusTable_Object = MibTable
sonusGwStatusTable = _SonusGwStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 2, 3, 3)
)
if mibBuilder.loadTexts:
    sonusGwStatusTable.setStatus("current")
_SonusGwStatusEntry_Object = MibTableRow
sonusGwStatusEntry = _SonusGwStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 2, 3, 3, 1)
)
sonusGwStatusEntry.setIndexNames(
    (0, "SONUS-TRUNK-GROUP-RESOURCES-MIB", "sonusGwStatusIndex"),
)
if mibBuilder.loadTexts:
    sonusGwStatusEntry.setStatus("current")
_SonusGwStatusIndex_Type = Integer32
_SonusGwStatusIndex_Object = MibTableColumn
sonusGwStatusIndex = _SonusGwStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 2, 3, 3, 1, 1),
    _SonusGwStatusIndex_Type()
)
sonusGwStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusGwStatusIndex.setStatus("current")
_SonusGwCurrConnections_Type = Integer32
_SonusGwCurrConnections_Object = MibTableColumn
sonusGwCurrConnections = _SonusGwCurrConnections_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 2, 3, 3, 1, 2),
    _SonusGwCurrConnections_Type()
)
sonusGwCurrConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusGwCurrConnections.setStatus("current")
_SonusCarrierObjects_ObjectIdentity = ObjectIdentity
sonusCarrierObjects = _SonusCarrierObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 3)
)
_SonusCarrierConfigObjects_ObjectIdentity = ObjectIdentity
sonusCarrierConfigObjects = _SonusCarrierConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 3, 1)
)


class _SonusTgMaxCarrierCodes_Type(Integer32):
    """Custom type sonusTgMaxCarrierCodes based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonusTgMaxCarrierCodes_Type.__name__ = "Integer32"
_SonusTgMaxCarrierCodes_Object = MibScalar
sonusTgMaxCarrierCodes = _SonusTgMaxCarrierCodes_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 3, 1, 1),
    _SonusTgMaxCarrierCodes_Type()
)
sonusTgMaxCarrierCodes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTgMaxCarrierCodes.setStatus("current")
_SonusCarrierCodeObjects_ObjectIdentity = ObjectIdentity
sonusCarrierCodeObjects = _SonusCarrierCodeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 3, 2)
)
_SonusCarrierCodeNextIndex_Type = Integer32
_SonusCarrierCodeNextIndex_Object = MibScalar
sonusCarrierCodeNextIndex = _SonusCarrierCodeNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 3, 2, 1),
    _SonusCarrierCodeNextIndex_Type()
)
sonusCarrierCodeNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCarrierCodeNextIndex.setStatus("current")
_SonusCarrierCodeTable_Object = MibTable
sonusCarrierCodeTable = _SonusCarrierCodeTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    sonusCarrierCodeTable.setStatus("current")
_SonusCarrierCodeEntry_Object = MibTableRow
sonusCarrierCodeEntry = _SonusCarrierCodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 3, 2, 2, 1)
)
sonusCarrierCodeEntry.setIndexNames(
    (0, "SONUS-TRUNK-GROUP-RESOURCES-MIB", "sonusCarrierCodeIndex"),
)
if mibBuilder.loadTexts:
    sonusCarrierCodeEntry.setStatus("current")
_SonusCarrierCodeIndex_Type = Integer32
_SonusCarrierCodeIndex_Object = MibTableColumn
sonusCarrierCodeIndex = _SonusCarrierCodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 3, 2, 2, 1, 1),
    _SonusCarrierCodeIndex_Type()
)
sonusCarrierCodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCarrierCodeIndex.setStatus("current")
_SonusCarrierCodeName_Type = SonusName
_SonusCarrierCodeName_Object = MibTableColumn
sonusCarrierCodeName = _SonusCarrierCodeName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 3, 2, 2, 1, 2),
    _SonusCarrierCodeName_Type()
)
sonusCarrierCodeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCarrierCodeName.setStatus("current")


class _SonusCarrierCode_Type(DisplayString):
    """Custom type sonusCarrierCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_SonusCarrierCode_Type.__name__ = "DisplayString"
_SonusCarrierCode_Object = MibTableColumn
sonusCarrierCode = _SonusCarrierCode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 3, 2, 2, 1, 3),
    _SonusCarrierCode_Type()
)
sonusCarrierCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCarrierCode.setStatus("current")


class _SonusCarrierCodeAdminState_Type(Integer32):
    """Custom type sonusCarrierCodeAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SonusCarrierCodeAdminState_Type.__name__ = "Integer32"
_SonusCarrierCodeAdminState_Object = MibTableColumn
sonusCarrierCodeAdminState = _SonusCarrierCodeAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 3, 2, 2, 1, 4),
    _SonusCarrierCodeAdminState_Type()
)
sonusCarrierCodeAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCarrierCodeAdminState.setStatus("current")
_SonusCarrierCodeRowStatus_Type = RowStatus
_SonusCarrierCodeRowStatus_Object = MibTableColumn
sonusCarrierCodeRowStatus = _SonusCarrierCodeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 3, 2, 2, 1, 5),
    _SonusCarrierCodeRowStatus_Type()
)
sonusCarrierCodeRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCarrierCodeRowStatus.setStatus("current")


class _SonusCarrierCodeNetworkIdType_Type(Integer32):
    """Custom type sonusCarrierCodeNetworkIdType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ccitt", 1),
          ("national", 2),
          ("other", 3))
    )


_SonusCarrierCodeNetworkIdType_Type.__name__ = "Integer32"
_SonusCarrierCodeNetworkIdType_Object = MibTableColumn
sonusCarrierCodeNetworkIdType = _SonusCarrierCodeNetworkIdType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 3, 2, 2, 1, 6),
    _SonusCarrierCodeNetworkIdType_Type()
)
sonusCarrierCodeNetworkIdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCarrierCodeNetworkIdType.setStatus("current")


class _SonusCarrierCodeNetworkIdPlan_Type(Integer32):
    """Custom type sonusCarrierCodeNetworkIdPlan based on Integer32"""
    defaultValue = 8

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
        *(("ccittlandmobilenetwork", 3),
          ("ccittpublicdatanetwork", 2),
          ("ccittreserved1", 4),
          ("ccittreserved2", 5),
          ("ccittunknown", 1),
          ("national3digitcarriercode", 7),
          ("national4digitcarriercode", 8),
          ("nationalreserved1", 9),
          ("nationalreserved2", 10),
          ("nationalunknown", 6))
    )


_SonusCarrierCodeNetworkIdPlan_Type.__name__ = "Integer32"
_SonusCarrierCodeNetworkIdPlan_Object = MibTableColumn
sonusCarrierCodeNetworkIdPlan = _SonusCarrierCodeNetworkIdPlan_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 1, 3, 2, 2, 1, 7),
    _SonusCarrierCodeNetworkIdPlan_Type()
)
sonusCarrierCodeNetworkIdPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCarrierCodeNetworkIdPlan.setStatus("current")
_SonusTrunkGroupResourcesMIBNotifications_ObjectIdentity = ObjectIdentity
sonusTrunkGroupResourcesMIBNotifications = _SonusTrunkGroupResourcesMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 2)
)
_SonusTrunkGroupResourcesMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
sonusTrunkGroupResourcesMIBNotificationsPrefix = _SonusTrunkGroupResourcesMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 2, 0)
)
_SonusTrunkGroupResourcesMIBNotificationsObjects_ObjectIdentity = ObjectIdentity
sonusTrunkGroupResourcesMIBNotificationsObjects = _SonusTrunkGroupResourcesMIBNotificationsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 2, 1)
)


class _SonusTrunkOutOfServiceReason_Type(Integer32):
    """Custom type sonusTrunkOutOfServiceReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allResourcesBlocked", 2),
          ("configured", 1))
    )


_SonusTrunkOutOfServiceReason_Type.__name__ = "Integer32"
_SonusTrunkOutOfServiceReason_Object = MibScalar
sonusTrunkOutOfServiceReason = _SonusTrunkOutOfServiceReason_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 2, 1, 1),
    _SonusTrunkOutOfServiceReason_Type()
)
sonusTrunkOutOfServiceReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTrunkOutOfServiceReason.setStatus("current")

# Managed Objects groups


# Notification objects

sonusTrunkEnabledNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 2, 0, 1)
)
sonusTrunkEnabledNotification.setObjects(
      *(("SONUS-TRUNK-GROUP-RESOURCES-MIB", "sonusTgName"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusTrunkEnabledNotification.setStatus(
        "current"
    )

sonusTrunkDisabledNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 2, 0, 2)
)
sonusTrunkDisabledNotification.setObjects(
      *(("SONUS-TRUNK-GROUP-RESOURCES-MIB", "sonusTgName"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusTrunkDisabledNotification.setStatus(
        "current"
    )

sonusTrunkInServiceNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 2, 0, 3)
)
sonusTrunkInServiceNotification.setObjects(
      *(("SONUS-TRUNK-GROUP-RESOURCES-MIB", "sonusTgName"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusTrunkInServiceNotification.setStatus(
        "current"
    )

sonusTrunkOutOfServiceNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 2, 0, 4)
)
sonusTrunkOutOfServiceNotification.setObjects(
      *(("SONUS-TRUNK-GROUP-RESOURCES-MIB", "sonusTgName"),
        ("SONUS-TRUNK-GROUP-RESOURCES-MIB", "sonusTrunkOutOfServiceReason"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusTrunkOutOfServiceNotification.setStatus(
        "current"
    )

sonusTrunkDeletedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 3, 2, 0, 5)
)
sonusTrunkDeletedNotification.setObjects(
      *(("SONUS-TRUNK-GROUP-RESOURCES-MIB", "sonusTgName"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusTrunkDeletedNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONUS-TRUNK-GROUP-RESOURCES-MIB",
    **{"sonusTrunkGroupResourcesMIB": sonusTrunkGroupResourcesMIB,
       "sonusTrunkGroupResourcesMIBObjects": sonusTrunkGroupResourcesMIBObjects,
       "sonusTrunkObjects": sonusTrunkObjects,
       "sonusTrunkConfigObjects": sonusTrunkConfigObjects,
       "sonusTgMaxRpcLpcs": sonusTgMaxRpcLpcs,
       "sonusTgMaxCics": sonusTgMaxCics,
       "sonusTgMaxTrunkGroups": sonusTgMaxTrunkGroups,
       "sonusTgMaxServiceGroups": sonusTgMaxServiceGroups,
       "sonusTgMaxSgInstances": sonusTgMaxSgInstances,
       "sonusTgObjects": sonusTgObjects,
       "sonusTgNextIndex": sonusTgNextIndex,
       "sonusTgTable": sonusTgTable,
       "sonusTgEntry": sonusTgEntry,
       "sonusTgIndex": sonusTgIndex,
       "sonusTgName": sonusTgName,
       "sonusTgProfName": sonusTgProfName,
       "sonusTgSgSelect": sonusTgSgSelect,
       "sonusTgLnpTranslate": sonusTgLnpTranslate,
       "sonusTg800Translate": sonusTg800Translate,
       "sonusTgCallingNumVerify": sonusTgCallingNumVerify,
       "sonusTgInboundReserved": sonusTgInboundReserved,
       "sonusTgIsupOnly": sonusTgIsupOnly,
       "sonusTgCarrier": sonusTgCarrier,
       "sonusTgIsupNode": sonusTgIsupNode,
       "sonusTgAdminState": sonusTgAdminState,
       "sonusTgMode": sonusTgMode,
       "sonusTgAction": sonusTgAction,
       "sonusTgTimeout": sonusTgTimeout,
       "sonusTgRowStatus": sonusTgRowStatus,
       "sonusTgCirResvState": sonusTgCirResvState,
       "sonusTgPriorityCallReserve": sonusTgPriorityCallReserve,
       "sonusTgIncomingCallReserve": sonusTgIncomingCallReserve,
       "sonusTgOutgoingCallReserve": sonusTgOutgoingCallReserve,
       "sonusTgStatusTable": sonusTgStatusTable,
       "sonusTgStatusEntry": sonusTgStatusEntry,
       "sonusTgStatusIndex": sonusTgStatusIndex,
       "sonusTgOperState": sonusTgOperState,
       "sonusTgPstnTotalAvailable": sonusTgPstnTotalAvailable,
       "sonusTgPstnTotalInboundRsv": sonusTgPstnTotalInboundRsv,
       "sonusTgPstnInboundUsage": sonusTgPstnInboundUsage,
       "sonusTgPstnOutboundUsage": sonusTgPstnOutboundUsage,
       "sonusTgPstnTotalConfigured": sonusTgPstnTotalConfigured,
       "sonusTgAccCurrentACL": sonusTgAccCurrentACL,
       "sonusTgPriorityCallUsage": sonusTgPriorityCallUsage,
       "sonusTgSgTable": sonusTgSgTable,
       "sonusTgSgEntry": sonusTgSgEntry,
       "sonusTgSgTgIndex": sonusTgSgTgIndex,
       "sonusTgSgIndex": sonusTgSgIndex,
       "sonusTgSgName": sonusTgSgName,
       "sonusTgSgType": sonusTgSgType,
       "sonusTgProfileObjects": sonusTgProfileObjects,
       "sonusTgProfileNextIndex": sonusTgProfileNextIndex,
       "sonusTgProfileTable": sonusTgProfileTable,
       "sonusTgProfileEntry": sonusTgProfileEntry,
       "sonusTgProfileIndex": sonusTgProfileIndex,
       "sonusTgProfileName": sonusTgProfileName,
       "sonusTgProfileSgSelect": sonusTgProfileSgSelect,
       "sonusTgProfileAdminState": sonusTgProfileAdminState,
       "sonusTgProfileInboundReserved": sonusTgProfileInboundReserved,
       "sonusTgProfileLnpTranslate": sonusTgProfileLnpTranslate,
       "sonusTgProfile800Translate": sonusTgProfile800Translate,
       "sonusTgProfileCallingNumVerify": sonusTgProfileCallingNumVerify,
       "sonusTgProfileIsupOnly": sonusTgProfileIsupOnly,
       "sonusTgProfileCarrier": sonusTgProfileCarrier,
       "sonusTgProfileIsupNode": sonusTgProfileIsupNode,
       "sonusTgProfSgSelectState": sonusTgProfSgSelectState,
       "sonusTgProfInboundReservedState": sonusTgProfInboundReservedState,
       "sonusTgProfLnpTranslateState": sonusTgProfLnpTranslateState,
       "sonusTgProf800TranslateState": sonusTgProf800TranslateState,
       "sonusTgProfCallingNumVerifyState": sonusTgProfCallingNumVerifyState,
       "sonusTgProfIsupOnlyState": sonusTgProfIsupOnlyState,
       "sonusTgProfCarrierState": sonusTgProfCarrierState,
       "sonusTgProfIsupNodeState": sonusTgProfIsupNodeState,
       "sonusTgProfileRowStatus": sonusTgProfileRowStatus,
       "sonusGatewayObjects": sonusGatewayObjects,
       "sonusGatewayConfigObjects": sonusGatewayConfigObjects,
       "sonusTgMaxGateways": sonusTgMaxGateways,
       "sonusDestGatewayObjects": sonusDestGatewayObjects,
       "sonusGatewayNextIndex": sonusGatewayNextIndex,
       "sonusGatewayTable": sonusGatewayTable,
       "sonusGatewayEntry": sonusGatewayEntry,
       "sonusGatewayIndex": sonusGatewayIndex,
       "sonusGatewayName": sonusGatewayName,
       "sonusGatewayProfName": sonusGatewayProfName,
       "sonusGatewayType": sonusGatewayType,
       "sonusGatewayIpAddress": sonusGatewayIpAddress,
       "sonusGatewayPortNum": sonusGatewayPortNum,
       "sonusGatewayMaxConn": sonusGatewayMaxConn,
       "sonusGatewayAdminState": sonusGatewayAdminState,
       "sonusGatewayRowStatus": sonusGatewayRowStatus,
       "sonusDestGatewayStatusObjects": sonusDestGatewayStatusObjects,
       "sonusGwStatusTable": sonusGwStatusTable,
       "sonusGwStatusEntry": sonusGwStatusEntry,
       "sonusGwStatusIndex": sonusGwStatusIndex,
       "sonusGwCurrConnections": sonusGwCurrConnections,
       "sonusCarrierObjects": sonusCarrierObjects,
       "sonusCarrierConfigObjects": sonusCarrierConfigObjects,
       "sonusTgMaxCarrierCodes": sonusTgMaxCarrierCodes,
       "sonusCarrierCodeObjects": sonusCarrierCodeObjects,
       "sonusCarrierCodeNextIndex": sonusCarrierCodeNextIndex,
       "sonusCarrierCodeTable": sonusCarrierCodeTable,
       "sonusCarrierCodeEntry": sonusCarrierCodeEntry,
       "sonusCarrierCodeIndex": sonusCarrierCodeIndex,
       "sonusCarrierCodeName": sonusCarrierCodeName,
       "sonusCarrierCode": sonusCarrierCode,
       "sonusCarrierCodeAdminState": sonusCarrierCodeAdminState,
       "sonusCarrierCodeRowStatus": sonusCarrierCodeRowStatus,
       "sonusCarrierCodeNetworkIdType": sonusCarrierCodeNetworkIdType,
       "sonusCarrierCodeNetworkIdPlan": sonusCarrierCodeNetworkIdPlan,
       "sonusTrunkGroupResourcesMIBNotifications": sonusTrunkGroupResourcesMIBNotifications,
       "sonusTrunkGroupResourcesMIBNotificationsPrefix": sonusTrunkGroupResourcesMIBNotificationsPrefix,
       "sonusTrunkEnabledNotification": sonusTrunkEnabledNotification,
       "sonusTrunkDisabledNotification": sonusTrunkDisabledNotification,
       "sonusTrunkInServiceNotification": sonusTrunkInServiceNotification,
       "sonusTrunkOutOfServiceNotification": sonusTrunkOutOfServiceNotification,
       "sonusTrunkDeletedNotification": sonusTrunkDeletedNotification,
       "sonusTrunkGroupResourcesMIBNotificationsObjects": sonusTrunkGroupResourcesMIBNotificationsObjects,
       "sonusTrunkOutOfServiceReason": sonusTrunkOutOfServiceReason}
)
