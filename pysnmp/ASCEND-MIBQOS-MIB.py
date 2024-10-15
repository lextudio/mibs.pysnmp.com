# SNMP MIB module (ASCEND-MIBQOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBQOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:05 2024
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

(configuration,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "configuration")

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


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MibqosProfile_ObjectIdentity = ObjectIdentity
mibqosProfile = _MibqosProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 169)
)
_MibqosProfileTable_Object = MibTable
mibqosProfileTable = _MibqosProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 169, 1)
)
if mibBuilder.loadTexts:
    mibqosProfileTable.setStatus("mandatory")
_MibqosProfileEntry_Object = MibTableRow
mibqosProfileEntry = _MibqosProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 169, 1, 1)
)
mibqosProfileEntry.setIndexNames(
    (0, "ASCEND-MIBQOS-MIB", "qosProfile-Index-o"),
)
if mibBuilder.loadTexts:
    mibqosProfileEntry.setStatus("mandatory")
_QosProfile_Index_o_Type = Integer32
_QosProfile_Index_o_Object = MibScalar
qosProfile_Index_o = _QosProfile_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 169, 1, 1, 1),
    _QosProfile_Index_o_Type()
)
qosProfile_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosProfile_Index_o.setStatus("mandatory")


class _QosProfile_Enabled_Type(Integer32):
    """Custom type qosProfile_Enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_QosProfile_Enabled_Type.__name__ = "Integer32"
_QosProfile_Enabled_Object = MibScalar
qosProfile_Enabled = _QosProfile_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 169, 1, 1, 2),
    _QosProfile_Enabled_Type()
)
qosProfile_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosProfile_Enabled.setStatus("mandatory")


class _QosProfile_AllowClientDscp_Type(Integer32):
    """Custom type qosProfile_AllowClientDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_QosProfile_AllowClientDscp_Type.__name__ = "Integer32"
_QosProfile_AllowClientDscp_Object = MibScalar
qosProfile_AllowClientDscp = _QosProfile_AllowClientDscp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 169, 1, 1, 3),
    _QosProfile_AllowClientDscp_Type()
)
qosProfile_AllowClientDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosProfile_AllowClientDscp.setStatus("mandatory")


class _QosProfile_Action_o_Type(Integer32):
    """Custom type qosProfile_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_QosProfile_Action_o_Type.__name__ = "Integer32"
_QosProfile_Action_o_Object = MibScalar
qosProfile_Action_o = _QosProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 169, 1, 1, 4),
    _QosProfile_Action_o_Type()
)
qosProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosProfile_Action_o.setStatus("mandatory")
_MibqosProfile_TagMapTable_Object = MibTable
mibqosProfile_TagMapTable = _MibqosProfile_TagMapTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 169, 2)
)
if mibBuilder.loadTexts:
    mibqosProfile_TagMapTable.setStatus("mandatory")
_MibqosProfile_TagMapEntry_Object = MibTableRow
mibqosProfile_TagMapEntry = _MibqosProfile_TagMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 169, 2, 1)
)
mibqosProfile_TagMapEntry.setIndexNames(
    (0, "ASCEND-MIBQOS-MIB", "qosProfile-TagMap-Index-o"),
    (0, "ASCEND-MIBQOS-MIB", "qosProfile-TagMap-Index1-o"),
)
if mibBuilder.loadTexts:
    mibqosProfile_TagMapEntry.setStatus("mandatory")
_QosProfile_TagMap_Index_o_Type = Integer32
_QosProfile_TagMap_Index_o_Object = MibScalar
qosProfile_TagMap_Index_o = _QosProfile_TagMap_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 169, 2, 1, 1),
    _QosProfile_TagMap_Index_o_Type()
)
qosProfile_TagMap_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosProfile_TagMap_Index_o.setStatus("mandatory")
_QosProfile_TagMap_Index1_o_Type = Integer32
_QosProfile_TagMap_Index1_o_Object = MibScalar
qosProfile_TagMap_Index1_o = _QosProfile_TagMap_Index1_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 169, 2, 1, 2),
    _QosProfile_TagMap_Index1_o_Type()
)
qosProfile_TagMap_Index1_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosProfile_TagMap_Index1_o.setStatus("mandatory")


class _QosProfile_TagMap_Active_Type(Integer32):
    """Custom type qosProfile_TagMap_Active based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_QosProfile_TagMap_Active_Type.__name__ = "Integer32"
_QosProfile_TagMap_Active_Object = MibScalar
qosProfile_TagMap_Active = _QosProfile_TagMap_Active_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 169, 2, 1, 3),
    _QosProfile_TagMap_Active_Type()
)
qosProfile_TagMap_Active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosProfile_TagMap_Active.setStatus("mandatory")
_QosProfile_TagMap_Dscp_Type = DisplayString
_QosProfile_TagMap_Dscp_Object = MibScalar
qosProfile_TagMap_Dscp = _QosProfile_TagMap_Dscp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 169, 2, 1, 4),
    _QosProfile_TagMap_Dscp_Type()
)
qosProfile_TagMap_Dscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosProfile_TagMap_Dscp.setStatus("mandatory")
_QosProfile_TagMap_QosTag_Type = Integer32
_QosProfile_TagMap_QosTag_Object = MibScalar
qosProfile_TagMap_QosTag = _QosProfile_TagMap_QosTag_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 169, 2, 1, 5),
    _QosProfile_TagMap_QosTag_Type()
)
qosProfile_TagMap_QosTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosProfile_TagMap_QosTag.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBQOS-MIB",
    **{"DisplayString": DisplayString,
       "mibqosProfile": mibqosProfile,
       "mibqosProfileTable": mibqosProfileTable,
       "mibqosProfileEntry": mibqosProfileEntry,
       "qosProfile-Index-o": qosProfile_Index_o,
       "qosProfile-Enabled": qosProfile_Enabled,
       "qosProfile-AllowClientDscp": qosProfile_AllowClientDscp,
       "qosProfile-Action-o": qosProfile_Action_o,
       "mibqosProfile-TagMapTable": mibqosProfile_TagMapTable,
       "mibqosProfile-TagMapEntry": mibqosProfile_TagMapEntry,
       "qosProfile-TagMap-Index-o": qosProfile_TagMap_Index_o,
       "qosProfile-TagMap-Index1-o": qosProfile_TagMap_Index1_o,
       "qosProfile-TagMap-Active": qosProfile_TagMap_Active,
       "qosProfile-TagMap-Dscp": qosProfile_TagMap_Dscp,
       "qosProfile-TagMap-QosTag": qosProfile_TagMap_QosTag}
)
