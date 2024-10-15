# SNMP MIB module (ASCEND-MIBSNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBSNMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:13 2024
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

_MibsnmpProfile_ObjectIdentity = ObjectIdentity
mibsnmpProfile = _MibsnmpProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 114)
)
_MibsnmpProfileTable_Object = MibTable
mibsnmpProfileTable = _MibsnmpProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 114, 1)
)
if mibBuilder.loadTexts:
    mibsnmpProfileTable.setStatus("mandatory")
_MibsnmpProfileEntry_Object = MibTableRow
mibsnmpProfileEntry = _MibsnmpProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 114, 1, 1)
)
mibsnmpProfileEntry.setIndexNames(
    (0, "ASCEND-MIBSNMP-MIB", "snmpProfile-Index-o"),
)
if mibBuilder.loadTexts:
    mibsnmpProfileEntry.setStatus("mandatory")
_SnmpProfile_Index_o_Type = Integer32
_SnmpProfile_Index_o_Object = MibScalar
snmpProfile_Index_o = _SnmpProfile_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 114, 1, 1, 1),
    _SnmpProfile_Index_o_Type()
)
snmpProfile_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpProfile_Index_o.setStatus("mandatory")


class _SnmpProfile_Enabled_Type(Integer32):
    """Custom type snmpProfile_Enabled based on Integer32"""
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


_SnmpProfile_Enabled_Type.__name__ = "Integer32"
_SnmpProfile_Enabled_Object = MibScalar
snmpProfile_Enabled = _SnmpProfile_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 114, 1, 1, 2),
    _SnmpProfile_Enabled_Type()
)
snmpProfile_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpProfile_Enabled.setStatus("mandatory")
_SnmpProfile_ReadCommunity_Type = DisplayString
_SnmpProfile_ReadCommunity_Object = MibScalar
snmpProfile_ReadCommunity = _SnmpProfile_ReadCommunity_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 114, 1, 1, 3),
    _SnmpProfile_ReadCommunity_Type()
)
snmpProfile_ReadCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpProfile_ReadCommunity.setStatus("mandatory")


class _SnmpProfile_ReadWriteEnabled_Type(Integer32):
    """Custom type snmpProfile_ReadWriteEnabled based on Integer32"""
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


_SnmpProfile_ReadWriteEnabled_Type.__name__ = "Integer32"
_SnmpProfile_ReadWriteEnabled_Object = MibScalar
snmpProfile_ReadWriteEnabled = _SnmpProfile_ReadWriteEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 114, 1, 1, 4),
    _SnmpProfile_ReadWriteEnabled_Type()
)
snmpProfile_ReadWriteEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpProfile_ReadWriteEnabled.setStatus("mandatory")
_SnmpProfile_ReadWriteCommunity_Type = DisplayString
_SnmpProfile_ReadWriteCommunity_Object = MibScalar
snmpProfile_ReadWriteCommunity = _SnmpProfile_ReadWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 114, 1, 1, 5),
    _SnmpProfile_ReadWriteCommunity_Type()
)
snmpProfile_ReadWriteCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpProfile_ReadWriteCommunity.setStatus("mandatory")


class _SnmpProfile_EnforceAddressSecurity_Type(Integer32):
    """Custom type snmpProfile_EnforceAddressSecurity based on Integer32"""
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


_SnmpProfile_EnforceAddressSecurity_Type.__name__ = "Integer32"
_SnmpProfile_EnforceAddressSecurity_Object = MibScalar
snmpProfile_EnforceAddressSecurity = _SnmpProfile_EnforceAddressSecurity_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 114, 1, 1, 6),
    _SnmpProfile_EnforceAddressSecurity_Type()
)
snmpProfile_EnforceAddressSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpProfile_EnforceAddressSecurity.setStatus("mandatory")
_SnmpProfile_Contact_Type = DisplayString
_SnmpProfile_Contact_Object = MibScalar
snmpProfile_Contact = _SnmpProfile_Contact_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 114, 1, 1, 7),
    _SnmpProfile_Contact_Type()
)
snmpProfile_Contact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpProfile_Contact.setStatus("mandatory")
_SnmpProfile_Location_Type = DisplayString
_SnmpProfile_Location_Object = MibScalar
snmpProfile_Location = _SnmpProfile_Location_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 114, 1, 1, 8),
    _SnmpProfile_Location_Type()
)
snmpProfile_Location.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpProfile_Location.setStatus("mandatory")
_SnmpProfile_QueueDepth_Type = Integer32
_SnmpProfile_QueueDepth_Object = MibScalar
snmpProfile_QueueDepth = _SnmpProfile_QueueDepth_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 114, 1, 1, 9),
    _SnmpProfile_QueueDepth_Type()
)
snmpProfile_QueueDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpProfile_QueueDepth.setStatus("mandatory")


class _SnmpProfile_CsmModemDiag_Type(Integer32):
    """Custom type snmpProfile_CsmModemDiag based on Integer32"""
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


_SnmpProfile_CsmModemDiag_Type.__name__ = "Integer32"
_SnmpProfile_CsmModemDiag_Object = MibScalar
snmpProfile_CsmModemDiag = _SnmpProfile_CsmModemDiag_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 114, 1, 1, 10),
    _SnmpProfile_CsmModemDiag_Type()
)
snmpProfile_CsmModemDiag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpProfile_CsmModemDiag.setStatus("mandatory")


class _SnmpProfile_SnmpMessageType_Type(Integer32):
    """Custom type snmpProfile_SnmpMessageType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v1AndV3", 1),
          ("v1Only", 2),
          ("v3Only", 3))
    )


_SnmpProfile_SnmpMessageType_Type.__name__ = "Integer32"
_SnmpProfile_SnmpMessageType_Object = MibScalar
snmpProfile_SnmpMessageType = _SnmpProfile_SnmpMessageType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 114, 1, 1, 11),
    _SnmpProfile_SnmpMessageType_Type()
)
snmpProfile_SnmpMessageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpProfile_SnmpMessageType.setStatus("mandatory")


class _SnmpProfile_SecurityLevel_Type(Integer32):
    """Custom type snmpProfile_SecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("authNopriv", 2),
          ("authPriv", 3),
          ("none", 1))
    )


_SnmpProfile_SecurityLevel_Type.__name__ = "Integer32"
_SnmpProfile_SecurityLevel_Object = MibScalar
snmpProfile_SecurityLevel = _SnmpProfile_SecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 114, 1, 1, 12),
    _SnmpProfile_SecurityLevel_Type()
)
snmpProfile_SecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpProfile_SecurityLevel.setStatus("mandatory")


class _SnmpProfile_EnableVacm_Type(Integer32):
    """Custom type snmpProfile_EnableVacm based on Integer32"""
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


_SnmpProfile_EnableVacm_Type.__name__ = "Integer32"
_SnmpProfile_EnableVacm_Object = MibScalar
snmpProfile_EnableVacm = _SnmpProfile_EnableVacm_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 114, 1, 1, 13),
    _SnmpProfile_EnableVacm_Type()
)
snmpProfile_EnableVacm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpProfile_EnableVacm.setStatus("mandatory")


class _SnmpProfile_Action_o_Type(Integer32):
    """Custom type snmpProfile_Action_o based on Integer32"""
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


_SnmpProfile_Action_o_Type.__name__ = "Integer32"
_SnmpProfile_Action_o_Object = MibScalar
snmpProfile_Action_o = _SnmpProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 114, 1, 1, 14),
    _SnmpProfile_Action_o_Type()
)
snmpProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpProfile_Action_o.setStatus("mandatory")
_SnmpProfile_NotificationLogAgeOut_Type = Integer32
_SnmpProfile_NotificationLogAgeOut_Object = MibScalar
snmpProfile_NotificationLogAgeOut = _SnmpProfile_NotificationLogAgeOut_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 114, 1, 1, 15),
    _SnmpProfile_NotificationLogAgeOut_Type()
)
snmpProfile_NotificationLogAgeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpProfile_NotificationLogAgeOut.setStatus("mandatory")


class _SnmpProfile_EarlyQueueDiscard_Type(Integer32):
    """Custom type snmpProfile_EarlyQueueDiscard based on Integer32"""
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


_SnmpProfile_EarlyQueueDiscard_Type.__name__ = "Integer32"
_SnmpProfile_EarlyQueueDiscard_Object = MibScalar
snmpProfile_EarlyQueueDiscard = _SnmpProfile_EarlyQueueDiscard_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 114, 1, 1, 16),
    _SnmpProfile_EarlyQueueDiscard_Type()
)
snmpProfile_EarlyQueueDiscard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpProfile_EarlyQueueDiscard.setStatus("mandatory")


class _SnmpProfile_BitStringsAllowed_Type(Integer32):
    """Custom type snmpProfile_BitStringsAllowed based on Integer32"""
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


_SnmpProfile_BitStringsAllowed_Type.__name__ = "Integer32"
_SnmpProfile_BitStringsAllowed_Object = MibScalar
snmpProfile_BitStringsAllowed = _SnmpProfile_BitStringsAllowed_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 114, 1, 1, 17),
    _SnmpProfile_BitStringsAllowed_Type()
)
snmpProfile_BitStringsAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpProfile_BitStringsAllowed.setStatus("mandatory")
_SnmpProfile_AlarmClearTableLimit_Type = Integer32
_SnmpProfile_AlarmClearTableLimit_Object = MibScalar
snmpProfile_AlarmClearTableLimit = _SnmpProfile_AlarmClearTableLimit_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 114, 1, 1, 18),
    _SnmpProfile_AlarmClearTableLimit_Type()
)
snmpProfile_AlarmClearTableLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpProfile_AlarmClearTableLimit.setStatus("mandatory")
_MibusmUserProfile_ObjectIdentity = ObjectIdentity
mibusmUserProfile = _MibusmUserProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 115)
)
_MibusmUserProfileTable_Object = MibTable
mibusmUserProfileTable = _MibusmUserProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 115, 1)
)
if mibBuilder.loadTexts:
    mibusmUserProfileTable.setStatus("mandatory")
_MibusmUserProfileEntry_Object = MibTableRow
mibusmUserProfileEntry = _MibusmUserProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 115, 1, 1)
)
mibusmUserProfileEntry.setIndexNames(
    (0, "ASCEND-MIBSNMP-MIB", "usmUserProfile-Name"),
)
if mibBuilder.loadTexts:
    mibusmUserProfileEntry.setStatus("mandatory")
_UsmUserProfile_Name_Type = OctetString
_UsmUserProfile_Name_Object = MibScalar
usmUserProfile_Name = _UsmUserProfile_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 115, 1, 1, 1),
    _UsmUserProfile_Name_Type()
)
usmUserProfile_Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usmUserProfile_Name.setStatus("mandatory")


class _UsmUserProfile_ActiveEnabled_Type(Integer32):
    """Custom type usmUserProfile_ActiveEnabled based on Integer32"""
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


_UsmUserProfile_ActiveEnabled_Type.__name__ = "Integer32"
_UsmUserProfile_ActiveEnabled_Object = MibScalar
usmUserProfile_ActiveEnabled = _UsmUserProfile_ActiveEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 115, 1, 1, 2),
    _UsmUserProfile_ActiveEnabled_Type()
)
usmUserProfile_ActiveEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usmUserProfile_ActiveEnabled.setStatus("mandatory")


class _UsmUserProfile_ReadWriteAccess_Type(Integer32):
    """Custom type usmUserProfile_ReadWriteAccess based on Integer32"""
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


_UsmUserProfile_ReadWriteAccess_Type.__name__ = "Integer32"
_UsmUserProfile_ReadWriteAccess_Object = MibScalar
usmUserProfile_ReadWriteAccess = _UsmUserProfile_ReadWriteAccess_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 115, 1, 1, 3),
    _UsmUserProfile_ReadWriteAccess_Type()
)
usmUserProfile_ReadWriteAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usmUserProfile_ReadWriteAccess.setStatus("mandatory")


class _UsmUserProfile_AuthProtocol_Type(Integer32):
    """Custom type usmUserProfile_AuthProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("md5Auth", 2),
          ("noAuth", 1),
          ("shaAuth", 3))
    )


_UsmUserProfile_AuthProtocol_Type.__name__ = "Integer32"
_UsmUserProfile_AuthProtocol_Object = MibScalar
usmUserProfile_AuthProtocol = _UsmUserProfile_AuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 115, 1, 1, 4),
    _UsmUserProfile_AuthProtocol_Type()
)
usmUserProfile_AuthProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usmUserProfile_AuthProtocol.setStatus("mandatory")


class _UsmUserProfile_PrivProtocol_Type(Integer32):
    """Custom type usmUserProfile_PrivProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("desPriv", 2),
          ("noPriv", 1))
    )


_UsmUserProfile_PrivProtocol_Type.__name__ = "Integer32"
_UsmUserProfile_PrivProtocol_Object = MibScalar
usmUserProfile_PrivProtocol = _UsmUserProfile_PrivProtocol_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 115, 1, 1, 5),
    _UsmUserProfile_PrivProtocol_Type()
)
usmUserProfile_PrivProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usmUserProfile_PrivProtocol.setStatus("mandatory")
_UsmUserProfile_AuthKey_Type = OctetString
_UsmUserProfile_AuthKey_Object = MibScalar
usmUserProfile_AuthKey = _UsmUserProfile_AuthKey_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 115, 1, 1, 6),
    _UsmUserProfile_AuthKey_Type()
)
usmUserProfile_AuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usmUserProfile_AuthKey.setStatus("mandatory")
_UsmUserProfile_PrivKey_Type = OctetString
_UsmUserProfile_PrivKey_Object = MibScalar
usmUserProfile_PrivKey = _UsmUserProfile_PrivKey_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 115, 1, 1, 7),
    _UsmUserProfile_PrivKey_Type()
)
usmUserProfile_PrivKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usmUserProfile_PrivKey.setStatus("mandatory")


class _UsmUserProfile_Action_o_Type(Integer32):
    """Custom type usmUserProfile_Action_o based on Integer32"""
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


_UsmUserProfile_Action_o_Type.__name__ = "Integer32"
_UsmUserProfile_Action_o_Object = MibScalar
usmUserProfile_Action_o = _UsmUserProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 115, 1, 1, 8),
    _UsmUserProfile_Action_o_Type()
)
usmUserProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usmUserProfile_Action_o.setStatus("mandatory")
_Mibsnmpv3TargetParamProfile_ObjectIdentity = ObjectIdentity
mibsnmpv3TargetParamProfile = _Mibsnmpv3TargetParamProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 116)
)
_Mibsnmpv3TargetParamProfileTable_Object = MibTable
mibsnmpv3TargetParamProfileTable = _Mibsnmpv3TargetParamProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 116, 1)
)
if mibBuilder.loadTexts:
    mibsnmpv3TargetParamProfileTable.setStatus("mandatory")
_Mibsnmpv3TargetParamProfileEntry_Object = MibTableRow
mibsnmpv3TargetParamProfileEntry = _Mibsnmpv3TargetParamProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 116, 1, 1)
)
mibsnmpv3TargetParamProfileEntry.setIndexNames(
    (0, "ASCEND-MIBSNMP-MIB", "snmpv3TargetParamProfile-Name"),
)
if mibBuilder.loadTexts:
    mibsnmpv3TargetParamProfileEntry.setStatus("mandatory")
_Snmpv3TargetParamProfile_Name_Type = OctetString
_Snmpv3TargetParamProfile_Name_Object = MibScalar
snmpv3TargetParamProfile_Name = _Snmpv3TargetParamProfile_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 116, 1, 1, 1),
    _Snmpv3TargetParamProfile_Name_Type()
)
snmpv3TargetParamProfile_Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpv3TargetParamProfile_Name.setStatus("mandatory")


class _Snmpv3TargetParamProfile_ActiveEnabled_Type(Integer32):
    """Custom type snmpv3TargetParamProfile_ActiveEnabled based on Integer32"""
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


_Snmpv3TargetParamProfile_ActiveEnabled_Type.__name__ = "Integer32"
_Snmpv3TargetParamProfile_ActiveEnabled_Object = MibScalar
snmpv3TargetParamProfile_ActiveEnabled = _Snmpv3TargetParamProfile_ActiveEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 116, 1, 1, 2),
    _Snmpv3TargetParamProfile_ActiveEnabled_Type()
)
snmpv3TargetParamProfile_ActiveEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpv3TargetParamProfile_ActiveEnabled.setStatus("mandatory")


class _Snmpv3TargetParamProfile_MsgProcModel_Type(Integer32):
    """Custom type snmpv3TargetParamProfile_MsgProcModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v3", 4))
    )


_Snmpv3TargetParamProfile_MsgProcModel_Type.__name__ = "Integer32"
_Snmpv3TargetParamProfile_MsgProcModel_Object = MibScalar
snmpv3TargetParamProfile_MsgProcModel = _Snmpv3TargetParamProfile_MsgProcModel_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 116, 1, 1, 3),
    _Snmpv3TargetParamProfile_MsgProcModel_Type()
)
snmpv3TargetParamProfile_MsgProcModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpv3TargetParamProfile_MsgProcModel.setStatus("mandatory")


class _Snmpv3TargetParamProfile_SecurityModel_Type(Integer32):
    """Custom type snmpv3TargetParamProfile_SecurityModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("v1", 2),
          ("v3Usm", 4))
    )


_Snmpv3TargetParamProfile_SecurityModel_Type.__name__ = "Integer32"
_Snmpv3TargetParamProfile_SecurityModel_Object = MibScalar
snmpv3TargetParamProfile_SecurityModel = _Snmpv3TargetParamProfile_SecurityModel_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 116, 1, 1, 4),
    _Snmpv3TargetParamProfile_SecurityModel_Type()
)
snmpv3TargetParamProfile_SecurityModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpv3TargetParamProfile_SecurityModel.setStatus("mandatory")
_Snmpv3TargetParamProfile_SecurityName_Type = OctetString
_Snmpv3TargetParamProfile_SecurityName_Object = MibScalar
snmpv3TargetParamProfile_SecurityName = _Snmpv3TargetParamProfile_SecurityName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 116, 1, 1, 5),
    _Snmpv3TargetParamProfile_SecurityName_Type()
)
snmpv3TargetParamProfile_SecurityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpv3TargetParamProfile_SecurityName.setStatus("mandatory")


class _Snmpv3TargetParamProfile_SecurityLevel_Type(Integer32):
    """Custom type snmpv3TargetParamProfile_SecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("authNopriv", 2),
          ("authPriv", 3),
          ("none", 1))
    )


_Snmpv3TargetParamProfile_SecurityLevel_Type.__name__ = "Integer32"
_Snmpv3TargetParamProfile_SecurityLevel_Object = MibScalar
snmpv3TargetParamProfile_SecurityLevel = _Snmpv3TargetParamProfile_SecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 116, 1, 1, 6),
    _Snmpv3TargetParamProfile_SecurityLevel_Type()
)
snmpv3TargetParamProfile_SecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpv3TargetParamProfile_SecurityLevel.setStatus("mandatory")


class _Snmpv3TargetParamProfile_Action_o_Type(Integer32):
    """Custom type snmpv3TargetParamProfile_Action_o based on Integer32"""
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


_Snmpv3TargetParamProfile_Action_o_Type.__name__ = "Integer32"
_Snmpv3TargetParamProfile_Action_o_Object = MibScalar
snmpv3TargetParamProfile_Action_o = _Snmpv3TargetParamProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 116, 1, 1, 7),
    _Snmpv3TargetParamProfile_Action_o_Type()
)
snmpv3TargetParamProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpv3TargetParamProfile_Action_o.setStatus("mandatory")
_Mibsnmpv3NotifyProfile_ObjectIdentity = ObjectIdentity
mibsnmpv3NotifyProfile = _Mibsnmpv3NotifyProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 117)
)
_Mibsnmpv3NotifyProfileTable_Object = MibTable
mibsnmpv3NotifyProfileTable = _Mibsnmpv3NotifyProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 117, 1)
)
if mibBuilder.loadTexts:
    mibsnmpv3NotifyProfileTable.setStatus("mandatory")
_Mibsnmpv3NotifyProfileEntry_Object = MibTableRow
mibsnmpv3NotifyProfileEntry = _Mibsnmpv3NotifyProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 117, 1, 1)
)
mibsnmpv3NotifyProfileEntry.setIndexNames(
    (0, "ASCEND-MIBSNMP-MIB", "snmpv3NotifyProfile-Name"),
)
if mibBuilder.loadTexts:
    mibsnmpv3NotifyProfileEntry.setStatus("mandatory")
_Snmpv3NotifyProfile_Name_Type = OctetString
_Snmpv3NotifyProfile_Name_Object = MibScalar
snmpv3NotifyProfile_Name = _Snmpv3NotifyProfile_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 117, 1, 1, 1),
    _Snmpv3NotifyProfile_Name_Type()
)
snmpv3NotifyProfile_Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpv3NotifyProfile_Name.setStatus("mandatory")


class _Snmpv3NotifyProfile_ActiveEnabled_Type(Integer32):
    """Custom type snmpv3NotifyProfile_ActiveEnabled based on Integer32"""
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


_Snmpv3NotifyProfile_ActiveEnabled_Type.__name__ = "Integer32"
_Snmpv3NotifyProfile_ActiveEnabled_Object = MibScalar
snmpv3NotifyProfile_ActiveEnabled = _Snmpv3NotifyProfile_ActiveEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 117, 1, 1, 2),
    _Snmpv3NotifyProfile_ActiveEnabled_Type()
)
snmpv3NotifyProfile_ActiveEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpv3NotifyProfile_ActiveEnabled.setStatus("mandatory")
_Snmpv3NotifyProfile_Tag_Type = OctetString
_Snmpv3NotifyProfile_Tag_Object = MibScalar
snmpv3NotifyProfile_Tag = _Snmpv3NotifyProfile_Tag_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 117, 1, 1, 3),
    _Snmpv3NotifyProfile_Tag_Type()
)
snmpv3NotifyProfile_Tag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpv3NotifyProfile_Tag.setStatus("mandatory")


class _Snmpv3NotifyProfile_Type_Type(Integer32):
    """Custom type snmpv3NotifyProfile_Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inform", 3),
          ("trap", 2))
    )


_Snmpv3NotifyProfile_Type_Type.__name__ = "Integer32"
_Snmpv3NotifyProfile_Type_Object = MibScalar
snmpv3NotifyProfile_Type = _Snmpv3NotifyProfile_Type_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 117, 1, 1, 4),
    _Snmpv3NotifyProfile_Type_Type()
)
snmpv3NotifyProfile_Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpv3NotifyProfile_Type.setStatus("mandatory")


class _Snmpv3NotifyProfile_Action_o_Type(Integer32):
    """Custom type snmpv3NotifyProfile_Action_o based on Integer32"""
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


_Snmpv3NotifyProfile_Action_o_Type.__name__ = "Integer32"
_Snmpv3NotifyProfile_Action_o_Object = MibScalar
snmpv3NotifyProfile_Action_o = _Snmpv3NotifyProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 117, 1, 1, 5),
    _Snmpv3NotifyProfile_Action_o_Type()
)
snmpv3NotifyProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpv3NotifyProfile_Action_o.setStatus("mandatory")
_MibsnmpManagerProfile_ObjectIdentity = ObjectIdentity
mibsnmpManagerProfile = _MibsnmpManagerProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 118)
)
_MibsnmpManagerProfileTable_Object = MibTable
mibsnmpManagerProfileTable = _MibsnmpManagerProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 118, 1)
)
if mibBuilder.loadTexts:
    mibsnmpManagerProfileTable.setStatus("mandatory")
_MibsnmpManagerProfileEntry_Object = MibTableRow
mibsnmpManagerProfileEntry = _MibsnmpManagerProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 118, 1, 1)
)
mibsnmpManagerProfileEntry.setIndexNames(
    (0, "ASCEND-MIBSNMP-MIB", "snmpManagerProfile-Name"),
)
if mibBuilder.loadTexts:
    mibsnmpManagerProfileEntry.setStatus("mandatory")
_SnmpManagerProfile_Name_Type = DisplayString
_SnmpManagerProfile_Name_Object = MibScalar
snmpManagerProfile_Name = _SnmpManagerProfile_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 118, 1, 1, 1),
    _SnmpManagerProfile_Name_Type()
)
snmpManagerProfile_Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpManagerProfile_Name.setStatus("mandatory")


class _SnmpManagerProfile_Active_Type(Integer32):
    """Custom type snmpManagerProfile_Active based on Integer32"""
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


_SnmpManagerProfile_Active_Type.__name__ = "Integer32"
_SnmpManagerProfile_Active_Object = MibScalar
snmpManagerProfile_Active = _SnmpManagerProfile_Active_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 118, 1, 1, 2),
    _SnmpManagerProfile_Active_Type()
)
snmpManagerProfile_Active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpManagerProfile_Active.setStatus("mandatory")


class _SnmpManagerProfile_WriteAccess_Type(Integer32):
    """Custom type snmpManagerProfile_WriteAccess based on Integer32"""
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


_SnmpManagerProfile_WriteAccess_Type.__name__ = "Integer32"
_SnmpManagerProfile_WriteAccess_Object = MibScalar
snmpManagerProfile_WriteAccess = _SnmpManagerProfile_WriteAccess_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 118, 1, 1, 3),
    _SnmpManagerProfile_WriteAccess_Type()
)
snmpManagerProfile_WriteAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpManagerProfile_WriteAccess.setStatus("mandatory")


class _SnmpManagerProfile_SnmpMessageType_Type(Integer32):
    """Custom type snmpManagerProfile_SnmpMessageType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v1AndV3", 1),
          ("v1Only", 2),
          ("v3Only", 3))
    )


_SnmpManagerProfile_SnmpMessageType_Type.__name__ = "Integer32"
_SnmpManagerProfile_SnmpMessageType_Object = MibScalar
snmpManagerProfile_SnmpMessageType = _SnmpManagerProfile_SnmpMessageType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 118, 1, 1, 4),
    _SnmpManagerProfile_SnmpMessageType_Type()
)
snmpManagerProfile_SnmpMessageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpManagerProfile_SnmpMessageType.setStatus("mandatory")


class _SnmpManagerProfile_Action_o_Type(Integer32):
    """Custom type snmpManagerProfile_Action_o based on Integer32"""
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


_SnmpManagerProfile_Action_o_Type.__name__ = "Integer32"
_SnmpManagerProfile_Action_o_Object = MibScalar
snmpManagerProfile_Action_o = _SnmpManagerProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 118, 1, 1, 5),
    _SnmpManagerProfile_Action_o_Type()
)
snmpManagerProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpManagerProfile_Action_o.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBSNMP-MIB",
    **{"DisplayString": DisplayString,
       "mibsnmpProfile": mibsnmpProfile,
       "mibsnmpProfileTable": mibsnmpProfileTable,
       "mibsnmpProfileEntry": mibsnmpProfileEntry,
       "snmpProfile-Index-o": snmpProfile_Index_o,
       "snmpProfile-Enabled": snmpProfile_Enabled,
       "snmpProfile-ReadCommunity": snmpProfile_ReadCommunity,
       "snmpProfile-ReadWriteEnabled": snmpProfile_ReadWriteEnabled,
       "snmpProfile-ReadWriteCommunity": snmpProfile_ReadWriteCommunity,
       "snmpProfile-EnforceAddressSecurity": snmpProfile_EnforceAddressSecurity,
       "snmpProfile-Contact": snmpProfile_Contact,
       "snmpProfile-Location": snmpProfile_Location,
       "snmpProfile-QueueDepth": snmpProfile_QueueDepth,
       "snmpProfile-CsmModemDiag": snmpProfile_CsmModemDiag,
       "snmpProfile-SnmpMessageType": snmpProfile_SnmpMessageType,
       "snmpProfile-SecurityLevel": snmpProfile_SecurityLevel,
       "snmpProfile-EnableVacm": snmpProfile_EnableVacm,
       "snmpProfile-Action-o": snmpProfile_Action_o,
       "snmpProfile-NotificationLogAgeOut": snmpProfile_NotificationLogAgeOut,
       "snmpProfile-EarlyQueueDiscard": snmpProfile_EarlyQueueDiscard,
       "snmpProfile-BitStringsAllowed": snmpProfile_BitStringsAllowed,
       "snmpProfile-AlarmClearTableLimit": snmpProfile_AlarmClearTableLimit,
       "mibusmUserProfile": mibusmUserProfile,
       "mibusmUserProfileTable": mibusmUserProfileTable,
       "mibusmUserProfileEntry": mibusmUserProfileEntry,
       "usmUserProfile-Name": usmUserProfile_Name,
       "usmUserProfile-ActiveEnabled": usmUserProfile_ActiveEnabled,
       "usmUserProfile-ReadWriteAccess": usmUserProfile_ReadWriteAccess,
       "usmUserProfile-AuthProtocol": usmUserProfile_AuthProtocol,
       "usmUserProfile-PrivProtocol": usmUserProfile_PrivProtocol,
       "usmUserProfile-AuthKey": usmUserProfile_AuthKey,
       "usmUserProfile-PrivKey": usmUserProfile_PrivKey,
       "usmUserProfile-Action-o": usmUserProfile_Action_o,
       "mibsnmpv3TargetParamProfile": mibsnmpv3TargetParamProfile,
       "mibsnmpv3TargetParamProfileTable": mibsnmpv3TargetParamProfileTable,
       "mibsnmpv3TargetParamProfileEntry": mibsnmpv3TargetParamProfileEntry,
       "snmpv3TargetParamProfile-Name": snmpv3TargetParamProfile_Name,
       "snmpv3TargetParamProfile-ActiveEnabled": snmpv3TargetParamProfile_ActiveEnabled,
       "snmpv3TargetParamProfile-MsgProcModel": snmpv3TargetParamProfile_MsgProcModel,
       "snmpv3TargetParamProfile-SecurityModel": snmpv3TargetParamProfile_SecurityModel,
       "snmpv3TargetParamProfile-SecurityName": snmpv3TargetParamProfile_SecurityName,
       "snmpv3TargetParamProfile-SecurityLevel": snmpv3TargetParamProfile_SecurityLevel,
       "snmpv3TargetParamProfile-Action-o": snmpv3TargetParamProfile_Action_o,
       "mibsnmpv3NotifyProfile": mibsnmpv3NotifyProfile,
       "mibsnmpv3NotifyProfileTable": mibsnmpv3NotifyProfileTable,
       "mibsnmpv3NotifyProfileEntry": mibsnmpv3NotifyProfileEntry,
       "snmpv3NotifyProfile-Name": snmpv3NotifyProfile_Name,
       "snmpv3NotifyProfile-ActiveEnabled": snmpv3NotifyProfile_ActiveEnabled,
       "snmpv3NotifyProfile-Tag": snmpv3NotifyProfile_Tag,
       "snmpv3NotifyProfile-Type": snmpv3NotifyProfile_Type,
       "snmpv3NotifyProfile-Action-o": snmpv3NotifyProfile_Action_o,
       "mibsnmpManagerProfile": mibsnmpManagerProfile,
       "mibsnmpManagerProfileTable": mibsnmpManagerProfileTable,
       "mibsnmpManagerProfileEntry": mibsnmpManagerProfileEntry,
       "snmpManagerProfile-Name": snmpManagerProfile_Name,
       "snmpManagerProfile-Active": snmpManagerProfile_Active,
       "snmpManagerProfile-WriteAccess": snmpManagerProfile_WriteAccess,
       "snmpManagerProfile-SnmpMessageType": snmpManagerProfile_SnmpMessageType,
       "snmpManagerProfile-Action-o": snmpManagerProfile_Action_o}
)
