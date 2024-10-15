# SNMP MIB module (TPLINK-SDM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-SDM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:37 2024
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

(tplinkMgmt,) = mibBuilder.importSymbols(
    "TPLINK-MIB",
    "tplinkMgmt")


# MODULE-IDENTITY

tplinkSDMMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 90)
)
tplinkSDMMIB.setRevisions(
        ("2012-12-13 09:30",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkSDMMIBObjects_ObjectIdentity = ObjectIdentity
tplinkSDMMIBObjects = _TplinkSDMMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 90, 1)
)
_SdmTemLayOutTable_Object = MibTable
sdmTemLayOutTable = _SdmTemLayOutTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 90, 1, 1)
)
if mibBuilder.loadTexts:
    sdmTemLayOutTable.setStatus("current")
_SdmTemLayOutEntry_Object = MibTableRow
sdmTemLayOutEntry = _SdmTemLayOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 90, 1, 1, 1)
)
sdmTemLayOutEntry.setIndexNames(
    (0, "TPLINK-SDM-MIB", "sdmTemName"),
)
if mibBuilder.loadTexts:
    sdmTemLayOutEntry.setStatus("current")
_SdmTemName_Type = DisplayString
_SdmTemName_Object = MibTableColumn
sdmTemName = _SdmTemName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 90, 1, 1, 1, 2),
    _SdmTemName_Type()
)
sdmTemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdmTemName.setStatus("current")
_IpAclRuleNum_Type = Integer32
_IpAclRuleNum_Object = MibTableColumn
ipAclRuleNum = _IpAclRuleNum_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 90, 1, 1, 1, 3),
    _IpAclRuleNum_Type()
)
ipAclRuleNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAclRuleNum.setStatus("current")
_MacAclRuleNum_Type = Integer32
_MacAclRuleNum_Object = MibTableColumn
macAclRuleNum = _MacAclRuleNum_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 90, 1, 1, 1, 4),
    _MacAclRuleNum_Type()
)
macAclRuleNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macAclRuleNum.setStatus("current")
_CombinedAclRuleNum_Type = Integer32
_CombinedAclRuleNum_Object = MibTableColumn
combinedAclRuleNum = _CombinedAclRuleNum_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 90, 1, 1, 1, 5),
    _CombinedAclRuleNum_Type()
)
combinedAclRuleNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    combinedAclRuleNum.setStatus("current")
_Ipv6AclRuleNum_Type = Integer32
_Ipv6AclRuleNum_Object = MibTableColumn
ipv6AclRuleNum = _Ipv6AclRuleNum_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 90, 1, 1, 1, 6),
    _Ipv6AclRuleNum_Type()
)
ipv6AclRuleNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6AclRuleNum.setStatus("current")
_ArpDetectionNum_Type = Integer32
_ArpDetectionNum_Object = MibTableColumn
arpDetectionNum = _ArpDetectionNum_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 90, 1, 1, 1, 7),
    _ArpDetectionNum_Type()
)
arpDetectionNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpDetectionNum.setStatus("current")
_V6SourceNum_Type = Integer32
_V6SourceNum_Object = MibTableColumn
v6SourceNum = _V6SourceNum_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 90, 1, 1, 1, 8),
    _V6SourceNum_Type()
)
v6SourceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v6SourceNum.setStatus("current")
_SdmCurTemName_Type = DisplayString
_SdmCurTemName_Object = MibScalar
sdmCurTemName = _SdmCurTemName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 90, 1, 2),
    _SdmCurTemName_Type()
)
sdmCurTemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdmCurTemName.setStatus("current")


class _SdmNextTemID_Type(Integer32):
    """Custom type sdmNextTemID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("enterpriseV4", 1),
          ("enterpriseV6", 2))
    )


_SdmNextTemID_Type.__name__ = "Integer32"
_SdmNextTemID_Object = MibScalar
sdmNextTemID = _SdmNextTemID_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 90, 1, 3),
    _SdmNextTemID_Type()
)
sdmNextTemID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdmNextTemID.setStatus("current")
_TplinkSDMNotifications_ObjectIdentity = ObjectIdentity
tplinkSDMNotifications = _TplinkSDMNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 90, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-SDM-MIB",
    **{"tplinkSDMMIB": tplinkSDMMIB,
       "tplinkSDMMIBObjects": tplinkSDMMIBObjects,
       "sdmTemLayOutTable": sdmTemLayOutTable,
       "sdmTemLayOutEntry": sdmTemLayOutEntry,
       "sdmTemName": sdmTemName,
       "ipAclRuleNum": ipAclRuleNum,
       "macAclRuleNum": macAclRuleNum,
       "combinedAclRuleNum": combinedAclRuleNum,
       "ipv6AclRuleNum": ipv6AclRuleNum,
       "arpDetectionNum": arpDetectionNum,
       "v6SourceNum": v6SourceNum,
       "sdmCurTemName": sdmCurTemName,
       "sdmNextTemID": sdmNextTemID,
       "tplinkSDMNotifications": tplinkSDMNotifications}
)
