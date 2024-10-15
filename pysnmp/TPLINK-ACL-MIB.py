# SNMP MIB module (TPLINK-ACL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-ACL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:05:46 2024
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

(TPRowStatus,) = mibBuilder.importSymbols(
    "TPLINK-TC-MIB",
    "TPRowStatus")


# MODULE-IDENTITY

tplinkAclMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26)
)
tplinkAclMIB.setRevisions(
        ("2012-12-13 09:30",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkAclMIBObjects_ObjectIdentity = ObjectIdentity
tplinkAclMIBObjects = _TplinkAclMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1)
)
_TpPolicyConfigure_ObjectIdentity = ObjectIdentity
tpPolicyConfigure = _TpPolicyConfigure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 2)
)
_TpPolicyTable_Object = MibTable
tpPolicyTable = _TpPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tpPolicyTable.setStatus("current")
_TpPolicyEntry_Object = MibTableRow
tpPolicyEntry = _TpPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 2, 1, 1)
)
tpPolicyEntry.setIndexNames(
    (0, "TPLINK-ACL-MIB", "tpPolicyName"),
    (0, "TPLINK-ACL-MIB", "tpAclId"),
)
if mibBuilder.loadTexts:
    tpPolicyEntry.setStatus("current")
_TpPolicyName_Type = OctetString
_TpPolicyName_Object = MibTableColumn
tpPolicyName = _TpPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 2, 1, 1, 1),
    _TpPolicyName_Type()
)
tpPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPolicyName.setStatus("current")
_TpAclId_Type = Integer32
_TpAclId_Object = MibTableColumn
tpAclId = _TpAclId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 2, 1, 1, 2),
    _TpAclId_Type()
)
tpAclId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpAclId.setStatus("current")
_TpMirrorPort_Type = Integer32
_TpMirrorPort_Object = MibTableColumn
tpMirrorPort = _TpMirrorPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 2, 1, 1, 3),
    _TpMirrorPort_Type()
)
tpMirrorPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMirrorPort.setStatus("current")
_TpConditionRate_Type = Integer32
_TpConditionRate_Object = MibTableColumn
tpConditionRate = _TpConditionRate_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 2, 1, 1, 4),
    _TpConditionRate_Type()
)
tpConditionRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpConditionRate.setStatus("current")


class _TpIfExceedOperation_Type(Integer32):
    """Custom type tpIfExceedOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("none", 0))
    )


_TpIfExceedOperation_Type.__name__ = "Integer32"
_TpIfExceedOperation_Object = MibTableColumn
tpIfExceedOperation = _TpIfExceedOperation_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 2, 1, 1, 5),
    _TpIfExceedOperation_Type()
)
tpIfExceedOperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIfExceedOperation.setStatus("current")
_TpRedirectPort_Type = Integer32
_TpRedirectPort_Object = MibTableColumn
tpRedirectPort = _TpRedirectPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 2, 1, 1, 6),
    _TpRedirectPort_Type()
)
tpRedirectPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpRedirectPort.setStatus("current")


class _TpQosRemarkDSCP_Type(Integer32):
    """Custom type tpQosRemarkDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64)
        )
    )
    namedValues = NamedValues(
        *(("dscp0-be-000000", 0),
          ("dscp1", 1),
          ("dscp10-af11-001010", 10),
          ("dscp11", 11),
          ("dscp12-af12-001100", 12),
          ("dscp13", 13),
          ("dscp14-af13-001110", 14),
          ("dscp15", 15),
          ("dscp16-cs2-010000", 16),
          ("dscp17", 17),
          ("dscp18-af21-010010", 18),
          ("dscp19", 19),
          ("dscp2", 2),
          ("dscp20-af22-010100", 20),
          ("dscp21", 21),
          ("dscp22-af23-010110", 22),
          ("dscp23", 23),
          ("dscp24-cs3-011000", 24),
          ("dscp25", 25),
          ("dscp26-af31-011010", 26),
          ("dscp27", 27),
          ("dscp28-af32-011100", 28),
          ("dscp29", 29),
          ("dscp3", 3),
          ("dscp30-af33-011110", 30),
          ("dscp31", 31),
          ("dscp32-cs4-100000", 32),
          ("dscp33", 33),
          ("dscp34-af41-100010", 34),
          ("dscp35", 35),
          ("dscp36-af42-100100", 36),
          ("dscp37", 37),
          ("dscp38-af43-100110", 38),
          ("dscp39", 39),
          ("dscp4", 4),
          ("dscp40-cs5-101000", 40),
          ("dscp41", 41),
          ("dscp42", 42),
          ("dscp43", 43),
          ("dscp44", 44),
          ("dscp45", 45),
          ("dscp46-ef-101110", 46),
          ("dscp47", 47),
          ("dscp48-cs6-110000", 48),
          ("dscp49", 49),
          ("dscp5", 5),
          ("dscp50", 50),
          ("dscp51", 51),
          ("dscp52", 52),
          ("dscp53", 53),
          ("dscp54", 54),
          ("dscp55", 55),
          ("dscp56-cs7-111000", 56),
          ("dscp57", 57),
          ("dscp58", 58),
          ("dscp59", 59),
          ("dscp6", 6),
          ("dscp60", 60),
          ("dscp61", 61),
          ("dscp62", 62),
          ("dscp63", 63),
          ("dscp64-noLimit", 64),
          ("dscp7", 7),
          ("dscp8-cs1-001000", 8),
          ("dscp9", 9))
    )


_TpQosRemarkDSCP_Type.__name__ = "Integer32"
_TpQosRemarkDSCP_Object = MibTableColumn
tpQosRemarkDSCP = _TpQosRemarkDSCP_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 2, 1, 1, 7),
    _TpQosRemarkDSCP_Type()
)
tpQosRemarkDSCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpQosRemarkDSCP.setStatus("current")


class _TpQosRemarkLocalPri_Type(Integer32):
    """Custom type tpQosRemarkLocalPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("default", 0),
          ("tc0", 1),
          ("tc1", 2),
          ("tc2", 3),
          ("tc3", 4),
          ("tc4", 5),
          ("tc5", 6),
          ("tc6", 7),
          ("tc7", 8))
    )


_TpQosRemarkLocalPri_Type.__name__ = "Integer32"
_TpQosRemarkLocalPri_Object = MibTableColumn
tpQosRemarkLocalPri = _TpQosRemarkLocalPri_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 2, 1, 1, 8),
    _TpQosRemarkLocalPri_Type()
)
tpQosRemarkLocalPri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpQosRemarkLocalPri.setStatus("current")
_TpPolicyStatus_Type = TPRowStatus
_TpPolicyStatus_Object = MibTableColumn
tpPolicyStatus = _TpPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 2, 1, 1, 9),
    _TpPolicyStatus_Type()
)
tpPolicyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpPolicyStatus.setStatus("current")
_TpPolicyBindConfigure_ObjectIdentity = ObjectIdentity
tpPolicyBindConfigure = _TpPolicyBindConfigure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 3)
)
_TpPolicyBindPortTable_Object = MibTable
tpPolicyBindPortTable = _TpPolicyBindPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 3, 1)
)
if mibBuilder.loadTexts:
    tpPolicyBindPortTable.setStatus("current")
_TpPolicyBindPortEntry_Object = MibTableRow
tpPolicyBindPortEntry = _TpPolicyBindPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 3, 1, 1)
)
tpPolicyBindPortEntry.setIndexNames(
    (0, "TPLINK-ACL-MIB", "tpBindPortPolicyName"),
    (0, "TPLINK-ACL-MIB", "tpPolicyPort"),
)
if mibBuilder.loadTexts:
    tpPolicyBindPortEntry.setStatus("current")
_TpBindPortPolicyName_Type = OctetString
_TpBindPortPolicyName_Object = MibTableColumn
tpBindPortPolicyName = _TpBindPortPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 3, 1, 1, 1),
    _TpBindPortPolicyName_Type()
)
tpBindPortPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpBindPortPolicyName.setStatus("current")
_TpPolicyPort_Type = Integer32
_TpPolicyPort_Object = MibTableColumn
tpPolicyPort = _TpPolicyPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 3, 1, 1, 2),
    _TpPolicyPort_Type()
)
tpPolicyPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPolicyPort.setStatus("current")
_TpPolicyBindPortStatus_Type = TPRowStatus
_TpPolicyBindPortStatus_Object = MibTableColumn
tpPolicyBindPortStatus = _TpPolicyBindPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 3, 1, 1, 3),
    _TpPolicyBindPortStatus_Type()
)
tpPolicyBindPortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpPolicyBindPortStatus.setStatus("current")
_TpPolicyBindVlanTable_Object = MibTable
tpPolicyBindVlanTable = _TpPolicyBindVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 3, 2)
)
if mibBuilder.loadTexts:
    tpPolicyBindVlanTable.setStatus("current")
_TpPolicyBindVlanEntry_Object = MibTableRow
tpPolicyBindVlanEntry = _TpPolicyBindVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 3, 2, 1)
)
tpPolicyBindVlanEntry.setIndexNames(
    (0, "TPLINK-ACL-MIB", "tpBindVlanPolicyName"),
    (0, "TPLINK-ACL-MIB", "tpPolicyVlan"),
)
if mibBuilder.loadTexts:
    tpPolicyBindVlanEntry.setStatus("current")
_TpBindVlanPolicyName_Type = OctetString
_TpBindVlanPolicyName_Object = MibTableColumn
tpBindVlanPolicyName = _TpBindVlanPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 3, 2, 1, 1),
    _TpBindVlanPolicyName_Type()
)
tpBindVlanPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpBindVlanPolicyName.setStatus("current")
_TpPolicyVlan_Type = Integer32
_TpPolicyVlan_Object = MibTableColumn
tpPolicyVlan = _TpPolicyVlan_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 3, 2, 1, 2),
    _TpPolicyVlan_Type()
)
tpPolicyVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPolicyVlan.setStatus("current")
_TpPolicyBindVlanStatus_Type = TPRowStatus
_TpPolicyBindVlanStatus_Object = MibTableColumn
tpPolicyBindVlanStatus = _TpPolicyBindVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 3, 2, 1, 3),
    _TpPolicyBindVlanStatus_Type()
)
tpPolicyBindVlanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpPolicyBindVlanStatus.setStatus("current")
_TpAclBindConfigure_ObjectIdentity = ObjectIdentity
tpAclBindConfigure = _TpAclBindConfigure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 4)
)
_TpAclBindPortTable_Object = MibTable
tpAclBindPortTable = _TpAclBindPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 4, 1)
)
if mibBuilder.loadTexts:
    tpAclBindPortTable.setStatus("current")
_TpAclBindPortEntry_Object = MibTableRow
tpAclBindPortEntry = _TpAclBindPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 4, 1, 1)
)
tpAclBindPortEntry.setIndexNames(
    (0, "TPLINK-ACL-MIB", "tpBindPortAclId"),
    (0, "TPLINK-ACL-MIB", "tpAclPort"),
)
if mibBuilder.loadTexts:
    tpAclBindPortEntry.setStatus("current")
_TpBindPortAclId_Type = OctetString
_TpBindPortAclId_Object = MibTableColumn
tpBindPortAclId = _TpBindPortAclId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 4, 1, 1, 1),
    _TpBindPortAclId_Type()
)
tpBindPortAclId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpBindPortAclId.setStatus("current")
_TpAclPort_Type = Integer32
_TpAclPort_Object = MibTableColumn
tpAclPort = _TpAclPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 4, 1, 1, 2),
    _TpAclPort_Type()
)
tpAclPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpAclPort.setStatus("current")
_TpAclBindPortStatus_Type = TPRowStatus
_TpAclBindPortStatus_Object = MibTableColumn
tpAclBindPortStatus = _TpAclBindPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 4, 1, 1, 3),
    _TpAclBindPortStatus_Type()
)
tpAclBindPortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpAclBindPortStatus.setStatus("current")
_TpAclBindVlanTable_Object = MibTable
tpAclBindVlanTable = _TpAclBindVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 4, 2)
)
if mibBuilder.loadTexts:
    tpAclBindVlanTable.setStatus("current")
_TpAclBindVlanEntry_Object = MibTableRow
tpAclBindVlanEntry = _TpAclBindVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 4, 2, 1)
)
tpAclBindVlanEntry.setIndexNames(
    (0, "TPLINK-ACL-MIB", "tpBindVlanAclId"),
    (0, "TPLINK-ACL-MIB", "tpAclVlan"),
)
if mibBuilder.loadTexts:
    tpAclBindVlanEntry.setStatus("current")
_TpBindVlanAclId_Type = OctetString
_TpBindVlanAclId_Object = MibTableColumn
tpBindVlanAclId = _TpBindVlanAclId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 4, 2, 1, 1),
    _TpBindVlanAclId_Type()
)
tpBindVlanAclId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpBindVlanAclId.setStatus("current")
_TpAclVlan_Type = Integer32
_TpAclVlan_Object = MibTableColumn
tpAclVlan = _TpAclVlan_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 4, 2, 1, 2),
    _TpAclVlan_Type()
)
tpAclVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpAclVlan.setStatus("current")
_TpAclBindVlanStatus_Type = TPRowStatus
_TpAclBindVlanStatus_Object = MibTableColumn
tpAclBindVlanStatus = _TpAclBindVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 4, 2, 1, 3),
    _TpAclBindVlanStatus_Type()
)
tpAclBindVlanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpAclBindVlanStatus.setStatus("current")
_TplinkAclNotifications_ObjectIdentity = ObjectIdentity
tplinkAclNotifications = _TplinkAclNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-ACL-MIB",
    **{"tplinkAclMIB": tplinkAclMIB,
       "tplinkAclMIBObjects": tplinkAclMIBObjects,
       "tpPolicyConfigure": tpPolicyConfigure,
       "tpPolicyTable": tpPolicyTable,
       "tpPolicyEntry": tpPolicyEntry,
       "tpPolicyName": tpPolicyName,
       "tpAclId": tpAclId,
       "tpMirrorPort": tpMirrorPort,
       "tpConditionRate": tpConditionRate,
       "tpIfExceedOperation": tpIfExceedOperation,
       "tpRedirectPort": tpRedirectPort,
       "tpQosRemarkDSCP": tpQosRemarkDSCP,
       "tpQosRemarkLocalPri": tpQosRemarkLocalPri,
       "tpPolicyStatus": tpPolicyStatus,
       "tpPolicyBindConfigure": tpPolicyBindConfigure,
       "tpPolicyBindPortTable": tpPolicyBindPortTable,
       "tpPolicyBindPortEntry": tpPolicyBindPortEntry,
       "tpBindPortPolicyName": tpBindPortPolicyName,
       "tpPolicyPort": tpPolicyPort,
       "tpPolicyBindPortStatus": tpPolicyBindPortStatus,
       "tpPolicyBindVlanTable": tpPolicyBindVlanTable,
       "tpPolicyBindVlanEntry": tpPolicyBindVlanEntry,
       "tpBindVlanPolicyName": tpBindVlanPolicyName,
       "tpPolicyVlan": tpPolicyVlan,
       "tpPolicyBindVlanStatus": tpPolicyBindVlanStatus,
       "tpAclBindConfigure": tpAclBindConfigure,
       "tpAclBindPortTable": tpAclBindPortTable,
       "tpAclBindPortEntry": tpAclBindPortEntry,
       "tpBindPortAclId": tpBindPortAclId,
       "tpAclPort": tpAclPort,
       "tpAclBindPortStatus": tpAclBindPortStatus,
       "tpAclBindVlanTable": tpAclBindVlanTable,
       "tpAclBindVlanEntry": tpAclBindVlanEntry,
       "tpBindVlanAclId": tpBindVlanAclId,
       "tpAclVlan": tpAclVlan,
       "tpAclBindVlanStatus": tpAclBindVlanStatus,
       "tplinkAclNotifications": tplinkAclNotifications}
)
