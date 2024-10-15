# SNMP MIB module (ANS-COMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ANS-COMMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:55 2024
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



class TruthValue(Integer32):
    """Custom type TruthValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )





class PhysAddress(OctetString):
    """Custom type PhysAddress based on OctetString"""




class RowPointer(ObjectIdentifier):
    """Custom type RowPointer based on ObjectIdentifier"""




class RowStatus(Integer32):
    """Custom type RowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )





class DateAndTime(OctetString):
    """Custom type DateAndTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(11, 11),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ericsson_ObjectIdentity = ObjectIdentity
ericsson = _Ericsson_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193)
)
_Mlpmp_ObjectIdentity = ObjectIdentity
mlpmp = _Mlpmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 96)
)
_MlpmpR115_ObjectIdentity = ObjectIdentity
mlpmpR115 = _MlpmpR115_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 96, 115)
)
_Common_ObjectIdentity = ObjectIdentity
common = _Common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1)
)
_ErrorMessage_ObjectIdentity = ObjectIdentity
errorMessage = _ErrorMessage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 2)
)
_ErrorMessageTable_Object = MibTable
errorMessageTable = _ErrorMessageTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 2, 1)
)
if mibBuilder.loadTexts:
    errorMessageTable.setStatus("mandatory")
_ErrorMessageEntry_Object = MibTableRow
errorMessageEntry = _ErrorMessageEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 2, 1, 1)
)
errorMessageEntry.setIndexNames(
    (0, "ANS-COMMON-MIB", "errorMessageRequestId"),
)
if mibBuilder.loadTexts:
    errorMessageEntry.setStatus("mandatory")
_ErrorMessageRequestId_Type = Integer32
_ErrorMessageRequestId_Object = MibTableColumn
errorMessageRequestId = _ErrorMessageRequestId_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 2, 1, 1, 1),
    _ErrorMessageRequestId_Type()
)
errorMessageRequestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorMessageRequestId.setStatus("mandatory")
_ErrorMessageCode_Type = Integer32
_ErrorMessageCode_Object = MibTableColumn
errorMessageCode = _ErrorMessageCode_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 2, 1, 1, 2),
    _ErrorMessageCode_Type()
)
errorMessageCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorMessageCode.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ANS-COMMON-MIB",
    **{"TruthValue": TruthValue,
       "PhysAddress": PhysAddress,
       "RowPointer": RowPointer,
       "RowStatus": RowStatus,
       "DateAndTime": DateAndTime,
       "ericsson": ericsson,
       "mlpmp": mlpmp,
       "mlpmpR115": mlpmpR115,
       "common": common,
       "errorMessage": errorMessage,
       "errorMessageTable": errorMessageTable,
       "errorMessageEntry": errorMessageEntry,
       "errorMessageRequestId": errorMessageRequestId,
       "errorMessageCode": errorMessageCode}
)
