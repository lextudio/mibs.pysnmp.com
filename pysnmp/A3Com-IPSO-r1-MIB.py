# SNMP MIB module (A3COM-IPSO-R1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-IPSO-R1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:29:34 2024
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




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_A3Com_ObjectIdentity = ObjectIdentity
a3Com = _A3Com_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43)
)
_BrouterMIB_ObjectIdentity = ObjectIdentity
brouterMIB = _BrouterMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2)
)
_A3ComIPSO_ObjectIdentity = ObjectIdentity
a3ComIPSO = _A3ComIPSO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 12)
)


class _A3IPsecureCtl_Type(Integer32):
    """Custom type a3IPsecureCtl based on Integer32"""
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
        *(("noSecurity", 3),
          ("security1038", 2),
          ("security1108", 1))
    )


_A3IPsecureCtl_Type.__name__ = "Integer32"
_A3IPsecureCtl_Object = MibScalar
a3IPsecureCtl = _A3IPsecureCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 12, 1),
    _A3IPsecureCtl_Type()
)
a3IPsecureCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3IPsecureCtl.setStatus("mandatory")


class _A3IPsecureFileServer_Type(Integer32):
    """Custom type a3IPsecureFileServer based on Integer32"""
    defaultValue = 2

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


_A3IPsecureFileServer_Type.__name__ = "Integer32"
_A3IPsecureFileServer_Object = MibScalar
a3IPsecureFileServer = _A3IPsecureFileServer_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 12, 2),
    _A3IPsecureFileServer_Type()
)
a3IPsecureFileServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3IPsecureFileServer.setStatus("mandatory")
_A3IPsecureParamTable_Object = MibTable
a3IPsecureParamTable = _A3IPsecureParamTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 12, 3)
)
if mibBuilder.loadTexts:
    a3IPsecureParamTable.setStatus("mandatory")
_A3IPsecureParamEntry_Object = MibTableRow
a3IPsecureParamEntry = _A3IPsecureParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 12, 3, 1)
)
a3IPsecureParamEntry.setIndexNames(
    (0, "A3COM-IPSO-R1-MIB", "a3IPsecureParamPortIndex"),
)
if mibBuilder.loadTexts:
    a3IPsecureParamEntry.setStatus("mandatory")
_A3IPsecureParamPortIndex_Type = Integer32
_A3IPsecureParamPortIndex_Object = MibTableColumn
a3IPsecureParamPortIndex = _A3IPsecureParamPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 12, 3, 1, 1),
    _A3IPsecureParamPortIndex_Type()
)
a3IPsecureParamPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3IPsecureParamPortIndex.setStatus("mandatory")


class _A3IPsecureParamCtl_Type(Integer32):
    """Custom type a3IPsecureParamCtl based on Integer32"""
    defaultValue = 0


_A3IPsecureParamCtl_Object = MibTableColumn
a3IPsecureParamCtl = _A3IPsecureParamCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 12, 3, 1, 2),
    _A3IPsecureParamCtl_Type()
)
a3IPsecureParamCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3IPsecureParamCtl.setStatus("mandatory")


class _A3IPsecureLabelDefaultLevel_Type(Integer32):
    """Custom type a3IPsecureLabelDefaultLevel based on Integer32"""
    defaultValue = 1

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
        *(("confidential", 4),
          ("none", 1),
          ("secret", 3),
          ("topSecret", 2),
          ("unclassified", 5))
    )


_A3IPsecureLabelDefaultLevel_Type.__name__ = "Integer32"
_A3IPsecureLabelDefaultLevel_Object = MibTableColumn
a3IPsecureLabelDefaultLevel = _A3IPsecureLabelDefaultLevel_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 12, 3, 1, 3),
    _A3IPsecureLabelDefaultLevel_Type()
)
a3IPsecureLabelDefaultLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3IPsecureLabelDefaultLevel.setStatus("mandatory")


class _A3IPsecureLabelDefaultAuth_Type(Integer32):
    """Custom type a3IPsecureLabelDefaultAuth based on Integer32"""
    defaultValue = 0


_A3IPsecureLabelDefaultAuth_Object = MibTableColumn
a3IPsecureLabelDefaultAuth = _A3IPsecureLabelDefaultAuth_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 12, 3, 1, 4),
    _A3IPsecureLabelDefaultAuth_Type()
)
a3IPsecureLabelDefaultAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3IPsecureLabelDefaultAuth.setStatus("mandatory")


class _A3IPsecureLabelSysLevel_Type(Integer32):
    """Custom type a3IPsecureLabelSysLevel based on Integer32"""
    defaultValue = 5

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
        *(("confidential", 4),
          ("none", 1),
          ("secret", 3),
          ("topSecret", 2),
          ("unclassified", 5))
    )


_A3IPsecureLabelSysLevel_Type.__name__ = "Integer32"
_A3IPsecureLabelSysLevel_Object = MibTableColumn
a3IPsecureLabelSysLevel = _A3IPsecureLabelSysLevel_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 12, 3, 1, 5),
    _A3IPsecureLabelSysLevel_Type()
)
a3IPsecureLabelSysLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3IPsecureLabelSysLevel.setStatus("mandatory")


class _A3IPsecureLabelSysAuth_Type(Integer32):
    """Custom type a3IPsecureLabelSysAuth based on Integer32"""
    defaultValue = 128


_A3IPsecureLabelSysAuth_Object = MibTableColumn
a3IPsecureLabelSysAuth = _A3IPsecureLabelSysAuth_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 12, 3, 1, 6),
    _A3IPsecureLabelSysAuth_Type()
)
a3IPsecureLabelSysAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3IPsecureLabelSysAuth.setStatus("mandatory")


class _A3IPsecureMinLevel_Type(Integer32):
    """Custom type a3IPsecureMinLevel based on Integer32"""
    defaultValue = 4

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
        *(("confidential", 3),
          ("secret", 2),
          ("topSecret", 1),
          ("unclassified", 4))
    )


_A3IPsecureMinLevel_Type.__name__ = "Integer32"
_A3IPsecureMinLevel_Object = MibTableColumn
a3IPsecureMinLevel = _A3IPsecureMinLevel_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 12, 3, 1, 7),
    _A3IPsecureMinLevel_Type()
)
a3IPsecureMinLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3IPsecureMinLevel.setStatus("mandatory")


class _A3IPsecureMaxLevel_Type(Integer32):
    """Custom type a3IPsecureMaxLevel based on Integer32"""
    defaultValue = 4

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
        *(("confidential", 3),
          ("secret", 2),
          ("topSecret", 1),
          ("unclassified", 4))
    )


_A3IPsecureMaxLevel_Type.__name__ = "Integer32"
_A3IPsecureMaxLevel_Object = MibTableColumn
a3IPsecureMaxLevel = _A3IPsecureMaxLevel_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 12, 3, 1, 8),
    _A3IPsecureMaxLevel_Type()
)
a3IPsecureMaxLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3IPsecureMaxLevel.setStatus("mandatory")
_A3IPsecureAuthInTable_Object = MibTable
a3IPsecureAuthInTable = _A3IPsecureAuthInTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 12, 4)
)
if mibBuilder.loadTexts:
    a3IPsecureAuthInTable.setStatus("mandatory")
_A3IPsecureAuthInEntry_Object = MibTableRow
a3IPsecureAuthInEntry = _A3IPsecureAuthInEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 12, 4, 1)
)
a3IPsecureAuthInEntry.setIndexNames(
    (0, "A3COM-IPSO-R1-MIB", "a3IPsecureAuthInPort"),
    (0, "A3COM-IPSO-R1-MIB", "a3IPsecureAuthInFlags"),
)
if mibBuilder.loadTexts:
    a3IPsecureAuthInEntry.setStatus("mandatory")
_A3IPsecureAuthInPort_Type = Integer32
_A3IPsecureAuthInPort_Object = MibTableColumn
a3IPsecureAuthInPort = _A3IPsecureAuthInPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 12, 4, 1, 1),
    _A3IPsecureAuthInPort_Type()
)
a3IPsecureAuthInPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3IPsecureAuthInPort.setStatus("mandatory")
_A3IPsecureAuthInFlags_Type = Integer32
_A3IPsecureAuthInFlags_Object = MibTableColumn
a3IPsecureAuthInFlags = _A3IPsecureAuthInFlags_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 12, 4, 1, 2),
    _A3IPsecureAuthInFlags_Type()
)
a3IPsecureAuthInFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3IPsecureAuthInFlags.setStatus("mandatory")


class _A3IPsecureAuthInMatch_Type(Integer32):
    """Custom type a3IPsecureAuthInMatch based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 2),
          ("exact", 1))
    )


_A3IPsecureAuthInMatch_Type.__name__ = "Integer32"
_A3IPsecureAuthInMatch_Object = MibTableColumn
a3IPsecureAuthInMatch = _A3IPsecureAuthInMatch_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 12, 4, 1, 3),
    _A3IPsecureAuthInMatch_Type()
)
a3IPsecureAuthInMatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3IPsecureAuthInMatch.setStatus("mandatory")
_A3IPsecureAuthInStatus_Type = RowStatus
_A3IPsecureAuthInStatus_Object = MibTableColumn
a3IPsecureAuthInStatus = _A3IPsecureAuthInStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 12, 4, 1, 4),
    _A3IPsecureAuthInStatus_Type()
)
a3IPsecureAuthInStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3IPsecureAuthInStatus.setStatus("mandatory")
_A3IPsecureAuthOutTable_Object = MibTable
a3IPsecureAuthOutTable = _A3IPsecureAuthOutTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 12, 5)
)
if mibBuilder.loadTexts:
    a3IPsecureAuthOutTable.setStatus("mandatory")
_A3IPsecureAuthOutEntry_Object = MibTableRow
a3IPsecureAuthOutEntry = _A3IPsecureAuthOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 12, 5, 1)
)
a3IPsecureAuthOutEntry.setIndexNames(
    (0, "A3COM-IPSO-R1-MIB", "a3IPsecureAuthOutPort"),
    (0, "A3COM-IPSO-R1-MIB", "a3IPsecureAuthOutFlags"),
)
if mibBuilder.loadTexts:
    a3IPsecureAuthOutEntry.setStatus("mandatory")
_A3IPsecureAuthOutPort_Type = Integer32
_A3IPsecureAuthOutPort_Object = MibTableColumn
a3IPsecureAuthOutPort = _A3IPsecureAuthOutPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 12, 5, 1, 1),
    _A3IPsecureAuthOutPort_Type()
)
a3IPsecureAuthOutPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3IPsecureAuthOutPort.setStatus("mandatory")
_A3IPsecureAuthOutFlags_Type = Integer32
_A3IPsecureAuthOutFlags_Object = MibTableColumn
a3IPsecureAuthOutFlags = _A3IPsecureAuthOutFlags_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 12, 5, 1, 2),
    _A3IPsecureAuthOutFlags_Type()
)
a3IPsecureAuthOutFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3IPsecureAuthOutFlags.setStatus("mandatory")


class _A3IPsecureAuthOutMatch_Type(Integer32):
    """Custom type a3IPsecureAuthOutMatch based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 2),
          ("exact", 1))
    )


_A3IPsecureAuthOutMatch_Type.__name__ = "Integer32"
_A3IPsecureAuthOutMatch_Object = MibTableColumn
a3IPsecureAuthOutMatch = _A3IPsecureAuthOutMatch_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 12, 5, 1, 3),
    _A3IPsecureAuthOutMatch_Type()
)
a3IPsecureAuthOutMatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3IPsecureAuthOutMatch.setStatus("mandatory")
_A3IPsecureAuthOutStatus_Type = RowStatus
_A3IPsecureAuthOutStatus_Object = MibTableColumn
a3IPsecureAuthOutStatus = _A3IPsecureAuthOutStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 12, 5, 1, 4),
    _A3IPsecureAuthOutStatus_Type()
)
a3IPsecureAuthOutStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3IPsecureAuthOutStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-IPSO-R1-MIB",
    **{"RowStatus": RowStatus,
       "a3Com": a3Com,
       "brouterMIB": brouterMIB,
       "a3ComIPSO": a3ComIPSO,
       "a3IPsecureCtl": a3IPsecureCtl,
       "a3IPsecureFileServer": a3IPsecureFileServer,
       "a3IPsecureParamTable": a3IPsecureParamTable,
       "a3IPsecureParamEntry": a3IPsecureParamEntry,
       "a3IPsecureParamPortIndex": a3IPsecureParamPortIndex,
       "a3IPsecureParamCtl": a3IPsecureParamCtl,
       "a3IPsecureLabelDefaultLevel": a3IPsecureLabelDefaultLevel,
       "a3IPsecureLabelDefaultAuth": a3IPsecureLabelDefaultAuth,
       "a3IPsecureLabelSysLevel": a3IPsecureLabelSysLevel,
       "a3IPsecureLabelSysAuth": a3IPsecureLabelSysAuth,
       "a3IPsecureMinLevel": a3IPsecureMinLevel,
       "a3IPsecureMaxLevel": a3IPsecureMaxLevel,
       "a3IPsecureAuthInTable": a3IPsecureAuthInTable,
       "a3IPsecureAuthInEntry": a3IPsecureAuthInEntry,
       "a3IPsecureAuthInPort": a3IPsecureAuthInPort,
       "a3IPsecureAuthInFlags": a3IPsecureAuthInFlags,
       "a3IPsecureAuthInMatch": a3IPsecureAuthInMatch,
       "a3IPsecureAuthInStatus": a3IPsecureAuthInStatus,
       "a3IPsecureAuthOutTable": a3IPsecureAuthOutTable,
       "a3IPsecureAuthOutEntry": a3IPsecureAuthOutEntry,
       "a3IPsecureAuthOutPort": a3IPsecureAuthOutPort,
       "a3IPsecureAuthOutFlags": a3IPsecureAuthOutFlags,
       "a3IPsecureAuthOutMatch": a3IPsecureAuthOutMatch,
       "a3IPsecureAuthOutStatus": a3IPsecureAuthOutStatus}
)
