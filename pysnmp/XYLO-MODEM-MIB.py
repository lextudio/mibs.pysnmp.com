# SNMP MIB module (XYLO-MODEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XYLO-MODEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:19:32 2024
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

(anxModem,) = mibBuilder.importSymbols(
    "XYLO-MIB-SMI",
    "anxModem")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MdmIdObjects_ObjectIdentity = ObjectIdentity
mdmIdObjects = _MdmIdObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 2, 100, 3)
)
_MdmIdTable_Object = MibTable
mdmIdTable = _MdmIdTable_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 100, 3, 1)
)
if mibBuilder.loadTexts:
    mdmIdTable.setStatus("mandatory")
_MdmIdEntry_Object = MibTableRow
mdmIdEntry = _MdmIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 100, 3, 1, 1)
)
mdmIdEntry.setIndexNames(
    (0, "XYLO-MODEM-MIB", "mdmNumber"),
)
if mibBuilder.loadTexts:
    mdmIdEntry.setStatus("mandatory")


class _MdmNumber_Type(Integer32):
    """Custom type mdmNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MdmNumber_Type.__name__ = "Integer32"
_MdmNumber_Object = MibTableColumn
mdmNumber = _MdmNumber_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 100, 3, 1, 1, 1),
    _MdmNumber_Type()
)
mdmNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmNumber.setStatus("mandatory")


class _MdmIdHardwareRev_Type(DisplayString):
    """Custom type mdmIdHardwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_MdmIdHardwareRev_Type.__name__ = "DisplayString"
_MdmIdHardwareRev_Object = MibTableColumn
mdmIdHardwareRev = _MdmIdHardwareRev_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 100, 3, 1, 1, 2),
    _MdmIdHardwareRev_Type()
)
mdmIdHardwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmIdHardwareRev.setStatus("mandatory")


class _MdmIdSoftwareRev_Type(DisplayString):
    """Custom type mdmIdSoftwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_MdmIdSoftwareRev_Type.__name__ = "DisplayString"
_MdmIdSoftwareRev_Object = MibTableColumn
mdmIdSoftwareRev = _MdmIdSoftwareRev_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 100, 3, 1, 1, 3),
    _MdmIdSoftwareRev_Type()
)
mdmIdSoftwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmIdSoftwareRev.setStatus("mandatory")


class _MdmId56kProprietaryCode_Type(Integer32):
    """Custom type mdmId56kProprietaryCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("k56flex-v34", 3),
          ("none", 1),
          ("x2-v34", 2))
    )


_MdmId56kProprietaryCode_Type.__name__ = "Integer32"
_MdmId56kProprietaryCode_Object = MibScalar
mdmId56kProprietaryCode = _MdmId56kProprietaryCode_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 100, 3, 2),
    _MdmId56kProprietaryCode_Type()
)
mdmId56kProprietaryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmId56kProprietaryCode.setStatus("mandatory")
_MdmCtlObjects_ObjectIdentity = ObjectIdentity
mdmCtlObjects = _MdmCtlObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 2, 100, 4)
)


class _MdmCtlResetAll_Type(Integer32):
    """Custom type mdmCtlResetAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_MdmCtlResetAll_Type.__name__ = "Integer32"
_MdmCtlResetAll_Object = MibScalar
mdmCtlResetAll = _MdmCtlResetAll_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 100, 4, 1),
    _MdmCtlResetAll_Type()
)
mdmCtlResetAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCtlResetAll.setStatus("mandatory")


class _MdmCtlReadConfig_Type(Integer32):
    """Custom type mdmCtlReadConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_MdmCtlReadConfig_Type.__name__ = "Integer32"
_MdmCtlReadConfig_Object = MibScalar
mdmCtlReadConfig = _MdmCtlReadConfig_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 100, 4, 2),
    _MdmCtlReadConfig_Type()
)
mdmCtlReadConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCtlReadConfig.setStatus("mandatory")
_MdmCtlTable_Object = MibTable
mdmCtlTable = _MdmCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 100, 4, 3)
)
if mibBuilder.loadTexts:
    mdmCtlTable.setStatus("mandatory")
_MdmCtlEntry_Object = MibTableRow
mdmCtlEntry = _MdmCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 100, 4, 3, 1)
)
mdmCtlEntry.setIndexNames(
    (0, "XYLO-MODEM-MIB", "mdmNumber"),
)
if mibBuilder.loadTexts:
    mdmCtlEntry.setStatus("mandatory")


class _MdmCtlReset_Type(Integer32):
    """Custom type mdmCtlReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_MdmCtlReset_Type.__name__ = "Integer32"
_MdmCtlReset_Object = MibTableColumn
mdmCtlReset = _MdmCtlReset_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 100, 4, 3, 1, 1),
    _MdmCtlReset_Type()
)
mdmCtlReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCtlReset.setStatus("mandatory")


class _MdmCtlState_Type(Integer32):
    """Custom type mdmCtlState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("available", 2),
          ("busiedOut", 3),
          ("busy", 1),
          ("crashed", 5),
          ("failed", 4),
          ("outOfService", 6))
    )


_MdmCtlState_Type.__name__ = "Integer32"
_MdmCtlState_Object = MibTableColumn
mdmCtlState = _MdmCtlState_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 100, 4, 3, 1, 2),
    _MdmCtlState_Type()
)
mdmCtlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCtlState.setStatus("mandatory")


class _MdmCtlResetModemThresh_Type(Integer32):
    """Custom type mdmCtlResetModemThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MdmCtlResetModemThresh_Type.__name__ = "Integer32"
_MdmCtlResetModemThresh_Object = MibScalar
mdmCtlResetModemThresh = _MdmCtlResetModemThresh_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 100, 4, 4),
    _MdmCtlResetModemThresh_Type()
)
mdmCtlResetModemThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCtlResetModemThresh.setStatus("mandatory")
_MdmStatsObjects_ObjectIdentity = ObjectIdentity
mdmStatsObjects = _MdmStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 2, 100, 7)
)
_MdmStatTable_Object = MibTable
mdmStatTable = _MdmStatTable_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 100, 7, 1)
)
if mibBuilder.loadTexts:
    mdmStatTable.setStatus("mandatory")
_MdmStatEntry_Object = MibTableRow
mdmStatEntry = _MdmStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 100, 7, 1, 1)
)
mdmStatEntry.setIndexNames(
    (0, "XYLO-MODEM-MIB", "mdmNumber"),
)
if mibBuilder.loadTexts:
    mdmStatEntry.setStatus("mandatory")
_MdmStatAssign_Type = Counter32
_MdmStatAssign_Object = MibTableColumn
mdmStatAssign = _MdmStatAssign_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 100, 7, 1, 1, 1),
    _MdmStatAssign_Type()
)
mdmStatAssign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmStatAssign.setStatus("mandatory")
_MdmStatChat_Type = Counter32
_MdmStatChat_Object = MibTableColumn
mdmStatChat = _MdmStatChat_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 100, 7, 1, 1, 2),
    _MdmStatChat_Type()
)
mdmStatChat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmStatChat.setStatus("mandatory")
_MdmStatDcd_Type = Counter32
_MdmStatDcd_Object = MibTableColumn
mdmStatDcd = _MdmStatDcd_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 100, 7, 1, 1, 3),
    _MdmStatDcd_Type()
)
mdmStatDcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmStatDcd.setStatus("mandatory")
_MdmStatConsecFail_Type = Counter32
_MdmStatConsecFail_Object = MibTableColumn
mdmStatConsecFail = _MdmStatConsecFail_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 100, 7, 1, 1, 4),
    _MdmStatConsecFail_Type()
)
mdmStatConsecFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmStatConsecFail.setStatus("mandatory")


class _MdmStatStatus_Type(Integer32):
    """Custom type mdmStatStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("available", 2),
          ("busiedOut", 3),
          ("busy", 1),
          ("crashed", 5),
          ("failed", 4),
          ("outOfService", 6))
    )


_MdmStatStatus_Type.__name__ = "Integer32"
_MdmStatStatus_Object = MibTableColumn
mdmStatStatus = _MdmStatStatus_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 100, 7, 1, 1, 5),
    _MdmStatStatus_Type()
)
mdmStatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmStatStatus.setStatus("mandatory")
_MdmStatTotCalls_Type = Counter32
_MdmStatTotCalls_Object = MibTableColumn
mdmStatTotCalls = _MdmStatTotCalls_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 100, 7, 1, 1, 6),
    _MdmStatTotCalls_Type()
)
mdmStatTotCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmStatTotCalls.setStatus("mandatory")
_MdmStatTotFailures_Type = Counter32
_MdmStatTotFailures_Object = MibTableColumn
mdmStatTotFailures = _MdmStatTotFailures_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 100, 7, 1, 1, 7),
    _MdmStatTotFailures_Type()
)
mdmStatTotFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmStatTotFailures.setStatus("mandatory")
_MdmAvailModems_Type = Integer32
_MdmAvailModems_Object = MibScalar
mdmAvailModems = _MdmAvailModems_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 100, 7, 2),
    _MdmAvailModems_Type()
)
mdmAvailModems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmAvailModems.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XYLO-MODEM-MIB",
    **{"mdmIdObjects": mdmIdObjects,
       "mdmIdTable": mdmIdTable,
       "mdmIdEntry": mdmIdEntry,
       "mdmNumber": mdmNumber,
       "mdmIdHardwareRev": mdmIdHardwareRev,
       "mdmIdSoftwareRev": mdmIdSoftwareRev,
       "mdmId56kProprietaryCode": mdmId56kProprietaryCode,
       "mdmCtlObjects": mdmCtlObjects,
       "mdmCtlResetAll": mdmCtlResetAll,
       "mdmCtlReadConfig": mdmCtlReadConfig,
       "mdmCtlTable": mdmCtlTable,
       "mdmCtlEntry": mdmCtlEntry,
       "mdmCtlReset": mdmCtlReset,
       "mdmCtlState": mdmCtlState,
       "mdmCtlResetModemThresh": mdmCtlResetModemThresh,
       "mdmStatsObjects": mdmStatsObjects,
       "mdmStatTable": mdmStatTable,
       "mdmStatEntry": mdmStatEntry,
       "mdmStatAssign": mdmStatAssign,
       "mdmStatChat": mdmStatChat,
       "mdmStatDcd": mdmStatDcd,
       "mdmStatConsecFail": mdmStatConsecFail,
       "mdmStatStatus": mdmStatStatus,
       "mdmStatTotCalls": mdmStatTotCalls,
       "mdmStatTotFailures": mdmStatTotFailures,
       "mdmAvailModems": mdmAvailModems}
)
