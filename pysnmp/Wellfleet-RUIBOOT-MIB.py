# SNMP MIB module (Wellfleet-RUIBOOT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-RUIBOOT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:03 2024
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
 Opaque,
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso,
 mgmt,
 mib_2) = mibBuilder.importSymbols(
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
    "Opaque",
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso",
    "mgmt",
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(wfRuiBootGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfRuiBootGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfRuiBoot_ObjectIdentity = ObjectIdentity
wfRuiBoot = _WfRuiBoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 14, 1)
)


class _WfRuiBootBaseDelete_Type(Integer32):
    """Custom type wfRuiBootBaseDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfRuiBootBaseDelete_Type.__name__ = "Integer32"
_WfRuiBootBaseDelete_Object = MibScalar
wfRuiBootBaseDelete = _WfRuiBootBaseDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 14, 1, 1),
    _WfRuiBootBaseDelete_Type()
)
wfRuiBootBaseDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRuiBootBaseDelete.setStatus("mandatory")


class _WfRuiBootBaseDisable_Type(Integer32):
    """Custom type wfRuiBootBaseDisable based on Integer32"""
    defaultValue = 1

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


_WfRuiBootBaseDisable_Type.__name__ = "Integer32"
_WfRuiBootBaseDisable_Object = MibScalar
wfRuiBootBaseDisable = _WfRuiBootBaseDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 14, 1, 2),
    _WfRuiBootBaseDisable_Type()
)
wfRuiBootBaseDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRuiBootBaseDisable.setStatus("mandatory")


class _WfRuiBootBaseState_Type(Integer32):
    """Custom type wfRuiBootBaseState based on Integer32"""
    defaultValue = 4

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
        *(("down", 2),
          ("init", 3),
          ("notpres", 4),
          ("up", 1))
    )


_WfRuiBootBaseState_Type.__name__ = "Integer32"
_WfRuiBootBaseState_Object = MibScalar
wfRuiBootBaseState = _WfRuiBootBaseState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 14, 1, 3),
    _WfRuiBootBaseState_Type()
)
wfRuiBootBaseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRuiBootBaseState.setStatus("mandatory")
_WfRuiBootTable_Object = MibTable
wfRuiBootTable = _WfRuiBootTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 14, 2)
)
if mibBuilder.loadTexts:
    wfRuiBootTable.setStatus("mandatory")
_WfRuiBootEntry_Object = MibTableRow
wfRuiBootEntry = _WfRuiBootEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 14, 2, 1)
)
wfRuiBootEntry.setIndexNames(
    (0, "Wellfleet-RUIBOOT-MIB", "wfRuiBootDateAndTime"),
)
if mibBuilder.loadTexts:
    wfRuiBootEntry.setStatus("mandatory")


class _WfRuiBootDelete_Type(Integer32):
    """Custom type wfRuiBootDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfRuiBootDelete_Type.__name__ = "Integer32"
_WfRuiBootDelete_Object = MibTableColumn
wfRuiBootDelete = _WfRuiBootDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 14, 2, 1, 1),
    _WfRuiBootDelete_Type()
)
wfRuiBootDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRuiBootDelete.setStatus("mandatory")


class _WfRuiBootDisable_Type(Integer32):
    """Custom type wfRuiBootDisable based on Integer32"""
    defaultValue = 1

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


_WfRuiBootDisable_Type.__name__ = "Integer32"
_WfRuiBootDisable_Object = MibTableColumn
wfRuiBootDisable = _WfRuiBootDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 14, 2, 1, 2),
    _WfRuiBootDisable_Type()
)
wfRuiBootDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRuiBootDisable.setStatus("mandatory")


class _WfRuiBootState_Type(Integer32):
    """Custom type wfRuiBootState based on Integer32"""
    defaultValue = 5

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
        *(("aged", 2),
          ("error", 4),
          ("initializing", 5),
          ("scheduled", 1),
          ("time", 3))
    )


_WfRuiBootState_Type.__name__ = "Integer32"
_WfRuiBootState_Object = MibTableColumn
wfRuiBootState = _WfRuiBootState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 14, 2, 1, 3),
    _WfRuiBootState_Type()
)
wfRuiBootState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRuiBootState.setStatus("mandatory")


class _WfRuiBootDateAndTime_Type(OctetString):
    """Custom type wfRuiBootDateAndTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )


_WfRuiBootDateAndTime_Type.__name__ = "OctetString"
_WfRuiBootDateAndTime_Object = MibTableColumn
wfRuiBootDateAndTime = _WfRuiBootDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 14, 2, 1, 4),
    _WfRuiBootDateAndTime_Type()
)
wfRuiBootDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRuiBootDateAndTime.setStatus("mandatory")
_WfRuiBootImageName_Type = DisplayString
_WfRuiBootImageName_Object = MibTableColumn
wfRuiBootImageName = _WfRuiBootImageName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 14, 2, 1, 5),
    _WfRuiBootImageName_Type()
)
wfRuiBootImageName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRuiBootImageName.setStatus("mandatory")
_WfRuiBootConfigName_Type = DisplayString
_WfRuiBootConfigName_Object = MibTableColumn
wfRuiBootConfigName = _WfRuiBootConfigName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 14, 2, 1, 6),
    _WfRuiBootConfigName_Type()
)
wfRuiBootConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRuiBootConfigName.setStatus("mandatory")


class _WfRuiBootErrorCode_Type(Integer32):
    """Custom type wfRuiBootErrorCode based on Integer32"""
    defaultValue = 1

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
        *(("configfilenotfound", 5),
          ("configname", 3),
          ("filesystem", 7),
          ("imagefilecorrupt", 6),
          ("imagefilenotfound", 4),
          ("imagename", 2),
          ("invalidtime", 8),
          ("none", 1))
    )


_WfRuiBootErrorCode_Type.__name__ = "Integer32"
_WfRuiBootErrorCode_Object = MibTableColumn
wfRuiBootErrorCode = _WfRuiBootErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 14, 2, 1, 7),
    _WfRuiBootErrorCode_Type()
)
wfRuiBootErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRuiBootErrorCode.setStatus("mandatory")
_WfRuiBootSystemErrorCode_Type = Integer32
_WfRuiBootSystemErrorCode_Object = MibTableColumn
wfRuiBootSystemErrorCode = _WfRuiBootSystemErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 14, 2, 1, 8),
    _WfRuiBootSystemErrorCode_Type()
)
wfRuiBootSystemErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRuiBootSystemErrorCode.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-RUIBOOT-MIB",
    **{"wfRuiBoot": wfRuiBoot,
       "wfRuiBootBaseDelete": wfRuiBootBaseDelete,
       "wfRuiBootBaseDisable": wfRuiBootBaseDisable,
       "wfRuiBootBaseState": wfRuiBootBaseState,
       "wfRuiBootTable": wfRuiBootTable,
       "wfRuiBootEntry": wfRuiBootEntry,
       "wfRuiBootDelete": wfRuiBootDelete,
       "wfRuiBootDisable": wfRuiBootDisable,
       "wfRuiBootState": wfRuiBootState,
       "wfRuiBootDateAndTime": wfRuiBootDateAndTime,
       "wfRuiBootImageName": wfRuiBootImageName,
       "wfRuiBootConfigName": wfRuiBootConfigName,
       "wfRuiBootErrorCode": wfRuiBootErrorCode,
       "wfRuiBootSystemErrorCode": wfRuiBootSystemErrorCode}
)
