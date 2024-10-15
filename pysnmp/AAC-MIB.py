# SNMP MIB module (AAC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AAC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:31:26 2024
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

swDlinkAACMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwAACCtrl_ObjectIdentity = ObjectIdentity
swAACCtrl = _SwAACCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 1)
)


class _SwAACAuthenAdminState_Type(Integer32):
    """Custom type swAACAuthenAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwAACAuthenAdminState_Type.__name__ = "Integer32"
_SwAACAuthenAdminState_Object = MibScalar
swAACAuthenAdminState = _SwAACAuthenAdminState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 1, 1),
    _SwAACAuthenAdminState_Type()
)
swAACAuthenAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAACAuthenAdminState.setStatus("current")
_SwAACInfo_ObjectIdentity = ObjectIdentity
swAACInfo = _SwAACInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 2)
)
_SwAACMaxLoginMethodList_Type = Integer32
_SwAACMaxLoginMethodList_Object = MibScalar
swAACMaxLoginMethodList = _SwAACMaxLoginMethodList_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 2, 1),
    _SwAACMaxLoginMethodList_Type()
)
swAACMaxLoginMethodList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAACMaxLoginMethodList.setStatus("current")
_SwAACMaxEnableMethodList_Type = Integer32
_SwAACMaxEnableMethodList_Object = MibScalar
swAACMaxEnableMethodList = _SwAACMaxEnableMethodList_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 2, 2),
    _SwAACMaxEnableMethodList_Type()
)
swAACMaxEnableMethodList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAACMaxEnableMethodList.setStatus("current")
_SwAACMaxServerGroup_Type = Integer32
_SwAACMaxServerGroup_Object = MibScalar
swAACMaxServerGroup = _SwAACMaxServerGroup_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 2, 3),
    _SwAACMaxServerGroup_Type()
)
swAACMaxServerGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAACMaxServerGroup.setStatus("current")
_SwAACMaxServer_Type = Integer32
_SwAACMaxServer_Object = MibScalar
swAACMaxServer = _SwAACMaxServer_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 2, 4),
    _SwAACMaxServer_Type()
)
swAACMaxServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAACMaxServer.setStatus("current")
_SwAACLoginMethodListTable_Object = MibTable
swAACLoginMethodListTable = _SwAACLoginMethodListTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 3)
)
if mibBuilder.loadTexts:
    swAACLoginMethodListTable.setStatus("current")
_SwAACLoginMethodListEntry_Object = MibTableRow
swAACLoginMethodListEntry = _SwAACLoginMethodListEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 3, 1)
)
swAACLoginMethodListEntry.setIndexNames(
    (0, "AAC-MIB", "swAACLoginMethodListName"),
)
if mibBuilder.loadTexts:
    swAACLoginMethodListEntry.setStatus("current")


class _SwAACLoginMethodListName_Type(DisplayString):
    """Custom type swAACLoginMethodListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_SwAACLoginMethodListName_Type.__name__ = "DisplayString"
_SwAACLoginMethodListName_Object = MibTableColumn
swAACLoginMethodListName = _SwAACLoginMethodListName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 3, 1, 1),
    _SwAACLoginMethodListName_Type()
)
swAACLoginMethodListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAACLoginMethodListName.setStatus("current")


class _SwAACLoginMethod1Type_Type(Integer32):
    """Custom type swAACLoginMethod1Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("local", 6),
          ("none", 8),
          ("other", 9),
          ("radius", 4),
          ("server-group", 5),
          ("tacacs", 1),
          ("tacacs-plus", 3),
          ("xtacacs", 2))
    )


_SwAACLoginMethod1Type_Type.__name__ = "Integer32"
_SwAACLoginMethod1Type_Object = MibTableColumn
swAACLoginMethod1Type = _SwAACLoginMethod1Type_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 3, 1, 2),
    _SwAACLoginMethod1Type_Type()
)
swAACLoginMethod1Type.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAACLoginMethod1Type.setStatus("current")


class _SwAACLoginMethod1ServerGroup_Type(DisplayString):
    """Custom type swAACLoginMethod1ServerGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SwAACLoginMethod1ServerGroup_Type.__name__ = "DisplayString"
_SwAACLoginMethod1ServerGroup_Object = MibTableColumn
swAACLoginMethod1ServerGroup = _SwAACLoginMethod1ServerGroup_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 3, 1, 3),
    _SwAACLoginMethod1ServerGroup_Type()
)
swAACLoginMethod1ServerGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAACLoginMethod1ServerGroup.setStatus("current")


class _SwAACLoginMethod2Type_Type(Integer32):
    """Custom type swAACLoginMethod2Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("local", 6),
          ("none", 8),
          ("other", 9),
          ("radius", 4),
          ("server-group", 5),
          ("tacacs", 1),
          ("tacacs-plus", 3),
          ("xtacacs", 2))
    )


_SwAACLoginMethod2Type_Type.__name__ = "Integer32"
_SwAACLoginMethod2Type_Object = MibTableColumn
swAACLoginMethod2Type = _SwAACLoginMethod2Type_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 3, 1, 4),
    _SwAACLoginMethod2Type_Type()
)
swAACLoginMethod2Type.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAACLoginMethod2Type.setStatus("current")


class _SwAACLoginMethod2ServerGroup_Type(DisplayString):
    """Custom type swAACLoginMethod2ServerGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SwAACLoginMethod2ServerGroup_Type.__name__ = "DisplayString"
_SwAACLoginMethod2ServerGroup_Object = MibTableColumn
swAACLoginMethod2ServerGroup = _SwAACLoginMethod2ServerGroup_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 3, 1, 5),
    _SwAACLoginMethod2ServerGroup_Type()
)
swAACLoginMethod2ServerGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAACLoginMethod2ServerGroup.setStatus("current")


class _SwAACLoginMethod3Type_Type(Integer32):
    """Custom type swAACLoginMethod3Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("local", 6),
          ("none", 8),
          ("other", 9),
          ("radius", 4),
          ("server-group", 5),
          ("tacacs", 1),
          ("tacacs-plus", 3),
          ("xtacacs", 2))
    )


_SwAACLoginMethod3Type_Type.__name__ = "Integer32"
_SwAACLoginMethod3Type_Object = MibTableColumn
swAACLoginMethod3Type = _SwAACLoginMethod3Type_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 3, 1, 6),
    _SwAACLoginMethod3Type_Type()
)
swAACLoginMethod3Type.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAACLoginMethod3Type.setStatus("current")


class _SwAACLoginMethod3ServerGroup_Type(DisplayString):
    """Custom type swAACLoginMethod3ServerGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SwAACLoginMethod3ServerGroup_Type.__name__ = "DisplayString"
_SwAACLoginMethod3ServerGroup_Object = MibTableColumn
swAACLoginMethod3ServerGroup = _SwAACLoginMethod3ServerGroup_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 3, 1, 7),
    _SwAACLoginMethod3ServerGroup_Type()
)
swAACLoginMethod3ServerGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAACLoginMethod3ServerGroup.setStatus("current")


class _SwAACLoginMethod4Type_Type(Integer32):
    """Custom type swAACLoginMethod4Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("local", 6),
          ("none", 8),
          ("other", 9),
          ("radius", 4),
          ("server-group", 5),
          ("tacacs", 1),
          ("tacacs-plus", 3),
          ("xtacacs", 2))
    )


_SwAACLoginMethod4Type_Type.__name__ = "Integer32"
_SwAACLoginMethod4Type_Object = MibTableColumn
swAACLoginMethod4Type = _SwAACLoginMethod4Type_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 3, 1, 8),
    _SwAACLoginMethod4Type_Type()
)
swAACLoginMethod4Type.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAACLoginMethod4Type.setStatus("current")


class _SwAACLoginMethod4ServerGroup_Type(DisplayString):
    """Custom type swAACLoginMethod4ServerGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SwAACLoginMethod4ServerGroup_Type.__name__ = "DisplayString"
_SwAACLoginMethod4ServerGroup_Object = MibTableColumn
swAACLoginMethod4ServerGroup = _SwAACLoginMethod4ServerGroup_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 3, 1, 9),
    _SwAACLoginMethod4ServerGroup_Type()
)
swAACLoginMethod4ServerGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAACLoginMethod4ServerGroup.setStatus("current")
_SwAACLoginMethodListRowStatus_Type = RowStatus
_SwAACLoginMethodListRowStatus_Object = MibTableColumn
swAACLoginMethodListRowStatus = _SwAACLoginMethodListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 3, 1, 10),
    _SwAACLoginMethodListRowStatus_Type()
)
swAACLoginMethodListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAACLoginMethodListRowStatus.setStatus("current")
_SwAACEnableMethodListTable_Object = MibTable
swAACEnableMethodListTable = _SwAACEnableMethodListTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 4)
)
if mibBuilder.loadTexts:
    swAACEnableMethodListTable.setStatus("current")
_SwAACEnableMethodListEntry_Object = MibTableRow
swAACEnableMethodListEntry = _SwAACEnableMethodListEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 4, 1)
)
swAACEnableMethodListEntry.setIndexNames(
    (0, "AAC-MIB", "swAACEnableMethodListName"),
)
if mibBuilder.loadTexts:
    swAACEnableMethodListEntry.setStatus("current")


class _SwAACEnableMethodListName_Type(DisplayString):
    """Custom type swAACEnableMethodListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_SwAACEnableMethodListName_Type.__name__ = "DisplayString"
_SwAACEnableMethodListName_Object = MibTableColumn
swAACEnableMethodListName = _SwAACEnableMethodListName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 4, 1, 1),
    _SwAACEnableMethodListName_Type()
)
swAACEnableMethodListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAACEnableMethodListName.setStatus("current")


class _SwAACEnableMethod1Type_Type(Integer32):
    """Custom type swAACEnableMethod1Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("local-enable", 7),
          ("none", 8),
          ("other", 9),
          ("radius", 4),
          ("server-group", 5),
          ("tacacs", 1),
          ("tacacs-plus", 3),
          ("xtacacs", 2))
    )


_SwAACEnableMethod1Type_Type.__name__ = "Integer32"
_SwAACEnableMethod1Type_Object = MibTableColumn
swAACEnableMethod1Type = _SwAACEnableMethod1Type_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 4, 1, 2),
    _SwAACEnableMethod1Type_Type()
)
swAACEnableMethod1Type.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAACEnableMethod1Type.setStatus("current")


class _SwAACEnableMethod1ServerGroup_Type(DisplayString):
    """Custom type swAACEnableMethod1ServerGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SwAACEnableMethod1ServerGroup_Type.__name__ = "DisplayString"
_SwAACEnableMethod1ServerGroup_Object = MibTableColumn
swAACEnableMethod1ServerGroup = _SwAACEnableMethod1ServerGroup_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 4, 1, 3),
    _SwAACEnableMethod1ServerGroup_Type()
)
swAACEnableMethod1ServerGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAACEnableMethod1ServerGroup.setStatus("current")


class _SwAACEnableMethod2Type_Type(Integer32):
    """Custom type swAACEnableMethod2Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("local-enable", 7),
          ("none", 8),
          ("other", 9),
          ("radius", 4),
          ("server-group", 5),
          ("tacacs", 1),
          ("tacacs-plus", 3),
          ("xtacacs", 2))
    )


_SwAACEnableMethod2Type_Type.__name__ = "Integer32"
_SwAACEnableMethod2Type_Object = MibTableColumn
swAACEnableMethod2Type = _SwAACEnableMethod2Type_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 4, 1, 4),
    _SwAACEnableMethod2Type_Type()
)
swAACEnableMethod2Type.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAACEnableMethod2Type.setStatus("current")


class _SwAACEnableMethod2ServerGroup_Type(DisplayString):
    """Custom type swAACEnableMethod2ServerGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SwAACEnableMethod2ServerGroup_Type.__name__ = "DisplayString"
_SwAACEnableMethod2ServerGroup_Object = MibTableColumn
swAACEnableMethod2ServerGroup = _SwAACEnableMethod2ServerGroup_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 4, 1, 5),
    _SwAACEnableMethod2ServerGroup_Type()
)
swAACEnableMethod2ServerGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAACEnableMethod2ServerGroup.setStatus("current")


class _SwAACEnableMethod3Type_Type(Integer32):
    """Custom type swAACEnableMethod3Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("local-enable", 7),
          ("none", 8),
          ("other", 9),
          ("radius", 4),
          ("server-group", 5),
          ("tacacs", 1),
          ("tacacs-plus", 3),
          ("xtacacs", 2))
    )


_SwAACEnableMethod3Type_Type.__name__ = "Integer32"
_SwAACEnableMethod3Type_Object = MibTableColumn
swAACEnableMethod3Type = _SwAACEnableMethod3Type_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 4, 1, 6),
    _SwAACEnableMethod3Type_Type()
)
swAACEnableMethod3Type.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAACEnableMethod3Type.setStatus("current")


class _SwAACEnableMethod3ServerGroup_Type(DisplayString):
    """Custom type swAACEnableMethod3ServerGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SwAACEnableMethod3ServerGroup_Type.__name__ = "DisplayString"
_SwAACEnableMethod3ServerGroup_Object = MibTableColumn
swAACEnableMethod3ServerGroup = _SwAACEnableMethod3ServerGroup_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 4, 1, 7),
    _SwAACEnableMethod3ServerGroup_Type()
)
swAACEnableMethod3ServerGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAACEnableMethod3ServerGroup.setStatus("current")


class _SwAACEnableMethod4Type_Type(Integer32):
    """Custom type swAACEnableMethod4Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("local-enable", 7),
          ("none", 8),
          ("other", 9),
          ("radius", 4),
          ("server-group", 5),
          ("tacacs", 1),
          ("tacacs-plus", 3),
          ("xtacacs", 2))
    )


_SwAACEnableMethod4Type_Type.__name__ = "Integer32"
_SwAACEnableMethod4Type_Object = MibTableColumn
swAACEnableMethod4Type = _SwAACEnableMethod4Type_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 4, 1, 8),
    _SwAACEnableMethod4Type_Type()
)
swAACEnableMethod4Type.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAACEnableMethod4Type.setStatus("current")


class _SwAACEnableMethod4ServerGroup_Type(DisplayString):
    """Custom type swAACEnableMethod4ServerGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SwAACEnableMethod4ServerGroup_Type.__name__ = "DisplayString"
_SwAACEnableMethod4ServerGroup_Object = MibTableColumn
swAACEnableMethod4ServerGroup = _SwAACEnableMethod4ServerGroup_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 4, 1, 9),
    _SwAACEnableMethod4ServerGroup_Type()
)
swAACEnableMethod4ServerGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAACEnableMethod4ServerGroup.setStatus("current")
_SwAACEnableMethodListRowStatus_Type = RowStatus
_SwAACEnableMethodListRowStatus_Object = MibTableColumn
swAACEnableMethodListRowStatus = _SwAACEnableMethodListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 4, 1, 10),
    _SwAACEnableMethodListRowStatus_Type()
)
swAACEnableMethodListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAACEnableMethodListRowStatus.setStatus("current")
_SwAACAPAuthMethodGroup_ObjectIdentity = ObjectIdentity
swAACAPAuthMethodGroup = _SwAACAPAuthMethodGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 7)
)
_SwAACAPLoginMethod_ObjectIdentity = ObjectIdentity
swAACAPLoginMethod = _SwAACAPLoginMethod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 7, 1)
)


class _SwAACAPConsoleLoginMethod_Type(DisplayString):
    """Custom type swAACAPConsoleLoginMethod based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_SwAACAPConsoleLoginMethod_Type.__name__ = "DisplayString"
_SwAACAPConsoleLoginMethod_Object = MibScalar
swAACAPConsoleLoginMethod = _SwAACAPConsoleLoginMethod_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 7, 1, 1),
    _SwAACAPConsoleLoginMethod_Type()
)
swAACAPConsoleLoginMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAACAPConsoleLoginMethod.setStatus("current")


class _SwAACAPTelnetLoginMethod_Type(DisplayString):
    """Custom type swAACAPTelnetLoginMethod based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_SwAACAPTelnetLoginMethod_Type.__name__ = "DisplayString"
_SwAACAPTelnetLoginMethod_Object = MibScalar
swAACAPTelnetLoginMethod = _SwAACAPTelnetLoginMethod_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 7, 1, 2),
    _SwAACAPTelnetLoginMethod_Type()
)
swAACAPTelnetLoginMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAACAPTelnetLoginMethod.setStatus("current")


class _SwAACAPSSHLoginMethod_Type(DisplayString):
    """Custom type swAACAPSSHLoginMethod based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_SwAACAPSSHLoginMethod_Type.__name__ = "DisplayString"
_SwAACAPSSHLoginMethod_Object = MibScalar
swAACAPSSHLoginMethod = _SwAACAPSSHLoginMethod_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 7, 1, 3),
    _SwAACAPSSHLoginMethod_Type()
)
swAACAPSSHLoginMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAACAPSSHLoginMethod.setStatus("current")


class _SwAACAPHttpLoginMethod_Type(DisplayString):
    """Custom type swAACAPHttpLoginMethod based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_SwAACAPHttpLoginMethod_Type.__name__ = "DisplayString"
_SwAACAPHttpLoginMethod_Object = MibScalar
swAACAPHttpLoginMethod = _SwAACAPHttpLoginMethod_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 7, 1, 4),
    _SwAACAPHttpLoginMethod_Type()
)
swAACAPHttpLoginMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAACAPHttpLoginMethod.setStatus("current")
_SwAACAPEnableMethod_ObjectIdentity = ObjectIdentity
swAACAPEnableMethod = _SwAACAPEnableMethod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 7, 2)
)


class _SwAACAPConsoleEnableMethod_Type(DisplayString):
    """Custom type swAACAPConsoleEnableMethod based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_SwAACAPConsoleEnableMethod_Type.__name__ = "DisplayString"
_SwAACAPConsoleEnableMethod_Object = MibScalar
swAACAPConsoleEnableMethod = _SwAACAPConsoleEnableMethod_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 7, 2, 1),
    _SwAACAPConsoleEnableMethod_Type()
)
swAACAPConsoleEnableMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAACAPConsoleEnableMethod.setStatus("current")


class _SwAACAPTelnetEnableMethod_Type(DisplayString):
    """Custom type swAACAPTelnetEnableMethod based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_SwAACAPTelnetEnableMethod_Type.__name__ = "DisplayString"
_SwAACAPTelnetEnableMethod_Object = MibScalar
swAACAPTelnetEnableMethod = _SwAACAPTelnetEnableMethod_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 7, 2, 2),
    _SwAACAPTelnetEnableMethod_Type()
)
swAACAPTelnetEnableMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAACAPTelnetEnableMethod.setStatus("current")


class _SwAACAPSSHEnableMethod_Type(DisplayString):
    """Custom type swAACAPSSHEnableMethod based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_SwAACAPSSHEnableMethod_Type.__name__ = "DisplayString"
_SwAACAPSSHEnableMethod_Object = MibScalar
swAACAPSSHEnableMethod = _SwAACAPSSHEnableMethod_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 7, 2, 3),
    _SwAACAPSSHEnableMethod_Type()
)
swAACAPSSHEnableMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAACAPSSHEnableMethod.setStatus("current")


class _SwAACAPHttpEnableMethod_Type(DisplayString):
    """Custom type swAACAPHttpEnableMethod based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_SwAACAPHttpEnableMethod_Type.__name__ = "DisplayString"
_SwAACAPHttpEnableMethod_Object = MibScalar
swAACAPHttpEnableMethod = _SwAACAPHttpEnableMethod_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 7, 2, 4),
    _SwAACAPHttpEnableMethod_Type()
)
swAACAPHttpEnableMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAACAPHttpEnableMethod.setStatus("current")
_SwAACAuthParamGroup_ObjectIdentity = ObjectIdentity
swAACAuthParamGroup = _SwAACAuthParamGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 8)
)


class _SwAACAuthParamResponseTimeout_Type(Integer32):
    """Custom type swAACAuthParamResponseTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SwAACAuthParamResponseTimeout_Type.__name__ = "Integer32"
_SwAACAuthParamResponseTimeout_Object = MibScalar
swAACAuthParamResponseTimeout = _SwAACAuthParamResponseTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 8, 1),
    _SwAACAuthParamResponseTimeout_Type()
)
swAACAuthParamResponseTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAACAuthParamResponseTimeout.setStatus("current")


class _SwAACAuthParamAttempt_Type(Integer32):
    """Custom type swAACAuthParamAttempt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SwAACAuthParamAttempt_Type.__name__ = "Integer32"
_SwAACAuthParamAttempt_Object = MibScalar
swAACAuthParamAttempt = _SwAACAuthParamAttempt_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 8, 2),
    _SwAACAuthParamAttempt_Type()
)
swAACAuthParamAttempt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAACAuthParamAttempt.setStatus("current")
_SwAACServerGroupTable_Object = MibTable
swAACServerGroupTable = _SwAACServerGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 9)
)
if mibBuilder.loadTexts:
    swAACServerGroupTable.setStatus("current")
_SwAACServerGroupEntry_Object = MibTableRow
swAACServerGroupEntry = _SwAACServerGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 9, 1)
)
swAACServerGroupEntry.setIndexNames(
    (0, "AAC-MIB", "swAACServerGroupName"),
)
if mibBuilder.loadTexts:
    swAACServerGroupEntry.setStatus("current")


class _SwAACServerGroupName_Type(DisplayString):
    """Custom type swAACServerGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_SwAACServerGroupName_Type.__name__ = "DisplayString"
_SwAACServerGroupName_Object = MibTableColumn
swAACServerGroupName = _SwAACServerGroupName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 9, 1, 1),
    _SwAACServerGroupName_Type()
)
swAACServerGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAACServerGroupName.setStatus("current")
_SwAACServerGroupIPAddr1_Type = IpAddress
_SwAACServerGroupIPAddr1_Object = MibTableColumn
swAACServerGroupIPAddr1 = _SwAACServerGroupIPAddr1_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 9, 1, 2),
    _SwAACServerGroupIPAddr1_Type()
)
swAACServerGroupIPAddr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAACServerGroupIPAddr1.setStatus("current")


class _SwAACServerGroupAuthProtocol1_Type(Integer32):
    """Custom type swAACServerGroupAuthProtocol1 based on Integer32"""
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
        *(("none", 5),
          ("other", 6),
          ("radius", 4),
          ("tacacs", 1),
          ("tacacs-plus", 3),
          ("xtacacs", 2))
    )


_SwAACServerGroupAuthProtocol1_Type.__name__ = "Integer32"
_SwAACServerGroupAuthProtocol1_Object = MibTableColumn
swAACServerGroupAuthProtocol1 = _SwAACServerGroupAuthProtocol1_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 9, 1, 3),
    _SwAACServerGroupAuthProtocol1_Type()
)
swAACServerGroupAuthProtocol1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAACServerGroupAuthProtocol1.setStatus("current")
_SwAACServerGroupIPAddr2_Type = IpAddress
_SwAACServerGroupIPAddr2_Object = MibTableColumn
swAACServerGroupIPAddr2 = _SwAACServerGroupIPAddr2_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 9, 1, 4),
    _SwAACServerGroupIPAddr2_Type()
)
swAACServerGroupIPAddr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAACServerGroupIPAddr2.setStatus("current")


class _SwAACServerGroupAuthProtocol2_Type(Integer32):
    """Custom type swAACServerGroupAuthProtocol2 based on Integer32"""
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
        *(("none", 5),
          ("other", 6),
          ("radius", 4),
          ("tacacs", 1),
          ("tacacs-plus", 3),
          ("xtacacs", 2))
    )


_SwAACServerGroupAuthProtocol2_Type.__name__ = "Integer32"
_SwAACServerGroupAuthProtocol2_Object = MibTableColumn
swAACServerGroupAuthProtocol2 = _SwAACServerGroupAuthProtocol2_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 9, 1, 5),
    _SwAACServerGroupAuthProtocol2_Type()
)
swAACServerGroupAuthProtocol2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAACServerGroupAuthProtocol2.setStatus("current")
_SwAACServerGroupIPAddr3_Type = IpAddress
_SwAACServerGroupIPAddr3_Object = MibTableColumn
swAACServerGroupIPAddr3 = _SwAACServerGroupIPAddr3_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 9, 1, 6),
    _SwAACServerGroupIPAddr3_Type()
)
swAACServerGroupIPAddr3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAACServerGroupIPAddr3.setStatus("current")


class _SwAACServerGroupAuthProtocol3_Type(Integer32):
    """Custom type swAACServerGroupAuthProtocol3 based on Integer32"""
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
        *(("none", 5),
          ("other", 6),
          ("radius", 4),
          ("tacacs", 1),
          ("tacacs-plus", 3),
          ("xtacacs", 2))
    )


_SwAACServerGroupAuthProtocol3_Type.__name__ = "Integer32"
_SwAACServerGroupAuthProtocol3_Object = MibTableColumn
swAACServerGroupAuthProtocol3 = _SwAACServerGroupAuthProtocol3_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 9, 1, 7),
    _SwAACServerGroupAuthProtocol3_Type()
)
swAACServerGroupAuthProtocol3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAACServerGroupAuthProtocol3.setStatus("current")
_SwAACServerGroupIPAddr4_Type = IpAddress
_SwAACServerGroupIPAddr4_Object = MibTableColumn
swAACServerGroupIPAddr4 = _SwAACServerGroupIPAddr4_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 9, 1, 8),
    _SwAACServerGroupIPAddr4_Type()
)
swAACServerGroupIPAddr4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAACServerGroupIPAddr4.setStatus("current")


class _SwAACServerGroupAuthProtocol4_Type(Integer32):
    """Custom type swAACServerGroupAuthProtocol4 based on Integer32"""
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
        *(("none", 5),
          ("other", 6),
          ("radius", 4),
          ("tacacs", 1),
          ("tacacs-plus", 3),
          ("xtacacs", 2))
    )


_SwAACServerGroupAuthProtocol4_Type.__name__ = "Integer32"
_SwAACServerGroupAuthProtocol4_Object = MibTableColumn
swAACServerGroupAuthProtocol4 = _SwAACServerGroupAuthProtocol4_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 9, 1, 9),
    _SwAACServerGroupAuthProtocol4_Type()
)
swAACServerGroupAuthProtocol4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAACServerGroupAuthProtocol4.setStatus("current")
_SwAACServerGroupIPAddr5_Type = IpAddress
_SwAACServerGroupIPAddr5_Object = MibTableColumn
swAACServerGroupIPAddr5 = _SwAACServerGroupIPAddr5_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 9, 1, 10),
    _SwAACServerGroupIPAddr5_Type()
)
swAACServerGroupIPAddr5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAACServerGroupIPAddr5.setStatus("current")


class _SwAACServerGroupAuthProtocol5_Type(Integer32):
    """Custom type swAACServerGroupAuthProtocol5 based on Integer32"""
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
        *(("none", 5),
          ("other", 6),
          ("radius", 4),
          ("tacacs", 1),
          ("tacacs-plus", 3),
          ("xtacacs", 2))
    )


_SwAACServerGroupAuthProtocol5_Type.__name__ = "Integer32"
_SwAACServerGroupAuthProtocol5_Object = MibTableColumn
swAACServerGroupAuthProtocol5 = _SwAACServerGroupAuthProtocol5_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 9, 1, 11),
    _SwAACServerGroupAuthProtocol5_Type()
)
swAACServerGroupAuthProtocol5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAACServerGroupAuthProtocol5.setStatus("current")
_SwAACServerGroupIPAddr6_Type = IpAddress
_SwAACServerGroupIPAddr6_Object = MibTableColumn
swAACServerGroupIPAddr6 = _SwAACServerGroupIPAddr6_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 9, 1, 12),
    _SwAACServerGroupIPAddr6_Type()
)
swAACServerGroupIPAddr6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAACServerGroupIPAddr6.setStatus("current")


class _SwAACServerGroupAuthProtocol6_Type(Integer32):
    """Custom type swAACServerGroupAuthProtocol6 based on Integer32"""
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
        *(("none", 5),
          ("other", 6),
          ("radius", 4),
          ("tacacs", 1),
          ("tacacs-plus", 3),
          ("xtacacs", 2))
    )


_SwAACServerGroupAuthProtocol6_Type.__name__ = "Integer32"
_SwAACServerGroupAuthProtocol6_Object = MibTableColumn
swAACServerGroupAuthProtocol6 = _SwAACServerGroupAuthProtocol6_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 9, 1, 13),
    _SwAACServerGroupAuthProtocol6_Type()
)
swAACServerGroupAuthProtocol6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAACServerGroupAuthProtocol6.setStatus("current")
_SwAACServerGroupIPAddr7_Type = IpAddress
_SwAACServerGroupIPAddr7_Object = MibTableColumn
swAACServerGroupIPAddr7 = _SwAACServerGroupIPAddr7_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 9, 1, 14),
    _SwAACServerGroupIPAddr7_Type()
)
swAACServerGroupIPAddr7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAACServerGroupIPAddr7.setStatus("current")


class _SwAACServerGroupAuthProtocol7_Type(Integer32):
    """Custom type swAACServerGroupAuthProtocol7 based on Integer32"""
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
        *(("none", 5),
          ("other", 6),
          ("radius", 4),
          ("tacacs", 1),
          ("tacacs-plus", 3),
          ("xtacacs", 2))
    )


_SwAACServerGroupAuthProtocol7_Type.__name__ = "Integer32"
_SwAACServerGroupAuthProtocol7_Object = MibTableColumn
swAACServerGroupAuthProtocol7 = _SwAACServerGroupAuthProtocol7_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 9, 1, 15),
    _SwAACServerGroupAuthProtocol7_Type()
)
swAACServerGroupAuthProtocol7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAACServerGroupAuthProtocol7.setStatus("current")
_SwAACServerGroupIPAddr8_Type = IpAddress
_SwAACServerGroupIPAddr8_Object = MibTableColumn
swAACServerGroupIPAddr8 = _SwAACServerGroupIPAddr8_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 9, 1, 16),
    _SwAACServerGroupIPAddr8_Type()
)
swAACServerGroupIPAddr8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAACServerGroupIPAddr8.setStatus("current")


class _SwAACServerGroupAuthProtocol8_Type(Integer32):
    """Custom type swAACServerGroupAuthProtocol8 based on Integer32"""
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
        *(("none", 5),
          ("other", 6),
          ("radius", 4),
          ("tacacs", 1),
          ("tacacs-plus", 3),
          ("xtacacs", 2))
    )


_SwAACServerGroupAuthProtocol8_Type.__name__ = "Integer32"
_SwAACServerGroupAuthProtocol8_Object = MibTableColumn
swAACServerGroupAuthProtocol8 = _SwAACServerGroupAuthProtocol8_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 9, 1, 17),
    _SwAACServerGroupAuthProtocol8_Type()
)
swAACServerGroupAuthProtocol8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAACServerGroupAuthProtocol8.setStatus("current")
_SwAACServerGroupRowStatus_Type = RowStatus
_SwAACServerGroupRowStatus_Object = MibTableColumn
swAACServerGroupRowStatus = _SwAACServerGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 9, 1, 18),
    _SwAACServerGroupRowStatus_Type()
)
swAACServerGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAACServerGroupRowStatus.setStatus("current")
_SwAACServerInfoTable_Object = MibTable
swAACServerInfoTable = _SwAACServerInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 10)
)
if mibBuilder.loadTexts:
    swAACServerInfoTable.setStatus("current")
_SwAACServerInfoEntry_Object = MibTableRow
swAACServerInfoEntry = _SwAACServerInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 10, 1)
)
swAACServerInfoEntry.setIndexNames(
    (0, "AAC-MIB", "swAACServerIPAddr"),
    (0, "AAC-MIB", "swAACServerAuthProtocol"),
)
if mibBuilder.loadTexts:
    swAACServerInfoEntry.setStatus("current")
_SwAACServerIPAddr_Type = IpAddress
_SwAACServerIPAddr_Object = MibTableColumn
swAACServerIPAddr = _SwAACServerIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 10, 1, 1),
    _SwAACServerIPAddr_Type()
)
swAACServerIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAACServerIPAddr.setStatus("current")


class _SwAACServerAuthProtocol_Type(Integer32):
    """Custom type swAACServerAuthProtocol based on Integer32"""
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
        *(("radius", 4),
          ("tacacs", 1),
          ("tacacs-plus", 3),
          ("xtacacs", 2))
    )


_SwAACServerAuthProtocol_Type.__name__ = "Integer32"
_SwAACServerAuthProtocol_Object = MibTableColumn
swAACServerAuthProtocol = _SwAACServerAuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 10, 1, 2),
    _SwAACServerAuthProtocol_Type()
)
swAACServerAuthProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAACServerAuthProtocol.setStatus("current")


class _SwAACServerAuthPort_Type(Integer32):
    """Custom type swAACServerAuthPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwAACServerAuthPort_Type.__name__ = "Integer32"
_SwAACServerAuthPort_Object = MibTableColumn
swAACServerAuthPort = _SwAACServerAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 10, 1, 3),
    _SwAACServerAuthPort_Type()
)
swAACServerAuthPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAACServerAuthPort.setStatus("current")


class _SwAACServerAuthKey_Type(DisplayString):
    """Custom type swAACServerAuthKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_SwAACServerAuthKey_Type.__name__ = "DisplayString"
_SwAACServerAuthKey_Object = MibTableColumn
swAACServerAuthKey = _SwAACServerAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 10, 1, 4),
    _SwAACServerAuthKey_Type()
)
swAACServerAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAACServerAuthKey.setStatus("current")


class _SwAACServerTimeout_Type(Integer32):
    """Custom type swAACServerTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SwAACServerTimeout_Type.__name__ = "Integer32"
_SwAACServerTimeout_Object = MibTableColumn
swAACServerTimeout = _SwAACServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 10, 1, 5),
    _SwAACServerTimeout_Type()
)
swAACServerTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAACServerTimeout.setStatus("current")


class _SwAACServerRetryCount_Type(Integer32):
    """Custom type swAACServerRetryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SwAACServerRetryCount_Type.__name__ = "Integer32"
_SwAACServerRetryCount_Object = MibTableColumn
swAACServerRetryCount = _SwAACServerRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 10, 1, 6),
    _SwAACServerRetryCount_Type()
)
swAACServerRetryCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAACServerRetryCount.setStatus("current")
_SwAACServerRowStatus_Type = RowStatus
_SwAACServerRowStatus_Object = MibTableColumn
swAACServerRowStatus = _SwAACServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 10, 1, 7),
    _SwAACServerRowStatus_Type()
)
swAACServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAACServerRowStatus.setStatus("current")
_SwAACServerCtrlTable_Object = MibTable
swAACServerCtrlTable = _SwAACServerCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 12)
)
if mibBuilder.loadTexts:
    swAACServerCtrlTable.setStatus("current")
_SwAACServerCtrlEntry_Object = MibTableRow
swAACServerCtrlEntry = _SwAACServerCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 12, 1)
)
swAACServerCtrlEntry.setIndexNames(
    (0, "AAC-MIB", "swAACCtrlServerGroupName"),
    (0, "AAC-MIB", "swAACCtrlServerIPAddr"),
    (0, "AAC-MIB", "swAACCtrlServerAuthProtocol"),
)
if mibBuilder.loadTexts:
    swAACServerCtrlEntry.setStatus("current")


class _SwAACCtrlServerGroupName_Type(DisplayString):
    """Custom type swAACCtrlServerGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_SwAACCtrlServerGroupName_Type.__name__ = "DisplayString"
_SwAACCtrlServerGroupName_Object = MibTableColumn
swAACCtrlServerGroupName = _SwAACCtrlServerGroupName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 12, 1, 1),
    _SwAACCtrlServerGroupName_Type()
)
swAACCtrlServerGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swAACCtrlServerGroupName.setStatus("current")
_SwAACCtrlServerIPAddr_Type = IpAddress
_SwAACCtrlServerIPAddr_Object = MibTableColumn
swAACCtrlServerIPAddr = _SwAACCtrlServerIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 12, 1, 2),
    _SwAACCtrlServerIPAddr_Type()
)
swAACCtrlServerIPAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swAACCtrlServerIPAddr.setStatus("current")


class _SwAACCtrlServerAuthProtocol_Type(Integer32):
    """Custom type swAACCtrlServerAuthProtocol based on Integer32"""
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
        *(("radius", 4),
          ("tacacs", 1),
          ("tacacs-plus", 3),
          ("xtacacs", 2))
    )


_SwAACCtrlServerAuthProtocol_Type.__name__ = "Integer32"
_SwAACCtrlServerAuthProtocol_Object = MibTableColumn
swAACCtrlServerAuthProtocol = _SwAACCtrlServerAuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 12, 1, 3),
    _SwAACCtrlServerAuthProtocol_Type()
)
swAACCtrlServerAuthProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swAACCtrlServerAuthProtocol.setStatus("current")


class _SwAACCtrlServerRowState_Type(Integer32):
    """Custom type swAACCtrlServerRowState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("delete", 2))
    )


_SwAACCtrlServerRowState_Type.__name__ = "Integer32"
_SwAACCtrlServerRowState_Object = MibTableColumn
swAACCtrlServerRowState = _SwAACCtrlServerRowState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 5, 12, 1, 4),
    _SwAACCtrlServerRowState_Type()
)
swAACCtrlServerRowState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAACCtrlServerRowState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AAC-MIB",
    **{"swDlinkAACMIB": swDlinkAACMIB,
       "swAACCtrl": swAACCtrl,
       "swAACAuthenAdminState": swAACAuthenAdminState,
       "swAACInfo": swAACInfo,
       "swAACMaxLoginMethodList": swAACMaxLoginMethodList,
       "swAACMaxEnableMethodList": swAACMaxEnableMethodList,
       "swAACMaxServerGroup": swAACMaxServerGroup,
       "swAACMaxServer": swAACMaxServer,
       "swAACLoginMethodListTable": swAACLoginMethodListTable,
       "swAACLoginMethodListEntry": swAACLoginMethodListEntry,
       "swAACLoginMethodListName": swAACLoginMethodListName,
       "swAACLoginMethod1Type": swAACLoginMethod1Type,
       "swAACLoginMethod1ServerGroup": swAACLoginMethod1ServerGroup,
       "swAACLoginMethod2Type": swAACLoginMethod2Type,
       "swAACLoginMethod2ServerGroup": swAACLoginMethod2ServerGroup,
       "swAACLoginMethod3Type": swAACLoginMethod3Type,
       "swAACLoginMethod3ServerGroup": swAACLoginMethod3ServerGroup,
       "swAACLoginMethod4Type": swAACLoginMethod4Type,
       "swAACLoginMethod4ServerGroup": swAACLoginMethod4ServerGroup,
       "swAACLoginMethodListRowStatus": swAACLoginMethodListRowStatus,
       "swAACEnableMethodListTable": swAACEnableMethodListTable,
       "swAACEnableMethodListEntry": swAACEnableMethodListEntry,
       "swAACEnableMethodListName": swAACEnableMethodListName,
       "swAACEnableMethod1Type": swAACEnableMethod1Type,
       "swAACEnableMethod1ServerGroup": swAACEnableMethod1ServerGroup,
       "swAACEnableMethod2Type": swAACEnableMethod2Type,
       "swAACEnableMethod2ServerGroup": swAACEnableMethod2ServerGroup,
       "swAACEnableMethod3Type": swAACEnableMethod3Type,
       "swAACEnableMethod3ServerGroup": swAACEnableMethod3ServerGroup,
       "swAACEnableMethod4Type": swAACEnableMethod4Type,
       "swAACEnableMethod4ServerGroup": swAACEnableMethod4ServerGroup,
       "swAACEnableMethodListRowStatus": swAACEnableMethodListRowStatus,
       "swAACAPAuthMethodGroup": swAACAPAuthMethodGroup,
       "swAACAPLoginMethod": swAACAPLoginMethod,
       "swAACAPConsoleLoginMethod": swAACAPConsoleLoginMethod,
       "swAACAPTelnetLoginMethod": swAACAPTelnetLoginMethod,
       "swAACAPSSHLoginMethod": swAACAPSSHLoginMethod,
       "swAACAPHttpLoginMethod": swAACAPHttpLoginMethod,
       "swAACAPEnableMethod": swAACAPEnableMethod,
       "swAACAPConsoleEnableMethod": swAACAPConsoleEnableMethod,
       "swAACAPTelnetEnableMethod": swAACAPTelnetEnableMethod,
       "swAACAPSSHEnableMethod": swAACAPSSHEnableMethod,
       "swAACAPHttpEnableMethod": swAACAPHttpEnableMethod,
       "swAACAuthParamGroup": swAACAuthParamGroup,
       "swAACAuthParamResponseTimeout": swAACAuthParamResponseTimeout,
       "swAACAuthParamAttempt": swAACAuthParamAttempt,
       "swAACServerGroupTable": swAACServerGroupTable,
       "swAACServerGroupEntry": swAACServerGroupEntry,
       "swAACServerGroupName": swAACServerGroupName,
       "swAACServerGroupIPAddr1": swAACServerGroupIPAddr1,
       "swAACServerGroupAuthProtocol1": swAACServerGroupAuthProtocol1,
       "swAACServerGroupIPAddr2": swAACServerGroupIPAddr2,
       "swAACServerGroupAuthProtocol2": swAACServerGroupAuthProtocol2,
       "swAACServerGroupIPAddr3": swAACServerGroupIPAddr3,
       "swAACServerGroupAuthProtocol3": swAACServerGroupAuthProtocol3,
       "swAACServerGroupIPAddr4": swAACServerGroupIPAddr4,
       "swAACServerGroupAuthProtocol4": swAACServerGroupAuthProtocol4,
       "swAACServerGroupIPAddr5": swAACServerGroupIPAddr5,
       "swAACServerGroupAuthProtocol5": swAACServerGroupAuthProtocol5,
       "swAACServerGroupIPAddr6": swAACServerGroupIPAddr6,
       "swAACServerGroupAuthProtocol6": swAACServerGroupAuthProtocol6,
       "swAACServerGroupIPAddr7": swAACServerGroupIPAddr7,
       "swAACServerGroupAuthProtocol7": swAACServerGroupAuthProtocol7,
       "swAACServerGroupIPAddr8": swAACServerGroupIPAddr8,
       "swAACServerGroupAuthProtocol8": swAACServerGroupAuthProtocol8,
       "swAACServerGroupRowStatus": swAACServerGroupRowStatus,
       "swAACServerInfoTable": swAACServerInfoTable,
       "swAACServerInfoEntry": swAACServerInfoEntry,
       "swAACServerIPAddr": swAACServerIPAddr,
       "swAACServerAuthProtocol": swAACServerAuthProtocol,
       "swAACServerAuthPort": swAACServerAuthPort,
       "swAACServerAuthKey": swAACServerAuthKey,
       "swAACServerTimeout": swAACServerTimeout,
       "swAACServerRetryCount": swAACServerRetryCount,
       "swAACServerRowStatus": swAACServerRowStatus,
       "swAACServerCtrlTable": swAACServerCtrlTable,
       "swAACServerCtrlEntry": swAACServerCtrlEntry,
       "swAACCtrlServerGroupName": swAACCtrlServerGroupName,
       "swAACCtrlServerIPAddr": swAACCtrlServerIPAddr,
       "swAACCtrlServerAuthProtocol": swAACCtrlServerAuthProtocol,
       "swAACCtrlServerRowState": swAACCtrlServerRowState}
)
