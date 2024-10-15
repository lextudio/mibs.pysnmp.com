# SNMP MIB module (QWESCOM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/QWESCOM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:41:07 2024
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class PhysAddress(OctetString):
    """Custom type PhysAddress based on OctetString"""




class TimeDateString(Integer32):
    """Custom type TimeDateString based on Integer32"""




class Boolean(Integer32):
    """Custom type Boolean based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Qwescom_ObjectIdentity = ObjectIdentity
qwescom = _Qwescom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3662)
)
_OemTree_ObjectIdentity = ObjectIdentity
oemTree = _OemTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3662, 3662)
)
_Oem_ObjectIdentity = ObjectIdentity
oem = _Oem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662)
)
_QproprietaryMib2_ObjectIdentity = ObjectIdentity
qproprietaryMib2 = _QproprietaryMib2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 1)
)
_Qsnmp_ObjectIdentity = ObjectIdentity
qsnmp = _Qsnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 1, 11)
)
_QsnmpCommunityTable_Object = MibTable
qsnmpCommunityTable = _QsnmpCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 1, 11, 1)
)
if mibBuilder.loadTexts:
    qsnmpCommunityTable.setStatus("mandatory")
_QsnmpCommunityEntry_Object = MibTableRow
qsnmpCommunityEntry = _QsnmpCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 1, 11, 1, 1)
)
qsnmpCommunityEntry.setIndexNames(
    (0, "QWESCOM-MIB", "qsnmpCommunityIndex"),
)
if mibBuilder.loadTexts:
    qsnmpCommunityEntry.setStatus("mandatory")


class _QsnmpCommunityIndex_Type(Integer32):
    """Custom type qsnmpCommunityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_QsnmpCommunityIndex_Type.__name__ = "Integer32"
_QsnmpCommunityIndex_Object = MibTableColumn
qsnmpCommunityIndex = _QsnmpCommunityIndex_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 1, 11, 1, 1, 1),
    _QsnmpCommunityIndex_Type()
)
qsnmpCommunityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsnmpCommunityIndex.setStatus("mandatory")


class _QsnmpCommunityRights_Type(Integer32):
    """Custom type qsnmpCommunityRights based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("readonly", 0),
          ("readwrite", 1))
    )


_QsnmpCommunityRights_Type.__name__ = "Integer32"
_QsnmpCommunityRights_Object = MibTableColumn
qsnmpCommunityRights = _QsnmpCommunityRights_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 1, 11, 1, 1, 2),
    _QsnmpCommunityRights_Type()
)
qsnmpCommunityRights.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsnmpCommunityRights.setStatus("optional")


class _QsnmpCommunityName_Type(DisplayString):
    """Custom type qsnmpCommunityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QsnmpCommunityName_Type.__name__ = "DisplayString"
_QsnmpCommunityName_Object = MibTableColumn
qsnmpCommunityName = _QsnmpCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 1, 11, 1, 1, 3),
    _QsnmpCommunityName_Type()
)
qsnmpCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qsnmpCommunityName.setStatus("mandatory")
_QsnmpNMSTable_Object = MibTable
qsnmpNMSTable = _QsnmpNMSTable_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 1, 11, 2)
)
if mibBuilder.loadTexts:
    qsnmpNMSTable.setStatus("mandatory")
_QsnmpNMSEntry_Object = MibTableRow
qsnmpNMSEntry = _QsnmpNMSEntry_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 1, 11, 2, 1)
)
qsnmpNMSEntry.setIndexNames(
    (0, "QWESCOM-MIB", "qsnmpNMSIndex"),
)
if mibBuilder.loadTexts:
    qsnmpNMSEntry.setStatus("mandatory")


class _QsnmpNMSIndex_Type(Integer32):
    """Custom type qsnmpNMSIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_QsnmpNMSIndex_Type.__name__ = "Integer32"
_QsnmpNMSIndex_Object = MibTableColumn
qsnmpNMSIndex = _QsnmpNMSIndex_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 1, 11, 2, 1, 1),
    _QsnmpNMSIndex_Type()
)
qsnmpNMSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsnmpNMSIndex.setStatus("mandatory")
_QsnmpNMSIpAddress_Type = IpAddress
_QsnmpNMSIpAddress_Object = MibTableColumn
qsnmpNMSIpAddress = _QsnmpNMSIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 1, 11, 2, 1, 2),
    _QsnmpNMSIpAddress_Type()
)
qsnmpNMSIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qsnmpNMSIpAddress.setStatus("mandatory")
_QsnmpTrapTable_Object = MibTable
qsnmpTrapTable = _QsnmpTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 1, 11, 3)
)
if mibBuilder.loadTexts:
    qsnmpTrapTable.setStatus("mandatory")
_QsnmpTrapEntry_Object = MibTableRow
qsnmpTrapEntry = _QsnmpTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 1, 11, 3, 1)
)
qsnmpTrapEntry.setIndexNames(
    (0, "QWESCOM-MIB", "qsnmpTrapIndex"),
)
if mibBuilder.loadTexts:
    qsnmpTrapEntry.setStatus("mandatory")


class _QsnmpTrapIndex_Type(Integer32):
    """Custom type qsnmpTrapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_QsnmpTrapIndex_Type.__name__ = "Integer32"
_QsnmpTrapIndex_Object = MibTableColumn
qsnmpTrapIndex = _QsnmpTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 1, 11, 3, 1, 1),
    _QsnmpTrapIndex_Type()
)
qsnmpTrapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qsnmpTrapIndex.setStatus("mandatory")
_QsnmpTrapIpAddress_Type = IpAddress
_QsnmpTrapIpAddress_Object = MibTableColumn
qsnmpTrapIpAddress = _QsnmpTrapIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 1, 11, 3, 1, 2),
    _QsnmpTrapIpAddress_Type()
)
qsnmpTrapIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qsnmpTrapIpAddress.setStatus("mandatory")


class _QsnmpForwardTrap_Type(Integer32):
    """Custom type qsnmpForwardTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_QsnmpForwardTrap_Type.__name__ = "Integer32"
_QsnmpForwardTrap_Object = MibScalar
qsnmpForwardTrap = _QsnmpForwardTrap_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 1, 11, 4),
    _QsnmpForwardTrap_Type()
)
qsnmpForwardTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qsnmpForwardTrap.setStatus("mandatory")
_Qproducts_ObjectIdentity = ObjectIdentity
qproducts = _Qproducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 2)
)
_Qslots_ObjectIdentity = ObjectIdentity
qslots = _Qslots_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 3)
)
_QFlowClass_ObjectIdentity = ObjectIdentity
qFlowClass = _QFlowClass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4)
)
_QClassDefinitionMaxEntries_Type = Counter32
_QClassDefinitionMaxEntries_Object = MibScalar
qClassDefinitionMaxEntries = _QClassDefinitionMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 1),
    _QClassDefinitionMaxEntries_Type()
)
qClassDefinitionMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qClassDefinitionMaxEntries.setStatus("mandatory")
_QClassDefinitionTable_Object = MibTable
qClassDefinitionTable = _QClassDefinitionTable_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 2)
)
if mibBuilder.loadTexts:
    qClassDefinitionTable.setStatus("mandatory")
_QClassDefinitionEntry_Object = MibTableRow
qClassDefinitionEntry = _QClassDefinitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 2, 1)
)
qClassDefinitionEntry.setIndexNames(
    (0, "QWESCOM-MIB", "qClassDefinitionIndex"),
)
if mibBuilder.loadTexts:
    qClassDefinitionEntry.setStatus("mandatory")


class _QClassDefinitionIndex_Type(Integer32):
    """Custom type qClassDefinitionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 1024),
    )


_QClassDefinitionIndex_Type.__name__ = "Integer32"
_QClassDefinitionIndex_Object = MibTableColumn
qClassDefinitionIndex = _QClassDefinitionIndex_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 2, 1, 1),
    _QClassDefinitionIndex_Type()
)
qClassDefinitionIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qClassDefinitionIndex.setStatus("mandatory")


class _QClassDefinitionAlias_Type(DisplayString):
    """Custom type qClassDefinitionAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QClassDefinitionAlias_Type.__name__ = "DisplayString"
_QClassDefinitionAlias_Object = MibTableColumn
qClassDefinitionAlias = _QClassDefinitionAlias_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 2, 1, 2),
    _QClassDefinitionAlias_Type()
)
qClassDefinitionAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qClassDefinitionAlias.setStatus("optional")


class _QClassDefinitionParentClassID_Type(Integer32):
    """Custom type qClassDefinitionParentClassID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_QClassDefinitionParentClassID_Type.__name__ = "Integer32"
_QClassDefinitionParentClassID_Object = MibTableColumn
qClassDefinitionParentClassID = _QClassDefinitionParentClassID_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 2, 1, 3),
    _QClassDefinitionParentClassID_Type()
)
qClassDefinitionParentClassID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qClassDefinitionParentClassID.setStatus("optional")


class _QClassDefinitionFlowType_Type(Integer32):
    """Custom type qClassDefinitionFlowType based on Integer32"""
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
        *(("dsegress", 3),
          ("dsingres", 2),
          ("dsnode", 4),
          ("invalid", 5),
          ("normal", 1))
    )


_QClassDefinitionFlowType_Type.__name__ = "Integer32"
_QClassDefinitionFlowType_Object = MibTableColumn
qClassDefinitionFlowType = _QClassDefinitionFlowType_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 2, 1, 4),
    _QClassDefinitionFlowType_Type()
)
qClassDefinitionFlowType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qClassDefinitionFlowType.setStatus("mandatory")
_QClassDefinitionSourceIPMask_Type = IpAddress
_QClassDefinitionSourceIPMask_Object = MibTableColumn
qClassDefinitionSourceIPMask = _QClassDefinitionSourceIPMask_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 2, 1, 5),
    _QClassDefinitionSourceIPMask_Type()
)
qClassDefinitionSourceIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qClassDefinitionSourceIPMask.setStatus("optional")
_QClassDefinitionSourceIPLowerBound_Type = IpAddress
_QClassDefinitionSourceIPLowerBound_Object = MibTableColumn
qClassDefinitionSourceIPLowerBound = _QClassDefinitionSourceIPLowerBound_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 2, 1, 6),
    _QClassDefinitionSourceIPLowerBound_Type()
)
qClassDefinitionSourceIPLowerBound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qClassDefinitionSourceIPLowerBound.setStatus("optional")
_QClassDefinitionSourceIPUpperBound_Type = IpAddress
_QClassDefinitionSourceIPUpperBound_Object = MibTableColumn
qClassDefinitionSourceIPUpperBound = _QClassDefinitionSourceIPUpperBound_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 2, 1, 7),
    _QClassDefinitionSourceIPUpperBound_Type()
)
qClassDefinitionSourceIPUpperBound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qClassDefinitionSourceIPUpperBound.setStatus("optional")
_QClassDefinitionDestIPMask_Type = IpAddress
_QClassDefinitionDestIPMask_Object = MibTableColumn
qClassDefinitionDestIPMask = _QClassDefinitionDestIPMask_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 2, 1, 8),
    _QClassDefinitionDestIPMask_Type()
)
qClassDefinitionDestIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qClassDefinitionDestIPMask.setStatus("optional")
_QClassDefinitionDestIPLowerBound_Type = IpAddress
_QClassDefinitionDestIPLowerBound_Object = MibTableColumn
qClassDefinitionDestIPLowerBound = _QClassDefinitionDestIPLowerBound_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 2, 1, 9),
    _QClassDefinitionDestIPLowerBound_Type()
)
qClassDefinitionDestIPLowerBound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qClassDefinitionDestIPLowerBound.setStatus("optional")
_QClassDefinitionDestIPUpperBound_Type = IpAddress
_QClassDefinitionDestIPUpperBound_Object = MibTableColumn
qClassDefinitionDestIPUpperBound = _QClassDefinitionDestIPUpperBound_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 2, 1, 10),
    _QClassDefinitionDestIPUpperBound_Type()
)
qClassDefinitionDestIPUpperBound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qClassDefinitionDestIPUpperBound.setStatus("optional")


class _QClassDefinitionDSMask_Type(Integer32):
    """Custom type qClassDefinitionDSMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QClassDefinitionDSMask_Type.__name__ = "Integer32"
_QClassDefinitionDSMask_Object = MibTableColumn
qClassDefinitionDSMask = _QClassDefinitionDSMask_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 2, 1, 11),
    _QClassDefinitionDSMask_Type()
)
qClassDefinitionDSMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qClassDefinitionDSMask.setStatus("optional")


class _QClassDefinitionDSLowerBound_Type(Integer32):
    """Custom type qClassDefinitionDSLowerBound based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QClassDefinitionDSLowerBound_Type.__name__ = "Integer32"
_QClassDefinitionDSLowerBound_Object = MibTableColumn
qClassDefinitionDSLowerBound = _QClassDefinitionDSLowerBound_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 2, 1, 12),
    _QClassDefinitionDSLowerBound_Type()
)
qClassDefinitionDSLowerBound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qClassDefinitionDSLowerBound.setStatus("optional")


class _QClassDefinitionDSUpperBound_Type(Integer32):
    """Custom type qClassDefinitionDSUpperBound based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QClassDefinitionDSUpperBound_Type.__name__ = "Integer32"
_QClassDefinitionDSUpperBound_Object = MibTableColumn
qClassDefinitionDSUpperBound = _QClassDefinitionDSUpperBound_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 2, 1, 13),
    _QClassDefinitionDSUpperBound_Type()
)
qClassDefinitionDSUpperBound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qClassDefinitionDSUpperBound.setStatus("optional")


class _QClassDefinitionWellKnownApplication_Type(Integer32):
    """Custom type qClassDefinitionWellKnownApplication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
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
              61)
        )
    )
    namedValues = NamedValues(
        *(("appletalk", 47),
          ("audiomail", 55),
          ("audionews", 35),
          ("authentication", 34),
          ("autodesk", 57),
          ("bootp", 21),
          ("ciscofna", 40),
          ("ciscosys", 42),
          ("ciscotna", 41),
          ("daytime", 5),
          ("discard", 4),
          ("dns", 19),
          ("doom", 53),
          ("echo", 3),
          ("finger", 24),
          ("ftp", 8),
          ("gopher", 23),
          ("hostname", 28),
          ("http", 25),
          ("ibm", 58),
          ("ipx", 48),
          ("isotsap", 29),
          ("kerberos", 26),
          ("ldap", 50),
          ("login", 16),
          ("lotusnotes", 54),
          ("management", 45),
          ("microsoft", 52),
          ("msg", 11),
          ("msp", 7),
          ("netbios", 43),
          ("netmeeting", 2),
          ("networktime", 38),
          ("news", 44),
          ("novell", 51),
          ("npp", 27),
          ("oracle", 60),
          ("performancedata", 49),
          ("pop3", 32),
          ("pwdgen", 39),
          ("quoteofday", 6),
          ("rap", 13),
          ("realaudio", 1),
          ("remotemail", 17),
          ("remotetelnet", 30),
          ("rip", 5),
          ("rlp", 14),
          ("rpc", 33),
          ("send", 46),
          ("sftp", 36),
          ("smtp", 10),
          ("sna", 31),
          ("sql", 20),
          ("telnet", 9),
          ("tftp", 22),
          ("time", 12),
          ("unspecified", 0),
          ("uucp", 37),
          ("videomail", 56),
          ("vlsi", 59),
          ("whois", 15),
          ("xns", 18),
          ("xwindows", 61))
    )


_QClassDefinitionWellKnownApplication_Type.__name__ = "Integer32"
_QClassDefinitionWellKnownApplication_Object = MibTableColumn
qClassDefinitionWellKnownApplication = _QClassDefinitionWellKnownApplication_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 2, 1, 14),
    _QClassDefinitionWellKnownApplication_Type()
)
qClassDefinitionWellKnownApplication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qClassDefinitionWellKnownApplication.setStatus("mandatory")


class _QClassDefinitionProtocol_Type(Integer32):
    """Custom type qClassDefinitionProtocol based on Integer32"""
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("all", 0),
          ("arp", 5),
          ("egp", 7),
          ("icmp", 4),
          ("idrp", 11),
          ("igrp", 17),
          ("ipinip", 8),
          ("isoip", 13),
          ("isotp4", 10),
          ("nsfnetigp", 16),
          ("ospfigp", 18),
          ("pvp", 12),
          ("rdp", 9),
          ("rsvp", 6),
          ("tcp", 3),
          ("ttp", 15),
          ("udp", 2),
          ("udptcp", 1),
          ("vines", 14))
    )


_QClassDefinitionProtocol_Type.__name__ = "Integer32"
_QClassDefinitionProtocol_Object = MibTableColumn
qClassDefinitionProtocol = _QClassDefinitionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 2, 1, 15),
    _QClassDefinitionProtocol_Type()
)
qClassDefinitionProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qClassDefinitionProtocol.setStatus("mandatory")


class _QClassDefinitionSourcePortLowerBound_Type(Integer32):
    """Custom type qClassDefinitionSourcePortLowerBound based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QClassDefinitionSourcePortLowerBound_Type.__name__ = "Integer32"
_QClassDefinitionSourcePortLowerBound_Object = MibTableColumn
qClassDefinitionSourcePortLowerBound = _QClassDefinitionSourcePortLowerBound_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 2, 1, 16),
    _QClassDefinitionSourcePortLowerBound_Type()
)
qClassDefinitionSourcePortLowerBound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qClassDefinitionSourcePortLowerBound.setStatus("optional")


class _QClassDefinitionSourcePortUpperBound_Type(Integer32):
    """Custom type qClassDefinitionSourcePortUpperBound based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QClassDefinitionSourcePortUpperBound_Type.__name__ = "Integer32"
_QClassDefinitionSourcePortUpperBound_Object = MibTableColumn
qClassDefinitionSourcePortUpperBound = _QClassDefinitionSourcePortUpperBound_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 2, 1, 17),
    _QClassDefinitionSourcePortUpperBound_Type()
)
qClassDefinitionSourcePortUpperBound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qClassDefinitionSourcePortUpperBound.setStatus("optional")


class _QClassDefinitionDestPortLowerBound_Type(Integer32):
    """Custom type qClassDefinitionDestPortLowerBound based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QClassDefinitionDestPortLowerBound_Type.__name__ = "Integer32"
_QClassDefinitionDestPortLowerBound_Object = MibTableColumn
qClassDefinitionDestPortLowerBound = _QClassDefinitionDestPortLowerBound_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 2, 1, 18),
    _QClassDefinitionDestPortLowerBound_Type()
)
qClassDefinitionDestPortLowerBound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qClassDefinitionDestPortLowerBound.setStatus("optional")


class _QClassDefinitionDestPortUpperBound_Type(Integer32):
    """Custom type qClassDefinitionDestPortUpperBound based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QClassDefinitionDestPortUpperBound_Type.__name__ = "Integer32"
_QClassDefinitionDestPortUpperBound_Object = MibTableColumn
qClassDefinitionDestPortUpperBound = _QClassDefinitionDestPortUpperBound_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 2, 1, 19),
    _QClassDefinitionDestPortUpperBound_Type()
)
qClassDefinitionDestPortUpperBound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qClassDefinitionDestPortUpperBound.setStatus("optional")


class _QClassDefinitionFlowAgingTime_Type(Integer32):
    """Custom type qClassDefinitionFlowAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QClassDefinitionFlowAgingTime_Type.__name__ = "Integer32"
_QClassDefinitionFlowAgingTime_Object = MibTableColumn
qClassDefinitionFlowAgingTime = _QClassDefinitionFlowAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 2, 1, 20),
    _QClassDefinitionFlowAgingTime_Type()
)
qClassDefinitionFlowAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qClassDefinitionFlowAgingTime.setStatus("mandatory")


class _QPolicyDefinitionMaxEntries_Type(Integer32):
    """Custom type qPolicyDefinitionMaxEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QPolicyDefinitionMaxEntries_Type.__name__ = "Integer32"
_QPolicyDefinitionMaxEntries_Object = MibScalar
qPolicyDefinitionMaxEntries = _QPolicyDefinitionMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 3),
    _QPolicyDefinitionMaxEntries_Type()
)
qPolicyDefinitionMaxEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qPolicyDefinitionMaxEntries.setStatus("mandatory")
_QPolicyDefinitionTable_Object = MibTable
qPolicyDefinitionTable = _QPolicyDefinitionTable_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 4)
)
if mibBuilder.loadTexts:
    qPolicyDefinitionTable.setStatus("mandatory")
_QPolicyDefinitionEntry_Object = MibTableRow
qPolicyDefinitionEntry = _QPolicyDefinitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 4, 1)
)
qPolicyDefinitionEntry.setIndexNames(
    (0, "QWESCOM-MIB", "qPolicyDefinitionIndex"),
)
if mibBuilder.loadTexts:
    qPolicyDefinitionEntry.setStatus("mandatory")


class _QPolicyDefinitionIndex_Type(Integer32):
    """Custom type qPolicyDefinitionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 1024),
    )


_QPolicyDefinitionIndex_Type.__name__ = "Integer32"
_QPolicyDefinitionIndex_Object = MibTableColumn
qPolicyDefinitionIndex = _QPolicyDefinitionIndex_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 4, 1, 1),
    _QPolicyDefinitionIndex_Type()
)
qPolicyDefinitionIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qPolicyDefinitionIndex.setStatus("mandatory")


class _QPolicyDefinitionAlias_Type(DisplayString):
    """Custom type qPolicyDefinitionAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QPolicyDefinitionAlias_Type.__name__ = "DisplayString"
_QPolicyDefinitionAlias_Object = MibTableColumn
qPolicyDefinitionAlias = _QPolicyDefinitionAlias_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 4, 1, 2),
    _QPolicyDefinitionAlias_Type()
)
qPolicyDefinitionAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qPolicyDefinitionAlias.setStatus("optional")


class _QPolicyDefinitionType_Type(Integer32):
    """Custom type qPolicyDefinitionType based on Integer32"""
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
        *(("delete", 6),
          ("discard", 5),
          ("dsegress", 4),
          ("dsingress", 2),
          ("dsnode", 3),
          ("normal", 1))
    )


_QPolicyDefinitionType_Type.__name__ = "Integer32"
_QPolicyDefinitionType_Object = MibTableColumn
qPolicyDefinitionType = _QPolicyDefinitionType_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 4, 1, 3),
    _QPolicyDefinitionType_Type()
)
qPolicyDefinitionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qPolicyDefinitionType.setStatus("optional")


class _QPolicyDefinitionLP_Type(Integer32):
    """Custom type qPolicyDefinitionLP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_QPolicyDefinitionLP_Type.__name__ = "Integer32"
_QPolicyDefinitionLP_Object = MibTableColumn
qPolicyDefinitionLP = _QPolicyDefinitionLP_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 4, 1, 4),
    _QPolicyDefinitionLP_Type()
)
qPolicyDefinitionLP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qPolicyDefinitionLP.setStatus("optional")
_QPolicyDefinitionStartTime_Type = TimeDateString
_QPolicyDefinitionStartTime_Object = MibTableColumn
qPolicyDefinitionStartTime = _QPolicyDefinitionStartTime_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 4, 1, 5),
    _QPolicyDefinitionStartTime_Type()
)
qPolicyDefinitionStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qPolicyDefinitionStartTime.setStatus("optional")
_QPolicyDefinitionEndTime_Type = TimeDateString
_QPolicyDefinitionEndTime_Object = MibTableColumn
qPolicyDefinitionEndTime = _QPolicyDefinitionEndTime_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 4, 1, 6),
    _QPolicyDefinitionEndTime_Type()
)
qPolicyDefinitionEndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qPolicyDefinitionEndTime.setStatus("optional")


class _QPolicyDefinitionDayofWeek_Type(Integer32):
    """Custom type qPolicyDefinitionDayofWeek based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QPolicyDefinitionDayofWeek_Type.__name__ = "Integer32"
_QPolicyDefinitionDayofWeek_Object = MibTableColumn
qPolicyDefinitionDayofWeek = _QPolicyDefinitionDayofWeek_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 4, 1, 7),
    _QPolicyDefinitionDayofWeek_Type()
)
qPolicyDefinitionDayofWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qPolicyDefinitionDayofWeek.setStatus("optional")


class _QPolicyDefinitionPipeID_Type(Integer32):
    """Custom type qPolicyDefinitionPipeID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_QPolicyDefinitionPipeID_Type.__name__ = "Integer32"
_QPolicyDefinitionPipeID_Object = MibTableColumn
qPolicyDefinitionPipeID = _QPolicyDefinitionPipeID_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 4, 1, 8),
    _QPolicyDefinitionPipeID_Type()
)
qPolicyDefinitionPipeID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qPolicyDefinitionPipeID.setStatus("mandatory")


class _QPolicyDefinitionClassID_Type(Integer32):
    """Custom type qPolicyDefinitionClassID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_QPolicyDefinitionClassID_Type.__name__ = "Integer32"
_QPolicyDefinitionClassID_Object = MibTableColumn
qPolicyDefinitionClassID = _QPolicyDefinitionClassID_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 4, 1, 9),
    _QPolicyDefinitionClassID_Type()
)
qPolicyDefinitionClassID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qPolicyDefinitionClassID.setStatus("mandatory")


class _QPolicyDefinitionChannelized_Type(Integer32):
    """Custom type qPolicyDefinitionChannelized based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QPolicyDefinitionChannelized_Type.__name__ = "Integer32"
_QPolicyDefinitionChannelized_Object = MibTableColumn
qPolicyDefinitionChannelized = _QPolicyDefinitionChannelized_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 4, 1, 10),
    _QPolicyDefinitionChannelized_Type()
)
qPolicyDefinitionChannelized.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qPolicyDefinitionChannelized.setStatus("optional")


class _QPolicyDefinitionOutboundDSValue_Type(Integer32):
    """Custom type qPolicyDefinitionOutboundDSValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_QPolicyDefinitionOutboundDSValue_Type.__name__ = "Integer32"
_QPolicyDefinitionOutboundDSValue_Object = MibTableColumn
qPolicyDefinitionOutboundDSValue = _QPolicyDefinitionOutboundDSValue_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 4, 1, 11),
    _QPolicyDefinitionOutboundDSValue_Type()
)
qPolicyDefinitionOutboundDSValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qPolicyDefinitionOutboundDSValue.setStatus("optional")


class _QPolicyDefinitionPriority_Type(Integer32):
    """Custom type qPolicyDefinitionPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QPolicyDefinitionPriority_Type.__name__ = "Integer32"
_QPolicyDefinitionPriority_Object = MibTableColumn
qPolicyDefinitionPriority = _QPolicyDefinitionPriority_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 4, 1, 12),
    _QPolicyDefinitionPriority_Type()
)
qPolicyDefinitionPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qPolicyDefinitionPriority.setStatus("optional")


class _QPolicyDefinitionEvent_Type(Integer32):
    """Custom type qPolicyDefinitionEvent based on Integer32"""
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
        *(("increasedbw", 4),
          ("reducedbw", 3),
          ("static", 1),
          ("time", 2))
    )


_QPolicyDefinitionEvent_Type.__name__ = "Integer32"
_QPolicyDefinitionEvent_Object = MibTableColumn
qPolicyDefinitionEvent = _QPolicyDefinitionEvent_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 4, 1, 13),
    _QPolicyDefinitionEvent_Type()
)
qPolicyDefinitionEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qPolicyDefinitionEvent.setStatus("mandatory")
_QPipeDefinitionMaxEntries_Type = Counter32
_QPipeDefinitionMaxEntries_Object = MibScalar
qPipeDefinitionMaxEntries = _QPipeDefinitionMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 5),
    _QPipeDefinitionMaxEntries_Type()
)
qPipeDefinitionMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qPipeDefinitionMaxEntries.setStatus("mandatory")
_QPipeDefinitionTable_Object = MibTable
qPipeDefinitionTable = _QPipeDefinitionTable_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 6)
)
if mibBuilder.loadTexts:
    qPipeDefinitionTable.setStatus("mandatory")
_QPipeDefinitionEntry_Object = MibTableRow
qPipeDefinitionEntry = _QPipeDefinitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 6, 1)
)
qPipeDefinitionEntry.setIndexNames(
    (0, "QWESCOM-MIB", "qPipeDefinitionIndex"),
)
if mibBuilder.loadTexts:
    qPipeDefinitionEntry.setStatus("mandatory")


class _QPipeDefinitionIndex_Type(Integer32):
    """Custom type qPipeDefinitionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 1024),
    )


_QPipeDefinitionIndex_Type.__name__ = "Integer32"
_QPipeDefinitionIndex_Object = MibTableColumn
qPipeDefinitionIndex = _QPipeDefinitionIndex_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 6, 1, 1),
    _QPipeDefinitionIndex_Type()
)
qPipeDefinitionIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qPipeDefinitionIndex.setStatus("mandatory")


class _QPipeDefinitionAlias_Type(DisplayString):
    """Custom type qPipeDefinitionAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QPipeDefinitionAlias_Type.__name__ = "DisplayString"
_QPipeDefinitionAlias_Object = MibTableColumn
qPipeDefinitionAlias = _QPipeDefinitionAlias_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 6, 1, 2),
    _QPipeDefinitionAlias_Type()
)
qPipeDefinitionAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qPipeDefinitionAlias.setStatus("optional")


class _QPipeDefinitionType_Type(Integer32):
    """Custom type qPipeDefinitionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("valid", 1))
    )


_QPipeDefinitionType_Type.__name__ = "Integer32"
_QPipeDefinitionType_Object = MibTableColumn
qPipeDefinitionType = _QPipeDefinitionType_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 6, 1, 3),
    _QPipeDefinitionType_Type()
)
qPipeDefinitionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qPipeDefinitionType.setStatus("optional")


class _QPipeDefinitionCircuitID_Type(Integer32):
    """Custom type qPipeDefinitionCircuitID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_QPipeDefinitionCircuitID_Type.__name__ = "Integer32"
_QPipeDefinitionCircuitID_Object = MibTableColumn
qPipeDefinitionCircuitID = _QPipeDefinitionCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 6, 1, 4),
    _QPipeDefinitionCircuitID_Type()
)
qPipeDefinitionCircuitID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qPipeDefinitionCircuitID.setStatus("optional")
_QPipeDefinitionBandwidth_Type = Integer32
_QPipeDefinitionBandwidth_Object = MibTableColumn
qPipeDefinitionBandwidth = _QPipeDefinitionBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 6, 1, 5),
    _QPipeDefinitionBandwidth_Type()
)
qPipeDefinitionBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qPipeDefinitionBandwidth.setStatus("optional")
_QPipeDefinitionPeak_Type = Integer32
_QPipeDefinitionPeak_Object = MibTableColumn
qPipeDefinitionPeak = _QPipeDefinitionPeak_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 6, 1, 6),
    _QPipeDefinitionPeak_Type()
)
qPipeDefinitionPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qPipeDefinitionPeak.setStatus("optional")
_QPipeDefinitionMBS_Type = Integer32
_QPipeDefinitionMBS_Object = MibTableColumn
qPipeDefinitionMBS = _QPipeDefinitionMBS_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 6, 1, 7),
    _QPipeDefinitionMBS_Type()
)
qPipeDefinitionMBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qPipeDefinitionMBS.setStatus("mandatory")
_QPipeDefinitionBufferAllocation_Type = Integer32
_QPipeDefinitionBufferAllocation_Object = MibTableColumn
qPipeDefinitionBufferAllocation = _QPipeDefinitionBufferAllocation_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 6, 1, 8),
    _QPipeDefinitionBufferAllocation_Type()
)
qPipeDefinitionBufferAllocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qPipeDefinitionBufferAllocation.setStatus("mandatory")
_QPipeDefinitionDelay_Type = Integer32
_QPipeDefinitionDelay_Object = MibTableColumn
qPipeDefinitionDelay = _QPipeDefinitionDelay_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 6, 1, 9),
    _QPipeDefinitionDelay_Type()
)
qPipeDefinitionDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qPipeDefinitionDelay.setStatus("mandatory")
_QPipeDefinitionPhyIdx_Type = Integer32
_QPipeDefinitionPhyIdx_Object = MibTableColumn
qPipeDefinitionPhyIdx = _QPipeDefinitionPhyIdx_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 6, 1, 10),
    _QPipeDefinitionPhyIdx_Type()
)
qPipeDefinitionPhyIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qPipeDefinitionPhyIdx.setStatus("mandatory")
_QPipeDefinitionPhyType_Type = Integer32
_QPipeDefinitionPhyType_Object = MibTableColumn
qPipeDefinitionPhyType = _QPipeDefinitionPhyType_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 6, 1, 11),
    _QPipeDefinitionPhyType_Type()
)
qPipeDefinitionPhyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qPipeDefinitionPhyType.setStatus("mandatory")
_QClassStatisticsTable_Object = MibTable
qClassStatisticsTable = _QClassStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 7)
)
if mibBuilder.loadTexts:
    qClassStatisticsTable.setStatus("mandatory")
_QClassStatisticsEntry_Object = MibTableRow
qClassStatisticsEntry = _QClassStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 7, 1)
)
qClassStatisticsEntry.setIndexNames(
    (0, "QWESCOM-MIB", "qClassStatisticsIndex"),
)
if mibBuilder.loadTexts:
    qClassStatisticsEntry.setStatus("mandatory")


class _QClassStatisticsIndex_Type(Integer32):
    """Custom type qClassStatisticsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_QClassStatisticsIndex_Type.__name__ = "Integer32"
_QClassStatisticsIndex_Object = MibTableColumn
qClassStatisticsIndex = _QClassStatisticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 7, 1, 1),
    _QClassStatisticsIndex_Type()
)
qClassStatisticsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qClassStatisticsIndex.setStatus("mandatory")
_QClassStatisticsAlias_Type = DisplayString
_QClassStatisticsAlias_Object = MibTableColumn
qClassStatisticsAlias = _QClassStatisticsAlias_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 7, 1, 2),
    _QClassStatisticsAlias_Type()
)
qClassStatisticsAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qClassStatisticsAlias.setStatus("mandatory")
_QClassStatisticsTransmittedCount_Type = Counter32
_QClassStatisticsTransmittedCount_Object = MibTableColumn
qClassStatisticsTransmittedCount = _QClassStatisticsTransmittedCount_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 7, 1, 3),
    _QClassStatisticsTransmittedCount_Type()
)
qClassStatisticsTransmittedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qClassStatisticsTransmittedCount.setStatus("mandatory")
_QClassStatisticsDiscardCount_Type = Counter32
_QClassStatisticsDiscardCount_Object = MibTableColumn
qClassStatisticsDiscardCount = _QClassStatisticsDiscardCount_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 7, 1, 4),
    _QClassStatisticsDiscardCount_Type()
)
qClassStatisticsDiscardCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qClassStatisticsDiscardCount.setStatus("mandatory")
_QClassStatisticsFallbackCount_Type = Counter32
_QClassStatisticsFallbackCount_Object = MibTableColumn
qClassStatisticsFallbackCount = _QClassStatisticsFallbackCount_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 4, 7, 1, 5),
    _QClassStatisticsFallbackCount_Type()
)
qClassStatisticsFallbackCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qClassStatisticsFallbackCount.setStatus("mandatory")
_Qatm_ObjectIdentity = ObjectIdentity
qatm = _Qatm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5)
)
_QatmCircuitTable_Object = MibTable
qatmCircuitTable = _QatmCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 1)
)
if mibBuilder.loadTexts:
    qatmCircuitTable.setStatus("mandatory")
_QatmCircuitEntry_Object = MibTableRow
qatmCircuitEntry = _QatmCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 1, 1)
)
qatmCircuitEntry.setIndexNames(
    (0, "QWESCOM-MIB", "qatmCircuitId"),
)
if mibBuilder.loadTexts:
    qatmCircuitEntry.setStatus("mandatory")


class _QatmCircuitId_Type(Integer32):
    """Custom type qatmCircuitId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_QatmCircuitId_Type.__name__ = "Integer32"
_QatmCircuitId_Object = MibTableColumn
qatmCircuitId = _QatmCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 1, 1, 1),
    _QatmCircuitId_Type()
)
qatmCircuitId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qatmCircuitId.setStatus("mandatory")


class _QatmCircuitAlias_Type(DisplayString):
    """Custom type qatmCircuitAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 52),
    )


_QatmCircuitAlias_Type.__name__ = "DisplayString"
_QatmCircuitAlias_Object = MibTableColumn
qatmCircuitAlias = _QatmCircuitAlias_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 1, 1, 2),
    _QatmCircuitAlias_Type()
)
qatmCircuitAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qatmCircuitAlias.setStatus("mandatory")


class _QatmCircuitUNI_Type(Integer32):
    """Custom type qatmCircuitUNI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_QatmCircuitUNI_Type.__name__ = "Integer32"
_QatmCircuitUNI_Object = MibTableColumn
qatmCircuitUNI = _QatmCircuitUNI_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 1, 1, 3),
    _QatmCircuitUNI_Type()
)
qatmCircuitUNI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qatmCircuitUNI.setStatus("mandatory")


class _QatmCircuitLogicalInterface_Type(Integer32):
    """Custom type qatmCircuitLogicalInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 1024),
    )


_QatmCircuitLogicalInterface_Type.__name__ = "Integer32"
_QatmCircuitLogicalInterface_Object = MibTableColumn
qatmCircuitLogicalInterface = _QatmCircuitLogicalInterface_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 1, 1, 4),
    _QatmCircuitLogicalInterface_Type()
)
qatmCircuitLogicalInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qatmCircuitLogicalInterface.setStatus("mandatory")


class _QatmCircuitVpi_Type(Integer32):
    """Custom type qatmCircuitVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QatmCircuitVpi_Type.__name__ = "Integer32"
_QatmCircuitVpi_Object = MibTableColumn
qatmCircuitVpi = _QatmCircuitVpi_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 1, 1, 5),
    _QatmCircuitVpi_Type()
)
qatmCircuitVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qatmCircuitVpi.setStatus("mandatory")


class _QatmCircuitFirstVci_Type(Integer32):
    """Custom type qatmCircuitFirstVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QatmCircuitFirstVci_Type.__name__ = "Integer32"
_QatmCircuitFirstVci_Object = MibTableColumn
qatmCircuitFirstVci = _QatmCircuitFirstVci_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 1, 1, 6),
    _QatmCircuitFirstVci_Type()
)
qatmCircuitFirstVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qatmCircuitFirstVci.setStatus("mandatory")


class _QatmCircuitMode_Type(Integer32):
    """Custom type qatmCircuitMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cell", 1),
          ("packet", 2))
    )


_QatmCircuitMode_Type.__name__ = "Integer32"
_QatmCircuitMode_Object = MibTableColumn
qatmCircuitMode = _QatmCircuitMode_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 1, 1, 7),
    _QatmCircuitMode_Type()
)
qatmCircuitMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qatmCircuitMode.setStatus("mandatory")


class _QatmCircuitStatus_Type(Integer32):
    """Custom type qatmCircuitStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deltete", 2),
          ("valid", 1))
    )


_QatmCircuitStatus_Type.__name__ = "Integer32"
_QatmCircuitStatus_Object = MibTableColumn
qatmCircuitStatus = _QatmCircuitStatus_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 1, 1, 8),
    _QatmCircuitStatus_Type()
)
qatmCircuitStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qatmCircuitStatus.setStatus("mandatory")
_QatmUniTable_Object = MibTable
qatmUniTable = _QatmUniTable_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 2)
)
if mibBuilder.loadTexts:
    qatmUniTable.setStatus("mandatory")
_QatmUniEntry_Object = MibTableRow
qatmUniEntry = _QatmUniEntry_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 2, 1)
)
qatmUniEntry.setIndexNames(
    (0, "QWESCOM-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    qatmUniEntry.setStatus("mandatory")


class _QatmSpanPort_Type(Integer32):
    """Custom type qatmSpanPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25),
    )


_QatmSpanPort_Type.__name__ = "Integer32"
_QatmSpanPort_Object = MibTableColumn
qatmSpanPort = _QatmSpanPort_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 2, 1, 1),
    _QatmSpanPort_Type()
)
qatmSpanPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qatmSpanPort.setStatus("mandatory")


class _QatmUniName_Type(DisplayString):
    """Custom type qatmUniName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QatmUniName_Type.__name__ = "DisplayString"
_QatmUniName_Object = MibTableColumn
qatmUniName = _QatmUniName_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 2, 1, 2),
    _QatmUniName_Type()
)
qatmUniName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qatmUniName.setStatus("mandatory")


class _QatmUniAlias_Type(DisplayString):
    """Custom type qatmUniAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QatmUniAlias_Type.__name__ = "DisplayString"
_QatmUniAlias_Object = MibTableColumn
qatmUniAlias = _QatmUniAlias_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 2, 1, 3),
    _QatmUniAlias_Type()
)
qatmUniAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qatmUniAlias.setStatus("mandatory")


class _QatmUniTrapStatus_Type(Integer32):
    """Custom type qatmUniTrapStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_QatmUniTrapStatus_Type.__name__ = "Integer32"
_QatmUniTrapStatus_Object = MibTableColumn
qatmUniTrapStatus = _QatmUniTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 2, 1, 4),
    _QatmUniTrapStatus_Type()
)
qatmUniTrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qatmUniTrapStatus.setStatus("mandatory")
_QatmUniMaxQueueDelay_Type = Integer32
_QatmUniMaxQueueDelay_Object = MibTableColumn
qatmUniMaxQueueDelay = _QatmUniMaxQueueDelay_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 2, 1, 5),
    _QatmUniMaxQueueDelay_Type()
)
qatmUniMaxQueueDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qatmUniMaxQueueDelay.setStatus("mandatory")
_QatmUniMinAllocBuffer_Type = Integer32
_QatmUniMinAllocBuffer_Object = MibTableColumn
qatmUniMinAllocBuffer = _QatmUniMinAllocBuffer_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 2, 1, 6),
    _QatmUniMinAllocBuffer_Type()
)
qatmUniMinAllocBuffer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qatmUniMinAllocBuffer.setStatus("mandatory")
_QatmUniSharedBuffer_Type = Integer32
_QatmUniSharedBuffer_Object = MibTableColumn
qatmUniSharedBuffer = _QatmUniSharedBuffer_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 2, 1, 7),
    _QatmUniSharedBuffer_Type()
)
qatmUniSharedBuffer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qatmUniSharedBuffer.setStatus("mandatory")
_QatmUniLinkBandwidth_Type = Integer32
_QatmUniLinkBandwidth_Object = MibTableColumn
qatmUniLinkBandwidth = _QatmUniLinkBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 2, 1, 8),
    _QatmUniLinkBandwidth_Type()
)
qatmUniLinkBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qatmUniLinkBandwidth.setStatus("mandatory")
_QatmUniLinkDelay_Type = Integer32
_QatmUniLinkDelay_Object = MibTableColumn
qatmUniLinkDelay = _QatmUniLinkDelay_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 2, 1, 9),
    _QatmUniLinkDelay_Type()
)
qatmUniLinkDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qatmUniLinkDelay.setStatus("mandatory")
_QatmUniBandwidthGranularity_Type = Integer32
_QatmUniBandwidthGranularity_Object = MibTableColumn
qatmUniBandwidthGranularity = _QatmUniBandwidthGranularity_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 2, 1, 10),
    _QatmUniBandwidthGranularity_Type()
)
qatmUniBandwidthGranularity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qatmUniBandwidthGranularity.setStatus("mandatory")


class _QatmUniIlmiStatus_Type(Integer32):
    """Custom type qatmUniIlmiStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_QatmUniIlmiStatus_Type.__name__ = "Integer32"
_QatmUniIlmiStatus_Object = MibTableColumn
qatmUniIlmiStatus = _QatmUniIlmiStatus_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 2, 1, 11),
    _QatmUniIlmiStatus_Type()
)
qatmUniIlmiStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qatmUniIlmiStatus.setStatus("mandatory")
_QatmUniRowStatus_Type = RowStatus
_QatmUniRowStatus_Object = MibTableColumn
qatmUniRowStatus = _QatmUniRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 2, 1, 12),
    _QatmUniRowStatus_Type()
)
qatmUniRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qatmUniRowStatus.setStatus("mandatory")
_QatmVplTable_Object = MibTable
qatmVplTable = _QatmVplTable_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 3)
)
if mibBuilder.loadTexts:
    qatmVplTable.setStatus("mandatory")
_QatmVplEntry_Object = MibTableRow
qatmVplEntry = _QatmVplEntry_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 3, 1)
)
qatmVplEntry.setIndexNames(
    (0, "QWESCOM-MIB", "ifIndex"),
    (0, "QWESCOM-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    qatmVplEntry.setStatus("mandatory")


class _QatmVplMaxVcc_Type(Integer32):
    """Custom type qatmVplMaxVcc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_QatmVplMaxVcc_Type.__name__ = "Integer32"
_QatmVplMaxVcc_Object = MibTableColumn
qatmVplMaxVcc = _QatmVplMaxVcc_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 3, 1, 1),
    _QatmVplMaxVcc_Type()
)
qatmVplMaxVcc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qatmVplMaxVcc.setStatus("mandatory")


class _QatmVplLowestVci_Type(Integer32):
    """Custom type qatmVplLowestVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QatmVplLowestVci_Type.__name__ = "Integer32"
_QatmVplLowestVci_Object = MibTableColumn
qatmVplLowestVci = _QatmVplLowestVci_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 3, 1, 2),
    _QatmVplLowestVci_Type()
)
qatmVplLowestVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qatmVplLowestVci.setStatus("mandatory")
_QatmVplMaxQueueDelay_Type = Integer32
_QatmVplMaxQueueDelay_Object = MibTableColumn
qatmVplMaxQueueDelay = _QatmVplMaxQueueDelay_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 3, 1, 3),
    _QatmVplMaxQueueDelay_Type()
)
qatmVplMaxQueueDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qatmVplMaxQueueDelay.setStatus("mandatory")
_QatmVplReservedBuffer_Type = Integer32
_QatmVplReservedBuffer_Object = MibTableColumn
qatmVplReservedBuffer = _QatmVplReservedBuffer_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 3, 1, 4),
    _QatmVplReservedBuffer_Type()
)
qatmVplReservedBuffer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qatmVplReservedBuffer.setStatus("mandatory")
_QatmVplBwGranularity_Type = Integer32
_QatmVplBwGranularity_Object = MibTableColumn
qatmVplBwGranularity = _QatmVplBwGranularity_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 3, 1, 5),
    _QatmVplBwGranularity_Type()
)
qatmVplBwGranularity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qatmVplBwGranularity.setStatus("mandatory")
_QatmVplMtu_Type = Integer32
_QatmVplMtu_Object = MibTableColumn
qatmVplMtu = _QatmVplMtu_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 3, 1, 6),
    _QatmVplMtu_Type()
)
qatmVplMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qatmVplMtu.setStatus("mandatory")
_QatmVplSharedBuffer_Type = Integer32
_QatmVplSharedBuffer_Object = MibTableColumn
qatmVplSharedBuffer = _QatmVplSharedBuffer_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 3, 1, 7),
    _QatmVplSharedBuffer_Type()
)
qatmVplSharedBuffer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qatmVplSharedBuffer.setStatus("mandatory")
_QatmVclTable_Object = MibTable
qatmVclTable = _QatmVclTable_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 4)
)
if mibBuilder.loadTexts:
    qatmVclTable.setStatus("mandatory")
_QatmVclEntry_Object = MibTableRow
qatmVclEntry = _QatmVclEntry_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 4, 1)
)
qatmVclEntry.setIndexNames(
    (0, "QWESCOM-MIB", "ifIndex"),
    (0, "QWESCOM-MIB", "ifIndex"),
    (0, "QWESCOM-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    qatmVclEntry.setStatus("mandatory")
_QatmVclBwGranularity_Type = Integer32
_QatmVclBwGranularity_Object = MibTableColumn
qatmVclBwGranularity = _QatmVclBwGranularity_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 4, 1, 1),
    _QatmVclBwGranularity_Type()
)
qatmVclBwGranularity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qatmVclBwGranularity.setStatus("mandatory")


class _QatmVclMaxSubChannels_Type(Integer32):
    """Custom type qatmVclMaxSubChannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QatmVclMaxSubChannels_Type.__name__ = "Integer32"
_QatmVclMaxSubChannels_Object = MibTableColumn
qatmVclMaxSubChannels = _QatmVclMaxSubChannels_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 4, 1, 2),
    _QatmVclMaxSubChannels_Type()
)
qatmVclMaxSubChannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qatmVclMaxSubChannels.setStatus("mandatory")
_QatmVclMaxQueueDelay_Type = Integer32
_QatmVclMaxQueueDelay_Object = MibTableColumn
qatmVclMaxQueueDelay = _QatmVclMaxQueueDelay_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 4, 1, 3),
    _QatmVclMaxQueueDelay_Type()
)
qatmVclMaxQueueDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qatmVclMaxQueueDelay.setStatus("mandatory")
_QatmVclReservedBuffer_Type = Integer32
_QatmVclReservedBuffer_Object = MibTableColumn
qatmVclReservedBuffer = _QatmVclReservedBuffer_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 4, 1, 4),
    _QatmVclReservedBuffer_Type()
)
qatmVclReservedBuffer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qatmVclReservedBuffer.setStatus("mandatory")
_QatmVclSharedBuffer_Type = Integer32
_QatmVclSharedBuffer_Object = MibTableColumn
qatmVclSharedBuffer = _QatmVclSharedBuffer_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 4, 1, 5),
    _QatmVclSharedBuffer_Type()
)
qatmVclSharedBuffer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qatmVclSharedBuffer.setStatus("mandatory")
_QatmAal5Table_Object = MibTable
qatmAal5Table = _QatmAal5Table_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 5)
)
if mibBuilder.loadTexts:
    qatmAal5Table.setStatus("mandatory")
_QatmAal5Entry_Object = MibTableRow
qatmAal5Entry = _QatmAal5Entry_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 5, 1)
)
qatmAal5Entry.setIndexNames(
    (0, "QWESCOM-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    qatmAal5Entry.setStatus("mandatory")


class _QatmAal5Uni_Type(Integer32):
    """Custom type qatmAal5Uni based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_QatmAal5Uni_Type.__name__ = "Integer32"
_QatmAal5Uni_Object = MibTableColumn
qatmAal5Uni = _QatmAal5Uni_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 5, 1, 1),
    _QatmAal5Uni_Type()
)
qatmAal5Uni.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qatmAal5Uni.setStatus("mandatory")


class _QatmAal5Aal5Name_Type(DisplayString):
    """Custom type qatmAal5Aal5Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QatmAal5Aal5Name_Type.__name__ = "DisplayString"
_QatmAal5Aal5Name_Object = MibTableColumn
qatmAal5Aal5Name = _QatmAal5Aal5Name_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 5, 1, 2),
    _QatmAal5Aal5Name_Type()
)
qatmAal5Aal5Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qatmAal5Aal5Name.setStatus("mandatory")


class _QatmAal5Aal5Alias_Type(DisplayString):
    """Custom type qatmAal5Aal5Alias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QatmAal5Aal5Alias_Type.__name__ = "DisplayString"
_QatmAal5Aal5Alias_Object = MibTableColumn
qatmAal5Aal5Alias = _QatmAal5Aal5Alias_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 5, 1, 3),
    _QatmAal5Aal5Alias_Type()
)
qatmAal5Aal5Alias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qatmAal5Aal5Alias.setStatus("mandatory")


class _QatmAal5AdminStatus_Type(Integer32):
    """Custom type qatmAal5AdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_QatmAal5AdminStatus_Type.__name__ = "Integer32"
_QatmAal5AdminStatus_Object = MibTableColumn
qatmAal5AdminStatus = _QatmAal5AdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 5, 1, 4),
    _QatmAal5AdminStatus_Type()
)
qatmAal5AdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qatmAal5AdminStatus.setStatus("mandatory")


class _QatmAal5TrapStatus_Type(Integer32):
    """Custom type qatmAal5TrapStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_QatmAal5TrapStatus_Type.__name__ = "Integer32"
_QatmAal5TrapStatus_Object = MibTableColumn
qatmAal5TrapStatus = _QatmAal5TrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 5, 1, 5),
    _QatmAal5TrapStatus_Type()
)
qatmAal5TrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qatmAal5TrapStatus.setStatus("mandatory")


class _QatmAal5MtuSize_Type(Integer32):
    """Custom type qatmAal5MtuSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_QatmAal5MtuSize_Type.__name__ = "Integer32"
_QatmAal5MtuSize_Object = MibTableColumn
qatmAal5MtuSize = _QatmAal5MtuSize_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 5, 1, 6),
    _QatmAal5MtuSize_Type()
)
qatmAal5MtuSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qatmAal5MtuSize.setStatus("mandatory")


class _QatmAal5RowStatus_Type(Integer32):
    """Custom type qatmAal5RowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_QatmAal5RowStatus_Type.__name__ = "Integer32"
_QatmAal5RowStatus_Object = MibTableColumn
qatmAal5RowStatus = _QatmAal5RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 5, 1, 7),
    _QatmAal5RowStatus_Type()
)
qatmAal5RowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qatmAal5RowStatus.setStatus("mandatory")
_QatmTrafficDescriptorTable_Object = MibTable
qatmTrafficDescriptorTable = _QatmTrafficDescriptorTable_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 6)
)
if mibBuilder.loadTexts:
    qatmTrafficDescriptorTable.setStatus("mandatory")
_QatmTrafficDescriptorEntry_Object = MibTableRow
qatmTrafficDescriptorEntry = _QatmTrafficDescriptorEntry_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 6, 1)
)
qatmTrafficDescriptorEntry.setIndexNames(
    (0, "QWESCOM-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    qatmTrafficDescriptorEntry.setStatus("mandatory")


class _QatmTrafficDescriptorAlias_Type(DisplayString):
    """Custom type qatmTrafficDescriptorAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QatmTrafficDescriptorAlias_Type.__name__ = "DisplayString"
_QatmTrafficDescriptorAlias_Object = MibTableColumn
qatmTrafficDescriptorAlias = _QatmTrafficDescriptorAlias_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 6, 1, 1),
    _QatmTrafficDescriptorAlias_Type()
)
qatmTrafficDescriptorAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qatmTrafficDescriptorAlias.setStatus("mandatory")
_QatmTcTable_Object = MibTable
qatmTcTable = _QatmTcTable_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 7)
)
if mibBuilder.loadTexts:
    qatmTcTable.setStatus("mandatory")
_QatmTcEntry_Object = MibTableRow
qatmTcEntry = _QatmTcEntry_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 7, 1)
)
qatmTcEntry.setIndexNames(
    (0, "QWESCOM-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    qatmTcEntry.setStatus("mandatory")
_QatmTcCellSync_Type = Integer32
_QatmTcCellSync_Object = MibTableColumn
qatmTcCellSync = _QatmTcCellSync_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 7, 1, 1),
    _QatmTcCellSync_Type()
)
qatmTcCellSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qatmTcCellSync.setStatus("mandatory")
_QatmTcPortErrors_Type = Integer32
_QatmTcPortErrors_Object = MibTableColumn
qatmTcPortErrors = _QatmTcPortErrors_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 7, 1, 2),
    _QatmTcPortErrors_Type()
)
qatmTcPortErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qatmTcPortErrors.setStatus("mandatory")
_QatmTcDmaErrors_Type = Integer32
_QatmTcDmaErrors_Object = MibTableColumn
qatmTcDmaErrors = _QatmTcDmaErrors_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 7, 1, 3),
    _QatmTcDmaErrors_Type()
)
qatmTcDmaErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qatmTcDmaErrors.setStatus("mandatory")
_QatmInvalidCells_Type = Integer32
_QatmInvalidCells_Object = MibTableColumn
qatmInvalidCells = _QatmInvalidCells_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 7, 1, 4),
    _QatmInvalidCells_Type()
)
qatmInvalidCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qatmInvalidCells.setStatus("mandatory")
_QatmCellsForInactiveVcc_Type = Integer32
_QatmCellsForInactiveVcc_Object = MibTableColumn
qatmCellsForInactiveVcc = _QatmCellsForInactiveVcc_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 7, 1, 5),
    _QatmCellsForInactiveVcc_Type()
)
qatmCellsForInactiveVcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qatmCellsForInactiveVcc.setStatus("mandatory")
_QatmAal5VccStatsTable_Object = MibTable
qatmAal5VccStatsTable = _QatmAal5VccStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 8)
)
if mibBuilder.loadTexts:
    qatmAal5VccStatsTable.setStatus("mandatory")
_QatmAal5VccStatsEntry_Object = MibTableRow
qatmAal5VccStatsEntry = _QatmAal5VccStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 8, 1)
)
qatmAal5VccStatsEntry.setIndexNames(
    (0, "QWESCOM-MIB", "ifIndex"),
    (0, "QWESCOM-MIB", "ifIndex"),
    (0, "QWESCOM-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    qatmAal5VccStatsEntry.setStatus("mandatory")
_QatmAal5VccStatsInBytes_Type = Integer32
_QatmAal5VccStatsInBytes_Object = MibTableColumn
qatmAal5VccStatsInBytes = _QatmAal5VccStatsInBytes_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 8, 1, 1),
    _QatmAal5VccStatsInBytes_Type()
)
qatmAal5VccStatsInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qatmAal5VccStatsInBytes.setStatus("mandatory")
_QatmAal5VccStatsOutBytes_Type = Integer32
_QatmAal5VccStatsOutBytes_Object = MibTableColumn
qatmAal5VccStatsOutBytes = _QatmAal5VccStatsOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 8, 1, 2),
    _QatmAal5VccStatsOutBytes_Type()
)
qatmAal5VccStatsOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qatmAal5VccStatsOutBytes.setStatus("mandatory")
_QatmAal5VccStatsInSdus_Type = Integer32
_QatmAal5VccStatsInSdus_Object = MibTableColumn
qatmAal5VccStatsInSdus = _QatmAal5VccStatsInSdus_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 8, 1, 3),
    _QatmAal5VccStatsInSdus_Type()
)
qatmAal5VccStatsInSdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qatmAal5VccStatsInSdus.setStatus("mandatory")
_QatmAal5VccStatsOutSdus_Type = Integer32
_QatmAal5VccStatsOutSdus_Object = MibTableColumn
qatmAal5VccStatsOutSdus = _QatmAal5VccStatsOutSdus_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 8, 1, 4),
    _QatmAal5VccStatsOutSdus_Type()
)
qatmAal5VccStatsOutSdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qatmAal5VccStatsOutSdus.setStatus("mandatory")
_QatmAal5VccStatsErrsAndDiscards_Type = Integer32
_QatmAal5VccStatsErrsAndDiscards_Object = MibTableColumn
qatmAal5VccStatsErrsAndDiscards = _QatmAal5VccStatsErrsAndDiscards_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 8, 1, 5),
    _QatmAal5VccStatsErrsAndDiscards_Type()
)
qatmAal5VccStatsErrsAndDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qatmAal5VccStatsErrsAndDiscards.setStatus("mandatory")
_QatmAal5VccStatsLengthMismatchs_Type = Integer32
_QatmAal5VccStatsLengthMismatchs_Object = MibTableColumn
qatmAal5VccStatsLengthMismatchs = _QatmAal5VccStatsLengthMismatchs_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 8, 1, 6),
    _QatmAal5VccStatsLengthMismatchs_Type()
)
qatmAal5VccStatsLengthMismatchs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qatmAal5VccStatsLengthMismatchs.setStatus("mandatory")
_QatmAal5VccStatsUserAborts_Type = Integer32
_QatmAal5VccStatsUserAborts_Object = MibTableColumn
qatmAal5VccStatsUserAborts = _QatmAal5VccStatsUserAborts_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 8, 1, 7),
    _QatmAal5VccStatsUserAborts_Type()
)
qatmAal5VccStatsUserAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qatmAal5VccStatsUserAborts.setStatus("mandatory")
_QatmAal5VccStatsPoolDepleteds_Type = Integer32
_QatmAal5VccStatsPoolDepleteds_Object = MibTableColumn
qatmAal5VccStatsPoolDepleteds = _QatmAal5VccStatsPoolDepleteds_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 5, 8, 1, 8),
    _QatmAal5VccStatsPoolDepleteds_Type()
)
qatmAal5VccStatsPoolDepleteds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qatmAal5VccStatsPoolDepleteds.setStatus("mandatory")
_QcraftPort_ObjectIdentity = ObjectIdentity
qcraftPort = _QcraftPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 6)
)


class _QcpStatus_Type(Integer32):
    """Custom type qcpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_QcpStatus_Type.__name__ = "Integer32"
_QcpStatus_Object = MibScalar
qcpStatus = _QcpStatus_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 6, 1),
    _QcpStatus_Type()
)
qcpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qcpStatus.setStatus("mandatory")


class _QcpBaudRate_Type(Integer32):
    """Custom type qcpBaudRate based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("br-115200", 9),
          ("br-1200", 0),
          ("br-14400", 4),
          ("br-19200", 5),
          ("br-2400", 1),
          ("br-28800", 6),
          ("br-38400", 7),
          ("br-4800", 2),
          ("br-57600", 8),
          ("br-9600", 3))
    )


_QcpBaudRate_Type.__name__ = "Integer32"
_QcpBaudRate_Object = MibScalar
qcpBaudRate = _QcpBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 6, 2),
    _QcpBaudRate_Type()
)
qcpBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qcpBaudRate.setStatus("mandatory")


class _QcpStopBitLength_Type(Integer32):
    """Custom type qcpStopBitLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("sb-1", 0),
          ("sb-2", 1))
    )


_QcpStopBitLength_Type.__name__ = "Integer32"
_QcpStopBitLength_Object = MibScalar
qcpStopBitLength = _QcpStopBitLength_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 6, 3),
    _QcpStopBitLength_Type()
)
qcpStopBitLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qcpStopBitLength.setStatus("mandatory")


class _QcpParity_Type(Integer32):
    """Custom type qcpParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("even", 0),
          ("none", 2),
          ("odd", 1))
    )


_QcpParity_Type.__name__ = "Integer32"
_QcpParity_Object = MibScalar
qcpParity = _QcpParity_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 6, 4),
    _QcpParity_Type()
)
qcpParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qcpParity.setStatus("mandatory")


class _QcpDataBits_Type(Integer32):
    """Custom type qcpDataBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("db-7", 0),
          ("db-8", 1))
    )


_QcpDataBits_Type.__name__ = "Integer32"
_QcpDataBits_Object = MibScalar
qcpDataBits = _QcpDataBits_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 6, 5),
    _QcpDataBits_Type()
)
qcpDataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qcpDataBits.setStatus("mandatory")
_QcpCharsSent_Type = Integer32
_QcpCharsSent_Object = MibScalar
qcpCharsSent = _QcpCharsSent_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 6, 6),
    _QcpCharsSent_Type()
)
qcpCharsSent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qcpCharsSent.setStatus("mandatory")
_QcpCharsReceived_Type = Integer32
_QcpCharsReceived_Object = MibScalar
qcpCharsReceived = _QcpCharsReceived_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 6, 7),
    _QcpCharsReceived_Type()
)
qcpCharsReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qcpCharsReceived.setStatus("mandatory")
_QeventGroup_ObjectIdentity = ObjectIdentity
qeventGroup = _QeventGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 8)
)
_QEventConfigTable_Object = MibTable
qEventConfigTable = _QEventConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 8, 1)
)
if mibBuilder.loadTexts:
    qEventConfigTable.setStatus("mandatory")
_QEventConfigEntry_Object = MibTableRow
qEventConfigEntry = _QEventConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 8, 1, 1)
)
qEventConfigEntry.setIndexNames(
    (0, "QWESCOM-MIB", "qEventConfigIndex"),
)
if mibBuilder.loadTexts:
    qEventConfigEntry.setStatus("mandatory")


class _QEventConfigIndex_Type(Integer32):
    """Custom type qEventConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_QEventConfigIndex_Type.__name__ = "Integer32"
_QEventConfigIndex_Object = MibTableColumn
qEventConfigIndex = _QEventConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 8, 1, 1, 1),
    _QEventConfigIndex_Type()
)
qEventConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qEventConfigIndex.setStatus("mandatory")


class _QEventSeverityType_Type(Integer32):
    """Custom type qEventSeverityType based on Integer32"""
    defaultValue = 4

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
        *(("critical", 2),
          ("debug", 6),
          ("fatal", 1),
          ("informational", 5),
          ("mild", 3),
          ("standard-snmp", 4))
    )


_QEventSeverityType_Type.__name__ = "Integer32"
_QEventSeverityType_Object = MibTableColumn
qEventSeverityType = _QEventSeverityType_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 8, 1, 1, 2),
    _QEventSeverityType_Type()
)
qEventSeverityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qEventSeverityType.setStatus("mandatory")


class _QLogFileType_Type(Integer32):
    """Custom type qLogFileType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("none", 3),
          ("system", 2))
    )


_QLogFileType_Type.__name__ = "Integer32"
_QLogFileType_Object = MibTableColumn
qLogFileType = _QLogFileType_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 8, 1, 1, 3),
    _QLogFileType_Type()
)
qLogFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qLogFileType.setStatus("mandatory")


class _QLogOption_Type(Integer32):
    """Custom type qLogOption based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_QLogOption_Type.__name__ = "Integer32"
_QLogOption_Object = MibTableColumn
qLogOption = _QLogOption_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 8, 1, 1, 4),
    _QLogOption_Type()
)
qLogOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qLogOption.setStatus("mandatory")


class _QDisplayOption_Type(Integer32):
    """Custom type qDisplayOption based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_QDisplayOption_Type.__name__ = "Integer32"
_QDisplayOption_Object = MibTableColumn
qDisplayOption = _QDisplayOption_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 8, 1, 1, 5),
    _QDisplayOption_Type()
)
qDisplayOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qDisplayOption.setStatus("mandatory")


class _QTrapOption_Type(Integer32):
    """Custom type qTrapOption based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_QTrapOption_Type.__name__ = "Integer32"
_QTrapOption_Object = MibTableColumn
qTrapOption = _QTrapOption_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 8, 1, 1, 6),
    _QTrapOption_Type()
)
qTrapOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qTrapOption.setStatus("mandatory")
_QEventSystemTable_Object = MibTable
qEventSystemTable = _QEventSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 8, 2)
)
if mibBuilder.loadTexts:
    qEventSystemTable.setStatus("mandatory")
_QEventSystemEntry_Object = MibTableRow
qEventSystemEntry = _QEventSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 8, 2, 1)
)
qEventSystemEntry.setIndexNames(
    (0, "QWESCOM-MIB", "qEventSystemIndex"),
)
if mibBuilder.loadTexts:
    qEventSystemEntry.setStatus("mandatory")


class _QEventSystemIndex_Type(Integer32):
    """Custom type qEventSystemIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QEventSystemIndex_Type.__name__ = "Integer32"
_QEventSystemIndex_Object = MibTableColumn
qEventSystemIndex = _QEventSystemIndex_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 8, 2, 1, 1),
    _QEventSystemIndex_Type()
)
qEventSystemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qEventSystemIndex.setStatus("mandatory")
_QEventSystemDateTime_Type = DisplayString
_QEventSystemDateTime_Object = MibTableColumn
qEventSystemDateTime = _QEventSystemDateTime_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 8, 2, 1, 2),
    _QEventSystemDateTime_Type()
)
qEventSystemDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qEventSystemDateTime.setStatus("mandatory")


class _QEventSystemType_Type(Integer32):
    """Custom type qEventSystemType based on Integer32"""
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
        *(("critical", 2),
          ("debug", 6),
          ("fatal", 1),
          ("informational", 5),
          ("mild", 3),
          ("standard-snmp", 4))
    )


_QEventSystemType_Type.__name__ = "Integer32"
_QEventSystemType_Object = MibTableColumn
qEventSystemType = _QEventSystemType_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 8, 2, 1, 3),
    _QEventSystemType_Type()
)
qEventSystemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qEventSystemType.setStatus("mandatory")


class _QEventSystemSubSystem_Type(Integer32):
    """Custom type qEventSystemSubSystem based on Integer32"""
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
              25)
        )
    )
    namedValues = NamedValues(
        *(("arp-subsystem", 25),
          ("atm-subsystem", 3),
          ("circuit-subsystem", 24),
          ("clip-subsystem", 7),
          ("ethernet-subsystem", 4),
          ("flash-subsystem", 8),
          ("flow-subsystem", 9),
          ("general-subsystem", 1),
          ("get-subsystem", 12),
          ("icmp-subsystem", 16),
          ("igmp-subsystem", 17),
          ("ip-subsystem", 2),
          ("lif-subsystem", 23),
          ("lp-subsystem", 22),
          ("oam-subsystem", 13),
          ("ping-subsystem", 18),
          ("port-manager-subsystem", 11),
          ("reset-subsystem", 14),
          ("serial-subsystem", 10),
          ("snmp-subsystem", 19),
          ("tcp-subsystem", 20),
          ("telnet-subsystem", 6),
          ("tftp-subsystem", 5),
          ("time-subsystem", 15),
          ("upd-subsystem", 21))
    )


_QEventSystemSubSystem_Type.__name__ = "Integer32"
_QEventSystemSubSystem_Object = MibTableColumn
qEventSystemSubSystem = _QEventSystemSubSystem_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 8, 2, 1, 4),
    _QEventSystemSubSystem_Type()
)
qEventSystemSubSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qEventSystemSubSystem.setStatus("mandatory")
_QEventSystemID_Number_Type = Integer32
_QEventSystemID_Number_Object = MibScalar
qEventSystemID_Number = _QEventSystemID_Number_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 8, 2, 1, 5),
    _QEventSystemID_Number_Type()
)
qEventSystemID_Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qEventSystemID_Number.setStatus("mandatory")
_QEventSystemDescription_Type = DisplayString
_QEventSystemDescription_Object = MibTableColumn
qEventSystemDescription = _QEventSystemDescription_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 8, 2, 1, 6),
    _QEventSystemDescription_Type()
)
qEventSystemDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qEventSystemDescription.setStatus("mandatory")
_QEventAlarmTable_Object = MibTable
qEventAlarmTable = _QEventAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 8, 3)
)
if mibBuilder.loadTexts:
    qEventAlarmTable.setStatus("mandatory")
_QEventAlarmEntry_Object = MibTableRow
qEventAlarmEntry = _QEventAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 8, 3, 1)
)
qEventAlarmEntry.setIndexNames(
    (0, "QWESCOM-MIB", "qEventAlarmIndex"),
)
if mibBuilder.loadTexts:
    qEventAlarmEntry.setStatus("mandatory")


class _QEventAlarmIndex_Type(Integer32):
    """Custom type qEventAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QEventAlarmIndex_Type.__name__ = "Integer32"
_QEventAlarmIndex_Object = MibTableColumn
qEventAlarmIndex = _QEventAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 8, 3, 1, 1),
    _QEventAlarmIndex_Type()
)
qEventAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qEventAlarmIndex.setStatus("mandatory")
_QEventAlarmDateTime_Type = DisplayString
_QEventAlarmDateTime_Object = MibTableColumn
qEventAlarmDateTime = _QEventAlarmDateTime_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 8, 3, 1, 2),
    _QEventAlarmDateTime_Type()
)
qEventAlarmDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qEventAlarmDateTime.setStatus("mandatory")


class _QEventAlarmType_Type(Integer32):
    """Custom type qEventAlarmType based on Integer32"""
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
        *(("critical", 2),
          ("debug", 6),
          ("fatal", 1),
          ("informational", 5),
          ("mild", 3),
          ("standard-snmp", 4))
    )


_QEventAlarmType_Type.__name__ = "Integer32"
_QEventAlarmType_Object = MibTableColumn
qEventAlarmType = _QEventAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 8, 3, 1, 3),
    _QEventAlarmType_Type()
)
qEventAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qEventAlarmType.setStatus("mandatory")


class _QEventAlarmSubSystem_Type(Integer32):
    """Custom type qEventAlarmSubSystem based on Integer32"""
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
              25)
        )
    )
    namedValues = NamedValues(
        *(("arp-subsystem", 25),
          ("atm-subsystem", 3),
          ("circuit-subsystem", 24),
          ("clip-subsystem", 7),
          ("ethernet-subsystem", 4),
          ("flash-subsystem", 8),
          ("flow-subsystem", 9),
          ("general-subsystem", 1),
          ("get-subsystem", 12),
          ("icmp-subsystem", 16),
          ("igmp-subsystem", 17),
          ("ip-subsystem", 2),
          ("lif-subsystem", 23),
          ("lp-subsystem", 22),
          ("oam-subsystem", 13),
          ("ping-subsystem", 18),
          ("port-manager-subsystem", 11),
          ("reset-subsystem", 14),
          ("serial-subsystem", 10),
          ("snmp-subsystem", 19),
          ("tcp-subsystem", 20),
          ("telnet-subsystem", 6),
          ("tftp-subsystem", 5),
          ("time-subsystem", 15),
          ("upd-subsystem", 21))
    )


_QEventAlarmSubSystem_Type.__name__ = "Integer32"
_QEventAlarmSubSystem_Object = MibTableColumn
qEventAlarmSubSystem = _QEventAlarmSubSystem_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 8, 3, 1, 4),
    _QEventAlarmSubSystem_Type()
)
qEventAlarmSubSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qEventAlarmSubSystem.setStatus("mandatory")
_QEventAlarmID_Number_Type = Integer32
_QEventAlarmID_Number_Object = MibScalar
qEventAlarmID_Number = _QEventAlarmID_Number_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 8, 3, 1, 5),
    _QEventAlarmID_Number_Type()
)
qEventAlarmID_Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qEventAlarmID_Number.setStatus("mandatory")
_QEventAlarmDescription_Type = DisplayString
_QEventAlarmDescription_Object = MibTableColumn
qEventAlarmDescription = _QEventAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 8, 3, 1, 6),
    _QEventAlarmDescription_Type()
)
qEventAlarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qEventAlarmDescription.setStatus("mandatory")
_Qextmib_ObjectIdentity = ObjectIdentity
qextmib = _Qextmib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 9)
)
_QipExt_ObjectIdentity = ObjectIdentity
qipExt = _QipExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 9, 1)
)
_QipCircExtTable_Object = MibTable
qipCircExtTable = _QipCircExtTable_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 9, 1, 1)
)
if mibBuilder.loadTexts:
    qipCircExtTable.setStatus("mandatory")
_QipCircExtEntry_Object = MibTableRow
qipCircExtEntry = _QipCircExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 9, 1, 1, 1)
)
qipCircExtEntry.setIndexNames(
    (0, "QWESCOM-MIB", "qipCircExtIndex"),
)
if mibBuilder.loadTexts:
    qipCircExtEntry.setStatus("mandatory")
_QipCircExtIndex_Type = Integer32
_QipCircExtIndex_Object = MibTableColumn
qipCircExtIndex = _QipCircExtIndex_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 9, 1, 1, 1, 1),
    _QipCircExtIndex_Type()
)
qipCircExtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qipCircExtIndex.setStatus("mandatory")
_QipCircExtIfIndex_Type = Integer32
_QipCircExtIfIndex_Object = MibTableColumn
qipCircExtIfIndex = _QipCircExtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 9, 1, 1, 1, 2),
    _QipCircExtIfIndex_Type()
)
qipCircExtIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qipCircExtIfIndex.setStatus("mandatory")


class _QipCircExtAdminState_Type(Integer32):
    """Custom type qipCircExtAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_QipCircExtAdminState_Type.__name__ = "Integer32"
_QipCircExtAdminState_Object = MibTableColumn
qipCircExtAdminState = _QipCircExtAdminState_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 9, 1, 1, 1, 3),
    _QipCircExtAdminState_Type()
)
qipCircExtAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qipCircExtAdminState.setStatus("mandatory")


class _QipCircExtOperState_Type(Integer32):
    """Custom type qipCircExtOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_QipCircExtOperState_Type.__name__ = "Integer32"
_QipCircExtOperState_Object = MibTableColumn
qipCircExtOperState = _QipCircExtOperState_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 9, 1, 1, 1, 4),
    _QipCircExtOperState_Type()
)
qipCircExtOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qipCircExtOperState.setStatus("mandatory")
_QarpExt_ObjectIdentity = ObjectIdentity
qarpExt = _QarpExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 9, 2)
)
_QarpExtTtl_Type = Integer32
_QarpExtTtl_Object = MibScalar
qarpExtTtl = _QarpExtTtl_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 9, 2, 1),
    _QarpExtTtl_Type()
)
qarpExtTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qarpExtTtl.setStatus("mandatory")
_QarpCircExtTable_Object = MibTable
qarpCircExtTable = _QarpCircExtTable_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 9, 2, 2)
)
if mibBuilder.loadTexts:
    qarpCircExtTable.setStatus("mandatory")
_QarpCircExtEntry_Object = MibTableRow
qarpCircExtEntry = _QarpCircExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 9, 2, 2, 1)
)
qarpCircExtEntry.setIndexNames(
    (0, "QWESCOM-MIB", "qarpCircExtIndex"),
)
if mibBuilder.loadTexts:
    qarpCircExtEntry.setStatus("mandatory")
_QarpCircExtIndex_Type = Integer32
_QarpCircExtIndex_Object = MibTableColumn
qarpCircExtIndex = _QarpCircExtIndex_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 9, 2, 2, 1, 1),
    _QarpCircExtIndex_Type()
)
qarpCircExtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qarpCircExtIndex.setStatus("mandatory")
_QarpCircExtIfIndex_Type = Integer32
_QarpCircExtIfIndex_Object = MibTableColumn
qarpCircExtIfIndex = _QarpCircExtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 9, 2, 2, 1, 2),
    _QarpCircExtIfIndex_Type()
)
qarpCircExtIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qarpCircExtIfIndex.setStatus("mandatory")


class _QarpCircExtDoProxy_Type(Integer32):
    """Custom type qarpCircExtDoProxy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_QarpCircExtDoProxy_Type.__name__ = "Integer32"
_QarpCircExtDoProxy_Object = MibTableColumn
qarpCircExtDoProxy = _QarpCircExtDoProxy_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 9, 2, 2, 1, 3),
    _QarpCircExtDoProxy_Type()
)
qarpCircExtDoProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qarpCircExtDoProxy.setStatus("mandatory")


class _QarpCircExtDoResp_Type(Integer32):
    """Custom type qarpCircExtDoResp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_QarpCircExtDoResp_Type.__name__ = "Integer32"
_QarpCircExtDoResp_Object = MibTableColumn
qarpCircExtDoResp = _QarpCircExtDoResp_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 9, 2, 2, 1, 4),
    _QarpCircExtDoResp_Type()
)
qarpCircExtDoResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qarpCircExtDoResp.setStatus("mandatory")
_QripExt_ObjectIdentity = ObjectIdentity
qripExt = _QripExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 9, 3)
)


class _QripExtAdminState_Type(Integer32):
    """Custom type qripExtAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_QripExtAdminState_Type.__name__ = "Integer32"
_QripExtAdminState_Object = MibScalar
qripExtAdminState = _QripExtAdminState_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 9, 3, 1),
    _QripExtAdminState_Type()
)
qripExtAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qripExtAdminState.setStatus("mandatory")
_QripExtUpdateTime_Type = Integer32
_QripExtUpdateTime_Object = MibScalar
qripExtUpdateTime = _QripExtUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 9, 3, 2),
    _QripExtUpdateTime_Type()
)
qripExtUpdateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qripExtUpdateTime.setStatus("mandatory")
_QripCircExtTable_Object = MibTable
qripCircExtTable = _QripCircExtTable_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 9, 3, 3)
)
if mibBuilder.loadTexts:
    qripCircExtTable.setStatus("mandatory")
_QripCircExtEntry_Object = MibTableRow
qripCircExtEntry = _QripCircExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 9, 3, 3, 1)
)
qripCircExtEntry.setIndexNames(
    (0, "QWESCOM-MIB", "qripCircExtIndex"),
)
if mibBuilder.loadTexts:
    qripCircExtEntry.setStatus("mandatory")
_QripCircExtIndex_Type = Integer32
_QripCircExtIndex_Object = MibTableColumn
qripCircExtIndex = _QripCircExtIndex_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 9, 3, 3, 1, 1),
    _QripCircExtIndex_Type()
)
qripCircExtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qripCircExtIndex.setStatus("mandatory")
_QripCircExtIfIndex_Type = Integer32
_QripCircExtIfIndex_Object = MibTableColumn
qripCircExtIfIndex = _QripCircExtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 9, 3, 3, 1, 2),
    _QripCircExtIfIndex_Type()
)
qripCircExtIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qripCircExtIfIndex.setStatus("mandatory")


class _QripCircExtTalk_Type(Integer32):
    """Custom type qripCircExtTalk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_QripCircExtTalk_Type.__name__ = "Integer32"
_QripCircExtTalk_Object = MibTableColumn
qripCircExtTalk = _QripCircExtTalk_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 9, 3, 3, 1, 3),
    _QripCircExtTalk_Type()
)
qripCircExtTalk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qripCircExtTalk.setStatus("mandatory")


class _QripCircExtListen_Type(Integer32):
    """Custom type qripCircExtListen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_QripCircExtListen_Type.__name__ = "Integer32"
_QripCircExtListen_Object = MibTableColumn
qripCircExtListen = _QripCircExtListen_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 9, 3, 3, 1, 4),
    _QripCircExtListen_Type()
)
qripCircExtListen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qripCircExtListen.setStatus("mandatory")


class _QripCircExtPoison_Type(Integer32):
    """Custom type qripCircExtPoison based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_QripCircExtPoison_Type.__name__ = "Integer32"
_QripCircExtPoison_Object = MibTableColumn
qripCircExtPoison = _QripCircExtPoison_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 9, 3, 3, 1, 5),
    _QripCircExtPoison_Type()
)
qripCircExtPoison.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qripCircExtPoison.setStatus("mandatory")
_QmanufactRecord_ObjectIdentity = ObjectIdentity
qmanufactRecord = _QmanufactRecord_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 10)
)
_QmrCheckSum_Type = Counter32
_QmrCheckSum_Object = MibScalar
qmrCheckSum = _QmrCheckSum_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 10, 1),
    _QmrCheckSum_Type()
)
qmrCheckSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmrCheckSum.setStatus("mandatory")
_QmrBurnDate_Type = DisplayString
_QmrBurnDate_Object = MibScalar
qmrBurnDate = _QmrBurnDate_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 10, 2),
    _QmrBurnDate_Type()
)
qmrBurnDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmrBurnDate.setStatus("mandatory")
_QmrBurnTime_Type = DisplayString
_QmrBurnTime_Object = MibScalar
qmrBurnTime = _QmrBurnTime_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 10, 3),
    _QmrBurnTime_Type()
)
qmrBurnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmrBurnTime.setStatus("mandatory")
_QmrOemName_Type = DisplayString
_QmrOemName_Object = MibScalar
qmrOemName = _QmrOemName_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 10, 4),
    _QmrOemName_Type()
)
qmrOemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmrOemName.setStatus("mandatory")
_QmrOemID_Type = Counter32
_QmrOemID_Object = MibScalar
qmrOemID = _QmrOemID_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 10, 5),
    _QmrOemID_Type()
)
qmrOemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmrOemID.setStatus("mandatory")
_QmrSerialNumber_Type = Counter32
_QmrSerialNumber_Object = MibScalar
qmrSerialNumber = _QmrSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 10, 6),
    _QmrSerialNumber_Type()
)
qmrSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmrSerialNumber.setStatus("mandatory")


class _QmrProductID_Type(Integer32):
    """Custom type qmrProductID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("qwes-span", 1)
    )


_QmrProductID_Type.__name__ = "Integer32"
_QmrProductID_Object = MibScalar
qmrProductID = _QmrProductID_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 10, 7),
    _QmrProductID_Type()
)
qmrProductID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmrProductID.setStatus("mandatory")


class _QmrModelID_Type(Integer32):
    """Custom type qmrModelID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("prototype", 1),
          ("rev3", 2))
    )


_QmrModelID_Type.__name__ = "Integer32"
_QmrModelID_Object = MibScalar
qmrModelID = _QmrModelID_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 10, 8),
    _QmrModelID_Type()
)
qmrModelID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmrModelID.setStatus("mandatory")
_QmrMacAddress_Type = PhysAddress
_QmrMacAddress_Object = MibScalar
qmrMacAddress = _QmrMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 10, 9),
    _QmrMacAddress_Type()
)
qmrMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmrMacAddress.setStatus("mandatory")
_QmrRepairTable_Object = MibTable
qmrRepairTable = _QmrRepairTable_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 10, 10)
)
if mibBuilder.loadTexts:
    qmrRepairTable.setStatus("mandatory")
_QmrRepairEntry_Object = MibTableRow
qmrRepairEntry = _QmrRepairEntry_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 10, 10, 1)
)
qmrRepairEntry.setIndexNames(
    (0, "QWESCOM-MIB", "qmrRepType"),
    (0, "QWESCOM-MIB", "qmrRepCode"),
)
if mibBuilder.loadTexts:
    qmrRepairEntry.setStatus("mandatory")


class _QmrRepType_Type(Integer32):
    """Custom type qmrRepType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eco", 2),
          ("repair", 1))
    )


_QmrRepType_Type.__name__ = "Integer32"
_QmrRepType_Object = MibTableColumn
qmrRepType = _QmrRepType_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 10, 10, 1, 1),
    _QmrRepType_Type()
)
qmrRepType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmrRepType.setStatus("mandatory")
_QmrRepCode_Type = Counter32
_QmrRepCode_Object = MibTableColumn
qmrRepCode = _QmrRepCode_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 10, 10, 1, 2),
    _QmrRepCode_Type()
)
qmrRepCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmrRepCode.setStatus("mandatory")
_QmrRepDate_Type = DisplayString
_QmrRepDate_Object = MibTableColumn
qmrRepDate = _QmrRepDate_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 10, 10, 1, 3),
    _QmrRepDate_Type()
)
qmrRepDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmrRepDate.setStatus("mandatory")
_QmrRepTime_Type = DisplayString
_QmrRepTime_Object = MibTableColumn
qmrRepTime = _QmrRepTime_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 10, 10, 1, 4),
    _QmrRepTime_Type()
)
qmrRepTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmrRepTime.setStatus("mandatory")
_Qethernet_ObjectIdentity = ObjectIdentity
qethernet = _Qethernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 11)
)
_QethernetCfgTable_Object = MibTable
qethernetCfgTable = _QethernetCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 11, 1)
)
if mibBuilder.loadTexts:
    qethernetCfgTable.setStatus("mandatory")
_QethernetCfgEntry_Object = MibTableRow
qethernetCfgEntry = _QethernetCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 11, 1, 1)
)
qethernetCfgEntry.setIndexNames(
    (0, "QWESCOM-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    qethernetCfgEntry.setStatus("mandatory")
_QethernetMacAddress_Type = PhysAddress
_QethernetMacAddress_Object = MibTableColumn
qethernetMacAddress = _QethernetMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 11, 1, 1, 1),
    _QethernetMacAddress_Type()
)
qethernetMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qethernetMacAddress.setStatus("mandatory")


class _QethernetSpeedMode_Type(Integer32):
    """Custom type qethernetSpeedMode based on Integer32"""
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
        *(("full-duplex-10-mbps", 2),
          ("full-duplex-100-mbps", 1),
          ("half-duplex-10-mbps", 4),
          ("half-duplex-100-mbps", 3))
    )


_QethernetSpeedMode_Type.__name__ = "Integer32"
_QethernetSpeedMode_Object = MibTableColumn
qethernetSpeedMode = _QethernetSpeedMode_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 11, 1, 1, 2),
    _QethernetSpeedMode_Type()
)
qethernetSpeedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qethernetSpeedMode.setStatus("mandatory")


class _QethernetEncapsulation_Type(Integer32):
    """Custom type qethernetEncapsulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("etherv2encap", 1),
          ("ieee8023encap", 2))
    )


_QethernetEncapsulation_Type.__name__ = "Integer32"
_QethernetEncapsulation_Object = MibTableColumn
qethernetEncapsulation = _QethernetEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 11, 1, 1, 3),
    _QethernetEncapsulation_Type()
)
qethernetEncapsulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qethernetEncapsulation.setStatus("mandatory")


class _QethernetAutoSense_Type(Integer32):
    """Custom type qethernetAutoSense based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_QethernetAutoSense_Type.__name__ = "Integer32"
_QethernetAutoSense_Object = MibTableColumn
qethernetAutoSense = _QethernetAutoSense_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 11, 1, 1, 4),
    _QethernetAutoSense_Type()
)
qethernetAutoSense.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qethernetAutoSense.setStatus("mandatory")


class _QethernetName_Type(DisplayString):
    """Custom type qethernetName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QethernetName_Type.__name__ = "DisplayString"
_QethernetName_Object = MibTableColumn
qethernetName = _QethernetName_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 11, 1, 1, 5),
    _QethernetName_Type()
)
qethernetName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qethernetName.setStatus("mandatory")


class _QethernetCurrentSpeedMode_Type(Integer32):
    """Custom type qethernetCurrentSpeedMode based on Integer32"""
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
        *(("full-duplex-10-mbps", 2),
          ("full-duplex-100-mbps", 1),
          ("half-duplex-10-mbps", 4),
          ("half-duplex-100-mbps", 3),
          ("no-link", 5))
    )


_QethernetCurrentSpeedMode_Type.__name__ = "Integer32"
_QethernetCurrentSpeedMode_Object = MibScalar
qethernetCurrentSpeedMode = _QethernetCurrentSpeedMode_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 11, 1, 1, 6),
    _QethernetCurrentSpeedMode_Type()
)
qethernetCurrentSpeedMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qethernetCurrentSpeedMode.setStatus("mandatory")
_Qds1_e1_ObjectIdentity = ObjectIdentity
qds1_e1 = _Qds1_e1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 12)
)


class _Qds1AutoClockSourceSearching_Type(Integer32):
    """Custom type qds1AutoClockSourceSearching based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Qds1AutoClockSourceSearching_Type.__name__ = "Integer32"
_Qds1AutoClockSourceSearching_Object = MibScalar
qds1AutoClockSourceSearching = _Qds1AutoClockSourceSearching_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 12, 1),
    _Qds1AutoClockSourceSearching_Type()
)
qds1AutoClockSourceSearching.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qds1AutoClockSourceSearching.setStatus("mandatory")


class _Qds1PrimaryClockSource_Type(Integer32):
    """Custom type qds1PrimaryClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("span-1", 2),
          ("span-2", 3),
          ("span-3", 4),
          ("span-4", 5),
          ("span-5", 6),
          ("span-6", 7))
    )


_Qds1PrimaryClockSource_Type.__name__ = "Integer32"
_Qds1PrimaryClockSource_Object = MibScalar
qds1PrimaryClockSource = _Qds1PrimaryClockSource_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 12, 2),
    _Qds1PrimaryClockSource_Type()
)
qds1PrimaryClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qds1PrimaryClockSource.setStatus("mandatory")


class _Qds1PrimaryClockSourceAction_Type(Integer32):
    """Custom type qds1PrimaryClockSourceAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("restore-to-primary-source", 2),
          ("use-current-source", 1))
    )


_Qds1PrimaryClockSourceAction_Type.__name__ = "Integer32"
_Qds1PrimaryClockSourceAction_Object = MibScalar
qds1PrimaryClockSourceAction = _Qds1PrimaryClockSourceAction_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 12, 3),
    _Qds1PrimaryClockSourceAction_Type()
)
qds1PrimaryClockSourceAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qds1PrimaryClockSourceAction.setStatus("mandatory")
_Qds1SpanCfgTable_Object = MibTable
qds1SpanCfgTable = _Qds1SpanCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 12, 4)
)
if mibBuilder.loadTexts:
    qds1SpanCfgTable.setStatus("mandatory")
_Qds1SpanCfgEntry_Object = MibTableRow
qds1SpanCfgEntry = _Qds1SpanCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 12, 4, 1)
)
qds1SpanCfgEntry.setIndexNames(
    (0, "QWESCOM-MIB", "qds1LineCfgIndex"),
)
if mibBuilder.loadTexts:
    qds1SpanCfgEntry.setStatus("mandatory")
_Qds1LineCfgIndex_Type = Integer32
_Qds1LineCfgIndex_Object = MibTableColumn
qds1LineCfgIndex = _Qds1LineCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 12, 4, 1, 1),
    _Qds1LineCfgIndex_Type()
)
qds1LineCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qds1LineCfgIndex.setStatus("mandatory")


class _Qds1LineBuildOut_Type(Integer32):
    """Custom type qds1LineBuildOut based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("line-build-out-133-ft", 1),
          ("line-build-out-266-ft", 2),
          ("line-build-out-399-ft", 3),
          ("line-build-out-533-ft", 4),
          ("line-build-out-655-ft", 5),
          ("line-build-out-n15db", 7),
          ("line-build-out-n22-5db", 8),
          ("line-build-out-n7-5db", 6),
          ("not-applicable", 9))
    )


_Qds1LineBuildOut_Type.__name__ = "Integer32"
_Qds1LineBuildOut_Object = MibTableColumn
qds1LineBuildOut = _Qds1LineBuildOut_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 12, 4, 1, 2),
    _Qds1LineBuildOut_Type()
)
qds1LineBuildOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qds1LineBuildOut.setStatus("mandatory")


class _Qds1ClockSourceEligibility_Type(Integer32):
    """Custom type qds1ClockSourceEligibility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eligible", 1),
          ("ineligible", 2))
    )


_Qds1ClockSourceEligibility_Type.__name__ = "Integer32"
_Qds1ClockSourceEligibility_Object = MibTableColumn
qds1ClockSourceEligibility = _Qds1ClockSourceEligibility_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 12, 4, 1, 3),
    _Qds1ClockSourceEligibility_Type()
)
qds1ClockSourceEligibility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qds1ClockSourceEligibility.setStatus("mandatory")


class _Qds1ClockMode_Type(Integer32):
    """Custom type qds1ClockMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("providemasterclock", 2),
          ("slavetonetwork", 1))
    )


_Qds1ClockMode_Type.__name__ = "Integer32"
_Qds1ClockMode_Object = MibTableColumn
qds1ClockMode = _Qds1ClockMode_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 12, 4, 1, 4),
    _Qds1ClockMode_Type()
)
qds1ClockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qds1ClockMode.setStatus("mandatory")


class _Qds1PerformanceMonitor_Type(Integer32):
    """Custom type qds1PerformanceMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_Qds1PerformanceMonitor_Type.__name__ = "Integer32"
_Qds1PerformanceMonitor_Object = MibTableColumn
qds1PerformanceMonitor = _Qds1PerformanceMonitor_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 12, 4, 1, 5),
    _Qds1PerformanceMonitor_Type()
)
qds1PerformanceMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qds1PerformanceMonitor.setStatus("optional")


class _Qds1Scrambler_Type(Integer32):
    """Custom type qds1Scrambler based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_Qds1Scrambler_Type.__name__ = "Integer32"
_Qds1Scrambler_Object = MibTableColumn
qds1Scrambler = _Qds1Scrambler_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 12, 4, 1, 6),
    _Qds1Scrambler_Type()
)
qds1Scrambler.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qds1Scrambler.setStatus("optional")
_Qds1SpanLoopBackCmdTable_Object = MibTable
qds1SpanLoopBackCmdTable = _Qds1SpanLoopBackCmdTable_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 12, 5)
)
if mibBuilder.loadTexts:
    qds1SpanLoopBackCmdTable.setStatus("mandatory")
_Qds1SpanLoopBackCmdEntry_Object = MibTableRow
qds1SpanLoopBackCmdEntry = _Qds1SpanLoopBackCmdEntry_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 12, 5, 1)
)
qds1SpanLoopBackCmdEntry.setIndexNames(
    (0, "QWESCOM-MIB", "qds1LineLoopbackIndex"),
)
if mibBuilder.loadTexts:
    qds1SpanLoopBackCmdEntry.setStatus("mandatory")
_Qds1LineLoopbackIndex_Type = Integer32
_Qds1LineLoopbackIndex_Object = MibTableColumn
qds1LineLoopbackIndex = _Qds1LineLoopbackIndex_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 12, 5, 1, 1),
    _Qds1LineLoopbackIndex_Type()
)
qds1LineLoopbackIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qds1LineLoopbackIndex.setStatus("mandatory")


class _Qds1LoopbackCommand_Type(Integer32):
    """Custom type qds1LoopbackCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activate", 1),
          ("deactivate", 2))
    )


_Qds1LoopbackCommand_Type.__name__ = "Integer32"
_Qds1LoopbackCommand_Object = MibTableColumn
qds1LoopbackCommand = _Qds1LoopbackCommand_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 12, 5, 1, 2),
    _Qds1LoopbackCommand_Type()
)
qds1LoopbackCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qds1LoopbackCommand.setStatus("mandatory")


class _Qds1LoopbackDuration_Type(Integer32):
    """Custom type qds1LoopbackDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_Qds1LoopbackDuration_Type.__name__ = "Integer32"
_Qds1LoopbackDuration_Object = MibTableColumn
qds1LoopbackDuration = _Qds1LoopbackDuration_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 12, 5, 1, 3),
    _Qds1LoopbackDuration_Type()
)
qds1LoopbackDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qds1LoopbackDuration.setStatus("mandatory")
_Qds1SpanLoopBackStatsTable_Object = MibTable
qds1SpanLoopBackStatsTable = _Qds1SpanLoopBackStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 12, 6)
)
if mibBuilder.loadTexts:
    qds1SpanLoopBackStatsTable.setStatus("mandatory")
_Qds1SpanLoopBackStatsEntry_Object = MibTableRow
qds1SpanLoopBackStatsEntry = _Qds1SpanLoopBackStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 12, 6, 1)
)
qds1SpanLoopBackStatsEntry.setIndexNames(
    (0, "QWESCOM-MIB", "qds1LineLoopbackStatIndex"),
)
if mibBuilder.loadTexts:
    qds1SpanLoopBackStatsEntry.setStatus("mandatory")
_Qds1LineLoopbackStatIndex_Type = Integer32
_Qds1LineLoopbackStatIndex_Object = MibTableColumn
qds1LineLoopbackStatIndex = _Qds1LineLoopbackStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 12, 6, 1, 1),
    _Qds1LineLoopbackStatIndex_Type()
)
qds1LineLoopbackStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qds1LineLoopbackStatIndex.setStatus("mandatory")
_Qds1OamSegmentSent_Type = Counter32
_Qds1OamSegmentSent_Object = MibTableColumn
qds1OamSegmentSent = _Qds1OamSegmentSent_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 12, 6, 1, 2),
    _Qds1OamSegmentSent_Type()
)
qds1OamSegmentSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qds1OamSegmentSent.setStatus("mandatory")
_Qds1OamSegmentReceived_Type = Counter32
_Qds1OamSegmentReceived_Object = MibTableColumn
qds1OamSegmentReceived = _Qds1OamSegmentReceived_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 12, 6, 1, 3),
    _Qds1OamSegmentReceived_Type()
)
qds1OamSegmentReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qds1OamSegmentReceived.setStatus("mandatory")
_Qds1OamSegmentFailures_Type = Counter32
_Qds1OamSegmentFailures_Object = MibTableColumn
qds1OamSegmentFailures = _Qds1OamSegmentFailures_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 12, 6, 1, 4),
    _Qds1OamSegmentFailures_Type()
)
qds1OamSegmentFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qds1OamSegmentFailures.setStatus("mandatory")
_Qds10amRunnigTime_Type = Counter32
_Qds10amRunnigTime_Object = MibTableColumn
qds10amRunnigTime = _Qds10amRunnigTime_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 12, 6, 1, 5),
    _Qds10amRunnigTime_Type()
)
qds10amRunnigTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qds10amRunnigTime.setStatus("mandatory")
_QconfigManager_ObjectIdentity = ObjectIdentity
qconfigManager = _QconfigManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 13)
)


class _QcmSystemFile_Type(DisplayString):
    """Custom type qcmSystemFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_QcmSystemFile_Type.__name__ = "DisplayString"
_QcmSystemFile_Object = MibScalar
qcmSystemFile = _QcmSystemFile_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 13, 1),
    _QcmSystemFile_Type()
)
qcmSystemFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qcmSystemFile.setStatus("mandatory")
_QcmConfigMaxEntries_Type = Counter32
_QcmConfigMaxEntries_Object = MibScalar
qcmConfigMaxEntries = _QcmConfigMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 13, 2),
    _QcmConfigMaxEntries_Type()
)
qcmConfigMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qcmConfigMaxEntries.setStatus("mandatory")
_QcmConfigTable_Object = MibTable
qcmConfigTable = _QcmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 13, 3)
)
if mibBuilder.loadTexts:
    qcmConfigTable.setStatus("mandatory")
_QcmConfigEntry_Object = MibTableRow
qcmConfigEntry = _QcmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 13, 3, 1)
)
qcmConfigEntry.setIndexNames(
    (0, "QWESCOM-MIB", "qcmTableIndex"),
)
if mibBuilder.loadTexts:
    qcmConfigEntry.setStatus("mandatory")


class _QcmTableIndex_Type(Integer32):
    """Custom type qcmTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_QcmTableIndex_Type.__name__ = "Integer32"
_QcmTableIndex_Object = MibTableColumn
qcmTableIndex = _QcmTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 13, 3, 1, 1),
    _QcmTableIndex_Type()
)
qcmTableIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qcmTableIndex.setStatus("mandatory")


class _QcmCurrentConfig_Type(Integer32):
    """Custom type qcmCurrentConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_QcmCurrentConfig_Type.__name__ = "Integer32"
_QcmCurrentConfig_Object = MibTableColumn
qcmCurrentConfig = _QcmCurrentConfig_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 13, 3, 1, 2),
    _QcmCurrentConfig_Type()
)
qcmCurrentConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qcmCurrentConfig.setStatus("mandatory")


class _QcmActionOnConfig_Type(Integer32):
    """Custom type qcmActionOnConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("activatelater", 3),
          ("activatenow", 2),
          ("delete", 1),
          ("none", 0),
          ("save", 4),
          ("saveas", 5))
    )


_QcmActionOnConfig_Type.__name__ = "Integer32"
_QcmActionOnConfig_Object = MibTableColumn
qcmActionOnConfig = _QcmActionOnConfig_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 13, 3, 1, 3),
    _QcmActionOnConfig_Type()
)
qcmActionOnConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qcmActionOnConfig.setStatus("mandatory")


class _QcmFileAlias_Type(DisplayString):
    """Custom type qcmFileAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_QcmFileAlias_Type.__name__ = "DisplayString"
_QcmFileAlias_Object = MibTableColumn
qcmFileAlias = _QcmFileAlias_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 13, 3, 1, 4),
    _QcmFileAlias_Type()
)
qcmFileAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qcmFileAlias.setStatus("mandatory")


class _QcmRelease_Type(DisplayString):
    """Custom type qcmRelease based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_QcmRelease_Type.__name__ = "DisplayString"
_QcmRelease_Object = MibTableColumn
qcmRelease = _QcmRelease_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 13, 3, 1, 5),
    _QcmRelease_Type()
)
qcmRelease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qcmRelease.setStatus("mandatory")


class _QcmConfigFile_Type(DisplayString):
    """Custom type qcmConfigFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_QcmConfigFile_Type.__name__ = "DisplayString"
_QcmConfigFile_Object = MibTableColumn
qcmConfigFile = _QcmConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 13, 3, 1, 6),
    _QcmConfigFile_Type()
)
qcmConfigFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qcmConfigFile.setStatus("mandatory")


class _QcmBootSequence_Type(DisplayString):
    """Custom type qcmBootSequence based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_QcmBootSequence_Type.__name__ = "DisplayString"
_QcmBootSequence_Object = MibTableColumn
qcmBootSequence = _QcmBootSequence_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 13, 3, 1, 7),
    _QcmBootSequence_Type()
)
qcmBootSequence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qcmBootSequence.setStatus("mandatory")


class _QcmCreateDateTime_Type(DisplayString):
    """Custom type qcmCreateDateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_QcmCreateDateTime_Type.__name__ = "DisplayString"
_QcmCreateDateTime_Object = MibTableColumn
qcmCreateDateTime = _QcmCreateDateTime_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 13, 3, 1, 8),
    _QcmCreateDateTime_Type()
)
qcmCreateDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qcmCreateDateTime.setStatus("mandatory")


class _QcmOperSchedDateTime_Type(DisplayString):
    """Custom type qcmOperSchedDateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_QcmOperSchedDateTime_Type.__name__ = "DisplayString"
_QcmOperSchedDateTime_Object = MibTableColumn
qcmOperSchedDateTime = _QcmOperSchedDateTime_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 13, 3, 1, 9),
    _QcmOperSchedDateTime_Type()
)
qcmOperSchedDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qcmOperSchedDateTime.setStatus("mandatory")
_QcmReleaseTable_Object = MibTable
qcmReleaseTable = _QcmReleaseTable_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 13, 4)
)
if mibBuilder.loadTexts:
    qcmReleaseTable.setStatus("mandatory")
_QcmReleaseEntry_Object = MibTableRow
qcmReleaseEntry = _QcmReleaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 13, 4, 1)
)
qcmReleaseEntry.setIndexNames(
    (0, "QWESCOM-MIB", "qcmReleaseIndex"),
)
if mibBuilder.loadTexts:
    qcmReleaseEntry.setStatus("mandatory")


class _QcmReleaseIndex_Type(Integer32):
    """Custom type qcmReleaseIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_QcmReleaseIndex_Type.__name__ = "Integer32"
_QcmReleaseIndex_Object = MibTableColumn
qcmReleaseIndex = _QcmReleaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 13, 4, 1, 1),
    _QcmReleaseIndex_Type()
)
qcmReleaseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qcmReleaseIndex.setStatus("mandatory")


class _QcmReleaseName_Type(DisplayString):
    """Custom type qcmReleaseName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_QcmReleaseName_Type.__name__ = "DisplayString"
_QcmReleaseName_Object = MibTableColumn
qcmReleaseName = _QcmReleaseName_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 13, 4, 1, 2),
    _QcmReleaseName_Type()
)
qcmReleaseName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qcmReleaseName.setStatus("mandatory")


class _QcmReleaseVersion_Type(Integer32):
    """Custom type qcmReleaseVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_QcmReleaseVersion_Type.__name__ = "Integer32"
_QcmReleaseVersion_Object = MibTableColumn
qcmReleaseVersion = _QcmReleaseVersion_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 13, 4, 1, 3),
    _QcmReleaseVersion_Type()
)
qcmReleaseVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qcmReleaseVersion.setStatus("mandatory")
_QcmConfigVerTable_Object = MibTable
qcmConfigVerTable = _QcmConfigVerTable_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 13, 5)
)
if mibBuilder.loadTexts:
    qcmConfigVerTable.setStatus("mandatory")
_QcmConfigVerEntry_Object = MibTableRow
qcmConfigVerEntry = _QcmConfigVerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 13, 5, 1)
)
qcmConfigVerEntry.setIndexNames(
    (0, "QWESCOM-MIB", "qcmConfigVerIndex"),
)
if mibBuilder.loadTexts:
    qcmConfigVerEntry.setStatus("mandatory")


class _QcmConfigVerIndex_Type(Integer32):
    """Custom type qcmConfigVerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_QcmConfigVerIndex_Type.__name__ = "Integer32"
_QcmConfigVerIndex_Object = MibTableColumn
qcmConfigVerIndex = _QcmConfigVerIndex_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 13, 5, 1, 1),
    _QcmConfigVerIndex_Type()
)
qcmConfigVerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qcmConfigVerIndex.setStatus("mandatory")


class _QcmConfigName_Type(DisplayString):
    """Custom type qcmConfigName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_QcmConfigName_Type.__name__ = "DisplayString"
_QcmConfigName_Object = MibTableColumn
qcmConfigName = _QcmConfigName_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 13, 5, 1, 2),
    _QcmConfigName_Type()
)
qcmConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qcmConfigName.setStatus("mandatory")


class _QcmConfigVersion_Type(Integer32):
    """Custom type qcmConfigVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_QcmConfigVersion_Type.__name__ = "Integer32"
_QcmConfigVersion_Object = MibTableColumn
qcmConfigVersion = _QcmConfigVersion_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 13, 5, 1, 3),
    _QcmConfigVersion_Type()
)
qcmConfigVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qcmConfigVersion.setStatus("mandatory")


class _QcmConfigWorkWithMin_Type(Integer32):
    """Custom type qcmConfigWorkWithMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_QcmConfigWorkWithMin_Type.__name__ = "Integer32"
_QcmConfigWorkWithMin_Object = MibTableColumn
qcmConfigWorkWithMin = _QcmConfigWorkWithMin_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 13, 5, 1, 4),
    _QcmConfigWorkWithMin_Type()
)
qcmConfigWorkWithMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qcmConfigWorkWithMin.setStatus("mandatory")


class _QcmConfigWorkWithMax_Type(Integer32):
    """Custom type qcmConfigWorkWithMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_QcmConfigWorkWithMax_Type.__name__ = "Integer32"
_QcmConfigWorkWithMax_Object = MibTableColumn
qcmConfigWorkWithMax = _QcmConfigWorkWithMax_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 13, 5, 1, 5),
    _QcmConfigWorkWithMax_Type()
)
qcmConfigWorkWithMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qcmConfigWorkWithMax.setStatus("mandatory")


class _QcmWhichFile_Type(Integer32):
    """Custom type qcmWhichFile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("base", 1),
          ("default", 3),
          ("new", 2),
          ("operational", 0))
    )


_QcmWhichFile_Type.__name__ = "Integer32"
_QcmWhichFile_Object = MibScalar
qcmWhichFile = _QcmWhichFile_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 13, 6),
    _QcmWhichFile_Type()
)
qcmWhichFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qcmWhichFile.setStatus("mandatory")


class _QcmUserBaseCfgFile_Type(DisplayString):
    """Custom type qcmUserBaseCfgFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_QcmUserBaseCfgFile_Type.__name__ = "DisplayString"
_QcmUserBaseCfgFile_Object = MibScalar
qcmUserBaseCfgFile = _QcmUserBaseCfgFile_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 13, 7),
    _QcmUserBaseCfgFile_Type()
)
qcmUserBaseCfgFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qcmUserBaseCfgFile.setStatus("mandatory")


class _QcmUserNewCfgFile_Type(DisplayString):
    """Custom type qcmUserNewCfgFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_QcmUserNewCfgFile_Type.__name__ = "DisplayString"
_QcmUserNewCfgFile_Object = MibScalar
qcmUserNewCfgFile = _QcmUserNewCfgFile_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 13, 8),
    _QcmUserNewCfgFile_Type()
)
qcmUserNewCfgFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qcmUserNewCfgFile.setStatus("mandatory")


class _QcmUserFileAlias_Type(DisplayString):
    """Custom type qcmUserFileAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_QcmUserFileAlias_Type.__name__ = "DisplayString"
_QcmUserFileAlias_Object = MibScalar
qcmUserFileAlias = _QcmUserFileAlias_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 13, 9),
    _QcmUserFileAlias_Type()
)
qcmUserFileAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qcmUserFileAlias.setStatus("mandatory")


class _QcmUserRelease_Type(DisplayString):
    """Custom type qcmUserRelease based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_QcmUserRelease_Type.__name__ = "DisplayString"
_QcmUserRelease_Object = MibScalar
qcmUserRelease = _QcmUserRelease_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 13, 10),
    _QcmUserRelease_Type()
)
qcmUserRelease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qcmUserRelease.setStatus("mandatory")


class _QcmUserBootSequence_Type(DisplayString):
    """Custom type qcmUserBootSequence based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_QcmUserBootSequence_Type.__name__ = "DisplayString"
_QcmUserBootSequence_Object = MibScalar
qcmUserBootSequence = _QcmUserBootSequence_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 13, 11),
    _QcmUserBootSequence_Type()
)
qcmUserBootSequence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qcmUserBootSequence.setStatus("mandatory")


class _QcmUserDateTime_Type(DisplayString):
    """Custom type qcmUserDateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_QcmUserDateTime_Type.__name__ = "DisplayString"
_QcmUserDateTime_Object = MibScalar
qcmUserDateTime = _QcmUserDateTime_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 13, 12),
    _QcmUserDateTime_Type()
)
qcmUserDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qcmUserDateTime.setStatus("mandatory")


class _QcmStartConfig_Type(Integer32):
    """Custom type qcmStartConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_QcmStartConfig_Type.__name__ = "Integer32"
_QcmStartConfig_Object = MibScalar
qcmStartConfig = _QcmStartConfig_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 13, 13),
    _QcmStartConfig_Type()
)
qcmStartConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qcmStartConfig.setStatus("mandatory")


class _QcmStopConfig_Type(Integer32):
    """Custom type qcmStopConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_QcmStopConfig_Type.__name__ = "Integer32"
_QcmStopConfig_Object = MibScalar
qcmStopConfig = _QcmStopConfig_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 13, 14),
    _QcmStopConfig_Type()
)
qcmStopConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qcmStopConfig.setStatus("mandatory")


class _QcmStartViewConfig_Type(Integer32):
    """Custom type qcmStartViewConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_QcmStartViewConfig_Type.__name__ = "Integer32"
_QcmStartViewConfig_Object = MibScalar
qcmStartViewConfig = _QcmStartViewConfig_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 13, 15),
    _QcmStartViewConfig_Type()
)
qcmStartViewConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qcmStartViewConfig.setStatus("mandatory")


class _QcmStopViewConfig_Type(Integer32):
    """Custom type qcmStopViewConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_QcmStopViewConfig_Type.__name__ = "Integer32"
_QcmStopViewConfig_Object = MibScalar
qcmStopViewConfig = _QcmStopViewConfig_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 13, 16),
    _QcmStopViewConfig_Type()
)
qcmStopViewConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qcmStopViewConfig.setStatus("mandatory")


class _QcmCancelConfig_Type(Integer32):
    """Custom type qcmCancelConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_QcmCancelConfig_Type.__name__ = "Integer32"
_QcmCancelConfig_Object = MibScalar
qcmCancelConfig = _QcmCancelConfig_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 13, 17),
    _QcmCancelConfig_Type()
)
qcmCancelConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qcmCancelConfig.setStatus("mandatory")
_QportManagement_ObjectIdentity = ObjectIdentity
qportManagement = _QportManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 15)
)
_QwesLpTable_Object = MibTable
qwesLpTable = _QwesLpTable_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 15, 1)
)
if mibBuilder.loadTexts:
    qwesLpTable.setStatus("mandatory")
_QwesLpEntry_Object = MibTableRow
qwesLpEntry = _QwesLpEntry_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 15, 1, 1)
)
qwesLpEntry.setIndexNames(
    (0, "QWESCOM-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    qwesLpEntry.setStatus("mandatory")


class _QwesLpName_Type(DisplayString):
    """Custom type qwesLpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QwesLpName_Type.__name__ = "DisplayString"
_QwesLpName_Object = MibTableColumn
qwesLpName = _QwesLpName_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 15, 1, 1, 1),
    _QwesLpName_Type()
)
qwesLpName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qwesLpName.setStatus("current")


class _QwesLpAlias_Type(DisplayString):
    """Custom type qwesLpAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QwesLpAlias_Type.__name__ = "DisplayString"
_QwesLpAlias_Object = MibTableColumn
qwesLpAlias = _QwesLpAlias_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 15, 1, 1, 2),
    _QwesLpAlias_Type()
)
qwesLpAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qwesLpAlias.setStatus("current")


class _QwesLpPhysicalInterface_Type(Integer32):
    """Custom type qwesLpPhysicalInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_QwesLpPhysicalInterface_Type.__name__ = "Integer32"
_QwesLpPhysicalInterface_Object = MibTableColumn
qwesLpPhysicalInterface = _QwesLpPhysicalInterface_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 15, 1, 1, 3),
    _QwesLpPhysicalInterface_Type()
)
qwesLpPhysicalInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qwesLpPhysicalInterface.setStatus("mandatory")


class _QwesLpDataLinkInterface_Type(Integer32):
    """Custom type qwesLpDataLinkInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 88),
    )


_QwesLpDataLinkInterface_Type.__name__ = "Integer32"
_QwesLpDataLinkInterface_Object = MibTableColumn
qwesLpDataLinkInterface = _QwesLpDataLinkInterface_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 15, 1, 1, 4),
    _QwesLpDataLinkInterface_Type()
)
qwesLpDataLinkInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qwesLpDataLinkInterface.setStatus("mandatory")


class _QwesLpTrapStatus_Type(Integer32):
    """Custom type qwesLpTrapStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_QwesLpTrapStatus_Type.__name__ = "Integer32"
_QwesLpTrapStatus_Object = MibTableColumn
qwesLpTrapStatus = _QwesLpTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 15, 1, 1, 5),
    _QwesLpTrapStatus_Type()
)
qwesLpTrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qwesLpTrapStatus.setStatus("mandatory")


class _QwesLpAdminStatus_Type(Integer32):
    """Custom type qwesLpAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_QwesLpAdminStatus_Type.__name__ = "Integer32"
_QwesLpAdminStatus_Object = MibTableColumn
qwesLpAdminStatus = _QwesLpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 15, 1, 1, 6),
    _QwesLpAdminStatus_Type()
)
qwesLpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qwesLpAdminStatus.setStatus("mandatory")
_QwesLpRowStatus_Type = RowStatus
_QwesLpRowStatus_Object = MibTableColumn
qwesLpRowStatus = _QwesLpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 15, 1, 1, 7),
    _QwesLpRowStatus_Type()
)
qwesLpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qwesLpRowStatus.setStatus("mandatory")
_QwesLifTable_Object = MibTable
qwesLifTable = _QwesLifTable_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 15, 2)
)
if mibBuilder.loadTexts:
    qwesLifTable.setStatus("mandatory")
_QwesLifEntry_Object = MibTableRow
qwesLifEntry = _QwesLifEntry_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 15, 2, 1)
)
qwesLifEntry.setIndexNames(
    (0, "QWESCOM-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    qwesLifEntry.setStatus("mandatory")


class _QwesLifName_Type(DisplayString):
    """Custom type qwesLifName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QwesLifName_Type.__name__ = "DisplayString"
_QwesLifName_Object = MibTableColumn
qwesLifName = _QwesLifName_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 15, 2, 1, 1),
    _QwesLifName_Type()
)
qwesLifName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qwesLifName.setStatus("current")


class _QwesLifAlias_Type(DisplayString):
    """Custom type qwesLifAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QwesLifAlias_Type.__name__ = "DisplayString"
_QwesLifAlias_Object = MibTableColumn
qwesLifAlias = _QwesLifAlias_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 15, 2, 1, 2),
    _QwesLifAlias_Type()
)
qwesLifAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qwesLifAlias.setStatus("current")


class _QwesLifLpIndex_Type(Integer32):
    """Custom type qwesLifLpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(257, 512),
    )


_QwesLifLpIndex_Type.__name__ = "Integer32"
_QwesLifLpIndex_Object = MibTableColumn
qwesLifLpIndex = _QwesLifLpIndex_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 15, 2, 1, 3),
    _QwesLifLpIndex_Type()
)
qwesLifLpIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qwesLifLpIndex.setStatus("mandatory")


class _QwesLifTrapStatus_Type(Integer32):
    """Custom type qwesLifTrapStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_QwesLifTrapStatus_Type.__name__ = "Integer32"
_QwesLifTrapStatus_Object = MibTableColumn
qwesLifTrapStatus = _QwesLifTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 15, 2, 1, 4),
    _QwesLifTrapStatus_Type()
)
qwesLifTrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qwesLifTrapStatus.setStatus("mandatory")


class _QwesLifAdminStatus_Type(Integer32):
    """Custom type qwesLifAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_QwesLifAdminStatus_Type.__name__ = "Integer32"
_QwesLifAdminStatus_Object = MibTableColumn
qwesLifAdminStatus = _QwesLifAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 15, 2, 1, 5),
    _QwesLifAdminStatus_Type()
)
qwesLifAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qwesLifAdminStatus.setStatus("mandatory")
_QwesLifRowStatus_Type = RowStatus
_QwesLifRowStatus_Object = MibTableColumn
qwesLifRowStatus = _QwesLifRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 15, 2, 1, 6),
    _QwesLifRowStatus_Type()
)
qwesLifRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qwesLifRowStatus.setStatus("mandatory")
_QwesAtmArpTable_Object = MibTable
qwesAtmArpTable = _QwesAtmArpTable_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 15, 3)
)
if mibBuilder.loadTexts:
    qwesAtmArpTable.setStatus("mandatory")
_QwesAtmArpEntry_Object = MibTableRow
qwesAtmArpEntry = _QwesAtmArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 15, 3, 1)
)
qwesAtmArpEntry.setIndexNames(
    (0, "QWESCOM-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    qwesAtmArpEntry.setStatus("mandatory")
_QwesAtmArpLifIndex_Type = Integer32
_QwesAtmArpLifIndex_Object = MibTableColumn
qwesAtmArpLifIndex = _QwesAtmArpLifIndex_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 15, 3, 1, 1),
    _QwesAtmArpLifIndex_Type()
)
qwesAtmArpLifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qwesAtmArpLifIndex.setStatus("mandatory")
_Qip_ObjectIdentity = ObjectIdentity
qip = _Qip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16)
)
_QipPortTable_Object = MibTable
qipPortTable = _QipPortTable_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 1)
)
if mibBuilder.loadTexts:
    qipPortTable.setStatus("mandatory")
_QipPortEntry_Object = MibTableRow
qipPortEntry = _QipPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 1, 1)
)
qipPortEntry.setIndexNames(
    (0, "QWESCOM-MIB", "qIpLp"),
)
if mibBuilder.loadTexts:
    qipPortEntry.setStatus("mandatory")
_QIpLp_Type = Integer32
_QIpLp_Object = MibTableColumn
qIpLp = _QIpLp_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 1, 1, 1),
    _QIpLp_Type()
)
qIpLp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qIpLp.setStatus("current")
_QIpAddr_Type = IpAddress
_QIpAddr_Object = MibTableColumn
qIpAddr = _QIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 1, 1, 2),
    _QIpAddr_Type()
)
qIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qIpAddr.setStatus("mandatory")
_QIpSubnet_Type = IpAddress
_QIpSubnet_Object = MibTableColumn
qIpSubnet = _QIpSubnet_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 1, 1, 3),
    _QIpSubnet_Type()
)
qIpSubnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qIpSubnet.setStatus("mandatory")


class _QIpMulticast_Type(Integer32):
    """Custom type qIpMulticast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_QIpMulticast_Type.__name__ = "Integer32"
_QIpMulticast_Object = MibTableColumn
qIpMulticast = _QIpMulticast_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 1, 1, 4),
    _QIpMulticast_Type()
)
qIpMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qIpMulticast.setStatus("current")


class _QIpRipStatus_Type(Integer32):
    """Custom type qIpRipStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_QIpRipStatus_Type.__name__ = "Integer32"
_QIpRipStatus_Object = MibTableColumn
qIpRipStatus = _QIpRipStatus_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 1, 1, 5),
    _QIpRipStatus_Type()
)
qIpRipStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qIpRipStatus.setStatus("current")
_QIpArpTimeout_Type = Integer32
_QIpArpTimeout_Object = MibTableColumn
qIpArpTimeout = _QIpArpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 1, 1, 6),
    _QIpArpTimeout_Type()
)
qIpArpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qIpArpTimeout.setStatus("current")


class _QIpEncap_Type(Integer32):
    """Custom type qIpEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hp", 2),
          ("standard", 1))
    )


_QIpEncap_Type.__name__ = "Integer32"
_QIpEncap_Object = MibTableColumn
qIpEncap = _QIpEncap_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 1, 1, 7),
    _QIpEncap_Type()
)
qIpEncap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qIpEncap.setStatus("current")
_QRipPortTable_Object = MibTable
qRipPortTable = _QRipPortTable_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 2)
)
if mibBuilder.loadTexts:
    qRipPortTable.setStatus("mandatory")
_QRipPortEntry_Object = MibTableRow
qRipPortEntry = _QRipPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 2, 1)
)
qRipPortEntry.setIndexNames(
    (0, "QWESCOM-MIB", "qRipIpAddr"),
)
if mibBuilder.loadTexts:
    qRipPortEntry.setStatus("mandatory")
_QRipIpAddr_Type = IpAddress
_QRipIpAddr_Object = MibTableColumn
qRipIpAddr = _QRipIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 2, 1, 1),
    _QRipIpAddr_Type()
)
qRipIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qRipIpAddr.setStatus("mandatory")


class _QMode_Type(Integer32):
    """Custom type qMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("md5", 3),
          ("none", 1),
          ("password", 2))
    )


_QMode_Type.__name__ = "Integer32"
_QMode_Object = MibTableColumn
qMode = _QMode_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 2, 1, 2),
    _QMode_Type()
)
qMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qMode.setStatus("current")


class _QAuthentication_Type(DisplayString):
    """Custom type qAuthentication based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_QAuthentication_Type.__name__ = "DisplayString"
_QAuthentication_Object = MibTableColumn
qAuthentication = _QAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 2, 1, 3),
    _QAuthentication_Type()
)
qAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qAuthentication.setStatus("current")


class _QSplitHorizon_Type(Integer32):
    """Custom type qSplitHorizon based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("poisoned-reverse", 1),
          ("simple", 2))
    )


_QSplitHorizon_Type.__name__ = "Integer32"
_QSplitHorizon_Object = MibTableColumn
qSplitHorizon = _QSplitHorizon_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 2, 1, 4),
    _QSplitHorizon_Type()
)
qSplitHorizon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qSplitHorizon.setStatus("current")


class _QAdvertiseStaticRoutes_Type(Integer32):
    """Custom type qAdvertiseStaticRoutes based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_QAdvertiseStaticRoutes_Type.__name__ = "Integer32"
_QAdvertiseStaticRoutes_Object = MibTableColumn
qAdvertiseStaticRoutes = _QAdvertiseStaticRoutes_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 2, 1, 5),
    _QAdvertiseStaticRoutes_Type()
)
qAdvertiseStaticRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qAdvertiseStaticRoutes.setStatus("current")


class _QAdvertiseIntf_Type(Integer32):
    """Custom type qAdvertiseIntf based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_QAdvertiseIntf_Type.__name__ = "Integer32"
_QAdvertiseIntf_Object = MibTableColumn
qAdvertiseIntf = _QAdvertiseIntf_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 2, 1, 6),
    _QAdvertiseIntf_Type()
)
qAdvertiseIntf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qAdvertiseIntf.setStatus("current")


class _QBroadcastType_Type(Integer32):
    """Custom type qBroadcastType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("direct-with-ones", 2),
          ("direct-with-zeros", 3),
          ("local", 1))
    )


_QBroadcastType_Type.__name__ = "Integer32"
_QBroadcastType_Object = MibTableColumn
qBroadcastType = _QBroadcastType_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 2, 1, 7),
    _QBroadcastType_Type()
)
qBroadcastType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qBroadcastType.setStatus("current")


class _QHoldDownInterval_Type(Integer32):
    """Custom type qHoldDownInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_QHoldDownInterval_Type.__name__ = "Integer32"
_QHoldDownInterval_Object = MibTableColumn
qHoldDownInterval = _QHoldDownInterval_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 2, 1, 8),
    _QHoldDownInterval_Type()
)
qHoldDownInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qHoldDownInterval.setStatus("current")


class _QUpdatesSend_Type(Integer32):
    """Custom type qUpdatesSend based on Integer32"""
    defaultValue = 2

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
        *(("rip-1-compatible", 3),
          ("silent", 1),
          ("version-1", 2),
          ("version-1-demand", 5),
          ("version-2", 4),
          ("version-2-demand", 6))
    )


_QUpdatesSend_Type.__name__ = "Integer32"
_QUpdatesSend_Object = MibTableColumn
qUpdatesSend = _QUpdatesSend_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 2, 1, 9),
    _QUpdatesSend_Type()
)
qUpdatesSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qUpdatesSend.setStatus("current")


class _QUpdatesReceive_Type(Integer32):
    """Custom type qUpdatesReceive based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 3),
          ("rip1", 1),
          ("rip1-or-rip2", 3),
          ("rip2", 2))
    )


_QUpdatesReceive_Type.__name__ = "Integer32"
_QUpdatesReceive_Object = MibTableColumn
qUpdatesReceive = _QUpdatesReceive_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 2, 1, 10),
    _QUpdatesReceive_Type()
)
qUpdatesReceive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qUpdatesReceive.setStatus("current")


class _QDefaultRouteMetric_Type(Integer32):
    """Custom type qDefaultRouteMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_QDefaultRouteMetric_Type.__name__ = "Integer32"
_QDefaultRouteMetric_Object = MibTableColumn
qDefaultRouteMetric = _QDefaultRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 2, 1, 11),
    _QDefaultRouteMetric_Type()
)
qDefaultRouteMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qDefaultRouteMetric.setStatus("current")
_QStaticArpTable_Object = MibTable
qStaticArpTable = _QStaticArpTable_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 3)
)
if mibBuilder.loadTexts:
    qStaticArpTable.setStatus("mandatory")
_QStaticArpEntry_Object = MibTableRow
qStaticArpEntry = _QStaticArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 3, 1)
)
qStaticArpEntry.setIndexNames(
    (0, "QWESCOM-MIB", "qStaticArpAddr"),
)
if mibBuilder.loadTexts:
    qStaticArpEntry.setStatus("mandatory")
_QStaticArpAddr_Type = IpAddress
_QStaticArpAddr_Object = MibTableColumn
qStaticArpAddr = _QStaticArpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 3, 1, 1),
    _QStaticArpAddr_Type()
)
qStaticArpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qStaticArpAddr.setStatus("mandatory")


class _QLif_Type(Integer32):
    """Custom type qLif based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(513, 1536),
    )


_QLif_Type.__name__ = "Integer32"
_QLif_Object = MibTableColumn
qLif = _QLif_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 3, 1, 2),
    _QLif_Type()
)
qLif.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qLif.setStatus("mandatory")


class _QPhysType_Type(Integer32):
    """Custom type qPhysType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("atm-and-others", 2),
          ("ethernet", 1))
    )


_QPhysType_Type.__name__ = "Integer32"
_QPhysType_Object = MibTableColumn
qPhysType = _QPhysType_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 3, 1, 3),
    _QPhysType_Type()
)
qPhysType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qPhysType.setStatus("mandatory")
_QMacAddr_Type = PhysAddress
_QMacAddr_Object = MibTableColumn
qMacAddr = _QMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 3, 1, 4),
    _QMacAddr_Type()
)
qMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qMacAddr.setStatus("mandatory")


class _QType_Type(Integer32):
    """Custom type qType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("add-activate", 1),
          ("add-not-activate", 2),
          ("delete", 3))
    )


_QType_Type.__name__ = "Integer32"
_QType_Object = MibTableColumn
qType = _QType_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 3, 1, 5),
    _QType_Type()
)
qType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qType.setStatus("mandatory")


class _QipTtl_Type(Integer32):
    """Custom type qipTtl based on Integer32"""
    defaultValue = 60


_QipTtl_Object = MibScalar
qipTtl = _QipTtl_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 4),
    _QipTtl_Type()
)
qipTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qipTtl.setStatus("mandatory")


class _QipRoutePriority_Type(Integer32):
    """Custom type qipRoutePriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rip", 1),
          ("static", 2))
    )


_QipRoutePriority_Type.__name__ = "Integer32"
_QipRoutePriority_Object = MibScalar
qipRoutePriority = _QipRoutePriority_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 5),
    _QipRoutePriority_Type()
)
qipRoutePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qipRoutePriority.setStatus("mandatory")


class _QipRipStatus_Type(Integer32):
    """Custom type qipRipStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_QipRipStatus_Type.__name__ = "Integer32"
_QipRipStatus_Object = MibScalar
qipRipStatus = _QipRipStatus_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 6),
    _QipRipStatus_Type()
)
qipRipStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qipRipStatus.setStatus("mandatory")
_Qigmp_ObjectIdentity = ObjectIdentity
qigmp = _Qigmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 7)
)
_QigmpInMsgs_Type = Integer32
_QigmpInMsgs_Object = MibScalar
qigmpInMsgs = _QigmpInMsgs_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 7, 1),
    _QigmpInMsgs_Type()
)
qigmpInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qigmpInMsgs.setStatus("mandatory")
_QigmpOutMsgs_Type = Integer32
_QigmpOutMsgs_Object = MibScalar
qigmpOutMsgs = _QigmpOutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 7, 2),
    _QigmpOutMsgs_Type()
)
qigmpOutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qigmpOutMsgs.setStatus("mandatory")
_QigmpInErrors_Type = Integer32
_QigmpInErrors_Object = MibScalar
qigmpInErrors = _QigmpInErrors_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 7, 3),
    _QigmpInErrors_Type()
)
qigmpInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qigmpInErrors.setStatus("mandatory")
_QigmpInReports_Type = Integer32
_QigmpInReports_Object = MibScalar
qigmpInReports = _QigmpInReports_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 7, 4),
    _QigmpInReports_Type()
)
qigmpInReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qigmpInReports.setStatus("mandatory")
_QigmpInQueries_Type = Integer32
_QigmpInQueries_Object = MibScalar
qigmpInQueries = _QigmpInQueries_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 7, 5),
    _QigmpInQueries_Type()
)
qigmpInQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qigmpInQueries.setStatus("mandatory")
_QigmpInUnknownType_Type = Integer32
_QigmpInUnknownType_Object = MibScalar
qigmpInUnknownType = _QigmpInUnknownType_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 7, 6),
    _QigmpInUnknownType_Type()
)
qigmpInUnknownType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qigmpInUnknownType.setStatus("mandatory")
_QIgmpStaticTable_Object = MibTable
qIgmpStaticTable = _QIgmpStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 7, 7)
)
if mibBuilder.loadTexts:
    qIgmpStaticTable.setStatus("mandatory")
_QIgmpStaticEntry_Object = MibTableRow
qIgmpStaticEntry = _QIgmpStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 7, 7, 1)
)
qIgmpStaticEntry.setIndexNames(
    (0, "QWESCOM-MIB", "qIgmpStaticAddr"),
)
if mibBuilder.loadTexts:
    qIgmpStaticEntry.setStatus("mandatory")
_QIgmpStaticAddr_Type = IpAddress
_QIgmpStaticAddr_Object = MibTableColumn
qIgmpStaticAddr = _QIgmpStaticAddr_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 7, 7, 1, 1),
    _QIgmpStaticAddr_Type()
)
qIgmpStaticAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qIgmpStaticAddr.setStatus("mandatory")
_QIgmpLp_Type = Integer32
_QIgmpLp_Object = MibTableColumn
qIgmpLp = _QIgmpLp_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 7, 7, 1, 2),
    _QIgmpLp_Type()
)
qIgmpLp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qIgmpLp.setStatus("current")


class _QIgmpType_Type(Integer32):
    """Custom type qIgmpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("add-activate", 1),
          ("add-not-activate", 2),
          ("delete", 3))
    )


_QIgmpType_Type.__name__ = "Integer32"
_QIgmpType_Object = MibTableColumn
qIgmpType = _QIgmpType_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 7, 7, 1, 3),
    _QIgmpType_Type()
)
qIgmpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qIgmpType.setStatus("current")
_QIgmpGroupTable_Object = MibTable
qIgmpGroupTable = _QIgmpGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 7, 8)
)
if mibBuilder.loadTexts:
    qIgmpGroupTable.setStatus("current")
_QIgmpGroupEntry_Object = MibTableRow
qIgmpGroupEntry = _QIgmpGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 7, 8, 1)
)
qIgmpGroupEntry.setIndexNames(
    (0, "QWESCOM-MIB", "qIgmpGroupLp"),
    (0, "QWESCOM-MIB", "qIgmpGroupAddr"),
)
if mibBuilder.loadTexts:
    qIgmpGroupEntry.setStatus("current")
_QIgmpGroupAddr_Type = IpAddress
_QIgmpGroupAddr_Object = MibTableColumn
qIgmpGroupAddr = _QIgmpGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 7, 8, 1, 1),
    _QIgmpGroupAddr_Type()
)
qIgmpGroupAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qIgmpGroupAddr.setStatus("current")
_QIgmpGroupLp_Type = Integer32
_QIgmpGroupLp_Object = MibTableColumn
qIgmpGroupLp = _QIgmpGroupLp_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 7, 8, 1, 2),
    _QIgmpGroupLp_Type()
)
qIgmpGroupLp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qIgmpGroupLp.setStatus("current")
_QIgmpGroupMacAddr_Type = PhysAddress
_QIgmpGroupMacAddr_Object = MibTableColumn
qIgmpGroupMacAddr = _QIgmpGroupMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 7, 8, 1, 3),
    _QIgmpGroupMacAddr_Type()
)
qIgmpGroupMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qIgmpGroupMacAddr.setStatus("current")


class _QIgmpGroupInstallType_Type(Integer32):
    """Custom type qIgmpGroupInstallType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1),
          ("unknown", 3))
    )


_QIgmpGroupInstallType_Type.__name__ = "Integer32"
_QIgmpGroupInstallType_Object = MibTableColumn
qIgmpGroupInstallType = _QIgmpGroupInstallType_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 7, 8, 1, 4),
    _QIgmpGroupInstallType_Type()
)
qIgmpGroupInstallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qIgmpGroupInstallType.setStatus("current")
_QarpInMsgs_Type = Integer32
_QarpInMsgs_Object = MibScalar
qarpInMsgs = _QarpInMsgs_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 13),
    _QarpInMsgs_Type()
)
qarpInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qarpInMsgs.setStatus("mandatory")
_QarpOutMsgs_Type = Integer32
_QarpOutMsgs_Object = MibScalar
qarpOutMsgs = _QarpOutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 14),
    _QarpOutMsgs_Type()
)
qarpOutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qarpOutMsgs.setStatus("mandatory")
_QarpReqInMsg_Type = Integer32
_QarpReqInMsg_Object = MibScalar
qarpReqInMsg = _QarpReqInMsg_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 15),
    _QarpReqInMsg_Type()
)
qarpReqInMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qarpReqInMsg.setStatus("mandatory")
_QarpReqOutMsgs_Type = Integer32
_QarpReqOutMsgs_Object = MibScalar
qarpReqOutMsgs = _QarpReqOutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 16),
    _QarpReqOutMsgs_Type()
)
qarpReqOutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qarpReqOutMsgs.setStatus("mandatory")
_QarpRespInMsgs_Type = Integer32
_QarpRespInMsgs_Object = MibScalar
qarpRespInMsgs = _QarpRespInMsgs_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 17),
    _QarpRespInMsgs_Type()
)
qarpRespInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qarpRespInMsgs.setStatus("mandatory")
_QarpRespOutMsgs_Type = Integer32
_QarpRespOutMsgs_Object = MibScalar
qarpRespOutMsgs = _QarpRespOutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 18),
    _QarpRespOutMsgs_Type()
)
qarpRespOutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qarpRespOutMsgs.setStatus("mandatory")
_QarpSendDiscards_Type = Integer32
_QarpSendDiscards_Object = MibScalar
qarpSendDiscards = _QarpSendDiscards_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 19),
    _QarpSendDiscards_Type()
)
qarpSendDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qarpSendDiscards.setStatus("mandatory")
_QarpSendTimeouts_Type = Integer32
_QarpSendTimeouts_Object = MibScalar
qarpSendTimeouts = _QarpSendTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 20),
    _QarpSendTimeouts_Type()
)
qarpSendTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qarpSendTimeouts.setStatus("mandatory")
_QarpInResourceErrors_Type = Integer32
_QarpInResourceErrors_Object = MibScalar
qarpInResourceErrors = _QarpInResourceErrors_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 21),
    _QarpInResourceErrors_Type()
)
qarpInResourceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qarpInResourceErrors.setStatus("mandatory")
_QarpOutResourceErrors_Type = Integer32
_QarpOutResourceErrors_Object = MibScalar
qarpOutResourceErrors = _QarpOutResourceErrors_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 22),
    _QarpOutResourceErrors_Type()
)
qarpOutResourceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qarpOutResourceErrors.setStatus("mandatory")
_QRipStatsTable_Object = MibTable
qRipStatsTable = _QRipStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 23)
)
if mibBuilder.loadTexts:
    qRipStatsTable.setStatus("mandatory")
_QRipStatsEntry_Object = MibTableRow
qRipStatsEntry = _QRipStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 23, 1)
)
qRipStatsEntry.setIndexNames(
    (0, "QWESCOM-MIB", "qRipStatsAddr"),
)
if mibBuilder.loadTexts:
    qRipStatsEntry.setStatus("mandatory")
_QRipStatsAddr_Type = IpAddress
_QRipStatsAddr_Object = MibTableColumn
qRipStatsAddr = _QRipStatsAddr_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 23, 1, 1),
    _QRipStatsAddr_Type()
)
qRipStatsAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qRipStatsAddr.setStatus("mandatory")
_Qrip2IfStatsUpdatesReceives_Type = Counter32
_Qrip2IfStatsUpdatesReceives_Object = MibTableColumn
qrip2IfStatsUpdatesReceives = _Qrip2IfStatsUpdatesReceives_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 16, 23, 1, 2),
    _Qrip2IfStatsUpdatesReceives_Type()
)
qrip2IfStatsUpdatesReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qrip2IfStatsUpdatesReceives.setStatus("mandatory")
_QmanagementGroup_ObjectIdentity = ObjectIdentity
qmanagementGroup = _QmanagementGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 17)
)


class _QSysTime_Type(DisplayString):
    """Custom type qSysTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 28),
    )


_QSysTime_Type.__name__ = "DisplayString"
_QSysTime_Object = MibScalar
qSysTime = _QSysTime_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 17, 1),
    _QSysTime_Type()
)
qSysTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qSysTime.setStatus("mandatory")
_QTftpType_Type = Integer32
_QTftpType_Object = MibScalar
qTftpType = _QTftpType_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 17, 2),
    _QTftpType_Type()
)
qTftpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qTftpType.setStatus("mandatory")


class _QTftpFileName_Type(DisplayString):
    """Custom type qTftpFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_QTftpFileName_Type.__name__ = "DisplayString"
_QTftpFileName_Object = MibScalar
qTftpFileName = _QTftpFileName_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 17, 3),
    _QTftpFileName_Type()
)
qTftpFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qTftpFileName.setStatus("mandatory")
_QTftpServerIpAddress_Type = IpAddress
_QTftpServerIpAddress_Object = MibScalar
qTftpServerIpAddress = _QTftpServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 17, 4),
    _QTftpServerIpAddress_Type()
)
qTftpServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qTftpServerIpAddress.setStatus("mandatory")


class _QTftpServerFileName_Type(DisplayString):
    """Custom type qTftpServerFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_QTftpServerFileName_Type.__name__ = "DisplayString"
_QTftpServerFileName_Object = MibScalar
qTftpServerFileName = _QTftpServerFileName_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 17, 5),
    _QTftpServerFileName_Type()
)
qTftpServerFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qTftpServerFileName.setStatus("mandatory")
_QTftpAdminStatus_Type = Integer32
_QTftpAdminStatus_Object = MibScalar
qTftpAdminStatus = _QTftpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 17, 6),
    _QTftpAdminStatus_Type()
)
qTftpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qTftpAdminStatus.setStatus("mandatory")
_QTftpOperStatus_Type = Integer32
_QTftpOperStatus_Object = MibScalar
qTftpOperStatus = _QTftpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 17, 7),
    _QTftpOperStatus_Type()
)
qTftpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qTftpOperStatus.setStatus("mandatory")
_QTftpRxCount_Type = Integer32
_QTftpRxCount_Object = MibScalar
qTftpRxCount = _QTftpRxCount_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 17, 8),
    _QTftpRxCount_Type()
)
qTftpRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qTftpRxCount.setStatus("mandatory")


class _QTimeZone_Type(Integer32):
    """Custom type qTimeZone based on Integer32"""
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
              27)
        )
    )
    namedValues = NamedValues(
        *(("abu-dhabi", 19),
          ("alaska", 4),
          ("almaty", 21),
          ("arizona", 6),
          ("atlantic", 9),
          ("auckland", 27),
          ("azores", 13),
          ("bangkok", 22),
          ("beijing", 23),
          ("brisbane", 25),
          ("buenos-aires", 11),
          ("central", 8),
          ("eniwetok", 1),
          ("gmt", 14),
          ("hawaii", 3),
          ("islamabad", 20),
          ("israel", 16),
          ("mid-atlantic", 12),
          ("moscow", 17),
          ("mountain", 7),
          ("new-caledonia", 26),
          ("newfoundland", 10),
          ("pacific", 5),
          ("paris", 15),
          ("samoa", 2),
          ("tehran", 18),
          ("tokyo", 24))
    )


_QTimeZone_Type.__name__ = "Integer32"
_QTimeZone_Object = MibScalar
qTimeZone = _QTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 17, 9),
    _QTimeZone_Type()
)
qTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qTimeZone.setStatus("mandatory")
_QOamGroup_ObjectIdentity = ObjectIdentity
qOamGroup = _QOamGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 18)
)
_QoamGroupConfigTable_Object = MibTable
qoamGroupConfigTable = _QoamGroupConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 18, 1)
)
if mibBuilder.loadTexts:
    qoamGroupConfigTable.setStatus("mandatory")
_QoamGroupConfigEntry_Object = MibTableRow
qoamGroupConfigEntry = _QoamGroupConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 18, 1, 1)
)
qoamGroupConfigEntry.setIndexNames(
    (0, "QWESCOM-MIB", "qoamGroupConfigIndex"),
)
if mibBuilder.loadTexts:
    qoamGroupConfigEntry.setStatus("mandatory")
_QoamGroupConfigIndex_Type = Integer32
_QoamGroupConfigIndex_Object = MibTableColumn
qoamGroupConfigIndex = _QoamGroupConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 18, 1, 1, 1),
    _QoamGroupConfigIndex_Type()
)
qoamGroupConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qoamGroupConfigIndex.setStatus("current")


class _QoamGroupConfigAlias_Type(DisplayString):
    """Custom type qoamGroupConfigAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QoamGroupConfigAlias_Type.__name__ = "DisplayString"
_QoamGroupConfigAlias_Object = MibTableColumn
qoamGroupConfigAlias = _QoamGroupConfigAlias_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 18, 1, 1, 2),
    _QoamGroupConfigAlias_Type()
)
qoamGroupConfigAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qoamGroupConfigAlias.setStatus("current")


class _QoamGroupConfigType_Type(Integer32):
    """Custom type qoamGroupConfigType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("end-2-end", 2),
          ("segment-2-segment", 1))
    )


_QoamGroupConfigType_Type.__name__ = "Integer32"
_QoamGroupConfigType_Object = MibTableColumn
qoamGroupConfigType = _QoamGroupConfigType_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 18, 1, 1, 3),
    _QoamGroupConfigType_Type()
)
qoamGroupConfigType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qoamGroupConfigType.setStatus("current")


class _QoamGroupConfigTransmitInterval_Type(Integer32):
    """Custom type qoamGroupConfigTransmitInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_QoamGroupConfigTransmitInterval_Type.__name__ = "Integer32"
_QoamGroupConfigTransmitInterval_Object = MibTableColumn
qoamGroupConfigTransmitInterval = _QoamGroupConfigTransmitInterval_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 18, 1, 1, 4),
    _QoamGroupConfigTransmitInterval_Type()
)
qoamGroupConfigTransmitInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qoamGroupConfigTransmitInterval.setStatus("current")


class _QoamGroupConfigS2SAlarmThreshold_Type(Integer32):
    """Custom type qoamGroupConfigS2SAlarmThreshold based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_QoamGroupConfigS2SAlarmThreshold_Type.__name__ = "Integer32"
_QoamGroupConfigS2SAlarmThreshold_Object = MibTableColumn
qoamGroupConfigS2SAlarmThreshold = _QoamGroupConfigS2SAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 18, 1, 1, 5),
    _QoamGroupConfigS2SAlarmThreshold_Type()
)
qoamGroupConfigS2SAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qoamGroupConfigS2SAlarmThreshold.setStatus("current")


class _QoamGroupConfigE2EAlarmThreshold_Type(Integer32):
    """Custom type qoamGroupConfigE2EAlarmThreshold based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_QoamGroupConfigE2EAlarmThreshold_Type.__name__ = "Integer32"
_QoamGroupConfigE2EAlarmThreshold_Object = MibTableColumn
qoamGroupConfigE2EAlarmThreshold = _QoamGroupConfigE2EAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 18, 1, 1, 6),
    _QoamGroupConfigE2EAlarmThreshold_Type()
)
qoamGroupConfigE2EAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qoamGroupConfigE2EAlarmThreshold.setStatus("current")


class _QoamGroupConfigStatus_Type(Integer32):
    """Custom type qoamGroupConfigStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_QoamGroupConfigStatus_Type.__name__ = "Integer32"
_QoamGroupConfigStatus_Object = MibTableColumn
qoamGroupConfigStatus = _QoamGroupConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 18, 1, 1, 7),
    _QoamGroupConfigStatus_Type()
)
qoamGroupConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qoamGroupConfigStatus.setStatus("current")
_QoamCircuitConfigTable_Object = MibTable
qoamCircuitConfigTable = _QoamCircuitConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 18, 2)
)
if mibBuilder.loadTexts:
    qoamCircuitConfigTable.setStatus("mandatory")
_QoamCircuitConfigEntry_Object = MibTableRow
qoamCircuitConfigEntry = _QoamCircuitConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 18, 2, 1)
)
qoamCircuitConfigEntry.setIndexNames(
    (0, "QWESCOM-MIB", "qoamCircuitConfigIndex"),
)
if mibBuilder.loadTexts:
    qoamCircuitConfigEntry.setStatus("mandatory")


class _QoamCircuitConfigIndex_Type(Integer32):
    """Custom type qoamCircuitConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_QoamCircuitConfigIndex_Type.__name__ = "Integer32"
_QoamCircuitConfigIndex_Object = MibTableColumn
qoamCircuitConfigIndex = _QoamCircuitConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 18, 2, 1, 1),
    _QoamCircuitConfigIndex_Type()
)
qoamCircuitConfigIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qoamCircuitConfigIndex.setStatus("current")


class _QoamCircuitConfigType_Type(Integer32):
    """Custom type qoamCircuitConfigType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("end-2-end", 2),
          ("segment-2-segment", 1))
    )


_QoamCircuitConfigType_Type.__name__ = "Integer32"
_QoamCircuitConfigType_Object = MibTableColumn
qoamCircuitConfigType = _QoamCircuitConfigType_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 18, 2, 1, 2),
    _QoamCircuitConfigType_Type()
)
qoamCircuitConfigType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qoamCircuitConfigType.setStatus("current")


class _QoamCircuitConfigTransmitInterval_Type(Integer32):
    """Custom type qoamCircuitConfigTransmitInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_QoamCircuitConfigTransmitInterval_Type.__name__ = "Integer32"
_QoamCircuitConfigTransmitInterval_Object = MibTableColumn
qoamCircuitConfigTransmitInterval = _QoamCircuitConfigTransmitInterval_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 18, 2, 1, 3),
    _QoamCircuitConfigTransmitInterval_Type()
)
qoamCircuitConfigTransmitInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qoamCircuitConfigTransmitInterval.setStatus("current")


class _QoamCircuitConfigS2SAlarmThreshold_Type(Integer32):
    """Custom type qoamCircuitConfigS2SAlarmThreshold based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_QoamCircuitConfigS2SAlarmThreshold_Type.__name__ = "Integer32"
_QoamCircuitConfigS2SAlarmThreshold_Object = MibTableColumn
qoamCircuitConfigS2SAlarmThreshold = _QoamCircuitConfigS2SAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 18, 2, 1, 4),
    _QoamCircuitConfigS2SAlarmThreshold_Type()
)
qoamCircuitConfigS2SAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qoamCircuitConfigS2SAlarmThreshold.setStatus("current")


class _QoamCircuitConfigE2EAlarmThreshold_Type(Integer32):
    """Custom type qoamCircuitConfigE2EAlarmThreshold based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_QoamCircuitConfigE2EAlarmThreshold_Type.__name__ = "Integer32"
_QoamCircuitConfigE2EAlarmThreshold_Object = MibTableColumn
qoamCircuitConfigE2EAlarmThreshold = _QoamCircuitConfigE2EAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 18, 2, 1, 5),
    _QoamCircuitConfigE2EAlarmThreshold_Type()
)
qoamCircuitConfigE2EAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qoamCircuitConfigE2EAlarmThreshold.setStatus("current")


class _QoamCircuitConfigStatus_Type(Integer32):
    """Custom type qoamCircuitConfigStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("add-activate", 1),
          ("add-not-activate", 2),
          ("delete", 3))
    )


_QoamCircuitConfigStatus_Type.__name__ = "Integer32"
_QoamCircuitConfigStatus_Object = MibTableColumn
qoamCircuitConfigStatus = _QoamCircuitConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 18, 2, 1, 6),
    _QoamCircuitConfigStatus_Type()
)
qoamCircuitConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qoamCircuitConfigStatus.setStatus("current")
_QoamGroupControlTable_Object = MibTable
qoamGroupControlTable = _QoamGroupControlTable_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 18, 3)
)
if mibBuilder.loadTexts:
    qoamGroupControlTable.setStatus("mandatory")
_QoamGroupControlEntry_Object = MibTableRow
qoamGroupControlEntry = _QoamGroupControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 18, 3, 1)
)
qoamGroupControlEntry.setIndexNames(
    (0, "QWESCOM-MIB", "qoamGroupControlIndex"),
)
if mibBuilder.loadTexts:
    qoamGroupControlEntry.setStatus("mandatory")


class _QoamGroupControlIndex_Type(Integer32):
    """Custom type qoamGroupControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_QoamGroupControlIndex_Type.__name__ = "Integer32"
_QoamGroupControlIndex_Object = MibTableColumn
qoamGroupControlIndex = _QoamGroupControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 18, 3, 1, 1),
    _QoamGroupControlIndex_Type()
)
qoamGroupControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qoamGroupControlIndex.setStatus("current")


class _QoamGroupControlType_Type(Integer32):
    """Custom type qoamGroupControlType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("end-2-end", 2),
          ("segment-2-segment", 1))
    )


_QoamGroupControlType_Type.__name__ = "Integer32"
_QoamGroupControlType_Object = MibTableColumn
qoamGroupControlType = _QoamGroupControlType_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 18, 3, 1, 2),
    _QoamGroupControlType_Type()
)
qoamGroupControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qoamGroupControlType.setStatus("current")


class _QoamGroupControlStatus_Type(Integer32):
    """Custom type qoamGroupControlStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("restore", 3),
          ("start", 1),
          ("stop", 2))
    )


_QoamGroupControlStatus_Type.__name__ = "Integer32"
_QoamGroupControlStatus_Object = MibTableColumn
qoamGroupControlStatus = _QoamGroupControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 18, 3, 1, 3),
    _QoamGroupControlStatus_Type()
)
qoamGroupControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qoamGroupControlStatus.setStatus("current")
_QoamCircuitControlTable_Object = MibTable
qoamCircuitControlTable = _QoamCircuitControlTable_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 18, 4)
)
if mibBuilder.loadTexts:
    qoamCircuitControlTable.setStatus("mandatory")
_QoamCircuitControlEntry_Object = MibTableRow
qoamCircuitControlEntry = _QoamCircuitControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 18, 4, 1)
)
qoamCircuitControlEntry.setIndexNames(
    (0, "QWESCOM-MIB", "qoamCircuitControlIndex"),
)
if mibBuilder.loadTexts:
    qoamCircuitControlEntry.setStatus("mandatory")


class _QoamCircuitControlIndex_Type(Integer32):
    """Custom type qoamCircuitControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_QoamCircuitControlIndex_Type.__name__ = "Integer32"
_QoamCircuitControlIndex_Object = MibTableColumn
qoamCircuitControlIndex = _QoamCircuitControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 18, 4, 1, 1),
    _QoamCircuitControlIndex_Type()
)
qoamCircuitControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qoamCircuitControlIndex.setStatus("current")


class _QoamCircuitControlType_Type(Integer32):
    """Custom type qoamCircuitControlType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("end-2-end", 2),
          ("segment-2-segment", 1))
    )


_QoamCircuitControlType_Type.__name__ = "Integer32"
_QoamCircuitControlType_Object = MibTableColumn
qoamCircuitControlType = _QoamCircuitControlType_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 18, 4, 1, 2),
    _QoamCircuitControlType_Type()
)
qoamCircuitControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qoamCircuitControlType.setStatus("current")


class _QoamCircuitControlStatus_Type(Integer32):
    """Custom type qoamCircuitControlStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("restore", 3),
          ("start", 1),
          ("stop", 2))
    )


_QoamCircuitControlStatus_Type.__name__ = "Integer32"
_QoamCircuitControlStatus_Object = MibTableColumn
qoamCircuitControlStatus = _QoamCircuitControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 18, 4, 1, 3),
    _QoamCircuitControlStatus_Type()
)
qoamCircuitControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qoamCircuitControlStatus.setStatus("current")
_QoamStatsTable_Object = MibTable
qoamStatsTable = _QoamStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 18, 5)
)
if mibBuilder.loadTexts:
    qoamStatsTable.setStatus("mandatory")
_QoamStatsEntry_Object = MibTableRow
qoamStatsEntry = _QoamStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 18, 5, 1)
)
qoamStatsEntry.setIndexNames(
    (0, "QWESCOM-MIB", "qatmCircuitId"),
)
if mibBuilder.loadTexts:
    qoamStatsEntry.setStatus("mandatory")
_QoamStatsCircuit_Type = Integer32
_QoamStatsCircuit_Object = MibTableColumn
qoamStatsCircuit = _QoamStatsCircuit_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 18, 5, 1, 1),
    _QoamStatsCircuit_Type()
)
qoamStatsCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qoamStatsCircuit.setStatus("current")
_QoamStatsVpi_Type = Integer32
_QoamStatsVpi_Object = MibTableColumn
qoamStatsVpi = _QoamStatsVpi_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 18, 5, 1, 2),
    _QoamStatsVpi_Type()
)
qoamStatsVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qoamStatsVpi.setStatus("current")
_QoamStatsVci_Type = Integer32
_QoamStatsVci_Object = MibTableColumn
qoamStatsVci = _QoamStatsVci_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 18, 5, 1, 3),
    _QoamStatsVci_Type()
)
qoamStatsVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qoamStatsVci.setStatus("current")


class _QoamStatsType_Type(Integer32):
    """Custom type qoamStatsType based on Integer32"""
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
        *(("f4-end", 2),
          ("f4-segment", 1),
          ("f5-end", 4),
          ("f5-segment", 3))
    )


_QoamStatsType_Type.__name__ = "Integer32"
_QoamStatsType_Object = MibTableColumn
qoamStatsType = _QoamStatsType_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 18, 5, 1, 4),
    _QoamStatsType_Type()
)
qoamStatsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qoamStatsType.setStatus("current")


class _QoamStatsStatus_Type(Integer32):
    """Custom type qoamStatsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_QoamStatsStatus_Type.__name__ = "Integer32"
_QoamStatsStatus_Object = MibTableColumn
qoamStatsStatus = _QoamStatsStatus_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 18, 5, 1, 5),
    _QoamStatsStatus_Type()
)
qoamStatsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qoamStatsStatus.setStatus("current")
_QoamRequestTx_Type = Integer32
_QoamRequestTx_Object = MibTableColumn
qoamRequestTx = _QoamRequestTx_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 18, 5, 1, 6),
    _QoamRequestTx_Type()
)
qoamRequestTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qoamRequestTx.setStatus("current")
_QoamRequestRx_Type = Integer32
_QoamRequestRx_Object = MibTableColumn
qoamRequestRx = _QoamRequestRx_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 18, 5, 1, 7),
    _QoamRequestRx_Type()
)
qoamRequestRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qoamRequestRx.setStatus("current")
_QoamReplyTx_Type = Integer32
_QoamReplyTx_Object = MibTableColumn
qoamReplyTx = _QoamReplyTx_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 18, 5, 1, 8),
    _QoamReplyTx_Type()
)
qoamReplyTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qoamReplyTx.setStatus("current")
_QoamReplyRx_Type = Integer32
_QoamReplyRx_Object = MibTableColumn
qoamReplyRx = _QoamReplyRx_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 18, 5, 1, 9),
    _QoamReplyRx_Type()
)
qoamReplyRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qoamReplyRx.setStatus("current")
_QoamTimeouts_Type = Integer32
_QoamTimeouts_Object = MibTableColumn
qoamTimeouts = _QoamTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 18, 5, 1, 10),
    _QoamTimeouts_Type()
)
qoamTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qoamTimeouts.setStatus("current")
_QoamMinRt_Type = Integer32
_QoamMinRt_Object = MibTableColumn
qoamMinRt = _QoamMinRt_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 18, 5, 1, 11),
    _QoamMinRt_Type()
)
qoamMinRt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qoamMinRt.setStatus("current")
_QoamMaxRt_Type = Integer32
_QoamMaxRt_Object = MibTableColumn
qoamMaxRt = _QoamMaxRt_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 18, 5, 1, 12),
    _QoamMaxRt_Type()
)
qoamMaxRt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qoamMaxRt.setStatus("current")
_QoamAveRt_Type = Integer32
_QoamAveRt_Object = MibTableColumn
qoamAveRt = _QoamAveRt_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 18, 5, 1, 13),
    _QoamAveRt_Type()
)
qoamAveRt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qoamAveRt.setStatus("current")
_QoamOtherInErrs_Type = Integer32
_QoamOtherInErrs_Object = MibTableColumn
qoamOtherInErrs = _QoamOtherInErrs_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 18, 5, 1, 14),
    _QoamOtherInErrs_Type()
)
qoamOtherInErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qoamOtherInErrs.setStatus("current")
_QoamOtherOutErrs_Type = Integer32
_QoamOtherOutErrs_Object = MibTableColumn
qoamOtherOutErrs = _QoamOtherOutErrs_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 18, 5, 1, 15),
    _QoamOtherOutErrs_Type()
)
qoamOtherOutErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qoamOtherOutErrs.setStatus("current")
_QoamCrc10InErrs_Type = Integer32
_QoamCrc10InErrs_Object = MibTableColumn
qoamCrc10InErrs = _QoamCrc10InErrs_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 18, 5, 1, 16),
    _QoamCrc10InErrs_Type()
)
qoamCrc10InErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qoamCrc10InErrs.setStatus("current")
_QoamCrc10OutErrs_Type = Integer32
_QoamCrc10OutErrs_Object = MibTableColumn
qoamCrc10OutErrs = _QoamCrc10OutErrs_Object(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 18, 5, 1, 17),
    _QoamCrc10OutErrs_Type()
)
qoamCrc10OutErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qoamCrc10OutErrs.setStatus("current")
_QmiscGroup_ObjectIdentity = ObjectIdentity
qmiscGroup = _QmiscGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3662, 3662, 3662, 19)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QWESCOM-MIB",
    **{"DisplayString": DisplayString,
       "PhysAddress": PhysAddress,
       "TimeDateString": TimeDateString,
       "Boolean": Boolean,
       "qwescom": qwescom,
       "oemTree": oemTree,
       "oem": oem,
       "qproprietaryMib2": qproprietaryMib2,
       "qsnmp": qsnmp,
       "qsnmpCommunityTable": qsnmpCommunityTable,
       "qsnmpCommunityEntry": qsnmpCommunityEntry,
       "qsnmpCommunityIndex": qsnmpCommunityIndex,
       "qsnmpCommunityRights": qsnmpCommunityRights,
       "qsnmpCommunityName": qsnmpCommunityName,
       "qsnmpNMSTable": qsnmpNMSTable,
       "qsnmpNMSEntry": qsnmpNMSEntry,
       "qsnmpNMSIndex": qsnmpNMSIndex,
       "qsnmpNMSIpAddress": qsnmpNMSIpAddress,
       "qsnmpTrapTable": qsnmpTrapTable,
       "qsnmpTrapEntry": qsnmpTrapEntry,
       "qsnmpTrapIndex": qsnmpTrapIndex,
       "qsnmpTrapIpAddress": qsnmpTrapIpAddress,
       "qsnmpForwardTrap": qsnmpForwardTrap,
       "qproducts": qproducts,
       "qslots": qslots,
       "qFlowClass": qFlowClass,
       "qClassDefinitionMaxEntries": qClassDefinitionMaxEntries,
       "qClassDefinitionTable": qClassDefinitionTable,
       "qClassDefinitionEntry": qClassDefinitionEntry,
       "qClassDefinitionIndex": qClassDefinitionIndex,
       "qClassDefinitionAlias": qClassDefinitionAlias,
       "qClassDefinitionParentClassID": qClassDefinitionParentClassID,
       "qClassDefinitionFlowType": qClassDefinitionFlowType,
       "qClassDefinitionSourceIPMask": qClassDefinitionSourceIPMask,
       "qClassDefinitionSourceIPLowerBound": qClassDefinitionSourceIPLowerBound,
       "qClassDefinitionSourceIPUpperBound": qClassDefinitionSourceIPUpperBound,
       "qClassDefinitionDestIPMask": qClassDefinitionDestIPMask,
       "qClassDefinitionDestIPLowerBound": qClassDefinitionDestIPLowerBound,
       "qClassDefinitionDestIPUpperBound": qClassDefinitionDestIPUpperBound,
       "qClassDefinitionDSMask": qClassDefinitionDSMask,
       "qClassDefinitionDSLowerBound": qClassDefinitionDSLowerBound,
       "qClassDefinitionDSUpperBound": qClassDefinitionDSUpperBound,
       "qClassDefinitionWellKnownApplication": qClassDefinitionWellKnownApplication,
       "qClassDefinitionProtocol": qClassDefinitionProtocol,
       "qClassDefinitionSourcePortLowerBound": qClassDefinitionSourcePortLowerBound,
       "qClassDefinitionSourcePortUpperBound": qClassDefinitionSourcePortUpperBound,
       "qClassDefinitionDestPortLowerBound": qClassDefinitionDestPortLowerBound,
       "qClassDefinitionDestPortUpperBound": qClassDefinitionDestPortUpperBound,
       "qClassDefinitionFlowAgingTime": qClassDefinitionFlowAgingTime,
       "qPolicyDefinitionMaxEntries": qPolicyDefinitionMaxEntries,
       "qPolicyDefinitionTable": qPolicyDefinitionTable,
       "qPolicyDefinitionEntry": qPolicyDefinitionEntry,
       "qPolicyDefinitionIndex": qPolicyDefinitionIndex,
       "qPolicyDefinitionAlias": qPolicyDefinitionAlias,
       "qPolicyDefinitionType": qPolicyDefinitionType,
       "qPolicyDefinitionLP": qPolicyDefinitionLP,
       "qPolicyDefinitionStartTime": qPolicyDefinitionStartTime,
       "qPolicyDefinitionEndTime": qPolicyDefinitionEndTime,
       "qPolicyDefinitionDayofWeek": qPolicyDefinitionDayofWeek,
       "qPolicyDefinitionPipeID": qPolicyDefinitionPipeID,
       "qPolicyDefinitionClassID": qPolicyDefinitionClassID,
       "qPolicyDefinitionChannelized": qPolicyDefinitionChannelized,
       "qPolicyDefinitionOutboundDSValue": qPolicyDefinitionOutboundDSValue,
       "qPolicyDefinitionPriority": qPolicyDefinitionPriority,
       "qPolicyDefinitionEvent": qPolicyDefinitionEvent,
       "qPipeDefinitionMaxEntries": qPipeDefinitionMaxEntries,
       "qPipeDefinitionTable": qPipeDefinitionTable,
       "qPipeDefinitionEntry": qPipeDefinitionEntry,
       "qPipeDefinitionIndex": qPipeDefinitionIndex,
       "qPipeDefinitionAlias": qPipeDefinitionAlias,
       "qPipeDefinitionType": qPipeDefinitionType,
       "qPipeDefinitionCircuitID": qPipeDefinitionCircuitID,
       "qPipeDefinitionBandwidth": qPipeDefinitionBandwidth,
       "qPipeDefinitionPeak": qPipeDefinitionPeak,
       "qPipeDefinitionMBS": qPipeDefinitionMBS,
       "qPipeDefinitionBufferAllocation": qPipeDefinitionBufferAllocation,
       "qPipeDefinitionDelay": qPipeDefinitionDelay,
       "qPipeDefinitionPhyIdx": qPipeDefinitionPhyIdx,
       "qPipeDefinitionPhyType": qPipeDefinitionPhyType,
       "qClassStatisticsTable": qClassStatisticsTable,
       "qClassStatisticsEntry": qClassStatisticsEntry,
       "qClassStatisticsIndex": qClassStatisticsIndex,
       "qClassStatisticsAlias": qClassStatisticsAlias,
       "qClassStatisticsTransmittedCount": qClassStatisticsTransmittedCount,
       "qClassStatisticsDiscardCount": qClassStatisticsDiscardCount,
       "qClassStatisticsFallbackCount": qClassStatisticsFallbackCount,
       "qatm": qatm,
       "qatmCircuitTable": qatmCircuitTable,
       "qatmCircuitEntry": qatmCircuitEntry,
       "qatmCircuitId": qatmCircuitId,
       "qatmCircuitAlias": qatmCircuitAlias,
       "qatmCircuitUNI": qatmCircuitUNI,
       "qatmCircuitLogicalInterface": qatmCircuitLogicalInterface,
       "qatmCircuitVpi": qatmCircuitVpi,
       "qatmCircuitFirstVci": qatmCircuitFirstVci,
       "qatmCircuitMode": qatmCircuitMode,
       "qatmCircuitStatus": qatmCircuitStatus,
       "qatmUniTable": qatmUniTable,
       "qatmUniEntry": qatmUniEntry,
       "qatmSpanPort": qatmSpanPort,
       "qatmUniName": qatmUniName,
       "qatmUniAlias": qatmUniAlias,
       "qatmUniTrapStatus": qatmUniTrapStatus,
       "qatmUniMaxQueueDelay": qatmUniMaxQueueDelay,
       "qatmUniMinAllocBuffer": qatmUniMinAllocBuffer,
       "qatmUniSharedBuffer": qatmUniSharedBuffer,
       "qatmUniLinkBandwidth": qatmUniLinkBandwidth,
       "qatmUniLinkDelay": qatmUniLinkDelay,
       "qatmUniBandwidthGranularity": qatmUniBandwidthGranularity,
       "qatmUniIlmiStatus": qatmUniIlmiStatus,
       "qatmUniRowStatus": qatmUniRowStatus,
       "qatmVplTable": qatmVplTable,
       "qatmVplEntry": qatmVplEntry,
       "qatmVplMaxVcc": qatmVplMaxVcc,
       "qatmVplLowestVci": qatmVplLowestVci,
       "qatmVplMaxQueueDelay": qatmVplMaxQueueDelay,
       "qatmVplReservedBuffer": qatmVplReservedBuffer,
       "qatmVplBwGranularity": qatmVplBwGranularity,
       "qatmVplMtu": qatmVplMtu,
       "qatmVplSharedBuffer": qatmVplSharedBuffer,
       "qatmVclTable": qatmVclTable,
       "qatmVclEntry": qatmVclEntry,
       "qatmVclBwGranularity": qatmVclBwGranularity,
       "qatmVclMaxSubChannels": qatmVclMaxSubChannels,
       "qatmVclMaxQueueDelay": qatmVclMaxQueueDelay,
       "qatmVclReservedBuffer": qatmVclReservedBuffer,
       "qatmVclSharedBuffer": qatmVclSharedBuffer,
       "qatmAal5Table": qatmAal5Table,
       "qatmAal5Entry": qatmAal5Entry,
       "qatmAal5Uni": qatmAal5Uni,
       "qatmAal5Aal5Name": qatmAal5Aal5Name,
       "qatmAal5Aal5Alias": qatmAal5Aal5Alias,
       "qatmAal5AdminStatus": qatmAal5AdminStatus,
       "qatmAal5TrapStatus": qatmAal5TrapStatus,
       "qatmAal5MtuSize": qatmAal5MtuSize,
       "qatmAal5RowStatus": qatmAal5RowStatus,
       "qatmTrafficDescriptorTable": qatmTrafficDescriptorTable,
       "qatmTrafficDescriptorEntry": qatmTrafficDescriptorEntry,
       "qatmTrafficDescriptorAlias": qatmTrafficDescriptorAlias,
       "qatmTcTable": qatmTcTable,
       "qatmTcEntry": qatmTcEntry,
       "qatmTcCellSync": qatmTcCellSync,
       "qatmTcPortErrors": qatmTcPortErrors,
       "qatmTcDmaErrors": qatmTcDmaErrors,
       "qatmInvalidCells": qatmInvalidCells,
       "qatmCellsForInactiveVcc": qatmCellsForInactiveVcc,
       "qatmAal5VccStatsTable": qatmAal5VccStatsTable,
       "qatmAal5VccStatsEntry": qatmAal5VccStatsEntry,
       "qatmAal5VccStatsInBytes": qatmAal5VccStatsInBytes,
       "qatmAal5VccStatsOutBytes": qatmAal5VccStatsOutBytes,
       "qatmAal5VccStatsInSdus": qatmAal5VccStatsInSdus,
       "qatmAal5VccStatsOutSdus": qatmAal5VccStatsOutSdus,
       "qatmAal5VccStatsErrsAndDiscards": qatmAal5VccStatsErrsAndDiscards,
       "qatmAal5VccStatsLengthMismatchs": qatmAal5VccStatsLengthMismatchs,
       "qatmAal5VccStatsUserAborts": qatmAal5VccStatsUserAborts,
       "qatmAal5VccStatsPoolDepleteds": qatmAal5VccStatsPoolDepleteds,
       "qcraftPort": qcraftPort,
       "qcpStatus": qcpStatus,
       "qcpBaudRate": qcpBaudRate,
       "qcpStopBitLength": qcpStopBitLength,
       "qcpParity": qcpParity,
       "qcpDataBits": qcpDataBits,
       "qcpCharsSent": qcpCharsSent,
       "qcpCharsReceived": qcpCharsReceived,
       "qeventGroup": qeventGroup,
       "qEventConfigTable": qEventConfigTable,
       "qEventConfigEntry": qEventConfigEntry,
       "qEventConfigIndex": qEventConfigIndex,
       "qEventSeverityType": qEventSeverityType,
       "qLogFileType": qLogFileType,
       "qLogOption": qLogOption,
       "qDisplayOption": qDisplayOption,
       "qTrapOption": qTrapOption,
       "qEventSystemTable": qEventSystemTable,
       "qEventSystemEntry": qEventSystemEntry,
       "qEventSystemIndex": qEventSystemIndex,
       "qEventSystemDateTime": qEventSystemDateTime,
       "qEventSystemType": qEventSystemType,
       "qEventSystemSubSystem": qEventSystemSubSystem,
       "qEventSystemID-Number": qEventSystemID_Number,
       "qEventSystemDescription": qEventSystemDescription,
       "qEventAlarmTable": qEventAlarmTable,
       "qEventAlarmEntry": qEventAlarmEntry,
       "qEventAlarmIndex": qEventAlarmIndex,
       "qEventAlarmDateTime": qEventAlarmDateTime,
       "qEventAlarmType": qEventAlarmType,
       "qEventAlarmSubSystem": qEventAlarmSubSystem,
       "qEventAlarmID-Number": qEventAlarmID_Number,
       "qEventAlarmDescription": qEventAlarmDescription,
       "qextmib": qextmib,
       "qipExt": qipExt,
       "qipCircExtTable": qipCircExtTable,
       "qipCircExtEntry": qipCircExtEntry,
       "qipCircExtIndex": qipCircExtIndex,
       "qipCircExtIfIndex": qipCircExtIfIndex,
       "qipCircExtAdminState": qipCircExtAdminState,
       "qipCircExtOperState": qipCircExtOperState,
       "qarpExt": qarpExt,
       "qarpExtTtl": qarpExtTtl,
       "qarpCircExtTable": qarpCircExtTable,
       "qarpCircExtEntry": qarpCircExtEntry,
       "qarpCircExtIndex": qarpCircExtIndex,
       "qarpCircExtIfIndex": qarpCircExtIfIndex,
       "qarpCircExtDoProxy": qarpCircExtDoProxy,
       "qarpCircExtDoResp": qarpCircExtDoResp,
       "qripExt": qripExt,
       "qripExtAdminState": qripExtAdminState,
       "qripExtUpdateTime": qripExtUpdateTime,
       "qripCircExtTable": qripCircExtTable,
       "qripCircExtEntry": qripCircExtEntry,
       "qripCircExtIndex": qripCircExtIndex,
       "qripCircExtIfIndex": qripCircExtIfIndex,
       "qripCircExtTalk": qripCircExtTalk,
       "qripCircExtListen": qripCircExtListen,
       "qripCircExtPoison": qripCircExtPoison,
       "qmanufactRecord": qmanufactRecord,
       "qmrCheckSum": qmrCheckSum,
       "qmrBurnDate": qmrBurnDate,
       "qmrBurnTime": qmrBurnTime,
       "qmrOemName": qmrOemName,
       "qmrOemID": qmrOemID,
       "qmrSerialNumber": qmrSerialNumber,
       "qmrProductID": qmrProductID,
       "qmrModelID": qmrModelID,
       "qmrMacAddress": qmrMacAddress,
       "qmrRepairTable": qmrRepairTable,
       "qmrRepairEntry": qmrRepairEntry,
       "qmrRepType": qmrRepType,
       "qmrRepCode": qmrRepCode,
       "qmrRepDate": qmrRepDate,
       "qmrRepTime": qmrRepTime,
       "qethernet": qethernet,
       "qethernetCfgTable": qethernetCfgTable,
       "qethernetCfgEntry": qethernetCfgEntry,
       "qethernetMacAddress": qethernetMacAddress,
       "qethernetSpeedMode": qethernetSpeedMode,
       "qethernetEncapsulation": qethernetEncapsulation,
       "qethernetAutoSense": qethernetAutoSense,
       "qethernetName": qethernetName,
       "qethernetCurrentSpeedMode": qethernetCurrentSpeedMode,
       "qds1-e1": qds1_e1,
       "qds1AutoClockSourceSearching": qds1AutoClockSourceSearching,
       "qds1PrimaryClockSource": qds1PrimaryClockSource,
       "qds1PrimaryClockSourceAction": qds1PrimaryClockSourceAction,
       "qds1SpanCfgTable": qds1SpanCfgTable,
       "qds1SpanCfgEntry": qds1SpanCfgEntry,
       "qds1LineCfgIndex": qds1LineCfgIndex,
       "qds1LineBuildOut": qds1LineBuildOut,
       "qds1ClockSourceEligibility": qds1ClockSourceEligibility,
       "qds1ClockMode": qds1ClockMode,
       "qds1PerformanceMonitor": qds1PerformanceMonitor,
       "qds1Scrambler": qds1Scrambler,
       "qds1SpanLoopBackCmdTable": qds1SpanLoopBackCmdTable,
       "qds1SpanLoopBackCmdEntry": qds1SpanLoopBackCmdEntry,
       "qds1LineLoopbackIndex": qds1LineLoopbackIndex,
       "qds1LoopbackCommand": qds1LoopbackCommand,
       "qds1LoopbackDuration": qds1LoopbackDuration,
       "qds1SpanLoopBackStatsTable": qds1SpanLoopBackStatsTable,
       "qds1SpanLoopBackStatsEntry": qds1SpanLoopBackStatsEntry,
       "qds1LineLoopbackStatIndex": qds1LineLoopbackStatIndex,
       "qds1OamSegmentSent": qds1OamSegmentSent,
       "qds1OamSegmentReceived": qds1OamSegmentReceived,
       "qds1OamSegmentFailures": qds1OamSegmentFailures,
       "qds10amRunnigTime": qds10amRunnigTime,
       "qconfigManager": qconfigManager,
       "qcmSystemFile": qcmSystemFile,
       "qcmConfigMaxEntries": qcmConfigMaxEntries,
       "qcmConfigTable": qcmConfigTable,
       "qcmConfigEntry": qcmConfigEntry,
       "qcmTableIndex": qcmTableIndex,
       "qcmCurrentConfig": qcmCurrentConfig,
       "qcmActionOnConfig": qcmActionOnConfig,
       "qcmFileAlias": qcmFileAlias,
       "qcmRelease": qcmRelease,
       "qcmConfigFile": qcmConfigFile,
       "qcmBootSequence": qcmBootSequence,
       "qcmCreateDateTime": qcmCreateDateTime,
       "qcmOperSchedDateTime": qcmOperSchedDateTime,
       "qcmReleaseTable": qcmReleaseTable,
       "qcmReleaseEntry": qcmReleaseEntry,
       "qcmReleaseIndex": qcmReleaseIndex,
       "qcmReleaseName": qcmReleaseName,
       "qcmReleaseVersion": qcmReleaseVersion,
       "qcmConfigVerTable": qcmConfigVerTable,
       "qcmConfigVerEntry": qcmConfigVerEntry,
       "qcmConfigVerIndex": qcmConfigVerIndex,
       "qcmConfigName": qcmConfigName,
       "qcmConfigVersion": qcmConfigVersion,
       "qcmConfigWorkWithMin": qcmConfigWorkWithMin,
       "qcmConfigWorkWithMax": qcmConfigWorkWithMax,
       "qcmWhichFile": qcmWhichFile,
       "qcmUserBaseCfgFile": qcmUserBaseCfgFile,
       "qcmUserNewCfgFile": qcmUserNewCfgFile,
       "qcmUserFileAlias": qcmUserFileAlias,
       "qcmUserRelease": qcmUserRelease,
       "qcmUserBootSequence": qcmUserBootSequence,
       "qcmUserDateTime": qcmUserDateTime,
       "qcmStartConfig": qcmStartConfig,
       "qcmStopConfig": qcmStopConfig,
       "qcmStartViewConfig": qcmStartViewConfig,
       "qcmStopViewConfig": qcmStopViewConfig,
       "qcmCancelConfig": qcmCancelConfig,
       "qportManagement": qportManagement,
       "qwesLpTable": qwesLpTable,
       "qwesLpEntry": qwesLpEntry,
       "qwesLpName": qwesLpName,
       "qwesLpAlias": qwesLpAlias,
       "qwesLpPhysicalInterface": qwesLpPhysicalInterface,
       "qwesLpDataLinkInterface": qwesLpDataLinkInterface,
       "qwesLpTrapStatus": qwesLpTrapStatus,
       "qwesLpAdminStatus": qwesLpAdminStatus,
       "qwesLpRowStatus": qwesLpRowStatus,
       "qwesLifTable": qwesLifTable,
       "qwesLifEntry": qwesLifEntry,
       "qwesLifName": qwesLifName,
       "qwesLifAlias": qwesLifAlias,
       "qwesLifLpIndex": qwesLifLpIndex,
       "qwesLifTrapStatus": qwesLifTrapStatus,
       "qwesLifAdminStatus": qwesLifAdminStatus,
       "qwesLifRowStatus": qwesLifRowStatus,
       "qwesAtmArpTable": qwesAtmArpTable,
       "qwesAtmArpEntry": qwesAtmArpEntry,
       "qwesAtmArpLifIndex": qwesAtmArpLifIndex,
       "qip": qip,
       "qipPortTable": qipPortTable,
       "qipPortEntry": qipPortEntry,
       "qIpLp": qIpLp,
       "qIpAddr": qIpAddr,
       "qIpSubnet": qIpSubnet,
       "qIpMulticast": qIpMulticast,
       "qIpRipStatus": qIpRipStatus,
       "qIpArpTimeout": qIpArpTimeout,
       "qIpEncap": qIpEncap,
       "qRipPortTable": qRipPortTable,
       "qRipPortEntry": qRipPortEntry,
       "qRipIpAddr": qRipIpAddr,
       "qMode": qMode,
       "qAuthentication": qAuthentication,
       "qSplitHorizon": qSplitHorizon,
       "qAdvertiseStaticRoutes": qAdvertiseStaticRoutes,
       "qAdvertiseIntf": qAdvertiseIntf,
       "qBroadcastType": qBroadcastType,
       "qHoldDownInterval": qHoldDownInterval,
       "qUpdatesSend": qUpdatesSend,
       "qUpdatesReceive": qUpdatesReceive,
       "qDefaultRouteMetric": qDefaultRouteMetric,
       "qStaticArpTable": qStaticArpTable,
       "qStaticArpEntry": qStaticArpEntry,
       "qStaticArpAddr": qStaticArpAddr,
       "qLif": qLif,
       "qPhysType": qPhysType,
       "qMacAddr": qMacAddr,
       "qType": qType,
       "qipTtl": qipTtl,
       "qipRoutePriority": qipRoutePriority,
       "qipRipStatus": qipRipStatus,
       "qigmp": qigmp,
       "qigmpInMsgs": qigmpInMsgs,
       "qigmpOutMsgs": qigmpOutMsgs,
       "qigmpInErrors": qigmpInErrors,
       "qigmpInReports": qigmpInReports,
       "qigmpInQueries": qigmpInQueries,
       "qigmpInUnknownType": qigmpInUnknownType,
       "qIgmpStaticTable": qIgmpStaticTable,
       "qIgmpStaticEntry": qIgmpStaticEntry,
       "qIgmpStaticAddr": qIgmpStaticAddr,
       "qIgmpLp": qIgmpLp,
       "qIgmpType": qIgmpType,
       "qIgmpGroupTable": qIgmpGroupTable,
       "qIgmpGroupEntry": qIgmpGroupEntry,
       "qIgmpGroupAddr": qIgmpGroupAddr,
       "qIgmpGroupLp": qIgmpGroupLp,
       "qIgmpGroupMacAddr": qIgmpGroupMacAddr,
       "qIgmpGroupInstallType": qIgmpGroupInstallType,
       "qarpInMsgs": qarpInMsgs,
       "qarpOutMsgs": qarpOutMsgs,
       "qarpReqInMsg": qarpReqInMsg,
       "qarpReqOutMsgs": qarpReqOutMsgs,
       "qarpRespInMsgs": qarpRespInMsgs,
       "qarpRespOutMsgs": qarpRespOutMsgs,
       "qarpSendDiscards": qarpSendDiscards,
       "qarpSendTimeouts": qarpSendTimeouts,
       "qarpInResourceErrors": qarpInResourceErrors,
       "qarpOutResourceErrors": qarpOutResourceErrors,
       "qRipStatsTable": qRipStatsTable,
       "qRipStatsEntry": qRipStatsEntry,
       "qRipStatsAddr": qRipStatsAddr,
       "qrip2IfStatsUpdatesReceives": qrip2IfStatsUpdatesReceives,
       "qmanagementGroup": qmanagementGroup,
       "qSysTime": qSysTime,
       "qTftpType": qTftpType,
       "qTftpFileName": qTftpFileName,
       "qTftpServerIpAddress": qTftpServerIpAddress,
       "qTftpServerFileName": qTftpServerFileName,
       "qTftpAdminStatus": qTftpAdminStatus,
       "qTftpOperStatus": qTftpOperStatus,
       "qTftpRxCount": qTftpRxCount,
       "qTimeZone": qTimeZone,
       "qOamGroup": qOamGroup,
       "qoamGroupConfigTable": qoamGroupConfigTable,
       "qoamGroupConfigEntry": qoamGroupConfigEntry,
       "qoamGroupConfigIndex": qoamGroupConfigIndex,
       "qoamGroupConfigAlias": qoamGroupConfigAlias,
       "qoamGroupConfigType": qoamGroupConfigType,
       "qoamGroupConfigTransmitInterval": qoamGroupConfigTransmitInterval,
       "qoamGroupConfigS2SAlarmThreshold": qoamGroupConfigS2SAlarmThreshold,
       "qoamGroupConfigE2EAlarmThreshold": qoamGroupConfigE2EAlarmThreshold,
       "qoamGroupConfigStatus": qoamGroupConfigStatus,
       "qoamCircuitConfigTable": qoamCircuitConfigTable,
       "qoamCircuitConfigEntry": qoamCircuitConfigEntry,
       "qoamCircuitConfigIndex": qoamCircuitConfigIndex,
       "qoamCircuitConfigType": qoamCircuitConfigType,
       "qoamCircuitConfigTransmitInterval": qoamCircuitConfigTransmitInterval,
       "qoamCircuitConfigS2SAlarmThreshold": qoamCircuitConfigS2SAlarmThreshold,
       "qoamCircuitConfigE2EAlarmThreshold": qoamCircuitConfigE2EAlarmThreshold,
       "qoamCircuitConfigStatus": qoamCircuitConfigStatus,
       "qoamGroupControlTable": qoamGroupControlTable,
       "qoamGroupControlEntry": qoamGroupControlEntry,
       "qoamGroupControlIndex": qoamGroupControlIndex,
       "qoamGroupControlType": qoamGroupControlType,
       "qoamGroupControlStatus": qoamGroupControlStatus,
       "qoamCircuitControlTable": qoamCircuitControlTable,
       "qoamCircuitControlEntry": qoamCircuitControlEntry,
       "qoamCircuitControlIndex": qoamCircuitControlIndex,
       "qoamCircuitControlType": qoamCircuitControlType,
       "qoamCircuitControlStatus": qoamCircuitControlStatus,
       "qoamStatsTable": qoamStatsTable,
       "qoamStatsEntry": qoamStatsEntry,
       "qoamStatsCircuit": qoamStatsCircuit,
       "qoamStatsVpi": qoamStatsVpi,
       "qoamStatsVci": qoamStatsVci,
       "qoamStatsType": qoamStatsType,
       "qoamStatsStatus": qoamStatsStatus,
       "qoamRequestTx": qoamRequestTx,
       "qoamRequestRx": qoamRequestRx,
       "qoamReplyTx": qoamReplyTx,
       "qoamReplyRx": qoamReplyRx,
       "qoamTimeouts": qoamTimeouts,
       "qoamMinRt": qoamMinRt,
       "qoamMaxRt": qoamMaxRt,
       "qoamAveRt": qoamAveRt,
       "qoamOtherInErrs": qoamOtherInErrs,
       "qoamOtherOutErrs": qoamOtherOutErrs,
       "qoamCrc10InErrs": qoamCrc10InErrs,
       "qoamCrc10OutErrs": qoamCrc10OutErrs,
       "qmiscGroup": qmiscGroup}
)
