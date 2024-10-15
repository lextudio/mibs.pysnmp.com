# SNMP MIB module (ANIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ANIC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:53 2024
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
 enterprises,
 experimental,
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
    "enterprises",
    "experimental",
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

_Usr_ObjectIdentity = ObjectIdentity
usr = _Usr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429)
)
_Nas_ObjectIdentity = ObjectIdentity
nas = _Nas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1)
)
_Anic_ObjectIdentity = ObjectIdentity
anic = _Anic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 7)
)
_AnicCmd_ObjectIdentity = ObjectIdentity
anicCmd = _AnicCmd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 7, 1)
)
_AnicCmdTable_Object = MibTable
anicCmdTable = _AnicCmdTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 7, 1, 1)
)
if mibBuilder.loadTexts:
    anicCmdTable.setStatus("mandatory")
_AnicCmdEntry_Object = MibTableRow
anicCmdEntry = _AnicCmdEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 7, 1, 1, 1)
)
anicCmdEntry.setIndexNames(
    (0, "ANIC-MIB", "anicCmdIndex"),
)
if mibBuilder.loadTexts:
    anicCmdEntry.setStatus("mandatory")
_AnicCmdIndex_Type = Integer32
_AnicCmdIndex_Object = MibTableColumn
anicCmdIndex = _AnicCmdIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 7, 1, 1, 1, 1),
    _AnicCmdIndex_Type()
)
anicCmdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anicCmdIndex.setStatus("mandatory")


class _AnicCmdMgtStationId_Type(OctetString):
    """Custom type anicCmdMgtStationId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AnicCmdMgtStationId_Type.__name__ = "OctetString"
_AnicCmdMgtStationId_Object = MibTableColumn
anicCmdMgtStationId = _AnicCmdMgtStationId_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 7, 1, 1, 1, 2),
    _AnicCmdMgtStationId_Type()
)
anicCmdMgtStationId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anicCmdMgtStationId.setStatus("mandatory")
_AnicCmdReqId_Type = Integer32
_AnicCmdReqId_Object = MibTableColumn
anicCmdReqId = _AnicCmdReqId_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 7, 1, 1, 1, 3),
    _AnicCmdReqId_Type()
)
anicCmdReqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anicCmdReqId.setStatus("mandatory")


class _AnicCmdFunction_Type(Integer32):
    """Custom type anicCmdFunction based on Integer32"""
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
        *(("busyOutPhoneLine", 3),
          ("noCommand", 1),
          ("nonDisruptSelfTest", 2),
          ("restorePhoneLine", 4))
    )


_AnicCmdFunction_Type.__name__ = "Integer32"
_AnicCmdFunction_Object = MibTableColumn
anicCmdFunction = _AnicCmdFunction_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 7, 1, 1, 1, 4),
    _AnicCmdFunction_Type()
)
anicCmdFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anicCmdFunction.setStatus("mandatory")


class _AnicCmdForce_Type(Integer32):
    """Custom type anicCmdForce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("force", 1),
          ("noForce", 2))
    )


_AnicCmdForce_Type.__name__ = "Integer32"
_AnicCmdForce_Object = MibTableColumn
anicCmdForce = _AnicCmdForce_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 7, 1, 1, 1, 5),
    _AnicCmdForce_Type()
)
anicCmdForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anicCmdForce.setStatus("mandatory")


class _AnicCmdParam_Type(OctetString):
    """Custom type anicCmdParam based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_AnicCmdParam_Type.__name__ = "OctetString"
_AnicCmdParam_Object = MibTableColumn
anicCmdParam = _AnicCmdParam_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 7, 1, 1, 1, 6),
    _AnicCmdParam_Type()
)
anicCmdParam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anicCmdParam.setStatus("mandatory")


class _AnicCmdResult_Type(Integer32):
    """Custom type anicCmdResult based on Integer32"""
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
        *(("aborted", 6),
          ("failed", 7),
          ("inProgress", 3),
          ("none", 1),
          ("notSupported", 4),
          ("success", 2),
          ("unAbleToRun", 5))
    )


_AnicCmdResult_Type.__name__ = "Integer32"
_AnicCmdResult_Object = MibTableColumn
anicCmdResult = _AnicCmdResult_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 7, 1, 1, 1, 7),
    _AnicCmdResult_Type()
)
anicCmdResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anicCmdResult.setStatus("mandatory")


class _AnicCmdCode_Type(Integer32):
    """Custom type anicCmdCode based on Integer32"""
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
        *(("deviceDisabled", 5),
          ("noError", 1),
          ("noResponse", 4),
          ("slotEmpty", 3),
          ("unable", 2))
    )


_AnicCmdCode_Type.__name__ = "Integer32"
_AnicCmdCode_Object = MibTableColumn
anicCmdCode = _AnicCmdCode_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 7, 1, 1, 1, 8),
    _AnicCmdCode_Type()
)
anicCmdCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anicCmdCode.setStatus("mandatory")
_AnicCfg_ObjectIdentity = ObjectIdentity
anicCfg = _AnicCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 7, 2)
)
_AnicCfgTable_Object = MibTable
anicCfgTable = _AnicCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 7, 2, 1)
)
if mibBuilder.loadTexts:
    anicCfgTable.setStatus("mandatory")
_AnicCfgEntry_Object = MibTableRow
anicCfgEntry = _AnicCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 7, 2, 1, 1)
)
anicCfgEntry.setIndexNames(
    (0, "ANIC-MIB", "anicCfgIndex"),
)
if mibBuilder.loadTexts:
    anicCfgEntry.setStatus("mandatory")
_AnicCfgIndex_Type = Integer32
_AnicCfgIndex_Object = MibTableColumn
anicCfgIndex = _AnicCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 7, 2, 1, 1, 1),
    _AnicCfgIndex_Type()
)
anicCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anicCfgIndex.setStatus("mandatory")


class _AnicCfgMdmRingNATrapEna_Type(Integer32):
    """Custom type anicCfgMdmRingNATrapEna based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_AnicCfgMdmRingNATrapEna_Type.__name__ = "Integer32"
_AnicCfgMdmRingNATrapEna_Object = MibTableColumn
anicCfgMdmRingNATrapEna = _AnicCfgMdmRingNATrapEna_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 7, 2, 1, 1, 2),
    _AnicCfgMdmRingNATrapEna_Type()
)
anicCfgMdmRingNATrapEna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anicCfgMdmRingNATrapEna.setStatus("mandatory")


class _AnicCfgDteRingNATrapEna_Type(Integer32):
    """Custom type anicCfgDteRingNATrapEna based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_AnicCfgDteRingNATrapEna_Type.__name__ = "Integer32"
_AnicCfgDteRingNATrapEna_Object = MibTableColumn
anicCfgDteRingNATrapEna = _AnicCfgDteRingNATrapEna_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 7, 2, 1, 1, 3),
    _AnicCfgDteRingNATrapEna_Type()
)
anicCfgDteRingNATrapEna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anicCfgDteRingNATrapEna.setStatus("mandatory")


class _AnicCfgRingThresh_Type(Integer32):
    """Custom type anicCfgRingThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AnicCfgRingThresh_Type.__name__ = "Integer32"
_AnicCfgRingThresh_Object = MibTableColumn
anicCfgRingThresh = _AnicCfgRingThresh_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 7, 2, 1, 1, 4),
    _AnicCfgRingThresh_Type()
)
anicCfgRingThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anicCfgRingThresh.setStatus("mandatory")


class _AnicCfgLineStatus_Type(Integer32):
    """Custom type anicCfgLineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("busy", 2),
          ("normal", 1))
    )


_AnicCfgLineStatus_Type.__name__ = "Integer32"
_AnicCfgLineStatus_Object = MibTableColumn
anicCfgLineStatus = _AnicCfgLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 7, 2, 1, 1, 5),
    _AnicCfgLineStatus_Type()
)
anicCfgLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anicCfgLineStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ANIC-MIB",
    **{"usr": usr,
       "nas": nas,
       "anic": anic,
       "anicCmd": anicCmd,
       "anicCmdTable": anicCmdTable,
       "anicCmdEntry": anicCmdEntry,
       "anicCmdIndex": anicCmdIndex,
       "anicCmdMgtStationId": anicCmdMgtStationId,
       "anicCmdReqId": anicCmdReqId,
       "anicCmdFunction": anicCmdFunction,
       "anicCmdForce": anicCmdForce,
       "anicCmdParam": anicCmdParam,
       "anicCmdResult": anicCmdResult,
       "anicCmdCode": anicCmdCode,
       "anicCfg": anicCfg,
       "anicCfgTable": anicCfgTable,
       "anicCfgEntry": anicCfgEntry,
       "anicCfgIndex": anicCfgIndex,
       "anicCfgMdmRingNATrapEna": anicCfgMdmRingNATrapEna,
       "anicCfgDteRingNATrapEna": anicCfgDteRingNATrapEna,
       "anicCfgRingThresh": anicCfgRingThresh,
       "anicCfgLineStatus": anicCfgLineStatus}
)
