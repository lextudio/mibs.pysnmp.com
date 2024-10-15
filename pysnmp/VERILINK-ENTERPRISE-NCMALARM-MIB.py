# SNMP MIB module (VERILINK-ENTERPRISE-NCMALARM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VERILINK-ENTERPRISE-NCMALARM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:10 2024
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
 NotificationType,
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
    "NotificationType",
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Verilink_ObjectIdentity = ObjectIdentity
verilink = _Verilink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321)
)
_As2000_ObjectIdentity = ObjectIdentity
as2000 = _As2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 1)
)
_NcmAlarm_ObjectIdentity = ObjectIdentity
ncmAlarm = _NcmAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 1, 100)
)
_NcmAlarmNodeAddr_Type = Integer32
_NcmAlarmNodeAddr_Object = MibScalar
ncmAlarmNodeAddr = _NcmAlarmNodeAddr_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 100, 1),
    _NcmAlarmNodeAddr_Type()
)
ncmAlarmNodeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmAlarmNodeAddr.setStatus("mandatory")
_NcmAlarmShelf_Type = Integer32
_NcmAlarmShelf_Object = MibScalar
ncmAlarmShelf = _NcmAlarmShelf_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 100, 2),
    _NcmAlarmShelf_Type()
)
ncmAlarmShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmAlarmShelf.setStatus("mandatory")
_NcmAlarmSlot_Type = Integer32
_NcmAlarmSlot_Object = MibScalar
ncmAlarmSlot = _NcmAlarmSlot_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 100, 3),
    _NcmAlarmSlot_Type()
)
ncmAlarmSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmAlarmSlot.setStatus("mandatory")
_NcmAlarmPort_Type = Integer32
_NcmAlarmPort_Object = MibScalar
ncmAlarmPort = _NcmAlarmPort_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 100, 4),
    _NcmAlarmPort_Type()
)
ncmAlarmPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmAlarmPort.setStatus("mandatory")


class _NcmAlarmCard_Type(DisplayString):
    """Custom type ncmAlarmCard based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NcmAlarmCard_Type.__name__ = "DisplayString"
_NcmAlarmCard_Object = MibScalar
ncmAlarmCard = _NcmAlarmCard_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 100, 5),
    _NcmAlarmCard_Type()
)
ncmAlarmCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmAlarmCard.setStatus("mandatory")
_NcmAlarmTimestamp_Type = Integer32
_NcmAlarmTimestamp_Object = MibScalar
ncmAlarmTimestamp = _NcmAlarmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 100, 6),
    _NcmAlarmTimestamp_Type()
)
ncmAlarmTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmAlarmTimestamp.setStatus("mandatory")
_NcmAlarmSeverity_Type = Integer32
_NcmAlarmSeverity_Object = MibScalar
ncmAlarmSeverity = _NcmAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 100, 7),
    _NcmAlarmSeverity_Type()
)
ncmAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmAlarmSeverity.setStatus("mandatory")
_NcmAlarmInstance_Type = Integer32
_NcmAlarmInstance_Object = MibScalar
ncmAlarmInstance = _NcmAlarmInstance_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 100, 8),
    _NcmAlarmInstance_Type()
)
ncmAlarmInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmAlarmInstance.setStatus("mandatory")
_NcmAlarmEquipId_Type = Integer32
_NcmAlarmEquipId_Object = MibScalar
ncmAlarmEquipId = _NcmAlarmEquipId_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 100, 9),
    _NcmAlarmEquipId_Type()
)
ncmAlarmEquipId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmAlarmEquipId.setStatus("mandatory")
_NcmAlarmObjectType_Type = Integer32
_NcmAlarmObjectType_Object = MibScalar
ncmAlarmObjectType = _NcmAlarmObjectType_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 100, 10),
    _NcmAlarmObjectType_Type()
)
ncmAlarmObjectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmAlarmObjectType.setStatus("mandatory")


class _NcmAlarmString_Type(DisplayString):
    """Custom type ncmAlarmString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NcmAlarmString_Type.__name__ = "DisplayString"
_NcmAlarmString_Object = MibScalar
ncmAlarmString = _NcmAlarmString_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 100, 11),
    _NcmAlarmString_Type()
)
ncmAlarmString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmAlarmString.setStatus("mandatory")
_Ncm_generic_ObjectIdentity = ObjectIdentity
ncm_generic = _Ncm_generic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 1, 3012)
)
_Ncm_dsu_ObjectIdentity = ObjectIdentity
ncm_dsu = _Ncm_dsu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 1, 3022)
)
_Ncm_dbu_ObjectIdentity = ObjectIdentity
ncm_dbu = _Ncm_dbu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 1, 3023)
)
_Ncm_dds_ObjectIdentity = ObjectIdentity
ncm_dds = _Ncm_dds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 1, 3024)
)
_Ncm_csu_ObjectIdentity = ObjectIdentity
ncm_csu = _Ncm_csu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025)
)
_Ncm_idcsu_ObjectIdentity = ObjectIdentity
ncm_idcsu = _Ncm_idcsu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027)
)
_Ncm_ddsu_ObjectIdentity = ObjectIdentity
ncm_ddsu = _Ncm_ddsu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 1, 3028)
)
_Ncm_sdiu_ObjectIdentity = ObjectIdentity
ncm_sdiu = _Ncm_sdiu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 1, 3029)
)
_Ncm_imux_ObjectIdentity = ObjectIdentity
ncm_imux = _Ncm_imux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 1, 3030)
)
_Ncm_isdn_ObjectIdentity = ObjectIdentity
ncm_isdn = _Ncm_isdn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031)
)
_Ncm_ds3_ObjectIdentity = ObjectIdentity
ncm_ds3 = _Ncm_ds3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 1, 3036)
)
_Ncm_m13_ObjectIdentity = ObjectIdentity
ncm_m13 = _Ncm_m13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 1, 3037)
)
_Ncm_japisdn_ObjectIdentity = ObjectIdentity
ncm_japisdn = _Ncm_japisdn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038)
)

# Managed Objects groups


# Notification objects

ncmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 4000)
)
ncmTrap.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmTrap.setStatus(
        ""
    )

ncmnearCSUPowerUP = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 4001)
)
ncmnearCSUPowerUP.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearCSUPowerUP.setStatus(
        ""
    )

ncmncmfarCSUPowrUP = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 4003)
)
ncmncmfarCSUPowrUP.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmncmfarCSUPowrUP.setStatus(
        ""
    )

ncmnearBERexceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5101)
)
ncmnearBERexceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearBERexceeded.setStatus(
        ""
    )

ncmnearBERexceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5102)
)
ncmnearBERexceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearBERexceededCleared.setStatus(
        ""
    )

ncmnearESLexceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5103)
)
ncmnearESLexceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearESLexceeded.setStatus(
        ""
    )

ncmnearESLexceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5104)
)
ncmnearESLexceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearESLexceededCleared.setStatus(
        ""
    )

ncmnearESexceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5105)
)
ncmnearESexceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearESexceeded.setStatus(
        ""
    )

ncmnearESexceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5106)
)
ncmnearESexceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearESexceededCleared.setStatus(
        ""
    )

ncmnearUASexceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5107)
)
ncmnearUASexceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearUASexceeded.setStatus(
        ""
    )

ncmnearUASexceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5108)
)
ncmnearUASexceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearUASexceededCleared.setStatus(
        ""
    )

ncmnearLELBlooped = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5109)
)
ncmnearLELBlooped.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearLELBlooped.setStatus(
        ""
    )

ncmnearLELBloopedCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5110)
)
ncmnearLELBloopedCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearLELBloopedCleared.setStatus(
        ""
    )

ncmnearPRLBlooped = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5111)
)
ncmnearPRLBlooped.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearPRLBlooped.setStatus(
        ""
    )

ncmnearPRLBloopedCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5112)
)
ncmnearPRLBloopedCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearPRLBloopedCleared.setStatus(
        ""
    )

ncmnearLOS = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5113)
)
ncmnearLOS.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearLOS.setStatus(
        ""
    )

ncmnearLOSCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5114)
)
ncmnearLOSCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearLOSCleared.setStatus(
        ""
    )

ncmnearRAI = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5115)
)
ncmnearRAI.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearRAI.setStatus(
        ""
    )

ncmnearRAICleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5116)
)
ncmnearRAICleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearRAICleared.setStatus(
        ""
    )

ncmnearLOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5117)
)
ncmnearLOF.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearLOF.setStatus(
        ""
    )

ncmnearLOFCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5118)
)
ncmnearLOFCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearLOFCleared.setStatus(
        ""
    )

ncmnearAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5119)
)
ncmnearAIS.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearAIS.setStatus(
        ""
    )

ncmnearAISCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5120)
)
ncmnearAISCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearAISCleared.setStatus(
        ""
    )

ncmnearTestSIG = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5121)
)
ncmnearTestSIG.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearTestSIG.setStatus(
        ""
    )

ncmnearTestSIGCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5122)
)
ncmnearTestSIGCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearTestSIGCleared.setStatus(
        ""
    )

ncmnearCSULossExtClk = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5123)
)
ncmnearCSULossExtClk.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearCSULossExtClk.setStatus(
        ""
    )

ncmnearCSULossExtClkCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5124)
)
ncmnearCSULossExtClkCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearCSULossExtClkCleared.setStatus(
        ""
    )

ncmnearEQPTBERExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5201)
)
ncmnearEQPTBERExceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearEQPTBERExceeded.setStatus(
        ""
    )

ncmnearEQPTBERExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5202)
)
ncmnearEQPTBERExceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearEQPTBERExceededCleared.setStatus(
        ""
    )

ncmnearEQPTESLExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5203)
)
ncmnearEQPTESLExceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearEQPTESLExceeded.setStatus(
        ""
    )

ncmnearEQPTESLExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5204)
)
ncmnearEQPTESLExceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearEQPTESLExceededCleared.setStatus(
        ""
    )

ncmnearEQPTESExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5205)
)
ncmnearEQPTESExceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearEQPTESExceeded.setStatus(
        ""
    )

ncmnearEQPTESExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5206)
)
ncmnearEQPTESExceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearEQPTESExceededCleared.setStatus(
        ""
    )

ncmnearEQPTUASExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5207)
)
ncmnearEQPTUASExceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearEQPTUASExceeded.setStatus(
        ""
    )

ncmnearEQPTUASExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5208)
)
ncmnearEQPTUASExceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearEQPTUASExceededCleared.setStatus(
        ""
    )

ncmnearEQPTELBLooped = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5209)
)
ncmnearEQPTELBLooped.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearEQPTELBLooped.setStatus(
        ""
    )

ncmnearEQPTELBLoopedCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5210)
)
ncmnearEQPTELBLoopedCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearEQPTELBLoopedCleared.setStatus(
        ""
    )

ncmnearEQPTRLBLooped = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5211)
)
ncmnearEQPTRLBLooped.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearEQPTRLBLooped.setStatus(
        ""
    )

ncmnearEQPTRLBLoopedCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5212)
)
ncmnearEQPTRLBLoopedCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearEQPTRLBLoopedCleared.setStatus(
        ""
    )

ncmnearEQPTLOS = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5213)
)
ncmnearEQPTLOS.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearEQPTLOS.setStatus(
        ""
    )

ncmnearEQPTLOSCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5214)
)
ncmnearEQPTLOSCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearEQPTLOSCleared.setStatus(
        ""
    )

ncmnearEQPTRAI = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5215)
)
ncmnearEQPTRAI.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearEQPTRAI.setStatus(
        ""
    )

ncmnearEQPTRAICleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5216)
)
ncmnearEQPTRAICleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearEQPTRAICleared.setStatus(
        ""
    )

ncmnearEQPTLOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5217)
)
ncmnearEQPTLOF.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearEQPTLOF.setStatus(
        ""
    )

ncmnearEQPTLOFCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5218)
)
ncmnearEQPTLOFCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearEQPTLOFCleared.setStatus(
        ""
    )

ncmnearEQPTAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5219)
)
ncmnearEQPTAIS.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearEQPTAIS.setStatus(
        ""
    )

ncmnearEQPTAISCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5220)
)
ncmnearEQPTAISCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearEQPTAISCleared.setStatus(
        ""
    )

ncmnearEQPTTSA = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5221)
)
ncmnearEQPTTSA.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearEQPTTSA.setStatus(
        ""
    )

ncmnearEQPTTSACleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5222)
)
ncmnearEQPTTSACleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearEQPTTSACleared.setStatus(
        ""
    )

ncmnearEQPTLowDensity = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5223)
)
ncmnearEQPTLowDensity.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearEQPTLowDensity.setStatus(
        ""
    )

ncmnearEQPTLowDensityCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5224)
)
ncmnearEQPTLowDensityCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearEQPTLowDensityCleared.setStatus(
        ""
    )

ncmfarBERexceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5301)
)
ncmfarBERexceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmfarBERexceeded.setStatus(
        ""
    )

ncmfarBERexceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5302)
)
ncmfarBERexceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmfarBERexceededCleared.setStatus(
        ""
    )

ncmfarESLexceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5303)
)
ncmfarESLexceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmfarESLexceeded.setStatus(
        ""
    )

ncmfarESLexceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5304)
)
ncmfarESLexceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmfarESLexceededCleared.setStatus(
        ""
    )

ncmfarESexceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5305)
)
ncmfarESexceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmfarESexceeded.setStatus(
        ""
    )

ncmfarESexceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5306)
)
ncmfarESexceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmfarESexceededCleared.setStatus(
        ""
    )

ncmfarUASexceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5307)
)
ncmfarUASexceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmfarUASexceeded.setStatus(
        ""
    )

ncmfarUASexceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5308)
)
ncmfarUASexceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmfarUASexceededCleared.setStatus(
        ""
    )

ncmfarLELBlooped = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5309)
)
ncmfarLELBlooped.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmfarLELBlooped.setStatus(
        ""
    )

ncmfarLELBloopedCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5310)
)
ncmfarLELBloopedCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmfarLELBloopedCleared.setStatus(
        ""
    )

ncmfarPRLBlooped = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5311)
)
ncmfarPRLBlooped.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmfarPRLBlooped.setStatus(
        ""
    )

ncmfarPRLBloopedCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5312)
)
ncmfarPRLBloopedCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmfarPRLBloopedCleared.setStatus(
        ""
    )

ncmfarLOS = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5313)
)
ncmfarLOS.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmfarLOS.setStatus(
        ""
    )

ncmfarLOSCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5314)
)
ncmfarLOSCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmfarLOSCleared.setStatus(
        ""
    )

ncmfarRAI = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5315)
)
ncmfarRAI.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmfarRAI.setStatus(
        ""
    )

ncmfarRAICleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5316)
)
ncmfarRAICleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmfarRAICleared.setStatus(
        ""
    )

ncmfarLOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5317)
)
ncmfarLOF.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmfarLOF.setStatus(
        ""
    )

ncmfarLOFCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5318)
)
ncmfarLOFCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmfarLOFCleared.setStatus(
        ""
    )

ncmfarAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5319)
)
ncmfarAIS.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmfarAIS.setStatus(
        ""
    )

ncmfarAISCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5320)
)
ncmfarAISCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmfarAISCleared.setStatus(
        ""
    )

ncmfarTestSIG = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5321)
)
ncmfarTestSIG.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmfarTestSIG.setStatus(
        ""
    )

ncmfarTestSIGCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5322)
)
ncmfarTestSIGCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmfarTestSIGCleared.setStatus(
        ""
    )

ncmfarCSULossExtClk = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5323)
)
ncmfarCSULossExtClk.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmfarCSULossExtClk.setStatus(
        ""
    )

ncmfarCSULossExtClkCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5324)
)
ncmfarCSULossExtClkCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmfarCSULossExtClkCleared.setStatus(
        ""
    )

ncmFarEQPTBERExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5401)
)
ncmFarEQPTBERExceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmFarEQPTBERExceeded.setStatus(
        ""
    )

ncmFarEQPTBERExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5402)
)
ncmFarEQPTBERExceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmFarEQPTBERExceededCleared.setStatus(
        ""
    )

ncmFarEQPTESLExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5404)
)
ncmFarEQPTESLExceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmFarEQPTESLExceededCleared.setStatus(
        ""
    )

ncmFarEQPTESExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5405)
)
ncmFarEQPTESExceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmFarEQPTESExceeded.setStatus(
        ""
    )

ncmFarEQPTESExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5406)
)
ncmFarEQPTESExceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmFarEQPTESExceededCleared.setStatus(
        ""
    )

ncmFarEQPTUASExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5407)
)
ncmFarEQPTUASExceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmFarEQPTUASExceeded.setStatus(
        ""
    )

ncmFarEQPTUASExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5408)
)
ncmFarEQPTUASExceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmFarEQPTUASExceededCleared.setStatus(
        ""
    )

ncmFarEQPTELBLooped = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5409)
)
ncmFarEQPTELBLooped.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmFarEQPTELBLooped.setStatus(
        ""
    )

ncmFarEQPTELBLoopedCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5410)
)
ncmFarEQPTELBLoopedCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmFarEQPTELBLoopedCleared.setStatus(
        ""
    )

ncmFarEQPTRLBLooped = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5411)
)
ncmFarEQPTRLBLooped.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmFarEQPTRLBLooped.setStatus(
        ""
    )

ncmFarEQPTRLBLoopedCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5412)
)
ncmFarEQPTRLBLoopedCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmFarEQPTRLBLoopedCleared.setStatus(
        ""
    )

ncmFarEQPTLOS = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5413)
)
ncmFarEQPTLOS.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmFarEQPTLOS.setStatus(
        ""
    )

ncmFarEQPTLOSCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5414)
)
ncmFarEQPTLOSCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmFarEQPTLOSCleared.setStatus(
        ""
    )

ncmFarEQPTRAI = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5415)
)
ncmFarEQPTRAI.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmFarEQPTRAI.setStatus(
        ""
    )

ncmFarEQPTRAICleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5416)
)
ncmFarEQPTRAICleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmFarEQPTRAICleared.setStatus(
        ""
    )

ncmFarEQPTLOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5417)
)
ncmFarEQPTLOF.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmFarEQPTLOF.setStatus(
        ""
    )

ncmFarEQPTLOFCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5418)
)
ncmFarEQPTLOFCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmFarEQPTLOFCleared.setStatus(
        ""
    )

ncmFarEQPTAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5419)
)
ncmFarEQPTAIS.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmFarEQPTAIS.setStatus(
        ""
    )

ncmFarEQPTAISCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5420)
)
ncmFarEQPTAISCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmFarEQPTAISCleared.setStatus(
        ""
    )

ncmFarEQPTTSA = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5421)
)
ncmFarEQPTTSA.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmFarEQPTTSA.setStatus(
        ""
    )

ncmFarEQPTTSACleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5422)
)
ncmFarEQPTTSACleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmFarEQPTTSACleared.setStatus(
        ""
    )

ncmFarEQPTLowDensity = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5423)
)
ncmFarEQPTLowDensity.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmFarEQPTLowDensity.setStatus(
        ""
    )

ncmFarEQPTLowDensityCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 5424)
)
ncmFarEQPTLowDensityCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmFarEQPTLowDensityCleared.setStatus(
        ""
    )

ncmnearNewPlug = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6501)
)
ncmnearNewPlug.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearNewPlug.setStatus(
        ""
    )

ncmnearPlugAbsent = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6503)
)
ncmnearPlugAbsent.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearPlugAbsent.setStatus(
        ""
    )

ncmnearPlugPresent = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6505)
)
ncmnearPlugPresent.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearPlugPresent.setStatus(
        ""
    )

ncmtiuDualClksPresent = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6601)
)
ncmtiuDualClksPresent.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmtiuDualClksPresent.setStatus(
        ""
    )

ncmtiuDualClksPresentCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6602)
)
ncmtiuDualClksPresentCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmtiuDualClksPresentCleared.setStatus(
        ""
    )

ncmtiuNoClksPresent = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6603)
)
ncmtiuNoClksPresent.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmtiuNoClksPresent.setStatus(
        ""
    )

ncmtiuNoClksPresentCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6604)
)
ncmtiuNoClksPresentCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmtiuNoClksPresentCleared.setStatus(
        ""
    )

ncmdiuPort1LOS = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6801)
)
ncmdiuPort1LOS.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmdiuPort1LOS.setStatus(
        ""
    )

ncmdiuPort1LOSCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6802)
)
ncmdiuPort1LOSCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmdiuPort1LOSCleared.setStatus(
        ""
    )

ncmdiuPort2LOS = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6803)
)
ncmdiuPort2LOS.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmdiuPort2LOS.setStatus(
        ""
    )

ncmdiuPort2LOSCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6804)
)
ncmdiuPort2LOSCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmdiuPort2LOSCleared.setStatus(
        ""
    )

ncmddsPortAbnormalStationCodeExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6805)
)
ncmddsPortAbnormalStationCodeExceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmddsPortAbnormalStationCodeExceeded.setStatus(
        ""
    )

ncmddsPortAbnormalStationCodeExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6806)
)
ncmddsPortAbnormalStationCodeExceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmddsPortAbnormalStationCodeExceededCleared.setStatus(
        ""
    )

ncmddsPortControlModeIdleExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6807)
)
ncmddsPortControlModeIdleExceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmddsPortControlModeIdleExceeded.setStatus(
        ""
    )

ncmddsPortControlModeIdleExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6808)
)
ncmddsPortControlModeIdleExceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmddsPortControlModeIdleExceededCleared.setStatus(
        ""
    )

ncmddsPortMuxOutSyncExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6809)
)
ncmddsPortMuxOutSyncExceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmddsPortMuxOutSyncExceeded.setStatus(
        ""
    )

ncmddsPortMuxOutSyncExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6810)
)
ncmddsPortMuxOutSyncExceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmddsPortMuxOutSyncExceededCleared.setStatus(
        ""
    )

ncmddsPortUnassignedMuxChannelExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6811)
)
ncmddsPortUnassignedMuxChannelExceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmddsPortUnassignedMuxChannelExceeded.setStatus(
        ""
    )

ncmddsPortUnassignedMuxChannelExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6812)
)
ncmddsPortUnassignedMuxChannelExceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmddsPortUnassignedMuxChannelExceededCleared.setStatus(
        ""
    )

ncmddsPortMJUAlertExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6813)
)
ncmddsPortMJUAlertExceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmddsPortMJUAlertExceeded.setStatus(
        ""
    )

ncmddsPortMJUAlertExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6814)
)
ncmddsPortMJUAlertExceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmddsPortMJUAlertExceededCleared.setStatus(
        ""
    )

ncmddsPortTestCodeExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6815)
)
ncmddsPortTestCodeExceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmddsPortTestCodeExceeded.setStatus(
        ""
    )

ncmddsPortTestCodeExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6816)
)
ncmddsPortTestCodeExceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmddsPortTestCodeExceededCleared.setStatus(
        ""
    )

ncmddsPortTestAlertExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6817)
)
ncmddsPortTestAlertExceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmddsPortTestAlertExceeded.setStatus(
        ""
    )

ncmddsPortTestAlertExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6818)
)
ncmddsPortTestAlertExceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmddsPortTestAlertExceededCleared.setStatus(
        ""
    )

ncmddsPortBlockExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6819)
)
ncmddsPortBlockExceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmddsPortBlockExceeded.setStatus(
        ""
    )

ncmddsPortBlockExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6820)
)
ncmddsPortBlockExceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmddsPortBlockExceededCleared.setStatus(
        ""
    )

ncmddsPortReleaseExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6821)
)
ncmddsPortReleaseExceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmddsPortReleaseExceeded.setStatus(
        ""
    )

ncmddsPortReleaseExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6822)
)
ncmddsPortReleaseExceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmddsPortReleaseExceededCleared.setStatus(
        ""
    )

ncmddsPortLoop = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6823)
)
ncmddsPortLoop.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmddsPortLoop.setStatus(
        ""
    )

ncmddsPortLoopCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6824)
)
ncmddsPortLoopCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmddsPortLoopCleared.setStatus(
        ""
    )

ncmddsPortncmFarLooped = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6825)
)
ncmddsPortncmFarLooped.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmddsPortncmFarLooped.setStatus(
        ""
    )

ncmddsPortncmFarLoopCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6826)
)
ncmddsPortncmFarLoopCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmddsPortncmFarLoopCleared.setStatus(
        ""
    )

ncmddsPortTestSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6827)
)
ncmddsPortTestSignal.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmddsPortTestSignal.setStatus(
        ""
    )

ncmddsPortTestSignalCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6828)
)
ncmddsPortTestSignalCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmddsPortTestSignalCleared.setStatus(
        ""
    )

ncmddsPort2AbnormalStationCodeExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6829)
)
ncmddsPort2AbnormalStationCodeExceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmddsPort2AbnormalStationCodeExceeded.setStatus(
        ""
    )

ncmddsPort2AbnormalStationCodeExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6830)
)
ncmddsPort2AbnormalStationCodeExceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmddsPort2AbnormalStationCodeExceededCleared.setStatus(
        ""
    )

ncmddsPort2ControlModeIdleExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6831)
)
ncmddsPort2ControlModeIdleExceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmddsPort2ControlModeIdleExceeded.setStatus(
        ""
    )

ncmddsPort2ControlModeIdleExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6832)
)
ncmddsPort2ControlModeIdleExceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmddsPort2ControlModeIdleExceededCleared.setStatus(
        ""
    )

ncmddsPort2MuxOutSyncExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6833)
)
ncmddsPort2MuxOutSyncExceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmddsPort2MuxOutSyncExceeded.setStatus(
        ""
    )

ncmddsPort2MuxOutSyncExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6834)
)
ncmddsPort2MuxOutSyncExceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmddsPort2MuxOutSyncExceededCleared.setStatus(
        ""
    )

ncmddsPort2UnassignedMuxChannelExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6835)
)
ncmddsPort2UnassignedMuxChannelExceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmddsPort2UnassignedMuxChannelExceeded.setStatus(
        ""
    )

ncmddsPort2UnassignedMuxChannelExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6836)
)
ncmddsPort2UnassignedMuxChannelExceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmddsPort2UnassignedMuxChannelExceededCleared.setStatus(
        ""
    )

ncmddsPort2MJUAlertExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6837)
)
ncmddsPort2MJUAlertExceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmddsPort2MJUAlertExceeded.setStatus(
        ""
    )

ncmddsPort2MJUAlertExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6838)
)
ncmddsPort2MJUAlertExceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmddsPort2MJUAlertExceededCleared.setStatus(
        ""
    )

ncmddsPort2TestCodeExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6839)
)
ncmddsPort2TestCodeExceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmddsPort2TestCodeExceeded.setStatus(
        ""
    )

ncmddsPort2TestCodeExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6840)
)
ncmddsPort2TestCodeExceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmddsPort2TestCodeExceededCleared.setStatus(
        ""
    )

ncmddsPort2TestAlertExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6841)
)
ncmddsPort2TestAlertExceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmddsPort2TestAlertExceeded.setStatus(
        ""
    )

ncmddsPort2TestAlertExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6842)
)
ncmddsPort2TestAlertExceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmddsPort2TestAlertExceededCleared.setStatus(
        ""
    )

ncmddsPort2BlockExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6843)
)
ncmddsPort2BlockExceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmddsPort2BlockExceeded.setStatus(
        ""
    )

ncmddsPort2BlockExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6844)
)
ncmddsPort2BlockExceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmddsPort2BlockExceededCleared.setStatus(
        ""
    )

ncmddsPort2ReleaseExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6845)
)
ncmddsPort2ReleaseExceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmddsPort2ReleaseExceeded.setStatus(
        ""
    )

ncmddsPort2ReleaseExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6846)
)
ncmddsPort2ReleaseExceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmddsPort2ReleaseExceededCleared.setStatus(
        ""
    )

ncmddsPort2Loop = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6847)
)
ncmddsPort2Loop.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmddsPort2Loop.setStatus(
        ""
    )

ncmddsPort2LoopCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6848)
)
ncmddsPort2LoopCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmddsPort2LoopCleared.setStatus(
        ""
    )

ncmddsPort2ncmFarLooped = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6849)
)
ncmddsPort2ncmFarLooped.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmddsPort2ncmFarLooped.setStatus(
        ""
    )

ncmddsPort2ncmFarLoopCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6850)
)
ncmddsPort2ncmFarLoopCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmddsPort2ncmFarLoopCleared.setStatus(
        ""
    )

ncmddsPort2TestSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6851)
)
ncmddsPort2TestSignal.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmddsPort2TestSignal.setStatus(
        ""
    )

ncmddsPort2TestSignalCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6852)
)
ncmddsPort2TestSignalCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmddsPort2TestSignalCleared.setStatus(
        ""
    )

ncmdbuAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6853)
)
ncmdbuAlarm.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmdbuAlarm.setStatus(
        ""
    )

ncmdbuAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6854)
)
ncmdbuAlarmClear.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmdbuAlarmClear.setStatus(
        ""
    )

ncmdbuBackupConnection = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6855)
)
ncmdbuBackupConnection.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmdbuBackupConnection.setStatus(
        ""
    )

ncmdiuPortALLOnes = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6857)
)
ncmdiuPortALLOnes.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmdiuPortALLOnes.setStatus(
        ""
    )

ncmdiuPortALLOnesCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6858)
)
ncmdiuPortALLOnesCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmdiuPortALLOnesCleared.setStatus(
        ""
    )

ncmdbuPortASCOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6861)
)
ncmdbuPortASCOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmdbuPortASCOn.setStatus(
        ""
    )

ncmdbuPortASCOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6862)
)
ncmdbuPortASCOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmdbuPortASCOff.setStatus(
        ""
    )

ncmdbuPortLOFOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6863)
)
ncmdbuPortLOFOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmdbuPortLOFOn.setStatus(
        ""
    )

ncmdbuPortLOFOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6864)
)
ncmdbuPortLOFOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmdbuPortLOFOff.setStatus(
        ""
    )

ncmdbuPortCDOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6865)
)
ncmdbuPortCDOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmdbuPortCDOn.setStatus(
        ""
    )

ncmdbuPortCDOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6866)
)
ncmdbuPortCDOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmdbuPortCDOff.setStatus(
        ""
    )

ncmdbuPortUSEROn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6867)
)
ncmdbuPortUSEROn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmdbuPortUSEROn.setStatus(
        ""
    )

ncmdbuPortUSEROff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6868)
)
ncmdbuPortUSEROff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmdbuPortUSEROff.setStatus(
        ""
    )

ncmdbuPortYELAlarmOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6869)
)
ncmdbuPortYELAlarmOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmdbuPortYELAlarmOn.setStatus(
        ""
    )

ncmdbuPortYELAlarmOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6870)
)
ncmdbuPortYELAlarmOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmdbuPortYELAlarmOff.setStatus(
        ""
    )

ncmdbuPortNetworkBEROn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6871)
)
ncmdbuPortNetworkBEROn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmdbuPortNetworkBEROn.setStatus(
        ""
    )

ncmdbuPortNetworkBEROff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6872)
)
ncmdbuPortNetworkBEROff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmdbuPortNetworkBEROff.setStatus(
        ""
    )

ncmdbuPortAllOnesAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6873)
)
ncmdbuPortAllOnesAlarm.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmdbuPortAllOnesAlarm.setStatus(
        ""
    )

ncmdbuPortAllOnesAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6874)
)
ncmdbuPortAllOnesAlarmCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmdbuPortAllOnesAlarmCleared.setStatus(
        ""
    )

ncmdbuPortLOSOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6875)
)
ncmdbuPortLOSOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmdbuPortLOSOn.setStatus(
        ""
    )

ncmdbuPortLOSOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6876)
)
ncmdbuPortLOSOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmdbuPortLOSOff.setStatus(
        ""
    )

ncmPlugPresent = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6996)
)
ncmPlugPresent.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmPlugPresent.setStatus(
        ""
    )

ncmPlugAbsent = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6997)
)
ncmPlugAbsent.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmPlugAbsent.setStatus(
        ""
    )

ncmFEPlugPresent = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6998)
)
ncmFEPlugPresent.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmFEPlugPresent.setStatus(
        ""
    )

ncmFEPlugAbsent = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 6999)
)
ncmFEPlugAbsent.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmFEPlugAbsent.setStatus(
        ""
    )

ncmalarmBufferFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 7001)
)
ncmalarmBufferFull.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalarmBufferFull.setStatus(
        ""
    )

ncmnearAPowerSupply = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 7002)
)
ncmnearAPowerSupply.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearAPowerSupply.setStatus(
        ""
    )

ncmnearAPowerSupplyCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 7003)
)
ncmnearAPowerSupplyCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearAPowerSupplyCleared.setStatus(
        ""
    )

ncmfarAPowerSupply = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 7004)
)
ncmfarAPowerSupply.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmfarAPowerSupply.setStatus(
        ""
    )

ncmfarAPowerSupplyCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 7005)
)
ncmfarAPowerSupplyCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmfarAPowerSupplyCleared.setStatus(
        ""
    )

ncmnearBPowerSupply = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 7006)
)
ncmnearBPowerSupply.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearBPowerSupply.setStatus(
        ""
    )

ncmnearBPowerSupplyCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 7007)
)
ncmnearBPowerSupplyCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearBPowerSupplyCleared.setStatus(
        ""
    )

ncmfarBPowerSupply = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 7008)
)
ncmfarBPowerSupply.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmfarBPowerSupply.setStatus(
        ""
    )

ncmfarBPowerSupplyCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 7009)
)
ncmfarBPowerSupplyCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmfarBPowerSupplyCleared.setStatus(
        ""
    )

powerUPLoopExists = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 7010)
)
powerUPLoopExists.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    powerUPLoopExists.setStatus(
        ""
    )

postNETFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 7011)
)
postNETFailure.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    postNETFailure.setStatus(
        ""
    )

postEQPTFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 7012)
)
postEQPTFailure.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    postEQPTFailure.setStatus(
        ""
    )

lowBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 7013)
)
lowBattery.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    lowBattery.setStatus(
        ""
    )

ncminvDownload = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 7014)
)
ncminvDownload.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncminvDownload.setStatus(
        ""
    )

ncmActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 8000)
)
ncmActive.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmActive.setStatus(
        ""
    )

ncmStandBy = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 8001)
)
ncmStandBy.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmStandBy.setStatus(
        ""
    )

ncmCircuitErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 8002)
)
ncmCircuitErr.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmCircuitErr.setStatus(
        ""
    )

ncmFanShelfFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 8003)
)
ncmFanShelfFail.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmFanShelfFail.setStatus(
        ""
    )

ncmFanShelfAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 8004)
)
ncmFanShelfAlarmCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmFanShelfAlarmCleared.setStatus(
        ""
    )

ncmapsAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 9001)
)
ncmapsAlarmSet.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmapsAlarmSet.setStatus(
        ""
    )

ncmapsAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 9002)
)
ncmapsAlarmClear.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmapsAlarmClear.setStatus(
        ""
    )

ncmapsSwitchedSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 9003)
)
ncmapsSwitchedSet.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmapsSwitchedSet.setStatus(
        ""
    )

ncmapsSwitchedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 9004)
)
ncmapsSwitchedClear.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmapsSwitchedClear.setStatus(
        ""
    )

ncmipOverT1LinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 9005)
)
ncmipOverT1LinkDown.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmipOverT1LinkDown.setStatus(
        ""
    )

ncmipOverT1LinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 9006)
)
ncmipOverT1LinkUp.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmipOverT1LinkUp.setStatus(
        ""
    )

ncmnearquadCSUPowerUP = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 10000)
)
ncmnearquadCSUPowerUP.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearquadCSUPowerUP.setStatus(
        ""
    )

ncmfarCSUPowerUP = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 10003)
)
ncmfarCSUPowerUP.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmfarCSUPowerUP.setStatus(
        ""
    )

ncmnearQuadAPowerSupply = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 11002)
)
ncmnearQuadAPowerSupply.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearQuadAPowerSupply.setStatus(
        ""
    )

ncmnearQuadAPowerSupplyCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 11003)
)
ncmnearQuadAPowerSupplyCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearQuadAPowerSupplyCleared.setStatus(
        ""
    )

ncmnearQuadBPowerSupply = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 11006)
)
ncmnearQuadBPowerSupply.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearQuadBPowerSupply.setStatus(
        ""
    )

ncmnearQuadBPowerSupplyCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 11007)
)
ncmnearQuadBPowerSupplyCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearQuadBPowerSupplyCleared.setStatus(
        ""
    )

ncmnearAceLOS = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 11100)
)
ncmnearAceLOS.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearAceLOS.setStatus(
        ""
    )

ncmnearAceLOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 11101)
)
ncmnearAceLOF.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearAceLOF.setStatus(
        ""
    )

ncmnearRemoteAI = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 11102)
)
ncmnearRemoteAI.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearRemoteAI.setStatus(
        ""
    )

ncmnearLOMFalignm = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 11103)
)
ncmnearLOMFalignm.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearLOMFalignm.setStatus(
        ""
    )

ncmnearRemoteMAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 11104)
)
ncmnearRemoteMAS.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearRemoteMAS.setStatus(
        ""
    )

ncmnearIAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 11105)
)
ncmnearIAS.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearIAS.setStatus(
        ""
    )

ncmnearFAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 11106)
)
ncmnearFAS.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearFAS.setStatus(
        ""
    )

ncmnearFASeXceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 11107)
)
ncmnearFASeXceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearFASeXceeded.setStatus(
        ""
    )

ncmnearCVCeXceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 11108)
)
ncmnearCVCeXceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearCVCeXceeded.setStatus(
        ""
    )

ncmnearCRCeXceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 11109)
)
ncmnearCRCeXceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearCRCeXceeded.setStatus(
        ""
    )

ncmnearFECeXceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 11110)
)
ncmnearFECeXceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearFECeXceeded.setStatus(
        ""
    )

ncmnearCarrier = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 11111)
)
ncmnearCarrier.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearCarrier.setStatus(
        ""
    )

ncmnearDwnLdCode = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 11113)
)
ncmnearDwnLdCode.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearDwnLdCode.setStatus(
        ""
    )

ncmnearLActCLK = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 11114)
)
ncmnearLActCLK.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearLActCLK.setStatus(
        ""
    )

ncmnearLstdbyCLK = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 11115)
)
ncmnearLstdbyCLK.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearLstdbyCLK.setStatus(
        ""
    )

ncmnearRefTBUS = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 11116)
)
ncmnearRefTBUS.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearRefTBUS.setStatus(
        ""
    )

ncmnearTBUS = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 11117)
)
ncmnearTBUS.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearTBUS.setStatus(
        ""
    )

ncmnearLLB = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 11119)
)
ncmnearLLB.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearLLB.setStatus(
        ""
    )

ncmnearELB = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 11120)
)
ncmnearELB.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearELB.setStatus(
        ""
    )

ncmnearPLB = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 11121)
)
ncmnearPLB.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearPLB.setStatus(
        ""
    )

ncmnearRLB = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 11122)
)
ncmnearRLB.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearRLB.setStatus(
        ""
    )

ncmalmSESExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 11123)
)
ncmalmSESExceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmSESExceeded.setStatus(
        ""
    )

ncmalmUASExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 11124)
)
ncmalmUASExceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmUASExceeded.setStatus(
        ""
    )

ncmalmBERExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 11125)
)
ncmalmBERExceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmBERExceeded.setStatus(
        ""
    )

ncmalmQ931LinkUP = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 11126)
)
ncmalmQ931LinkUP.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmQ931LinkUP.setStatus(
        ""
    )

ncmalmQ931LinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 11127)
)
ncmalmQ931LinkDown.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmQ931LinkDown.setStatus(
        ""
    )

ncmalmPortDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 11128)
)
ncmalmPortDown.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmPortDown.setStatus(
        ""
    )

ncmalmCGA = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 11129)
)
ncmalmCGA.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmCGA.setStatus(
        ""
    )

ncmalmLOFThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 11130)
)
ncmalmLOFThresholdExceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmLOFThresholdExceeded.setStatus(
        ""
    )

ncmalmLOSThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 11131)
)
ncmalmLOSThresholdExceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmLOSThresholdExceeded.setStatus(
        ""
    )

ncmalmRAIThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 11132)
)
ncmalmRAIThresholdExceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmRAIThresholdExceeded.setStatus(
        ""
    )

ncmalmAISThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 11133)
)
ncmalmAISThresholdExceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmAISThresholdExceeded.setStatus(
        ""
    )

ncmalmBPVThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 11134)
)
ncmalmBPVThresholdExceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmBPVThresholdExceeded.setStatus(
        ""
    )

ncmalmES15MINThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 11135)
)
ncmalmES15MINThresholdExceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmES15MINThresholdExceeded.setStatus(
        ""
    )

ncmalmES24HRThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 11136)
)
ncmalmES24HRThresholdExceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmES24HRThresholdExceeded.setStatus(
        ""
    )

ncmalmSES15MINThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 11137)
)
ncmalmSES15MINThresholdExceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmSES15MINThresholdExceeded.setStatus(
        ""
    )

ncmalmSES24HRThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 11138)
)
ncmalmSES24HRThresholdExceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmSES24HRThresholdExceeded.setStatus(
        ""
    )

ncmalmCVP15MINThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 11139)
)
ncmalmCVP15MINThresholdExceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmCVP15MINThresholdExceeded.setStatus(
        ""
    )

ncmalmCVP24HRThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 11140)
)
ncmalmCVP24HRThresholdExceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmCVP24HRThresholdExceeded.setStatus(
        ""
    )

ncmalmCVL15MINThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 11141)
)
ncmalmCVL15MINThresholdExceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmCVL15MINThresholdExceeded.setStatus(
        ""
    )

ncmalmCVL24HRThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 11142)
)
ncmalmCVL24HRThresholdExceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmCVL24HRThresholdExceeded.setStatus(
        ""
    )

ncmalmESL15MINThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 11143)
)
ncmalmESL15MINThresholdExceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmESL15MINThresholdExceeded.setStatus(
        ""
    )

ncmalmESL24HRThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 11144)
)
ncmalmESL24HRThresholdExceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmESL24HRThresholdExceeded.setStatus(
        ""
    )

ncmalmSESL15MINThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 11145)
)
ncmalmSESL15MINThresholdExceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmSESL15MINThresholdExceeded.setStatus(
        ""
    )

ncmalmSESL24HRThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 11146)
)
ncmalmSESL24HRThresholdExceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmSESL24HRThresholdExceeded.setStatus(
        ""
    )

ncmalmUASP15MINThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 11147)
)
ncmalmUASP15MINThresholdExceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmUASP15MINThresholdExceeded.setStatus(
        ""
    )

ncmalmUASP24HRThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 11148)
)
ncmalmUASP24HRThresholdExceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmUASP24HRThresholdExceeded.setStatus(
        ""
    )

ncmalmBBERThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 11149)
)
ncmalmBBERThresholdExceeded.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmBBERThresholdExceeded.setStatus(
        ""
    )

ncmalmDataPortRTS = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 11160)
)
ncmalmDataPortRTS.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmDataPortRTS.setStatus(
        ""
    )

ncmalmDataPortDTR = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 11161)
)
ncmalmDataPortDTR.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmDataPortDTR.setStatus(
        ""
    )

ncmalmImxDTEport = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 12105)
)
ncmalmImxDTEport.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmImxDTEport.setStatus(
        ""
    )

ncmalmImxDTEportReady = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 12106)
)
ncmalmImxDTEportReady.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmImxDTEportReady.setStatus(
        ""
    )

ncmalmImxLocOsc = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 12107)
)
ncmalmImxLocOsc.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmImxLocOsc.setStatus(
        ""
    )

ncmalmImxLocOscClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 12108)
)
ncmalmImxLocOscClear.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmImxLocOscClear.setStatus(
        ""
    )

ncmalmLn1BndwidClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 12111)
)
ncmalmLn1BndwidClear.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmLn1BndwidClear.setStatus(
        ""
    )

ncmimuxLn1Bndwid = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 12112)
)
ncmimuxLn1Bndwid.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmimuxLn1Bndwid.setStatus(
        ""
    )

ncmimuxLn2BndwidClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 12113)
)
ncmimuxLn2BndwidClear.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmimuxLn2BndwidClear.setStatus(
        ""
    )

ncmimuxLn2Bndwid = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 12114)
)
ncmimuxLn2Bndwid.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmimuxLn2Bndwid.setStatus(
        ""
    )

ncmimuxLn3BndwidClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 12115)
)
ncmimuxLn3BndwidClear.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmimuxLn3BndwidClear.setStatus(
        ""
    )

ncmimuxLn3Bndwid = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 12116)
)
ncmimuxLn3Bndwid.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmimuxLn3Bndwid.setStatus(
        ""
    )

ncmimuxLn4BndwidClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 12117)
)
ncmimuxLn4BndwidClear.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmimuxLn4BndwidClear.setStatus(
        ""
    )

ncmimuxLn4Bndwid = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 12118)
)
ncmimuxLn4Bndwid.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmimuxLn4Bndwid.setStatus(
        ""
    )

ncmimuxLn5BndwidClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 12121)
)
ncmimuxLn5BndwidClear.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmimuxLn5BndwidClear.setStatus(
        ""
    )

ncmimuxLn5Bndwid = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 12122)
)
ncmimuxLn5Bndwid.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmimuxLn5Bndwid.setStatus(
        ""
    )

ncmimuxLn6BndwidClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 12123)
)
ncmimuxLn6BndwidClear.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmimuxLn6BndwidClear.setStatus(
        ""
    )

ncmimuxLn6Bndwid = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 12124)
)
ncmimuxLn6Bndwid.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmimuxLn6Bndwid.setStatus(
        ""
    )

ncmimuxLn7BndwidClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 12125)
)
ncmimuxLn7BndwidClear.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmimuxLn7BndwidClear.setStatus(
        ""
    )

ncmimuxLn7Bndwid = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 12126)
)
ncmimuxLn7Bndwid.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmimuxLn7Bndwid.setStatus(
        ""
    )

ncmimuxLn8BndwidClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 12127)
)
ncmimuxLn8BndwidClear.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmimuxLn8BndwidClear.setStatus(
        ""
    )

ncmimuxLn8Bndwid = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 12128)
)
ncmimuxLn8Bndwid.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmimuxLn8Bndwid.setStatus(
        ""
    )

ncmimuxELBLoopbackActivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 12131)
)
ncmimuxELBLoopbackActivated.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmimuxELBLoopbackActivated.setStatus(
        ""
    )

ncmimuxELBLoopbackDeActivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 12132)
)
ncmimuxELBLoopbackDeActivated.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmimuxELBLoopbackDeActivated.setStatus(
        ""
    )

ncmimuxPLBLoopbackActivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 12133)
)
ncmimuxPLBLoopbackActivated.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmimuxPLBLoopbackActivated.setStatus(
        ""
    )

ncmimuxPLBLoopbackDeActivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 12134)
)
ncmimuxPLBLoopbackDeActivated.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmimuxPLBLoopbackDeActivated.setStatus(
        ""
    )

ncmimuxILBLoopbackActivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 12135)
)
ncmimuxILBLoopbackActivated.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmimuxILBLoopbackActivated.setStatus(
        ""
    )

ncmimuxILBLoopbackDeActivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 12136)
)
ncmimuxILBLoopbackDeActivated.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmimuxILBLoopbackDeActivated.setStatus(
        ""
    )

ncmPriIllegalConfiguration = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 13401)
)
ncmPriIllegalConfiguration.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmPriIllegalConfiguration.setStatus(
        ""
    )

ncmPriL2Up = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 13402)
)
ncmPriL2Up.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmPriL2Up.setStatus(
        ""
    )

ncmPriL2Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 13403)
)
ncmPriL2Down.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmPriL2Down.setStatus(
        ""
    )

ncmPriDISCReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 13404)
)
ncmPriDISCReceived.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmPriDISCReceived.setStatus(
        ""
    )

ncmPriDISCSent = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 13405)
)
ncmPriDISCSent.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmPriDISCSent.setStatus(
        ""
    )

ncmPriL2IllegalMessageReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 13406)
)
ncmPriL2IllegalMessageReceived.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmPriL2IllegalMessageReceived.setStatus(
        ""
    )

ncmPriUnknownAcpCommand = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 13407)
)
ncmPriUnknownAcpCommand.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmPriUnknownAcpCommand.setStatus(
        ""
    )

ncmPriIllegalAcpCommand = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 13408)
)
ncmPriIllegalAcpCommand.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmPriIllegalAcpCommand.setStatus(
        ""
    )

ncmPriL3Up = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 13410)
)
ncmPriL3Up.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmPriL3Up.setStatus(
        ""
    )

ncmPriL3Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 13411)
)
ncmPriL3Down.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmPriL3Down.setStatus(
        ""
    )

ncmPriDChannelBackupSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 13412)
)
ncmPriDChannelBackupSuccess.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmPriDChannelBackupSuccess.setStatus(
        ""
    )

ncmPriDChannelBackupFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 13413)
)
ncmPriDChannelBackupFailure.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmPriDChannelBackupFailure.setStatus(
        ""
    )

ncmPriL3IllegalMessageReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 13414)
)
ncmPriL3IllegalMessageReceived.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmPriL3IllegalMessageReceived.setStatus(
        ""
    )

ncmPriL3SwitchError = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 13415)
)
ncmPriL3SwitchError.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmPriL3SwitchError.setStatus(
        ""
    )

ncmPriCallSetUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 13416)
)
ncmPriCallSetUp.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmPriCallSetUp.setStatus(
        ""
    )

ncmPriCallSetUpFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 13417)
)
ncmPriCallSetUpFailure.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmPriCallSetUpFailure.setStatus(
        ""
    )

ncmPriCallTakeDownSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 13418)
)
ncmPriCallTakeDownSuccess.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmPriCallTakeDownSuccess.setStatus(
        ""
    )

ncmPriCallTakeDownFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 13419)
)
ncmPriCallTakeDownFailure.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmPriCallTakeDownFailure.setStatus(
        ""
    )

ncmPriTestCallFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 13420)
)
ncmPriTestCallFailure.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmPriTestCallFailure.setStatus(
        ""
    )

ncmPriSecurityIncomingCallReject = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 13421)
)
ncmPriSecurityIncomingCallReject.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmPriSecurityIncomingCallReject.setStatus(
        ""
    )

ncmPriSecurityOutgoingCallReject = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 13422)
)
ncmPriSecurityOutgoingCallReject.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmPriSecurityOutgoingCallReject.setStatus(
        ""
    )

ncmPriStackUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 13423)
)
ncmPriStackUp.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmPriStackUp.setStatus(
        ""
    )

ncmPriStackDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 13424)
)
ncmPriStackDown.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmPriStackDown.setStatus(
        ""
    )

ncmPriApplicationIllegalMessage = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 13425)
)
ncmPriApplicationIllegalMessage.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmPriApplicationIllegalMessage.setStatus(
        ""
    )

ncmPriCircuitBuilderCallReject = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 13426)
)
ncmPriCircuitBuilderCallReject.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmPriCircuitBuilderCallReject.setStatus(
        ""
    )

ncmPriStackActivationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 13427)
)
ncmPriStackActivationFailure.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmPriStackActivationFailure.setStatus(
        ""
    )

ncmPriCircuitManagerCallRejectTakeDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 13428)
)
ncmPriCircuitManagerCallRejectTakeDown.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmPriCircuitManagerCallRejectTakeDown.setStatus(
        ""
    )

ncmDS3LosOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14001)
)
ncmDS3LosOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3LosOn.setStatus(
        ""
    )

ncmDS3LosOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14002)
)
ncmDS3LosOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3LosOff.setStatus(
        ""
    )

ncmDS3OOFOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14003)
)
ncmDS3OOFOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3OOFOn.setStatus(
        ""
    )

ncmDS3OOFOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14004)
)
ncmDS3OOFOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3OOFOff.setStatus(
        ""
    )

ncmDS3AISOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14005)
)
ncmDS3AISOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3AISOn.setStatus(
        ""
    )

ncmDS3AISOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14006)
)
ncmDS3AISOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3AISOff.setStatus(
        ""
    )

ncmDS3IdleOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14007)
)
ncmDS3IdleOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3IdleOn.setStatus(
        ""
    )

ncmDS3IdleOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14008)
)
ncmDS3IdleOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3IdleOff.setStatus(
        ""
    )

ncmDS3YellowOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14009)
)
ncmDS3YellowOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3YellowOn.setStatus(
        ""
    )

ncmDS3YellowOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14010)
)
ncmDS3YellowOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3YellowOff.setStatus(
        ""
    )

ncmDS3LOSFailureOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14040)
)
ncmDS3LOSFailureOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3LOSFailureOn.setStatus(
        ""
    )

ncmDS3LOSFailureOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14041)
)
ncmDS3LOSFailureOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3LOSFailureOff.setStatus(
        ""
    )

ncmDS3OutOfFrameFailureOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14042)
)
ncmDS3OutOfFrameFailureOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3OutOfFrameFailureOn.setStatus(
        ""
    )

ncmDS3OutOfFrameFailureOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14043)
)
ncmDS3OutOfFrameFailureOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3OutOfFrameFailureOff.setStatus(
        ""
    )

ncmDS3AISFailureOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14046)
)
ncmDS3AISFailureOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3AISFailureOn.setStatus(
        ""
    )

ncmDS3AISFailureOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14047)
)
ncmDS3AISFailureOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3AISFailureOff.setStatus(
        ""
    )

ncmDS3ReceiveFIFOOverflowOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14048)
)
ncmDS3ReceiveFIFOOverflowOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3ReceiveFIFOOverflowOn.setStatus(
        ""
    )

ncmDS3ReceiveFIFOOverflowOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14049)
)
ncmDS3ReceiveFIFOOverflowOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3ReceiveFIFOOverflowOff.setStatus(
        ""
    )

ncmDS3TransmitFIFOOverflowOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14050)
)
ncmDS3TransmitFIFOOverflowOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3TransmitFIFOOverflowOn.setStatus(
        ""
    )

ncmDS3TransmitFIFOOverflowOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14051)
)
ncmDS3TransmitFIFOOverflowOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3TransmitFIFOOverflowOff.setStatus(
        ""
    )

ncmDS3LossTransmitClockOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14052)
)
ncmDS3LossTransmitClockOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3LossTransmitClockOn.setStatus(
        ""
    )

ncmDS3LossTransmitClockOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14053)
)
ncmDS3LossTransmitClockOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3LossTransmitClockOff.setStatus(
        ""
    )

ncmDS3ncmFarEndBlockErrorOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14054)
)
ncmDS3ncmFarEndBlockErrorOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3ncmFarEndBlockErrorOn.setStatus(
        ""
    )

ncmDS3ncmFarEndBlockErrorOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14055)
)
ncmDS3ncmFarEndBlockErrorOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3ncmFarEndBlockErrorOff.setStatus(
        ""
    )

ncmDS3QRTLCVCrossThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14080)
)
ncmDS3QRTLCVCrossThreshold.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3QRTLCVCrossThreshold.setStatus(
        ""
    )

ncmDS3QRTLESCrossThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14081)
)
ncmDS3QRTLESCrossThreshold.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3QRTLESCrossThreshold.setStatus(
        ""
    )

ncmDS3QRTLSESCrossThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14082)
)
ncmDS3QRTLSESCrossThreshold.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3QRTLSESCrossThreshold.setStatus(
        ""
    )

ncmDS3QRTPCVCrossThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14083)
)
ncmDS3QRTPCVCrossThreshold.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3QRTPCVCrossThreshold.setStatus(
        ""
    )

ncmDS3QRTPESCrossThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14084)
)
ncmDS3QRTPESCrossThreshold.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3QRTPESCrossThreshold.setStatus(
        ""
    )

ncmDS3QRTPSESCrossThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14085)
)
ncmDS3QRTPSESCrossThreshold.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3QRTPSESCrossThreshold.setStatus(
        ""
    )

ncmDS3QRTSEFSCrossThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14086)
)
ncmDS3QRTSEFSCrossThreshold.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3QRTSEFSCrossThreshold.setStatus(
        ""
    )

ncmDS3QRTAISSCrossThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14087)
)
ncmDS3QRTAISSCrossThreshold.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3QRTAISSCrossThreshold.setStatus(
        ""
    )

ncmDS3QRTUASCrossThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14088)
)
ncmDS3QRTUASCrossThreshold.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3QRTUASCrossThreshold.setStatus(
        ""
    )

ncmDS3QRTCCVCrossThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14097)
)
ncmDS3QRTCCVCrossThreshold.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3QRTCCVCrossThreshold.setStatus(
        ""
    )

ncmDS3QRTCESCrossThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14098)
)
ncmDS3QRTCESCrossThreshold.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3QRTCESCrossThreshold.setStatus(
        ""
    )

ncmDS3QRTCSESCrossThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14099)
)
ncmDS3QRTCSESCrossThreshold.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3QRTCSESCrossThreshold.setStatus(
        ""
    )

ncmDS3QRTLOSSCrossThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14100)
)
ncmDS3QRTLOSSCrossThreshold.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3QRTLOSSCrossThreshold.setStatus(
        ""
    )

ncmDS3QRTLOFCCrossThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14101)
)
ncmDS3QRTLOFCCrossThreshold.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3QRTLOFCCrossThreshold.setStatus(
        ""
    )

ncmDS3ncmFarEndQRTCCVCrossThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14102)
)
ncmDS3ncmFarEndQRTCCVCrossThreshold.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3ncmFarEndQRTCCVCrossThreshold.setStatus(
        ""
    )

ncmDS3ncmFarEndQRTCESCrossThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14103)
)
ncmDS3ncmFarEndQRTCESCrossThreshold.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3ncmFarEndQRTCESCrossThreshold.setStatus(
        ""
    )

ncmDS3ncmFarEndQRTCSESCrossThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14104)
)
ncmDS3ncmFarEndQRTCSESCrossThreshold.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3ncmFarEndQRTCSESCrossThreshold.setStatus(
        ""
    )

ncmDS3ncmFarEndQRTUASCrossThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14105)
)
ncmDS3ncmFarEndQRTUASCrossThreshold.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3ncmFarEndQRTUASCrossThreshold.setStatus(
        ""
    )

ncmDS3DayLCVCrossThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14112)
)
ncmDS3DayLCVCrossThreshold.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3DayLCVCrossThreshold.setStatus(
        ""
    )

ncmDS3DayLESCrossThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14113)
)
ncmDS3DayLESCrossThreshold.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3DayLESCrossThreshold.setStatus(
        ""
    )

ncmDS3DayLSESCrossThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14114)
)
ncmDS3DayLSESCrossThreshold.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3DayLSESCrossThreshold.setStatus(
        ""
    )

ncmDS3DayPCVCrossThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14115)
)
ncmDS3DayPCVCrossThreshold.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3DayPCVCrossThreshold.setStatus(
        ""
    )

ncmDS3DayPESCrossThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14116)
)
ncmDS3DayPESCrossThreshold.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3DayPESCrossThreshold.setStatus(
        ""
    )

ncmDS3DayPSESCrossThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14117)
)
ncmDS3DayPSESCrossThreshold.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3DayPSESCrossThreshold.setStatus(
        ""
    )

ncmDS3DayPSEFSCrossThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14118)
)
ncmDS3DayPSEFSCrossThreshold.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3DayPSEFSCrossThreshold.setStatus(
        ""
    )

ncmDS3DayAISSCrossThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14119)
)
ncmDS3DayAISSCrossThreshold.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3DayAISSCrossThreshold.setStatus(
        ""
    )

ncmDS3DayUASCrossThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14120)
)
ncmDS3DayUASCrossThreshold.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3DayUASCrossThreshold.setStatus(
        ""
    )

ncmDS3DayCCVCrossThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14129)
)
ncmDS3DayCCVCrossThreshold.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3DayCCVCrossThreshold.setStatus(
        ""
    )

ncmDS3DayCESCrossThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14130)
)
ncmDS3DayCESCrossThreshold.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3DayCESCrossThreshold.setStatus(
        ""
    )

ncmDS3DayCSESCrossThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14131)
)
ncmDS3DayCSESCrossThreshold.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3DayCSESCrossThreshold.setStatus(
        ""
    )

ncmDS3DayLOSSCrossThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14132)
)
ncmDS3DayLOSSCrossThreshold.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3DayLOSSCrossThreshold.setStatus(
        ""
    )

ncmDS3DayLOFCCrossThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14133)
)
ncmDS3DayLOFCCrossThreshold.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3DayLOFCCrossThreshold.setStatus(
        ""
    )

ncmDS3ncmFarEndDayCCVCrossThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14134)
)
ncmDS3ncmFarEndDayCCVCrossThreshold.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3ncmFarEndDayCCVCrossThreshold.setStatus(
        ""
    )

ncmDS3ncmFarEndDayCESCrossThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14135)
)
ncmDS3ncmFarEndDayCESCrossThreshold.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3ncmFarEndDayCESCrossThreshold.setStatus(
        ""
    )

ncmDS3ncmFarEndDayCSESCrossThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14136)
)
ncmDS3ncmFarEndDayCSESCrossThreshold.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3ncmFarEndDayCSESCrossThreshold.setStatus(
        ""
    )

ncmDS3ncmFarEndDayUASCrossThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14137)
)
ncmDS3ncmFarEndDayUASCrossThreshold.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3ncmFarEndDayUASCrossThreshold.setStatus(
        ""
    )

ncmDS3IPCChannelFailureOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14145)
)
ncmDS3IPCChannelFailureOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3IPCChannelFailureOn.setStatus(
        ""
    )

ncmDS3IPCChannelFailureOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14146)
)
ncmDS3IPCChannelFailureOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3IPCChannelFailureOff.setStatus(
        ""
    )

ncmDS3SARCardMajorAlarmOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14147)
)
ncmDS3SARCardMajorAlarmOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3SARCardMajorAlarmOn.setStatus(
        ""
    )

ncmDS3SARCardMajorAlarmOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14148)
)
ncmDS3SARCardMajorAlarmOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3SARCardMajorAlarmOff.setStatus(
        ""
    )

ncmDS3DxiHeartBeatFailureOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14149)
)
ncmDS3DxiHeartBeatFailureOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3DxiHeartBeatFailureOn.setStatus(
        ""
    )

ncmDS3DxiHeartBeatFailureOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14150)
)
ncmDS3DxiHeartBeatFailureOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3DxiHeartBeatFailureOff.setStatus(
        ""
    )

ncmDS3HSSIPortUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14151)
)
ncmDS3HSSIPortUp.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3HSSIPortUp.setStatus(
        ""
    )

ncmDS3HSSIPortDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14152)
)
ncmDS3HSSIPortDown.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3HSSIPortDown.setStatus(
        ""
    )

ncmDS3FEACEquipmentFailureSAOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14160)
)
ncmDS3FEACEquipmentFailureSAOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3FEACEquipmentFailureSAOn.setStatus(
        ""
    )

ncmDS3FEACLosOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14161)
)
ncmDS3FEACLosOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3FEACLosOn.setStatus(
        ""
    )

ncmDS3FEACOOFOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14162)
)
ncmDS3FEACOOFOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3FEACOOFOn.setStatus(
        ""
    )

ncmDS3FEACAISOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14163)
)
ncmDS3FEACAISOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3FEACAISOn.setStatus(
        ""
    )

ncmDS3FEACIDLEOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14164)
)
ncmDS3FEACIDLEOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3FEACIDLEOn.setStatus(
        ""
    )

ncmDS3FEACEqptFailureNSAOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14165)
)
ncmDS3FEACEqptFailureNSAOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3FEACEqptFailureNSAOn.setStatus(
        ""
    )

ncmDS3FEACCommonEqptFailureOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14166)
)
ncmDS3FEACCommonEqptFailureOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3FEACCommonEqptFailureOn.setStatus(
        ""
    )

ncmDS3FEACMultiDs1LosHBEROn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14167)
)
ncmDS3FEACMultiDs1LosHBEROn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3FEACMultiDs1LosHBEROn.setStatus(
        ""
    )

ncmDS3FEACDs1EqptFailureOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14168)
)
ncmDS3FEACDs1EqptFailureOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3FEACDs1EqptFailureOn.setStatus(
        ""
    )

ncmDS3FEACSingleDs1LosHBEROn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14169)
)
ncmDS3FEACSingleDs1LosHBEROn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3FEACSingleDs1LosHBEROn.setStatus(
        ""
    )

ncmDS3FEACDs1EqptFailureNSAOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14170)
)
ncmDS3FEACDs1EqptFailureNSAOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3FEACDs1EqptFailureNSAOn.setStatus(
        ""
    )

ncmDS3FEACLineLoopActivationOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14171)
)
ncmDS3FEACLineLoopActivationOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3FEACLineLoopActivationOn.setStatus(
        ""
    )

ncmDS3FEACLineLoopDeActivationOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14172)
)
ncmDS3FEACLineLoopDeActivationOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3FEACLineLoopDeActivationOn.setStatus(
        ""
    )

ncmDS3FEACLineOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14173)
)
ncmDS3FEACLineOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3FEACLineOn.setStatus(
        ""
    )

ncmDS3FEACEquipmentFailureSAOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14176)
)
ncmDS3FEACEquipmentFailureSAOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3FEACEquipmentFailureSAOff.setStatus(
        ""
    )

ncmDS3FEACLosOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14177)
)
ncmDS3FEACLosOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3FEACLosOff.setStatus(
        ""
    )

ncmDS3FEACOOFOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14178)
)
ncmDS3FEACOOFOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3FEACOOFOff.setStatus(
        ""
    )

ncmDS3FEACAISOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14179)
)
ncmDS3FEACAISOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3FEACAISOff.setStatus(
        ""
    )

ncmDS3FEACIDLEOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14180)
)
ncmDS3FEACIDLEOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3FEACIDLEOff.setStatus(
        ""
    )

ncmDS3FEACEqptFailureNSAOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14181)
)
ncmDS3FEACEqptFailureNSAOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3FEACEqptFailureNSAOff.setStatus(
        ""
    )

ncmDS3FEACCommonEqptFailureOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14182)
)
ncmDS3FEACCommonEqptFailureOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3FEACCommonEqptFailureOff.setStatus(
        ""
    )

ncmDS3FEACMultiDs1LosHBEROff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14183)
)
ncmDS3FEACMultiDs1LosHBEROff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3FEACMultiDs1LosHBEROff.setStatus(
        ""
    )

ncmDS3FEACDs1EqptFailureOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14184)
)
ncmDS3FEACDs1EqptFailureOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3FEACDs1EqptFailureOff.setStatus(
        ""
    )

ncmDS3FEACSingleDs1LosHBEROff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14185)
)
ncmDS3FEACSingleDs1LosHBEROff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3FEACSingleDs1LosHBEROff.setStatus(
        ""
    )

ncmDS3FEACDs1EqptFailureNSAOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14186)
)
ncmDS3FEACDs1EqptFailureNSAOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3FEACDs1EqptFailureNSAOff.setStatus(
        ""
    )

ncmDS3FEACLineLoopActivationOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14187)
)
ncmDS3FEACLineLoopActivationOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3FEACLineLoopActivationOff.setStatus(
        ""
    )

ncmDS3FEACLineLoopDeActivationOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14188)
)
ncmDS3FEACLineLoopDeActivationOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3FEACLineLoopDeActivationOff.setStatus(
        ""
    )

ncmDS3FEACLineOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14189)
)
ncmDS3FEACLineOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3FEACLineOff.setStatus(
        ""
    )

ncmDS3DataRateSetFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14224)
)
ncmDS3DataRateSetFailure.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3DataRateSetFailure.setStatus(
        ""
    )

ncmDS3TransmitFEACLineLoopActivationOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14225)
)
ncmDS3TransmitFEACLineLoopActivationOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3TransmitFEACLineLoopActivationOn.setStatus(
        ""
    )

ncmDS3TransmitFEACLineLoopActivationOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14226)
)
ncmDS3TransmitFEACLineLoopActivationOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3TransmitFEACLineLoopActivationOff.setStatus(
        ""
    )

ncmDS3TransmitFEACLineLoopDeActivationOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14227)
)
ncmDS3TransmitFEACLineLoopDeActivationOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3TransmitFEACLineLoopDeActivationOn.setStatus(
        ""
    )

ncmDS3TransmitFEACLineLoopDeActivationOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14228)
)
ncmDS3TransmitFEACLineLoopDeActivationOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3TransmitFEACLineLoopDeActivationOff.setStatus(
        ""
    )

ncmDS3TransmitYellowAlarmOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14229)
)
ncmDS3TransmitYellowAlarmOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3TransmitYellowAlarmOn.setStatus(
        ""
    )

ncmDS3TransmitYellowAlarmOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14230)
)
ncmDS3TransmitYellowAlarmOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3TransmitYellowAlarmOff.setStatus(
        ""
    )

ncmDS3TransmitAISAlarmOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14231)
)
ncmDS3TransmitAISAlarmOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3TransmitAISAlarmOn.setStatus(
        ""
    )

ncmDS3TransmitAISAlarmOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14232)
)
ncmDS3TransmitAISAlarmOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3TransmitAISAlarmOff.setStatus(
        ""
    )

ncmDS3TransmitIdleAlarmOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14233)
)
ncmDS3TransmitIdleAlarmOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3TransmitIdleAlarmOn.setStatus(
        ""
    )

ncmDS3TransmitIdleAlarmOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14234)
)
ncmDS3TransmitIdleAlarmOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3TransmitIdleAlarmOff.setStatus(
        ""
    )

ncmDS3TransmitFEBEAlarmOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14235)
)
ncmDS3TransmitFEBEAlarmOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3TransmitFEBEAlarmOn.setStatus(
        ""
    )

ncmDS3TransmitFEBEAlarmOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14236)
)
ncmDS3TransmitFEBEAlarmOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3TransmitFEBEAlarmOff.setStatus(
        ""
    )

ncmDS3TransmitFEACLosOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14239)
)
ncmDS3TransmitFEACLosOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3TransmitFEACLosOn.setStatus(
        ""
    )

ncmDS3TransmitFEACLosOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14240)
)
ncmDS3TransmitFEACLosOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3TransmitFEACLosOff.setStatus(
        ""
    )

ncmDS3TransmitFEACOOFOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14241)
)
ncmDS3TransmitFEACOOFOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3TransmitFEACOOFOn.setStatus(
        ""
    )

ncmDS3TransmitFEACOOFOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14242)
)
ncmDS3TransmitFEACOOFOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3TransmitFEACOOFOff.setStatus(
        ""
    )

ncmDS3TransmitFEACAISOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14243)
)
ncmDS3TransmitFEACAISOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3TransmitFEACAISOn.setStatus(
        ""
    )

ncmDS3TransmitFEACAISOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14244)
)
ncmDS3TransmitFEACAISOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3TransmitFEACAISOff.setStatus(
        ""
    )

ncmDS3TransmitFEACIdleOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14245)
)
ncmDS3TransmitFEACIdleOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3TransmitFEACIdleOn.setStatus(
        ""
    )

ncmDS3TransmitFEACIdleOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14246)
)
ncmDS3TransmitFEACIdleOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3TransmitFEACIdleOff.setStatus(
        ""
    )

ncmDS3TransmitFEACEqptFailureNSAOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14247)
)
ncmDS3TransmitFEACEqptFailureNSAOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3TransmitFEACEqptFailureNSAOn.setStatus(
        ""
    )

ncmDS3TransmitFEACEqptFailureNSAOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14248)
)
ncmDS3TransmitFEACEqptFailureNSAOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3TransmitFEACEqptFailureNSAOff.setStatus(
        ""
    )

ncmDS3TransmitFEACCommonEqptFailureNSAOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14249)
)
ncmDS3TransmitFEACCommonEqptFailureNSAOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3TransmitFEACCommonEqptFailureNSAOn.setStatus(
        ""
    )

ncmDS3TransmitFEACCommonEqptFailureNSAOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14250)
)
ncmDS3TransmitFEACCommonEqptFailureNSAOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3TransmitFEACCommonEqptFailureNSAOff.setStatus(
        ""
    )

ncmDS3TransmitFEACLineOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14251)
)
ncmDS3TransmitFEACLineOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3TransmitFEACLineOn.setStatus(
        ""
    )

ncmDS3TransmitFEACLineOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14252)
)
ncmDS3TransmitFEACLineOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3TransmitFEACLineOff.setStatus(
        ""
    )

ncmDS3TransmitFEACNoAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14253)
)
ncmDS3TransmitFEACNoAlarm.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3TransmitFEACNoAlarm.setStatus(
        ""
    )

ncmDS3UserLocalLoopbackOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14256)
)
ncmDS3UserLocalLoopbackOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3UserLocalLoopbackOn.setStatus(
        ""
    )

ncmDS3UserLocalLoopbackOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14257)
)
ncmDS3UserLocalLoopbackOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3UserLocalLoopbackOff.setStatus(
        ""
    )

ncmDS3UserPayloadLoopbackOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14258)
)
ncmDS3UserPayloadLoopbackOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3UserPayloadLoopbackOn.setStatus(
        ""
    )

ncmDS3UserPayloadLoopbackOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14259)
)
ncmDS3UserPayloadLoopbackOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3UserPayloadLoopbackOff.setStatus(
        ""
    )

ncmDS3UserEquipmentLoopbackOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14260)
)
ncmDS3UserEquipmentLoopbackOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3UserEquipmentLoopbackOn.setStatus(
        ""
    )

ncmDS3UserEquipmentLoopbackOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14261)
)
ncmDS3UserEquipmentLoopbackOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3UserEquipmentLoopbackOff.setStatus(
        ""
    )

ncmDS3UserNoLoopbackOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14262)
)
ncmDS3UserNoLoopbackOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3UserNoLoopbackOn.setStatus(
        ""
    )

ncmDS3UserNoLoopbackOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14263)
)
ncmDS3UserNoLoopbackOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3UserNoLoopbackOff.setStatus(
        ""
    )

ncmDS3HSSILocalLoopbackOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14264)
)
ncmDS3HSSILocalLoopbackOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3HSSILocalLoopbackOn.setStatus(
        ""
    )

ncmDS3HSSILocalLoopbackOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14265)
)
ncmDS3HSSILocalLoopbackOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3HSSILocalLoopbackOff.setStatus(
        ""
    )

ncmDS3HSSIPayloadLoopbackOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14266)
)
ncmDS3HSSIPayloadLoopbackOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3HSSIPayloadLoopbackOn.setStatus(
        ""
    )

ncmDS3HSSIPayloadLoopbackOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14267)
)
ncmDS3HSSIPayloadLoopbackOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3HSSIPayloadLoopbackOff.setStatus(
        ""
    )

ncmDS3HSSIEquipmentLoopbackOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14268)
)
ncmDS3HSSIEquipmentLoopbackOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3HSSIEquipmentLoopbackOn.setStatus(
        ""
    )

ncmDS3HSSIEquipmentLoopbackOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14269)
)
ncmDS3HSSIEquipmentLoopbackOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3HSSIEquipmentLoopbackOff.setStatus(
        ""
    )

ncmDS3HSSINoLoopbackOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14270)
)
ncmDS3HSSINoLoopbackOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3HSSINoLoopbackOn.setStatus(
        ""
    )

ncmDS3HSSINoLoopbackOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14271)
)
ncmDS3HSSINoLoopbackOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3HSSINoLoopbackOff.setStatus(
        ""
    )

ncmDS3ncmFarEndLocalLoopbackOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14272)
)
ncmDS3ncmFarEndLocalLoopbackOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3ncmFarEndLocalLoopbackOn.setStatus(
        ""
    )

ncmDS3ncmFarEndLocalLoopbackOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14273)
)
ncmDS3ncmFarEndLocalLoopbackOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3ncmFarEndLocalLoopbackOff.setStatus(
        ""
    )

ncmDS3ncmFarEndPayloadLoopbackOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14274)
)
ncmDS3ncmFarEndPayloadLoopbackOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3ncmFarEndPayloadLoopbackOn.setStatus(
        ""
    )

ncmDS3ncmFarEndPayloadLoopbackOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14275)
)
ncmDS3ncmFarEndPayloadLoopbackOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3ncmFarEndPayloadLoopbackOff.setStatus(
        ""
    )

ncmDS3ncmFarEndEqptLoopbackOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14276)
)
ncmDS3ncmFarEndEqptLoopbackOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3ncmFarEndEqptLoopbackOn.setStatus(
        ""
    )

ncmDS3ncmFarEndEqptLoopbackOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14277)
)
ncmDS3ncmFarEndEqptLoopbackOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3ncmFarEndEqptLoopbackOff.setStatus(
        ""
    )

ncmDS3ncmFarEndNoLoopbackOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14278)
)
ncmDS3ncmFarEndNoLoopbackOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3ncmFarEndNoLoopbackOn.setStatus(
        ""
    )

ncmDS3ncmFarEndNoLoopbackOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14279)
)
ncmDS3ncmFarEndNoLoopbackOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3ncmFarEndNoLoopbackOff.setStatus(
        ""
    )

ncmDS3ncmFarEndPayloadLoopbackOnFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14280)
)
ncmDS3ncmFarEndPayloadLoopbackOnFailure.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3ncmFarEndPayloadLoopbackOnFailure.setStatus(
        ""
    )

ncmDS3ncmFarEndPayloadLoopbackOffFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14281)
)
ncmDS3ncmFarEndPayloadLoopbackOffFailure.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3ncmFarEndPayloadLoopbackOffFailure.setStatus(
        ""
    )

ncmDS3UserEquipmentLoopbackOnPortTwo = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14288)
)
ncmDS3UserEquipmentLoopbackOnPortTwo.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3UserEquipmentLoopbackOnPortTwo.setStatus(
        ""
    )

ncmDS3UserEquipmentLoopbackOFFPortTwo = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14289)
)
ncmDS3UserEquipmentLoopbackOFFPortTwo.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3UserEquipmentLoopbackOFFPortTwo.setStatus(
        ""
    )

ncmDS3HssiEquipmentLoopbackOnPortTwo = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14290)
)
ncmDS3HssiEquipmentLoopbackOnPortTwo.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3HssiEquipmentLoopbackOnPortTwo.setStatus(
        ""
    )

ncmDS3HssiEquipmentLoopbackOFFPortTwo = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14291)
)
ncmDS3HssiEquipmentLoopbackOFFPortTwo.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3HssiEquipmentLoopbackOFFPortTwo.setStatus(
        ""
    )

ncmDS3FarEndEquipmentLoopbackONPortTwo = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14292)
)
ncmDS3FarEndEquipmentLoopbackONPortTwo.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3FarEndEquipmentLoopbackONPortTwo.setStatus(
        ""
    )

ncmDS3FarEndEquipmentLoopbackOFFPortTwo = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14293)
)
ncmDS3FarEndEquipmentLoopbackOFFPortTwo.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3FarEndEquipmentLoopbackOFFPortTwo.setStatus(
        ""
    )

ncmDS3HssiPortUpPortTwo = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14294)
)
ncmDS3HssiPortUpPortTwo.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3HssiPortUpPortTwo.setStatus(
        ""
    )

ncmDS3HssiPortDownPortTwo = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14295)
)
ncmDS3HssiPortDownPortTwo.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3HssiPortDownPortTwo.setStatus(
        ""
    )

ncmDS3HssiPortOneRateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14296)
)
ncmDS3HssiPortOneRateChange.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3HssiPortOneRateChange.setStatus(
        ""
    )

ncmDS3HssiPortTwoRateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14297)
)
ncmDS3HssiPortTwoRateChange.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3HssiPortTwoRateChange.setStatus(
        ""
    )

ncmDS3HssiPortOneRateChangeFarEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14298)
)
ncmDS3HssiPortOneRateChangeFarEnd.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3HssiPortOneRateChangeFarEnd.setStatus(
        ""
    )

ncmDS3HssiPortTwoRateChangeFarEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14299)
)
ncmDS3HssiPortTwoRateChangeFarEnd.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3HssiPortTwoRateChangeFarEnd.setStatus(
        ""
    )

ncmDS3HssiLocalLoopbackOnDual = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14300)
)
ncmDS3HssiLocalLoopbackOnDual.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3HssiLocalLoopbackOnDual.setStatus(
        ""
    )

ncmDS3HssiLocalLoopbackOffDual = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14301)
)
ncmDS3HssiLocalLoopbackOffDual.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3HssiLocalLoopbackOffDual.setStatus(
        ""
    )

ncmDS3UserLineLoopbackOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14304)
)
ncmDS3UserLineLoopbackOn.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3UserLineLoopbackOn.setStatus(
        ""
    )

ncmDS3UserLineLoopbackOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14305)
)
ncmDS3UserLineLoopbackOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmDS3UserLineLoopbackOff.setStatus(
        ""
    )

ncmT1LOS = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14320)
)
ncmT1LOS.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmT1LOS.setStatus(
        ""
    )

ncmT1LOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14321)
)
ncmT1LOF.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmT1LOF.setStatus(
        ""
    )

ncmT1AIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14322)
)
ncmT1AIS.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmT1AIS.setStatus(
        ""
    )

ncmT1YEL = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14323)
)
ncmT1YEL.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmT1YEL.setStatus(
        ""
    )

ncmT1OUT = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14324)
)
ncmT1OUT.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmT1OUT.setStatus(
        ""
    )

ncmT1LineLoop = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14325)
)
ncmT1LineLoop.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmT1LineLoop.setStatus(
        ""
    )

ncmT1LocalLoop = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14326)
)
ncmT1LocalLoop.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmT1LocalLoop.setStatus(
        ""
    )

ncmT1FarEndLoopback = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14327)
)
ncmT1FarEndLoopback.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmT1FarEndLoopback.setStatus(
        ""
    )

ncmActiveReferenceClockLOS = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14328)
)
ncmActiveReferenceClockLOS.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmActiveReferenceClockLOS.setStatus(
        ""
    )

ncmStandbyReferenceClockLOS = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14329)
)
ncmStandbyReferenceClockLOS.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmStandbyReferenceClockLOS.setStatus(
        ""
    )

ncmBothReferenceClockLOS = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14330)
)
ncmBothReferenceClockLOS.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmBothReferenceClockLOS.setStatus(
        ""
    )

ncmTimeBusLOS = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14331)
)
ncmTimeBusLOS.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmTimeBusLOS.setStatus(
        ""
    )

ncmT1In = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14336)
)
ncmT1In.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmT1In.setStatus(
        ""
    )

ncmT1LineLoopbackOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14337)
)
ncmT1LineLoopbackOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmT1LineLoopbackOff.setStatus(
        ""
    )

ncmT1LocalLoopbackOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14338)
)
ncmT1LocalLoopbackOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmT1LocalLoopbackOff.setStatus(
        ""
    )

ncmT1FarEndLoopbackOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 14339)
)
ncmT1FarEndLoopbackOff.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmT1FarEndLoopbackOff.setStatus(
        ""
    )

ncmnearAceLOSCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 16101)
)
ncmnearAceLOSCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearAceLOSCleared.setStatus(
        ""
    )

ncmnearAceLOFCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 16102)
)
ncmnearAceLOFCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearAceLOFCleared.setStatus(
        ""
    )

ncmnearRemoteAICleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 16103)
)
ncmnearRemoteAICleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearRemoteAICleared.setStatus(
        ""
    )

ncmnearLOMFalignmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 16104)
)
ncmnearLOMFalignmCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearLOMFalignmCleared.setStatus(
        ""
    )

ncmnearRemoteMASCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 16105)
)
ncmnearRemoteMASCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearRemoteMASCleared.setStatus(
        ""
    )

ncmnearIASCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 16106)
)
ncmnearIASCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearIASCleared.setStatus(
        ""
    )

ncmnearFASCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 16107)
)
ncmnearFASCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearFASCleared.setStatus(
        ""
    )

ncmnearFASeXceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 16108)
)
ncmnearFASeXceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearFASeXceededCleared.setStatus(
        ""
    )

ncmnearCVCeXceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 16109)
)
ncmnearCVCeXceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearCVCeXceededCleared.setStatus(
        ""
    )

ncmnearCRCeXceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 16110)
)
ncmnearCRCeXceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearCRCeXceededCleared.setStatus(
        ""
    )

ncmnearFECeXceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 16111)
)
ncmnearFECeXceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearFECeXceededCleared.setStatus(
        ""
    )

ncmnearCarrierCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 16112)
)
ncmnearCarrierCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearCarrierCleared.setStatus(
        ""
    )

ncmnearDwnLdCodeCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 16114)
)
ncmnearDwnLdCodeCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearDwnLdCodeCleared.setStatus(
        ""
    )

ncmnearLActCLKCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 16115)
)
ncmnearLActCLKCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearLActCLKCleared.setStatus(
        ""
    )

ncmnearLstdbyCLKCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 16116)
)
ncmnearLstdbyCLKCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearLstdbyCLKCleared.setStatus(
        ""
    )

ncmnearRefTBUSCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 16117)
)
ncmnearRefTBUSCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearRefTBUSCleared.setStatus(
        ""
    )

ncmnearTBUSCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 16118)
)
ncmnearTBUSCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearTBUSCleared.setStatus(
        ""
    )

ncmnearLLBCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 16120)
)
ncmnearLLBCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearLLBCleared.setStatus(
        ""
    )

ncmnearELBCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 16121)
)
ncmnearELBCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearELBCleared.setStatus(
        ""
    )

ncmnearPLBCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 16122)
)
ncmnearPLBCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearPLBCleared.setStatus(
        ""
    )

ncmnearRLBCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 16123)
)
ncmnearRLBCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmnearRLBCleared.setStatus(
        ""
    )

ncmalmSESExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 16124)
)
ncmalmSESExceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmSESExceededCleared.setStatus(
        ""
    )

ncmalmUASExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 16125)
)
ncmalmUASExceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmUASExceededCleared.setStatus(
        ""
    )

ncmalmBERExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 16126)
)
ncmalmBERExceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmBERExceededCleared.setStatus(
        ""
    )

ncmalmPortDownCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 16129)
)
ncmalmPortDownCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmPortDownCleared.setStatus(
        ""
    )

ncmalmCGACleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 16130)
)
ncmalmCGACleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmCGACleared.setStatus(
        ""
    )

ncmalmLOFThresholdExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 16131)
)
ncmalmLOFThresholdExceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmLOFThresholdExceededCleared.setStatus(
        ""
    )

ncmalmLOSThresholdExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 16132)
)
ncmalmLOSThresholdExceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmLOSThresholdExceededCleared.setStatus(
        ""
    )

ncmalmRAIThresholdExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 16133)
)
ncmalmRAIThresholdExceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmRAIThresholdExceededCleared.setStatus(
        ""
    )

ncmalmAISThresholdExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 16134)
)
ncmalmAISThresholdExceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmAISThresholdExceededCleared.setStatus(
        ""
    )

ncmalmBPVThresholdExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 16135)
)
ncmalmBPVThresholdExceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmBPVThresholdExceededCleared.setStatus(
        ""
    )

ncmalmES15MINThresholdExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 16136)
)
ncmalmES15MINThresholdExceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmES15MINThresholdExceededCleared.setStatus(
        ""
    )

ncmalmES24HRThresholdExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 16137)
)
ncmalmES24HRThresholdExceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmES24HRThresholdExceededCleared.setStatus(
        ""
    )

ncmalmSES15MINThresholdExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 16138)
)
ncmalmSES15MINThresholdExceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmSES15MINThresholdExceededCleared.setStatus(
        ""
    )

ncmalmSES24HRThresholdExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 16139)
)
ncmalmSES24HRThresholdExceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmSES24HRThresholdExceededCleared.setStatus(
        ""
    )

ncmalmCVP15MINThresholdExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 16140)
)
ncmalmCVP15MINThresholdExceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmCVP15MINThresholdExceededCleared.setStatus(
        ""
    )

ncmalmCVP24HRThresholdExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 16141)
)
ncmalmCVP24HRThresholdExceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmCVP24HRThresholdExceededCleared.setStatus(
        ""
    )

ncmalmCVL15MINThresholdExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 16142)
)
ncmalmCVL15MINThresholdExceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmCVL15MINThresholdExceededCleared.setStatus(
        ""
    )

ncmalmCVL24HRThresholdExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 16143)
)
ncmalmCVL24HRThresholdExceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmCVL24HRThresholdExceededCleared.setStatus(
        ""
    )

ncmalmESL15MINThresholdExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 16144)
)
ncmalmESL15MINThresholdExceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmESL15MINThresholdExceededCleared.setStatus(
        ""
    )

ncmalmESL24HRThresholdExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 16145)
)
ncmalmESL24HRThresholdExceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmESL24HRThresholdExceededCleared.setStatus(
        ""
    )

ncmalmSESL15MINThresholdExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 16146)
)
ncmalmSESL15MINThresholdExceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmSESL15MINThresholdExceededCleared.setStatus(
        ""
    )

ncmalmSESL24HRThresholdExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 16147)
)
ncmalmSESL24HRThresholdExceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmSESL24HRThresholdExceededCleared.setStatus(
        ""
    )

ncmalmUASP15MINThresholdExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 16148)
)
ncmalmUASP15MINThresholdExceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmUASP15MINThresholdExceededCleared.setStatus(
        ""
    )

ncmalmUASP24HRThresholdExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 16149)
)
ncmalmUASP24HRThresholdExceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmUASP24HRThresholdExceededCleared.setStatus(
        ""
    )

ncmalmBBERThresholdExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 16150)
)
ncmalmBBERThresholdExceededCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmBBERThresholdExceededCleared.setStatus(
        ""
    )

ncmalmDataPortRTSCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 16161)
)
ncmalmDataPortRTSCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmDataPortRTSCleared.setStatus(
        ""
    )

ncmalmDataPortDTRCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 1, 0, 16162)
)
ncmalmDataPortDTRCleared.setObjects(
      *(("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmNodeAddr"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmShelf"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSlot"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmPort"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmCard"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmTimestamp"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmSeverity"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmInstance"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmEquipId"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmObjectType"),
        ("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncmAlarmString"))
)
if mibBuilder.loadTexts:
    ncmalmDataPortDTRCleared.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VERILINK-ENTERPRISE-NCMALARM-MIB",
    **{"verilink": verilink,
       "as2000": as2000,
       "ncmTrap": ncmTrap,
       "ncmnearCSUPowerUP": ncmnearCSUPowerUP,
       "ncmncmfarCSUPowrUP": ncmncmfarCSUPowrUP,
       "ncmnearBERexceeded": ncmnearBERexceeded,
       "ncmnearBERexceededCleared": ncmnearBERexceededCleared,
       "ncmnearESLexceeded": ncmnearESLexceeded,
       "ncmnearESLexceededCleared": ncmnearESLexceededCleared,
       "ncmnearESexceeded": ncmnearESexceeded,
       "ncmnearESexceededCleared": ncmnearESexceededCleared,
       "ncmnearUASexceeded": ncmnearUASexceeded,
       "ncmnearUASexceededCleared": ncmnearUASexceededCleared,
       "ncmnearLELBlooped": ncmnearLELBlooped,
       "ncmnearLELBloopedCleared": ncmnearLELBloopedCleared,
       "ncmnearPRLBlooped": ncmnearPRLBlooped,
       "ncmnearPRLBloopedCleared": ncmnearPRLBloopedCleared,
       "ncmnearLOS": ncmnearLOS,
       "ncmnearLOSCleared": ncmnearLOSCleared,
       "ncmnearRAI": ncmnearRAI,
       "ncmnearRAICleared": ncmnearRAICleared,
       "ncmnearLOF": ncmnearLOF,
       "ncmnearLOFCleared": ncmnearLOFCleared,
       "ncmnearAIS": ncmnearAIS,
       "ncmnearAISCleared": ncmnearAISCleared,
       "ncmnearTestSIG": ncmnearTestSIG,
       "ncmnearTestSIGCleared": ncmnearTestSIGCleared,
       "ncmnearCSULossExtClk": ncmnearCSULossExtClk,
       "ncmnearCSULossExtClkCleared": ncmnearCSULossExtClkCleared,
       "ncmnearEQPTBERExceeded": ncmnearEQPTBERExceeded,
       "ncmnearEQPTBERExceededCleared": ncmnearEQPTBERExceededCleared,
       "ncmnearEQPTESLExceeded": ncmnearEQPTESLExceeded,
       "ncmnearEQPTESLExceededCleared": ncmnearEQPTESLExceededCleared,
       "ncmnearEQPTESExceeded": ncmnearEQPTESExceeded,
       "ncmnearEQPTESExceededCleared": ncmnearEQPTESExceededCleared,
       "ncmnearEQPTUASExceeded": ncmnearEQPTUASExceeded,
       "ncmnearEQPTUASExceededCleared": ncmnearEQPTUASExceededCleared,
       "ncmnearEQPTELBLooped": ncmnearEQPTELBLooped,
       "ncmnearEQPTELBLoopedCleared": ncmnearEQPTELBLoopedCleared,
       "ncmnearEQPTRLBLooped": ncmnearEQPTRLBLooped,
       "ncmnearEQPTRLBLoopedCleared": ncmnearEQPTRLBLoopedCleared,
       "ncmnearEQPTLOS": ncmnearEQPTLOS,
       "ncmnearEQPTLOSCleared": ncmnearEQPTLOSCleared,
       "ncmnearEQPTRAI": ncmnearEQPTRAI,
       "ncmnearEQPTRAICleared": ncmnearEQPTRAICleared,
       "ncmnearEQPTLOF": ncmnearEQPTLOF,
       "ncmnearEQPTLOFCleared": ncmnearEQPTLOFCleared,
       "ncmnearEQPTAIS": ncmnearEQPTAIS,
       "ncmnearEQPTAISCleared": ncmnearEQPTAISCleared,
       "ncmnearEQPTTSA": ncmnearEQPTTSA,
       "ncmnearEQPTTSACleared": ncmnearEQPTTSACleared,
       "ncmnearEQPTLowDensity": ncmnearEQPTLowDensity,
       "ncmnearEQPTLowDensityCleared": ncmnearEQPTLowDensityCleared,
       "ncmfarBERexceeded": ncmfarBERexceeded,
       "ncmfarBERexceededCleared": ncmfarBERexceededCleared,
       "ncmfarESLexceeded": ncmfarESLexceeded,
       "ncmfarESLexceededCleared": ncmfarESLexceededCleared,
       "ncmfarESexceeded": ncmfarESexceeded,
       "ncmfarESexceededCleared": ncmfarESexceededCleared,
       "ncmfarUASexceeded": ncmfarUASexceeded,
       "ncmfarUASexceededCleared": ncmfarUASexceededCleared,
       "ncmfarLELBlooped": ncmfarLELBlooped,
       "ncmfarLELBloopedCleared": ncmfarLELBloopedCleared,
       "ncmfarPRLBlooped": ncmfarPRLBlooped,
       "ncmfarPRLBloopedCleared": ncmfarPRLBloopedCleared,
       "ncmfarLOS": ncmfarLOS,
       "ncmfarLOSCleared": ncmfarLOSCleared,
       "ncmfarRAI": ncmfarRAI,
       "ncmfarRAICleared": ncmfarRAICleared,
       "ncmfarLOF": ncmfarLOF,
       "ncmfarLOFCleared": ncmfarLOFCleared,
       "ncmfarAIS": ncmfarAIS,
       "ncmfarAISCleared": ncmfarAISCleared,
       "ncmfarTestSIG": ncmfarTestSIG,
       "ncmfarTestSIGCleared": ncmfarTestSIGCleared,
       "ncmfarCSULossExtClk": ncmfarCSULossExtClk,
       "ncmfarCSULossExtClkCleared": ncmfarCSULossExtClkCleared,
       "ncmFarEQPTBERExceeded": ncmFarEQPTBERExceeded,
       "ncmFarEQPTBERExceededCleared": ncmFarEQPTBERExceededCleared,
       "ncmFarEQPTESLExceededCleared": ncmFarEQPTESLExceededCleared,
       "ncmFarEQPTESExceeded": ncmFarEQPTESExceeded,
       "ncmFarEQPTESExceededCleared": ncmFarEQPTESExceededCleared,
       "ncmFarEQPTUASExceeded": ncmFarEQPTUASExceeded,
       "ncmFarEQPTUASExceededCleared": ncmFarEQPTUASExceededCleared,
       "ncmFarEQPTELBLooped": ncmFarEQPTELBLooped,
       "ncmFarEQPTELBLoopedCleared": ncmFarEQPTELBLoopedCleared,
       "ncmFarEQPTRLBLooped": ncmFarEQPTRLBLooped,
       "ncmFarEQPTRLBLoopedCleared": ncmFarEQPTRLBLoopedCleared,
       "ncmFarEQPTLOS": ncmFarEQPTLOS,
       "ncmFarEQPTLOSCleared": ncmFarEQPTLOSCleared,
       "ncmFarEQPTRAI": ncmFarEQPTRAI,
       "ncmFarEQPTRAICleared": ncmFarEQPTRAICleared,
       "ncmFarEQPTLOF": ncmFarEQPTLOF,
       "ncmFarEQPTLOFCleared": ncmFarEQPTLOFCleared,
       "ncmFarEQPTAIS": ncmFarEQPTAIS,
       "ncmFarEQPTAISCleared": ncmFarEQPTAISCleared,
       "ncmFarEQPTTSA": ncmFarEQPTTSA,
       "ncmFarEQPTTSACleared": ncmFarEQPTTSACleared,
       "ncmFarEQPTLowDensity": ncmFarEQPTLowDensity,
       "ncmFarEQPTLowDensityCleared": ncmFarEQPTLowDensityCleared,
       "ncmnearNewPlug": ncmnearNewPlug,
       "ncmnearPlugAbsent": ncmnearPlugAbsent,
       "ncmnearPlugPresent": ncmnearPlugPresent,
       "ncmtiuDualClksPresent": ncmtiuDualClksPresent,
       "ncmtiuDualClksPresentCleared": ncmtiuDualClksPresentCleared,
       "ncmtiuNoClksPresent": ncmtiuNoClksPresent,
       "ncmtiuNoClksPresentCleared": ncmtiuNoClksPresentCleared,
       "ncmdiuPort1LOS": ncmdiuPort1LOS,
       "ncmdiuPort1LOSCleared": ncmdiuPort1LOSCleared,
       "ncmdiuPort2LOS": ncmdiuPort2LOS,
       "ncmdiuPort2LOSCleared": ncmdiuPort2LOSCleared,
       "ncmddsPortAbnormalStationCodeExceeded": ncmddsPortAbnormalStationCodeExceeded,
       "ncmddsPortAbnormalStationCodeExceededCleared": ncmddsPortAbnormalStationCodeExceededCleared,
       "ncmddsPortControlModeIdleExceeded": ncmddsPortControlModeIdleExceeded,
       "ncmddsPortControlModeIdleExceededCleared": ncmddsPortControlModeIdleExceededCleared,
       "ncmddsPortMuxOutSyncExceeded": ncmddsPortMuxOutSyncExceeded,
       "ncmddsPortMuxOutSyncExceededCleared": ncmddsPortMuxOutSyncExceededCleared,
       "ncmddsPortUnassignedMuxChannelExceeded": ncmddsPortUnassignedMuxChannelExceeded,
       "ncmddsPortUnassignedMuxChannelExceededCleared": ncmddsPortUnassignedMuxChannelExceededCleared,
       "ncmddsPortMJUAlertExceeded": ncmddsPortMJUAlertExceeded,
       "ncmddsPortMJUAlertExceededCleared": ncmddsPortMJUAlertExceededCleared,
       "ncmddsPortTestCodeExceeded": ncmddsPortTestCodeExceeded,
       "ncmddsPortTestCodeExceededCleared": ncmddsPortTestCodeExceededCleared,
       "ncmddsPortTestAlertExceeded": ncmddsPortTestAlertExceeded,
       "ncmddsPortTestAlertExceededCleared": ncmddsPortTestAlertExceededCleared,
       "ncmddsPortBlockExceeded": ncmddsPortBlockExceeded,
       "ncmddsPortBlockExceededCleared": ncmddsPortBlockExceededCleared,
       "ncmddsPortReleaseExceeded": ncmddsPortReleaseExceeded,
       "ncmddsPortReleaseExceededCleared": ncmddsPortReleaseExceededCleared,
       "ncmddsPortLoop": ncmddsPortLoop,
       "ncmddsPortLoopCleared": ncmddsPortLoopCleared,
       "ncmddsPortncmFarLooped": ncmddsPortncmFarLooped,
       "ncmddsPortncmFarLoopCleared": ncmddsPortncmFarLoopCleared,
       "ncmddsPortTestSignal": ncmddsPortTestSignal,
       "ncmddsPortTestSignalCleared": ncmddsPortTestSignalCleared,
       "ncmddsPort2AbnormalStationCodeExceeded": ncmddsPort2AbnormalStationCodeExceeded,
       "ncmddsPort2AbnormalStationCodeExceededCleared": ncmddsPort2AbnormalStationCodeExceededCleared,
       "ncmddsPort2ControlModeIdleExceeded": ncmddsPort2ControlModeIdleExceeded,
       "ncmddsPort2ControlModeIdleExceededCleared": ncmddsPort2ControlModeIdleExceededCleared,
       "ncmddsPort2MuxOutSyncExceeded": ncmddsPort2MuxOutSyncExceeded,
       "ncmddsPort2MuxOutSyncExceededCleared": ncmddsPort2MuxOutSyncExceededCleared,
       "ncmddsPort2UnassignedMuxChannelExceeded": ncmddsPort2UnassignedMuxChannelExceeded,
       "ncmddsPort2UnassignedMuxChannelExceededCleared": ncmddsPort2UnassignedMuxChannelExceededCleared,
       "ncmddsPort2MJUAlertExceeded": ncmddsPort2MJUAlertExceeded,
       "ncmddsPort2MJUAlertExceededCleared": ncmddsPort2MJUAlertExceededCleared,
       "ncmddsPort2TestCodeExceeded": ncmddsPort2TestCodeExceeded,
       "ncmddsPort2TestCodeExceededCleared": ncmddsPort2TestCodeExceededCleared,
       "ncmddsPort2TestAlertExceeded": ncmddsPort2TestAlertExceeded,
       "ncmddsPort2TestAlertExceededCleared": ncmddsPort2TestAlertExceededCleared,
       "ncmddsPort2BlockExceeded": ncmddsPort2BlockExceeded,
       "ncmddsPort2BlockExceededCleared": ncmddsPort2BlockExceededCleared,
       "ncmddsPort2ReleaseExceeded": ncmddsPort2ReleaseExceeded,
       "ncmddsPort2ReleaseExceededCleared": ncmddsPort2ReleaseExceededCleared,
       "ncmddsPort2Loop": ncmddsPort2Loop,
       "ncmddsPort2LoopCleared": ncmddsPort2LoopCleared,
       "ncmddsPort2ncmFarLooped": ncmddsPort2ncmFarLooped,
       "ncmddsPort2ncmFarLoopCleared": ncmddsPort2ncmFarLoopCleared,
       "ncmddsPort2TestSignal": ncmddsPort2TestSignal,
       "ncmddsPort2TestSignalCleared": ncmddsPort2TestSignalCleared,
       "ncmdbuAlarm": ncmdbuAlarm,
       "ncmdbuAlarmClear": ncmdbuAlarmClear,
       "ncmdbuBackupConnection": ncmdbuBackupConnection,
       "ncmdiuPortALLOnes": ncmdiuPortALLOnes,
       "ncmdiuPortALLOnesCleared": ncmdiuPortALLOnesCleared,
       "ncmdbuPortASCOn": ncmdbuPortASCOn,
       "ncmdbuPortASCOff": ncmdbuPortASCOff,
       "ncmdbuPortLOFOn": ncmdbuPortLOFOn,
       "ncmdbuPortLOFOff": ncmdbuPortLOFOff,
       "ncmdbuPortCDOn": ncmdbuPortCDOn,
       "ncmdbuPortCDOff": ncmdbuPortCDOff,
       "ncmdbuPortUSEROn": ncmdbuPortUSEROn,
       "ncmdbuPortUSEROff": ncmdbuPortUSEROff,
       "ncmdbuPortYELAlarmOn": ncmdbuPortYELAlarmOn,
       "ncmdbuPortYELAlarmOff": ncmdbuPortYELAlarmOff,
       "ncmdbuPortNetworkBEROn": ncmdbuPortNetworkBEROn,
       "ncmdbuPortNetworkBEROff": ncmdbuPortNetworkBEROff,
       "ncmdbuPortAllOnesAlarm": ncmdbuPortAllOnesAlarm,
       "ncmdbuPortAllOnesAlarmCleared": ncmdbuPortAllOnesAlarmCleared,
       "ncmdbuPortLOSOn": ncmdbuPortLOSOn,
       "ncmdbuPortLOSOff": ncmdbuPortLOSOff,
       "ncmPlugPresent": ncmPlugPresent,
       "ncmPlugAbsent": ncmPlugAbsent,
       "ncmFEPlugPresent": ncmFEPlugPresent,
       "ncmFEPlugAbsent": ncmFEPlugAbsent,
       "ncmalarmBufferFull": ncmalarmBufferFull,
       "ncmnearAPowerSupply": ncmnearAPowerSupply,
       "ncmnearAPowerSupplyCleared": ncmnearAPowerSupplyCleared,
       "ncmfarAPowerSupply": ncmfarAPowerSupply,
       "ncmfarAPowerSupplyCleared": ncmfarAPowerSupplyCleared,
       "ncmnearBPowerSupply": ncmnearBPowerSupply,
       "ncmnearBPowerSupplyCleared": ncmnearBPowerSupplyCleared,
       "ncmfarBPowerSupply": ncmfarBPowerSupply,
       "ncmfarBPowerSupplyCleared": ncmfarBPowerSupplyCleared,
       "powerUPLoopExists": powerUPLoopExists,
       "postNETFailure": postNETFailure,
       "postEQPTFailure": postEQPTFailure,
       "lowBattery": lowBattery,
       "ncminvDownload": ncminvDownload,
       "ncmActive": ncmActive,
       "ncmStandBy": ncmStandBy,
       "ncmCircuitErr": ncmCircuitErr,
       "ncmFanShelfFail": ncmFanShelfFail,
       "ncmFanShelfAlarmCleared": ncmFanShelfAlarmCleared,
       "ncmapsAlarmSet": ncmapsAlarmSet,
       "ncmapsAlarmClear": ncmapsAlarmClear,
       "ncmapsSwitchedSet": ncmapsSwitchedSet,
       "ncmapsSwitchedClear": ncmapsSwitchedClear,
       "ncmipOverT1LinkDown": ncmipOverT1LinkDown,
       "ncmipOverT1LinkUp": ncmipOverT1LinkUp,
       "ncmnearquadCSUPowerUP": ncmnearquadCSUPowerUP,
       "ncmfarCSUPowerUP": ncmfarCSUPowerUP,
       "ncmnearQuadAPowerSupply": ncmnearQuadAPowerSupply,
       "ncmnearQuadAPowerSupplyCleared": ncmnearQuadAPowerSupplyCleared,
       "ncmnearQuadBPowerSupply": ncmnearQuadBPowerSupply,
       "ncmnearQuadBPowerSupplyCleared": ncmnearQuadBPowerSupplyCleared,
       "ncmnearAceLOS": ncmnearAceLOS,
       "ncmnearAceLOF": ncmnearAceLOF,
       "ncmnearRemoteAI": ncmnearRemoteAI,
       "ncmnearLOMFalignm": ncmnearLOMFalignm,
       "ncmnearRemoteMAS": ncmnearRemoteMAS,
       "ncmnearIAS": ncmnearIAS,
       "ncmnearFAS": ncmnearFAS,
       "ncmnearFASeXceeded": ncmnearFASeXceeded,
       "ncmnearCVCeXceeded": ncmnearCVCeXceeded,
       "ncmnearCRCeXceeded": ncmnearCRCeXceeded,
       "ncmnearFECeXceeded": ncmnearFECeXceeded,
       "ncmnearCarrier": ncmnearCarrier,
       "ncmnearDwnLdCode": ncmnearDwnLdCode,
       "ncmnearLActCLK": ncmnearLActCLK,
       "ncmnearLstdbyCLK": ncmnearLstdbyCLK,
       "ncmnearRefTBUS": ncmnearRefTBUS,
       "ncmnearTBUS": ncmnearTBUS,
       "ncmnearLLB": ncmnearLLB,
       "ncmnearELB": ncmnearELB,
       "ncmnearPLB": ncmnearPLB,
       "ncmnearRLB": ncmnearRLB,
       "ncmalmSESExceeded": ncmalmSESExceeded,
       "ncmalmUASExceeded": ncmalmUASExceeded,
       "ncmalmBERExceeded": ncmalmBERExceeded,
       "ncmalmQ931LinkUP": ncmalmQ931LinkUP,
       "ncmalmQ931LinkDown": ncmalmQ931LinkDown,
       "ncmalmPortDown": ncmalmPortDown,
       "ncmalmCGA": ncmalmCGA,
       "ncmalmLOFThresholdExceeded": ncmalmLOFThresholdExceeded,
       "ncmalmLOSThresholdExceeded": ncmalmLOSThresholdExceeded,
       "ncmalmRAIThresholdExceeded": ncmalmRAIThresholdExceeded,
       "ncmalmAISThresholdExceeded": ncmalmAISThresholdExceeded,
       "ncmalmBPVThresholdExceeded": ncmalmBPVThresholdExceeded,
       "ncmalmES15MINThresholdExceeded": ncmalmES15MINThresholdExceeded,
       "ncmalmES24HRThresholdExceeded": ncmalmES24HRThresholdExceeded,
       "ncmalmSES15MINThresholdExceeded": ncmalmSES15MINThresholdExceeded,
       "ncmalmSES24HRThresholdExceeded": ncmalmSES24HRThresholdExceeded,
       "ncmalmCVP15MINThresholdExceeded": ncmalmCVP15MINThresholdExceeded,
       "ncmalmCVP24HRThresholdExceeded": ncmalmCVP24HRThresholdExceeded,
       "ncmalmCVL15MINThresholdExceeded": ncmalmCVL15MINThresholdExceeded,
       "ncmalmCVL24HRThresholdExceeded": ncmalmCVL24HRThresholdExceeded,
       "ncmalmESL15MINThresholdExceeded": ncmalmESL15MINThresholdExceeded,
       "ncmalmESL24HRThresholdExceeded": ncmalmESL24HRThresholdExceeded,
       "ncmalmSESL15MINThresholdExceeded": ncmalmSESL15MINThresholdExceeded,
       "ncmalmSESL24HRThresholdExceeded": ncmalmSESL24HRThresholdExceeded,
       "ncmalmUASP15MINThresholdExceeded": ncmalmUASP15MINThresholdExceeded,
       "ncmalmUASP24HRThresholdExceeded": ncmalmUASP24HRThresholdExceeded,
       "ncmalmBBERThresholdExceeded": ncmalmBBERThresholdExceeded,
       "ncmalmDataPortRTS": ncmalmDataPortRTS,
       "ncmalmDataPortDTR": ncmalmDataPortDTR,
       "ncmalmImxDTEport": ncmalmImxDTEport,
       "ncmalmImxDTEportReady": ncmalmImxDTEportReady,
       "ncmalmImxLocOsc": ncmalmImxLocOsc,
       "ncmalmImxLocOscClear": ncmalmImxLocOscClear,
       "ncmalmLn1BndwidClear": ncmalmLn1BndwidClear,
       "ncmimuxLn1Bndwid": ncmimuxLn1Bndwid,
       "ncmimuxLn2BndwidClear": ncmimuxLn2BndwidClear,
       "ncmimuxLn2Bndwid": ncmimuxLn2Bndwid,
       "ncmimuxLn3BndwidClear": ncmimuxLn3BndwidClear,
       "ncmimuxLn3Bndwid": ncmimuxLn3Bndwid,
       "ncmimuxLn4BndwidClear": ncmimuxLn4BndwidClear,
       "ncmimuxLn4Bndwid": ncmimuxLn4Bndwid,
       "ncmimuxLn5BndwidClear": ncmimuxLn5BndwidClear,
       "ncmimuxLn5Bndwid": ncmimuxLn5Bndwid,
       "ncmimuxLn6BndwidClear": ncmimuxLn6BndwidClear,
       "ncmimuxLn6Bndwid": ncmimuxLn6Bndwid,
       "ncmimuxLn7BndwidClear": ncmimuxLn7BndwidClear,
       "ncmimuxLn7Bndwid": ncmimuxLn7Bndwid,
       "ncmimuxLn8BndwidClear": ncmimuxLn8BndwidClear,
       "ncmimuxLn8Bndwid": ncmimuxLn8Bndwid,
       "ncmimuxELBLoopbackActivated": ncmimuxELBLoopbackActivated,
       "ncmimuxELBLoopbackDeActivated": ncmimuxELBLoopbackDeActivated,
       "ncmimuxPLBLoopbackActivated": ncmimuxPLBLoopbackActivated,
       "ncmimuxPLBLoopbackDeActivated": ncmimuxPLBLoopbackDeActivated,
       "ncmimuxILBLoopbackActivated": ncmimuxILBLoopbackActivated,
       "ncmimuxILBLoopbackDeActivated": ncmimuxILBLoopbackDeActivated,
       "ncmPriIllegalConfiguration": ncmPriIllegalConfiguration,
       "ncmPriL2Up": ncmPriL2Up,
       "ncmPriL2Down": ncmPriL2Down,
       "ncmPriDISCReceived": ncmPriDISCReceived,
       "ncmPriDISCSent": ncmPriDISCSent,
       "ncmPriL2IllegalMessageReceived": ncmPriL2IllegalMessageReceived,
       "ncmPriUnknownAcpCommand": ncmPriUnknownAcpCommand,
       "ncmPriIllegalAcpCommand": ncmPriIllegalAcpCommand,
       "ncmPriL3Up": ncmPriL3Up,
       "ncmPriL3Down": ncmPriL3Down,
       "ncmPriDChannelBackupSuccess": ncmPriDChannelBackupSuccess,
       "ncmPriDChannelBackupFailure": ncmPriDChannelBackupFailure,
       "ncmPriL3IllegalMessageReceived": ncmPriL3IllegalMessageReceived,
       "ncmPriL3SwitchError": ncmPriL3SwitchError,
       "ncmPriCallSetUp": ncmPriCallSetUp,
       "ncmPriCallSetUpFailure": ncmPriCallSetUpFailure,
       "ncmPriCallTakeDownSuccess": ncmPriCallTakeDownSuccess,
       "ncmPriCallTakeDownFailure": ncmPriCallTakeDownFailure,
       "ncmPriTestCallFailure": ncmPriTestCallFailure,
       "ncmPriSecurityIncomingCallReject": ncmPriSecurityIncomingCallReject,
       "ncmPriSecurityOutgoingCallReject": ncmPriSecurityOutgoingCallReject,
       "ncmPriStackUp": ncmPriStackUp,
       "ncmPriStackDown": ncmPriStackDown,
       "ncmPriApplicationIllegalMessage": ncmPriApplicationIllegalMessage,
       "ncmPriCircuitBuilderCallReject": ncmPriCircuitBuilderCallReject,
       "ncmPriStackActivationFailure": ncmPriStackActivationFailure,
       "ncmPriCircuitManagerCallRejectTakeDown": ncmPriCircuitManagerCallRejectTakeDown,
       "ncmDS3LosOn": ncmDS3LosOn,
       "ncmDS3LosOff": ncmDS3LosOff,
       "ncmDS3OOFOn": ncmDS3OOFOn,
       "ncmDS3OOFOff": ncmDS3OOFOff,
       "ncmDS3AISOn": ncmDS3AISOn,
       "ncmDS3AISOff": ncmDS3AISOff,
       "ncmDS3IdleOn": ncmDS3IdleOn,
       "ncmDS3IdleOff": ncmDS3IdleOff,
       "ncmDS3YellowOn": ncmDS3YellowOn,
       "ncmDS3YellowOff": ncmDS3YellowOff,
       "ncmDS3LOSFailureOn": ncmDS3LOSFailureOn,
       "ncmDS3LOSFailureOff": ncmDS3LOSFailureOff,
       "ncmDS3OutOfFrameFailureOn": ncmDS3OutOfFrameFailureOn,
       "ncmDS3OutOfFrameFailureOff": ncmDS3OutOfFrameFailureOff,
       "ncmDS3AISFailureOn": ncmDS3AISFailureOn,
       "ncmDS3AISFailureOff": ncmDS3AISFailureOff,
       "ncmDS3ReceiveFIFOOverflowOn": ncmDS3ReceiveFIFOOverflowOn,
       "ncmDS3ReceiveFIFOOverflowOff": ncmDS3ReceiveFIFOOverflowOff,
       "ncmDS3TransmitFIFOOverflowOn": ncmDS3TransmitFIFOOverflowOn,
       "ncmDS3TransmitFIFOOverflowOff": ncmDS3TransmitFIFOOverflowOff,
       "ncmDS3LossTransmitClockOn": ncmDS3LossTransmitClockOn,
       "ncmDS3LossTransmitClockOff": ncmDS3LossTransmitClockOff,
       "ncmDS3ncmFarEndBlockErrorOn": ncmDS3ncmFarEndBlockErrorOn,
       "ncmDS3ncmFarEndBlockErrorOff": ncmDS3ncmFarEndBlockErrorOff,
       "ncmDS3QRTLCVCrossThreshold": ncmDS3QRTLCVCrossThreshold,
       "ncmDS3QRTLESCrossThreshold": ncmDS3QRTLESCrossThreshold,
       "ncmDS3QRTLSESCrossThreshold": ncmDS3QRTLSESCrossThreshold,
       "ncmDS3QRTPCVCrossThreshold": ncmDS3QRTPCVCrossThreshold,
       "ncmDS3QRTPESCrossThreshold": ncmDS3QRTPESCrossThreshold,
       "ncmDS3QRTPSESCrossThreshold": ncmDS3QRTPSESCrossThreshold,
       "ncmDS3QRTSEFSCrossThreshold": ncmDS3QRTSEFSCrossThreshold,
       "ncmDS3QRTAISSCrossThreshold": ncmDS3QRTAISSCrossThreshold,
       "ncmDS3QRTUASCrossThreshold": ncmDS3QRTUASCrossThreshold,
       "ncmDS3QRTCCVCrossThreshold": ncmDS3QRTCCVCrossThreshold,
       "ncmDS3QRTCESCrossThreshold": ncmDS3QRTCESCrossThreshold,
       "ncmDS3QRTCSESCrossThreshold": ncmDS3QRTCSESCrossThreshold,
       "ncmDS3QRTLOSSCrossThreshold": ncmDS3QRTLOSSCrossThreshold,
       "ncmDS3QRTLOFCCrossThreshold": ncmDS3QRTLOFCCrossThreshold,
       "ncmDS3ncmFarEndQRTCCVCrossThreshold": ncmDS3ncmFarEndQRTCCVCrossThreshold,
       "ncmDS3ncmFarEndQRTCESCrossThreshold": ncmDS3ncmFarEndQRTCESCrossThreshold,
       "ncmDS3ncmFarEndQRTCSESCrossThreshold": ncmDS3ncmFarEndQRTCSESCrossThreshold,
       "ncmDS3ncmFarEndQRTUASCrossThreshold": ncmDS3ncmFarEndQRTUASCrossThreshold,
       "ncmDS3DayLCVCrossThreshold": ncmDS3DayLCVCrossThreshold,
       "ncmDS3DayLESCrossThreshold": ncmDS3DayLESCrossThreshold,
       "ncmDS3DayLSESCrossThreshold": ncmDS3DayLSESCrossThreshold,
       "ncmDS3DayPCVCrossThreshold": ncmDS3DayPCVCrossThreshold,
       "ncmDS3DayPESCrossThreshold": ncmDS3DayPESCrossThreshold,
       "ncmDS3DayPSESCrossThreshold": ncmDS3DayPSESCrossThreshold,
       "ncmDS3DayPSEFSCrossThreshold": ncmDS3DayPSEFSCrossThreshold,
       "ncmDS3DayAISSCrossThreshold": ncmDS3DayAISSCrossThreshold,
       "ncmDS3DayUASCrossThreshold": ncmDS3DayUASCrossThreshold,
       "ncmDS3DayCCVCrossThreshold": ncmDS3DayCCVCrossThreshold,
       "ncmDS3DayCESCrossThreshold": ncmDS3DayCESCrossThreshold,
       "ncmDS3DayCSESCrossThreshold": ncmDS3DayCSESCrossThreshold,
       "ncmDS3DayLOSSCrossThreshold": ncmDS3DayLOSSCrossThreshold,
       "ncmDS3DayLOFCCrossThreshold": ncmDS3DayLOFCCrossThreshold,
       "ncmDS3ncmFarEndDayCCVCrossThreshold": ncmDS3ncmFarEndDayCCVCrossThreshold,
       "ncmDS3ncmFarEndDayCESCrossThreshold": ncmDS3ncmFarEndDayCESCrossThreshold,
       "ncmDS3ncmFarEndDayCSESCrossThreshold": ncmDS3ncmFarEndDayCSESCrossThreshold,
       "ncmDS3ncmFarEndDayUASCrossThreshold": ncmDS3ncmFarEndDayUASCrossThreshold,
       "ncmDS3IPCChannelFailureOn": ncmDS3IPCChannelFailureOn,
       "ncmDS3IPCChannelFailureOff": ncmDS3IPCChannelFailureOff,
       "ncmDS3SARCardMajorAlarmOn": ncmDS3SARCardMajorAlarmOn,
       "ncmDS3SARCardMajorAlarmOff": ncmDS3SARCardMajorAlarmOff,
       "ncmDS3DxiHeartBeatFailureOn": ncmDS3DxiHeartBeatFailureOn,
       "ncmDS3DxiHeartBeatFailureOff": ncmDS3DxiHeartBeatFailureOff,
       "ncmDS3HSSIPortUp": ncmDS3HSSIPortUp,
       "ncmDS3HSSIPortDown": ncmDS3HSSIPortDown,
       "ncmDS3FEACEquipmentFailureSAOn": ncmDS3FEACEquipmentFailureSAOn,
       "ncmDS3FEACLosOn": ncmDS3FEACLosOn,
       "ncmDS3FEACOOFOn": ncmDS3FEACOOFOn,
       "ncmDS3FEACAISOn": ncmDS3FEACAISOn,
       "ncmDS3FEACIDLEOn": ncmDS3FEACIDLEOn,
       "ncmDS3FEACEqptFailureNSAOn": ncmDS3FEACEqptFailureNSAOn,
       "ncmDS3FEACCommonEqptFailureOn": ncmDS3FEACCommonEqptFailureOn,
       "ncmDS3FEACMultiDs1LosHBEROn": ncmDS3FEACMultiDs1LosHBEROn,
       "ncmDS3FEACDs1EqptFailureOn": ncmDS3FEACDs1EqptFailureOn,
       "ncmDS3FEACSingleDs1LosHBEROn": ncmDS3FEACSingleDs1LosHBEROn,
       "ncmDS3FEACDs1EqptFailureNSAOn": ncmDS3FEACDs1EqptFailureNSAOn,
       "ncmDS3FEACLineLoopActivationOn": ncmDS3FEACLineLoopActivationOn,
       "ncmDS3FEACLineLoopDeActivationOn": ncmDS3FEACLineLoopDeActivationOn,
       "ncmDS3FEACLineOn": ncmDS3FEACLineOn,
       "ncmDS3FEACEquipmentFailureSAOff": ncmDS3FEACEquipmentFailureSAOff,
       "ncmDS3FEACLosOff": ncmDS3FEACLosOff,
       "ncmDS3FEACOOFOff": ncmDS3FEACOOFOff,
       "ncmDS3FEACAISOff": ncmDS3FEACAISOff,
       "ncmDS3FEACIDLEOff": ncmDS3FEACIDLEOff,
       "ncmDS3FEACEqptFailureNSAOff": ncmDS3FEACEqptFailureNSAOff,
       "ncmDS3FEACCommonEqptFailureOff": ncmDS3FEACCommonEqptFailureOff,
       "ncmDS3FEACMultiDs1LosHBEROff": ncmDS3FEACMultiDs1LosHBEROff,
       "ncmDS3FEACDs1EqptFailureOff": ncmDS3FEACDs1EqptFailureOff,
       "ncmDS3FEACSingleDs1LosHBEROff": ncmDS3FEACSingleDs1LosHBEROff,
       "ncmDS3FEACDs1EqptFailureNSAOff": ncmDS3FEACDs1EqptFailureNSAOff,
       "ncmDS3FEACLineLoopActivationOff": ncmDS3FEACLineLoopActivationOff,
       "ncmDS3FEACLineLoopDeActivationOff": ncmDS3FEACLineLoopDeActivationOff,
       "ncmDS3FEACLineOff": ncmDS3FEACLineOff,
       "ncmDS3DataRateSetFailure": ncmDS3DataRateSetFailure,
       "ncmDS3TransmitFEACLineLoopActivationOn": ncmDS3TransmitFEACLineLoopActivationOn,
       "ncmDS3TransmitFEACLineLoopActivationOff": ncmDS3TransmitFEACLineLoopActivationOff,
       "ncmDS3TransmitFEACLineLoopDeActivationOn": ncmDS3TransmitFEACLineLoopDeActivationOn,
       "ncmDS3TransmitFEACLineLoopDeActivationOff": ncmDS3TransmitFEACLineLoopDeActivationOff,
       "ncmDS3TransmitYellowAlarmOn": ncmDS3TransmitYellowAlarmOn,
       "ncmDS3TransmitYellowAlarmOff": ncmDS3TransmitYellowAlarmOff,
       "ncmDS3TransmitAISAlarmOn": ncmDS3TransmitAISAlarmOn,
       "ncmDS3TransmitAISAlarmOff": ncmDS3TransmitAISAlarmOff,
       "ncmDS3TransmitIdleAlarmOn": ncmDS3TransmitIdleAlarmOn,
       "ncmDS3TransmitIdleAlarmOff": ncmDS3TransmitIdleAlarmOff,
       "ncmDS3TransmitFEBEAlarmOn": ncmDS3TransmitFEBEAlarmOn,
       "ncmDS3TransmitFEBEAlarmOff": ncmDS3TransmitFEBEAlarmOff,
       "ncmDS3TransmitFEACLosOn": ncmDS3TransmitFEACLosOn,
       "ncmDS3TransmitFEACLosOff": ncmDS3TransmitFEACLosOff,
       "ncmDS3TransmitFEACOOFOn": ncmDS3TransmitFEACOOFOn,
       "ncmDS3TransmitFEACOOFOff": ncmDS3TransmitFEACOOFOff,
       "ncmDS3TransmitFEACAISOn": ncmDS3TransmitFEACAISOn,
       "ncmDS3TransmitFEACAISOff": ncmDS3TransmitFEACAISOff,
       "ncmDS3TransmitFEACIdleOn": ncmDS3TransmitFEACIdleOn,
       "ncmDS3TransmitFEACIdleOff": ncmDS3TransmitFEACIdleOff,
       "ncmDS3TransmitFEACEqptFailureNSAOn": ncmDS3TransmitFEACEqptFailureNSAOn,
       "ncmDS3TransmitFEACEqptFailureNSAOff": ncmDS3TransmitFEACEqptFailureNSAOff,
       "ncmDS3TransmitFEACCommonEqptFailureNSAOn": ncmDS3TransmitFEACCommonEqptFailureNSAOn,
       "ncmDS3TransmitFEACCommonEqptFailureNSAOff": ncmDS3TransmitFEACCommonEqptFailureNSAOff,
       "ncmDS3TransmitFEACLineOn": ncmDS3TransmitFEACLineOn,
       "ncmDS3TransmitFEACLineOff": ncmDS3TransmitFEACLineOff,
       "ncmDS3TransmitFEACNoAlarm": ncmDS3TransmitFEACNoAlarm,
       "ncmDS3UserLocalLoopbackOn": ncmDS3UserLocalLoopbackOn,
       "ncmDS3UserLocalLoopbackOff": ncmDS3UserLocalLoopbackOff,
       "ncmDS3UserPayloadLoopbackOn": ncmDS3UserPayloadLoopbackOn,
       "ncmDS3UserPayloadLoopbackOff": ncmDS3UserPayloadLoopbackOff,
       "ncmDS3UserEquipmentLoopbackOn": ncmDS3UserEquipmentLoopbackOn,
       "ncmDS3UserEquipmentLoopbackOff": ncmDS3UserEquipmentLoopbackOff,
       "ncmDS3UserNoLoopbackOn": ncmDS3UserNoLoopbackOn,
       "ncmDS3UserNoLoopbackOff": ncmDS3UserNoLoopbackOff,
       "ncmDS3HSSILocalLoopbackOn": ncmDS3HSSILocalLoopbackOn,
       "ncmDS3HSSILocalLoopbackOff": ncmDS3HSSILocalLoopbackOff,
       "ncmDS3HSSIPayloadLoopbackOn": ncmDS3HSSIPayloadLoopbackOn,
       "ncmDS3HSSIPayloadLoopbackOff": ncmDS3HSSIPayloadLoopbackOff,
       "ncmDS3HSSIEquipmentLoopbackOn": ncmDS3HSSIEquipmentLoopbackOn,
       "ncmDS3HSSIEquipmentLoopbackOff": ncmDS3HSSIEquipmentLoopbackOff,
       "ncmDS3HSSINoLoopbackOn": ncmDS3HSSINoLoopbackOn,
       "ncmDS3HSSINoLoopbackOff": ncmDS3HSSINoLoopbackOff,
       "ncmDS3ncmFarEndLocalLoopbackOn": ncmDS3ncmFarEndLocalLoopbackOn,
       "ncmDS3ncmFarEndLocalLoopbackOff": ncmDS3ncmFarEndLocalLoopbackOff,
       "ncmDS3ncmFarEndPayloadLoopbackOn": ncmDS3ncmFarEndPayloadLoopbackOn,
       "ncmDS3ncmFarEndPayloadLoopbackOff": ncmDS3ncmFarEndPayloadLoopbackOff,
       "ncmDS3ncmFarEndEqptLoopbackOn": ncmDS3ncmFarEndEqptLoopbackOn,
       "ncmDS3ncmFarEndEqptLoopbackOff": ncmDS3ncmFarEndEqptLoopbackOff,
       "ncmDS3ncmFarEndNoLoopbackOn": ncmDS3ncmFarEndNoLoopbackOn,
       "ncmDS3ncmFarEndNoLoopbackOff": ncmDS3ncmFarEndNoLoopbackOff,
       "ncmDS3ncmFarEndPayloadLoopbackOnFailure": ncmDS3ncmFarEndPayloadLoopbackOnFailure,
       "ncmDS3ncmFarEndPayloadLoopbackOffFailure": ncmDS3ncmFarEndPayloadLoopbackOffFailure,
       "ncmDS3UserEquipmentLoopbackOnPortTwo": ncmDS3UserEquipmentLoopbackOnPortTwo,
       "ncmDS3UserEquipmentLoopbackOFFPortTwo": ncmDS3UserEquipmentLoopbackOFFPortTwo,
       "ncmDS3HssiEquipmentLoopbackOnPortTwo": ncmDS3HssiEquipmentLoopbackOnPortTwo,
       "ncmDS3HssiEquipmentLoopbackOFFPortTwo": ncmDS3HssiEquipmentLoopbackOFFPortTwo,
       "ncmDS3FarEndEquipmentLoopbackONPortTwo": ncmDS3FarEndEquipmentLoopbackONPortTwo,
       "ncmDS3FarEndEquipmentLoopbackOFFPortTwo": ncmDS3FarEndEquipmentLoopbackOFFPortTwo,
       "ncmDS3HssiPortUpPortTwo": ncmDS3HssiPortUpPortTwo,
       "ncmDS3HssiPortDownPortTwo": ncmDS3HssiPortDownPortTwo,
       "ncmDS3HssiPortOneRateChange": ncmDS3HssiPortOneRateChange,
       "ncmDS3HssiPortTwoRateChange": ncmDS3HssiPortTwoRateChange,
       "ncmDS3HssiPortOneRateChangeFarEnd": ncmDS3HssiPortOneRateChangeFarEnd,
       "ncmDS3HssiPortTwoRateChangeFarEnd": ncmDS3HssiPortTwoRateChangeFarEnd,
       "ncmDS3HssiLocalLoopbackOnDual": ncmDS3HssiLocalLoopbackOnDual,
       "ncmDS3HssiLocalLoopbackOffDual": ncmDS3HssiLocalLoopbackOffDual,
       "ncmDS3UserLineLoopbackOn": ncmDS3UserLineLoopbackOn,
       "ncmDS3UserLineLoopbackOff": ncmDS3UserLineLoopbackOff,
       "ncmT1LOS": ncmT1LOS,
       "ncmT1LOF": ncmT1LOF,
       "ncmT1AIS": ncmT1AIS,
       "ncmT1YEL": ncmT1YEL,
       "ncmT1OUT": ncmT1OUT,
       "ncmT1LineLoop": ncmT1LineLoop,
       "ncmT1LocalLoop": ncmT1LocalLoop,
       "ncmT1FarEndLoopback": ncmT1FarEndLoopback,
       "ncmActiveReferenceClockLOS": ncmActiveReferenceClockLOS,
       "ncmStandbyReferenceClockLOS": ncmStandbyReferenceClockLOS,
       "ncmBothReferenceClockLOS": ncmBothReferenceClockLOS,
       "ncmTimeBusLOS": ncmTimeBusLOS,
       "ncmT1In": ncmT1In,
       "ncmT1LineLoopbackOff": ncmT1LineLoopbackOff,
       "ncmT1LocalLoopbackOff": ncmT1LocalLoopbackOff,
       "ncmT1FarEndLoopbackOff": ncmT1FarEndLoopbackOff,
       "ncmnearAceLOSCleared": ncmnearAceLOSCleared,
       "ncmnearAceLOFCleared": ncmnearAceLOFCleared,
       "ncmnearRemoteAICleared": ncmnearRemoteAICleared,
       "ncmnearLOMFalignmCleared": ncmnearLOMFalignmCleared,
       "ncmnearRemoteMASCleared": ncmnearRemoteMASCleared,
       "ncmnearIASCleared": ncmnearIASCleared,
       "ncmnearFASCleared": ncmnearFASCleared,
       "ncmnearFASeXceededCleared": ncmnearFASeXceededCleared,
       "ncmnearCVCeXceededCleared": ncmnearCVCeXceededCleared,
       "ncmnearCRCeXceededCleared": ncmnearCRCeXceededCleared,
       "ncmnearFECeXceededCleared": ncmnearFECeXceededCleared,
       "ncmnearCarrierCleared": ncmnearCarrierCleared,
       "ncmnearDwnLdCodeCleared": ncmnearDwnLdCodeCleared,
       "ncmnearLActCLKCleared": ncmnearLActCLKCleared,
       "ncmnearLstdbyCLKCleared": ncmnearLstdbyCLKCleared,
       "ncmnearRefTBUSCleared": ncmnearRefTBUSCleared,
       "ncmnearTBUSCleared": ncmnearTBUSCleared,
       "ncmnearLLBCleared": ncmnearLLBCleared,
       "ncmnearELBCleared": ncmnearELBCleared,
       "ncmnearPLBCleared": ncmnearPLBCleared,
       "ncmnearRLBCleared": ncmnearRLBCleared,
       "ncmalmSESExceededCleared": ncmalmSESExceededCleared,
       "ncmalmUASExceededCleared": ncmalmUASExceededCleared,
       "ncmalmBERExceededCleared": ncmalmBERExceededCleared,
       "ncmalmPortDownCleared": ncmalmPortDownCleared,
       "ncmalmCGACleared": ncmalmCGACleared,
       "ncmalmLOFThresholdExceededCleared": ncmalmLOFThresholdExceededCleared,
       "ncmalmLOSThresholdExceededCleared": ncmalmLOSThresholdExceededCleared,
       "ncmalmRAIThresholdExceededCleared": ncmalmRAIThresholdExceededCleared,
       "ncmalmAISThresholdExceededCleared": ncmalmAISThresholdExceededCleared,
       "ncmalmBPVThresholdExceededCleared": ncmalmBPVThresholdExceededCleared,
       "ncmalmES15MINThresholdExceededCleared": ncmalmES15MINThresholdExceededCleared,
       "ncmalmES24HRThresholdExceededCleared": ncmalmES24HRThresholdExceededCleared,
       "ncmalmSES15MINThresholdExceededCleared": ncmalmSES15MINThresholdExceededCleared,
       "ncmalmSES24HRThresholdExceededCleared": ncmalmSES24HRThresholdExceededCleared,
       "ncmalmCVP15MINThresholdExceededCleared": ncmalmCVP15MINThresholdExceededCleared,
       "ncmalmCVP24HRThresholdExceededCleared": ncmalmCVP24HRThresholdExceededCleared,
       "ncmalmCVL15MINThresholdExceededCleared": ncmalmCVL15MINThresholdExceededCleared,
       "ncmalmCVL24HRThresholdExceededCleared": ncmalmCVL24HRThresholdExceededCleared,
       "ncmalmESL15MINThresholdExceededCleared": ncmalmESL15MINThresholdExceededCleared,
       "ncmalmESL24HRThresholdExceededCleared": ncmalmESL24HRThresholdExceededCleared,
       "ncmalmSESL15MINThresholdExceededCleared": ncmalmSESL15MINThresholdExceededCleared,
       "ncmalmSESL24HRThresholdExceededCleared": ncmalmSESL24HRThresholdExceededCleared,
       "ncmalmUASP15MINThresholdExceededCleared": ncmalmUASP15MINThresholdExceededCleared,
       "ncmalmUASP24HRThresholdExceededCleared": ncmalmUASP24HRThresholdExceededCleared,
       "ncmalmBBERThresholdExceededCleared": ncmalmBBERThresholdExceededCleared,
       "ncmalmDataPortRTSCleared": ncmalmDataPortRTSCleared,
       "ncmalmDataPortDTRCleared": ncmalmDataPortDTRCleared,
       "ncmAlarm": ncmAlarm,
       "ncmAlarmNodeAddr": ncmAlarmNodeAddr,
       "ncmAlarmShelf": ncmAlarmShelf,
       "ncmAlarmSlot": ncmAlarmSlot,
       "ncmAlarmPort": ncmAlarmPort,
       "ncmAlarmCard": ncmAlarmCard,
       "ncmAlarmTimestamp": ncmAlarmTimestamp,
       "ncmAlarmSeverity": ncmAlarmSeverity,
       "ncmAlarmInstance": ncmAlarmInstance,
       "ncmAlarmEquipId": ncmAlarmEquipId,
       "ncmAlarmObjectType": ncmAlarmObjectType,
       "ncmAlarmString": ncmAlarmString,
       "ncm-generic": ncm_generic,
       "ncm-dsu": ncm_dsu,
       "ncm-dbu": ncm_dbu,
       "ncm-dds": ncm_dds,
       "ncm-csu": ncm_csu,
       "ncm-idcsu": ncm_idcsu,
       "ncm-ddsu": ncm_ddsu,
       "ncm-sdiu": ncm_sdiu,
       "ncm-imux": ncm_imux,
       "ncm-isdn": ncm_isdn,
       "ncm-ds3": ncm_ds3,
       "ncm-m13": ncm_m13,
       "ncm-japisdn": ncm_japisdn}
)
