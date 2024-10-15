# SNMP MIB module (CISCO-DMN-DSG-DISEQC-DISH-POSITION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DMN-DSG-DISEQC-DISH-POSITION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:20 2024
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

(ciscoDSGUtilities,) = mibBuilder.importSymbols(
    "CISCO-DMN-DSG-ROOT-MIB",
    "ciscoDSGUtilities")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoDSGDiSEqC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 19)
)
ciscoDSGDiSEqC.setRevisions(
        ("2010-08-30 11:00",
         "2010-03-22 05:00",
         "2010-02-12 12:00",
         "2009-12-07 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DiSEqCTable_Object = MibTable
diSEqCTable = _DiSEqCTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 19, 1)
)
if mibBuilder.loadTexts:
    diSEqCTable.setStatus("current")
_DiSEqCEntry_Object = MibTableRow
diSEqCEntry = _DiSEqCEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 19, 1, 1)
)
diSEqCEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-DISEQC-DISH-POSITION-MIB", "diSEqCInstance"),
)
if mibBuilder.loadTexts:
    diSEqCEntry.setStatus("current")


class _DiSEqCInstance_Type(Integer32):
    """Custom type diSEqCInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_DiSEqCInstance_Type.__name__ = "Integer32"
_DiSEqCInstance_Object = MibTableColumn
diSEqCInstance = _DiSEqCInstance_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 19, 1, 1, 1),
    _DiSEqCInstance_Type()
)
diSEqCInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diSEqCInstance.setStatus("current")


class _DiSEqCEnable_Type(Integer32):
    """Custom type diSEqCEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_DiSEqCEnable_Type.__name__ = "Integer32"
_DiSEqCEnable_Object = MibTableColumn
diSEqCEnable = _DiSEqCEnable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 19, 1, 1, 2),
    _DiSEqCEnable_Type()
)
diSEqCEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diSEqCEnable.setStatus("current")


class _DiSEqCDishPosition_Type(Integer32):
    """Custom type diSEqCDishPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 750),
    )


_DiSEqCDishPosition_Type.__name__ = "Integer32"
_DiSEqCDishPosition_Object = MibTableColumn
diSEqCDishPosition = _DiSEqCDishPosition_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 19, 1, 1, 3),
    _DiSEqCDishPosition_Type()
)
diSEqCDishPosition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diSEqCDishPosition.setStatus("current")


class _DiSEqCPositionJog_Type(Integer32):
    """Custom type diSEqCPositionJog based on Integer32"""
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
        *(("coarseAdjustmentEast", 2),
          ("coarseAdjustmentWest", 3),
          ("fineAdjustmentEast", 4),
          ("fineAdjustmentWest", 5),
          ("writeOnly", 1))
    )


_DiSEqCPositionJog_Type.__name__ = "Integer32"
_DiSEqCPositionJog_Object = MibTableColumn
diSEqCPositionJog = _DiSEqCPositionJog_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 19, 1, 1, 4),
    _DiSEqCPositionJog_Type()
)
diSEqCPositionJog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diSEqCPositionJog.setStatus("current")


class _DiSEqCEWFlag_Type(Integer32):
    """Custom type diSEqCEWFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("east", 1),
          ("notApplicable", 3),
          ("west", 2))
    )


_DiSEqCEWFlag_Type.__name__ = "Integer32"
_DiSEqCEWFlag_Object = MibTableColumn
diSEqCEWFlag = _DiSEqCEWFlag_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 19, 1, 1, 5),
    _DiSEqCEWFlag_Type()
)
diSEqCEWFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diSEqCEWFlag.setStatus("current")


class _DiSEqCSatSelect_Type(Integer32):
    """Custom type diSEqCSatSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DiSEqCSatSelect_Type.__name__ = "Integer32"
_DiSEqCSatSelect_Object = MibTableColumn
diSEqCSatSelect = _DiSEqCSatSelect_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 19, 1, 1, 6),
    _DiSEqCSatSelect_Type()
)
diSEqCSatSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diSEqCSatSelect.setStatus("current")


class _DiSEqCInstallerAction_Type(Integer32):
    """Custom type diSEqCInstallerAction based on Integer32"""
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
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("calculatePosition", 13),
          ("clearLimits", 10),
          ("continuousEastMovement", 3),
          ("continuousWestMovement", 2),
          ("gotoAbsolutePositionEast", 6),
          ("gotoAbsolutePositionWest", 5),
          ("gotoReference", 7),
          ("gotoSatellite", 8),
          ("none", 1),
          ("stopMove", 4),
          ("storeEastLimits", 11),
          ("storeSatellite", 9),
          ("storeWestLimits", 12))
    )


_DiSEqCInstallerAction_Type.__name__ = "Integer32"
_DiSEqCInstallerAction_Object = MibTableColumn
diSEqCInstallerAction = _DiSEqCInstallerAction_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 19, 1, 1, 7),
    _DiSEqCInstallerAction_Type()
)
diSEqCInstallerAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diSEqCInstallerAction.setStatus("current")


class _DiSEqCUserAction_Type(Integer32):
    """Custom type diSEqCUserAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gotoSatellite", 2),
          ("none", 1))
    )


_DiSEqCUserAction_Type.__name__ = "Integer32"
_DiSEqCUserAction_Object = MibTableColumn
diSEqCUserAction = _DiSEqCUserAction_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 19, 1, 1, 8),
    _DiSEqCUserAction_Type()
)
diSEqCUserAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diSEqCUserAction.setStatus("current")


class _DiSEqCMode_Type(Integer32):
    """Custom type diSEqCMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("installer", 1),
          ("user", 2))
    )


_DiSEqCMode_Type.__name__ = "Integer32"
_DiSEqCMode_Object = MibTableColumn
diSEqCMode = _DiSEqCMode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 19, 1, 1, 9),
    _DiSEqCMode_Type()
)
diSEqCMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diSEqCMode.setStatus("current")


class _DiSEqCAction_Type(Integer32):
    """Custom type diSEqCAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activate", 2),
          ("writeOnly", 1))
    )


_DiSEqCAction_Type.__name__ = "Integer32"
_DiSEqCAction_Object = MibTableColumn
diSEqCAction = _DiSEqCAction_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 19, 1, 1, 10),
    _DiSEqCAction_Type()
)
diSEqCAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diSEqCAction.setStatus("current")


class _DiSEqCStatusMode_Type(Integer32):
    """Custom type diSEqCStatusMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("installer", 1),
          ("user", 2))
    )


_DiSEqCStatusMode_Type.__name__ = "Integer32"
_DiSEqCStatusMode_Object = MibTableColumn
diSEqCStatusMode = _DiSEqCStatusMode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 19, 1, 1, 11),
    _DiSEqCStatusMode_Type()
)
diSEqCStatusMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diSEqCStatusMode.setStatus("current")


class _DiSEqCStatusDishPosition_Type(DisplayString):
    """Custom type diSEqCStatusDishPosition based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DiSEqCStatusDishPosition_Type.__name__ = "DisplayString"
_DiSEqCStatusDishPosition_Object = MibTableColumn
diSEqCStatusDishPosition = _DiSEqCStatusDishPosition_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 19, 1, 1, 12),
    _DiSEqCStatusDishPosition_Type()
)
diSEqCStatusDishPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diSEqCStatusDishPosition.setStatus("current")


class _DiSEqCStatusEastWestFlag_Type(Integer32):
    """Custom type diSEqCStatusEastWestFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("east", 1),
          ("notApplicable", 3),
          ("west", 2))
    )


_DiSEqCStatusEastWestFlag_Type.__name__ = "Integer32"
_DiSEqCStatusEastWestFlag_Object = MibTableColumn
diSEqCStatusEastWestFlag = _DiSEqCStatusEastWestFlag_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 19, 1, 1, 13),
    _DiSEqCStatusEastWestFlag_Type()
)
diSEqCStatusEastWestFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diSEqCStatusEastWestFlag.setStatus("current")


class _DiSEqCStatusLastAction_Type(Integer32):
    """Custom type diSEqCStatusLastAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("coarseAdjustmenWest", 3),
          ("coarseAdjustmentEast", 2),
          ("fineAdjustmenEast", 4),
          ("fineAdjustmentWest", 5),
          ("installerAction", 6),
          ("userAction", 7))
    )


_DiSEqCStatusLastAction_Type.__name__ = "Integer32"
_DiSEqCStatusLastAction_Object = MibTableColumn
diSEqCStatusLastAction = _DiSEqCStatusLastAction_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 19, 1, 1, 14),
    _DiSEqCStatusLastAction_Type()
)
diSEqCStatusLastAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diSEqCStatusLastAction.setStatus("current")


class _DiSEqCStatusEnable_Type(Integer32):
    """Custom type diSEqCStatusEnable based on Integer32"""
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


_DiSEqCStatusEnable_Type.__name__ = "Integer32"
_DiSEqCStatusEnable_Object = MibTableColumn
diSEqCStatusEnable = _DiSEqCStatusEnable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 19, 1, 1, 15),
    _DiSEqCStatusEnable_Type()
)
diSEqCStatusEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diSEqCStatusEnable.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DMN-DSG-DISEQC-DISH-POSITION-MIB",
    **{"ciscoDSGDiSEqC": ciscoDSGDiSEqC,
       "diSEqCTable": diSEqCTable,
       "diSEqCEntry": diSEqCEntry,
       "diSEqCInstance": diSEqCInstance,
       "diSEqCEnable": diSEqCEnable,
       "diSEqCDishPosition": diSEqCDishPosition,
       "diSEqCPositionJog": diSEqCPositionJog,
       "diSEqCEWFlag": diSEqCEWFlag,
       "diSEqCSatSelect": diSEqCSatSelect,
       "diSEqCInstallerAction": diSEqCInstallerAction,
       "diSEqCUserAction": diSEqCUserAction,
       "diSEqCMode": diSEqCMode,
       "diSEqCAction": diSEqCAction,
       "diSEqCStatusMode": diSEqCStatusMode,
       "diSEqCStatusDishPosition": diSEqCStatusDishPosition,
       "diSEqCStatusEastWestFlag": diSEqCStatusEastWestFlag,
       "diSEqCStatusLastAction": diSEqCStatusLastAction,
       "diSEqCStatusEnable": diSEqCStatusEnable}
)
