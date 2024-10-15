# SNMP MIB module (ONEACCESS-GDOI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ONEACCESS-GDOI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:54 2024
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

(oacExpIMManagement,) = mibBuilder.importSymbols(
    "ONEACCESS-GLOBAL-REG",
    "oacExpIMManagement")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

oacExpIMGdoiMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class OacGdoiIdentificationType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 2),
          ("keyID", 1))
    )



class OacGdoiIdentificationValue(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class OacGdoiSPI(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )



class OacGdoiKEKEncryptionAlgorithm(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enc-3des", 2),
          ("enc-aes", 3),
          ("enc-des", 1))
    )



class OacGdoiHashAlogrithm(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("md5", 1),
          ("sha1", 2))
    )



class OacGdoiSignatureMethod(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dss", 2),
          ("ecdss", 3),
          ("rsa", 1))
    )



# MIB Managed Objects in the order of their OIDs

_OacGdoiMIBObjects_ObjectIdentity = ObjectIdentity
oacGdoiMIBObjects = _OacGdoiMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1)
)
_OacGdoiGroupTable_Object = MibTable
oacGdoiGroupTable = _OacGdoiGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 1)
)
if mibBuilder.loadTexts:
    oacGdoiGroupTable.setStatus("current")
_OacGdoiGroupEntry_Object = MibTableRow
oacGdoiGroupEntry = _OacGdoiGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 1, 1)
)
oacGdoiGroupEntry.setIndexNames(
    (0, "ONEACCESS-GDOI-MIB", "oacGdoiGroupName"),
)
if mibBuilder.loadTexts:
    oacGdoiGroupEntry.setStatus("current")
_OacGdoiGroupName_Type = DisplayString
_OacGdoiGroupName_Object = MibTableColumn
oacGdoiGroupName = _OacGdoiGroupName_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 1, 1, 1),
    _OacGdoiGroupName_Type()
)
oacGdoiGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacGdoiGroupName.setStatus("current")
_OacGdoiGroupIdType_Type = OacGdoiIdentificationType
_OacGdoiGroupIdType_Object = MibTableColumn
oacGdoiGroupIdType = _OacGdoiGroupIdType_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 1, 1, 2),
    _OacGdoiGroupIdType_Type()
)
oacGdoiGroupIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacGdoiGroupIdType.setStatus("current")
_OacGdoiGroupIdValue_Type = OacGdoiIdentificationValue
_OacGdoiGroupIdValue_Object = MibTableColumn
oacGdoiGroupIdValue = _OacGdoiGroupIdValue_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 1, 1, 3),
    _OacGdoiGroupIdValue_Type()
)
oacGdoiGroupIdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacGdoiGroupIdValue.setStatus("current")
_OacGdoiGm_ObjectIdentity = ObjectIdentity
oacGdoiGm = _OacGdoiGm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 2)
)
_OacGdoiGmTable_Object = MibTable
oacGdoiGmTable = _OacGdoiGmTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 2, 2)
)
if mibBuilder.loadTexts:
    oacGdoiGmTable.setStatus("current")
_OacGdoiGmEntry_Object = MibTableRow
oacGdoiGmEntry = _OacGdoiGmEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 2, 2, 1)
)
oacGdoiGmEntry.setIndexNames(
    (0, "ONEACCESS-GDOI-MIB", "oacGdoiGroupName"),
    (0, "ONEACCESS-GDOI-MIB", "oacGdoiGmActiveKEK"),
)
if mibBuilder.loadTexts:
    oacGdoiGmEntry.setStatus("current")
_OacGdoiGmIdType_Type = OacGdoiIdentificationType
_OacGdoiGmIdType_Object = MibTableColumn
oacGdoiGmIdType = _OacGdoiGmIdType_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 2, 2, 1, 1),
    _OacGdoiGmIdType_Type()
)
oacGdoiGmIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacGdoiGmIdType.setStatus("current")
_OacGdoiGmIdValue_Type = OacGdoiIdentificationValue
_OacGdoiGmIdValue_Object = MibTableColumn
oacGdoiGmIdValue = _OacGdoiGmIdValue_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 2, 2, 1, 2),
    _OacGdoiGmIdValue_Type()
)
oacGdoiGmIdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacGdoiGmIdValue.setStatus("current")
_OacGdoiGmRegKeyServerIdValue_Type = OacGdoiIdentificationValue
_OacGdoiGmRegKeyServerIdValue_Object = MibTableColumn
oacGdoiGmRegKeyServerIdValue = _OacGdoiGmRegKeyServerIdValue_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 2, 2, 1, 3),
    _OacGdoiGmRegKeyServerIdValue_Type()
)
oacGdoiGmRegKeyServerIdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacGdoiGmRegKeyServerIdValue.setStatus("current")
_OacGdoiGmActiveKEK_Type = OacGdoiSPI
_OacGdoiGmActiveKEK_Object = MibTableColumn
oacGdoiGmActiveKEK = _OacGdoiGmActiveKEK_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 2, 2, 1, 4),
    _OacGdoiGmActiveKEK_Type()
)
oacGdoiGmActiveKEK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacGdoiGmActiveKEK.setStatus("current")
_OacGdoiGmRekeysReceived_Type = Counter32
_OacGdoiGmRekeysReceived_Object = MibTableColumn
oacGdoiGmRekeysReceived = _OacGdoiGmRekeysReceived_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 2, 2, 1, 5),
    _OacGdoiGmRekeysReceived_Type()
)
oacGdoiGmRekeysReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacGdoiGmRekeysReceived.setStatus("current")
if mibBuilder.loadTexts:
    oacGdoiGmRekeysReceived.setUnits("GROUPKEY-PUSH Messages")
_OacGdoiPolicy_ObjectIdentity = ObjectIdentity
oacGdoiPolicy = _OacGdoiPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 3)
)
_OacGdoiGmKekTable_Object = MibTable
oacGdoiGmKekTable = _OacGdoiGmKekTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 3, 2)
)
if mibBuilder.loadTexts:
    oacGdoiGmKekTable.setStatus("current")
_OacGdoiGmKekEntry_Object = MibTableRow
oacGdoiGmKekEntry = _OacGdoiGmKekEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 3, 2, 1)
)
oacGdoiGmKekEntry.setIndexNames(
    (0, "ONEACCESS-GDOI-MIB", "oacGdoiGroupName"),
    (0, "ONEACCESS-GDOI-MIB", "oacGdoiGmKekSPI"),
)
if mibBuilder.loadTexts:
    oacGdoiGmKekEntry.setStatus("current")
_OacGdoiGmKekSPI_Type = OacGdoiSPI
_OacGdoiGmKekSPI_Object = MibTableColumn
oacGdoiGmKekSPI = _OacGdoiGmKekSPI_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 3, 2, 1, 1),
    _OacGdoiGmKekSPI_Type()
)
oacGdoiGmKekSPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacGdoiGmKekSPI.setStatus("current")
_OacGdoiGmKekSrcIdValue_Type = OacGdoiIdentificationValue
_OacGdoiGmKekSrcIdValue_Object = MibTableColumn
oacGdoiGmKekSrcIdValue = _OacGdoiGmKekSrcIdValue_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 3, 2, 1, 2),
    _OacGdoiGmKekSrcIdValue_Type()
)
oacGdoiGmKekSrcIdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacGdoiGmKekSrcIdValue.setStatus("current")
_OacGdoiGmKekDstIdValue_Type = OacGdoiIdentificationValue
_OacGdoiGmKekDstIdValue_Object = MibTableColumn
oacGdoiGmKekDstIdValue = _OacGdoiGmKekDstIdValue_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 3, 2, 1, 3),
    _OacGdoiGmKekDstIdValue_Type()
)
oacGdoiGmKekDstIdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacGdoiGmKekDstIdValue.setStatus("current")
_OacGdoiGmKekEncryptAlg_Type = OacGdoiKEKEncryptionAlgorithm
_OacGdoiGmKekEncryptAlg_Object = MibTableColumn
oacGdoiGmKekEncryptAlg = _OacGdoiGmKekEncryptAlg_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 3, 2, 1, 4),
    _OacGdoiGmKekEncryptAlg_Type()
)
oacGdoiGmKekEncryptAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacGdoiGmKekEncryptAlg.setStatus("current")
_OacGdoiGmKekEncryptKeyLength_Type = Unsigned32
_OacGdoiGmKekEncryptKeyLength_Object = MibTableColumn
oacGdoiGmKekEncryptKeyLength = _OacGdoiGmKekEncryptKeyLength_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 3, 2, 1, 5),
    _OacGdoiGmKekEncryptKeyLength_Type()
)
oacGdoiGmKekEncryptKeyLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacGdoiGmKekEncryptKeyLength.setStatus("current")
if mibBuilder.loadTexts:
    oacGdoiGmKekEncryptKeyLength.setUnits("Bits")
_OacGdoiGmKekSigHashAlg_Type = OacGdoiHashAlogrithm
_OacGdoiGmKekSigHashAlg_Object = MibTableColumn
oacGdoiGmKekSigHashAlg = _OacGdoiGmKekSigHashAlg_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 3, 2, 1, 6),
    _OacGdoiGmKekSigHashAlg_Type()
)
oacGdoiGmKekSigHashAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacGdoiGmKekSigHashAlg.setStatus("current")
_OacGdoiGmKekSigAlg_Type = OacGdoiSignatureMethod
_OacGdoiGmKekSigAlg_Object = MibTableColumn
oacGdoiGmKekSigAlg = _OacGdoiGmKekSigAlg_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 3, 2, 1, 7),
    _OacGdoiGmKekSigAlg_Type()
)
oacGdoiGmKekSigAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacGdoiGmKekSigAlg.setStatus("current")
_OacGdoiGmKekSigKeyLength_Type = Unsigned32
_OacGdoiGmKekSigKeyLength_Object = MibTableColumn
oacGdoiGmKekSigKeyLength = _OacGdoiGmKekSigKeyLength_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 3, 2, 1, 8),
    _OacGdoiGmKekSigKeyLength_Type()
)
oacGdoiGmKekSigKeyLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacGdoiGmKekSigKeyLength.setStatus("current")
if mibBuilder.loadTexts:
    oacGdoiGmKekSigKeyLength.setUnits("Bits")
_OacGdoiGmKekOriginalLifetime_Type = Unsigned32
_OacGdoiGmKekOriginalLifetime_Object = MibTableColumn
oacGdoiGmKekOriginalLifetime = _OacGdoiGmKekOriginalLifetime_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 3, 2, 1, 9),
    _OacGdoiGmKekOriginalLifetime_Type()
)
oacGdoiGmKekOriginalLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacGdoiGmKekOriginalLifetime.setStatus("current")
if mibBuilder.loadTexts:
    oacGdoiGmKekOriginalLifetime.setUnits("Seconds")
_OacGdoiGmKekRemainingLifetime_Type = Unsigned32
_OacGdoiGmKekRemainingLifetime_Object = MibTableColumn
oacGdoiGmKekRemainingLifetime = _OacGdoiGmKekRemainingLifetime_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 3, 2, 1, 10),
    _OacGdoiGmKekRemainingLifetime_Type()
)
oacGdoiGmKekRemainingLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacGdoiGmKekRemainingLifetime.setStatus("current")
if mibBuilder.loadTexts:
    oacGdoiGmKekRemainingLifetime.setUnits("Seconds")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ONEACCESS-GDOI-MIB",
    **{"OacGdoiIdentificationType": OacGdoiIdentificationType,
       "OacGdoiIdentificationValue": OacGdoiIdentificationValue,
       "OacGdoiSPI": OacGdoiSPI,
       "OacGdoiKEKEncryptionAlgorithm": OacGdoiKEKEncryptionAlgorithm,
       "OacGdoiHashAlogrithm": OacGdoiHashAlogrithm,
       "OacGdoiSignatureMethod": OacGdoiSignatureMethod,
       "oacExpIMGdoiMIB": oacExpIMGdoiMIB,
       "oacGdoiMIBObjects": oacGdoiMIBObjects,
       "oacGdoiGroupTable": oacGdoiGroupTable,
       "oacGdoiGroupEntry": oacGdoiGroupEntry,
       "oacGdoiGroupName": oacGdoiGroupName,
       "oacGdoiGroupIdType": oacGdoiGroupIdType,
       "oacGdoiGroupIdValue": oacGdoiGroupIdValue,
       "oacGdoiGm": oacGdoiGm,
       "oacGdoiGmTable": oacGdoiGmTable,
       "oacGdoiGmEntry": oacGdoiGmEntry,
       "oacGdoiGmIdType": oacGdoiGmIdType,
       "oacGdoiGmIdValue": oacGdoiGmIdValue,
       "oacGdoiGmRegKeyServerIdValue": oacGdoiGmRegKeyServerIdValue,
       "oacGdoiGmActiveKEK": oacGdoiGmActiveKEK,
       "oacGdoiGmRekeysReceived": oacGdoiGmRekeysReceived,
       "oacGdoiPolicy": oacGdoiPolicy,
       "oacGdoiGmKekTable": oacGdoiGmKekTable,
       "oacGdoiGmKekEntry": oacGdoiGmKekEntry,
       "oacGdoiGmKekSPI": oacGdoiGmKekSPI,
       "oacGdoiGmKekSrcIdValue": oacGdoiGmKekSrcIdValue,
       "oacGdoiGmKekDstIdValue": oacGdoiGmKekDstIdValue,
       "oacGdoiGmKekEncryptAlg": oacGdoiGmKekEncryptAlg,
       "oacGdoiGmKekEncryptKeyLength": oacGdoiGmKekEncryptKeyLength,
       "oacGdoiGmKekSigHashAlg": oacGdoiGmKekSigHashAlg,
       "oacGdoiGmKekSigAlg": oacGdoiGmKekSigAlg,
       "oacGdoiGmKekSigKeyLength": oacGdoiGmKekSigKeyLength,
       "oacGdoiGmKekOriginalLifetime": oacGdoiGmKekOriginalLifetime,
       "oacGdoiGmKekRemainingLifetime": oacGdoiGmKekRemainingLifetime}
)
