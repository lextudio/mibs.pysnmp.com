# SNMP MIB module (XYLAN-ASCONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XYLAN-ASCONFIG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:18:52 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(xylanAscCArch,) = mibBuilder.importSymbols(
    "XYLAN-BASE-MIB",
    "xylanAscCArch")


# MODULE-IDENTITY


# Types definitions



class AscSnapshotAction(Integer32):
    """Custom type AscSnapshotAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("excludeFromSnapshot", 1),
          ("includeInSnapshot", 2))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AscfgControl_ObjectIdentity = ObjectIdentity
ascfgControl = _AscfgControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 21, 1)
)


class _AscfgInputFileName_Type(DisplayString):
    """Custom type ascfgInputFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AscfgInputFileName_Type.__name__ = "DisplayString"
_AscfgInputFileName_Object = MibScalar
ascfgInputFileName = _AscfgInputFileName_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 21, 1, 1),
    _AscfgInputFileName_Type()
)
ascfgInputFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ascfgInputFileName.setStatus("mandatory")


class _AscfgAction_Type(Integer32):
    """Custom type ascfgAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("checkSyntax", 2),
          ("checkSyntaxAndApply", 3),
          ("noneAvail", 1))
    )


_AscfgAction_Type.__name__ = "Integer32"
_AscfgAction_Object = MibScalar
ascfgAction = _AscfgAction_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 21, 1, 2),
    _AscfgAction_Type()
)
ascfgAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ascfgAction.setStatus("mandatory")


class _AscfgErrorFileName_Type(DisplayString):
    """Custom type ascfgErrorFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AscfgErrorFileName_Type.__name__ = "DisplayString"
_AscfgErrorFileName_Object = MibScalar
ascfgErrorFileName = _AscfgErrorFileName_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 21, 1, 3),
    _AscfgErrorFileName_Type()
)
ascfgErrorFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ascfgErrorFileName.setStatus("mandatory")


class _AscfgStatus_Type(Integer32):
    """Custom type ascfgStatus based on Integer32"""
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
        *(("completeErrors", 4),
          ("completeNoErrors", 3),
          ("inProgress", 2),
          ("noneAvail", 1))
    )


_AscfgStatus_Type.__name__ = "Integer32"
_AscfgStatus_Object = MibScalar
ascfgStatus = _AscfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 21, 1, 4),
    _AscfgStatus_Type()
)
ascfgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ascfgStatus.setStatus("mandatory")
_AscfgErrors_Type = Integer32
_AscfgErrors_Object = MibScalar
ascfgErrors = _AscfgErrors_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 21, 1, 5),
    _AscfgErrors_Type()
)
ascfgErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ascfgErrors.setStatus("mandatory")


class _AscfgTimerFileName_Type(DisplayString):
    """Custom type ascfgTimerFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_AscfgTimerFileName_Type.__name__ = "DisplayString"
_AscfgTimerFileName_Object = MibScalar
ascfgTimerFileName = _AscfgTimerFileName_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 21, 1, 6),
    _AscfgTimerFileName_Type()
)
ascfgTimerFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ascfgTimerFileName.setStatus("mandatory")


class _AscfgTimerFileTime_Type(DisplayString):
    """Custom type ascfgTimerFileTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AscfgTimerFileTime_Type.__name__ = "DisplayString"
_AscfgTimerFileTime_Object = MibScalar
ascfgTimerFileTime = _AscfgTimerFileTime_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 21, 1, 7),
    _AscfgTimerFileTime_Type()
)
ascfgTimerFileTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ascfgTimerFileTime.setStatus("mandatory")


class _AscfgTimerFileStatus_Type(Integer32):
    """Custom type ascfgTimerFileStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("inprogress", 3),
          ("pending", 2))
    )


_AscfgTimerFileStatus_Type.__name__ = "Integer32"
_AscfgTimerFileStatus_Object = MibScalar
ascfgTimerFileStatus = _AscfgTimerFileStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 21, 1, 8),
    _AscfgTimerFileStatus_Type()
)
ascfgTimerFileStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ascfgTimerFileStatus.setStatus("mandatory")
_AscfgTimerClear_Type = Integer32
_AscfgTimerClear_Object = MibScalar
ascfgTimerClear = _AscfgTimerClear_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 21, 1, 9),
    _AscfgTimerClear_Type()
)
ascfgTimerClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ascfgTimerClear.setStatus("mandatory")


class _AscfgSnapshotFileName_Type(DisplayString):
    """Custom type ascfgSnapshotFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_AscfgSnapshotFileName_Type.__name__ = "DisplayString"
_AscfgSnapshotFileName_Object = MibScalar
ascfgSnapshotFileName = _AscfgSnapshotFileName_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 21, 1, 10),
    _AscfgSnapshotFileName_Type()
)
ascfgSnapshotFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ascfgSnapshotFileName.setStatus("mandatory")
_AscfgSnapshotInitiate_Type = Integer32
_AscfgSnapshotInitiate_Object = MibScalar
ascfgSnapshotInitiate = _AscfgSnapshotInitiate_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 21, 1, 11),
    _AscfgSnapshotInitiate_Type()
)
ascfgSnapshotInitiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ascfgSnapshotInitiate.setStatus("mandatory")
_AscfgSnapshotIpSelect_Type = AscSnapshotAction
_AscfgSnapshotIpSelect_Object = MibScalar
ascfgSnapshotIpSelect = _AscfgSnapshotIpSelect_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 21, 1, 12),
    _AscfgSnapshotIpSelect_Type()
)
ascfgSnapshotIpSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ascfgSnapshotIpSelect.setStatus("mandatory")
_AscfgSnapshotIpxSelect_Type = AscSnapshotAction
_AscfgSnapshotIpxSelect_Object = MibScalar
ascfgSnapshotIpxSelect = _AscfgSnapshotIpxSelect_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 21, 1, 13),
    _AscfgSnapshotIpxSelect_Type()
)
ascfgSnapshotIpxSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ascfgSnapshotIpxSelect.setStatus("mandatory")
_AscfgSnapshotSystemSelect_Type = AscSnapshotAction
_AscfgSnapshotSystemSelect_Object = MibScalar
ascfgSnapshotSystemSelect = _AscfgSnapshotSystemSelect_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 21, 1, 14),
    _AscfgSnapshotSystemSelect_Type()
)
ascfgSnapshotSystemSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ascfgSnapshotSystemSelect.setStatus("mandatory")
_AscfgSnapshotSnmpSelect_Type = AscSnapshotAction
_AscfgSnapshotSnmpSelect_Object = MibScalar
ascfgSnapshotSnmpSelect = _AscfgSnapshotSnmpSelect_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 21, 1, 15),
    _AscfgSnapshotSnmpSelect_Type()
)
ascfgSnapshotSnmpSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ascfgSnapshotSnmpSelect.setStatus("mandatory")
_AscfgSnapshotAtmSelect_Type = AscSnapshotAction
_AscfgSnapshotAtmSelect_Object = MibScalar
ascfgSnapshotAtmSelect = _AscfgSnapshotAtmSelect_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 21, 1, 16),
    _AscfgSnapshotAtmSelect_Type()
)
ascfgSnapshotAtmSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ascfgSnapshotAtmSelect.setStatus("mandatory")
_AscfgSnapshotVlanSelect_Type = AscSnapshotAction
_AscfgSnapshotVlanSelect_Object = MibScalar
ascfgSnapshotVlanSelect = _AscfgSnapshotVlanSelect_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 21, 1, 18),
    _AscfgSnapshotVlanSelect_Type()
)
ascfgSnapshotVlanSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ascfgSnapshotVlanSelect.setStatus("mandatory")
_AscfgSnapshotInterfaceSelect_Type = AscSnapshotAction
_AscfgSnapshotInterfaceSelect_Object = MibScalar
ascfgSnapshotInterfaceSelect = _AscfgSnapshotInterfaceSelect_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 21, 1, 19),
    _AscfgSnapshotInterfaceSelect_Type()
)
ascfgSnapshotInterfaceSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ascfgSnapshotInterfaceSelect.setStatus("mandatory")
_AscfgSnapshotBrdgSelect_Type = AscSnapshotAction
_AscfgSnapshotBrdgSelect_Object = MibScalar
ascfgSnapshotBrdgSelect = _AscfgSnapshotBrdgSelect_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 21, 1, 20),
    _AscfgSnapshotBrdgSelect_Type()
)
ascfgSnapshotBrdgSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ascfgSnapshotBrdgSelect.setStatus("mandatory")
_AscfgSnapshotAllSelect_Type = AscSnapshotAction
_AscfgSnapshotAllSelect_Object = MibScalar
ascfgSnapshotAllSelect = _AscfgSnapshotAllSelect_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 21, 1, 21),
    _AscfgSnapshotAllSelect_Type()
)
ascfgSnapshotAllSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ascfgSnapshotAllSelect.setStatus("mandatory")
_AscfgSnapshotSelectSummary_Type = Integer32
_AscfgSnapshotSelectSummary_Object = MibScalar
ascfgSnapshotSelectSummary = _AscfgSnapshotSelectSummary_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 21, 1, 22),
    _AscfgSnapshotSelectSummary_Type()
)
ascfgSnapshotSelectSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ascfgSnapshotSelectSummary.setStatus("mandatory")


class _AscfgCommandStr_Type(DisplayString):
    """Custom type ascfgCommandStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AscfgCommandStr_Type.__name__ = "DisplayString"
_AscfgCommandStr_Object = MibScalar
ascfgCommandStr = _AscfgCommandStr_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 21, 1, 23),
    _AscfgCommandStr_Type()
)
ascfgCommandStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ascfgCommandStr.setStatus("mandatory")


class _AscfgCommandStatus_Type(Integer32):
    """Custom type ascfgCommandStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failure", 1),
          ("success", 2))
    )


_AscfgCommandStatus_Type.__name__ = "Integer32"
_AscfgCommandStatus_Object = MibScalar
ascfgCommandStatus = _AscfgCommandStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 21, 1, 24),
    _AscfgCommandStatus_Type()
)
ascfgCommandStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ascfgCommandStatus.setStatus("mandatory")
_AscfgSaveConfiguration_Type = Integer32
_AscfgSaveConfiguration_Object = MibScalar
ascfgSaveConfiguration = _AscfgSaveConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 21, 1, 25),
    _AscfgSaveConfiguration_Type()
)
ascfgSaveConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ascfgSaveConfiguration.setStatus("mandatory")


class _AscfgConfigurationFileName_Type(DisplayString):
    """Custom type ascfgConfigurationFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_AscfgConfigurationFileName_Type.__name__ = "DisplayString"
_AscfgConfigurationFileName_Object = MibScalar
ascfgConfigurationFileName = _AscfgConfigurationFileName_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 21, 1, 26),
    _AscfgConfigurationFileName_Type()
)
ascfgConfigurationFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ascfgConfigurationFileName.setStatus("mandatory")


class _AscfgCacheOnly_Type(Integer32):
    """Custom type ascfgCacheOnly based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_AscfgCacheOnly_Type.__name__ = "Integer32"
_AscfgCacheOnly_Object = MibScalar
ascfgCacheOnly = _AscfgCacheOnly_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 21, 1, 27),
    _AscfgCacheOnly_Type()
)
ascfgCacheOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ascfgCacheOnly.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XYLAN-ASCONFIG-MIB",
    **{"AscSnapshotAction": AscSnapshotAction,
       "ascfgControl": ascfgControl,
       "ascfgInputFileName": ascfgInputFileName,
       "ascfgAction": ascfgAction,
       "ascfgErrorFileName": ascfgErrorFileName,
       "ascfgStatus": ascfgStatus,
       "ascfgErrors": ascfgErrors,
       "ascfgTimerFileName": ascfgTimerFileName,
       "ascfgTimerFileTime": ascfgTimerFileTime,
       "ascfgTimerFileStatus": ascfgTimerFileStatus,
       "ascfgTimerClear": ascfgTimerClear,
       "ascfgSnapshotFileName": ascfgSnapshotFileName,
       "ascfgSnapshotInitiate": ascfgSnapshotInitiate,
       "ascfgSnapshotIpSelect": ascfgSnapshotIpSelect,
       "ascfgSnapshotIpxSelect": ascfgSnapshotIpxSelect,
       "ascfgSnapshotSystemSelect": ascfgSnapshotSystemSelect,
       "ascfgSnapshotSnmpSelect": ascfgSnapshotSnmpSelect,
       "ascfgSnapshotAtmSelect": ascfgSnapshotAtmSelect,
       "ascfgSnapshotVlanSelect": ascfgSnapshotVlanSelect,
       "ascfgSnapshotInterfaceSelect": ascfgSnapshotInterfaceSelect,
       "ascfgSnapshotBrdgSelect": ascfgSnapshotBrdgSelect,
       "ascfgSnapshotAllSelect": ascfgSnapshotAllSelect,
       "ascfgSnapshotSelectSummary": ascfgSnapshotSelectSummary,
       "ascfgCommandStr": ascfgCommandStr,
       "ascfgCommandStatus": ascfgCommandStatus,
       "ascfgSaveConfiguration": ascfgSaveConfiguration,
       "ascfgConfigurationFileName": ascfgConfigurationFileName,
       "ascfgCacheOnly": ascfgCacheOnly}
)
