# SNMP MIB module (TIMETRA-BFD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIMETRA-BFD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:55 2024
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
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(TNamedItem,) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TNamedItem")


# MODULE-IDENTITY

timetraBfdMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 85)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TmnxBfdConformance_ObjectIdentity = ObjectIdentity
tmnxBfdConformance = _TmnxBfdConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 85)
)
_TmnxBfdCompliances_ObjectIdentity = ObjectIdentity
tmnxBfdCompliances = _TmnxBfdCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 85, 1)
)
_TmnxBfdGroups_ObjectIdentity = ObjectIdentity
tmnxBfdGroups = _TmnxBfdGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 85, 2)
)
_TmnxBfdObjects_ObjectIdentity = ObjectIdentity
tmnxBfdObjects = _TmnxBfdObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85)
)
_TmnxBfdOperObjects_ObjectIdentity = ObjectIdentity
tmnxBfdOperObjects = _TmnxBfdOperObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 1)
)
_TmnxBfdOperValueObjects_ObjectIdentity = ObjectIdentity
tmnxBfdOperValueObjects = _TmnxBfdOperValueObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 1, 1)
)
_TmnxBfdOperTemplateTable_Object = MibTable
tmnxBfdOperTemplateTable = _TmnxBfdOperTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxBfdOperTemplateTable.setStatus("current")
_TmnxBfdOperTemplateEntry_Object = MibTableRow
tmnxBfdOperTemplateEntry = _TmnxBfdOperTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 1, 1, 1, 1)
)
tmnxBfdOperTemplateEntry.setIndexNames(
    (0, "TIMETRA-BFD-MIB", "tmnxBfdOperTemplateName"),
)
if mibBuilder.loadTexts:
    tmnxBfdOperTemplateEntry.setStatus("current")
_TmnxBfdOperTemplateName_Type = TNamedItem
_TmnxBfdOperTemplateName_Object = MibTableColumn
tmnxBfdOperTemplateName = _TmnxBfdOperTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 1, 1, 1, 1, 1),
    _TmnxBfdOperTemplateName_Type()
)
tmnxBfdOperTemplateName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBfdOperTemplateName.setStatus("current")
_TmnxBfdOperTemplateRowStatus_Type = RowStatus
_TmnxBfdOperTemplateRowStatus_Object = MibTableColumn
tmnxBfdOperTemplateRowStatus = _TmnxBfdOperTemplateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 1, 1, 1, 1, 2),
    _TmnxBfdOperTemplateRowStatus_Type()
)
tmnxBfdOperTemplateRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBfdOperTemplateRowStatus.setStatus("current")


class _TmnxBfdOperTemplateTxInt_Type(Unsigned32):
    """Custom type tmnxBfdOperTemplateTxInt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100000),
    )


_TmnxBfdOperTemplateTxInt_Type.__name__ = "Unsigned32"
_TmnxBfdOperTemplateTxInt_Object = MibTableColumn
tmnxBfdOperTemplateTxInt = _TmnxBfdOperTemplateTxInt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 1, 1, 1, 1, 3),
    _TmnxBfdOperTemplateTxInt_Type()
)
tmnxBfdOperTemplateTxInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBfdOperTemplateTxInt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBfdOperTemplateTxInt.setUnits("milliseconds")


class _TmnxBfdOperTemplateRxInt_Type(Unsigned32):
    """Custom type tmnxBfdOperTemplateRxInt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100000),
    )


_TmnxBfdOperTemplateRxInt_Type.__name__ = "Unsigned32"
_TmnxBfdOperTemplateRxInt_Object = MibTableColumn
tmnxBfdOperTemplateRxInt = _TmnxBfdOperTemplateRxInt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 1, 1, 1, 1, 4),
    _TmnxBfdOperTemplateRxInt_Type()
)
tmnxBfdOperTemplateRxInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBfdOperTemplateRxInt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBfdOperTemplateRxInt.setUnits("milliseconds")


class _TmnxBfdOperTemplateMultiplier_Type(Unsigned32):
    """Custom type tmnxBfdOperTemplateMultiplier based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 20),
    )


_TmnxBfdOperTemplateMultiplier_Type.__name__ = "Unsigned32"
_TmnxBfdOperTemplateMultiplier_Object = MibTableColumn
tmnxBfdOperTemplateMultiplier = _TmnxBfdOperTemplateMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 1, 1, 1, 1, 5),
    _TmnxBfdOperTemplateMultiplier_Type()
)
tmnxBfdOperTemplateMultiplier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBfdOperTemplateMultiplier.setStatus("current")


class _TmnxBfdOperTemplateEchoRxInt_Type(Unsigned32):
    """Custom type tmnxBfdOperTemplateEchoRxInt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 100000),
    )


_TmnxBfdOperTemplateEchoRxInt_Type.__name__ = "Unsigned32"
_TmnxBfdOperTemplateEchoRxInt_Object = MibTableColumn
tmnxBfdOperTemplateEchoRxInt = _TmnxBfdOperTemplateEchoRxInt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 1, 1, 1, 1, 6),
    _TmnxBfdOperTemplateEchoRxInt_Type()
)
tmnxBfdOperTemplateEchoRxInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBfdOperTemplateEchoRxInt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBfdOperTemplateEchoRxInt.setUnits("milliseconds")


class _TmnxBfdOperTemplateType_Type(Integer32):
    """Custom type tmnxBfdOperTemplateType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("cpmNp", 1),
          ("iomHw", 3))
    )


_TmnxBfdOperTemplateType_Type.__name__ = "Integer32"
_TmnxBfdOperTemplateType_Object = MibTableColumn
tmnxBfdOperTemplateType = _TmnxBfdOperTemplateType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 1, 1, 1, 1, 7),
    _TmnxBfdOperTemplateType_Type()
)
tmnxBfdOperTemplateType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBfdOperTemplateType.setStatus("current")
_TmnxBfdAdminObjects_ObjectIdentity = ObjectIdentity
tmnxBfdAdminObjects = _TmnxBfdAdminObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 2)
)
_TmnxBfdAdminControlObjects_ObjectIdentity = ObjectIdentity
tmnxBfdAdminControlObjects = _TmnxBfdAdminControlObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 2, 1)
)


class _TmnxBfdAdminOwner_Type(DisplayString):
    """Custom type tmnxBfdAdminOwner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TmnxBfdAdminOwner_Type.__name__ = "DisplayString"
_TmnxBfdAdminOwner_Object = MibScalar
tmnxBfdAdminOwner = _TmnxBfdAdminOwner_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 2, 1, 1),
    _TmnxBfdAdminOwner_Type()
)
tmnxBfdAdminOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxBfdAdminOwner.setStatus("current")


class _TmnxBfdAdminControlApply_Type(Integer32):
    """Custom type tmnxBfdAdminControlApply based on Integer32"""
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
        *(("commit", 3),
          ("initialize", 2),
          ("none", 1))
    )


_TmnxBfdAdminControlApply_Type.__name__ = "Integer32"
_TmnxBfdAdminControlApply_Object = MibScalar
tmnxBfdAdminControlApply = _TmnxBfdAdminControlApply_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 2, 1, 2),
    _TmnxBfdAdminControlApply_Type()
)
tmnxBfdAdminControlApply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxBfdAdminControlApply.setStatus("current")
_TmnxBfdAdminLastSetTimer_Type = TimeInterval
_TmnxBfdAdminLastSetTimer_Object = MibScalar
tmnxBfdAdminLastSetTimer = _TmnxBfdAdminLastSetTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 2, 1, 3),
    _TmnxBfdAdminLastSetTimer_Type()
)
tmnxBfdAdminLastSetTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBfdAdminLastSetTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBfdAdminLastSetTimer.setUnits("centiseconds")


class _TmnxBfdAdminLastSetTimeout_Type(TimeInterval):
    """Custom type tmnxBfdAdminLastSetTimeout based on TimeInterval"""
    defaultValue = 180000


_TmnxBfdAdminLastSetTimeout_Object = MibScalar
tmnxBfdAdminLastSetTimeout = _TmnxBfdAdminLastSetTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 2, 1, 4),
    _TmnxBfdAdminLastSetTimeout_Type()
)
tmnxBfdAdminLastSetTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxBfdAdminLastSetTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBfdAdminLastSetTimeout.setUnits("centiseconds")
_TmnxBfdAdminValueObjects_ObjectIdentity = ObjectIdentity
tmnxBfdAdminValueObjects = _TmnxBfdAdminValueObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 2, 2)
)
_TmnxBfdAdminTemplateTable_Object = MibTable
tmnxBfdAdminTemplateTable = _TmnxBfdAdminTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 2, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxBfdAdminTemplateTable.setStatus("current")
_TmnxBfdAdminTemplateEntry_Object = MibTableRow
tmnxBfdAdminTemplateEntry = _TmnxBfdAdminTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 2, 2, 1, 1)
)
tmnxBfdAdminTemplateEntry.setIndexNames(
    (0, "TIMETRA-BFD-MIB", "tmnxBfdAdminTemplateName"),
)
if mibBuilder.loadTexts:
    tmnxBfdAdminTemplateEntry.setStatus("current")
_TmnxBfdAdminTemplateName_Type = TNamedItem
_TmnxBfdAdminTemplateName_Object = MibTableColumn
tmnxBfdAdminTemplateName = _TmnxBfdAdminTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 2, 2, 1, 1, 1),
    _TmnxBfdAdminTemplateName_Type()
)
tmnxBfdAdminTemplateName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBfdAdminTemplateName.setStatus("current")
_TmnxBfdAdminTemplateRowStatus_Type = RowStatus
_TmnxBfdAdminTemplateRowStatus_Object = MibTableColumn
tmnxBfdAdminTemplateRowStatus = _TmnxBfdAdminTemplateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 2, 2, 1, 1, 2),
    _TmnxBfdAdminTemplateRowStatus_Type()
)
tmnxBfdAdminTemplateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBfdAdminTemplateRowStatus.setStatus("current")


class _TmnxBfdAdminTemplateTxInt_Type(Unsigned32):
    """Custom type tmnxBfdAdminTemplateTxInt based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100000),
    )


_TmnxBfdAdminTemplateTxInt_Type.__name__ = "Unsigned32"
_TmnxBfdAdminTemplateTxInt_Object = MibTableColumn
tmnxBfdAdminTemplateTxInt = _TmnxBfdAdminTemplateTxInt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 2, 2, 1, 1, 3),
    _TmnxBfdAdminTemplateTxInt_Type()
)
tmnxBfdAdminTemplateTxInt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBfdAdminTemplateTxInt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBfdAdminTemplateTxInt.setUnits("milliseconds")


class _TmnxBfdAdminTemplateRxInt_Type(Unsigned32):
    """Custom type tmnxBfdAdminTemplateRxInt based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100000),
    )


_TmnxBfdAdminTemplateRxInt_Type.__name__ = "Unsigned32"
_TmnxBfdAdminTemplateRxInt_Object = MibTableColumn
tmnxBfdAdminTemplateRxInt = _TmnxBfdAdminTemplateRxInt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 2, 2, 1, 1, 4),
    _TmnxBfdAdminTemplateRxInt_Type()
)
tmnxBfdAdminTemplateRxInt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBfdAdminTemplateRxInt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBfdAdminTemplateRxInt.setUnits("milliseconds")


class _TmnxBfdAdminTemplateMultiplier_Type(Unsigned32):
    """Custom type tmnxBfdAdminTemplateMultiplier based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 20),
    )


_TmnxBfdAdminTemplateMultiplier_Type.__name__ = "Unsigned32"
_TmnxBfdAdminTemplateMultiplier_Object = MibTableColumn
tmnxBfdAdminTemplateMultiplier = _TmnxBfdAdminTemplateMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 2, 2, 1, 1, 5),
    _TmnxBfdAdminTemplateMultiplier_Type()
)
tmnxBfdAdminTemplateMultiplier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBfdAdminTemplateMultiplier.setStatus("current")


class _TmnxBfdAdminTemplateEchoRxInt_Type(Unsigned32):
    """Custom type tmnxBfdAdminTemplateEchoRxInt based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 100000),
    )


_TmnxBfdAdminTemplateEchoRxInt_Type.__name__ = "Unsigned32"
_TmnxBfdAdminTemplateEchoRxInt_Object = MibTableColumn
tmnxBfdAdminTemplateEchoRxInt = _TmnxBfdAdminTemplateEchoRxInt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 2, 2, 1, 1, 6),
    _TmnxBfdAdminTemplateEchoRxInt_Type()
)
tmnxBfdAdminTemplateEchoRxInt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBfdAdminTemplateEchoRxInt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBfdAdminTemplateEchoRxInt.setUnits("milliseconds")


class _TmnxBfdAdminTemplateType_Type(Integer32):
    """Custom type tmnxBfdAdminTemplateType based on Integer32"""
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
        *(("auto", 2),
          ("cpmNp", 1),
          ("iomHw", 3))
    )


_TmnxBfdAdminTemplateType_Type.__name__ = "Integer32"
_TmnxBfdAdminTemplateType_Object = MibTableColumn
tmnxBfdAdminTemplateType = _TmnxBfdAdminTemplateType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 2, 2, 1, 1, 7),
    _TmnxBfdAdminTemplateType_Type()
)
tmnxBfdAdminTemplateType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBfdAdminTemplateType.setStatus("current")

# Managed Objects groups

tmnxBfdV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 85, 2, 1)
)
tmnxBfdV11v0Group.setObjects(
      *(("TIMETRA-BFD-MIB", "tmnxBfdAdminOwner"),
        ("TIMETRA-BFD-MIB", "tmnxBfdAdminControlApply"),
        ("TIMETRA-BFD-MIB", "tmnxBfdAdminLastSetTimer"),
        ("TIMETRA-BFD-MIB", "tmnxBfdAdminLastSetTimeout"),
        ("TIMETRA-BFD-MIB", "tmnxBfdAdminTemplateRowStatus"),
        ("TIMETRA-BFD-MIB", "tmnxBfdAdminTemplateTxInt"),
        ("TIMETRA-BFD-MIB", "tmnxBfdAdminTemplateRxInt"),
        ("TIMETRA-BFD-MIB", "tmnxBfdAdminTemplateMultiplier"),
        ("TIMETRA-BFD-MIB", "tmnxBfdAdminTemplateEchoRxInt"),
        ("TIMETRA-BFD-MIB", "tmnxBfdAdminTemplateType"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOperTemplateRowStatus"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOperTemplateTxInt"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOperTemplateRxInt"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOperTemplateMultiplier"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOperTemplateEchoRxInt"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOperTemplateType"))
)
if mibBuilder.loadTexts:
    tmnxBfdV11v0Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tmnxBfdV11v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 85, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxBfdV11v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-BFD-MIB",
    **{"timetraBfdMIBModule": timetraBfdMIBModule,
       "tmnxBfdConformance": tmnxBfdConformance,
       "tmnxBfdCompliances": tmnxBfdCompliances,
       "tmnxBfdV11v0Compliance": tmnxBfdV11v0Compliance,
       "tmnxBfdGroups": tmnxBfdGroups,
       "tmnxBfdV11v0Group": tmnxBfdV11v0Group,
       "tmnxBfdObjects": tmnxBfdObjects,
       "tmnxBfdOperObjects": tmnxBfdOperObjects,
       "tmnxBfdOperValueObjects": tmnxBfdOperValueObjects,
       "tmnxBfdOperTemplateTable": tmnxBfdOperTemplateTable,
       "tmnxBfdOperTemplateEntry": tmnxBfdOperTemplateEntry,
       "tmnxBfdOperTemplateName": tmnxBfdOperTemplateName,
       "tmnxBfdOperTemplateRowStatus": tmnxBfdOperTemplateRowStatus,
       "tmnxBfdOperTemplateTxInt": tmnxBfdOperTemplateTxInt,
       "tmnxBfdOperTemplateRxInt": tmnxBfdOperTemplateRxInt,
       "tmnxBfdOperTemplateMultiplier": tmnxBfdOperTemplateMultiplier,
       "tmnxBfdOperTemplateEchoRxInt": tmnxBfdOperTemplateEchoRxInt,
       "tmnxBfdOperTemplateType": tmnxBfdOperTemplateType,
       "tmnxBfdAdminObjects": tmnxBfdAdminObjects,
       "tmnxBfdAdminControlObjects": tmnxBfdAdminControlObjects,
       "tmnxBfdAdminOwner": tmnxBfdAdminOwner,
       "tmnxBfdAdminControlApply": tmnxBfdAdminControlApply,
       "tmnxBfdAdminLastSetTimer": tmnxBfdAdminLastSetTimer,
       "tmnxBfdAdminLastSetTimeout": tmnxBfdAdminLastSetTimeout,
       "tmnxBfdAdminValueObjects": tmnxBfdAdminValueObjects,
       "tmnxBfdAdminTemplateTable": tmnxBfdAdminTemplateTable,
       "tmnxBfdAdminTemplateEntry": tmnxBfdAdminTemplateEntry,
       "tmnxBfdAdminTemplateName": tmnxBfdAdminTemplateName,
       "tmnxBfdAdminTemplateRowStatus": tmnxBfdAdminTemplateRowStatus,
       "tmnxBfdAdminTemplateTxInt": tmnxBfdAdminTemplateTxInt,
       "tmnxBfdAdminTemplateRxInt": tmnxBfdAdminTemplateRxInt,
       "tmnxBfdAdminTemplateMultiplier": tmnxBfdAdminTemplateMultiplier,
       "tmnxBfdAdminTemplateEchoRxInt": tmnxBfdAdminTemplateEchoRxInt,
       "tmnxBfdAdminTemplateType": tmnxBfdAdminTemplateType}
)
