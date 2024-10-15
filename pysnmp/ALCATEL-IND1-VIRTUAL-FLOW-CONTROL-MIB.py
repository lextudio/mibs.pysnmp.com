# SNMP MIB module (ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:49 2024
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

(softentIND1Vfc,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1Vfc")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1VfcMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1)
)
alcatelIND1VfcMIB.setRevisions(
        ("2010-03-15 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VfcEnableState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )



class VfcBwLimitType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mbits", 1),
          ("percentage", 2))
    )



class VfcProfileType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("qProfile", 3),
          ("qsetProfile", 2),
          ("wredProfile", 1))
    )



class VfcQueueType(Integer32, TextualConvention):
    status = "current"


class VfcQsetAction(Integer32, TextualConvention):
    status = "deprecated"
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
        *(("default", 0),
          ("detach", 2),
          ("override", 1),
          ("revert", 3))
    )



class VfcQsapList(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )



class VfcQsapType(Integer32, TextualConvention):
    status = "current"
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
        *(("all", 1),
          ("ipif", 5),
          ("lag", 4),
          ("lsp", 6),
          ("sap", 8),
          ("sbind", 7),
          ("slot", 2),
          ("slotport", 3))
    )



class VfcSchedulingMethod(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("queueSpecified", 2),
          ("strictPriority", 1))
    )



class VfcWfqMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("werr", 1),
          ("wrr", 2))
    )



class VfcProfileMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dcb", 2),
          ("nonDcb", 1))
    )



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1VfcMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1VfcMIBObjects = _AlcatelIND1VfcMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1VfcMIBObjects.setStatus("current")
_AlaVfcConfig_ObjectIdentity = ObjectIdentity
alaVfcConfig = _AlaVfcConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1)
)
_AlaVfcWREDProfileTable_Object = MibTable
alaVfcWREDProfileTable = _AlaVfcWREDProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    alaVfcWREDProfileTable.setStatus("current")
_AlaVfcWREDProfileEntry_Object = MibTableRow
alaVfcWREDProfileEntry = _AlaVfcWREDProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 1, 1)
)
alaVfcWREDProfileEntry.setIndexNames(
    (0, "ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcWRPId"),
)
if mibBuilder.loadTexts:
    alaVfcWREDProfileEntry.setStatus("current")


class _AlaVfcWRPId_Type(Unsigned32):
    """Custom type alaVfcWRPId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AlaVfcWRPId_Type.__name__ = "Unsigned32"
_AlaVfcWRPId_Object = MibTableColumn
alaVfcWRPId = _AlaVfcWRPId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 1, 1, 1),
    _AlaVfcWRPId_Type()
)
alaVfcWRPId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaVfcWRPId.setStatus("current")


class _AlaVfcWRPAdminState_Type(VfcEnableState):
    """Custom type alaVfcWRPAdminState based on VfcEnableState"""


_AlaVfcWRPAdminState_Object = MibTableColumn
alaVfcWRPAdminState = _AlaVfcWRPAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 1, 1, 2),
    _AlaVfcWRPAdminState_Type()
)
alaVfcWRPAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaVfcWRPAdminState.setStatus("deprecated")


class _AlaVfcWRPName_Type(SnmpAdminString):
    """Custom type alaVfcWRPName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaVfcWRPName_Type.__name__ = "SnmpAdminString"
_AlaVfcWRPName_Object = MibTableColumn
alaVfcWRPName = _AlaVfcWRPName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 1, 1, 3),
    _AlaVfcWRPName_Type()
)
alaVfcWRPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcWRPName.setStatus("current")


class _AlaVfcWRPGreenMinThreshold_Type(Unsigned32):
    """Custom type alaVfcWRPGreenMinThreshold based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AlaVfcWRPGreenMinThreshold_Type.__name__ = "Unsigned32"
_AlaVfcWRPGreenMinThreshold_Object = MibTableColumn
alaVfcWRPGreenMinThreshold = _AlaVfcWRPGreenMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 1, 1, 4),
    _AlaVfcWRPGreenMinThreshold_Type()
)
alaVfcWRPGreenMinThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcWRPGreenMinThreshold.setStatus("current")


class _AlaVfcWRPGreenMaxThreshold_Type(Unsigned32):
    """Custom type alaVfcWRPGreenMaxThreshold based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AlaVfcWRPGreenMaxThreshold_Type.__name__ = "Unsigned32"
_AlaVfcWRPGreenMaxThreshold_Object = MibTableColumn
alaVfcWRPGreenMaxThreshold = _AlaVfcWRPGreenMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 1, 1, 5),
    _AlaVfcWRPGreenMaxThreshold_Type()
)
alaVfcWRPGreenMaxThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcWRPGreenMaxThreshold.setStatus("current")


class _AlaVfcWRPGreenMaxDropProbability_Type(Unsigned32):
    """Custom type alaVfcWRPGreenMaxDropProbability based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AlaVfcWRPGreenMaxDropProbability_Type.__name__ = "Unsigned32"
_AlaVfcWRPGreenMaxDropProbability_Object = MibTableColumn
alaVfcWRPGreenMaxDropProbability = _AlaVfcWRPGreenMaxDropProbability_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 1, 1, 6),
    _AlaVfcWRPGreenMaxDropProbability_Type()
)
alaVfcWRPGreenMaxDropProbability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcWRPGreenMaxDropProbability.setStatus("current")


class _AlaVfcWRPGreenGain_Type(Unsigned32):
    """Custom type alaVfcWRPGreenGain based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AlaVfcWRPGreenGain_Type.__name__ = "Unsigned32"
_AlaVfcWRPGreenGain_Object = MibTableColumn
alaVfcWRPGreenGain = _AlaVfcWRPGreenGain_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 1, 1, 7),
    _AlaVfcWRPGreenGain_Type()
)
alaVfcWRPGreenGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcWRPGreenGain.setStatus("current")


class _AlaVfcWRPYellowMinThreshold_Type(Unsigned32):
    """Custom type alaVfcWRPYellowMinThreshold based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AlaVfcWRPYellowMinThreshold_Type.__name__ = "Unsigned32"
_AlaVfcWRPYellowMinThreshold_Object = MibTableColumn
alaVfcWRPYellowMinThreshold = _AlaVfcWRPYellowMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 1, 1, 8),
    _AlaVfcWRPYellowMinThreshold_Type()
)
alaVfcWRPYellowMinThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcWRPYellowMinThreshold.setStatus("current")


class _AlaVfcWRPYellowMaxThreshold_Type(Unsigned32):
    """Custom type alaVfcWRPYellowMaxThreshold based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AlaVfcWRPYellowMaxThreshold_Type.__name__ = "Unsigned32"
_AlaVfcWRPYellowMaxThreshold_Object = MibTableColumn
alaVfcWRPYellowMaxThreshold = _AlaVfcWRPYellowMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 1, 1, 9),
    _AlaVfcWRPYellowMaxThreshold_Type()
)
alaVfcWRPYellowMaxThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcWRPYellowMaxThreshold.setStatus("current")


class _AlaVfcWRPYellowMaxDropProbability_Type(Unsigned32):
    """Custom type alaVfcWRPYellowMaxDropProbability based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AlaVfcWRPYellowMaxDropProbability_Type.__name__ = "Unsigned32"
_AlaVfcWRPYellowMaxDropProbability_Object = MibTableColumn
alaVfcWRPYellowMaxDropProbability = _AlaVfcWRPYellowMaxDropProbability_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 1, 1, 10),
    _AlaVfcWRPYellowMaxDropProbability_Type()
)
alaVfcWRPYellowMaxDropProbability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcWRPYellowMaxDropProbability.setStatus("current")


class _AlaVfcWRPYellowGain_Type(Unsigned32):
    """Custom type alaVfcWRPYellowGain based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AlaVfcWRPYellowGain_Type.__name__ = "Unsigned32"
_AlaVfcWRPYellowGain_Object = MibTableColumn
alaVfcWRPYellowGain = _AlaVfcWRPYellowGain_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 1, 1, 11),
    _AlaVfcWRPYellowGain_Type()
)
alaVfcWRPYellowGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcWRPYellowGain.setStatus("current")


class _AlaVfcWRPRedMinThreshold_Type(Unsigned32):
    """Custom type alaVfcWRPRedMinThreshold based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AlaVfcWRPRedMinThreshold_Type.__name__ = "Unsigned32"
_AlaVfcWRPRedMinThreshold_Object = MibTableColumn
alaVfcWRPRedMinThreshold = _AlaVfcWRPRedMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 1, 1, 12),
    _AlaVfcWRPRedMinThreshold_Type()
)
alaVfcWRPRedMinThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcWRPRedMinThreshold.setStatus("current")


class _AlaVfcWRPRedMaxThreshold_Type(Unsigned32):
    """Custom type alaVfcWRPRedMaxThreshold based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AlaVfcWRPRedMaxThreshold_Type.__name__ = "Unsigned32"
_AlaVfcWRPRedMaxThreshold_Object = MibTableColumn
alaVfcWRPRedMaxThreshold = _AlaVfcWRPRedMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 1, 1, 13),
    _AlaVfcWRPRedMaxThreshold_Type()
)
alaVfcWRPRedMaxThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcWRPRedMaxThreshold.setStatus("current")


class _AlaVfcWRPRedMaxDropProbability_Type(Unsigned32):
    """Custom type alaVfcWRPRedMaxDropProbability based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AlaVfcWRPRedMaxDropProbability_Type.__name__ = "Unsigned32"
_AlaVfcWRPRedMaxDropProbability_Object = MibTableColumn
alaVfcWRPRedMaxDropProbability = _AlaVfcWRPRedMaxDropProbability_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 1, 1, 14),
    _AlaVfcWRPRedMaxDropProbability_Type()
)
alaVfcWRPRedMaxDropProbability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcWRPRedMaxDropProbability.setStatus("current")


class _AlaVfcWRPRedGain_Type(Unsigned32):
    """Custom type alaVfcWRPRedGain based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AlaVfcWRPRedGain_Type.__name__ = "Unsigned32"
_AlaVfcWRPRedGain_Object = MibTableColumn
alaVfcWRPRedGain = _AlaVfcWRPRedGain_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 1, 1, 15),
    _AlaVfcWRPRedGain_Type()
)
alaVfcWRPRedGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcWRPRedGain.setStatus("current")


class _AlaVfcWRPStatsAdmin_Type(VfcEnableState):
    """Custom type alaVfcWRPStatsAdmin based on VfcEnableState"""


_AlaVfcWRPStatsAdmin_Object = MibTableColumn
alaVfcWRPStatsAdmin = _AlaVfcWRPStatsAdmin_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 1, 1, 16),
    _AlaVfcWRPStatsAdmin_Type()
)
alaVfcWRPStatsAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcWRPStatsAdmin.setStatus("deprecated")


class _AlaVfcWRPAttachmentCount_Type(Unsigned32):
    """Custom type alaVfcWRPAttachmentCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )


_AlaVfcWRPAttachmentCount_Type.__name__ = "Unsigned32"
_AlaVfcWRPAttachmentCount_Object = MibTableColumn
alaVfcWRPAttachmentCount = _AlaVfcWRPAttachmentCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 1, 1, 17),
    _AlaVfcWRPAttachmentCount_Type()
)
alaVfcWRPAttachmentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcWRPAttachmentCount.setStatus("current")


class _AlaVfcWRPMTU_Type(Unsigned32):
    """Custom type alaVfcWRPMTU based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )


_AlaVfcWRPMTU_Type.__name__ = "Unsigned32"
_AlaVfcWRPMTU_Object = MibTableColumn
alaVfcWRPMTU = _AlaVfcWRPMTU_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 1, 1, 18),
    _AlaVfcWRPMTU_Type()
)
alaVfcWRPMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcWRPMTU.setStatus("current")
_AlaVfcWRPLastChange_Type = DateAndTime
_AlaVfcWRPLastChange_Object = MibTableColumn
alaVfcWRPLastChange = _AlaVfcWRPLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 1, 1, 19),
    _AlaVfcWRPLastChange_Type()
)
alaVfcWRPLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcWRPLastChange.setStatus("current")
_AlaVfcWRPRowStatus_Type = RowStatus
_AlaVfcWRPRowStatus_Object = MibTableColumn
alaVfcWRPRowStatus = _AlaVfcWRPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 1, 1, 20),
    _AlaVfcWRPRowStatus_Type()
)
alaVfcWRPRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcWRPRowStatus.setStatus("current")
_AlaVfcQsetProfileTable_Object = MibTable
alaVfcQsetProfileTable = _AlaVfcQsetProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    alaVfcQsetProfileTable.setStatus("current")
_AlaVfcQsetProfileEntry_Object = MibTableRow
alaVfcQsetProfileEntry = _AlaVfcQsetProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 2, 1)
)
alaVfcQsetProfileEntry.setIndexNames(
    (0, "ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQSPId"),
)
if mibBuilder.loadTexts:
    alaVfcQsetProfileEntry.setStatus("current")


class _AlaVfcQSPId_Type(Unsigned32):
    """Custom type alaVfcQSPId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AlaVfcQSPId_Type.__name__ = "Unsigned32"
_AlaVfcQSPId_Object = MibTableColumn
alaVfcQSPId = _AlaVfcQSPId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 2, 1, 1),
    _AlaVfcQSPId_Type()
)
alaVfcQSPId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaVfcQSPId.setStatus("current")


class _AlaVfcQSPAdminState_Type(VfcEnableState):
    """Custom type alaVfcQSPAdminState based on VfcEnableState"""


_AlaVfcQSPAdminState_Object = MibTableColumn
alaVfcQSPAdminState = _AlaVfcQSPAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 2, 1, 2),
    _AlaVfcQSPAdminState_Type()
)
alaVfcQSPAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQSPAdminState.setStatus("deprecated")


class _AlaVfcQSPName_Type(SnmpAdminString):
    """Custom type alaVfcQSPName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaVfcQSPName_Type.__name__ = "SnmpAdminString"
_AlaVfcQSPName_Object = MibTableColumn
alaVfcQSPName = _AlaVfcQSPName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 2, 1, 3),
    _AlaVfcQSPName_Type()
)
alaVfcQSPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQSPName.setStatus("current")


class _AlaVfcQSPType_Type(Integer32):
    """Custom type alaVfcQSPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_AlaVfcQSPType_Type.__name__ = "Integer32"
_AlaVfcQSPType_Object = MibTableColumn
alaVfcQSPType = _AlaVfcQSPType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 2, 1, 4),
    _AlaVfcQSPType_Type()
)
alaVfcQSPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQSPType.setStatus("current")


class _AlaVfcQSPTemplateId_Type(Unsigned32):
    """Custom type alaVfcQSPTemplateId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_AlaVfcQSPTemplateId_Type.__name__ = "Unsigned32"
_AlaVfcQSPTemplateId_Object = MibTableColumn
alaVfcQSPTemplateId = _AlaVfcQSPTemplateId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 2, 1, 5),
    _AlaVfcQSPTemplateId_Type()
)
alaVfcQSPTemplateId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQSPTemplateId.setStatus("current")


class _AlaVfcQSPTemplateName_Type(SnmpAdminString):
    """Custom type alaVfcQSPTemplateName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaVfcQSPTemplateName_Type.__name__ = "SnmpAdminString"
_AlaVfcQSPTemplateName_Object = MibTableColumn
alaVfcQSPTemplateName = _AlaVfcQSPTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 2, 1, 6),
    _AlaVfcQSPTemplateName_Type()
)
alaVfcQSPTemplateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQSPTemplateName.setStatus("current")


class _AlaVfcQSPBandwidthLimitType_Type(VfcBwLimitType):
    """Custom type alaVfcQSPBandwidthLimitType based on VfcBwLimitType"""


_AlaVfcQSPBandwidthLimitType_Object = MibTableColumn
alaVfcQSPBandwidthLimitType = _AlaVfcQSPBandwidthLimitType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 2, 1, 7),
    _AlaVfcQSPBandwidthLimitType_Type()
)
alaVfcQSPBandwidthLimitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQSPBandwidthLimitType.setStatus("current")
_AlaVfcQSPBandwidthLimitValue_Type = Unsigned32
_AlaVfcQSPBandwidthLimitValue_Object = MibTableColumn
alaVfcQSPBandwidthLimitValue = _AlaVfcQSPBandwidthLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 2, 1, 8),
    _AlaVfcQSPBandwidthLimitValue_Type()
)
alaVfcQSPBandwidthLimitValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQSPBandwidthLimitValue.setStatus("current")


class _AlaVfcQSPQueueCount_Type(Unsigned32):
    """Custom type alaVfcQSPQueueCount based on Unsigned32"""
    defaultValue = 8


_AlaVfcQSPQueueCount_Object = MibTableColumn
alaVfcQSPQueueCount = _AlaVfcQSPQueueCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 2, 1, 9),
    _AlaVfcQSPQueueCount_Type()
)
alaVfcQSPQueueCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQSPQueueCount.setStatus("current")


class _AlaVfcQSPWRPId_Type(Unsigned32):
    """Custom type alaVfcQSPWRPId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AlaVfcQSPWRPId_Type.__name__ = "Unsigned32"
_AlaVfcQSPWRPId_Object = MibTableColumn
alaVfcQSPWRPId = _AlaVfcQSPWRPId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 2, 1, 10),
    _AlaVfcQSPWRPId_Type()
)
alaVfcQSPWRPId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQSPWRPId.setStatus("current")


class _AlaVfcQSPWRPName_Type(SnmpAdminString):
    """Custom type alaVfcQSPWRPName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaVfcQSPWRPName_Type.__name__ = "SnmpAdminString"
_AlaVfcQSPWRPName_Object = MibTableColumn
alaVfcQSPWRPName = _AlaVfcQSPWRPName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 2, 1, 11),
    _AlaVfcQSPWRPName_Type()
)
alaVfcQSPWRPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQSPWRPName.setStatus("current")


class _AlaVfcQSPWRPAdminState_Type(VfcEnableState):
    """Custom type alaVfcQSPWRPAdminState based on VfcEnableState"""


_AlaVfcQSPWRPAdminState_Object = MibTableColumn
alaVfcQSPWRPAdminState = _AlaVfcQSPWRPAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 2, 1, 12),
    _AlaVfcQSPWRPAdminState_Type()
)
alaVfcQSPWRPAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaVfcQSPWRPAdminState.setStatus("deprecated")


class _AlaVfcQSPSchedulingMethod_Type(VfcSchedulingMethod):
    """Custom type alaVfcQSPSchedulingMethod based on VfcSchedulingMethod"""


_AlaVfcQSPSchedulingMethod_Object = MibTableColumn
alaVfcQSPSchedulingMethod = _AlaVfcQSPSchedulingMethod_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 2, 1, 13),
    _AlaVfcQSPSchedulingMethod_Type()
)
alaVfcQSPSchedulingMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQSPSchedulingMethod.setStatus("current")


class _AlaVfcQSPStatsAdmin_Type(VfcEnableState):
    """Custom type alaVfcQSPStatsAdmin based on VfcEnableState"""


_AlaVfcQSPStatsAdmin_Object = MibTableColumn
alaVfcQSPStatsAdmin = _AlaVfcQSPStatsAdmin_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 2, 1, 14),
    _AlaVfcQSPStatsAdmin_Type()
)
alaVfcQSPStatsAdmin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaVfcQSPStatsAdmin.setStatus("deprecated")


class _AlaVfcQSPAttachmentCount_Type(Unsigned32):
    """Custom type alaVfcQSPAttachmentCount based on Unsigned32"""
    defaultValue = 0


_AlaVfcQSPAttachmentCount_Object = MibTableColumn
alaVfcQSPAttachmentCount = _AlaVfcQSPAttachmentCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 2, 1, 15),
    _AlaVfcQSPAttachmentCount_Type()
)
alaVfcQSPAttachmentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQSPAttachmentCount.setStatus("current")
_AlaVfcQSPLastChange_Type = DateAndTime
_AlaVfcQSPLastChange_Object = MibTableColumn
alaVfcQSPLastChange = _AlaVfcQSPLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 2, 1, 16),
    _AlaVfcQSPLastChange_Type()
)
alaVfcQSPLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQSPLastChange.setStatus("current")
_AlaVfcQSPRowStatus_Type = RowStatus
_AlaVfcQSPRowStatus_Object = MibTableColumn
alaVfcQSPRowStatus = _AlaVfcQSPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 2, 1, 17),
    _AlaVfcQSPRowStatus_Type()
)
alaVfcQSPRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQSPRowStatus.setStatus("current")
_AlaVfcQsetInstanceTable_Object = MibTable
alaVfcQsetInstanceTable = _AlaVfcQsetInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    alaVfcQsetInstanceTable.setStatus("current")
_AlaVfcQsetInstanceEntry_Object = MibTableRow
alaVfcQsetInstanceEntry = _AlaVfcQsetInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 3, 1)
)
alaVfcQsetInstanceEntry.setIndexNames(
    (0, "ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQsetId"),
)
if mibBuilder.loadTexts:
    alaVfcQsetInstanceEntry.setStatus("current")
_AlaVfcQsetId_Type = Unsigned32
_AlaVfcQsetId_Object = MibTableColumn
alaVfcQsetId = _AlaVfcQsetId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 3, 1, 1),
    _AlaVfcQsetId_Type()
)
alaVfcQsetId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaVfcQsetId.setStatus("current")
_AlaVfcQsetQsapId_Type = Unsigned32
_AlaVfcQsetQsapId_Object = MibTableColumn
alaVfcQsetQsapId = _AlaVfcQsetQsapId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 3, 1, 2),
    _AlaVfcQsetQsapId_Type()
)
alaVfcQsetQsapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQsetQsapId.setStatus("current")


class _AlaVfcQsetAdminState_Type(VfcEnableState):
    """Custom type alaVfcQsetAdminState based on VfcEnableState"""


_AlaVfcQsetAdminState_Object = MibTableColumn
alaVfcQsetAdminState = _AlaVfcQsetAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 3, 1, 3),
    _AlaVfcQsetAdminState_Type()
)
alaVfcQsetAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVfcQsetAdminState.setStatus("deprecated")


class _AlaVfcQsetOperState_Type(VfcEnableState):
    """Custom type alaVfcQsetOperState based on VfcEnableState"""


_AlaVfcQsetOperState_Object = MibTableColumn
alaVfcQsetOperState = _AlaVfcQsetOperState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 3, 1, 4),
    _AlaVfcQsetOperState_Type()
)
alaVfcQsetOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQsetOperState.setStatus("deprecated")


class _AlaVfcQsetQSPId_Type(Unsigned32):
    """Custom type alaVfcQsetQSPId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_AlaVfcQsetQSPId_Type.__name__ = "Unsigned32"
_AlaVfcQsetQSPId_Object = MibTableColumn
alaVfcQsetQSPId = _AlaVfcQsetQSPId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 3, 1, 5),
    _AlaVfcQsetQSPId_Type()
)
alaVfcQsetQSPId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVfcQsetQSPId.setStatus("current")


class _AlaVfcQsetQSPName_Type(SnmpAdminString):
    """Custom type alaVfcQsetQSPName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaVfcQsetQSPName_Type.__name__ = "SnmpAdminString"
_AlaVfcQsetQSPName_Object = MibTableColumn
alaVfcQsetQSPName = _AlaVfcQsetQSPName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 3, 1, 6),
    _AlaVfcQsetQSPName_Type()
)
alaVfcQsetQSPName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVfcQsetQSPName.setStatus("current")


class _AlaVfcQsetOperBandwidthLimitType_Type(VfcBwLimitType):
    """Custom type alaVfcQsetOperBandwidthLimitType based on VfcBwLimitType"""


_AlaVfcQsetOperBandwidthLimitType_Object = MibTableColumn
alaVfcQsetOperBandwidthLimitType = _AlaVfcQsetOperBandwidthLimitType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 3, 1, 7),
    _AlaVfcQsetOperBandwidthLimitType_Type()
)
alaVfcQsetOperBandwidthLimitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQsetOperBandwidthLimitType.setStatus("current")
_AlaVfcQsetOperBandwidthLimitValue_Type = Unsigned32
_AlaVfcQsetOperBandwidthLimitValue_Object = MibTableColumn
alaVfcQsetOperBandwidthLimitValue = _AlaVfcQsetOperBandwidthLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 3, 1, 8),
    _AlaVfcQsetOperBandwidthLimitValue_Type()
)
alaVfcQsetOperBandwidthLimitValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQsetOperBandwidthLimitValue.setStatus("current")


class _AlaVfcQsetBandwidthLimitType_Type(VfcBwLimitType):
    """Custom type alaVfcQsetBandwidthLimitType based on VfcBwLimitType"""


_AlaVfcQsetBandwidthLimitType_Object = MibTableColumn
alaVfcQsetBandwidthLimitType = _AlaVfcQsetBandwidthLimitType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 3, 1, 9),
    _AlaVfcQsetBandwidthLimitType_Type()
)
alaVfcQsetBandwidthLimitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQsetBandwidthLimitType.setStatus("deprecated")
_AlaVfcQsetBandwidthLimitValue_Type = Unsigned32
_AlaVfcQsetBandwidthLimitValue_Object = MibTableColumn
alaVfcQsetBandwidthLimitValue = _AlaVfcQsetBandwidthLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 3, 1, 10),
    _AlaVfcQsetBandwidthLimitValue_Type()
)
alaVfcQsetBandwidthLimitValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQsetBandwidthLimitValue.setStatus("deprecated")


class _AlaVfcQsetQueueCount_Type(Unsigned32):
    """Custom type alaVfcQsetQueueCount based on Unsigned32"""
    defaultValue = 8


_AlaVfcQsetQueueCount_Object = MibTableColumn
alaVfcQsetQueueCount = _AlaVfcQsetQueueCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 3, 1, 11),
    _AlaVfcQsetQueueCount_Type()
)
alaVfcQsetQueueCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQsetQueueCount.setStatus("deprecated")


class _AlaVfcQsetWRPId_Type(Unsigned32):
    """Custom type alaVfcQsetWRPId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AlaVfcQsetWRPId_Type.__name__ = "Unsigned32"
_AlaVfcQsetWRPId_Object = MibTableColumn
alaVfcQsetWRPId = _AlaVfcQsetWRPId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 3, 1, 12),
    _AlaVfcQsetWRPId_Type()
)
alaVfcQsetWRPId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQsetWRPId.setStatus("deprecated")


class _AlaVfcQsetWRPName_Type(SnmpAdminString):
    """Custom type alaVfcQsetWRPName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaVfcQsetWRPName_Type.__name__ = "SnmpAdminString"
_AlaVfcQsetWRPName_Object = MibTableColumn
alaVfcQsetWRPName = _AlaVfcQsetWRPName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 3, 1, 13),
    _AlaVfcQsetWRPName_Type()
)
alaVfcQsetWRPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQsetWRPName.setStatus("deprecated")


class _AlaVfcQsetWRPAdminState_Type(VfcEnableState):
    """Custom type alaVfcQsetWRPAdminState based on VfcEnableState"""


_AlaVfcQsetWRPAdminState_Object = MibTableColumn
alaVfcQsetWRPAdminState = _AlaVfcQsetWRPAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 3, 1, 14),
    _AlaVfcQsetWRPAdminState_Type()
)
alaVfcQsetWRPAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVfcQsetWRPAdminState.setStatus("current")


class _AlaVfcQsetWRPOperState_Type(VfcEnableState):
    """Custom type alaVfcQsetWRPOperState based on VfcEnableState"""


_AlaVfcQsetWRPOperState_Object = MibTableColumn
alaVfcQsetWRPOperState = _AlaVfcQsetWRPOperState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 3, 1, 15),
    _AlaVfcQsetWRPOperState_Type()
)
alaVfcQsetWRPOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQsetWRPOperState.setStatus("current")


class _AlaVfcQsetSchedulingMethod_Type(VfcSchedulingMethod):
    """Custom type alaVfcQsetSchedulingMethod based on VfcSchedulingMethod"""


_AlaVfcQsetSchedulingMethod_Object = MibTableColumn
alaVfcQsetSchedulingMethod = _AlaVfcQsetSchedulingMethod_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 3, 1, 16),
    _AlaVfcQsetSchedulingMethod_Type()
)
alaVfcQsetSchedulingMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQsetSchedulingMethod.setStatus("deprecated")


class _AlaVfcQsetStatsAdmin_Type(VfcEnableState):
    """Custom type alaVfcQsetStatsAdmin based on VfcEnableState"""


_AlaVfcQsetStatsAdmin_Object = MibTableColumn
alaVfcQsetStatsAdmin = _AlaVfcQsetStatsAdmin_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 3, 1, 17),
    _AlaVfcQsetStatsAdmin_Type()
)
alaVfcQsetStatsAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVfcQsetStatsAdmin.setStatus("current")


class _AlaVfcQsetStatsOper_Type(VfcEnableState):
    """Custom type alaVfcQsetStatsOper based on VfcEnableState"""


_AlaVfcQsetStatsOper_Object = MibTableColumn
alaVfcQsetStatsOper = _AlaVfcQsetStatsOper_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 3, 1, 18),
    _AlaVfcQsetStatsOper_Type()
)
alaVfcQsetStatsOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQsetStatsOper.setStatus("current")
_AlaVfcQsetLastChange_Type = DateAndTime
_AlaVfcQsetLastChange_Object = MibTableColumn
alaVfcQsetLastChange = _AlaVfcQsetLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 3, 1, 19),
    _AlaVfcQsetLastChange_Type()
)
alaVfcQsetLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQsetLastChange.setStatus("current")


class _AlaVfcQsetStatsClear_Type(VfcEnableState):
    """Custom type alaVfcQsetStatsClear based on VfcEnableState"""


_AlaVfcQsetStatsClear_Object = MibTableColumn
alaVfcQsetStatsClear = _AlaVfcQsetStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 3, 1, 20),
    _AlaVfcQsetStatsClear_Type()
)
alaVfcQsetStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVfcQsetStatsClear.setStatus("current")


class _AlaVfcQsetStatsInterval_Type(Unsigned32):
    """Custom type alaVfcQsetStatsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_AlaVfcQsetStatsInterval_Type.__name__ = "Unsigned32"
_AlaVfcQsetStatsInterval_Object = MibTableColumn
alaVfcQsetStatsInterval = _AlaVfcQsetStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 3, 1, 21),
    _AlaVfcQsetStatsInterval_Type()
)
alaVfcQsetStatsInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVfcQsetStatsInterval.setStatus("current")


class _AlaVfcQsetMisconfigured_Type(VfcEnableState):
    """Custom type alaVfcQsetMisconfigured based on VfcEnableState"""


_AlaVfcQsetMisconfigured_Object = MibTableColumn
alaVfcQsetMisconfigured = _AlaVfcQsetMisconfigured_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 3, 1, 22),
    _AlaVfcQsetMisconfigured_Type()
)
alaVfcQsetMisconfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQsetMisconfigured.setStatus("current")
_AlaVfcQsetMode_Type = VfcProfileMode
_AlaVfcQsetMode_Object = MibTableColumn
alaVfcQsetMode = _AlaVfcQsetMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 3, 1, 23),
    _AlaVfcQsetMode_Type()
)
alaVfcQsetMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQsetMode.setStatus("current")
_AlaVfcQProfileTable_Object = MibTable
alaVfcQProfileTable = _AlaVfcQProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    alaVfcQProfileTable.setStatus("current")
_AlaVfcQProfileEntry_Object = MibTableRow
alaVfcQProfileEntry = _AlaVfcQProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 4, 1)
)
alaVfcQProfileEntry.setIndexNames(
    (0, "ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQPQSPId"),
    (0, "ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQPQId"),
)
if mibBuilder.loadTexts:
    alaVfcQProfileEntry.setStatus("current")


class _AlaVfcQPQSPId_Type(Unsigned32):
    """Custom type alaVfcQPQSPId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AlaVfcQPQSPId_Type.__name__ = "Unsigned32"
_AlaVfcQPQSPId_Object = MibTableColumn
alaVfcQPQSPId = _AlaVfcQPQSPId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 4, 1, 1),
    _AlaVfcQPQSPId_Type()
)
alaVfcQPQSPId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaVfcQPQSPId.setStatus("current")


class _AlaVfcQPQId_Type(Unsigned32):
    """Custom type alaVfcQPQId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AlaVfcQPQId_Type.__name__ = "Unsigned32"
_AlaVfcQPQId_Object = MibTableColumn
alaVfcQPQId = _AlaVfcQPQId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 4, 1, 2),
    _AlaVfcQPQId_Type()
)
alaVfcQPQId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaVfcQPQId.setStatus("current")


class _AlaVfcQPAdminState_Type(VfcEnableState):
    """Custom type alaVfcQPAdminState based on VfcEnableState"""


_AlaVfcQPAdminState_Object = MibTableColumn
alaVfcQPAdminState = _AlaVfcQPAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 4, 1, 3),
    _AlaVfcQPAdminState_Type()
)
alaVfcQPAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQPAdminState.setStatus("deprecated")


class _AlaVfcQPWRPId_Type(Unsigned32):
    """Custom type alaVfcQPWRPId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AlaVfcQPWRPId_Type.__name__ = "Unsigned32"
_AlaVfcQPWRPId_Object = MibTableColumn
alaVfcQPWRPId = _AlaVfcQPWRPId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 4, 1, 4),
    _AlaVfcQPWRPId_Type()
)
alaVfcQPWRPId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQPWRPId.setStatus("current")


class _AlaVfcQPWRPName_Type(SnmpAdminString):
    """Custom type alaVfcQPWRPName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaVfcQPWRPName_Type.__name__ = "SnmpAdminString"
_AlaVfcQPWRPName_Object = MibTableColumn
alaVfcQPWRPName = _AlaVfcQPWRPName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 4, 1, 5),
    _AlaVfcQPWRPName_Type()
)
alaVfcQPWRPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQPWRPName.setStatus("current")


class _AlaVfcQPWRPAdminState_Type(VfcEnableState):
    """Custom type alaVfcQPWRPAdminState based on VfcEnableState"""


_AlaVfcQPWRPAdminState_Object = MibTableColumn
alaVfcQPWRPAdminState = _AlaVfcQPWRPAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 4, 1, 6),
    _AlaVfcQPWRPAdminState_Type()
)
alaVfcQPWRPAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQPWRPAdminState.setStatus("deprecated")


class _AlaVfcQPQSPName_Type(SnmpAdminString):
    """Custom type alaVfcQPQSPName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaVfcQPQSPName_Type.__name__ = "SnmpAdminString"
_AlaVfcQPQSPName_Object = MibTableColumn
alaVfcQPQSPName = _AlaVfcQPQSPName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 4, 1, 7),
    _AlaVfcQPQSPName_Type()
)
alaVfcQPQSPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQPQSPName.setStatus("current")


class _AlaVfcQPTrafficClass_Type(Unsigned32):
    """Custom type alaVfcQPTrafficClass based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AlaVfcQPTrafficClass_Type.__name__ = "Unsigned32"
_AlaVfcQPTrafficClass_Object = MibTableColumn
alaVfcQPTrafficClass = _AlaVfcQPTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 4, 1, 8),
    _AlaVfcQPTrafficClass_Type()
)
alaVfcQPTrafficClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQPTrafficClass.setStatus("current")
_AlaVfcQPQType_Type = VfcQueueType
_AlaVfcQPQType_Object = MibTableColumn
alaVfcQPQType = _AlaVfcQPQType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 4, 1, 9),
    _AlaVfcQPQType_Type()
)
alaVfcQPQType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQPQType.setStatus("current")
_AlaVfcQPCIRBandwidthLimitType_Type = VfcBwLimitType
_AlaVfcQPCIRBandwidthLimitType_Object = MibTableColumn
alaVfcQPCIRBandwidthLimitType = _AlaVfcQPCIRBandwidthLimitType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 4, 1, 10),
    _AlaVfcQPCIRBandwidthLimitType_Type()
)
alaVfcQPCIRBandwidthLimitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQPCIRBandwidthLimitType.setStatus("current")
_AlaVfcQPCIRBandwidthLimitValue_Type = Unsigned32
_AlaVfcQPCIRBandwidthLimitValue_Object = MibTableColumn
alaVfcQPCIRBandwidthLimitValue = _AlaVfcQPCIRBandwidthLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 4, 1, 11),
    _AlaVfcQPCIRBandwidthLimitValue_Type()
)
alaVfcQPCIRBandwidthLimitValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQPCIRBandwidthLimitValue.setStatus("current")
_AlaVfcQPPIRBandwidthLimitType_Type = VfcBwLimitType
_AlaVfcQPPIRBandwidthLimitType_Object = MibTableColumn
alaVfcQPPIRBandwidthLimitType = _AlaVfcQPPIRBandwidthLimitType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 4, 1, 12),
    _AlaVfcQPPIRBandwidthLimitType_Type()
)
alaVfcQPPIRBandwidthLimitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQPPIRBandwidthLimitType.setStatus("current")
_AlaVfcQPPIRBandwidthLimitValue_Type = Unsigned32
_AlaVfcQPPIRBandwidthLimitValue_Object = MibTableColumn
alaVfcQPPIRBandwidthLimitValue = _AlaVfcQPPIRBandwidthLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 4, 1, 13),
    _AlaVfcQPPIRBandwidthLimitValue_Type()
)
alaVfcQPPIRBandwidthLimitValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQPPIRBandwidthLimitValue.setStatus("current")


class _AlaVfcQPStatsAdmin_Type(VfcEnableState):
    """Custom type alaVfcQPStatsAdmin based on VfcEnableState"""


_AlaVfcQPStatsAdmin_Object = MibTableColumn
alaVfcQPStatsAdmin = _AlaVfcQPStatsAdmin_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 4, 1, 14),
    _AlaVfcQPStatsAdmin_Type()
)
alaVfcQPStatsAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQPStatsAdmin.setStatus("deprecated")
_AlaVfcQPCbs_Type = Unsigned32
_AlaVfcQPCbs_Object = MibTableColumn
alaVfcQPCbs = _AlaVfcQPCbs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 4, 1, 15),
    _AlaVfcQPCbs_Type()
)
alaVfcQPCbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQPCbs.setStatus("current")
_AlaVfcQPMbs_Type = Unsigned32
_AlaVfcQPMbs_Object = MibTableColumn
alaVfcQPMbs = _AlaVfcQPMbs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 4, 1, 16),
    _AlaVfcQPMbs_Type()
)
alaVfcQPMbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQPMbs.setStatus("current")
_AlaVfcQPLastChange_Type = DateAndTime
_AlaVfcQPLastChange_Object = MibTableColumn
alaVfcQPLastChange = _AlaVfcQPLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 4, 1, 17),
    _AlaVfcQPLastChange_Type()
)
alaVfcQPLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQPLastChange.setStatus("current")
_AlaVfcQPWfqWeight_Type = Unsigned32
_AlaVfcQPWfqWeight_Object = MibTableColumn
alaVfcQPWfqWeight = _AlaVfcQPWfqWeight_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 4, 1, 18),
    _AlaVfcQPWfqWeight_Type()
)
alaVfcQPWfqWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQPWfqWeight.setStatus("current")
_AlaVfcQPWfqMode_Type = VfcWfqMode
_AlaVfcQPWfqMode_Object = MibTableColumn
alaVfcQPWfqMode = _AlaVfcQPWfqMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 4, 1, 19),
    _AlaVfcQPWfqMode_Type()
)
alaVfcQPWfqMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQPWfqMode.setStatus("current")
_AlaVfcQInstanceTable_Object = MibTable
alaVfcQInstanceTable = _AlaVfcQInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    alaVfcQInstanceTable.setStatus("current")
_AlaVfcQInstanceEntry_Object = MibTableRow
alaVfcQInstanceEntry = _AlaVfcQInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 5, 1)
)
alaVfcQInstanceEntry.setIndexNames(
    (0, "ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQInstanceQsiId"),
    (0, "ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQInstanceQId"),
)
if mibBuilder.loadTexts:
    alaVfcQInstanceEntry.setStatus("current")
_AlaVfcQInstanceQsiId_Type = Unsigned32
_AlaVfcQInstanceQsiId_Object = MibTableColumn
alaVfcQInstanceQsiId = _AlaVfcQInstanceQsiId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 5, 1, 1),
    _AlaVfcQInstanceQsiId_Type()
)
alaVfcQInstanceQsiId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaVfcQInstanceQsiId.setStatus("current")


class _AlaVfcQInstanceQId_Type(Unsigned32):
    """Custom type alaVfcQInstanceQId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AlaVfcQInstanceQId_Type.__name__ = "Unsigned32"
_AlaVfcQInstanceQId_Object = MibTableColumn
alaVfcQInstanceQId = _AlaVfcQInstanceQId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 5, 1, 2),
    _AlaVfcQInstanceQId_Type()
)
alaVfcQInstanceQId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaVfcQInstanceQId.setStatus("current")
_AlaVfcQInstanceQsapId_Type = Unsigned32
_AlaVfcQInstanceQsapId_Object = MibTableColumn
alaVfcQInstanceQsapId = _AlaVfcQInstanceQsapId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 5, 1, 3),
    _AlaVfcQInstanceQsapId_Type()
)
alaVfcQInstanceQsapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQInstanceQsapId.setStatus("deprecated")


class _AlaVfcQInstanceQSPId_Type(Unsigned32):
    """Custom type alaVfcQInstanceQSPId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AlaVfcQInstanceQSPId_Type.__name__ = "Unsigned32"
_AlaVfcQInstanceQSPId_Object = MibTableColumn
alaVfcQInstanceQSPId = _AlaVfcQInstanceQSPId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 5, 1, 4),
    _AlaVfcQInstanceQSPId_Type()
)
alaVfcQInstanceQSPId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQInstanceQSPId.setStatus("deprecated")


class _AlaVfcQInstanceQSPName_Type(SnmpAdminString):
    """Custom type alaVfcQInstanceQSPName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaVfcQInstanceQSPName_Type.__name__ = "SnmpAdminString"
_AlaVfcQInstanceQSPName_Object = MibTableColumn
alaVfcQInstanceQSPName = _AlaVfcQInstanceQSPName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 5, 1, 5),
    _AlaVfcQInstanceQSPName_Type()
)
alaVfcQInstanceQSPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQInstanceQSPName.setStatus("deprecated")


class _AlaVfcQInstanceAdminState_Type(VfcEnableState):
    """Custom type alaVfcQInstanceAdminState based on VfcEnableState"""


_AlaVfcQInstanceAdminState_Object = MibTableColumn
alaVfcQInstanceAdminState = _AlaVfcQInstanceAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 5, 1, 6),
    _AlaVfcQInstanceAdminState_Type()
)
alaVfcQInstanceAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVfcQInstanceAdminState.setStatus("deprecated")


class _AlaVfcQInstanceOperState_Type(VfcEnableState):
    """Custom type alaVfcQInstanceOperState based on VfcEnableState"""


_AlaVfcQInstanceOperState_Object = MibTableColumn
alaVfcQInstanceOperState = _AlaVfcQInstanceOperState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 5, 1, 7),
    _AlaVfcQInstanceOperState_Type()
)
alaVfcQInstanceOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQInstanceOperState.setStatus("deprecated")


class _AlaVfcQInstanceWRPAdminState_Type(VfcEnableState):
    """Custom type alaVfcQInstanceWRPAdminState based on VfcEnableState"""


_AlaVfcQInstanceWRPAdminState_Object = MibTableColumn
alaVfcQInstanceWRPAdminState = _AlaVfcQInstanceWRPAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 5, 1, 8),
    _AlaVfcQInstanceWRPAdminState_Type()
)
alaVfcQInstanceWRPAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVfcQInstanceWRPAdminState.setStatus("current")


class _AlaVfcQInstanceWRPOperState_Type(VfcEnableState):
    """Custom type alaVfcQInstanceWRPOperState based on VfcEnableState"""


_AlaVfcQInstanceWRPOperState_Object = MibTableColumn
alaVfcQInstanceWRPOperState = _AlaVfcQInstanceWRPOperState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 5, 1, 9),
    _AlaVfcQInstanceWRPOperState_Type()
)
alaVfcQInstanceWRPOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQInstanceWRPOperState.setStatus("current")


class _AlaVfcQInstanceWRPId_Type(Unsigned32):
    """Custom type alaVfcQInstanceWRPId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AlaVfcQInstanceWRPId_Type.__name__ = "Unsigned32"
_AlaVfcQInstanceWRPId_Object = MibTableColumn
alaVfcQInstanceWRPId = _AlaVfcQInstanceWRPId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 5, 1, 10),
    _AlaVfcQInstanceWRPId_Type()
)
alaVfcQInstanceWRPId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQInstanceWRPId.setStatus("deprecated")


class _AlaVfcQInstanceWRPName_Type(SnmpAdminString):
    """Custom type alaVfcQInstanceWRPName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaVfcQInstanceWRPName_Type.__name__ = "SnmpAdminString"
_AlaVfcQInstanceWRPName_Object = MibTableColumn
alaVfcQInstanceWRPName = _AlaVfcQInstanceWRPName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 5, 1, 11),
    _AlaVfcQInstanceWRPName_Type()
)
alaVfcQInstanceWRPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQInstanceWRPName.setStatus("deprecated")
_AlaVfcQInstanceCIRBandwidthLimitType_Type = VfcBwLimitType
_AlaVfcQInstanceCIRBandwidthLimitType_Object = MibTableColumn
alaVfcQInstanceCIRBandwidthLimitType = _AlaVfcQInstanceCIRBandwidthLimitType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 5, 1, 12),
    _AlaVfcQInstanceCIRBandwidthLimitType_Type()
)
alaVfcQInstanceCIRBandwidthLimitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQInstanceCIRBandwidthLimitType.setStatus("deprecated")
_AlaVfcQInstanceCIRBandwidthLimitValue_Type = Unsigned32
_AlaVfcQInstanceCIRBandwidthLimitValue_Object = MibTableColumn
alaVfcQInstanceCIRBandwidthLimitValue = _AlaVfcQInstanceCIRBandwidthLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 5, 1, 13),
    _AlaVfcQInstanceCIRBandwidthLimitValue_Type()
)
alaVfcQInstanceCIRBandwidthLimitValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQInstanceCIRBandwidthLimitValue.setStatus("deprecated")
_AlaVfcQInstancePIRBandwidthLimitType_Type = VfcBwLimitType
_AlaVfcQInstancePIRBandwidthLimitType_Object = MibTableColumn
alaVfcQInstancePIRBandwidthLimitType = _AlaVfcQInstancePIRBandwidthLimitType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 5, 1, 14),
    _AlaVfcQInstancePIRBandwidthLimitType_Type()
)
alaVfcQInstancePIRBandwidthLimitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQInstancePIRBandwidthLimitType.setStatus("deprecated")
_AlaVfcQInstancePIRBandwidthLimitValue_Type = Unsigned32
_AlaVfcQInstancePIRBandwidthLimitValue_Object = MibTableColumn
alaVfcQInstancePIRBandwidthLimitValue = _AlaVfcQInstancePIRBandwidthLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 5, 1, 15),
    _AlaVfcQInstancePIRBandwidthLimitValue_Type()
)
alaVfcQInstancePIRBandwidthLimitValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQInstancePIRBandwidthLimitValue.setStatus("deprecated")
_AlaVfcQInstanceCIROperationalBandwidthLimitType_Type = VfcBwLimitType
_AlaVfcQInstanceCIROperationalBandwidthLimitType_Object = MibTableColumn
alaVfcQInstanceCIROperationalBandwidthLimitType = _AlaVfcQInstanceCIROperationalBandwidthLimitType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 5, 1, 16),
    _AlaVfcQInstanceCIROperationalBandwidthLimitType_Type()
)
alaVfcQInstanceCIROperationalBandwidthLimitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQInstanceCIROperationalBandwidthLimitType.setStatus("current")
_AlaVfcQInstanceCIROperationalBandwidthLimitValue_Type = Unsigned32
_AlaVfcQInstanceCIROperationalBandwidthLimitValue_Object = MibTableColumn
alaVfcQInstanceCIROperationalBandwidthLimitValue = _AlaVfcQInstanceCIROperationalBandwidthLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 5, 1, 17),
    _AlaVfcQInstanceCIROperationalBandwidthLimitValue_Type()
)
alaVfcQInstanceCIROperationalBandwidthLimitValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQInstanceCIROperationalBandwidthLimitValue.setStatus("current")
_AlaVfcQInstancePIROperationalBandwidthLimitType_Type = VfcBwLimitType
_AlaVfcQInstancePIROperationalBandwidthLimitType_Object = MibTableColumn
alaVfcQInstancePIROperationalBandwidthLimitType = _AlaVfcQInstancePIROperationalBandwidthLimitType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 5, 1, 18),
    _AlaVfcQInstancePIROperationalBandwidthLimitType_Type()
)
alaVfcQInstancePIROperationalBandwidthLimitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQInstancePIROperationalBandwidthLimitType.setStatus("current")
_AlaVfcQInstancePIROperationalBandwidthLimitValue_Type = Unsigned32
_AlaVfcQInstancePIROperationalBandwidthLimitValue_Object = MibTableColumn
alaVfcQInstancePIROperationalBandwidthLimitValue = _AlaVfcQInstancePIROperationalBandwidthLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 5, 1, 19),
    _AlaVfcQInstancePIROperationalBandwidthLimitValue_Type()
)
alaVfcQInstancePIROperationalBandwidthLimitValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQInstancePIROperationalBandwidthLimitValue.setStatus("current")


class _AlaVfcQInstanceStatsAdmin_Type(VfcEnableState):
    """Custom type alaVfcQInstanceStatsAdmin based on VfcEnableState"""


_AlaVfcQInstanceStatsAdmin_Object = MibTableColumn
alaVfcQInstanceStatsAdmin = _AlaVfcQInstanceStatsAdmin_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 5, 1, 20),
    _AlaVfcQInstanceStatsAdmin_Type()
)
alaVfcQInstanceStatsAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVfcQInstanceStatsAdmin.setStatus("deprecated")


class _AlaVfcQInstanceStatsOper_Type(VfcEnableState):
    """Custom type alaVfcQInstanceStatsOper based on VfcEnableState"""


_AlaVfcQInstanceStatsOper_Object = MibTableColumn
alaVfcQInstanceStatsOper = _AlaVfcQInstanceStatsOper_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 5, 1, 21),
    _AlaVfcQInstanceStatsOper_Type()
)
alaVfcQInstanceStatsOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQInstanceStatsOper.setStatus("deprecated")
_AlaVfcQInstancePacketsEnqueued_Type = Counter64
_AlaVfcQInstancePacketsEnqueued_Object = MibTableColumn
alaVfcQInstancePacketsEnqueued = _AlaVfcQInstancePacketsEnqueued_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 5, 1, 22),
    _AlaVfcQInstancePacketsEnqueued_Type()
)
alaVfcQInstancePacketsEnqueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQInstancePacketsEnqueued.setStatus("current")
_AlaVfcQInstanceBytesEnqueued_Type = Counter64
_AlaVfcQInstanceBytesEnqueued_Object = MibTableColumn
alaVfcQInstanceBytesEnqueued = _AlaVfcQInstanceBytesEnqueued_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 5, 1, 23),
    _AlaVfcQInstanceBytesEnqueued_Type()
)
alaVfcQInstanceBytesEnqueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQInstanceBytesEnqueued.setStatus("current")
_AlaVfcQInstancePacketsDequeued_Type = Counter64
_AlaVfcQInstancePacketsDequeued_Object = MibTableColumn
alaVfcQInstancePacketsDequeued = _AlaVfcQInstancePacketsDequeued_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 5, 1, 24),
    _AlaVfcQInstancePacketsDequeued_Type()
)
alaVfcQInstancePacketsDequeued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQInstancePacketsDequeued.setStatus("deprecated")
_AlaVfcQInstanceBytesDequeued_Type = Counter64
_AlaVfcQInstanceBytesDequeued_Object = MibTableColumn
alaVfcQInstanceBytesDequeued = _AlaVfcQInstanceBytesDequeued_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 5, 1, 25),
    _AlaVfcQInstanceBytesDequeued_Type()
)
alaVfcQInstanceBytesDequeued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQInstanceBytesDequeued.setStatus("deprecated")
_AlaVfcQInstancePacketsDropped_Type = Counter64
_AlaVfcQInstancePacketsDropped_Object = MibTableColumn
alaVfcQInstancePacketsDropped = _AlaVfcQInstancePacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 5, 1, 26),
    _AlaVfcQInstancePacketsDropped_Type()
)
alaVfcQInstancePacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQInstancePacketsDropped.setStatus("current")
_AlaVfcQInstanceBytesDropped_Type = Counter64
_AlaVfcQInstanceBytesDropped_Object = MibTableColumn
alaVfcQInstanceBytesDropped = _AlaVfcQInstanceBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 5, 1, 27),
    _AlaVfcQInstanceBytesDropped_Type()
)
alaVfcQInstanceBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQInstanceBytesDropped.setStatus("current")
_AlaVfcQInstanceGreenPacketsAccepted_Type = Counter64
_AlaVfcQInstanceGreenPacketsAccepted_Object = MibTableColumn
alaVfcQInstanceGreenPacketsAccepted = _AlaVfcQInstanceGreenPacketsAccepted_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 5, 1, 28),
    _AlaVfcQInstanceGreenPacketsAccepted_Type()
)
alaVfcQInstanceGreenPacketsAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQInstanceGreenPacketsAccepted.setStatus("current")
_AlaVfcQInstanceGreenBytesAccepted_Type = Counter64
_AlaVfcQInstanceGreenBytesAccepted_Object = MibTableColumn
alaVfcQInstanceGreenBytesAccepted = _AlaVfcQInstanceGreenBytesAccepted_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 5, 1, 29),
    _AlaVfcQInstanceGreenBytesAccepted_Type()
)
alaVfcQInstanceGreenBytesAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQInstanceGreenBytesAccepted.setStatus("current")
_AlaVfcQInstanceGreenPacketsDropped_Type = Counter64
_AlaVfcQInstanceGreenPacketsDropped_Object = MibTableColumn
alaVfcQInstanceGreenPacketsDropped = _AlaVfcQInstanceGreenPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 5, 1, 30),
    _AlaVfcQInstanceGreenPacketsDropped_Type()
)
alaVfcQInstanceGreenPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQInstanceGreenPacketsDropped.setStatus("current")
_AlaVfcQInstanceGreenBytesDropped_Type = Counter64
_AlaVfcQInstanceGreenBytesDropped_Object = MibTableColumn
alaVfcQInstanceGreenBytesDropped = _AlaVfcQInstanceGreenBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 5, 1, 31),
    _AlaVfcQInstanceGreenBytesDropped_Type()
)
alaVfcQInstanceGreenBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQInstanceGreenBytesDropped.setStatus("current")
_AlaVfcQInstanceYellowPacketsAccepted_Type = Counter64
_AlaVfcQInstanceYellowPacketsAccepted_Object = MibTableColumn
alaVfcQInstanceYellowPacketsAccepted = _AlaVfcQInstanceYellowPacketsAccepted_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 5, 1, 32),
    _AlaVfcQInstanceYellowPacketsAccepted_Type()
)
alaVfcQInstanceYellowPacketsAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQInstanceYellowPacketsAccepted.setStatus("current")
_AlaVfcQInstanceYellowBytesAccepted_Type = Counter64
_AlaVfcQInstanceYellowBytesAccepted_Object = MibTableColumn
alaVfcQInstanceYellowBytesAccepted = _AlaVfcQInstanceYellowBytesAccepted_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 5, 1, 33),
    _AlaVfcQInstanceYellowBytesAccepted_Type()
)
alaVfcQInstanceYellowBytesAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQInstanceYellowBytesAccepted.setStatus("current")
_AlaVfcQInstanceYellowPacketsDropped_Type = Counter64
_AlaVfcQInstanceYellowPacketsDropped_Object = MibTableColumn
alaVfcQInstanceYellowPacketsDropped = _AlaVfcQInstanceYellowPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 5, 1, 34),
    _AlaVfcQInstanceYellowPacketsDropped_Type()
)
alaVfcQInstanceYellowPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQInstanceYellowPacketsDropped.setStatus("current")
_AlaVfcQInstanceYellowBytesDropped_Type = Counter64
_AlaVfcQInstanceYellowBytesDropped_Object = MibTableColumn
alaVfcQInstanceYellowBytesDropped = _AlaVfcQInstanceYellowBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 5, 1, 35),
    _AlaVfcQInstanceYellowBytesDropped_Type()
)
alaVfcQInstanceYellowBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQInstanceYellowBytesDropped.setStatus("current")
_AlaVfcQInstanceRedPacketsAccepted_Type = Counter64
_AlaVfcQInstanceRedPacketsAccepted_Object = MibTableColumn
alaVfcQInstanceRedPacketsAccepted = _AlaVfcQInstanceRedPacketsAccepted_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 5, 1, 36),
    _AlaVfcQInstanceRedPacketsAccepted_Type()
)
alaVfcQInstanceRedPacketsAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQInstanceRedPacketsAccepted.setStatus("current")
_AlaVfcQInstanceRedBytesAccepted_Type = Counter64
_AlaVfcQInstanceRedBytesAccepted_Object = MibTableColumn
alaVfcQInstanceRedBytesAccepted = _AlaVfcQInstanceRedBytesAccepted_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 5, 1, 37),
    _AlaVfcQInstanceRedBytesAccepted_Type()
)
alaVfcQInstanceRedBytesAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQInstanceRedBytesAccepted.setStatus("current")
_AlaVfcQInstanceRedPacketsDropped_Type = Counter64
_AlaVfcQInstanceRedPacketsDropped_Object = MibTableColumn
alaVfcQInstanceRedPacketsDropped = _AlaVfcQInstanceRedPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 5, 1, 38),
    _AlaVfcQInstanceRedPacketsDropped_Type()
)
alaVfcQInstanceRedPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQInstanceRedPacketsDropped.setStatus("current")
_AlaVfcQInstanceRedBytesDropped_Type = Counter64
_AlaVfcQInstanceRedBytesDropped_Object = MibTableColumn
alaVfcQInstanceRedBytesDropped = _AlaVfcQInstanceRedBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 5, 1, 39),
    _AlaVfcQInstanceRedBytesDropped_Type()
)
alaVfcQInstanceRedBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQInstanceRedBytesDropped.setStatus("current")
_AlaVfcQInstanceLastChange_Type = DateAndTime
_AlaVfcQInstanceLastChange_Object = MibTableColumn
alaVfcQInstanceLastChange = _AlaVfcQInstanceLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 5, 1, 40),
    _AlaVfcQInstanceLastChange_Type()
)
alaVfcQInstanceLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQInstanceLastChange.setStatus("current")


class _AlaVfcQInstanceStatsClear_Type(VfcEnableState):
    """Custom type alaVfcQInstanceStatsClear based on VfcEnableState"""


_AlaVfcQInstanceStatsClear_Object = MibTableColumn
alaVfcQInstanceStatsClear = _AlaVfcQInstanceStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 5, 1, 41),
    _AlaVfcQInstanceStatsClear_Type()
)
alaVfcQInstanceStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVfcQInstanceStatsClear.setStatus("deprecated")
_AlaVfcQsapTable_Object = MibTable
alaVfcQsapTable = _AlaVfcQsapTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 6)
)
if mibBuilder.loadTexts:
    alaVfcQsapTable.setStatus("current")
_AlaVfcQsapEntry_Object = MibTableRow
alaVfcQsapEntry = _AlaVfcQsapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 6, 1)
)
alaVfcQsapEntry.setIndexNames(
    (0, "ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQsapId"),
)
if mibBuilder.loadTexts:
    alaVfcQsapEntry.setStatus("current")
_AlaVfcQsapId_Type = Unsigned32
_AlaVfcQsapId_Object = MibTableColumn
alaVfcQsapId = _AlaVfcQsapId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 6, 1, 1),
    _AlaVfcQsapId_Type()
)
alaVfcQsapId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaVfcQsapId.setStatus("current")


class _AlaVfcQsapAdminState_Type(VfcEnableState):
    """Custom type alaVfcQsapAdminState based on VfcEnableState"""


_AlaVfcQsapAdminState_Object = MibTableColumn
alaVfcQsapAdminState = _AlaVfcQsapAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 6, 1, 2),
    _AlaVfcQsapAdminState_Type()
)
alaVfcQsapAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQsapAdminState.setStatus("deprecated")
_AlaVfcQsapType_Type = VfcQsapType
_AlaVfcQsapType_Object = MibTableColumn
alaVfcQsapType = _AlaVfcQsapType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 6, 1, 3),
    _AlaVfcQsapType_Type()
)
alaVfcQsapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQsapType.setStatus("current")
_AlaVfcQsapValue_Type = Unsigned32
_AlaVfcQsapValue_Object = MibTableColumn
alaVfcQsapValue = _AlaVfcQsapValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 6, 1, 4),
    _AlaVfcQsapValue_Type()
)
alaVfcQsapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQsapValue.setStatus("current")


class _AlaVfcQsapQSPId_Type(Unsigned32):
    """Custom type alaVfcQsapQSPId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AlaVfcQsapQSPId_Type.__name__ = "Unsigned32"
_AlaVfcQsapQSPId_Object = MibTableColumn
alaVfcQsapQSPId = _AlaVfcQsapQSPId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 6, 1, 5),
    _AlaVfcQsapQSPId_Type()
)
alaVfcQsapQSPId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVfcQsapQSPId.setStatus("deprecated")


class _AlaVfcQsapQSPName_Type(SnmpAdminString):
    """Custom type alaVfcQsapQSPName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaVfcQsapQSPName_Type.__name__ = "SnmpAdminString"
_AlaVfcQsapQSPName_Object = MibTableColumn
alaVfcQsapQSPName = _AlaVfcQsapQSPName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 6, 1, 6),
    _AlaVfcQsapQSPName_Type()
)
alaVfcQsapQSPName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVfcQsapQSPName.setStatus("deprecated")


class _AlaVfcQsapWRPAdminState_Type(VfcEnableState):
    """Custom type alaVfcQsapWRPAdminState based on VfcEnableState"""


_AlaVfcQsapWRPAdminState_Object = MibTableColumn
alaVfcQsapWRPAdminState = _AlaVfcQsapWRPAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 6, 1, 7),
    _AlaVfcQsapWRPAdminState_Type()
)
alaVfcQsapWRPAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVfcQsapWRPAdminState.setStatus("deprecated")


class _AlaVfcQsapStatsAdmin_Type(VfcEnableState):
    """Custom type alaVfcQsapStatsAdmin based on VfcEnableState"""


_AlaVfcQsapStatsAdmin_Object = MibTableColumn
alaVfcQsapStatsAdmin = _AlaVfcQsapStatsAdmin_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 6, 1, 8),
    _AlaVfcQsapStatsAdmin_Type()
)
alaVfcQsapStatsAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVfcQsapStatsAdmin.setStatus("deprecated")


class _AlaVfcQsapBandwidthLimitType_Type(VfcBwLimitType):
    """Custom type alaVfcQsapBandwidthLimitType based on VfcBwLimitType"""


_AlaVfcQsapBandwidthLimitType_Object = MibTableColumn
alaVfcQsapBandwidthLimitType = _AlaVfcQsapBandwidthLimitType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 6, 1, 9),
    _AlaVfcQsapBandwidthLimitType_Type()
)
alaVfcQsapBandwidthLimitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQsapBandwidthLimitType.setStatus("current")
_AlaVfcQsapBandwidthLimitValue_Type = Unsigned32
_AlaVfcQsapBandwidthLimitValue_Object = MibTableColumn
alaVfcQsapBandwidthLimitValue = _AlaVfcQsapBandwidthLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 6, 1, 10),
    _AlaVfcQsapBandwidthLimitValue_Type()
)
alaVfcQsapBandwidthLimitValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQsapBandwidthLimitValue.setStatus("current")


class _AlaVfcQsapClearStats_Type(Integer32):
    """Custom type alaVfcQsapClearStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("reset", 1))
    )


_AlaVfcQsapClearStats_Type.__name__ = "Integer32"
_AlaVfcQsapClearStats_Object = MibTableColumn
alaVfcQsapClearStats = _AlaVfcQsapClearStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 6, 1, 11),
    _AlaVfcQsapClearStats_Type()
)
alaVfcQsapClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVfcQsapClearStats.setStatus("deprecated")
_AlaVfcQsapQpId_Type = Unsigned32
_AlaVfcQsapQpId_Object = MibTableColumn
alaVfcQsapQpId = _AlaVfcQsapQpId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 6, 1, 12),
    _AlaVfcQsapQpId_Type()
)
alaVfcQsapQpId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVfcQsapQpId.setStatus("deprecated")
_AlaVfcQsapAction_Type = VfcQsetAction
_AlaVfcQsapAction_Object = MibTableColumn
alaVfcQsapAction = _AlaVfcQsapAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 6, 1, 13),
    _AlaVfcQsapAction_Type()
)
alaVfcQsapAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVfcQsapAction.setStatus("deprecated")
_AlaVfcQsapLastChange_Type = DateAndTime
_AlaVfcQsapLastChange_Object = MibTableColumn
alaVfcQsapLastChange = _AlaVfcQsapLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 6, 1, 14),
    _AlaVfcQsapLastChange_Type()
)
alaVfcQsapLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQsapLastChange.setStatus("current")
_AlaVfcQsapParent_Type = Unsigned32
_AlaVfcQsapParent_Object = MibTableColumn
alaVfcQsapParent = _AlaVfcQsapParent_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 6, 1, 15),
    _AlaVfcQsapParent_Type()
)
alaVfcQsapParent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQsapParent.setStatus("current")
_AlaVfcProfileIndexLookupTable_Object = MibTable
alaVfcProfileIndexLookupTable = _AlaVfcProfileIndexLookupTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 7)
)
if mibBuilder.loadTexts:
    alaVfcProfileIndexLookupTable.setStatus("current")
_AlaVfcProfileIndexLookupEntry_Object = MibTableRow
alaVfcProfileIndexLookupEntry = _AlaVfcProfileIndexLookupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 7, 1)
)
alaVfcProfileIndexLookupEntry.setIndexNames(
    (0, "ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcProfileType"),
    (1, "ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcProfileName"),
)
if mibBuilder.loadTexts:
    alaVfcProfileIndexLookupEntry.setStatus("current")
_AlaVfcProfileType_Type = VfcProfileType
_AlaVfcProfileType_Object = MibTableColumn
alaVfcProfileType = _AlaVfcProfileType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 7, 1, 1),
    _AlaVfcProfileType_Type()
)
alaVfcProfileType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaVfcProfileType.setStatus("current")


class _AlaVfcProfileName_Type(SnmpAdminString):
    """Custom type alaVfcProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaVfcProfileName_Type.__name__ = "SnmpAdminString"
_AlaVfcProfileName_Object = MibTableColumn
alaVfcProfileName = _AlaVfcProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 7, 1, 2),
    _AlaVfcProfileName_Type()
)
alaVfcProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaVfcProfileName.setStatus("current")


class _AlaVfcProfileId_Type(Unsigned32):
    """Custom type alaVfcProfileId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_AlaVfcProfileId_Type.__name__ = "Unsigned32"
_AlaVfcProfileId_Object = MibTableColumn
alaVfcProfileId = _AlaVfcProfileId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 7, 1, 3),
    _AlaVfcProfileId_Type()
)
alaVfcProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcProfileId.setStatus("current")
_AlaVfcProfileQsapLookupTable_Object = MibTable
alaVfcProfileQsapLookupTable = _AlaVfcProfileQsapLookupTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 8)
)
if mibBuilder.loadTexts:
    alaVfcProfileQsapLookupTable.setStatus("current")
_AlaVfcProfileQsapLookupEntry_Object = MibTableRow
alaVfcProfileQsapLookupEntry = _AlaVfcProfileQsapLookupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 8, 1)
)
alaVfcProfileQsapLookupEntry.setIndexNames(
    (0, "ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcProfileQsapLookupType"),
    (0, "ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcProfileQsapLookupId"),
    (0, "ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcProfileQsapLookupValue"),
)
if mibBuilder.loadTexts:
    alaVfcProfileQsapLookupEntry.setStatus("current")
_AlaVfcProfileQsapLookupType_Type = VfcProfileType
_AlaVfcProfileQsapLookupType_Object = MibTableColumn
alaVfcProfileQsapLookupType = _AlaVfcProfileQsapLookupType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 8, 1, 1),
    _AlaVfcProfileQsapLookupType_Type()
)
alaVfcProfileQsapLookupType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaVfcProfileQsapLookupType.setStatus("current")


class _AlaVfcProfileQsapLookupId_Type(Unsigned32):
    """Custom type alaVfcProfileQsapLookupId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_AlaVfcProfileQsapLookupId_Type.__name__ = "Unsigned32"
_AlaVfcProfileQsapLookupId_Object = MibTableColumn
alaVfcProfileQsapLookupId = _AlaVfcProfileQsapLookupId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 8, 1, 2),
    _AlaVfcProfileQsapLookupId_Type()
)
alaVfcProfileQsapLookupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaVfcProfileQsapLookupId.setStatus("current")
_AlaVfcProfileQsapLookupValue_Type = Unsigned32
_AlaVfcProfileQsapLookupValue_Object = MibTableColumn
alaVfcProfileQsapLookupValue = _AlaVfcProfileQsapLookupValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 8, 1, 3),
    _AlaVfcProfileQsapLookupValue_Type()
)
alaVfcProfileQsapLookupValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaVfcProfileQsapLookupValue.setStatus("current")
_AlaVfcProfileQsapLookupList_Type = VfcQsapList
_AlaVfcProfileQsapLookupList_Object = MibTableColumn
alaVfcProfileQsapLookupList = _AlaVfcProfileQsapLookupList_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 8, 1, 4),
    _AlaVfcProfileQsapLookupList_Type()
)
alaVfcProfileQsapLookupList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcProfileQsapLookupList.setStatus("current")
_AlaVfcQSIQsapLookupTable_Object = MibTable
alaVfcQSIQsapLookupTable = _AlaVfcQSIQsapLookupTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 9)
)
if mibBuilder.loadTexts:
    alaVfcQSIQsapLookupTable.setStatus("current")
_AlaVfcQSIQsapLookupEntry_Object = MibTableRow
alaVfcQSIQsapLookupEntry = _AlaVfcQSIQsapLookupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 9, 1)
)
alaVfcQSIQsapLookupEntry.setIndexNames(
    (0, "ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQSIQsapLookupQsetId"),
    (0, "ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQSIQsapLookupValue"),
)
if mibBuilder.loadTexts:
    alaVfcQSIQsapLookupEntry.setStatus("current")
_AlaVfcQSIQsapLookupQsetId_Type = Unsigned32
_AlaVfcQSIQsapLookupQsetId_Object = MibTableColumn
alaVfcQSIQsapLookupQsetId = _AlaVfcQSIQsapLookupQsetId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 9, 1, 1),
    _AlaVfcQSIQsapLookupQsetId_Type()
)
alaVfcQSIQsapLookupQsetId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaVfcQSIQsapLookupQsetId.setStatus("current")
_AlaVfcQSIQsapLookupValue_Type = Unsigned32
_AlaVfcQSIQsapLookupValue_Object = MibTableColumn
alaVfcQSIQsapLookupValue = _AlaVfcQSIQsapLookupValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 9, 1, 2),
    _AlaVfcQSIQsapLookupValue_Type()
)
alaVfcQSIQsapLookupValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaVfcQSIQsapLookupValue.setStatus("current")
_AlaVfcQSIQsapLookupList_Type = VfcQsapList
_AlaVfcQSIQsapLookupList_Object = MibTableColumn
alaVfcQSIQsapLookupList = _AlaVfcQSIQsapLookupList_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 9, 1, 3),
    _AlaVfcQSIQsapLookupList_Type()
)
alaVfcQSIQsapLookupList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcQSIQsapLookupList.setStatus("current")
_AlaVfcStatisticsCollectionInterval_Type = Unsigned32
_AlaVfcStatisticsCollectionInterval_Object = MibScalar
alaVfcStatisticsCollectionInterval = _AlaVfcStatisticsCollectionInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 10),
    _AlaVfcStatisticsCollectionInterval_Type()
)
alaVfcStatisticsCollectionInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcStatisticsCollectionInterval.setStatus("deprecated")
_AlaVfcStatisticsCollectionDuration_Type = Unsigned32
_AlaVfcStatisticsCollectionDuration_Object = MibScalar
alaVfcStatisticsCollectionDuration = _AlaVfcStatisticsCollectionDuration_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 1, 11),
    _AlaVfcStatisticsCollectionDuration_Type()
)
alaVfcStatisticsCollectionDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVfcStatisticsCollectionDuration.setStatus("deprecated")
_AlaVfcConformance_ObjectIdentity = ObjectIdentity
alaVfcConformance = _AlaVfcConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 1, 2)
)
_AlcatelIND1VfcMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1VfcMIBConformance = _AlcatelIND1VfcMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1VfcMIBConformance.setStatus("current")
_AlcatelIND1VfcMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1VfcMIBGroups = _AlcatelIND1VfcMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1VfcMIBGroups.setStatus("current")
_AlcatelIND1VfcMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1VfcMIBCompliances = _AlcatelIND1VfcMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1VfcMIBCompliances.setStatus("current")

# Managed Objects groups

alaVfcWREDProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 2, 1, 1)
)
alaVfcWREDProfileGroup.setObjects(
      *(("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcWRPAdminState"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcWRPName"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcWRPGreenMinThreshold"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcWRPGreenMaxThreshold"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcWRPGreenMaxDropProbability"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcWRPGreenGain"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcWRPYellowMinThreshold"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcWRPYellowMaxThreshold"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcWRPYellowMaxDropProbability"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcWRPYellowGain"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcWRPRedMinThreshold"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcWRPRedMaxThreshold"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcWRPRedMaxDropProbability"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcWRPRedGain"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcWRPStatsAdmin"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcWRPAttachmentCount"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcWRPMTU"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcWRPLastChange"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcWRPRowStatus"))
)
if mibBuilder.loadTexts:
    alaVfcWREDProfileGroup.setStatus("current")

alaVfcQsetProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 2, 1, 2)
)
alaVfcQsetProfileGroup.setObjects(
      *(("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQSPAdminState"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQSPName"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQSPType"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQSPTemplateId"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQSPTemplateName"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQSPBandwidthLimitType"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQSPBandwidthLimitValue"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQSPQueueCount"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQSPWRPId"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQSPWRPName"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQSPWRPAdminState"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQSPSchedulingMethod"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQSPStatsAdmin"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQSPAttachmentCount"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQSPLastChange"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQSPRowStatus"))
)
if mibBuilder.loadTexts:
    alaVfcQsetProfileGroup.setStatus("current")

alaVfcQsetInstanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 2, 1, 3)
)
alaVfcQsetInstanceGroup.setObjects(
      *(("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQsetQsapId"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQsetAdminState"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQsetOperState"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQsetQSPId"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQsetQSPName"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQsetBandwidthLimitType"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQsetBandwidthLimitValue"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQsetOperBandwidthLimitType"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQsetOperBandwidthLimitValue"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQsetQueueCount"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQsetWRPId"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQsetWRPName"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQsetWRPAdminState"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQsetWRPOperState"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQsetSchedulingMethod"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQsetStatsAdmin"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQsetStatsOper"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQsetLastChange"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQsetStatsClear"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQsetStatsInterval"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQsetMisconfigured"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQsetMode"))
)
if mibBuilder.loadTexts:
    alaVfcQsetInstanceGroup.setStatus("current")

alaVfcQProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 2, 1, 4)
)
alaVfcQProfileGroup.setObjects(
      *(("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQPAdminState"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQPWRPId"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQPWRPName"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQPWRPAdminState"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQPQSPName"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQPTrafficClass"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQPQType"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQPCIRBandwidthLimitType"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQPCIRBandwidthLimitValue"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQPPIRBandwidthLimitType"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQPPIRBandwidthLimitValue"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQPStatsAdmin"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQPCbs"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQPMbs"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQPLastChange"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQPWfqWeight"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQPWfqMode"))
)
if mibBuilder.loadTexts:
    alaVfcQProfileGroup.setStatus("current")

alaVfcQInstanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 2, 1, 5)
)
alaVfcQInstanceGroup.setObjects(
      *(("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQInstanceQsapId"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQInstanceQSPId"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQInstanceQSPName"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQInstanceAdminState"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQInstanceOperState"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQInstanceWRPAdminState"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQInstanceWRPOperState"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQInstanceWRPId"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQInstanceWRPName"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQInstanceCIRBandwidthLimitType"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQInstanceCIRBandwidthLimitValue"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQInstancePIRBandwidthLimitType"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQInstancePIRBandwidthLimitValue"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQInstanceCIROperationalBandwidthLimitType"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQInstanceCIROperationalBandwidthLimitValue"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQInstancePIROperationalBandwidthLimitType"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQInstancePIROperationalBandwidthLimitValue"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQInstanceStatsAdmin"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQInstanceStatsOper"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQInstancePacketsEnqueued"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQInstanceBytesEnqueued"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQInstancePacketsDequeued"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQInstanceBytesDequeued"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQInstancePacketsDropped"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQInstanceBytesDropped"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQInstanceGreenPacketsAccepted"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQInstanceGreenBytesAccepted"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQInstanceGreenPacketsDropped"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQInstanceGreenBytesDropped"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQInstanceYellowPacketsAccepted"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQInstanceYellowBytesAccepted"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQInstanceYellowPacketsDropped"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQInstanceYellowBytesDropped"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQInstanceRedPacketsAccepted"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQInstanceRedBytesAccepted"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQInstanceRedPacketsDropped"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQInstanceRedBytesDropped"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQInstanceLastChange"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQInstanceStatsClear"))
)
if mibBuilder.loadTexts:
    alaVfcQInstanceGroup.setStatus("current")

alaVfcQsapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 2, 1, 6)
)
alaVfcQsapGroup.setObjects(
      *(("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQsapAdminState"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQsapType"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQsapValue"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQsapQSPId"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQsapQSPName"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQsapWRPAdminState"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQsapStatsAdmin"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQsapBandwidthLimitType"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQsapBandwidthLimitValue"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQsapClearStats"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQsapQpId"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQsapAction"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQsapLastChange"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQsapParent"))
)
if mibBuilder.loadTexts:
    alaVfcQsapGroup.setStatus("current")

alaVfcProfileIndexLookupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 2, 1, 7)
)
alaVfcProfileIndexLookupGroup.setObjects(
    ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcProfileId")
)
if mibBuilder.loadTexts:
    alaVfcProfileIndexLookupGroup.setStatus("current")

alaVfcProfileQsapLookupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 2, 1, 8)
)
alaVfcProfileQsapLookupGroup.setObjects(
    ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcProfileQsapLookupList")
)
if mibBuilder.loadTexts:
    alaVfcProfileQsapLookupGroup.setStatus("current")

alaVfcQSIQsapLookupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 2, 1, 9)
)
alaVfcQSIQsapLookupGroup.setObjects(
    ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcQSIQsapLookupList")
)
if mibBuilder.loadTexts:
    alaVfcQSIQsapLookupGroup.setStatus("current")

alaVfcStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 2, 1, 10)
)
alaVfcStatsGroup.setObjects(
      *(("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcStatisticsCollectionInterval"),
        ("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "alaVfcStatisticsCollectionDuration"))
)
if mibBuilder.loadTexts:
    alaVfcStatsGroup.setStatus("deprecated")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alcatelIND1VfcMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1VfcMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB",
    **{"VfcEnableState": VfcEnableState,
       "VfcBwLimitType": VfcBwLimitType,
       "VfcProfileType": VfcProfileType,
       "VfcQueueType": VfcQueueType,
       "VfcQsetAction": VfcQsetAction,
       "VfcQsapList": VfcQsapList,
       "VfcQsapType": VfcQsapType,
       "VfcSchedulingMethod": VfcSchedulingMethod,
       "VfcWfqMode": VfcWfqMode,
       "VfcProfileMode": VfcProfileMode,
       "alcatelIND1VfcMIB": alcatelIND1VfcMIB,
       "alcatelIND1VfcMIBObjects": alcatelIND1VfcMIBObjects,
       "alaVfcConfig": alaVfcConfig,
       "alaVfcWREDProfileTable": alaVfcWREDProfileTable,
       "alaVfcWREDProfileEntry": alaVfcWREDProfileEntry,
       "alaVfcWRPId": alaVfcWRPId,
       "alaVfcWRPAdminState": alaVfcWRPAdminState,
       "alaVfcWRPName": alaVfcWRPName,
       "alaVfcWRPGreenMinThreshold": alaVfcWRPGreenMinThreshold,
       "alaVfcWRPGreenMaxThreshold": alaVfcWRPGreenMaxThreshold,
       "alaVfcWRPGreenMaxDropProbability": alaVfcWRPGreenMaxDropProbability,
       "alaVfcWRPGreenGain": alaVfcWRPGreenGain,
       "alaVfcWRPYellowMinThreshold": alaVfcWRPYellowMinThreshold,
       "alaVfcWRPYellowMaxThreshold": alaVfcWRPYellowMaxThreshold,
       "alaVfcWRPYellowMaxDropProbability": alaVfcWRPYellowMaxDropProbability,
       "alaVfcWRPYellowGain": alaVfcWRPYellowGain,
       "alaVfcWRPRedMinThreshold": alaVfcWRPRedMinThreshold,
       "alaVfcWRPRedMaxThreshold": alaVfcWRPRedMaxThreshold,
       "alaVfcWRPRedMaxDropProbability": alaVfcWRPRedMaxDropProbability,
       "alaVfcWRPRedGain": alaVfcWRPRedGain,
       "alaVfcWRPStatsAdmin": alaVfcWRPStatsAdmin,
       "alaVfcWRPAttachmentCount": alaVfcWRPAttachmentCount,
       "alaVfcWRPMTU": alaVfcWRPMTU,
       "alaVfcWRPLastChange": alaVfcWRPLastChange,
       "alaVfcWRPRowStatus": alaVfcWRPRowStatus,
       "alaVfcQsetProfileTable": alaVfcQsetProfileTable,
       "alaVfcQsetProfileEntry": alaVfcQsetProfileEntry,
       "alaVfcQSPId": alaVfcQSPId,
       "alaVfcQSPAdminState": alaVfcQSPAdminState,
       "alaVfcQSPName": alaVfcQSPName,
       "alaVfcQSPType": alaVfcQSPType,
       "alaVfcQSPTemplateId": alaVfcQSPTemplateId,
       "alaVfcQSPTemplateName": alaVfcQSPTemplateName,
       "alaVfcQSPBandwidthLimitType": alaVfcQSPBandwidthLimitType,
       "alaVfcQSPBandwidthLimitValue": alaVfcQSPBandwidthLimitValue,
       "alaVfcQSPQueueCount": alaVfcQSPQueueCount,
       "alaVfcQSPWRPId": alaVfcQSPWRPId,
       "alaVfcQSPWRPName": alaVfcQSPWRPName,
       "alaVfcQSPWRPAdminState": alaVfcQSPWRPAdminState,
       "alaVfcQSPSchedulingMethod": alaVfcQSPSchedulingMethod,
       "alaVfcQSPStatsAdmin": alaVfcQSPStatsAdmin,
       "alaVfcQSPAttachmentCount": alaVfcQSPAttachmentCount,
       "alaVfcQSPLastChange": alaVfcQSPLastChange,
       "alaVfcQSPRowStatus": alaVfcQSPRowStatus,
       "alaVfcQsetInstanceTable": alaVfcQsetInstanceTable,
       "alaVfcQsetInstanceEntry": alaVfcQsetInstanceEntry,
       "alaVfcQsetId": alaVfcQsetId,
       "alaVfcQsetQsapId": alaVfcQsetQsapId,
       "alaVfcQsetAdminState": alaVfcQsetAdminState,
       "alaVfcQsetOperState": alaVfcQsetOperState,
       "alaVfcQsetQSPId": alaVfcQsetQSPId,
       "alaVfcQsetQSPName": alaVfcQsetQSPName,
       "alaVfcQsetOperBandwidthLimitType": alaVfcQsetOperBandwidthLimitType,
       "alaVfcQsetOperBandwidthLimitValue": alaVfcQsetOperBandwidthLimitValue,
       "alaVfcQsetBandwidthLimitType": alaVfcQsetBandwidthLimitType,
       "alaVfcQsetBandwidthLimitValue": alaVfcQsetBandwidthLimitValue,
       "alaVfcQsetQueueCount": alaVfcQsetQueueCount,
       "alaVfcQsetWRPId": alaVfcQsetWRPId,
       "alaVfcQsetWRPName": alaVfcQsetWRPName,
       "alaVfcQsetWRPAdminState": alaVfcQsetWRPAdminState,
       "alaVfcQsetWRPOperState": alaVfcQsetWRPOperState,
       "alaVfcQsetSchedulingMethod": alaVfcQsetSchedulingMethod,
       "alaVfcQsetStatsAdmin": alaVfcQsetStatsAdmin,
       "alaVfcQsetStatsOper": alaVfcQsetStatsOper,
       "alaVfcQsetLastChange": alaVfcQsetLastChange,
       "alaVfcQsetStatsClear": alaVfcQsetStatsClear,
       "alaVfcQsetStatsInterval": alaVfcQsetStatsInterval,
       "alaVfcQsetMisconfigured": alaVfcQsetMisconfigured,
       "alaVfcQsetMode": alaVfcQsetMode,
       "alaVfcQProfileTable": alaVfcQProfileTable,
       "alaVfcQProfileEntry": alaVfcQProfileEntry,
       "alaVfcQPQSPId": alaVfcQPQSPId,
       "alaVfcQPQId": alaVfcQPQId,
       "alaVfcQPAdminState": alaVfcQPAdminState,
       "alaVfcQPWRPId": alaVfcQPWRPId,
       "alaVfcQPWRPName": alaVfcQPWRPName,
       "alaVfcQPWRPAdminState": alaVfcQPWRPAdminState,
       "alaVfcQPQSPName": alaVfcQPQSPName,
       "alaVfcQPTrafficClass": alaVfcQPTrafficClass,
       "alaVfcQPQType": alaVfcQPQType,
       "alaVfcQPCIRBandwidthLimitType": alaVfcQPCIRBandwidthLimitType,
       "alaVfcQPCIRBandwidthLimitValue": alaVfcQPCIRBandwidthLimitValue,
       "alaVfcQPPIRBandwidthLimitType": alaVfcQPPIRBandwidthLimitType,
       "alaVfcQPPIRBandwidthLimitValue": alaVfcQPPIRBandwidthLimitValue,
       "alaVfcQPStatsAdmin": alaVfcQPStatsAdmin,
       "alaVfcQPCbs": alaVfcQPCbs,
       "alaVfcQPMbs": alaVfcQPMbs,
       "alaVfcQPLastChange": alaVfcQPLastChange,
       "alaVfcQPWfqWeight": alaVfcQPWfqWeight,
       "alaVfcQPWfqMode": alaVfcQPWfqMode,
       "alaVfcQInstanceTable": alaVfcQInstanceTable,
       "alaVfcQInstanceEntry": alaVfcQInstanceEntry,
       "alaVfcQInstanceQsiId": alaVfcQInstanceQsiId,
       "alaVfcQInstanceQId": alaVfcQInstanceQId,
       "alaVfcQInstanceQsapId": alaVfcQInstanceQsapId,
       "alaVfcQInstanceQSPId": alaVfcQInstanceQSPId,
       "alaVfcQInstanceQSPName": alaVfcQInstanceQSPName,
       "alaVfcQInstanceAdminState": alaVfcQInstanceAdminState,
       "alaVfcQInstanceOperState": alaVfcQInstanceOperState,
       "alaVfcQInstanceWRPAdminState": alaVfcQInstanceWRPAdminState,
       "alaVfcQInstanceWRPOperState": alaVfcQInstanceWRPOperState,
       "alaVfcQInstanceWRPId": alaVfcQInstanceWRPId,
       "alaVfcQInstanceWRPName": alaVfcQInstanceWRPName,
       "alaVfcQInstanceCIRBandwidthLimitType": alaVfcQInstanceCIRBandwidthLimitType,
       "alaVfcQInstanceCIRBandwidthLimitValue": alaVfcQInstanceCIRBandwidthLimitValue,
       "alaVfcQInstancePIRBandwidthLimitType": alaVfcQInstancePIRBandwidthLimitType,
       "alaVfcQInstancePIRBandwidthLimitValue": alaVfcQInstancePIRBandwidthLimitValue,
       "alaVfcQInstanceCIROperationalBandwidthLimitType": alaVfcQInstanceCIROperationalBandwidthLimitType,
       "alaVfcQInstanceCIROperationalBandwidthLimitValue": alaVfcQInstanceCIROperationalBandwidthLimitValue,
       "alaVfcQInstancePIROperationalBandwidthLimitType": alaVfcQInstancePIROperationalBandwidthLimitType,
       "alaVfcQInstancePIROperationalBandwidthLimitValue": alaVfcQInstancePIROperationalBandwidthLimitValue,
       "alaVfcQInstanceStatsAdmin": alaVfcQInstanceStatsAdmin,
       "alaVfcQInstanceStatsOper": alaVfcQInstanceStatsOper,
       "alaVfcQInstancePacketsEnqueued": alaVfcQInstancePacketsEnqueued,
       "alaVfcQInstanceBytesEnqueued": alaVfcQInstanceBytesEnqueued,
       "alaVfcQInstancePacketsDequeued": alaVfcQInstancePacketsDequeued,
       "alaVfcQInstanceBytesDequeued": alaVfcQInstanceBytesDequeued,
       "alaVfcQInstancePacketsDropped": alaVfcQInstancePacketsDropped,
       "alaVfcQInstanceBytesDropped": alaVfcQInstanceBytesDropped,
       "alaVfcQInstanceGreenPacketsAccepted": alaVfcQInstanceGreenPacketsAccepted,
       "alaVfcQInstanceGreenBytesAccepted": alaVfcQInstanceGreenBytesAccepted,
       "alaVfcQInstanceGreenPacketsDropped": alaVfcQInstanceGreenPacketsDropped,
       "alaVfcQInstanceGreenBytesDropped": alaVfcQInstanceGreenBytesDropped,
       "alaVfcQInstanceYellowPacketsAccepted": alaVfcQInstanceYellowPacketsAccepted,
       "alaVfcQInstanceYellowBytesAccepted": alaVfcQInstanceYellowBytesAccepted,
       "alaVfcQInstanceYellowPacketsDropped": alaVfcQInstanceYellowPacketsDropped,
       "alaVfcQInstanceYellowBytesDropped": alaVfcQInstanceYellowBytesDropped,
       "alaVfcQInstanceRedPacketsAccepted": alaVfcQInstanceRedPacketsAccepted,
       "alaVfcQInstanceRedBytesAccepted": alaVfcQInstanceRedBytesAccepted,
       "alaVfcQInstanceRedPacketsDropped": alaVfcQInstanceRedPacketsDropped,
       "alaVfcQInstanceRedBytesDropped": alaVfcQInstanceRedBytesDropped,
       "alaVfcQInstanceLastChange": alaVfcQInstanceLastChange,
       "alaVfcQInstanceStatsClear": alaVfcQInstanceStatsClear,
       "alaVfcQsapTable": alaVfcQsapTable,
       "alaVfcQsapEntry": alaVfcQsapEntry,
       "alaVfcQsapId": alaVfcQsapId,
       "alaVfcQsapAdminState": alaVfcQsapAdminState,
       "alaVfcQsapType": alaVfcQsapType,
       "alaVfcQsapValue": alaVfcQsapValue,
       "alaVfcQsapQSPId": alaVfcQsapQSPId,
       "alaVfcQsapQSPName": alaVfcQsapQSPName,
       "alaVfcQsapWRPAdminState": alaVfcQsapWRPAdminState,
       "alaVfcQsapStatsAdmin": alaVfcQsapStatsAdmin,
       "alaVfcQsapBandwidthLimitType": alaVfcQsapBandwidthLimitType,
       "alaVfcQsapBandwidthLimitValue": alaVfcQsapBandwidthLimitValue,
       "alaVfcQsapClearStats": alaVfcQsapClearStats,
       "alaVfcQsapQpId": alaVfcQsapQpId,
       "alaVfcQsapAction": alaVfcQsapAction,
       "alaVfcQsapLastChange": alaVfcQsapLastChange,
       "alaVfcQsapParent": alaVfcQsapParent,
       "alaVfcProfileIndexLookupTable": alaVfcProfileIndexLookupTable,
       "alaVfcProfileIndexLookupEntry": alaVfcProfileIndexLookupEntry,
       "alaVfcProfileType": alaVfcProfileType,
       "alaVfcProfileName": alaVfcProfileName,
       "alaVfcProfileId": alaVfcProfileId,
       "alaVfcProfileQsapLookupTable": alaVfcProfileQsapLookupTable,
       "alaVfcProfileQsapLookupEntry": alaVfcProfileQsapLookupEntry,
       "alaVfcProfileQsapLookupType": alaVfcProfileQsapLookupType,
       "alaVfcProfileQsapLookupId": alaVfcProfileQsapLookupId,
       "alaVfcProfileQsapLookupValue": alaVfcProfileQsapLookupValue,
       "alaVfcProfileQsapLookupList": alaVfcProfileQsapLookupList,
       "alaVfcQSIQsapLookupTable": alaVfcQSIQsapLookupTable,
       "alaVfcQSIQsapLookupEntry": alaVfcQSIQsapLookupEntry,
       "alaVfcQSIQsapLookupQsetId": alaVfcQSIQsapLookupQsetId,
       "alaVfcQSIQsapLookupValue": alaVfcQSIQsapLookupValue,
       "alaVfcQSIQsapLookupList": alaVfcQSIQsapLookupList,
       "alaVfcStatisticsCollectionInterval": alaVfcStatisticsCollectionInterval,
       "alaVfcStatisticsCollectionDuration": alaVfcStatisticsCollectionDuration,
       "alaVfcConformance": alaVfcConformance,
       "alcatelIND1VfcMIBConformance": alcatelIND1VfcMIBConformance,
       "alcatelIND1VfcMIBGroups": alcatelIND1VfcMIBGroups,
       "alaVfcWREDProfileGroup": alaVfcWREDProfileGroup,
       "alaVfcQsetProfileGroup": alaVfcQsetProfileGroup,
       "alaVfcQsetInstanceGroup": alaVfcQsetInstanceGroup,
       "alaVfcQProfileGroup": alaVfcQProfileGroup,
       "alaVfcQInstanceGroup": alaVfcQInstanceGroup,
       "alaVfcQsapGroup": alaVfcQsapGroup,
       "alaVfcProfileIndexLookupGroup": alaVfcProfileIndexLookupGroup,
       "alaVfcProfileQsapLookupGroup": alaVfcProfileQsapLookupGroup,
       "alaVfcQSIQsapLookupGroup": alaVfcQSIQsapLookupGroup,
       "alaVfcStatsGroup": alaVfcStatsGroup,
       "alcatelIND1VfcMIBCompliances": alcatelIND1VfcMIBCompliances,
       "alcatelIND1VfcMIBCompliance": alcatelIND1VfcMIBCompliance}
)
