# SNMP MIB module (VPMT-OPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VPMT-OPT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:13:13 2024
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
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Codex_ObjectIdentity = ObjectIdentity
codex = _Codex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449)
)
_CdxProductSpecific_ObjectIdentity = ObjectIdentity
cdxProductSpecific = _CdxProductSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2)
)
_Cdx6500_ObjectIdentity = ObjectIdentity
cdx6500 = _Cdx6500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1)
)
_Cdx6500Configuration_ObjectIdentity = ObjectIdentity
cdx6500Configuration = _Cdx6500Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2)
)
_Cdx6500CfgGeneralGroup_ObjectIdentity = ObjectIdentity
cdx6500CfgGeneralGroup = _Cdx6500CfgGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2)
)
_Cdx6500VPMTCfgTable_Object = MibTable
cdx6500VPMTCfgTable = _Cdx6500VPMTCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 26)
)
if mibBuilder.loadTexts:
    cdx6500VPMTCfgTable.setStatus("mandatory")
_Cdx6500VPMTCfgEntry_Object = MibTableRow
cdx6500VPMTCfgEntry = _Cdx6500VPMTCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 26, 1)
)
cdx6500VPMTCfgEntry.setIndexNames(
    (0, "VPMT-OPT-MIB", "cdx6500VPMTCfgEntryNum"),
)
if mibBuilder.loadTexts:
    cdx6500VPMTCfgEntry.setStatus("mandatory")
_Cdx6500VPMTCfgEntryNum_Type = Integer32
_Cdx6500VPMTCfgEntryNum_Object = MibTableColumn
cdx6500VPMTCfgEntryNum = _Cdx6500VPMTCfgEntryNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 26, 1, 1),
    _Cdx6500VPMTCfgEntryNum_Type()
)
cdx6500VPMTCfgEntryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VPMTCfgEntryNum.setStatus("mandatory")


class _Cdx6500VPMTCfgvpType_Type(Integer32):
    """Custom type cdx6500VPMTCfgvpType based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("vpmt-ptype-aam", 11),
          ("vpmt-ptype-bri-voice", 10),
          ("vpmt-ptype-bypass-data", 7),
          ("vpmt-ptype-bypass-voice", 4),
          ("vpmt-ptype-ccs-bypass", 9),
          ("vpmt-ptype-null", 1),
          ("vpmt-ptype-num", 12),
          ("vpmt-ptype-pri-data", 6),
          ("vpmt-ptype-pri-voice", 3),
          ("vpmt-ptype-tdm-data", 5),
          ("vpmt-ptype-trans-ccs-voice", 8),
          ("vpmt-ptype-voice", 2))
    )


_Cdx6500VPMTCfgvpType_Type.__name__ = "Integer32"
_Cdx6500VPMTCfgvpType_Object = MibTableColumn
cdx6500VPMTCfgvpType = _Cdx6500VPMTCfgvpType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 26, 1, 2),
    _Cdx6500VPMTCfgvpType_Type()
)
cdx6500VPMTCfgvpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VPMTCfgvpType.setStatus("mandatory")


class _Cdx6500VPMTCfgvpNum_Type(Integer32):
    """Custom type cdx6500VPMTCfgvpNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 254),
    )


_Cdx6500VPMTCfgvpNum_Type.__name__ = "Integer32"
_Cdx6500VPMTCfgvpNum_Object = MibTableColumn
cdx6500VPMTCfgvpNum = _Cdx6500VPMTCfgvpNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 26, 1, 3),
    _Cdx6500VPMTCfgvpNum_Type()
)
cdx6500VPMTCfgvpNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VPMTCfgvpNum.setStatus("mandatory")


class _Cdx6500VPMTCfgdslNum_Type(Integer32):
    """Custom type cdx6500VPMTCfgdslNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 7),
    )


_Cdx6500VPMTCfgdslNum_Type.__name__ = "Integer32"
_Cdx6500VPMTCfgdslNum_Object = MibTableColumn
cdx6500VPMTCfgdslNum = _Cdx6500VPMTCfgdslNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 26, 1, 4),
    _Cdx6500VPMTCfgdslNum_Type()
)
cdx6500VPMTCfgdslNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VPMTCfgdslNum.setStatus("mandatory")


class _Cdx6500VPMTCfgds0Rate_Type(Integer32):
    """Custom type cdx6500VPMTCfgds0Rate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("vpmt-rate-56k", 1),
          ("vpmt-rate-64k", 2),
          ("vpmt-rate-num", 3))
    )


_Cdx6500VPMTCfgds0Rate_Type.__name__ = "Integer32"
_Cdx6500VPMTCfgds0Rate_Object = MibTableColumn
cdx6500VPMTCfgds0Rate = _Cdx6500VPMTCfgds0Rate_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 26, 1, 5),
    _Cdx6500VPMTCfgds0Rate_Type()
)
cdx6500VPMTCfgds0Rate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VPMTCfgds0Rate.setStatus("mandatory")
_Cdx6500VPMTCfgsrcTimeSlot_Type = Integer32
_Cdx6500VPMTCfgsrcTimeSlot_Object = MibTableColumn
cdx6500VPMTCfgsrcTimeSlot = _Cdx6500VPMTCfgsrcTimeSlot_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 26, 1, 6),
    _Cdx6500VPMTCfgsrcTimeSlot_Type()
)
cdx6500VPMTCfgsrcTimeSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VPMTCfgsrcTimeSlot.setStatus("mandatory")
_Cdx6500VPMTCfgdestTimeSlot_Type = Integer32
_Cdx6500VPMTCfgdestTimeSlot_Object = MibTableColumn
cdx6500VPMTCfgdestTimeSlot = _Cdx6500VPMTCfgdestTimeSlot_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 26, 1, 7),
    _Cdx6500VPMTCfgdestTimeSlot_Type()
)
cdx6500VPMTCfgdestTimeSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VPMTCfgdestTimeSlot.setStatus("mandatory")


class _Cdx6500VPMTCfglocalDialNum_Type(DisplayString):
    """Custom type cdx6500VPMTCfglocalDialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_Cdx6500VPMTCfglocalDialNum_Type.__name__ = "DisplayString"
_Cdx6500VPMTCfglocalDialNum_Object = MibTableColumn
cdx6500VPMTCfglocalDialNum = _Cdx6500VPMTCfglocalDialNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 26, 1, 8),
    _Cdx6500VPMTCfglocalDialNum_Type()
)
cdx6500VPMTCfglocalDialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VPMTCfglocalDialNum.setStatus("mandatory")


class _Cdx6500VPMTCfgsubAddress_Type(DisplayString):
    """Custom type cdx6500VPMTCfgsubAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_Cdx6500VPMTCfgsubAddress_Type.__name__ = "DisplayString"
_Cdx6500VPMTCfgsubAddress_Object = MibTableColumn
cdx6500VPMTCfgsubAddress = _Cdx6500VPMTCfgsubAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 26, 1, 9),
    _Cdx6500VPMTCfgsubAddress_Type()
)
cdx6500VPMTCfgsubAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VPMTCfgsubAddress.setStatus("mandatory")


class _Cdx6500VPMTCfgcallPermission_Type(Integer32):
    """Custom type cdx6500VPMTCfgcallPermission based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inc", 2),
          ("out", 1))
    )


_Cdx6500VPMTCfgcallPermission_Type.__name__ = "Integer32"
_Cdx6500VPMTCfgcallPermission_Object = MibTableColumn
cdx6500VPMTCfgcallPermission = _Cdx6500VPMTCfgcallPermission_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 26, 1, 10),
    _Cdx6500VPMTCfgcallPermission_Type()
)
cdx6500VPMTCfgcallPermission.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VPMTCfgcallPermission.setStatus("mandatory")
_Cdx6500VPMTCfgnum_ccs_bypass_connections_Type = Integer32
_Cdx6500VPMTCfgnum_ccs_bypass_connections_Object = MibScalar
cdx6500VPMTCfgnum_ccs_bypass_connections = _Cdx6500VPMTCfgnum_ccs_bypass_connections_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 26, 1, 11),
    _Cdx6500VPMTCfgnum_ccs_bypass_connections_Type()
)
cdx6500VPMTCfgnum_ccs_bypass_connections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VPMTCfgnum_ccs_bypass_connections.setStatus("mandatory")
_Cdx6500VPMTCfgPhysical_Port_Type = Integer32
_Cdx6500VPMTCfgPhysical_Port_Object = MibScalar
cdx6500VPMTCfgPhysical_Port = _Cdx6500VPMTCfgPhysical_Port_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 26, 1, 12),
    _Cdx6500VPMTCfgPhysical_Port_Type()
)
cdx6500VPMTCfgPhysical_Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VPMTCfgPhysical_Port.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VPMT-OPT-MIB",
    **{"DisplayString": DisplayString,
       "codex": codex,
       "cdxProductSpecific": cdxProductSpecific,
       "cdx6500": cdx6500,
       "cdx6500Configuration": cdx6500Configuration,
       "cdx6500CfgGeneralGroup": cdx6500CfgGeneralGroup,
       "cdx6500VPMTCfgTable": cdx6500VPMTCfgTable,
       "cdx6500VPMTCfgEntry": cdx6500VPMTCfgEntry,
       "cdx6500VPMTCfgEntryNum": cdx6500VPMTCfgEntryNum,
       "cdx6500VPMTCfgvpType": cdx6500VPMTCfgvpType,
       "cdx6500VPMTCfgvpNum": cdx6500VPMTCfgvpNum,
       "cdx6500VPMTCfgdslNum": cdx6500VPMTCfgdslNum,
       "cdx6500VPMTCfgds0Rate": cdx6500VPMTCfgds0Rate,
       "cdx6500VPMTCfgsrcTimeSlot": cdx6500VPMTCfgsrcTimeSlot,
       "cdx6500VPMTCfgdestTimeSlot": cdx6500VPMTCfgdestTimeSlot,
       "cdx6500VPMTCfglocalDialNum": cdx6500VPMTCfglocalDialNum,
       "cdx6500VPMTCfgsubAddress": cdx6500VPMTCfgsubAddress,
       "cdx6500VPMTCfgcallPermission": cdx6500VPMTCfgcallPermission,
       "cdx6500VPMTCfgnum-ccs-bypass-connections": cdx6500VPMTCfgnum_ccs_bypass_connections,
       "cdx6500VPMTCfgPhysical-Port": cdx6500VPMTCfgPhysical_Port}
)
