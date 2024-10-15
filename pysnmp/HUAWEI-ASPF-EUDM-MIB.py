# SNMP MIB module (HUAWEI-ASPF-EUDM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-ASPF-EUDM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:47 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(mplsVpnVrfName,) = mibBuilder.importSymbols(
    "MPLS-VPN-MIB",
    "mplsVpnVrfName")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hwASPFEudm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 6, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwASPF_ObjectIdentity = ObjectIdentity
hwASPF = _HwASPF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 6)
)
_HwAspfMibEudmObjects_ObjectIdentity = ObjectIdentity
hwAspfMibEudmObjects = _HwAspfMibEudmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 6, 2, 1)
)
_HwAspfEudmAppEnableTable_Object = MibTable
hwAspfEudmAppEnableTable = _HwAspfEudmAppEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 6, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hwAspfEudmAppEnableTable.setStatus("current")
_HwAspfEudmAppEnableEntry_Object = MibTableRow
hwAspfEudmAppEnableEntry = _HwAspfEudmAppEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 6, 2, 1, 1, 1)
)
hwAspfEudmAppEnableEntry.setIndexNames(
    (0, "MPLS-VPN-MIB", "mplsVpnVrfName"),
    (0, "HUAWEI-ASPF-EUDM-MIB", "hwAspfEudmAppEnableZoneID1"),
    (0, "HUAWEI-ASPF-EUDM-MIB", "hwAspfEudmAppEnableZoneID2"),
)
if mibBuilder.loadTexts:
    hwAspfEudmAppEnableEntry.setStatus("current")


class _HwAspfEudmAppEnableZoneID1_Type(Integer32):
    """Custom type hwAspfEudmAppEnableZoneID1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_HwAspfEudmAppEnableZoneID1_Type.__name__ = "Integer32"
_HwAspfEudmAppEnableZoneID1_Object = MibTableColumn
hwAspfEudmAppEnableZoneID1 = _HwAspfEudmAppEnableZoneID1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 6, 2, 1, 1, 1, 1),
    _HwAspfEudmAppEnableZoneID1_Type()
)
hwAspfEudmAppEnableZoneID1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwAspfEudmAppEnableZoneID1.setStatus("current")


class _HwAspfEudmAppEnableZoneID2_Type(Integer32):
    """Custom type hwAspfEudmAppEnableZoneID2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_HwAspfEudmAppEnableZoneID2_Type.__name__ = "Integer32"
_HwAspfEudmAppEnableZoneID2_Object = MibTableColumn
hwAspfEudmAppEnableZoneID2 = _HwAspfEudmAppEnableZoneID2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 6, 2, 1, 1, 1, 2),
    _HwAspfEudmAppEnableZoneID2_Type()
)
hwAspfEudmAppEnableZoneID2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwAspfEudmAppEnableZoneID2.setStatus("current")
_HwAspfEudmEnableFtp_Type = TruthValue
_HwAspfEudmEnableFtp_Object = MibTableColumn
hwAspfEudmEnableFtp = _HwAspfEudmEnableFtp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 6, 2, 1, 1, 1, 3),
    _HwAspfEudmEnableFtp_Type()
)
hwAspfEudmEnableFtp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAspfEudmEnableFtp.setStatus("current")
_HwAspfEudmEnableSmtp_Type = TruthValue
_HwAspfEudmEnableSmtp_Object = MibTableColumn
hwAspfEudmEnableSmtp = _HwAspfEudmEnableSmtp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 6, 2, 1, 1, 1, 4),
    _HwAspfEudmEnableSmtp_Type()
)
hwAspfEudmEnableSmtp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAspfEudmEnableSmtp.setStatus("current")
_HwAspfEudmEnableRstp_Type = TruthValue
_HwAspfEudmEnableRstp_Object = MibTableColumn
hwAspfEudmEnableRstp = _HwAspfEudmEnableRstp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 6, 2, 1, 1, 1, 5),
    _HwAspfEudmEnableRstp_Type()
)
hwAspfEudmEnableRstp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAspfEudmEnableRstp.setStatus("current")
_HwAspfEudmEnableH323_Type = TruthValue
_HwAspfEudmEnableH323_Object = MibTableColumn
hwAspfEudmEnableH323 = _HwAspfEudmEnableH323_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 6, 2, 1, 1, 1, 6),
    _HwAspfEudmEnableH323_Type()
)
hwAspfEudmEnableH323.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAspfEudmEnableH323.setStatus("current")
_HwAspfEudmEnableHttp_Type = TruthValue
_HwAspfEudmEnableHttp_Object = MibTableColumn
hwAspfEudmEnableHttp = _HwAspfEudmEnableHttp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 6, 2, 1, 1, 1, 7),
    _HwAspfEudmEnableHttp_Type()
)
hwAspfEudmEnableHttp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAspfEudmEnableHttp.setStatus("current")
_HwAspfEudmEnableJava_Type = TruthValue
_HwAspfEudmEnableJava_Object = MibTableColumn
hwAspfEudmEnableJava = _HwAspfEudmEnableJava_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 6, 2, 1, 1, 1, 8),
    _HwAspfEudmEnableJava_Type()
)
hwAspfEudmEnableJava.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAspfEudmEnableJava.setStatus("current")


class _HwAspfEudmEnableJavaAcl_Type(Integer32):
    """Custom type hwAspfEudmEnableJavaAcl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 2999),
    )


_HwAspfEudmEnableJavaAcl_Type.__name__ = "Integer32"
_HwAspfEudmEnableJavaAcl_Object = MibTableColumn
hwAspfEudmEnableJavaAcl = _HwAspfEudmEnableJavaAcl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 6, 2, 1, 1, 1, 9),
    _HwAspfEudmEnableJavaAcl_Type()
)
hwAspfEudmEnableJavaAcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAspfEudmEnableJavaAcl.setStatus("current")
_HwAspfEudmEnableActiveX_Type = TruthValue
_HwAspfEudmEnableActiveX_Object = MibTableColumn
hwAspfEudmEnableActiveX = _HwAspfEudmEnableActiveX_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 6, 2, 1, 1, 1, 10),
    _HwAspfEudmEnableActiveX_Type()
)
hwAspfEudmEnableActiveX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAspfEudmEnableActiveX.setStatus("current")


class _HwAspfEudmEnableActiveXAcl_Type(Integer32):
    """Custom type hwAspfEudmEnableActiveXAcl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 2999),
    )


_HwAspfEudmEnableActiveXAcl_Type.__name__ = "Integer32"
_HwAspfEudmEnableActiveXAcl_Object = MibTableColumn
hwAspfEudmEnableActiveXAcl = _HwAspfEudmEnableActiveXAcl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 6, 2, 1, 1, 1, 11),
    _HwAspfEudmEnableActiveXAcl_Type()
)
hwAspfEudmEnableActiveXAcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAspfEudmEnableActiveXAcl.setStatus("current")
_HwAspfEudmEnablePptp_Type = TruthValue
_HwAspfEudmEnablePptp_Object = MibTableColumn
hwAspfEudmEnablePptp = _HwAspfEudmEnablePptp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 6, 2, 1, 1, 1, 12),
    _HwAspfEudmEnablePptp_Type()
)
hwAspfEudmEnablePptp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAspfEudmEnablePptp.setStatus("current")
_HwAspfEudmEnableNetBios_Type = TruthValue
_HwAspfEudmEnableNetBios_Object = MibTableColumn
hwAspfEudmEnableNetBios = _HwAspfEudmEnableNetBios_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 6, 2, 1, 1, 1, 13),
    _HwAspfEudmEnableNetBios_Type()
)
hwAspfEudmEnableNetBios.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAspfEudmEnableNetBios.setStatus("current")
_HwAspfEudmEnableMsn_Type = TruthValue
_HwAspfEudmEnableMsn_Object = MibTableColumn
hwAspfEudmEnableMsn = _HwAspfEudmEnableMsn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 6, 2, 1, 1, 1, 14),
    _HwAspfEudmEnableMsn_Type()
)
hwAspfEudmEnableMsn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAspfEudmEnableMsn.setStatus("current")
_HwAspfEudmEnableQq_Type = TruthValue
_HwAspfEudmEnableQq_Object = MibTableColumn
hwAspfEudmEnableQq = _HwAspfEudmEnableQq_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 6, 2, 1, 1, 1, 15),
    _HwAspfEudmEnableQq_Type()
)
hwAspfEudmEnableQq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAspfEudmEnableQq.setStatus("current")
_HwAspfEudmEnableSip_Type = TruthValue
_HwAspfEudmEnableSip_Object = MibTableColumn
hwAspfEudmEnableSip = _HwAspfEudmEnableSip_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 6, 2, 1, 1, 1, 16),
    _HwAspfEudmEnableSip_Type()
)
hwAspfEudmEnableSip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAspfEudmEnableSip.setStatus("current")


class _HwAspfEudmEnableUserDefAcl_Type(Integer32):
    """Custom type hwAspfEudmEnableUserDefAcl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 2999),
    )


_HwAspfEudmEnableUserDefAcl_Type.__name__ = "Integer32"
_HwAspfEudmEnableUserDefAcl_Object = MibTableColumn
hwAspfEudmEnableUserDefAcl = _HwAspfEudmEnableUserDefAcl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 6, 2, 1, 1, 1, 17),
    _HwAspfEudmEnableUserDefAcl_Type()
)
hwAspfEudmEnableUserDefAcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAspfEudmEnableUserDefAcl.setStatus("current")


class _HwAspfEudmEnableUserDefAge_Type(Integer32):
    """Custom type hwAspfEudmEnableUserDefAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_HwAspfEudmEnableUserDefAge_Type.__name__ = "Integer32"
_HwAspfEudmEnableUserDefAge_Object = MibTableColumn
hwAspfEudmEnableUserDefAge = _HwAspfEudmEnableUserDefAge_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 6, 2, 1, 1, 1, 18),
    _HwAspfEudmEnableUserDefAge_Type()
)
hwAspfEudmEnableUserDefAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAspfEudmEnableUserDefAge.setStatus("current")
_HwAspfEudmEnableIdo_Type = TruthValue
_HwAspfEudmEnableIdo_Object = MibTableColumn
hwAspfEudmEnableIdo = _HwAspfEudmEnableIdo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 6, 2, 1, 1, 1, 19),
    _HwAspfEudmEnableIdo_Type()
)
hwAspfEudmEnableIdo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAspfEudmEnableIdo.setStatus("current")
_HwAspfEudmEnableIls_Type = TruthValue
_HwAspfEudmEnableIls_Object = MibTableColumn
hwAspfEudmEnableIls = _HwAspfEudmEnableIls_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 6, 2, 1, 1, 1, 20),
    _HwAspfEudmEnableIls_Type()
)
hwAspfEudmEnableIls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAspfEudmEnableIls.setStatus("current")
_HwAspfEudmConformance_ObjectIdentity = ObjectIdentity
hwAspfEudmConformance = _HwAspfEudmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 6, 2, 2)
)
_HwAspfEudmCompliance_ObjectIdentity = ObjectIdentity
hwAspfEudmCompliance = _HwAspfEudmCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 6, 2, 2, 1)
)
_HwAspfEudmMibGroups_ObjectIdentity = ObjectIdentity
hwAspfEudmMibGroups = _HwAspfEudmMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 6, 2, 2, 2)
)

# Managed Objects groups

hwAspfEudmAppEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 6, 2, 2, 2, 1)
)
hwAspfEudmAppEnableGroup.setObjects(
      *(("HUAWEI-ASPF-EUDM-MIB", "hwAspfEudmEnableFtp"),
        ("HUAWEI-ASPF-EUDM-MIB", "hwAspfEudmEnableRstp"),
        ("HUAWEI-ASPF-EUDM-MIB", "hwAspfEudmEnableH323"),
        ("HUAWEI-ASPF-EUDM-MIB", "hwAspfEudmEnableHttp"),
        ("HUAWEI-ASPF-EUDM-MIB", "hwAspfEudmEnableJava"),
        ("HUAWEI-ASPF-EUDM-MIB", "hwAspfEudmEnableJavaAcl"),
        ("HUAWEI-ASPF-EUDM-MIB", "hwAspfEudmEnableActiveX"),
        ("HUAWEI-ASPF-EUDM-MIB", "hwAspfEudmEnableActiveXAcl"),
        ("HUAWEI-ASPF-EUDM-MIB", "hwAspfEudmEnableSmtp"),
        ("HUAWEI-ASPF-EUDM-MIB", "hwAspfEudmEnablePptp"),
        ("HUAWEI-ASPF-EUDM-MIB", "hwAspfEudmEnableNetBios"),
        ("HUAWEI-ASPF-EUDM-MIB", "hwAspfEudmEnableMsn"),
        ("HUAWEI-ASPF-EUDM-MIB", "hwAspfEudmEnableQq"),
        ("HUAWEI-ASPF-EUDM-MIB", "hwAspfEudmEnableSip"),
        ("HUAWEI-ASPF-EUDM-MIB", "hwAspfEudmEnableUserDefAcl"),
        ("HUAWEI-ASPF-EUDM-MIB", "hwAspfEudmEnableUserDefAge"),
        ("HUAWEI-ASPF-EUDM-MIB", "hwAspfEudmEnableIdo"),
        ("HUAWEI-ASPF-EUDM-MIB", "hwAspfEudmEnableIls"))
)
if mibBuilder.loadTexts:
    hwAspfEudmAppEnableGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-ASPF-EUDM-MIB",
    **{"hwASPF": hwASPF,
       "hwASPFEudm": hwASPFEudm,
       "hwAspfMibEudmObjects": hwAspfMibEudmObjects,
       "hwAspfEudmAppEnableTable": hwAspfEudmAppEnableTable,
       "hwAspfEudmAppEnableEntry": hwAspfEudmAppEnableEntry,
       "hwAspfEudmAppEnableZoneID1": hwAspfEudmAppEnableZoneID1,
       "hwAspfEudmAppEnableZoneID2": hwAspfEudmAppEnableZoneID2,
       "hwAspfEudmEnableFtp": hwAspfEudmEnableFtp,
       "hwAspfEudmEnableSmtp": hwAspfEudmEnableSmtp,
       "hwAspfEudmEnableRstp": hwAspfEudmEnableRstp,
       "hwAspfEudmEnableH323": hwAspfEudmEnableH323,
       "hwAspfEudmEnableHttp": hwAspfEudmEnableHttp,
       "hwAspfEudmEnableJava": hwAspfEudmEnableJava,
       "hwAspfEudmEnableJavaAcl": hwAspfEudmEnableJavaAcl,
       "hwAspfEudmEnableActiveX": hwAspfEudmEnableActiveX,
       "hwAspfEudmEnableActiveXAcl": hwAspfEudmEnableActiveXAcl,
       "hwAspfEudmEnablePptp": hwAspfEudmEnablePptp,
       "hwAspfEudmEnableNetBios": hwAspfEudmEnableNetBios,
       "hwAspfEudmEnableMsn": hwAspfEudmEnableMsn,
       "hwAspfEudmEnableQq": hwAspfEudmEnableQq,
       "hwAspfEudmEnableSip": hwAspfEudmEnableSip,
       "hwAspfEudmEnableUserDefAcl": hwAspfEudmEnableUserDefAcl,
       "hwAspfEudmEnableUserDefAge": hwAspfEudmEnableUserDefAge,
       "hwAspfEudmEnableIdo": hwAspfEudmEnableIdo,
       "hwAspfEudmEnableIls": hwAspfEudmEnableIls,
       "hwAspfEudmConformance": hwAspfEudmConformance,
       "hwAspfEudmCompliance": hwAspfEudmCompliance,
       "hwAspfEudmMibGroups": hwAspfEudmMibGroups,
       "hwAspfEudmAppEnableGroup": hwAspfEudmAppEnableGroup}
)
