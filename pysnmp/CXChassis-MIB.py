# SNMP MIB module (CXChassis-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXChassis-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:13 2024
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

(cxChassis,
 cxRegChasCX1000) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "cxChassis",
    "cxRegChasCX1000")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _CxChasTrapCard_Type(Integer32):
    """Custom type cxChasTrapCard based on Integer32"""
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


_CxChasTrapCard_Type.__name__ = "Integer32"
_CxChasTrapCard_Object = MibScalar
cxChasTrapCard = _CxChasTrapCard_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 4, 1),
    _CxChasTrapCard_Type()
)
cxChasTrapCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxChasTrapCard.setStatus("mandatory")


class _CxFileTargetSlot_Type(Integer32):
    """Custom type cxFileTargetSlot based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_CxFileTargetSlot_Type.__name__ = "Integer32"
_CxFileTargetSlot_Object = MibScalar
cxFileTargetSlot = _CxFileTargetSlot_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 4, 2),
    _CxFileTargetSlot_Type()
)
cxFileTargetSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxFileTargetSlot.setStatus("mandatory")
_CxChasSubSysTable_Object = MibTable
cxChasSubSysTable = _CxChasSubSysTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 4, 5)
)
if mibBuilder.loadTexts:
    cxChasSubSysTable.setStatus("mandatory")
_CxChasSubSysEntry_Object = MibTableRow
cxChasSubSysEntry = _CxChasSubSysEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 4, 5, 1)
)
cxChasSubSysEntry.setIndexNames(
    (0, "CXChassis-MIB", "cxChasSubSysSlotNb"),
)
if mibBuilder.loadTexts:
    cxChasSubSysEntry.setStatus("mandatory")
_CxChasSubSysSlotNb_Type = Integer32
_CxChasSubSysSlotNb_Object = MibTableColumn
cxChasSubSysSlotNb = _CxChasSubSysSlotNb_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 4, 5, 1, 1),
    _CxChasSubSysSlotNb_Type()
)
cxChasSubSysSlotNb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxChasSubSysSlotNb.setStatus("mandatory")


class _CxChasSubSysDesc_Type(DisplayString):
    """Custom type cxChasSubSysDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CxChasSubSysDesc_Type.__name__ = "DisplayString"
_CxChasSubSysDesc_Object = MibTableColumn
cxChasSubSysDesc = _CxChasSubSysDesc_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 4, 5, 1, 2),
    _CxChasSubSysDesc_Type()
)
cxChasSubSysDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxChasSubSysDesc.setStatus("mandatory")
_CxChasSubSysObjectID_Type = ObjectIdentifier
_CxChasSubSysObjectID_Object = MibTableColumn
cxChasSubSysObjectID = _CxChasSubSysObjectID_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 4, 5, 1, 3),
    _CxChasSubSysObjectID_Type()
)
cxChasSubSysObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxChasSubSysObjectID.setStatus("mandatory")


class _CxChasSubSysName_Type(DisplayString):
    """Custom type cxChasSubSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CxChasSubSysName_Type.__name__ = "DisplayString"
_CxChasSubSysName_Object = MibTableColumn
cxChasSubSysName = _CxChasSubSysName_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 4, 5, 1, 4),
    _CxChasSubSysName_Type()
)
cxChasSubSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxChasSubSysName.setStatus("mandatory")
_CxChasSubSysServices_Type = Integer32
_CxChasSubSysServices_Object = MibTableColumn
cxChasSubSysServices = _CxChasSubSysServices_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 4, 5, 1, 5),
    _CxChasSubSysServices_Type()
)
cxChasSubSysServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxChasSubSysServices.setStatus("mandatory")
_CxChasSubSysVersion_Type = Integer32
_CxChasSubSysVersion_Object = MibTableColumn
cxChasSubSysVersion = _CxChasSubSysVersion_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 4, 5, 1, 6),
    _CxChasSubSysVersion_Type()
)
cxChasSubSysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxChasSubSysVersion.setStatus("mandatory")


class _CxChasSubSysOperState_Type(Integer32):
    """Custom type cxChasSubSysOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noresponse", 1),
          ("responding", 2))
    )


_CxChasSubSysOperState_Type.__name__ = "Integer32"
_CxChasSubSysOperState_Object = MibTableColumn
cxChasSubSysOperState = _CxChasSubSysOperState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 4, 5, 1, 7),
    _CxChasSubSysOperState_Type()
)
cxChasSubSysOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxChasSubSysOperState.setStatus("mandatory")


class _CxChasSubSysConfig_Type(Integer32):
    """Custom type cxChasSubSysConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("writetoflash", 1)
    )


_CxChasSubSysConfig_Type.__name__ = "Integer32"
_CxChasSubSysConfig_Object = MibTableColumn
cxChasSubSysConfig = _CxChasSubSysConfig_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 4, 5, 1, 8),
    _CxChasSubSysConfig_Type()
)
cxChasSubSysConfig.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cxChasSubSysConfig.setStatus("mandatory")


class _CxChasSubSysRestart_Type(Integer32):
    """Custom type cxChasSubSysRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("coldstart", 2),
          ("warmstart-with-save", 1),
          ("warmstart-without-save", 3))
    )


_CxChasSubSysRestart_Type.__name__ = "Integer32"
_CxChasSubSysRestart_Object = MibTableColumn
cxChasSubSysRestart = _CxChasSubSysRestart_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 4, 5, 1, 9),
    _CxChasSubSysRestart_Type()
)
cxChasSubSysRestart.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cxChasSubSysRestart.setStatus("mandatory")


class _ChassisMibLevel_Type(Integer32):
    """Custom type chassisMibLevel based on Integer32"""
    defaultValue = 0


_ChassisMibLevel_Object = MibScalar
chassisMibLevel = _ChassisMibLevel_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 4, 10),
    _ChassisMibLevel_Type()
)
chassisMibLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisMibLevel.setStatus("mandatory")

# Managed Objects groups


# Notification objects

cxChasCardUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 7, 1, 1, 0, 10)
)
cxChasCardUpTrap.setObjects(
    ("CXChassis-MIB", "cxChasSubSysSlotNb")
)
if mibBuilder.loadTexts:
    cxChasCardUpTrap.setStatus(
        ""
    )

cxChasCardDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 7, 1, 1, 0, 11)
)
cxChasCardDownTrap.setObjects(
    ("CXChassis-MIB", "cxChasSubSysSlotNb")
)
if mibBuilder.loadTexts:
    cxChasCardDownTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXChassis-MIB",
    **{"cxChasTrapCard": cxChasTrapCard,
       "cxFileTargetSlot": cxFileTargetSlot,
       "cxChasSubSysTable": cxChasSubSysTable,
       "cxChasSubSysEntry": cxChasSubSysEntry,
       "cxChasSubSysSlotNb": cxChasSubSysSlotNb,
       "cxChasSubSysDesc": cxChasSubSysDesc,
       "cxChasSubSysObjectID": cxChasSubSysObjectID,
       "cxChasSubSysName": cxChasSubSysName,
       "cxChasSubSysServices": cxChasSubSysServices,
       "cxChasSubSysVersion": cxChasSubSysVersion,
       "cxChasSubSysOperState": cxChasSubSysOperState,
       "cxChasSubSysConfig": cxChasSubSysConfig,
       "cxChasSubSysRestart": cxChasSubSysRestart,
       "chassisMibLevel": chassisMibLevel,
       "cxChasCardUpTrap": cxChasCardUpTrap,
       "cxChasCardDownTrap": cxChasCardDownTrap}
)
